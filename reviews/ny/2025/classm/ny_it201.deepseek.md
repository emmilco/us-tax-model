# Class M hand-work — ny_it201

`Form IT-201 (2025), Resident Income Tax Return — New York State and New York City` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-05 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 4adc1882e5f996313b8a7e29c80691048d6727c7e70f243a4c08637b437d6958 |
| cases | 7 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: All others:; Calculation of NYC school tax credit (rate reduction amount) for head of household ④; Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤; Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③; Joint returns; Line 40: New York State household credit; New York City household credit table 4—Filing status ① only (Single); New York City household credit table 5—Filing status ②, ④, and ⑤; New York State household credit table 1—Filing status ① only (Single); New York State household credit table 2—Filing status ②, ④, and ⑤; New York State standard deduction table; Table 1 - Full-year New York City residents: New York City school tax credit table; Tax computation worksheet 1; Tax computation worksheet 10; Tax computation worksheet 12; Tax computation worksheet 13; Tax computation worksheet 14; Tax computation worksheet 15; Tax computation worksheet 2; Tax computation worksheet 3; Tax computation worksheet 4; Tax computation worksheet 5; Tax computation worksheet 6; Tax computation worksheet 7; Tax computation worksheet 8; Tax computation worksheet 9; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it270i | Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit, for tax year 2025 (no printed edition line; address /pdf/2025/inc/, PDF metadata Title '... Tax Year 2025'); PDF modified 2025-10-27 | 1 | whole document | 66b713fa6ae58aafa2189310ed7d140b64c05d2c8bf2958a9651af7751ae15d5 | - | cc437e692bd1fcdbcc44f0e850e95f1cacee9a0e3285396d87e580ca559e082c |

## Lines

### case classm.ny_it201.1 — prompt sha256 36d6621e89c771b86dbba41a2023f42b0cf7cbe92982b04300331e16eaf6e518; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:true, ny_it201.ask.use_tax_st141:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.abode_part_year:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#0, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#0, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#0, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#1, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.1 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.1 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.1 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.1 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: No out-of-state bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: No 414(h) contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: No nonqualified NY 529 withdrawal

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: No other additions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **SKIPPED**

Model: blank
Work: No inflation refund included

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: No government pension subtraction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **SKIPPED**

Model: blank
Work: No Social Security subtraction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: No U.S. government bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: No pension/annuity exclusion

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: No NY 529 deduction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: No other subtractions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $8,000.00

### classm.ny_it201.1 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **AGREE**

Value: $3,100.00

### classm.ny_it201.1 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $8,000.00

### classm.ny_it201.1 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $32,000.00

### classm.ny_it201.1 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $32,000.00

### classm.ny_it201.1 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $32,000.00

### classm.ny_it201.1 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: 2025 NYS Tax Table for 32000

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: Tax Table used because taxable income below 65000

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: TCW not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not filing jointly

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: TCW not required

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not head of household

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: No TCW required

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: NY AGI not over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: From 2025 NYS Tax Table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.1 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: Table 2 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: Table 5 not used for single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: FAGI 40000 exceeds table 1 limit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: FAGI 40000 exceeds table 4 limit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: No state household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (48) — The city household credit table for the filing status
Status: **MISSING**

Project: $0.00
Model: no answer

Ruling: model error (omission); the reply gives no value for this line, so it carries no evidence. The project's $0 is the source's: IT-201-I (web edition), New York City household credit table 4 (single), "12,500 | No credit is allowed; do not make an entry on Form IT-201, line 48", federal adjusted gross income being $40,000. Dropped from the fixture (no assertion). [dropped]

### classm.ny_it201.1 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: No credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: No resident credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: No other nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: 1596 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 - 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,597.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: No other NYS taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: 1596 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 + 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,597.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 47 — NYC taxable income
Status: **AGREE**

Value: $32,000.00

### classm.ny_it201.1 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: NYC tax table for 32000

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,126. The amount is $32,000 (agreed on both sides). The model gave $1,125.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: From NYC resident tax table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,126. The amount is $32,000 (agreed on both sides). The model gave $1,125.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: No NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 - 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: Full-year NYC resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: No other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: No NYC nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 - 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: MCTMT skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: MCTMT skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: MCTMT skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: MCTMT skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: MCTMT skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: Not a Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: No Yonkers work income

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: No part-year Yonkers residency

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 + 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **AGREE**

Value: $7.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **AGREE**

Value: $7.00

### classm.ny_it201.1 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $10.00

### classm.ny_it201.1 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $10.00

### classm.ny_it201.1 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: No voluntary contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $2,733.00
Model: $2,731.00
Work: 1596 + 1125 + 10 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 + 1125 + 10 + 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,733.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $2,733.00
Model: $2,731.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,733.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: No qualifying child

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: No federal child/dependent care credit eligibility

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: No NYS EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: No child support paid

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: No real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: No college tuition expenses

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $63.00

### classm.ny_it201.1 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $63.00

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **DISAGREE**

Project: $55.00
Model: $54.72
Work: 0.171% x 32000

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.171% of taxable income" on New York City taxable income of $32,000 (a helper of the row this return does not take, line 47 being over $12,000): exactly $54.72, which the project rounds half-up to $55.00; the model's $54.72 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $46.00
Model: $45.60
Work: 0.228% x 20000

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.228% of the excess over $12,000" on New York City taxable income of $32,000: exactly $45.60, which the project rounds half-up to $46.00; the model's $45.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $21.00

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $67.00
Model: $66.60
Work: 21 + 45.60

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "$21 plus 0.228% of the excess over $12,000" on $32,000 (the 0.228% product rounded where it is computed): exactly $66.60, which the project rounds half-up to $67.00; the model's $66.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $67.00
Model: $66.60
Work: Rate reduction amount

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", the row over $12,000 but not over $500,000, "$21 plus 0.228% of the excess over $12,000", on $32,000: exactly $66.60, which the project rounds half-up to $67.00; the model's $66.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $67.00

### classm.ny_it201.1 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: No NYC EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: No dependents; elimination credit not allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: No other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $130.00

### classm.ny_it201.1 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $2,603.00
Model: $2,601.00
Work: 2731 - 130

Ruling: model error, carried: the model's own arithmetic on this line ("2731 - 130") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,603.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.1 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: No other penalties or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: Line 76 not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: No refund

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: No NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: No refund after 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 80 — Amount you owe
Status: **DISAGREE**

Project: $2,603.00
Model: $2,601.00
Work: 2731 - 130 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2731 - 130 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,603.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### case classm.ny_it201.2 — prompt sha256 81dc24314d6e1b0132aa406d16b869cdbd82bd03580717d2e66ac032f9c3dac6; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:false, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#1, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#6, ny_it201.hh_city_t5#6, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#5, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:floor, ny_it201.stc_rr_low_band:true, ny_it201.stc_rr#0, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.2 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.2 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 75

### classm.ny_it201.2 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.2 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: no state/local bond interest addition

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: no 414(h) contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: no NY 529 nonqualified withdrawal

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: no other IT-225 additions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: no NY/federal government pension subtraction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: no U.S. government bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: no pension annuity exclusion

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: no NY 529 deduction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: no other IT-225 subtractions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.2 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **SKIPPED**

Model: blank
Work: not single with item C yes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.2 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $91,638.00

### classm.ny_it201.2 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $75,000.00

### classm.ny_it201.2 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $16,638.00

### classm.ny_it201.2 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $16,638.00

### classm.ny_it201.2 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **SKIPPED**

Model: blank
Work: not used; NY AGI over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **SKIPPED**

Model: blank
Work: not used; NY AGI over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: not over 25M

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not single/MFS

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not HOH

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — 39 — NYS tax on line 38 amount
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 77

### classm.ny_it201.2 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: AGI over 32000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: AGI over 22500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: no credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: no credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: single table not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: single table not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: no credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (48) — The city household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: no credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: no NYS household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: no resident credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: no other nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: no other NYS taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — 47 — NYC taxable income
Status: **AGREE**

Value: $16,638.00

### classm.ny_it201.2 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 47a — NYC resident tax on line 47 amount
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: no NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: full-year NYC resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: no other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 52 — Add lines 49, 50, and 51
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: no NYC nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: skip MCTMT; no earnings over 50000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: skip MCTMT; no earnings over 50000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: skip MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: skip MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: skip MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: no Yonkers resident surcharge

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: no Yonkers nonresident earnings tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: no part-year Yonkers surcharge

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.cap) — $125
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **SKIPPED**

Model: blank
Work: sales chart not used; no use tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: no voluntary contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **AGREE**

Value: $1,178.00

### classm.ny_it201.2 — 62 — Enter amount from line 61
Status: **AGREE**

Value: $1,178.00

### classm.ny_it201.2 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: no qualifying child under 17

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: no federal child/dependent care credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: no NYS EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: no child support through SCU

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: no real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: no college tuition expenses

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $125.00

### classm.ny_it201.2 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $125.00

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **DISAGREE**

Project: $28.00
Model: $28.45
Work: 16638 x 0.00171

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.171% of taxable income" on New York City taxable income of $16,638: exactly $28.45098, which the project rounds half-up to $28.00; the model's $28.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **SKIPPED**

Model: blank
Work: not over 21600

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: not over 21600

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **SKIPPED**

Model: blank
Work: low bracket

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: low bracket

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **AGREE**

Value: $28.00

### classm.ny_it201.2 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $28.00

### classm.ny_it201.2 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: no NYC EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: FAGI exceeds elimination credit threshold by more than 5000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: no other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $153.00

### classm.ny_it201.2 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **AGREE**

Value: $1,025.00

### classm.ny_it201.2 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **SKIPPED**

Model: blank
Work: no estimated tax penalty

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: no other penalties or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: line 76 is not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: no NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: no refund

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 80 — Amount you owe
Status: **AGREE**

Value: $1,025.00

### case classm.ny_it201.3 — prompt sha256 3f00bc96adab7c8a6f8a88fdd282fc7879ef3e851fb6d52bc384f4b8a8cc754b; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:true, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:true, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:true, ny_it201.line34#0, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#0, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#0, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#0, ny_it201.line40#0, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#0, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:false, ny_it201.line69#1, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#0, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.3 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: yes

### classm.ny_it201.3 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.3 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.3 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: No other-state bond interest; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: No 414(h) contributions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: No NY 529 nonqualified withdrawal; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: No other additions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: No government pension; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: No U.S. government bond interest; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: No pension/annuity exclusion; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: No NY 529 deduction; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: No other subtractions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $8,000.00

### classm.ny_it201.3 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **AGREE**

Value: $3,100.00

### classm.ny_it201.3 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $3,100.00

### classm.ny_it201.3 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $36,900.00

### classm.ny_it201.3 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $36,900.00

### classm.ny_it201.3 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $36,900.00

### classm.ny_it201.3 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: 2025 NYS Tax Table on 36900

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: AGI <= 107650 and taxable income < 65000; tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: High-income worksheet not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Married worksheet not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: High-income single worksheet not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Head of household worksheet not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Tax computation worksheet not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: AGI not more than 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: NYS tax from tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.3 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: Table 2 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: Table 5 not applicable; Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: AGI over 28000; no table 1 credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: AGI over 12500; no table 4 credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (48) — The city household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: No resident credit; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: No other nonrefundable credits; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: 1865 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 - 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,866.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: No other NYS taxes; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: 1865 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 + 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,866.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 47 — NYC taxable income
Status: **AGREE**

Value: $36,900.00

### classm.ny_it201.3 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 2025 NYC Tax Table on 36900

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,313. The amount is $36,900 (agreed on both sides). The model gave $1,312.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: NYC resident tax on line 47

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,313. The amount is $36,900 (agreed on both sides). The model gave $1,312.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 - 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: Full-year NYC resident; no part-year tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: No other NYC taxes; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: No NYC nonrefundable credits; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 - 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: No MCTMT Zone 1 net earnings; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: No MCTMT Zone 2 net earnings; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: No Zone 1 MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: No Zone 2 MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: No total MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: Not a Yonkers resident; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: No Yonkers nonresident earnings tax; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: No part-year Yonkers surcharge; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 + 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.cap) — $125
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **SKIPPED**

Model: blank
Work: No sales/use tax owed; chart not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: No voluntary contributions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: 1865 + 1312 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 + 1312 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: No qualifying child; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: No federal child/dependent care credit qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: No federal EIC qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: No noncustodial parent EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: No real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: No college tuition credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **SKIPPED**

Model: blank
Work: Item C Yes; NYC school tax credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **SKIPPED**

Model: blank
Work: Item C Yes; NYC school tax credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 69 — NYC school tax credit (fixed amount)
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no fixed NYC school tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **SKIPPED**

Model: blank
Work: Item C Yes; rate reduction credit disqualified

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 69a — NYC school tax credit (rate reduction amount)
Status: **SKIPPED**

Model: blank
Work: Item C Yes; no NYC rate reduction credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: No federal EIC qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: No dependents claimed; NYC elimination credit not allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: No other refundable credits; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 74 — Total Yonkers tax withheld
Status: **SKIPPED**

Model: blank
Work: No Yonkers withholding

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: Line 62 3177 - line 76 0

Ruling: model error, carried: the model's own arithmetic on this line ("Line 62 3177 - line 76 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **SKIPPED**

Model: blank
Work: No estimated tax penalty

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: No late filing/payment penalty or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: Line 76 not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: No line 77 overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: No NYS 529 refund deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: No refund after NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 80 — Amount you owe
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: Line 62 3177 - line 76 0; no penalties

Ruling: model error, carried: the model's own arithmetic on this line ("Line 62 3177 - line 76 0; no penalties") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### case classm.ny_it201.4 — prompt sha256 a498e493efee6999410f5d48edfd34ecd6f5ee71a727d2aa929f1143ce8af031; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#4, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:true, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#2, ny_it201.hh_city_in_range:true, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#2, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#1, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:floor, ny_it201.stc_rr_low_band:true, ny_it201.stc_rr#0, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.4 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.4 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.4 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.4 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: skip: no out-of-state bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: skip: no 414(h) contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: skip: no NY 529 nonqualified withdrawal

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: skip: no other NY additions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: skip: no government pension

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: skip: no U.S. government interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: skip: no pension exclusion

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: skip: no NY 529 deduction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: skip: no other NY subtractions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $11,200.00

### classm.ny_it201.4 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **SKIPPED**

Model: blank
Work: not applicable: not single and item C No

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $11,200.00

### classm.ny_it201.4 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $8,800.00

### classm.ny_it201.4 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $8,800.00

### classm.ny_it201.4 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $8,800.00

### classm.ny_it201.4 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project: $353.00
Model: $352.00
Work: tax table for 8800 HOH

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $353.00
Model: $352.00
Work: AGI <= 107650 and taxable < 65000

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable: AGI not over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: not applicable: AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $353.00
Model: $352.00
Work: NYS tax from tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.4 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $75.00

### classm.ny_it201.4 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $30.00

### classm.ny_it201.4 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $90.00

### classm.ny_it201.4 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $45.00

### classm.ny_it201.4 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $105.00

### classm.ny_it201.4 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $120.00

### classm.ny_it201.4 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $75.00

### classm.ny_it201.4 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $135.00

### classm.ny_it201.4 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $90.00

### classm.ny_it201.4 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $150.00

### classm.ny_it201.4 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $105.00

### classm.ny_it201.4 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: not applicable: not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: not applicable: not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 40 — NYS household credit
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: skip: no resident credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: skip: no other nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $293.00
Model: $292.00
Work: 352 - 60

Ruling: model error, carried: the model's own arithmetic on this line ("352 - 60") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project), each ruled model error in this case; with the table amounts the line is the project's $293.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: skip: no other NYS taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $293.00
Model: $292.00
Work: 292 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("292 + 0") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project), each ruled model error in this case; with the table amounts the line is the project's $293.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 47 — NYC taxable income
Status: **AGREE**

Value: $8,800.00

### classm.ny_it201.4 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $272.00
Model: $271.00
Work: NYC tax table for 8800 HOH

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $272. The amount is $8,800 (agreed on both sides). The model gave $271.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $272.00
Model: $271.00
Work: NYC resident tax

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $272. The amount is $8,800 (agreed on both sides). The model gave $271.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 48 — NYC household credit
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 271 - 15

Ruling: model error, carried: the model's own arithmetic on this line ("271 - 15") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: skip: full-year NYC resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: skip: no other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("256 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: skip: no NYC nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("256 - 0") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: skip: no MCTMT Zone 1 earnings

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: skip: no MCTMT Zone 2 earnings

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: skip: no MCTMT Zone 1

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: skip: no MCTMT Zone 2

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: skip: no MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: skip: not a Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: skip: no Yonkers wages

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: skip: not part-year Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 + 0 MCTMT/Yonkers

Ruling: model error, carried: the model's own arithmetic on this line ("256 + 0 MCTMT/Yonkers") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project: $4.00
Model: $3.50
Work: 20000 × 0.000175 = 3.50

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $20,000 (the row this return does not take; its chart amount is another row's): exactly $3.50, which the project rounds half-up to $4.00; the model's $3.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $4.00
Model: $3.50
Work: smaller of 3.50 and 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $20,000 (the row this return does not take; its chart amount is another row's): exactly $3.50, which the project rounds half-up to $4.00; the model's $3.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $6.00

### classm.ny_it201.4 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: skip: no voluntary contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $550.00
Model: $548.00
Work: 292 + 256 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("292 + 256 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $550.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $550.00
Model: $548.00
Work: from line 61

Ruling: model error, carried: the model's own arithmetic on this line ("from line 61") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $550.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: skip: no qualifying child

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: skip: no federal child/dependent care credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: skip: no federal EIC claim

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: skip: no child support payments

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: skip: no real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: skip: no college tuition expenses

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $63.00

### classm.ny_it201.4 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $63.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **DISAGREE**

Project: $15.00
Model: $15.05
Work: 8800 × 0.00171 = 15.048

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for head of household ④", "0.171% of taxable income" on New York City taxable income of $8,800: exactly $15.048, which the project rounds half-up to $15.00; the model's $15.05 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $25.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **AGREE**

Value: $25.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $15.00
Model: $15.05
Work: use low bracket: 0.171% of taxable income

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for head of household ④", the row over $0 but not over $14,400, "0.171% of taxable income", on $8,800: exactly $15.048, which the project rounds half-up to $15.00; the model's $15.05 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: skip: no federal EIC claim

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: not eligible: no dependents claimed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: skip: no other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $78.00

### classm.ny_it201.4 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $472.00
Model: $470.00
Work: 548 - 78

Ruling: model error, carried: the model's own arithmetic on this line ("548 - 78") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $472.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.4 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: not applicable: line 76 not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: no NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: no refund after NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 80 — Amount you owe
Status: **DISAGREE**

Project: $472.00
Model: $470.00
Work: 548 - 78 = 470 amount owed

Ruling: model error, carried: the model's own arithmetic on this line ("548 - 78 = 470 amount owed") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $472.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### case classm.ny_it201.5 — prompt sha256 b2190d8337b86be2475302b7c6a2ef27df2cec148cdaa62574435c8dd5fc730d; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#1, ny_it201.hh_city_t5#1, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#3, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.5 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.5 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.5 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.5 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: no other-state bond interest; skip to line 21

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: no 414(h) contributions; skip to line 22

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: no NY 529 nonqualified withdrawal; skip to line 23

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: no NYS/local/federal government pension; skip to line 27

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: no U.S. government bond interest; skip to line 29

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: no qualifying pension/annuity income; skip to line 30

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: no NY 529 contributions/withdrawals; skip to line 31

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.5 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **SKIPPED**

Model: blank
Work: not applicable; MFJ and item C No

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.5 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $38,275.00

### classm.ny_it201.5 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $38,275.00

### classm.ny_it201.5 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $38,275.00

### classm.ny_it201.5 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: not applicable; NY AGI <= $107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: not applicable; NY AGI <= $107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable; filing status is MFJ

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable; filing status is MFJ

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: not applicable; NY AGI <= $107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: not applicable; NY AGI <= $107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 39 — NYS tax on line 38 amount
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 2

### classm.ny_it201.5 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 1) — New York State household credit table 1 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: no NYS household credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: no resident credit; skip to line 42

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: no other NYS nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: no net other NYS taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — 47 — NYC taxable income
Status: **AGREE**

Value: $38,275.00

### classm.ny_it201.5 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 47a — NYC resident tax on line 47 amount
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: no NYC household credit allowed

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: full-year NYC resident; no part-year tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: no other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 52 — Add lines 49, 50, and 51
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: no NYC nonrefundable credits; skip to line 54

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: no MCTMT Zone 1 net earnings over $50,000; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: no MCTMT Zone 2 net earnings over $50,000; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: skip MCTMT Zone 1

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: skip MCTMT Zone 2

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: skip total MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: not a Yonkers resident; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: no Yonkers nonresident earnings; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: not a part-year Yonkers resident; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project: $10.00
Model: $9.51
Work: 54,325 x 0.000175 = 9.506875

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $54,325 (the row this return does not take; its chart amount is another row's): exactly $9.50688, which the project rounds half-up to $10.00; the model's $9.51 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $10.00
Model: $9.51
Work: smaller of 9.506875 or 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $54,325 (the row this return does not take; its chart amount is another row's): exactly $9.50688, which the project rounds half-up to $10.00; the model's $9.51 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $15.00

### classm.ny_it201.5 — 59 — Sales or use tax (do not leave blank)
Status: **DISAGREE**

Project: $0.00
Model: $15.00
Work: sales/use tax chart amount for FAGI 54,325

Ruling: model error; the case answers No to "Do you owe New York sales or use tax on purchases made without paying New York tax ...?" (ny_it201.ask.owes_use_tax), so line 59 is $0 (owner decision B3, docs/ny/DECISIONS.md: "No enters 0; Yes uses the chart from federal AGI"); IT-201-I (web edition), Line 59: "Report your sales or use tax liability on this line." With no use tax owed the liability is zero. The model entered the chart amount ($15) regardless of the answer. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: no voluntary contributions; skip to line 61

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $3,065.00
Model: $3,080.00
Work: 46 + 58 + 59 + 60 = 1,773 + 1,292 + 15

Ruling: model error, carried: the model's own arithmetic on this line ("46 + 58 + 59 + 60 = 1,773 + 1,292 + 15") is the form's, but it starts from its table errors on line 59 ($15.00 model, $0.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,065.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $3,065.00
Model: $3,080.00
Work: from line 61

Ruling: model error, carried: the model's own arithmetic on this line ("from line 61") is the form's, but it starts from its table errors on line 59 ($15.00 model, $0.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,065.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: no qualifying child; no Empire State child credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: no federal child/dependent care credit qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: no federal EIC for 2025; no NYS EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: no child support through NYS Support Collection Unit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: no real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: no college tuition expenses

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $54,325.00

### classm.ny_it201.5 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $125.00

### classm.ny_it201.5 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $125.00

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **SKIPPED**

Model: blank
Work: not used; city taxable income exceeds $21,600

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $16,675.00

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $38.00
Model: $38.02
Work: 16,675 x 0.00228 = 38.019

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.228% of the excess over $21,600" on New York City taxable income of $38,275: exactly $38.019, which the project rounds half-up to $38.00; the model's $38.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $37.00

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $75.00
Model: $75.02
Work: 37 + 38.019 = 75.019

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "$37 plus 0.228% of the excess over $21,600" on $38,275 (the 0.228% product rounded where it is computed): exactly $75.019, which the project rounds half-up to $75.00; the model's $75.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **AGREE**

Value: $75.00

### classm.ny_it201.5 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $75.00

### classm.ny_it201.5 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: no federal EIC; no NYC EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: no dependents; not eligible for NYC income tax elimination credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: no other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $200.00

### classm.ny_it201.5 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $2,865.00
Model: $2,880.00
Work: 62 - 76 = 3,080 - 200

Ruling: model error, carried: the model's own arithmetic on this line ("62 - 76 = 3,080 - 200") is the form's, but it starts from its table errors on line 59 ($15.00 model, $0.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,865.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.5 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **SKIPPED**

Model: blank
Work: prepayments 0 >= safe harbor 0; no penalty

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: no late filing/payment penalty or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: 76 < 62; no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: no line 77 overpayment available for refund

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: no NYS 529 account deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: no refund after NYS 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.5 — 80 — Amount you owe
Status: **DISAGREE**

Project: $2,865.00
Model: $2,880.00
Work: amount owed = 3,080 - 200

Ruling: model error, carried: the model's own arithmetic on this line ("amount owed = 3,080 - 200") is the form's, but it starts from its table errors on line 59 ($15.00 model, $0.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,865.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### case classm.ny_it201.6 — prompt sha256 0dbca0d3bc2a1d74130f28559883c57942d0b69df42f0c0d7a9e77654ffbc38d; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#3, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#4, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#4, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.6 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.6 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.6 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **SKIPPED**

Model: blank
Work: no federal Form 4797 amount

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **SKIPPED**

Model: blank
Work: no Schedule E amount

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 12 — Rental real estate included in line 11
Status: **SKIPPED**

Model: blank
Work: no rental real estate in line 11

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 13 — Farm income or loss
Status: **SKIPPED**

Model: blank
Work: no Schedule F amount

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.6 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: no state/local bond interest; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: no 414(h) contributions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: no nonqualified 529 withdrawal; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: no other additions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: no government pension; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: no U.S. government bond interest; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: no pension/annuity exclusion; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: no 529 contributions/withdrawals; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: no other subtractions; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $8,000.00

### classm.ny_it201.6 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **SKIPPED**

Model: blank
Work: not single with item C Yes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $8,000.00

### classm.ny_it201.6 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.6 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.6 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.6 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: tax table for taxable 40,000

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: AGI <= 107,650; taxable < 65,000 so tax table = 2,036

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: not applicable: AGI not over 25,000,000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: not applicable: filing status not MFJ/QSS

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable: AGI <= 107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable: not head of household

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: not applicable: no tax computation worksheet

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: not applicable: AGI <= 107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: from tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.6 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: AGI 48,000 over table limit; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: single table; AGI over 28,000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: single NYC table; AGI over 12,500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: MFS table 3; AGI over 32,000; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (48) — The city household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: MFS table 6; AGI over 22,500; no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: no household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: no out-of-state tax; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: no other nonrefundable credits; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: 2,036 - 0 = 2,036

Ruling: model error, carried: the model's own arithmetic on this line ("2,036 - 0 = 2,036") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,037.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: no other NYS taxes; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: 2,036 + 0 = 2,036

Ruling: model error, carried: the model's own arithmetic on this line ("2,036 + 0 = 2,036") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,037.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 47 — NYC taxable income
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.6 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: given NYC resident tax

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $1,432. The amount is $40,000 (agreed on both sides). The model gave $1,431.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: NYC resident tax on line 47

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $1,432. The amount is $40,000 (agreed on both sides). The model gave $1,431.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: no NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 - 0 = 1,431

Ruling: model error, carried: the model's own arithmetic on this line ("1,431 - 0 = 1,431") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: full-year NYC resident; not part-year

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: no other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 + 0 + 0 = 1,431

Ruling: model error, carried: the model's own arithmetic on this line ("1,431 + 0 + 0 = 1,431") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: no NYC nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 - 0 = 1,431

Ruling: model error, carried: the model's own arithmetic on this line ("1,431 - 0 = 1,431") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: no MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: no MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: no MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: no MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: no MCTMT; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: not a Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: no Yonkers nonresident earnings

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: not part-year Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 + 0 = 1,431

Ruling: model error, carried: the model's own arithmetic on this line ("1,431 + 0 = 1,431") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project: $8.00
Model: $8.40
Work: 0.000175 * 48,000 = 8.40

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $48,000 (the row this return does not take; its chart amount is another row's): exactly $8.40, which the project rounds half-up to $8.00; the model's $8.40 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $8.00
Model: $8.40
Work: smaller of 8.40 and 125 = 8.40

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $48,000 (the row this return does not take; its chart amount is another row's): exactly $8.40, which the project rounds half-up to $8.00; the model's $8.40 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $10.00

### classm.ny_it201.6 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: no voluntary contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $3,469.00
Model: $3,467.00
Work: 2,036 + 1,431 + 0 + 0 = 3,467

Ruling: model error, carried: the model's own arithmetic on this line ("2,036 + 1,431 + 0 + 0 = 3,467") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,469.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $3,469.00
Model: $3,467.00
Work: from line 61

Ruling: model error, carried: the model's own arithmetic on this line ("from line 61") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,469.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: no qualifying child

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: no federal child/dependent care credit qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: no federal EIC eligibility

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: no child support payments through Support Collection Unit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: no real property tax credit qualification

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: no college tuition expenses

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $63.00

### classm.ny_it201.6 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $63.00

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **SKIPPED**

Model: blank
Work: not applicable; taxable income over 12,000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $28,000.00

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $64.00
Model: $63.84
Work: 0.00228 * 28,000 = 63.84

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.228% of the excess over $12,000" on New York City taxable income of $40,000: exactly $63.84, which the project rounds half-up to $64.00; the model's $63.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $21.00

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $85.00
Model: $84.84
Work: 21 + 63.84 = 84.84

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "$21 plus 0.228% of the excess over $12,000" on $40,000 (the 0.228% product rounded where it is computed): exactly $84.84, which the project rounds half-up to $85.00; the model's $84.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $85.00
Model: $84.84
Work: MFS rate reduction table amount = 84.84

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", the row over $12,000 but not over $500,000, "$21 plus 0.228% of the excess over $12,000", on $40,000: exactly $84.84, which the project rounds half-up to $85.00; the model's $84.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $85.00

### classm.ny_it201.6 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: no federal EIC eligibility

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: no dependents claimed; not eligible

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: no other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 74 — Total Yonkers tax withheld
Status: **SKIPPED**

Model: blank
Work: no Yonkers withholding

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $148.00

### classm.ny_it201.6 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $3,321.00
Model: $3,319.00
Work: 3,467 - 148 = 3,319

Ruling: model error, carried: the model's own arithmetic on this line ("3,467 - 148 = 3,319") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,321.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.6 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **SKIPPED**

Model: blank
Work: prepayments 0 >= safe harbor 0; no penalty

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: no late filing/payment penalty or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: line 76 not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: no overpayment available for refund

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: no 529 refund deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: no refund after 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 80 — Amount you owe
Status: **DISAGREE**

Project: $3,321.00
Model: $3,319.00
Work: 3,319 + 0 + 0 = 3,319

Ruling: model error, carried: the model's own arithmetic on this line ("3,319 + 0 + 0 = 3,319") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,321.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### case classm.ny_it201.7 — prompt sha256 f5088a37975f0ccc3803258b55958c7759d10e2d11fc2dcf8cf4f601c731d6de; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.gov_pension:false, ny_it201.ask.us_obligation_interest:false, ny_it201.ask.pension_exclusion:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.mctmt:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.dependent_care:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.refund_529:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.gate.line26:false, ny_it201.gate.line28:false, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#1, ny_it201.hh_city_t5#1, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#4, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

### classm.ny_it201.7 — C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

Value: no

### classm.ny_it201.7 — H (count) — Number of dependents listed in item H
Status: **AGREE**

Value: 0

### classm.ny_it201.7 — 1 — Wages, salaries, tips, etc.
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — 2 — Taxable interest income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 3 — Ordinary dividends
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 5 — Alimony received
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 104
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 14 — Unemployment compensation
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 16 — Other income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — 18 — Total federal adjustments to income
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **AGREE**

Value: yes

### classm.ny_it201.7 — 20 — Interest income on state and local bonds and obligations (but not those of NYS o
Status: **SKIPPED**

Model: blank
Work: no state/local bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **SKIPPED**

Model: blank
Work: no 414(h) contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 22 — New York’s 529 college savings program distributions
Status: **SKIPPED**

Model: blank
Work: no nonqualified 529 withdrawal

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 23 — Other (Form IT-225, line 9)
Status: **SKIPPED**

Model: blank
Work: no other additions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **SKIPPED**

Model: blank
Work: no inflation refund included

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 26 — Pensions of NYS and local governments and the federal government
Status: **SKIPPED**

Model: blank
Work: no government pension subtraction

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 28 — Interest income on U.S. government bonds
Status: **SKIPPED**

Model: blank
Work: no U.S. bond interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 29 — Pension and annuity income exclusion
Status: **SKIPPED**

Model: blank
Work: no qualifying pension exclusion

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 30 — New York’s 529 college savings program deduction/earnings
Status: **SKIPPED**

Model: blank
Work: no NY 529 contribution/withdrawal

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 31 — Other (Form IT-225, line 18)
Status: **SKIPPED**

Model: blank
Work: no other subtractions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 32 — Add lines 25 through 31
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.7 — (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **SKIPPED**

Model: blank
Work: not single/C yes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 34 — Enter your standard deduction
Status: **AGREE**

Value: $16,050.00

### classm.ny_it201.7 — 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **AGREE**

Value: $64,999.00

### classm.ny_it201.7 — 36 — Dependent exemption amount (multiply the number of dependents listed in item H b
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 37 — Taxable income (subtract line 36 from line 35)
Status: **AGREE**

Value: $64,999.00

### classm.ny_it201.7 — 38 — Taxable income (from line 37 on page 2)
Status: **AGREE**

Value: $64,999.00

### classm.ny_it201.7 — (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: 2025 NYS Tax Table for 64999 MFJ

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: AGI <=107650; taxable <65000 uses table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: AGI not >107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not single/MFS

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: not head of household

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: AGI not >107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: AGI not >107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: NYS tax

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 2

### classm.ny_it201.7 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: income over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: income over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: no state household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (48) — The city household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: no city household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: federal AGI 81049 > 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 41 — Resident credit
Status: **SKIPPED**

Model: blank
Work: no out-of-state income tax

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **SKIPPED**

Model: blank
Work: no other nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: 3242 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 - 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,241.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **SKIPPED**

Model: blank
Work: no net other NYS taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: 3242 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 + 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,241.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 47 — NYC taxable income
Status: **AGREE**

Value: $64,999.00

### classm.ny_it201.7 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: NYC Tax Table/schedule for 64999 MFJ

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $2,308. The amount is $64,999 (agreed on both sides). The model gave $2,309.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: NYC resident tax

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $2,308. The amount is $64,999 (agreed on both sides). The model gave $2,309.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: income over 22500, no NYC household credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 - 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: full-year NYC resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **SKIPPED**

Model: blank
Work: no other NYC taxes

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309+0+0

Ruling: model error, carried: the model's own arithmetic on this line ("2309+0+0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **SKIPPED**

Model: blank
Work: no NYC nonrefundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 - 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: not subject to MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: not subject to MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: not subject to MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: not subject to MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: not subject to MCTMT

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 55 — Yonkers resident income tax surcharge
Status: **SKIPPED**

Model: blank
Work: not a Yonkers resident

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **SKIPPED**

Model: blank
Work: no Yonkers wages

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **SKIPPED**

Model: blank
Work: not part-year Yonkers

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 + 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.cap) — $125
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **SKIPPED**

Model: blank
Work: not used (no sales/use tax)

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **SKIPPED**

Model: blank
Work: no voluntary contributions

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $5,549.00
Model: $5,551.00
Work: 3242 + 2309 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 + 2309 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,549.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $5,549.00
Model: $5,551.00
Work: from line 61

Ruling: model error, carried: the model's own arithmetic on this line ("from line 61") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,549.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — 63 — Empire State child credit
Status: **SKIPPED**

Model: blank
Work: no qualifying child

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 64 — NYS/NYC child and dependent care credit
Status: **SKIPPED**

Model: blank
Work: no federal child/dependent care credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 65 — NYS earned income credit (EIC)
Status: **SKIPPED**

Model: blank
Work: no federal EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 66 — NYS noncustodial parent EIC
Status: **SKIPPED**

Model: blank
Work: no support payments

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 67 — Real property tax credit
Status: **SKIPPED**

Model: blank
Work: not claiming real property tax credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 68 — College tuition credit
Status: **SKIPPED**

Model: blank
Work: no college tuition

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $125.00

### classm.ny_it201.7 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $125.00

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **SKIPPED**

Model: blank
Work: income over 21600; low bracket not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $43,399.00

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $99.00
Model: $98.95
Work: 0.228% × 43399

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.228% of the excess over $21,600" on New York City taxable income of $64,999: exactly $98.94972, which the project rounds half-up to $99.00; the model's $98.95 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $37.00

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $136.00
Model: $135.95
Work: 37 + 98.95

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "$37 plus 0.228% of the excess over $21,600" on $64,999 (the 0.228% product rounded where it is computed): exactly $135.94972, which the project rounds half-up to $136.00; the model's $135.95 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **AGREE**

Value: $136.00

### classm.ny_it201.7 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $136.00

### classm.ny_it201.7 — 70 — NYC earned income credit
Status: **SKIPPED**

Model: blank
Work: no federal EIC

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 70a — NYC income tax elimination credit
Status: **SKIPPED**

Model: blank
Work: no dependents; IT-270 not eligible

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **SKIPPED**

Model: blank
Work: no other refundable credits

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $261.00

### classm.ny_it201.7 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $5,288.00
Model: $5,290.00
Work: 5551 - 261

Ruling: model error, carried: the model's own arithmetic on this line ("5551 - 261") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,288.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment
Status: **SKIPPED**

Model: blank
Work: no penalty; prepayments 0 ≥ safe harbor 0

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 82 — Other penalties and interest
Status: **SKIPPED**

Model: blank
Work: no late filing/payment penalty or interest

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: line 76 not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: no overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: no 529 deposit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: no refund

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 80 — Amount you owe
Status: **DISAGREE**

Project: $5,288.00
Model: $5,290.00
Work: 5551 - 261 + 0 penalties

Ruling: model error, carried: the model's own arithmetic on this line ("5551 - 261 + 0 penalties") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,288.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. [dropped]

## Raw responses

### classm.ny_it201.1

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "Item C marked No"
  - printed: "line H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "line 1"
    value: "40000.00"
    work: "Federal Form 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "Federal taxable interest"
  - printed: "line 3"
    value: "0.00"
    work: "Federal ordinary dividends"
  - printed: "line 4"
    value: "0.00"
    work: "Federal Schedule 1 line 1"
  - printed: "line 5"
    value: "0.00"
    work: "Federal alimony received"
  - printed: "line 6"
    value: "0.00"
    work: "Federal business income"
  - printed: "line 7"
    value: "0.00"
    work: "Federal capital gain or loss"
  - printed: "line 8"
    value: "0.00"
    work: "No other gains or losses"
  - printed: "line 9"
    value: "0.00"
    work: "Federal IRA taxable amount"
  - printed: "line 10"
    value: "0.00"
    work: "Federal pension taxable amount"
  - printed: "line 11"
    value: "0.00"
    work: "No rental/partnership/etc. income"
  - printed: "line 12"
    value: "0.00"
    work: "No rental real estate in line 11"
  - printed: "line 13"
    value: "0.00"
    work: "No farm income"
  - printed: "line 14"
    value: "0.00"
    work: "Federal unemployment compensation"
  - printed: "line 15"
    value: "0.00"
    work: "Federal taxable Social Security"
  - printed: "line 16"
    value: "0.00"
    work: "Federal Schedule 1 line 9"
  - printed: "line 17"
    value: "40000.00"
    work: "40000 + 0"
  - printed: "line 18"
    value: "0.00"
    work: "Federal Schedule 1 line 26"
  - printed: "line 19"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "line (check)"
    value: "yes"
    work: "Line 19 equals federal AGI rounded"
  - printed: "line 20"
    value: ""
    work: "No out-of-state bond interest"
  - printed: "line 21"
    value: ""
    work: "No 414(h) contributions"
  - printed: "line 22"
    value: ""
    work: "No nonqualified NY 529 withdrawal"
  - printed: "line 23"
    value: ""
    work: "No other additions"
  - printed: "line 24"
    value: "40000.00"
    work: "40000 + 0"
  - printed: "line 25"
    value: ""
    work: "No inflation refund included"
  - printed: "line 26"
    value: ""
    work: "No government pension subtraction"
  - printed: "line 27"
    value: ""
    work: "No Social Security subtraction"
  - printed: "line 28"
    value: ""
    work: "No U.S. government bond interest"
  - printed: "line 29"
    value: ""
    work: "No pension/annuity exclusion"
  - printed: "line 30"
    value: ""
    work: "No NY 529 deduction"
  - printed: "line 31"
    value: ""
    work: "No other subtractions"
  - printed: "line 32"
    value: "0.00"
    work: "Sum lines 25-31"
  - printed: "line 33"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "Single with item C No"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Single with item C Yes"
  - printed: "line 34"
    value: "8000.00"
    work: "Standard deduction"
  - printed: "line 35"
    value: "32000.00"
    work: "40000 - 8000"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents x 1000"
  - printed: "line 37"
    value: "32000.00"
    work: "32000 - 0"
  - printed: "line 38"
    value: "32000.00"
    work: "From line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "1596.00"
    work: "2025 NYS Tax Table for 32000"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "1596.00"
    work: "Tax Table used because taxable income below 65000"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "TCW not applicable"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not filing jointly"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "TCW not required"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not head of household"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "No TCW required"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "NY AGI not over 107650"
  - printed: "line 39"
    value: "1596.00"
    work: "From 2025 NYS Tax Table"
  - printed: "line (Note 1)"
    value: "40000.00"
    work: "Line 19 federal AGI"
  - printed: "line (column)"
    value: "1"
    work: "0 dependents plus 1 for taxpayer"
  - printed: "line (table 2, column 1)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 1)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 2)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 2)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 3)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 3)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 4)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 4)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 5)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 5)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 6)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 6)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2, column 7)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5, column 7)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 2)"
    value: ""
    work: "Table 2 not used for single"
  - printed: "line (table 5)"
    value: ""
    work: "Table 5 not used for single"
  - printed: "line (table 1)"
    value: ""
    work: "FAGI 40000 exceeds table 1 limit"
  - printed: "line (table 4)"
    value: ""
    work: "FAGI 40000 exceeds table 4 limit"
  - printed: "line (40)"
    value: ""
    work: "No state household credit"
  - printed: "line 40"
    value: ""
    work: "No credit allowed"
  - printed: "line 41"
    value: ""
    work: "No resident credit"
  - printed: "line 42"
    value: ""
    work: "No other nonrefundable credits"
  - printed: "line 43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "line 44"
    value: "1596.00"
    work: "1596 - 0"
  - printed: "line 45"
    value: ""
    work: "No other NYS taxes"
  - printed: "line 46"
    value: "1596.00"
    work: "1596 + 0"
  - printed: "line 47"
    value: "32000.00"
    work: "Line 38 amount; no Charitable Gifts adjustment"
  - printed: "line (47a)"
    value: "1125.00"
    work: "NYC tax table for 32000"
  - printed: "line 47a"
    value: "1125.00"
    work: "From NYC resident tax table"
  - printed: "line 48"
    value: ""
    work: "No NYC household credit"
  - printed: "line 49"
    value: "1125.00"
    work: "1125 - 0"
  - printed: "line 50"
    value: ""
    work: "Full-year NYC resident"
  - printed: "line 51"
    value: ""
    work: "No other NYC taxes"
  - printed: "line 52"
    value: "1125.00"
    work: "1125 + 0 + 0"
  - printed: "line 53"
    value: ""
    work: "No NYC nonrefundable credits"
  - printed: "line 54"
    value: "1125.00"
    work: "1125 - 0"
  - printed: "line 54a"
    value: ""
    work: "MCTMT skipped"
  - printed: "line 54b"
    value: ""
    work: "MCTMT skipped"
  - printed: "line 54c"
    value: ""
    work: "MCTMT skipped"
  - printed: "line 54d"
    value: ""
    work: "MCTMT skipped"
  - printed: "line 54e"
    value: ""
    work: "MCTMT skipped"
  - printed: "line 55"
    value: ""
    work: "Not a Yonkers resident"
  - printed: "line 56"
    value: ""
    work: "No Yonkers work income"
  - printed: "line 57"
    value: ""
    work: "No part-year Yonkers residency"
  - printed: "line 58"
    value: "1125.00"
    work: "1125 + 0"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row up to 15000"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 15001-30000"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 30001-50000"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 50001-75000"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 75001-100000"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 100001-150000"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 150001-200000"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: "7.00"
    work: "0.000175 x 40000"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Chart cap"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: "7.00"
    work: "Smaller of 7 and 125"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: "10.00"
    work: "FAGI 40000 in 30001-50000 row"
  - printed: "line 59"
    value: "10.00"
    work: "Sales/use tax chart amount"
  - printed: "line 60"
    value: ""
    work: "No voluntary contributions"
  - printed: "line 61"
    value: "2731.00"
    work: "1596 + 1125 + 10 + 0"
  - printed: "line 62"
    value: "2731.00"
    work: "From line 61"
  - printed: "line 63"
    value: ""
    work: "No qualifying child"
  - printed: "line 64"
    value: ""
    work: "No federal child/dependent care credit eligibility"
  - printed: "line 65"
    value: ""
    work: "No NYS EIC"
  - printed: "line 66"
    value: ""
    work: "No child support paid"
  - printed: "line 67"
    value: ""
    work: "No real property tax credit"
  - printed: "line 68"
    value: ""
    work: "No college tuition expenses"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "40000.00"
    work: "40000 - 0 IRA distributions"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1 single amount"
  - printed: "line 69"
    value: "63.00"
    work: "Full-year NYC resident Table 1"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: "54.72"
    work: "0.171% x 32000"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: "20000.00"
    work: "32000 - 12000"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: "45.60"
    work: "0.228% x 20000"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: "21.00"
    work: "Single bracket base"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: "66.60"
    work: "21 + 45.60"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "66.60"
    work: "Rate reduction amount"
  - printed: "line 69a"
    value: "67.00"
    work: "66.60 rounded to whole dollars"
  - printed: "line 70"
    value: ""
    work: "No NYC EIC"
  - printed: "line 70a"
    value: ""
    work: "No dependents; elimination credit not allowed"
  - printed: "line 71"
    value: ""
    work: "No other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "NYS tax withheld"
  - printed: "line 73"
    value: "0.00"
    work: "NYC tax withheld"
  - printed: "line 74"
    value: "0.00"
    work: "Yonkers tax withheld"
  - printed: "line 75"
    value: "0.00"
    work: "Estimated tax payments"
  - printed: "line 76"
    value: "130.00"
    work: "63 + 67 + 0"
  - printed: "line (80)"
    value: "2601.00"
    work: "2731 - 130"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "Lines 72-75"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% of 2024 NY tax"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% of 2024 NY tax"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "Required prepayments"
  - printed: "line 81"
    value: "0.00"
    work: "No estimated tax penalty"
  - printed: "line 82"
    value: ""
    work: "No other penalties or interest"
  - printed: "line (77)"
    value: ""
    work: "Line 76 not more than line 62"
  - printed: "line 77"
    value: ""
    work: "No overpayment"
  - printed: "line 78"
    value: ""
    work: "No refund"
  - printed: "line 78a"
    value: ""
    work: "No NYS 529 deposit"
  - printed: "line 78b"
    value: ""
    work: "No refund after 529 deposit"
  - printed: "line 80"
    value: "2601.00"
    work: "2731 - 130 + 0 + 0"
```

### classm.ny_it201.2

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "item C answer is no"
  - printed: "line H (count)"
    value: "75"
    work: "75 dependent entries p1-p75"
  - printed: "line 1"
    value: "107688.00"
    work: "federal 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "federal 1040 line 2b"
  - printed: "line 3"
    value: "0.00"
    work: "federal 1040 line 3b"
  - printed: "line 4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "line 5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "line 6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "line 7"
    value: "0.00"
    work: "federal 1040 line 7a"
  - printed: "line 8"
    value: "0.00"
    work: "no other gains"
  - printed: "line 9"
    value: "0.00"
    work: "federal 1040 line 4b"
  - printed: "line 10"
    value: "0.00"
    work: "federal 1040 line 5b"
  - printed: "line 11"
    value: "0.00"
    work: "no Schedule E income"
  - printed: "line 12"
    value: "0.00"
    work: "none included in line 11"
  - printed: "line 13"
    value: "0.00"
    work: "no farm income"
  - printed: "line 14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "line 15"
    value: "0.00"
    work: "federal 1040 line 6b"
  - printed: "line 16"
    value: "0.00"
    work: "Schedule 1 line 9 total other income"
  - printed: "line 17"
    value: "107688.00"
    work: "107688 + zeros"
  - printed: "line 18"
    value: "0.00"
    work: "Schedule 1 line 26 adjustments"
  - printed: "line 19"
    value: "107688.00"
    work: "107688 - 0"
  - printed: "line (check)"
    value: "yes"
    work: "107688 equals federal AGI"
  - printed: "line 20"
    value: ""
    work: "no state/local bond interest addition"
  - printed: "line 21"
    value: ""
    work: "no 414(h) contributions"
  - printed: "line 22"
    value: ""
    work: "no NY 529 nonqualified withdrawal"
  - printed: "line 23"
    value: ""
    work: "no other IT-225 additions"
  - printed: "line 24"
    value: "107688.00"
    work: "107688 + 0"
  - printed: "line 25"
    value: "0.00"
    work: "from line 4"
  - printed: "line 26"
    value: ""
    work: "no NY/federal government pension subtraction"
  - printed: "line 27"
    value: "0.00"
    work: "from line 15"
  - printed: "line 28"
    value: ""
    work: "no U.S. government bond interest"
  - printed: "line 29"
    value: ""
    work: "no pension annuity exclusion"
  - printed: "line 30"
    value: ""
    work: "no NY 529 deduction"
  - printed: "line 31"
    value: ""
    work: "no other IT-225 subtractions"
  - printed: "line 32"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "line 33"
    value: "107688.00"
    work: "107688 - 0"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "MFJ standard deduction table"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: ""
    work: "not single with item C yes"
  - printed: "line 34"
    value: "16050.00"
    work: "standard deduction"
  - printed: "line 35"
    value: "91638.00"
    work: "107688 - 16050"
  - printed: "line 36"
    value: "75000.00"
    work: "75 dependents x 1000"
  - printed: "line 37"
    value: "16638.00"
    work: "91638 - 75000"
  - printed: "line 38"
    value: "16638.00"
    work: "from line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: ""
    work: "not used; NY AGI over 107650"
  - printed: "line (39) (ny_it201.tax_low)"
    value: ""
    work: "not used; NY AGI over 107650"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "not over 25M"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: "666.00"
    work: "worksheet 1 MFJ tax"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "not single/MFS"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "not HOH"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: "666.00"
    work: "MFJ worksheet tax"
  - printed: "line (39) (ny_it201.tax_high)"
    value: "666.00"
    work: "AGI over 107650 worksheet tax"
  - printed: "line 39"
    value: "666.00"
    work: "tax on 16638"
  - printed: "line (Note 1)"
    value: "107688.00"
    work: "line19 for household credit"
  - printed: "line (column)"
    value: "77"
    work: "75 dependents + taxpayer + spouse"
  - printed: "line (table 2, column 1)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 1)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 2)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 2)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 3)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 3)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 4)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 4)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 5)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 5)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 6)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 6)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2, column 7)"
    value: ""
    work: "AGI over 32000; no credit"
  - printed: "line (table 5, column 7)"
    value: ""
    work: "AGI over 22500; no credit"
  - printed: "line (table 2)"
    value: ""
    work: "no credit allowed"
  - printed: "line (table 5)"
    value: ""
    work: "no credit allowed"
  - printed: "line (table 1)"
    value: ""
    work: "single table not applicable"
  - printed: "line (table 4)"
    value: ""
    work: "single table not applicable"
  - printed: "line (40)"
    value: ""
    work: "no credit allowed"
  - printed: "line (48)"
    value: ""
    work: "no credit allowed"
  - printed: "line 40"
    value: ""
    work: "no NYS household credit"
  - printed: "line 41"
    value: ""
    work: "no resident credit"
  - printed: "line 42"
    value: ""
    work: "no other nonrefundable credits"
  - printed: "line 43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "line 44"
    value: "666.00"
    work: "666 - 0"
  - printed: "line 45"
    value: ""
    work: "no other NYS taxes"
  - printed: "line 46"
    value: "666.00"
    work: "666 + 0"
  - printed: "line 47"
    value: "16638.00"
    work: "NYC taxable income from line 38"
  - printed: "line (47a)"
    value: "512.00"
    work: "NYC tax table on 16638"
  - printed: "line 47a"
    value: "512.00"
    work: "NYC resident tax"
  - printed: "line 48"
    value: ""
    work: "no NYC household credit"
  - printed: "line 49"
    value: "512.00"
    work: "512 - 0"
  - printed: "line 50"
    value: ""
    work: "full-year NYC resident"
  - printed: "line 51"
    value: ""
    work: "no other NYC taxes"
  - printed: "line 52"
    value: "512.00"
    work: "512 + 0 + 0"
  - printed: "line 53"
    value: ""
    work: "no NYC nonrefundable credits"
  - printed: "line 54"
    value: "512.00"
    work: "512 - 0"
  - printed: "line 54a"
    value: ""
    work: "skip MCTMT; no earnings over 50000"
  - printed: "line 54b"
    value: ""
    work: "skip MCTMT; no earnings over 50000"
  - printed: "line 54c"
    value: ""
    work: "skip MCTMT"
  - printed: "line 54d"
    value: ""
    work: "skip MCTMT"
  - printed: "line 54e"
    value: ""
    work: "skip MCTMT"
  - printed: "line 55"
    value: ""
    work: "no Yonkers resident surcharge"
  - printed: "line 56"
    value: ""
    work: "no Yonkers nonresident earnings tax"
  - printed: "line 57"
    value: ""
    work: "no part-year Yonkers surcharge"
  - printed: "line 58"
    value: "512.00"
    work: "512 + zeros"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: ""
    work: "sales chart not used; no use tax"
  - printed: "line 59"
    value: "0.00"
    work: "no sales or use tax"
  - printed: "line 60"
    value: ""
    work: "no voluntary contributions"
  - printed: "line 61"
    value: "1178.00"
    work: "666 + 512 + 0 + 0"
  - printed: "line 62"
    value: "1178.00"
    work: "from line 61"
  - printed: "line 63"
    value: ""
    work: "no qualifying child under 17"
  - printed: "line 64"
    value: ""
    work: "no federal child/dependent care credit"
  - printed: "line 65"
    value: ""
    work: "no NYS EIC"
  - printed: "line 66"
    value: ""
    work: "no child support through SCU"
  - printed: "line 67"
    value: ""
    work: "no real property tax credit"
  - printed: "line 68"
    value: ""
    work: "no college tuition expenses"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "107688.00"
    work: "107688 - 0 IRA distributions"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1 MFJ full-year NYC"
  - printed: "line 69"
    value: "125.00"
    work: "NYC school tax fixed credit"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: "28.45"
    work: "16638 x 0.00171"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: ""
    work: "not over 21600"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: ""
    work: "not over 21600"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: ""
    work: "low bracket"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: ""
    work: "low bracket"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "28.00"
    work: "rounded low rate credit"
  - printed: "line 69a"
    value: "28.00"
    work: "NYC school tax rate reduction"
  - printed: "line 70"
    value: ""
    work: "no NYC EIC"
  - printed: "line 70a"
    value: ""
    work: "FAGI exceeds elimination credit threshold by more than 5000"
  - printed: "line 71"
    value: ""
    work: "no other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "NYS withholding is 0"
  - printed: "line 73"
    value: "0.00"
    work: "NYC withholding is 0"
  - printed: "line 74"
    value: "0.00"
    work: "Yonkers withholding is 0"
  - printed: "line 76"
    value: "153.00"
    work: "125 + 28 + 0 payments"
  - printed: "line (80)"
    value: "1025.00"
    work: "1178 - 153"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "lines 72-75 total"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% of 2024 NY tax"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% of 2024 NY tax"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "prepayments required are 0"
  - printed: "line 81"
    value: ""
    work: "no estimated tax penalty"
  - printed: "line 82"
    value: ""
    work: "no other penalties or interest"
  - printed: "line (77)"
    value: ""
    work: "line 76 is not more than line 62"
  - printed: "line 77"
    value: ""
    work: "no overpayment"
  - printed: "line 78"
    value: ""
    work: "no overpayment"
  - printed: "line 78a"
    value: ""
    work: "no NYS 529 deposit"
  - printed: "line 78b"
    value: ""
    work: "no refund"
  - printed: "line 80"
    value: "1025.00"
    work: "1178 - 153"
```

### classm.ny_it201.3

```yaml
lines:
  - printed: "line C"
    value: "yes"
    work: "Filer marked item C Yes"
  - printed: "line H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "line 1"
    value: "40000.00"
    work: "Federal Form 1040 line 1z wages"
  - printed: "line 2"
    value: "0.00"
    work: "Federal Form 1040 line 2b"
  - printed: "line 3"
    value: "0.00"
    work: "Federal Form 1040 line 3b"
  - printed: "line 4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "line 5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "line 6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "line 7"
    value: "0.00"
    work: "Federal Form 1040 line 7a"
  - printed: "line 8"
    value: "0.00"
    work: "No Form 4797 amount"
  - printed: "line 9"
    value: "0.00"
    work: "Federal Form 1040 line 4b"
  - printed: "line 10"
    value: "0.00"
    work: "Federal Form 1040 line 5b"
  - printed: "line 11"
    value: "0.00"
    work: "No Schedule E amount"
  - printed: "line 12"
    value: "0.00"
    work: "Rental real estate included in line 11"
  - printed: "line 13"
    value: "0.00"
    work: "No Schedule F amount"
  - printed: "line 14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "line 15"
    value: "0.00"
    work: "Federal Form 1040 line 6b"
  - printed: "line 16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "line 17"
    value: "40000.00"
    work: "Add lines 1-11 and 13-16"
  - printed: "line 18"
    value: "0.00"
    work: "Schedule 1 line 26 adjustments"
  - printed: "line 19"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "line (check)"
    value: "yes"
    work: "Line 19 equals federal AGI"
  - printed: "line 20"
    value: ""
    work: "No other-state bond interest; skip"
  - printed: "line 21"
    value: ""
    work: "No 414(h) contributions; skip"
  - printed: "line 22"
    value: ""
    work: "No NY 529 nonqualified withdrawal; skip"
  - printed: "line 23"
    value: ""
    work: "No other additions; skip"
  - printed: "line 24"
    value: "40000.00"
    work: "40000 + 0 additions"
  - printed: "line 25"
    value: "0.00"
    work: "From line 4"
  - printed: "line 26"
    value: ""
    work: "No government pension; skip"
  - printed: "line 27"
    value: "0.00"
    work: "From line 15"
  - printed: "line 28"
    value: ""
    work: "No U.S. government bond interest; skip"
  - printed: "line 29"
    value: ""
    work: "No pension/annuity exclusion; skip"
  - printed: "line 30"
    value: ""
    work: "No NY 529 deduction; skip"
  - printed: "line 31"
    value: ""
    work: "No other subtractions; skip"
  - printed: "line 32"
    value: "0.00"
    work: "Add lines 25-31"
  - printed: "line 33"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "Single standard deduction table amount"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Single and item C Yes"
  - printed: "line 34"
    value: "3100.00"
    work: "Single dependent standard deduction"
  - printed: "line 35"
    value: "36900.00"
    work: "40000 - 3100"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents x 1000"
  - printed: "line 37"
    value: "36900.00"
    work: "36900 - 0"
  - printed: "line 38"
    value: "36900.00"
    work: "From line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "1865.00"
    work: "2025 NYS Tax Table on 36900"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "1865.00"
    work: "AGI <= 107650 and taxable income < 65000; tax table"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "High-income worksheet not applicable"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Married worksheet not applicable"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "High-income single worksheet not applicable"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Head of household worksheet not applicable"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Tax computation worksheet not applicable"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "AGI not more than 107650"
  - printed: "line 39"
    value: "1865.00"
    work: "NYS tax from tax table"
  - printed: "line (Note 1)"
    value: "40000.00"
    work: "Federal AGI for household credit tables"
  - printed: "line (column)"
    value: "1"
    work: "0 dependents + 1 taxpayer"
  - printed: "line (table 2, column 1)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 1)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 2)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 2)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 3)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 3)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 4)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 4)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 5)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 5)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 6)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 6)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2, column 7)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5, column 7)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 2)"
    value: ""
    work: "Table 2 not applicable; Single"
  - printed: "line (table 5)"
    value: ""
    work: "Table 5 not applicable; Single"
  - printed: "line (table 1)"
    value: ""
    work: "AGI over 28000; no table 1 credit"
  - printed: "line (table 4)"
    value: ""
    work: "AGI over 12500; no table 4 credit"
  - printed: "line (40)"
    value: ""
    work: "Item C Yes; no household credit"
  - printed: "line (48)"
    value: ""
    work: "Item C Yes; no NYC household credit"
  - printed: "line 40"
    value: ""
    work: "Item C Yes; no household credit"
  - printed: "line 41"
    value: ""
    work: "No resident credit; skip"
  - printed: "line 42"
    value: ""
    work: "No other nonrefundable credits; skip"
  - printed: "line 43"
    value: "0.00"
    work: "Add lines 40-42"
  - printed: "line 44"
    value: "1865.00"
    work: "1865 - 0"
  - printed: "line 45"
    value: ""
    work: "No other NYS taxes; skip"
  - printed: "line 46"
    value: "1865.00"
    work: "1865 + 0"
  - printed: "line 47"
    value: "36900.00"
    work: "Line 38; no Charitable Gifts Trust Fund deduction"
  - printed: "line (47a)"
    value: "1312.00"
    work: "2025 NYC Tax Table on 36900"
  - printed: "line 47a"
    value: "1312.00"
    work: "NYC resident tax on line 47"
  - printed: "line 48"
    value: ""
    work: "Item C Yes; no NYC household credit"
  - printed: "line 49"
    value: "1312.00"
    work: "1312 - 0"
  - printed: "line 50"
    value: ""
    work: "Full-year NYC resident; no part-year tax"
  - printed: "line 51"
    value: ""
    work: "No other NYC taxes; skip"
  - printed: "line 52"
    value: "1312.00"
    work: "1312 + 0 + 0"
  - printed: "line 53"
    value: ""
    work: "No NYC nonrefundable credits; skip"
  - printed: "line 54"
    value: "1312.00"
    work: "1312 - 0"
  - printed: "line 54a"
    value: ""
    work: "No MCTMT Zone 1 net earnings; skip"
  - printed: "line 54b"
    value: ""
    work: "No MCTMT Zone 2 net earnings; skip"
  - printed: "line 54c"
    value: ""
    work: "No Zone 1 MCTMT; skip"
  - printed: "line 54d"
    value: ""
    work: "No Zone 2 MCTMT; skip"
  - printed: "line 54e"
    value: ""
    work: "No total MCTMT; skip"
  - printed: "line 55"
    value: ""
    work: "Not a Yonkers resident; skip"
  - printed: "line 56"
    value: ""
    work: "No Yonkers nonresident earnings tax; skip"
  - printed: "line 57"
    value: ""
    work: "No part-year Yonkers surcharge; skip"
  - printed: "line 58"
    value: "1312.00"
    work: "1312 + 0"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: ""
    work: "No sales/use tax owed; chart not used"
  - printed: "line 59"
    value: "0.00"
    work: "No sales or use tax owed; required 0 entry"
  - printed: "line 60"
    value: ""
    work: "No voluntary contributions; skip"
  - printed: "line 61"
    value: "3177.00"
    work: "1865 + 1312 + 0 + 0"
  - printed: "line 62"
    value: "3177.00"
    work: "From line 61"
  - printed: "line 63"
    value: ""
    work: "No qualifying child; no credit"
  - printed: "line 64"
    value: ""
    work: "No federal child/dependent care credit qualification"
  - printed: "line 65"
    value: ""
    work: "No federal EIC qualification"
  - printed: "line 66"
    value: ""
    work: "No noncustodial parent EIC"
  - printed: "line 67"
    value: ""
    work: "No real property tax credit"
  - printed: "line 68"
    value: ""
    work: "No college tuition credit"
  - printed: "line (69) (ny_it201.stc_income)"
    value: ""
    work: "Item C Yes; NYC school tax credit disqualified"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: ""
    work: "Item C Yes; NYC school tax credit disqualified"
  - printed: "line 69"
    value: ""
    work: "Item C Yes; no fixed NYC school tax credit"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: ""
    work: "Item C Yes; rate reduction credit disqualified"
  - printed: "line 69a"
    value: ""
    work: "Item C Yes; no NYC rate reduction credit"
  - printed: "line 70"
    value: ""
    work: "No federal EIC qualification"
  - printed: "line 70a"
    value: ""
    work: "No dependents claimed; NYC elimination credit not allowed"
  - printed: "line 71"
    value: ""
    work: "No other refundable credits; skip"
  - printed: "line 72"
    value: "0.00"
    work: "Form IT-2 NYS withholding"
  - printed: "line 73"
    value: "0.00"
    work: "Form IT-2 NYC withholding"
  - printed: "line 74"
    value: ""
    work: "No Yonkers withholding"
  - printed: "line 75"
    value: "0.00"
    work: "Estimated tax payments given"
  - printed: "line 76"
    value: "0.00"
    work: "Add lines 63-75"
  - printed: "line (80)"
    value: "3177.00"
    work: "Line 62 3177 - line 76 0"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "Lines 72-75 total"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% of 2024 NY tax 0"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% not applicable; 110% of 0"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "Prepayments 0 meet safe harbor 0"
  - printed: "line 81"
    value: ""
    work: "No estimated tax penalty"
  - printed: "line 82"
    value: ""
    work: "No late filing/payment penalty or interest"
  - printed: "line (77)"
    value: ""
    work: "Line 76 not more than line 62"
  - printed: "line 77"
    value: ""
    work: "No overpayment"
  - printed: "line 78"
    value: ""
    work: "No line 77 overpayment"
  - printed: "line 78a"
    value: ""
    work: "No NYS 529 refund deposit"
  - printed: "line 78b"
    value: ""
    work: "No refund after NYS 529 deposit"
  - printed: "line 80"
    value: "3177.00"
    work: "Line 62 3177 - line 76 0; no penalties"
```

### classm.ny_it201.4

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "filer supplied: cannot be claimed as a dependent"
  - printed: "line H (count)"
    value: "0"
    work: "no dependents listed in item H"
  - printed: "line 1"
    value: "20000.00"
    work: "federal Form 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "given taxable interest"
  - printed: "line 3"
    value: "0.00"
    work: "given ordinary dividends"
  - printed: "line 4"
    value: "0.00"
    work: "given state/local refund"
  - printed: "line 5"
    value: "0.00"
    work: "given alimony"
  - printed: "line 6"
    value: "0.00"
    work: "given business income"
  - printed: "line 7"
    value: "0.00"
    work: "given capital gain/loss"
  - printed: "line 8"
    value: "0.00"
    work: "no other gains"
  - printed: "line 9"
    value: "0.00"
    work: "given IRA distributions"
  - printed: "line 10"
    value: "0.00"
    work: "given pensions/annuities"
  - printed: "line 11"
    value: "0.00"
    work: "given rental/partnership/etc."
  - printed: "line 12"
    value: "0.00"
    work: "no rental real estate included"
  - printed: "line 13"
    value: "0.00"
    work: "given farm income"
  - printed: "line 14"
    value: "0.00"
    work: "given unemployment"
  - printed: "line 15"
    value: "0.00"
    work: "given Social Security"
  - printed: "line 16"
    value: "0.00"
    work: "given other income"
  - printed: "line 17"
    value: "20000.00"
    work: "add lines 1-11 and 13-16"
  - printed: "line 18"
    value: "0.00"
    work: "given federal adjustments"
  - printed: "line 19"
    value: "20000.00"
    work: "20000 - 0"
  - printed: "line (check)"
    value: "yes"
    work: "line 19 equals federal AGI rounded"
  - printed: "line 20"
    value: ""
    work: "skip: no out-of-state bond interest"
  - printed: "line 21"
    value: ""
    work: "skip: no 414(h) contributions"
  - printed: "line 22"
    value: ""
    work: "skip: no NY 529 nonqualified withdrawal"
  - printed: "line 23"
    value: ""
    work: "skip: no other NY additions"
  - printed: "line 24"
    value: "20000.00"
    work: "20000 + 0 additions"
  - printed: "line 25"
    value: "0.00"
    work: "from line 4; no inflation refund"
  - printed: "line 26"
    value: ""
    work: "skip: no government pension"
  - printed: "line 27"
    value: "0.00"
    work: "from line 15"
  - printed: "line 28"
    value: ""
    work: "skip: no U.S. government interest"
  - printed: "line 29"
    value: ""
    work: "skip: no pension exclusion"
  - printed: "line 30"
    value: ""
    work: "skip: no NY 529 deduction"
  - printed: "line 31"
    value: ""
    work: "skip: no other NY subtractions"
  - printed: "line 32"
    value: "0.00"
    work: "0 + 0 subtractions"
  - printed: "line 33"
    value: "20000.00"
    work: "20000 - 0"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "11200.00"
    work: "head of household standard deduction"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: ""
    work: "not applicable: not single and item C No"
  - printed: "line 34"
    value: "11200.00"
    work: "standard deduction for HOH"
  - printed: "line 35"
    value: "8800.00"
    work: "20000 - 11200"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents × 1000"
  - printed: "line 37"
    value: "8800.00"
    work: "8800 - 0"
  - printed: "line 38"
    value: "8800.00"
    work: "from line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "352.00"
    work: "tax table for 8800 HOH"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "352.00"
    work: "AGI <= 107650 and taxable < 65000"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "not applicable"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "not applicable"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "not applicable"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "not applicable: AGI not over 107650"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "not applicable"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "not applicable: AGI <= 107650"
  - printed: "line 39"
    value: "352.00"
    work: "NYS tax from tax table"
  - printed: "line (Note 1)"
    value: "20000.00"
    work: "line 19 federal AGI"
  - printed: "line (column)"
    value: "1"
    work: "0 dependents + 1 for you"
  - printed: "line (table 2, column 1)"
    value: "60.00"
    work: "FAGI 20000 row, column 1"
  - printed: "line (table 5, column 1)"
    value: "15.00"
    work: "FAGI 20000 row, column 1"
  - printed: "line (table 2, column 2)"
    value: "75.00"
    work: "FAGI 20000 row, column 2"
  - printed: "line (table 5, column 2)"
    value: "30.00"
    work: "FAGI 20000 row, column 2"
  - printed: "line (table 2, column 3)"
    value: "90.00"
    work: "FAGI 20000 row, column 3"
  - printed: "line (table 5, column 3)"
    value: "45.00"
    work: "FAGI 20000 row, column 3"
  - printed: "line (table 2, column 4)"
    value: "105.00"
    work: "FAGI 20000 row, column 4"
  - printed: "line (table 5, column 4)"
    value: "60.00"
    work: "FAGI 20000 row, column 4"
  - printed: "line (table 2, column 5)"
    value: "120.00"
    work: "FAGI 20000 row, column 5"
  - printed: "line (table 5, column 5)"
    value: "75.00"
    work: "FAGI 20000 row, column 5"
  - printed: "line (table 2, column 6)"
    value: "135.00"
    work: "FAGI 20000 row, column 6"
  - printed: "line (table 5, column 6)"
    value: "90.00"
    work: "FAGI 20000 row, column 6"
  - printed: "line (table 2, column 7)"
    value: "150.00"
    work: "FAGI 20000 row, column 7"
  - printed: "line (table 5, column 7)"
    value: "105.00"
    work: "FAGI 20000 row, column 7"
  - printed: "line (table 2)"
    value: "60.00"
    work: "number of people = 1 selects column 1"
  - printed: "line (table 5)"
    value: "15.00"
    work: "number of people = 1 selects column 1"
  - printed: "line (table 1)"
    value: ""
    work: "not applicable: not single"
  - printed: "line (table 4)"
    value: ""
    work: "not applicable: not single"
  - printed: "line (40)"
    value: "60.00"
    work: "NYS household credit table 2"
  - printed: "line (48)"
    value: "15.00"
    work: "NYC household credit table 5"
  - printed: "line 40"
    value: "60.00"
    work: "NYS household credit"
  - printed: "line 41"
    value: ""
    work: "skip: no resident credit"
  - printed: "line 42"
    value: ""
    work: "skip: no other nonrefundable credits"
  - printed: "line 43"
    value: "60.00"
    work: "60 + 0 + 0"
  - printed: "line 44"
    value: "292.00"
    work: "352 - 60"
  - printed: "line 45"
    value: ""
    work: "skip: no other NYS taxes"
  - printed: "line 46"
    value: "292.00"
    work: "292 + 0"
  - printed: "line 47"
    value: "8800.00"
    work: "no charitable gifts; from line 38"
  - printed: "line (47a)"
    value: "271.00"
    work: "NYC tax table for 8800 HOH"
  - printed: "line 47a"
    value: "271.00"
    work: "NYC resident tax"
  - printed: "line 48"
    value: "15.00"
    work: "NYC household credit"
  - printed: "line 49"
    value: "256.00"
    work: "271 - 15"
  - printed: "line 50"
    value: ""
    work: "skip: full-year NYC resident"
  - printed: "line 51"
    value: ""
    work: "skip: no other NYC taxes"
  - printed: "line 52"
    value: "256.00"
    work: "256 + 0 + 0"
  - printed: "line 53"
    value: ""
    work: "skip: no NYC nonrefundable credits"
  - printed: "line 54"
    value: "256.00"
    work: "256 - 0"
  - printed: "line 54a"
    value: ""
    work: "skip: no MCTMT Zone 1 earnings"
  - printed: "line 54b"
    value: ""
    work: "skip: no MCTMT Zone 2 earnings"
  - printed: "line 54c"
    value: ""
    work: "skip: no MCTMT Zone 1"
  - printed: "line 54d"
    value: ""
    work: "skip: no MCTMT Zone 2"
  - printed: "line 54e"
    value: ""
    work: "skip: no MCTMT"
  - printed: "line 55"
    value: ""
    work: "skip: not a Yonkers resident"
  - printed: "line 56"
    value: ""
    work: "skip: no Yonkers wages"
  - printed: "line 57"
    value: ""
    work: "skip: not part-year Yonkers resident"
  - printed: "line 58"
    value: "256.00"
    work: "256 + 0 MCTMT/Yonkers"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "chart row up to 15000"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "chart row 15001-30000"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "chart row 30001-50000"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "chart row 50001-75000"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "chart row 75001-100000"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "chart row 100001-150000"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "chart row 150001-200000"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: "3.50"
    work: "20000 × 0.000175 = 3.50"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "chart cap"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: "3.50"
    work: "smaller of 3.50 and 125"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: "6.00"
    work: "FAGI 20000 falls in 15001-30000 row"
  - printed: "line 59"
    value: "0.00"
    work: "no sales/use tax owed; enter 0"
  - printed: "line 60"
    value: ""
    work: "skip: no voluntary contributions"
  - printed: "line 61"
    value: "548.00"
    work: "292 + 256 + 0 + 0"
  - printed: "line 62"
    value: "548.00"
    work: "from line 61"
  - printed: "line 63"
    value: ""
    work: "skip: no qualifying child"
  - printed: "line 64"
    value: ""
    work: "skip: no federal child/dependent care credit"
  - printed: "line 65"
    value: ""
    work: "skip: no federal EIC claim"
  - printed: "line 66"
    value: ""
    work: "skip: no child support payments"
  - printed: "line 67"
    value: ""
    work: "skip: no real property tax credit"
  - printed: "line 68"
    value: ""
    work: "skip: no college tuition expenses"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "20000.00"
    work: "20000 - 0 IRA"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1, head of household, full-year NYC"
  - printed: "line 69"
    value: "63.00"
    work: "NYC school tax credit fixed amount"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: "15.05"
    work: "8800 × 0.00171 = 15.048"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: "0.00"
    work: "8800 - 14400 = 0"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: "0.00"
    work: "0 × 0.00228 = 0"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: "25.00"
    work: "HOH base amount"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: "25.00"
    work: "25 + 0"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "15.05"
    work: "use low bracket: 0.171% of taxable income"
  - printed: "line 69a"
    value: "15.00"
    work: "15.048 rounded to whole dollars"
  - printed: "line 70"
    value: ""
    work: "skip: no federal EIC claim"
  - printed: "line 70a"
    value: ""
    work: "not eligible: no dependents claimed"
  - printed: "line 71"
    value: ""
    work: "skip: no other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "NYS withheld from IT-2"
  - printed: "line 73"
    value: "0.00"
    work: "NYC withheld from IT-2"
  - printed: "line 74"
    value: "0.00"
    work: "no Yonkers withholding"
  - printed: "line 76"
    value: "78.00"
    work: "63 + 15 + 0 withholding/payments"
  - printed: "line (80)"
    value: "470.00"
    work: "548 - 78"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "lines 72-75 total"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% × 0 2024 tax"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% × 0 2024 tax"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "required prepayments = 0"
  - printed: "line 81"
    value: "0.00"
    work: "prepayments 0 meet safe harbor 0"
  - printed: "line 82"
    value: "0.00"
    work: "no late filing/payment penalty"
  - printed: "line (77)"
    value: ""
    work: "not applicable: line 76 not more than line 62"
  - printed: "line 77"
    value: ""
    work: "no overpayment"
  - printed: "line 78"
    value: ""
    work: "no overpayment"
  - printed: "line 78a"
    value: ""
    work: "no NYS 529 deposit"
  - printed: "line 78b"
    value: ""
    work: "no refund after NYS 529 deposit"
  - printed: "line 80"
    value: "470.00"
    work: "548 - 78 = 470 amount owed"
```

### classm.ny_it201.5

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "item C: cannot be claimed as a dependent"
  - printed: "line H (count)"
    value: "0"
    work: "no dependents listed"
  - printed: "line 1"
    value: "54325.00"
    work: "federal Form 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "federal 1040 line 2b = 0"
  - printed: "line 3"
    value: "0.00"
    work: "federal 1040 line 3b = 0"
  - printed: "line 4"
    value: "0.00"
    work: "federal Schedule 1 line 1 = 0"
  - printed: "line 5"
    value: "0.00"
    work: "federal Schedule 1 line 2a = 0"
  - printed: "line 6"
    value: "0.00"
    work: "federal Schedule 1 line 3 = 0"
  - printed: "line 7"
    value: "0.00"
    work: "federal 1040 line 7a = 0"
  - printed: "line 8"
    value: "0.00"
    work: "no other gains or losses"
  - printed: "line 9"
    value: "0.00"
    work: "federal 1040 line 4b = 0"
  - printed: "line 10"
    value: "0.00"
    work: "federal 1040 line 5b = 0"
  - printed: "line 11"
    value: "0.00"
    work: "no rental/partnership/S-corp/trust income"
  - printed: "line 12"
    value: "0.00"
    work: "no rental real estate included in line 11"
  - printed: "line 13"
    value: "0.00"
    work: "no farm income"
  - printed: "line 14"
    value: "0.00"
    work: "federal Schedule 1 line 7 = 0"
  - printed: "line 15"
    value: "0.00"
    work: "federal 1040 line 6b = 0"
  - printed: "line 16"
    value: "0.00"
    work: "federal Schedule 1 line 9 = 0"
  - printed: "line 17"
    value: "54325.00"
    work: "add lines 1-11 and 13-16 = 54,325"
  - printed: "line 18"
    value: "0.00"
    work: "federal Schedule 1 line 26 = 0"
  - printed: "line 19"
    value: "54325.00"
    work: "17 - 18 = 54,325"
  - printed: "line (check)"
    value: "yes"
    work: "line 19 equals federal AGI rounded"
  - printed: "line 20"
    value: ""
    work: "no other-state bond interest; skip to line 21"
  - printed: "line 21"
    value: ""
    work: "no 414(h) contributions; skip to line 22"
  - printed: "line 22"
    value: ""
    work: "no NY 529 nonqualified withdrawal; skip to line 23"
  - printed: "line 23"
    value: "0.00"
    work: "no other additions (IT-225 line 9 = 0)"
  - printed: "line 24"
    value: "54325.00"
    work: "19 + 20-23 = 54,325"
  - printed: "line 25"
    value: "0.00"
    work: "no inflation refund included in federal AGI"
  - printed: "line 26"
    value: ""
    work: "no NYS/local/federal government pension; skip to line 27"
  - printed: "line 27"
    value: "0.00"
    work: "from line 15 = 0"
  - printed: "line 28"
    value: ""
    work: "no U.S. government bond interest; skip to line 29"
  - printed: "line 29"
    value: ""
    work: "no qualifying pension/annuity income; skip to line 30"
  - printed: "line 30"
    value: ""
    work: "no NY 529 contributions/withdrawals; skip to line 31"
  - printed: "line 31"
    value: "0.00"
    work: "no other subtractions (IT-225 line 18 = 0)"
  - printed: "line 32"
    value: "0.00"
    work: "add lines 25-31 = 0"
  - printed: "line 33"
    value: "54325.00"
    work: "24 - 32 = 54,325"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "MFJ standard deduction"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: ""
    work: "not applicable; MFJ and item C No"
  - printed: "line 34"
    value: "16050.00"
    work: "MFJ standard deduction"
  - printed: "line 35"
    value: "38275.00"
    work: "33 - 34 = 54,325 - 16,050"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents x $1,000"
  - printed: "line 37"
    value: "38275.00"
    work: "35 - 36 = 38,275"
  - printed: "line 38"
    value: "38275.00"
    work: "from line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "1773.00"
    work: "2025 NYS Tax Table on 38,275 MFJ"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "1773.00"
    work: "AGI <= 107,650 and taxable < 65,000; use Tax Table"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "not applicable; NY AGI <= $107,650"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "not applicable; NY AGI <= $107,650"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "not applicable; filing status is MFJ"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "not applicable; filing status is MFJ"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "not applicable; NY AGI <= $107,650"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "not applicable; NY AGI <= $107,650"
  - printed: "line 39"
    value: "1773.00"
    work: "NYS tax from Tax Table on line 38"
  - printed: "line (Note 1)"
    value: "54325.00"
    work: "federal AGI for household credit tables = line 19"
  - printed: "line (column)"
    value: "2"
    work: "0 dependents + you + spouse = 2"
  - printed: "line (table 2, column 1)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 1)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 2)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 2)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 3)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 3)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 4)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 4)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 5)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 5)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 6)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 6)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2, column 7)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5, column 7)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 2)"
    value: "0.00"
    work: "AGI 54,325 > 32,000; no NYS household credit"
  - printed: "line (table 5)"
    value: "0.00"
    work: "AGI 54,325 > 22,500; no NYC household credit"
  - printed: "line (table 1)"
    value: "0.00"
    work: "single table not used; AGI 54,325 > 28,000"
  - printed: "line (table 4)"
    value: "0.00"
    work: "single table not used; AGI 54,325 > 12,500"
  - printed: "line (40)"
    value: "0.00"
    work: "state household credit table for MFJ = 0"
  - printed: "line (48)"
    value: "0.00"
    work: "city household credit table for MFJ = 0"
  - printed: "line 40"
    value: ""
    work: "no NYS household credit allowed"
  - printed: "line 41"
    value: ""
    work: "no resident credit; skip to line 42"
  - printed: "line 42"
    value: ""
    work: "no other NYS nonrefundable credits"
  - printed: "line 43"
    value: "0.00"
    work: "40 + 41 + 42 = 0"
  - printed: "line 44"
    value: "1773.00"
    work: "39 - 43 = 1,773"
  - printed: "line 45"
    value: ""
    work: "no net other NYS taxes"
  - printed: "line 46"
    value: "1773.00"
    work: "44 + 45 = 1,773"
  - printed: "line 47"
    value: "38275.00"
    work: "full-year NYC resident; line 38 amount"
  - printed: "line (47a)"
    value: "1292.00"
    work: "2025 NYC Tax Table on 38,275 MFJ"
  - printed: "line 47a"
    value: "1292.00"
    work: "NYC resident tax on line 47"
  - printed: "line 48"
    value: ""
    work: "no NYC household credit allowed"
  - printed: "line 49"
    value: "1292.00"
    work: "47a - 48 = 1,292 - 0"
  - printed: "line 50"
    value: ""
    work: "full-year NYC resident; no part-year tax"
  - printed: "line 51"
    value: ""
    work: "no other NYC taxes"
  - printed: "line 52"
    value: "1292.00"
    work: "49 + 50 + 51 = 1,292"
  - printed: "line 53"
    value: ""
    work: "no NYC nonrefundable credits; skip to line 54"
  - printed: "line 54"
    value: "1292.00"
    work: "52 - 53 = 1,292"
  - printed: "line 54a"
    value: ""
    work: "no MCTMT Zone 1 net earnings over $50,000; skip"
  - printed: "line 54b"
    value: ""
    work: "no MCTMT Zone 2 net earnings over $50,000; skip"
  - printed: "line 54c"
    value: ""
    work: "skip MCTMT Zone 1"
  - printed: "line 54d"
    value: ""
    work: "skip MCTMT Zone 2"
  - printed: "line 54e"
    value: ""
    work: "skip total MCTMT"
  - printed: "line 55"
    value: ""
    work: "not a Yonkers resident; skip"
  - printed: "line 56"
    value: ""
    work: "no Yonkers nonresident earnings; skip"
  - printed: "line 57"
    value: ""
    work: "not a part-year Yonkers resident; skip"
  - printed: "line 58"
    value: "1292.00"
    work: "54 + 54e-57 = 1,292"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "sales/use tax chart row up to 15,000"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "sales/use tax chart row 15,001-30,000"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "sales/use tax chart row 30,001-50,000"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "sales/use tax chart row 50,001-75,000"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "sales/use tax chart row 75,001-100,000"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "sales/use tax chart row 100,001-150,000"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "sales/use tax chart row 150,001-200,000"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: "9.51"
    work: "54,325 x 0.000175 = 9.506875"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "chart maximum"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: "9.51"
    work: "smaller of 9.506875 or 125"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: "15.00"
    work: "FAGI 54,325 falls in 50,001-75,000 row"
  - printed: "line 59"
    value: "15.00"
    work: "sales/use tax chart amount for FAGI 54,325"
  - printed: "line 60"
    value: ""
    work: "no voluntary contributions; skip to line 61"
  - printed: "line 61"
    value: "3080.00"
    work: "46 + 58 + 59 + 60 = 1,773 + 1,292 + 15"
  - printed: "line 62"
    value: "3080.00"
    work: "from line 61"
  - printed: "line 63"
    value: ""
    work: "no qualifying child; no Empire State child credit"
  - printed: "line 64"
    value: ""
    work: "no federal child/dependent care credit qualification"
  - printed: "line 65"
    value: ""
    work: "no federal EIC for 2025; no NYS EIC"
  - printed: "line 66"
    value: ""
    work: "no child support through NYS Support Collection Unit"
  - printed: "line 67"
    value: ""
    work: "no real property tax credit"
  - printed: "line 68"
    value: ""
    work: "no college tuition expenses"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "54325.00"
    work: "line 19 - line 9 = 54,325 - 0"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1 full-year NYC residents MFJ"
  - printed: "line 69"
    value: "125.00"
    work: "NYC school tax credit fixed amount"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "not used; city taxable income exceeds $21,600"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: "16675.00"
    work: "38,275 - 21,600"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: "38.02"
    work: "16,675 x 0.00228 = 38.019"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: "37.00"
    work: "MFJ bracket base over $21,600"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: "75.02"
    work: "37 + 38.019 = 75.019"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "75.00"
    work: "rate reduction amount rounded to whole dollars"
  - printed: "line 69a"
    value: "75.00"
    work: "NYC school tax credit rate reduction amount"
  - printed: "line 70"
    value: ""
    work: "no federal EIC; no NYC EIC"
  - printed: "line 70a"
    value: ""
    work: "no dependents; not eligible for NYC income tax elimination credit"
  - printed: "line 71"
    value: ""
    work: "no other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "IT-2 w0 NYS withheld = 0"
  - printed: "line 73"
    value: "0.00"
    work: "IT-2 w0 NYC withheld = 0"
  - printed: "line 74"
    value: "0.00"
    work: "no Yonkers tax withheld"
  - printed: "line 76"
    value: "200.00"
    work: "add lines 63-75 = 125 + 75"
  - printed: "line (80)"
    value: "2880.00"
    work: "62 - 76 = 3,080 - 200"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "lines 72-75 = 0"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 2024 NY tax 0"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 2024 NY tax 0"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 AGI <= 150,000; required = 100% = 0"
  - printed: "line 81"
    value: ""
    work: "prepayments 0 >= safe harbor 0; no penalty"
  - printed: "line 82"
    value: ""
    work: "no late filing/payment penalty or interest"
  - printed: "line (77)"
    value: ""
    work: "76 < 62; no overpayment"
  - printed: "line 77"
    value: ""
    work: "no overpayment"
  - printed: "line 78"
    value: ""
    work: "no line 77 overpayment available for refund"
  - printed: "line 78a"
    value: ""
    work: "no NYS 529 account deposit"
  - printed: "line 78b"
    value: ""
    work: "no refund after NYS 529 deposit"
  - printed: "line 80"
    value: "2880.00"
    work: "amount owed = 3,080 - 200"
```

### classm.ny_it201.6

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "item C answer is no"
  - printed: "line H (count)"
    value: "0"
    work: "no dependents listed"
  - printed: "line 1"
    value: "48000.00"
    work: "federal Form 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "federal Form 1040 line 2b"
  - printed: "line 3"
    value: "0.00"
    work: "federal Form 1040 line 3b"
  - printed: "line 4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "line 5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "line 6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "line 7"
    value: "0.00"
    work: "federal Form 1040 line 7a"
  - printed: "line 8"
    value: ""
    work: "no federal Form 4797 amount"
  - printed: "line 9"
    value: "0.00"
    work: "federal Form 1040 line 4b"
  - printed: "line 10"
    value: "0.00"
    work: "federal Form 1040 line 5b"
  - printed: "line 11"
    value: ""
    work: "no Schedule E amount"
  - printed: "line 12"
    value: ""
    work: "no rental real estate in line 11"
  - printed: "line 13"
    value: ""
    work: "no Schedule F amount"
  - printed: "line 14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "line 15"
    value: "0.00"
    work: "federal Form 1040 line 6b"
  - printed: "line 16"
    value: "0.00"
    work: "Schedule 1 line 9 total other income"
  - printed: "line 17"
    value: "48000.00"
    work: "48,000 wages plus zero other income"
  - printed: "line 18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "line 19"
    value: "48000.00"
    work: "48,000 - 0 = 48,000"
  - printed: "line (check)"
    value: "yes"
    work: "line 19 equals federal AGI 48,000"
  - printed: "line 20"
    value: ""
    work: "no state/local bond interest; skip"
  - printed: "line 21"
    value: ""
    work: "no 414(h) contributions; skip"
  - printed: "line 22"
    value: ""
    work: "no nonqualified 529 withdrawal; skip"
  - printed: "line 23"
    value: ""
    work: "no other additions; skip"
  - printed: "line 24"
    value: "48000.00"
    work: "48,000 + 0 = 48,000"
  - printed: "line 25"
    value: "0.00"
    work: "from line 4 = 0"
  - printed: "line 26"
    value: ""
    work: "no government pension; skip"
  - printed: "line 27"
    value: "0.00"
    work: "from line 15 = 0"
  - printed: "line 28"
    value: ""
    work: "no U.S. government bond interest; skip"
  - printed: "line 29"
    value: ""
    work: "no pension/annuity exclusion; skip"
  - printed: "line 30"
    value: ""
    work: "no 529 contributions/withdrawals; skip"
  - printed: "line 31"
    value: ""
    work: "no other subtractions; skip"
  - printed: "line 32"
    value: "0.00"
    work: "0 + 0 = 0"
  - printed: "line 33"
    value: "48000.00"
    work: "48,000 - 0 = 48,000"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "married filing separate standard deduction"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: ""
    work: "not single with item C Yes"
  - printed: "line 34"
    value: "8000.00"
    work: "standard deduction"
  - printed: "line 35"
    value: "40000.00"
    work: "48,000 - 8,000 = 40,000"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents * 1,000 = 0"
  - printed: "line 37"
    value: "40000.00"
    work: "40,000 - 0 = 40,000"
  - printed: "line 38"
    value: "40000.00"
    work: "from line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "2036.00"
    work: "tax table for taxable 40,000"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "2036.00"
    work: "AGI <= 107,650; taxable < 65,000 so tax table = 2,036"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "not applicable: AGI not over 25,000,000"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "not applicable: filing status not MFJ/QSS"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "not applicable: AGI <= 107,650"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "not applicable: not head of household"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "not applicable: no tax computation worksheet"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "not applicable: AGI <= 107,650"
  - printed: "line 39"
    value: "2036.00"
    work: "from tax table"
  - printed: "line (Note 1)"
    value: "48000.00"
    work: "line 19 federal AGI"
  - printed: "line (column)"
    value: "1"
    work: "0 dependents + 1 for you = 1"
  - printed: "line (table 2, column 1)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 1)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 2)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 2)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 3)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 3)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 4)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 4)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 5)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 5)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 6)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 6)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2, column 7)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5, column 7)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 2)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 5)"
    value: ""
    work: "AGI 48,000 over table limit; no credit"
  - printed: "line (table 1)"
    value: ""
    work: "single table; AGI over 28,000; no credit"
  - printed: "line (table 4)"
    value: ""
    work: "single NYC table; AGI over 12,500; no credit"
  - printed: "line (40)"
    value: ""
    work: "MFS table 3; AGI over 32,000; no credit"
  - printed: "line (48)"
    value: ""
    work: "MFS table 6; AGI over 22,500; no credit"
  - printed: "line 40"
    value: ""
    work: "no household credit"
  - printed: "line 41"
    value: ""
    work: "no out-of-state tax; skip"
  - printed: "line 42"
    value: ""
    work: "no other nonrefundable credits; skip"
  - printed: "line 43"
    value: "0.00"
    work: "0 + 0 + 0 = 0"
  - printed: "line 44"
    value: "2036.00"
    work: "2,036 - 0 = 2,036"
  - printed: "line 45"
    value: ""
    work: "no other NYS taxes; skip"
  - printed: "line 46"
    value: "2036.00"
    work: "2,036 + 0 = 2,036"
  - printed: "line 47"
    value: "40000.00"
    work: "NYC taxable income equals line 38"
  - printed: "line (47a)"
    value: "1431.00"
    work: "given NYC resident tax"
  - printed: "line 47a"
    value: "1431.00"
    work: "NYC resident tax on line 47"
  - printed: "line 48"
    value: ""
    work: "no NYC household credit"
  - printed: "line 49"
    value: "1431.00"
    work: "1,431 - 0 = 1,431"
  - printed: "line 50"
    value: ""
    work: "full-year NYC resident; not part-year"
  - printed: "line 51"
    value: ""
    work: "no other NYC taxes"
  - printed: "line 52"
    value: "1431.00"
    work: "1,431 + 0 + 0 = 1,431"
  - printed: "line 53"
    value: ""
    work: "no NYC nonrefundable credits"
  - printed: "line 54"
    value: "1431.00"
    work: "1,431 - 0 = 1,431"
  - printed: "line 54a"
    value: ""
    work: "no MCTMT; skip"
  - printed: "line 54b"
    value: ""
    work: "no MCTMT; skip"
  - printed: "line 54c"
    value: ""
    work: "no MCTMT; skip"
  - printed: "line 54d"
    value: ""
    work: "no MCTMT; skip"
  - printed: "line 54e"
    value: ""
    work: "no MCTMT; skip"
  - printed: "line 55"
    value: ""
    work: "not a Yonkers resident"
  - printed: "line 56"
    value: ""
    work: "no Yonkers nonresident earnings"
  - printed: "line 57"
    value: ""
    work: "not part-year Yonkers resident"
  - printed: "line 58"
    value: "1431.00"
    work: "1,431 + 0 = 1,431"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "chart row up to 15,000 = 3"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "chart row 15,001-30,000 = 6"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "chart row 30,001-50,000 = 10"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "chart row 50,001-75,000 = 15"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "chart row 75,001-100,000 = 18"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "chart row 100,001-150,000 = 26"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "chart row 150,001-200,000 = 34"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: "8.40"
    work: "0.000175 * 48,000 = 8.40"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "chart cap = 125"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: "8.40"
    work: "smaller of 8.40 and 125 = 8.40"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: "10.00"
    work: "AGI 48,000 falls in 30,001-50,000 row = 10"
  - printed: "line 59"
    value: "0.00"
    work: "no sales/use tax owed; enter 0"
  - printed: "line 60"
    value: ""
    work: "no voluntary contributions"
  - printed: "line 61"
    value: "3467.00"
    work: "2,036 + 1,431 + 0 + 0 = 3,467"
  - printed: "line 62"
    value: "3467.00"
    work: "from line 61"
  - printed: "line 63"
    value: ""
    work: "no qualifying child"
  - printed: "line 64"
    value: ""
    work: "no federal child/dependent care credit qualification"
  - printed: "line 65"
    value: ""
    work: "no federal EIC eligibility"
  - printed: "line 66"
    value: ""
    work: "no child support payments through Support Collection Unit"
  - printed: "line 67"
    value: ""
    work: "no real property tax credit qualification"
  - printed: "line 68"
    value: ""
    work: "no college tuition expenses"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "48000.00"
    work: "line 19 48,000 - line 9 0 = 48,000"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "full-year NYC MFS table 1 = 63"
  - printed: "line 69"
    value: "63.00"
    work: "NYC school tax credit fixed amount"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "not applicable; taxable income over 12,000"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: "28000.00"
    work: "40,000 - 12,000 = 28,000"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: "63.84"
    work: "0.00228 * 28,000 = 63.84"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: "21.00"
    work: "MFS base amount = 21"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: "84.84"
    work: "21 + 63.84 = 84.84"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "84.84"
    work: "MFS rate reduction table amount = 84.84"
  - printed: "line 69a"
    value: "85.00"
    work: "84.84 rounded to whole dollars = 85"
  - printed: "line 70"
    value: ""
    work: "no federal EIC eligibility"
  - printed: "line 70a"
    value: ""
    work: "no dependents claimed; not eligible"
  - printed: "line 71"
    value: ""
    work: "no other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "NYS withholding = 0"
  - printed: "line 73"
    value: "0.00"
    work: "NYC withholding = 0"
  - printed: "line 74"
    value: ""
    work: "no Yonkers withholding"
  - printed: "line 76"
    value: "148.00"
    work: "63 + 85 + 0 + 0 + 0 = 148"
  - printed: "line (80)"
    value: "3319.00"
    work: "3,467 - 148 = 3,319"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "withholding and estimated payments = 0"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% * 0 = 0"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% * 0 = 0"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 AGI not over 75,000; use 100% = 0"
  - printed: "line 81"
    value: ""
    work: "prepayments 0 >= safe harbor 0; no penalty"
  - printed: "line 82"
    value: ""
    work: "no late filing/payment penalty or interest"
  - printed: "line (77)"
    value: ""
    work: "line 76 not more than line 62"
  - printed: "line 77"
    value: ""
    work: "no overpayment"
  - printed: "line 78"
    value: ""
    work: "no overpayment available for refund"
  - printed: "line 78a"
    value: ""
    work: "no 529 refund deposit"
  - printed: "line 78b"
    value: ""
    work: "no refund after 529 deposit"
  - printed: "line 80"
    value: "3319.00"
    work: "3,319 + 0 + 0 = 3,319"
```

### classm.ny_it201.7

```yaml
lines:
  - printed: "line C"
    value: "no"
    work: "item C: cannot be claimed as a dependent"
  - printed: "line H (count)"
    value: "0"
    work: "no dependents listed"
  - printed: "line 1"
    value: "81049.00"
    work: "federal Form 1040 line 1z"
  - printed: "line 2"
    value: "0.00"
    work: "federal line 2b"
  - printed: "line 3"
    value: "0.00"
    work: "federal line 3b"
  - printed: "line 4"
    value: "0.00"
    work: "federal Schedule 1 line 1"
  - printed: "line 5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "line 6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "line 7"
    value: "0.00"
    work: "federal line 7a"
  - printed: "line 8"
    value: "0.00"
    work: "no other gains"
  - printed: "line 9"
    value: "0.00"
    work: "federal line 4b"
  - printed: "line 10"
    value: "0.00"
    work: "federal line 5b"
  - printed: "line 11"
    value: "0.00"
    work: "no rental/partnership income"
  - printed: "line 12"
    value: "0.00"
    work: "none included in line 11"
  - printed: "line 13"
    value: "0.00"
    work: "no farm income"
  - printed: "line 14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "line 15"
    value: "0.00"
    work: "federal line 6b"
  - printed: "line 16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "line 17"
    value: "81049.00"
    work: "81049 + zeros"
  - printed: "line 18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "line 19"
    value: "81049.00"
    work: "81049 - 0"
  - printed: "line (check)"
    value: "yes"
    work: "line 19 equals federal AGI rounded"
  - printed: "line 20"
    value: ""
    work: "no state/local bond interest"
  - printed: "line 21"
    value: ""
    work: "no 414(h) contributions"
  - printed: "line 22"
    value: ""
    work: "no nonqualified 529 withdrawal"
  - printed: "line 23"
    value: ""
    work: "no other additions"
  - printed: "line 24"
    value: "81049.00"
    work: "81049 + 0 additions"
  - printed: "line 25"
    value: ""
    work: "no inflation refund included"
  - printed: "line 26"
    value: ""
    work: "no government pension subtraction"
  - printed: "line 27"
    value: "0.00"
    work: "from line 15"
  - printed: "line 28"
    value: ""
    work: "no U.S. bond interest"
  - printed: "line 29"
    value: ""
    work: "no qualifying pension exclusion"
  - printed: "line 30"
    value: ""
    work: "no NY 529 contribution/withdrawal"
  - printed: "line 31"
    value: ""
    work: "no other subtractions"
  - printed: "line 32"
    value: "0.00"
    work: "0 subtractions"
  - printed: "line 33"
    value: "81049.00"
    work: "81049 - 0"
  - printed: "line (table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "MFJ standard deduction"
  - printed: "line (table) (ny_it201.std_deduction_dependent)"
    value: ""
    work: "not single/C yes"
  - printed: "line 34"
    value: "16050.00"
    work: "standard deduction"
  - printed: "line 35"
    value: "64999.00"
    work: "81049 - 16050"
  - printed: "line 36"
    value: "0.00"
    work: "0 dependents × 1000"
  - printed: "line 37"
    value: "64999.00"
    work: "64999 - 0"
  - printed: "line 38"
    value: "64999.00"
    work: "from line 37"
  - printed: "line (39) (ny_it201.tax_table)"
    value: "3242.00"
    work: "2025 NYS Tax Table for 64999 MFJ"
  - printed: "line (39) (ny_it201.tax_low)"
    value: "3242.00"
    work: "AGI <=107650; taxable <65000 uses table"
  - printed: "line (39) (ny_it201.tcw.top)"
    value: ""
    work: "not applicable"
  - printed: "line (39) (ny_it201.tcw.mfj)"
    value: ""
    work: "AGI not >107650"
  - printed: "line (39) (ny_it201.tcw.single)"
    value: ""
    work: "not single/MFS"
  - printed: "line (39) (ny_it201.tcw.hoh)"
    value: ""
    work: "not head of household"
  - printed: "line (39) (ny_it201.tcw.by_status)"
    value: ""
    work: "AGI not >107650"
  - printed: "line (39) (ny_it201.tax_high)"
    value: ""
    work: "AGI not >107650"
  - printed: "line 39"
    value: "3242.00"
    work: "NYS tax"
  - printed: "line (Note 1)"
    value: "81049.00"
    work: "line 19"
  - printed: "line (column)"
    value: "2"
    work: "0 dependents + you + spouse"
  - printed: "line (table 2, column 1)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 1)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 2)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 2)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 3)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 3)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 4)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 4)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 5)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 5)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 6)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 6)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2, column 7)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5, column 7)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 2)"
    value: ""
    work: "income over 32000, no credit"
  - printed: "line (table 5)"
    value: ""
    work: "income over 22500, no credit"
  - printed: "line (table 1)"
    value: ""
    work: "not single"
  - printed: "line (table 4)"
    value: ""
    work: "not single"
  - printed: "line (40)"
    value: ""
    work: "no state household credit"
  - printed: "line (48)"
    value: ""
    work: "no city household credit"
  - printed: "line 40"
    value: ""
    work: "federal AGI 81049 > 32000, no credit"
  - printed: "line 41"
    value: ""
    work: "no out-of-state income tax"
  - printed: "line 42"
    value: ""
    work: "no other nonrefundable credits"
  - printed: "line 43"
    value: "0.00"
    work: "0+0+0"
  - printed: "line 44"
    value: "3242.00"
    work: "3242 - 0"
  - printed: "line 45"
    value: ""
    work: "no net other NYS taxes"
  - printed: "line 46"
    value: "3242.00"
    work: "3242 + 0"
  - printed: "line 47"
    value: "64999.00"
    work: "NYC taxable income = line 38"
  - printed: "line (47a)"
    value: "2309.00"
    work: "NYC Tax Table/schedule for 64999 MFJ"
  - printed: "line 47a"
    value: "2309.00"
    work: "NYC resident tax"
  - printed: "line 48"
    value: ""
    work: "income over 22500, no NYC household credit"
  - printed: "line 49"
    value: "2309.00"
    work: "2309 - 0"
  - printed: "line 50"
    value: ""
    work: "full-year NYC resident"
  - printed: "line 51"
    value: ""
    work: "no other NYC taxes"
  - printed: "line 52"
    value: "2309.00"
    work: "2309+0+0"
  - printed: "line 53"
    value: ""
    work: "no NYC nonrefundable credits"
  - printed: "line 54"
    value: "2309.00"
    work: "2309 - 0"
  - printed: "line 54a"
    value: ""
    work: "not subject to MCTMT"
  - printed: "line 54b"
    value: ""
    work: "not subject to MCTMT"
  - printed: "line 54c"
    value: ""
    work: "not subject to MCTMT"
  - printed: "line 54d"
    value: ""
    work: "not subject to MCTMT"
  - printed: "line 54e"
    value: ""
    work: "not subject to MCTMT"
  - printed: "line 55"
    value: ""
    work: "not a Yonkers resident"
  - printed: "line 56"
    value: ""
    work: "no Yonkers wages"
  - printed: "line 57"
    value: ""
    work: "not part-year Yonkers"
  - printed: "line 58"
    value: "2309.00"
    work: "2309 + 0"
  - printed: "line (chart) (ny_it201.sut.b1)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b2)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b3)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b4)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b5)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b6)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.b7)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.top_product)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.cap)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.top)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line (chart) (ny_it201.sut.chart)"
    value: ""
    work: "not used (no sales/use tax)"
  - printed: "line 59"
    value: "0.00"
    work: "no sales/use tax owed; enter 0"
  - printed: "line 60"
    value: ""
    work: "no voluntary contributions"
  - printed: "line 61"
    value: "5551.00"
    work: "3242 + 2309 + 0 + 0"
  - printed: "line 62"
    value: "5551.00"
    work: "from line 61"
  - printed: "line 63"
    value: ""
    work: "no qualifying child"
  - printed: "line 64"
    value: ""
    work: "no federal child/dependent care credit"
  - printed: "line 65"
    value: ""
    work: "no federal EIC"
  - printed: "line 66"
    value: ""
    work: "no support payments"
  - printed: "line 67"
    value: ""
    work: "not claiming real property tax credit"
  - printed: "line 68"
    value: ""
    work: "no college tuition"
  - printed: "line (69) (ny_it201.stc_income)"
    value: "81049.00"
    work: "line 19 81049 - line 9 0"
  - printed: "line (69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1 MFJ full-year NYC"
  - printed: "line 69"
    value: "125.00"
    work: "NYC school tax credit fixed"
  - printed: "line (69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "income over 21600; low bracket not used"
  - printed: "line (69a) (ny_it201.stc_rr_excess)"
    value: "43399.00"
    work: "64999 - 21600"
  - printed: "line (69a) (ny_it201.stc_rr_excess_product)"
    value: "98.95"
    work: "0.228% × 43399"
  - printed: "line (69a) (ny_it201.stc_rr_base)"
    value: "37.00"
    work: "MFJ bracket base"
  - printed: "line (69a) (ny_it201.stc_rr_high)"
    value: "135.95"
    work: "37 + 98.95"
  - printed: "line (69a) (ny_it201.stc_rr)"
    value: "136.00"
    work: "rounded statutory credit"
  - printed: "line 69a"
    value: "136.00"
    work: "37 + 0.228% × (64999 - 21600) = 135.95 → 136"
  - printed: "line 70"
    value: ""
    work: "no federal EIC"
  - printed: "line 70a"
    value: ""
    work: "no dependents; IT-270 not eligible"
  - printed: "line 71"
    value: ""
    work: "no other refundable credits"
  - printed: "line 72"
    value: "0.00"
    work: "IT-2 NYS withholding"
  - printed: "line 73"
    value: "0.00"
    work: "IT-2 NYC withholding"
  - printed: "line 74"
    value: "0.00"
    work: "no Yonkers withholding"
  - printed: "line 76"
    value: "261.00"
    work: "125 + 136 + 0 payments"
  - printed: "line (80)"
    value: "5290.00"
    work: "5551 - 261"
  - printed: "line (81) (ny_it201.prepayments)"
    value: "0.00"
    work: "lines 72-75 = 0"
  - printed: "line (81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% × 2024 tax 0"
  - printed: "line (81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% × 2024 tax 0"
  - printed: "line (81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "prepayments required = 0"
  - printed: "line 81"
    value: ""
    work: "no penalty; prepayments 0 ≥ safe harbor 0"
  - printed: "line 82"
    value: ""
    work: "no late filing/payment penalty or interest"
  - printed: "line (77)"
    value: ""
    work: "line 76 not more than line 62"
  - printed: "line 77"
    value: ""
    work: "no overpayment"
  - printed: "line 78"
    value: ""
    work: "no overpayment"
  - printed: "line 78a"
    value: ""
    work: "no 529 deposit"
  - printed: "line 78b"
    value: ""
    work: "no refund"
  - printed: "line 80"
    value: "5290.00"
    work: "5551 - 261 + 0 penalties"
```
