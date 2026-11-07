# Class M hand-work — ny_it201

`Form IT-201 (2025), Resident Income Tax Return — New York State and New York City` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 401b1c884a45b43c69b6c2a38ede829506c1c50d11f3c1bfb30356cb135b03de |
| cases | 7 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: All others:; Calculation of NYC school tax credit (rate reduction amount) for head of household ④; Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤; Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③; Joint returns; Line 40: New York State household credit; New York City household credit table 4—Filing status ① only (Single); New York City household credit table 5—Filing status ②, ④, and ⑤; New York State household credit table 1—Filing status ① only (Single); New York State household credit table 2—Filing status ②, ④, and ⑤; New York State standard deduction table; Table 1 - Full-year New York City residents: New York City school tax credit table; Tax computation worksheet 1; Tax computation worksheet 10; Tax computation worksheet 12; Tax computation worksheet 13; Tax computation worksheet 14; Tax computation worksheet 15; Tax computation worksheet 2; Tax computation worksheet 3; Tax computation worksheet 4; Tax computation worksheet 5; Tax computation worksheet 6; Tax computation worksheet 7; Tax computation worksheet 8; Tax computation worksheet 9; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it216i | 2025 | 1 | cited pages | aaccbcdb1a41b6e6221e3b0f908cb845e48bb0435b736ce2cd8ed75239deb6ac | 1 | 64200221fb39e0126f8748f9cd859793e2faf9c24c3f4b9a0134ee079251128b |
| ny_it270i | Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit, for tax year 2025 (no printed edition line; address /pdf/2025/inc/, PDF metadata Title '... Tax Year 2025'); PDF modified 2025-10-27 | 1 | whole document | 66b713fa6ae58aafa2189310ed7d140b64c05d2c8bf2958a9651af7751ae15d5 | - | cc437e692bd1fcdbcc44f0e850e95f1cacee9a0e3285396d87e580ca559e082c |

## Lines

### case classm.ny_it201.1 — prompt sha256 d7bfd4d4d4c85d988dd62e4d5d374fbaa5d6bdc3145a65af553f960f87f026f8; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:true, ny_it201.ask.use_tax_st141:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.abode_part_year:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#0, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#0, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#0, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#1, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Work: Given tax table amount

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: NY AGI <= 107650 and TI < 65000, so tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: Tax table on 32000

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,597. The amount is $32,000 (agreed on both sides). The model gave $1,596.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.1 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.1 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **SKIPPED**

Model: blank
Work: AGI over 32000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **SKIPPED**

Model: blank
Work: AGI over 22500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **SKIPPED**

Model: blank
Work: No credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: AGI over 28000, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: AGI over 12500, no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (40) — The state household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: Single uses table 1: no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — (48) — The city household credit table for the filing status
Status: **SKIPPED**

Model: blank
Work: Single uses table 4: no credit

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 40 — NYS household credit
Status: **SKIPPED**

Model: blank
Work: No credit allowed; no entry

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: 1596 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 - 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,597.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $1,597.00
Model: $1,596.00
Work: 1596 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 + 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,597.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 47 — NYC taxable income
Status: **AGREE**

Value: $32,000.00

### classm.ny_it201.1 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: Given NYC tax table amount

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,126. The amount is $32,000 (agreed on both sides). The model gave $1,125.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: NYC TI < 65000, so NYC tax table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 32,000 But less than 32,050", column "Single or Married filing separately": $1,126. The amount is $32,000 (agreed on both sides). The model gave $1,125.00, which is the rate schedule applied to $32,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 48 — NYC household credit
Status: **SKIPPED**

Model: blank
Work: No credit allowed; no entry

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 - 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 - 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: No SE earnings over 50000; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,126.00
Model: $1,125.00
Work: 1125 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1125 + 0 + 0 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,126.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $2,733.00
Model: $2,731.00
Work: 1596 + 1125 + 10 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1596 + 1125 + 10 + 0") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,733.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $2,733.00
Model: $2,731.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,733.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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
Work: 32000 x 0.00171

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.171% of taxable income" on New York City taxable income of $32,000 (a helper of the row this return does not take, line 47 being over $12,000): exactly $54.72, which the project rounds half-up to $55.00; the model's $54.72 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $46.00
Model: $45.60
Work: 20000 x 0.00228

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.228% of the excess over $12,000" on New York City taxable income of $32,000: exactly $45.60, which the project rounds half-up to $46.00; the model's $45.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $21.00

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $67.00
Model: $66.60
Work: 21 + 45.60

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "$21 plus 0.228% of the excess over $12,000" on $32,000 (the 0.228% product rounded where it is computed): exactly $66.60, which the project rounds half-up to $67.00; the model's $66.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $67.00
Model: $66.60
Work: NYC TI over 12000, so high bracket

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", the row over $12,000 but not over $500,000, "$21 plus 0.228% of the excess over $12,000", on $32,000: exactly $66.60, which the project rounds half-up to $67.00; the model's $66.60 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.1 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $67.00

### classm.ny_it201.1 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

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

Ruling: model error, carried: the model's own arithmetic on this line ("2731 - 130") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,603.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.1 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **SKIPPED**

Model: blank
Work: Line 76 is not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.1 — 80 — Amount you owe
Status: **DISAGREE**

Project: $2,603.00
Model: $2,601.00
Work: 2601 + 0 penalty + 0 interest

Ruling: model error, carried: the model's own arithmetic on this line ("2601 + 0 penalty + 0 interest") is the form's, but it starts from its table errors on line 39 ($1,596.00 model, $1,597.00 project) and line 47a ($1,125.00 model, $1,126.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,603.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### case classm.ny_it201.2 — prompt sha256 dd528168e62419a870b3e56e2a3f0a55132657930877abb8c99d56c6359b0aea; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:false, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#1, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#6, ny_it201.hh_city_t5#6, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#5, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:floor, ny_it201.stc_rr_low_band:true, ny_it201.stc_rr#0, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $107,688.00

### classm.ny_it201.2 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Work: Not single with item C Yes

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
Status: **DISAGREE**

Project: $665.00
Model: $666.00
Work: Given: tax table on 16638

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 16,600 But less than 16,650", column "Married filing jointly": $665. The amount is $16,638 (agreed on both sides). The model gave $666.00, which is the rate schedule applied to $16,638 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Line 33 is $107,688, more than $107,650, so this return takes the tax computation worksheet and the helper is off its route; its value is still the table row. Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $665.00
Model: $666.00
Work: Given

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 16,600 But less than 16,650", column "Married filing jointly": $665. The amount is $16,638 (agreed on both sides). The model gave $666.00, which is the rate schedule applied to $16,638 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Line 33 is $107,688, more than $107,650, so this return takes the tax computation worksheet and the helper is off its route; its value is still the table row. Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: NY AGI not over $25,000,000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not single or MFS

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not head of household

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (table 1) — New York State household credit table 1 (single)
Status: **SKIPPED**

Model: blank
Work: Not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (table 4) — New York City household credit table 4 (single)
Status: **SKIPPED**

Model: blank
Work: Not single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 40 — NYS household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **AGREE**

Value: $666.00

### classm.ny_it201.2 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 52 — Add lines 49, 50, and 51
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: No self-employment earnings; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **AGREE**

Value: $512.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project: $19.00
Model: $18.85
Work: 107688 x 0.000175

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $107,688 (the row this return does not take; its chart amount is another row's): exactly $18.8454, which the project rounds half-up to $19.00; the model's $18.85 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.2 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $19.00
Model: $18.85
Work: Smaller of 18.85 or 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $107,688 (the row this return does not take; its chart amount is another row's): exactly $18.8454, which the project rounds half-up to $19.00; the model's $18.85 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $26.00

### classm.ny_it201.2 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **AGREE**

Value: $1,178.00

### classm.ny_it201.2 — 62 — Enter amount from line 61
Status: **AGREE**

Value: $1,178.00

### classm.ny_it201.2 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.171% of taxable income" on New York City taxable income of $16,638: exactly $28.45098, which the project rounds half-up to $28.00; the model's $28.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **SKIPPED**

Model: blank
Work: Taxable income not over 21600

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.2 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $28.00
Model: $28.45
Work: MFJ bracket 0-21600

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", the row over $0 but not over $21,600, "0.171% of taxable income", on $16,638: exactly $28.45098, which the project rounds half-up to $28.00; the model's $28.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.2 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $28.00

### classm.ny_it201.2 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 77 — Amount overpaid
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.2 — 80 — Amount you owe
Status: **AGREE**

Value: $1,025.00

### case classm.ny_it201.3 — prompt sha256 dfcd07e24aedac2689bff05489c1d8b6944c60588e7869bbd30ed7c7ff6518e5; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:true, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:true, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:true, ny_it201.line34#0, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#0, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#0, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#0, ny_it201.line40#0, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#0, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:false, ny_it201.line69#1, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#0, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Work: Given tax table amount for 36900

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: NY AGI is 107650 or less and taxable income is under 65000, so use the tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **DISAGREE**

Project: $4,022.00
Model: $4,022.10
Work: 36900 x 0.109

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." Tax computation worksheets 6, 11 and 16, line 1 times 10.9%, on taxable income (line 38) of $36,900: exactly $4,022.10, which the project rounds half-up to $4,022.00; the model's $4,022.10 is the same amount in cents. Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.3 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not applicable: filing status is Single and NY AGI is 107650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable: NY AGI is 107650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable: filing status is Single

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Not applicable: NY AGI is 107650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: Not applicable: NY AGI is 107650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.3 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: Tax table amount

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,866. The amount is $36,900 (agreed on both sides). The model gave $1,865.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.3 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 1) — New York State household credit table 1 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 40 — NYS household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: 1865 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 - 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,866.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $1,866.00
Model: $1,865.00
Work: 1865 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 + 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,866.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 47 — NYC taxable income
Status: **AGREE**

Value: $36,900.00

### classm.ny_it201.3 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: Given NYC tax table amount

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,313. The amount is $36,900 (agreed on both sides). The model gave $1,312.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: Line 47 under 65000, so NYC tax table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 36,900 But less than 36,950", column "Single or Married filing separately": $1,313. The amount is $36,900 (agreed on both sides). The model gave $1,312.00, which is the rate schedule applied to $36,900 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 48 — NYC household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 - 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 - 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 54a — MCTMT net earnings base for Zone 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 54b — MCTMT net earnings base for Zone 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 54c — MCTMT for Zone 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 54d — MCTMT for Zone 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,313.00
Model: $1,312.00
Work: 1312 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1312 + 0") is the form's, but it starts from its table errors on line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,313.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **AGREE**

Value: $7.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **AGREE**

Value: $7.00

### classm.ny_it201.3 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $10.00

### classm.ny_it201.3 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: 1865 + 1312 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1865 + 1312 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.3 — (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

Value: $63.00

### classm.ny_it201.3 — 69 — NYC school tax credit (fixed amount)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **DISAGREE**

Project: $63.00
Model: $63.10
Work: 36900 x 0.00171

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.171% of taxable income" on New York City taxable income of $36,900 (a helper of the row this return does not take, line 47 being over $12,000): exactly $63.099, which the project rounds half-up to $63.00; the model's $63.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $24,900.00

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $57.00
Model: $56.77
Work: 24900 x 0.00228

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.228% of the excess over $12,000" on New York City taxable income of $36,900: exactly $56.772, which the project rounds half-up to $57.00; the model's $56.77 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $21.00

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $78.00
Model: $77.77
Work: 21 + 56.77

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "$21 plus 0.228% of the excess over $12,000" on $36,900 (the 0.228% product rounded where it is computed): exactly $77.772, which the project rounds half-up to $78.00; the model's $77.77 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $78.00
Model: $77.77
Work: Taxable income over 12000, so use the high bracket

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", the row over $12,000 but not over $500,000, "$21 plus 0.228% of the excess over $12,000", on $36,900: exactly $77.772, which the project rounds half-up to $78.00; the model's $77.77 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.3 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: 3177 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("3177 - 0") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 77 — Amount overpaid
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.3 — 80 — Amount you owe
Status: **DISAGREE**

Project: $3,179.00
Model: $3,177.00
Work: 3177 + 0 penalty + 0 interest

Ruling: model error, carried: the model's own arithmetic on this line ("3177 + 0 penalty + 0 interest") is the form's, but it starts from its table errors on line 39 ($1,865.00 model, $1,866.00 project) and line 47a ($1,312.00 model, $1,313.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,179.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### case classm.ny_it201.4 — prompt sha256 38a10a781be71ad6c4c61646527c86ccd97a39b43655273f180b69522c2af9ab; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#4, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:true, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#2, ny_it201.hh_city_in_range:true, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#2, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#1, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:floor, ny_it201.stc_rr_low_band:true, ny_it201.stc_rr#0, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $20,000.00

### classm.ny_it201.4 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $3,100.00

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
Work: Given amount

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $353.00
Model: $352.00
Work: AGI <= 107650 and taxable income < 65000, so use the table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: Not applicable; AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: Not applicable; AGI <= 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $353.00
Model: $352.00
Work: Tax table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $353. The amount is $8,800 (agreed on both sides). The model gave $352.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $45.00

### classm.ny_it201.4 — (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $60.00

### classm.ny_it201.4 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $293.00
Model: $292.00
Work: 352 - 60

Ruling: model error, carried: the model's own arithmetic on this line ("352 - 60") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project), each ruled model error in this case; with the table amounts the line is the project's $293.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $293.00
Model: $292.00
Work: 292 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("292 + 0") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project), each ruled model error in this case; with the table amounts the line is the project's $293.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 47 — NYC taxable income
Status: **AGREE**

Value: $8,800.00

### classm.ny_it201.4 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $272.00
Model: $271.00
Work: Given amount

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $272. The amount is $8,800 (agreed on both sides). The model gave $271.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $272.00
Model: $271.00
Work: NYC tax table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 8,800 But less than 8,850", column "Head of a household": $272. The amount is $8,800 (agreed on both sides). The model gave $271.00, which is the rate schedule applied to $8,800 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 48 — NYC household credit
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 271 - 15

Ruling: model error, carried: the model's own arithmetic on this line ("271 - 15") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("256 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("256 - 0") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: Self-employment earnings not over 50000; skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $257.00
Model: $256.00
Work: 256 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("256 + 0") is the form's, but it starts from its table errors on line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $257.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Work: 20000 x 0.000175

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $20,000 (the row this return does not take; its chart amount is another row's): exactly $3.50, which the project rounds half-up to $4.00; the model's $3.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.4 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $4.00
Model: $3.50
Work: Smaller of 3.50 or 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $20,000 (the row this return does not take; its chart amount is another row's): exactly $3.50, which the project rounds half-up to $4.00; the model's $3.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $6.00

### classm.ny_it201.4 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $550.00
Model: $548.00
Work: 292 + 256 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("292 + 256 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $550.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $550.00
Model: $548.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $550.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.4 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **SKIPPED**

Model: blank
Work: 8800 is not over 14400

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $15.00

### classm.ny_it201.4 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.4 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

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

Ruling: model error, carried: the model's own arithmetic on this line ("548 - 78") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $472.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Work: Line 76 is not more than line 62

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 77 — Amount overpaid
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **SKIPPED**

Model: blank
Work: No overpayment

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.4 — 80 — Amount you owe
Status: **DISAGREE**

Project: $472.00
Model: $470.00
Work: 470 + 0 penalty + 0 interest

Ruling: model error, carried: the model's own arithmetic on this line ("548 - 78 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($352.00 model, $353.00 project) and line 47a ($271.00 model, $272.00 project), each ruled model error in this case; with the table amounts the line is the project's $472.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### case classm.ny_it201.5 — prompt sha256 c1b66be96615518d07d3e577eda8abfa024dab2f530122455f1fccdc33494c70; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#1, ny_it201.hh_city_t5#1, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#3, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $3,100.00

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
Status: **AGREE**

Value: $4,172.00

### classm.ny_it201.5 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **AGREE**

Value: $1,773.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **AGREE**

Value: $1,773.00

### classm.ny_it201.5 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 52 — Add lines 49, 50, and 51
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **AGREE**

Value: $1,292.00

### classm.ny_it201.5 — 54a — MCTMT net earnings base for Zone 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 54b — MCTMT net earnings base for Zone 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 54c — MCTMT for Zone 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 54d — MCTMT for Zone 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

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
Work: 54,325 x 0.000175

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $54,325 (the row this return does not take; its chart amount is another row's): exactly $9.50688, which the project rounds half-up to $10.00; the model's $9.51 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.5 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $10.00
Model: $9.51
Work: Smaller of 9.51 or 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $54,325 (the row this return does not take; its chart amount is another row's): exactly $9.50688, which the project rounds half-up to $10.00; the model's $9.51 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $15.00

### classm.ny_it201.5 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **AGREE**

Value: $3,065.00

### classm.ny_it201.5 — 62 — Enter amount from line 61
Status: **AGREE**

Value: $3,065.00

### classm.ny_it201.5 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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
Status: **DISAGREE**

Project: $65.00
Model: $65.45
Work: 38,275 x 0.00171

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.171% of taxable income" on New York City taxable income of $38,275 (a helper of the row this return does not take, line 47 being over $21,600): exactly $65.45025, which the project rounds half-up to $65.00; the model's $65.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $16,675.00

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $38.00
Model: $38.02
Work: 16,675 x 0.00228

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.228% of the excess over $21,600" on New York City taxable income of $38,275: exactly $38.019, which the project rounds half-up to $38.00; the model's $38.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $37.00

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $75.00
Model: $75.02
Work: 37 + 38.02

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "$37 plus 0.228% of the excess over $21,600" on $38,275 (the 0.228% product rounded where it is computed): exactly $75.019, which the project rounds half-up to $75.00; the model's $75.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $75.00
Model: $75.02
Work: NYC taxable income over 21,600, so the high formula applies

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", the row over $21,600 but not over $500,000, "$37 plus 0.228% of the excess over $21,600", on $38,275: exactly $75.019, which the project rounds half-up to $75.00; the model's $75.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.5 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $75.00

### classm.ny_it201.5 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $2,865.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 77 — Amount overpaid
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.5 — 80 — Amount you owe
Status: **AGREE**

Value: $2,865.00

### case classm.ny_it201.6 — prompt sha256 5238b9a56d90271c461686f14ad9e979e5789943267fa11496a2352795f48d43; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#3, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#0, ny_it201.hh_city_t5#0, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#4, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#4, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#2, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 9 — Taxable amount of IRA distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 10 — Taxable amount of pensions and annuities
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 12 — Rental real estate included in line 11
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 13 — Farm income or loss
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $3,100.00

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
Work: NYS Tax Table at 40,000 taxable income (given)

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: NY AGI 48,000 is $107,650 or less and taxable income is under 65,000, so use the Tax Table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI is $107,650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI is $107,650 or less

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Not applicable

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: Not applicable; NY AGI is not over 107,650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: Tax Table amount

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $2,037. The amount is $40,000 (agreed on both sides). The model gave $2,036.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $48,000.00

### classm.ny_it201.6 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 1

### classm.ny_it201.6 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 1) — New York State household credit table 1 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 40 — NYS household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: 2,036 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("2036 - 0") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,037.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $2,037.00
Model: $2,036.00
Work: 2,036 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2036 + 0") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,037.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 47 — NYC taxable income
Status: **AGREE**

Value: $40,000.00

### classm.ny_it201.6 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: NYC Tax Table at 40,000 (given)

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $1,432. The amount is $40,000 (agreed on both sides). The model gave $1,431.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: Line 47 is under 65,000, so use the NYC Tax Table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 40,000 But less than 40,050", column "Single or Married filing separately": $1,432. The amount is $40,000 (agreed on both sides). The model gave $1,431.00, which is the rate schedule applied to $40,000 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 48 — NYC household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1431 - 0") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1431 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("1431 - 0") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: No self-employment earnings over 50,000; skip lines 54a-54e

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: Skipped

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $1,432.00
Model: $1,431.00
Work: 1,431 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("1431 + 0") is the form's, but it starts from its table errors on line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $1,432.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Work: 48,000 x 0.000175

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $48,000 (the row this return does not take; its chart amount is another row's): exactly $8.40, which the project rounds half-up to $8.00; the model's $8.40 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.6 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $8.00
Model: $8.40
Work: Smaller of 8.40 or 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 59, Sales and use tax chart, "200,001 and greater | 0.0175% (0.000175) of income, or $125, whichever is smaller", on federal adjusted gross income (line 19) of $48,000 (the row this return does not take; its chart amount is another row's): exactly $8.40, which the project rounds half-up to $8.00; the model's $8.40 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $10.00

### classm.ny_it201.6 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $3,469.00
Model: $3,467.00
Work: 2,036 + 1,431 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2036 + 1431 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,469.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $3,469.00
Model: $3,467.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,469.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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
Work: Not applicable; NYC taxable income is over 12,000

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $28,000.00

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $64.00
Model: $63.84
Work: 28,000 x 0.00228

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "0.228% of the excess over $12,000" on New York City taxable income of $40,000: exactly $63.84, which the project rounds half-up to $64.00; the model's $63.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $21.00

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $85.00
Model: $84.84
Work: 21 + 63.84

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", "$21 plus 0.228% of the excess over $12,000" on $40,000 (the 0.228% product rounded where it is computed): exactly $84.84, which the project rounds half-up to $85.00; the model's $84.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $85.00
Model: $84.84
Work: MFS table, 12,000-500,000 bracket

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③", the row over $12,000 but not over $500,000, "$21 plus 0.228% of the excess over $12,000", on $40,000: exactly $84.84, which the project rounds half-up to $85.00; the model's $84.84 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.6 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $85.00

### classm.ny_it201.6 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 72 — Total New York State tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 73 — Total New York City tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 74 — Total Yonkers tax withheld
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 76 — Total payments (add lines 63 through 75)
Status: **AGREE**

Value: $148.00

### classm.ny_it201.6 — (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project: $3,321.00
Model: $3,319.00
Work: 3,467 - 148

Ruling: model error, carried: the model's own arithmetic on this line ("3467 - 148") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,321.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 77 — Amount overpaid
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.6 — 80 — Amount you owe
Status: **DISAGREE**

Project: $3,321.00
Model: $3,319.00
Work: 3,319 + 0 penalty + 0 interest

Ruling: model error, carried: the model's own arithmetic on this line ("3467 - 148 + 0 penalty + 0") is the form's, but it starts from its table errors on line 39 ($2,036.00 model, $2,037.00 project) and line 47a ($1,431.00 model, $1,432.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,321.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### case classm.ny_it201.7 — prompt sha256 e353ee077070263a6846133d73aea890ca7ea2d94afb1c1612268af269acc75b; branches: ny_it201.ask.state_resident:true, ny_it201.ask.city_resident:true, ny_it201.ask.special_accrual:false, ny_it201.ask.yonkers:false, ny_it201.ask.special_code:false, ny_it201.ask.decedent:false, ny_it201.ask.item_c:false, ny_it201.ask.inflation_check:false, ny_it201.ask.out_of_state_bond_interest:false, ny_it201.ask.414h:false, ny_it201.ask.529_nonqualified:false, ny_it201.ask.it225:false, ny_it201.ask.529_owner:false, ny_it201.ask.itemize:false, ny_it201.ask.resident_credit:false, ny_it201.ask.other_credits:false, ny_it201.ask.other_taxes:false, ny_it201.ask.city_credits:false, ny_it201.ask.owes_use_tax:false, ny_it201.ask.contributions:false, ny_it201.ask.noncustodial:false, ny_it201.ask.real_property_credit:false, ny_it201.ask.college_tuition:false, ny_it201.ask.other_withholding:false, ny_it201.ask.late_penalty:false, ny_it201.ask.prior_agi_high:false, ny_it201.ask.prior_full_year:true, ny_it201.ask.spouse_resident:true, ny_it201.gate.part_year_state:false, ny_it201.gate.part_year_city:false, ny_it201.gate.spouse_nonresident:false, ny_it201.gate.special_accrual:false, ny_it201.gate.yonkers:false, ny_it201.gate.special_code:false, ny_it201.gate.decedent:false, ny_it201.item_c:false, ny_it201.line19_agrees:true, ny_it201.gate.line20:false, ny_it201.gate.line21:false, ny_it201.gate.line22:false, ny_it201.gate.it225:false, ny_it201.gate.line25:false, ny_it201.no:false, ny_it201.has_pension_income:false, ny_it201.gate.line26#1, ny_it201.gate.line26:false, ny_it201.has_line28_income:false, ny_it201.gate.line28#1, ny_it201.gate.line28:false, ny_it201.gate.line29#1, ny_it201.gate.line29:false, ny_it201.gate.line30:false, ny_it201.gate.itemize:false, ny_it201.dependent_single:false, ny_it201.line34#1, ny_it201.line35:positive, ny_it201.line37:positive, ny_it201.agi_table_range:true, ny_it201.ti_table_range:true, ny_it201.tax_low#0, ny_it201.tcw.mfj#0, ny_it201.tcw.single#0, ny_it201.tcw.hoh#0, ny_it201.tcw.by_status#1, ny_it201.agi_top:false, ny_it201.tax_high#1, ny_it201.line39#0, ny_it201.hh_agi:positive, ny_it201.hh_state_t2#1, ny_it201.hh_city_t5#1, ny_it201.hh_state_in_range:false, ny_it201.gate.hh_state_mfs:false, ny_it201.gate.hh_state_over7:false, ny_it201.hh_state_by_status#1, ny_it201.hh_city_in_range:false, ny_it201.gate.hh_city_mfs:false, ny_it201.gate.hh_city_over7:false, ny_it201.hh_city_by_status#1, ny_it201.line40#1, ny_it201.gate.resident_credit:false, ny_it201.gate.other_credits:false, ny_it201.line44:positive, ny_it201.gate.other_taxes:false, ny_it201.city_table_range:true, ny_it201.line47a#0, ny_it201.line48#1, ny_it201.line49:positive, ny_it201.gate.city_credits:false, ny_it201.line54:positive, ny_it201.mctmt_possible:false, ny_it201.gate.mctmt#1, ny_it201.gate.mctmt:false, ny_it201.sut.top:left, ny_it201.sut.chart#4, ny_it201.gate.use_tax_abode:false, ny_it201.gate.use_tax_st141:false, ny_it201.line59#0, ny_it201.gate.contributions:false, ny_it201.gate.child_credit:false, ny_it201.federal_care:false, ny_it201.gate.dependent_care#1, ny_it201.gate.dependent_care:false, ny_it201.gate.eic:false, ny_it201.gate.noncustodial:false, ny_it201.gate.real_property:false, ny_it201.gate.college_tuition:false, ny_it201.stc_fixed_eligible:true, ny_it201.line69#0, ny_it201.gate.stc_rr_income:false, ny_it201.stc_rr_excess:positive, ny_it201.stc_rr_low_band:false, ny_it201.stc_rr#1, ny_it201.line69a#1, ny_it201.gate.it270:false, ny_it201.gate.other_withholding:false, ny_it201.tax_due:positive, ny_it201.safe_harbor#0, ny_it201.gate.estimated_penalty:false, ny_it201.gate.late:false, ny_it201.overpaid_before_penalty:floor, ny_it201.line77:floor, ny_it201.has_overpayment:false, ny_it201.line79#1, ny_it201.gate.line79_over:false, ny_it201.line78:floor, ny_it201.has_refund:false, ny_it201.gate.refund_529#1, ny_it201.gate.refund_529:false, ny_it201.line78b:floor

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 21 — Public employee 414(h) retirement contributions from your wage and tax statement
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 22 — New York’s 529 college savings program distributions
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 23 — Other (Form IT-225, line 9)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 24 — Add lines 19 through 23
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 27 — Taxable amount of Social Security benefits (from line 15)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 28 — Interest income on U.S. government bonds
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 29 — Pension and annuity income exclusion
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 31 — Other (Form IT-225, line 18)
Status: **AGREE**

Value: $0.00

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
Status: **AGREE**

Value: $3,100.00

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
Work: NYS Tax Table, MFJ, 64999

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: Line 33 <= 107650 and line 38 < 65000, so use Tax Table

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.
Status: **SKIPPED**

Model: blank
Work: Not used: NY AGI not over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the ta
Status: **SKIPPED**

Model: blank
Work: Not used: NY AGI not over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **SKIPPED**

Model: blank
Work: Not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **SKIPPED**

Model: blank
Work: Not used

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **SKIPPED**

Model: blank
Work: Not used: NY AGI not over 107650

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: Tax Table amount

Ruling: model error; the 2025 New York State Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $3,241. The amount is $64,999 (agreed on both sides). The model gave $3,242.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 39: "If Yes, find your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table); or if line 38 is $65,000 or more, use the New York State tax rate schedule below." The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negati
Status: **AGREE**

Value: $81,049.00

### classm.ny_it201.7 — (column) — The number of dependents listed in item H, plus one for you (and one for your sp
Status: **AGREE**

Value: 2

### classm.ny_it201.7 — (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 2) — New York State household credit table 2 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 5) — New York City household credit table 5 for the number of people (column 7 for 7
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 1) — New York State household credit table 1 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (40) — The state household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (48) — The city household credit table for the filing status
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 40 — NYS household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 41 — Resident credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 43 — Add lines 40, 41, and 42
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: 3242 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 - 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,241.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project: $3,241.00
Model: $3,242.00
Work: 3242 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 + 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project), each ruled model error in this case; with the table amounts the line is the project's $3,241.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 47 — NYC taxable income
Status: **AGREE**

Value: $64,999.00

### classm.ny_it201.7 — (47a) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: NYC Tax Table (given)

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $2,308. The amount is $64,999 (agreed on both sides). The model gave $2,309.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: Line 47 < 65000, so use NYC Tax Table

Ruling: model error; the 2025 New York City Tax Table (sources/ny/2025/ny_it201_tax_tables), the row "At least 64,950 But less than 65,000", column "Married filing jointly": $2,308. The amount is $64,999 (agreed on both sides). The model gave $2,309.00, which is the rate schedule applied to $64,999 itself (the amount the case gives as the rate-schedule helper), not the table row; the table rows step in $50 bands, so the two differ by a dollar here. IT-201-I (web edition), Line 47a: "NYC taxable income less than $65,000 (line 47) | NYC tax table". The table's own example: "Their taxable income on line 38 is $38,275. First, they find the 38,250 - 38,300 income line. ... The amount shown ... is $1,773." Recomputed from the archived table, not from the engine. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 48 — NYC household credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 - 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 + 0 + 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 - 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 - 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 54a — MCTMT net earnings base for Zone 1
Status: **SKIPPED**

Model: blank
Work: No self-employment earnings; skip lines 54a-54e

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54b — MCTMT net earnings base for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54c — MCTMT for Zone 1
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54d — MCTMT for Zone 2
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 54e — Total MCTMT (add lines 54c and 54d)
Status: **SKIPPED**

Model: blank
Work: Skip

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — 55 — Yonkers resident income tax surcharge
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 5
Status: **DISAGREE**

Project: $2,308.00
Model: $2,309.00
Work: 2309 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("2309 + 0") is the form's, but it starts from its table errors on line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $2,308.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

Value: $3.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

Value: $6.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

Value: $10.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

Value: $15.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

Value: $18.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

Value: $26.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

Value: $34.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project: $14.00
Model: $14.18
Work: 81049 x 0.000175

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." The sales and use tax chart's top row, 0.0175% (0.000175) of income, on federal adjusted gross income (line 19) of $81,049: exactly $14.183575, which the project rounds half-up to $14.00 (under the $125 cap); the model's $14.18 keeps cents. Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

Value: $125.00

### classm.ny_it201.7 — (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **DISAGREE**

Project: $14.00
Model: $14.18
Work: Smaller of 14.18 and 125

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." The sales and use tax chart's top row, 0.0175% (0.000175) of income, on federal adjusted gross income (line 19) of $81,049: exactly $14.183575, which the project rounds half-up to $14.00 (under the $125 cap); the model's $14.18 keeps cents. Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_it201.7 — (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; z
Status: **AGREE**

Value: $18.00

### classm.ny_it201.7 — 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and
Status: **DISAGREE**

Project: $5,549.00
Model: $5,551.00
Work: 3242 + 2309 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("3242 + 2309 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,549.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 62 — Enter amount from line 61
Status: **DISAGREE**

Project: $5,549.00
Model: $5,551.00
Work: From line 61

Ruling: model error, carried: the model's own arithmetic on this line ("From line 61") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,549.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 63 — Empire State child credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 65 — NYS earned income credit (EIC)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 66 — NYS noncustodial parent EIC
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 67 — Real property tax credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 68 — College tuition credit
Status: **AGREE**

Value: $0.00

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
Work: Not used: city taxable income over 21600

No numeric assertion or class M credit: the model left this line blank.

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **AGREE**

Value: $43,399.00

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project: $99.00
Model: $98.95
Work: 43399 x 0.00228

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "0.228% of the excess over $21,600" on New York City taxable income of $64,999: exactly $98.94972, which the project rounds half-up to $99.00; the model's $98.95 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

Value: $37.00

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project: $136.00
Model: $135.95
Work: 37 + 98.95

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", "$37 plus 0.228% of the excess over $21,600" on $64,999 (the 0.228% product rounded where it is computed): exactly $135.94972, which the project rounds half-up to $136.00; the model's $135.95 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project: $136.00
Model: $135.95
Work: MFJ table, 21600-500000 bracket

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Line 69a, "Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤", the row over $21,600 but not over $500,000, "$37 plus 0.228% of the excess over $21,600", on $64,999: exactly $135.94972, which the project rounds half-up to $136.00; the model's $135.95 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries p. 7's "Enter only whole dollar amounts on your New York return." but neither p. 2's rounding rule nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

### classm.ny_it201.7 — 69a — NYC school tax credit (rate reduction amount)
Status: **AGREE**

Value: $136.00

### classm.ny_it201.7 — 70 — NYC earned income credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 70a — NYC income tax elimination credit
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

Value: $0.00

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

Ruling: model error, carried: the model's own arithmetic on this line ("5551 - 261") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,288.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

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
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 82 — Other penalties and interest
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 77 — Amount overpaid
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 79 — Amount of line 77 that you want applied to your 2026 estimated tax
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195,
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **AGREE**

Value: $0.00

### classm.ny_it201.7 — 80 — Amount you owe
Status: **DISAGREE**

Project: $5,288.00
Model: $5,290.00
Work: 5290 + 0 + 0

Ruling: model error, carried: the model's own arithmetic on this line ("5290 + 0 + 0") is the form's, but it starts from its table errors on line 39 ($3,242.00 model, $3,241.00 project) and line 47a ($2,309.00 model, $2,308.00 project), each ruled model error in this case; with the table amounts the line is the project's $5,288.00, and the difference is exactly the carried amount. Dropped from the fixture as not evidence. (Carried over from the previous review of this log, git HEAD: the same case, line, project value and model value. carry.py declined it only because the line's transitive subject changed: the new year parameters ny.false and ny.mctmt.threshold, and for the lines reading lines 54a to 54e or 77 to 79 the new formal gates, none of which changes this value.) [dropped]

## Raw responses

### classm.ny_it201.1

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer cannot be claimed as a dependent"
  - printed: "H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "1"
    value: "40000.00"
    work: "Federal 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal 1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal 1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal 1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "None"
  - printed: "9"
    value: "0.00"
    work: "Federal 1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal 1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "None"
  - printed: "12"
    value: "0.00"
    work: "None"
  - printed: "13"
    value: "0.00"
    work: "None"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal 1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "17"
    value: "40000.00"
    work: "Sum of lines 1-11 and 13-16"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "19"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(check)"
    value: "yes"
    work: "40000 equals federal AGI 40000"
  - printed: "20"
    value: "0.00"
    work: "No other-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No IT-225 additions"
  - printed: "24"
    value: "40000.00"
    work: "40000 + 0"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund check"
  - printed: "26"
    value: "0.00"
    work: "None"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "None"
  - printed: "29"
    value: "0.00"
    work: "No pension income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No IT-225 subtractions"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31"
  - printed: "33"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "Single, item C No"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Table amount for Single, item C Yes"
  - printed: "34"
    value: "8000.00"
    work: "Standard deduction, Single, item C No"
  - printed: "35"
    value: "32000.00"
    work: "40000 - 8000"
  - printed: "36"
    value: "0.00"
    work: "0 x 1000"
  - printed: "37"
    value: "32000.00"
    work: "32000 - 0"
  - printed: "38"
    value: "32000.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "1596.00"
    work: "Given tax table amount"
  - printed: "(39) (ny_it201.tax_low)"
    value: "1596.00"
    work: "NY AGI <= 107650 and TI < 65000, so tax table"
  - printed: "(39) (ny_it201.tcw.top)"
    value: ""
    work: "Not applicable; NY AGI <= 107650"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.single)"
    value: ""
    work: "Not applicable; NY AGI <= 107650"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tax_high)"
    value: ""
    work: "Not applicable; NY AGI <= 107650"
  - printed: "39"
    value: "1596.00"
    work: "Tax table on 32000"
  - printed: "(Note 1)"
    value: "40000.00"
    work: "Line 19"
  - printed: "(column)"
    value: "1"
    work: "0 dependents + 1"
  - printed: "(table 2, column 1)"
    value: ""
    work: "AGI over 32000, no credit"
  - printed: "(table 5, column 1)"
    value: ""
    work: "AGI over 22500, no credit"
  - printed: "(table 2, column 2)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 2)"
    value: ""
    work: "No credit"
  - printed: "(table 2, column 3)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 3)"
    value: ""
    work: "No credit"
  - printed: "(table 2, column 4)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 4)"
    value: ""
    work: "No credit"
  - printed: "(table 2, column 5)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 5)"
    value: ""
    work: "No credit"
  - printed: "(table 2, column 6)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 6)"
    value: ""
    work: "No credit"
  - printed: "(table 2, column 7)"
    value: ""
    work: "No credit"
  - printed: "(table 5, column 7)"
    value: ""
    work: "No credit"
  - printed: "(table 2)"
    value: ""
    work: "No credit"
  - printed: "(table 5)"
    value: ""
    work: "No credit"
  - printed: "(table 1)"
    value: ""
    work: "AGI over 28000, no credit"
  - printed: "(table 4)"
    value: ""
    work: "AGI over 12500, no credit"
  - printed: "(40)"
    value: ""
    work: "Single uses table 1: no credit"
  - printed: "(48)"
    value: ""
    work: "Single uses table 4: no credit"
  - printed: "40"
    value: ""
    work: "No credit allowed; no entry"
  - printed: "41"
    value: "0.00"
    work: "No resident credit"
  - printed: "42"
    value: "0.00"
    work: "No other credits"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "1596.00"
    work: "1596 - 0"
  - printed: "45"
    value: "0.00"
    work: "None"
  - printed: "46"
    value: "1596.00"
    work: "1596 + 0"
  - printed: "47"
    value: "32000.00"
    work: "Line 38 amount (no Charitable Gifts Trust Fund contribution)"
  - printed: "(47a)"
    value: "1125.00"
    work: "Given NYC tax table amount"
  - printed: "47a"
    value: "1125.00"
    work: "NYC TI < 65000, so NYC tax table"
  - printed: "48"
    value: ""
    work: "No credit allowed; no entry"
  - printed: "49"
    value: "1125.00"
    work: "1125 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "None"
  - printed: "52"
    value: "1125.00"
    work: "1125 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "None"
  - printed: "54"
    value: "1125.00"
    work: "1125 - 0"
  - printed: "54a"
    value: ""
    work: "No SE earnings over 50000; skip"
  - printed: "54b"
    value: ""
    work: "Skip"
  - printed: "54c"
    value: ""
    work: "Skip"
  - printed: "54d"
    value: ""
    work: "Skip"
  - printed: "54e"
    value: ""
    work: "Skip"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "Not a part-year Yonkers resident"
  - printed: "58"
    value: "1125.00"
    work: "1125 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "7.00"
    work: "40000 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "7.00"
    work: "Smaller of 7 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "10.00"
    work: "AGI 40000 falls in the 30001-50000 row"
  - printed: "59"
    value: "10.00"
    work: "Chart amount; abode in NY all year"
  - printed: "60"
    value: "0.00"
    work: "No contributions"
  - printed: "61"
    value: "2731.00"
    work: "1596 + 1125 + 10 + 0"
  - printed: "62"
    value: "2731.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child"
  - printed: "64"
    value: "0.00"
    work: "Not eligible"
  - printed: "65"
    value: "0.00"
    work: "Not eligible"
  - printed: "66"
    value: "0.00"
    work: "No support payments"
  - printed: "67"
    value: "0.00"
    work: "Not eligible"
  - printed: "68"
    value: "0.00"
    work: "No tuition"
  - printed: "(69) (ny_it201.stc_income)"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1, Single, income <= 250000"
  - printed: "69"
    value: "63.00"
    work: "Full-year NYC resident, item C No"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: "54.72"
    work: "32000 x 0.00171"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "20000.00"
    work: "32000 - 12000"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "45.60"
    work: "20000 x 0.00228"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "21.00"
    work: "Single bracket base"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "66.60"
    work: "21 + 45.60"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "66.60"
    work: "NYC TI over 12000, so high bracket"
  - printed: "69a"
    value: "67.00"
    work: "66.60 rounded to whole dollars"
  - printed: "70"
    value: "0.00"
    work: "Not eligible"
  - printed: "70a"
    value: "0.00"
    work: "No dependents claimed; not eligible"
  - printed: "71"
    value: "0.00"
    work: "None"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "130.00"
    work: "63 + 67 + 0 (lines 63-75)"
  - printed: "(80)"
    value: "2601.00"
    work: "2731 - 130"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 NY AGI not over 150000, so 100% applies"
  - printed: "81"
    value: "0.00"
    work: "Prepayments 0 >= safe harbor 0; no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not late"
  - printed: "(77)"
    value: ""
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: ""
    work: "No overpayment"
  - printed: "79"
    value: ""
    work: "No overpayment"
  - printed: "78"
    value: ""
    work: "No overpayment"
  - printed: "78a"
    value: ""
    work: "No overpayment"
  - printed: "78b"
    value: ""
    work: "No overpayment"
  - printed: "80"
    value: "2601.00"
    work: "2601 + 0 penalty + 0 interest"
```
```

### classm.ny_it201.2

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer cannot be claimed as a dependent on another return"
  - printed: "H (count)"
    value: "75"
    work: "Dependent entries p1 through p75"
  - printed: "1"
    value: "107688.00"
    work: "Federal 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal 1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal 1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal 1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "No Form 4797 amount"
  - printed: "9"
    value: "0.00"
    work: "Federal 1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal 1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "No Schedule E amount"
  - printed: "12"
    value: "0.00"
    work: "No rental real estate"
  - printed: "13"
    value: "0.00"
    work: "No farm income"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal 1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "17"
    value: "107688.00"
    work: "Sum of lines 1-11 and 13-16"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "19"
    value: "107688.00"
    work: "107688 - 0"
  - printed: "(check)"
    value: "yes"
    work: "Line 19 equals federal AGI of 107688"
  - printed: "20"
    value: "0.00"
    work: "No out-of-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No IT-225 additions"
  - printed: "24"
    value: "107688.00"
    work: "Sum of lines 19-23"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund check"
  - printed: "26"
    value: "0.00"
    work: "No government pensions"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "No U.S. bond interest"
  - printed: "29"
    value: "0.00"
    work: "No pension or annuity income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No IT-225 subtractions"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31"
  - printed: "33"
    value: "107688.00"
    work: "107688 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "Married filing joint return"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "blank"
    work: "Not single with item C Yes"
  - printed: "34"
    value: "16050.00"
    work: "Standard deduction; itemized not larger"
  - printed: "35"
    value: "91638.00"
    work: "107688 - 16050"
  - printed: "36"
    value: "75000.00"
    work: "75 x 1000"
  - printed: "37"
    value: "16638.00"
    work: "91638 - 75000"
  - printed: "38"
    value: "16638.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "666.00"
    work: "Given: tax table on 16638"
  - printed: "(39) (ny_it201.tax_low)"
    value: "666.00"
    work: "Given"
  - printed: "(39) (ny_it201.tcw.top)"
    value: "blank"
    work: "NY AGI not over $25,000,000"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: "666.00"
    work: "Worksheet 1: 665.52 + (915.09 - 665.52) x 0.0008 = 666"
  - printed: "(39) (ny_it201.tcw.single)"
    value: "blank"
    work: "Not single or MFS"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: "blank"
    work: "Not head of household"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: "666.00"
    work: "MFJ worksheet"
  - printed: "(39) (ny_it201.tax_high)"
    value: "666.00"
    work: "NY AGI 107688 > 107650, so tax computation worksheet applies"
  - printed: "39"
    value: "666.00"
    work: "Tax computation worksheet result"
  - printed: "(Note 1)"
    value: "107688.00"
    work: "Line 19; no code A6"
  - printed: "(column)"
    value: "77"
    work: "75 dependents + 2"
  - printed: "(table 2, column 1)"
    value: "0.00"
    work: "FAGI over 32000: no credit"
  - printed: "(table 5, column 1)"
    value: "0.00"
    work: "FAGI over 22500: no credit"
  - printed: "(table 2, column 2)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 2)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 3)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 3)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 4)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 4)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 5)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 5)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 6)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 6)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 7)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 7)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 1)"
    value: "blank"
    work: "Not single"
  - printed: "(table 4)"
    value: "blank"
    work: "Not single"
  - printed: "(40)"
    value: "0.00"
    work: "Table 2 for MFJ: no credit"
  - printed: "(48)"
    value: "0.00"
    work: "Table 5 for MFJ: no credit"
  - printed: "40"
    value: "0.00"
    work: "No household credit"
  - printed: "41"
    value: "0.00"
    work: "No tax paid to other states"
  - printed: "42"
    value: "0.00"
    work: "No other credits"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "666.00"
    work: "666 - 0"
  - printed: "45"
    value: "0.00"
    work: "No other taxes"
  - printed: "46"
    value: "666.00"
    work: "666 + 0"
  - printed: "47"
    value: "16638.00"
    work: "Line 38; no Charitable Gifts Trust Fund contribution"
  - printed: "(47a)"
    value: "512.00"
    work: "Given: NYC tax table"
  - printed: "47a"
    value: "512.00"
    work: "NYC tax on 16638"
  - printed: "48"
    value: "0.00"
    work: "No NYC household credit"
  - printed: "49"
    value: "512.00"
    work: "512 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "None"
  - printed: "52"
    value: "512.00"
    work: "512 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "None"
  - printed: "54"
    value: "512.00"
    work: "512 - 0"
  - printed: "54a"
    value: "blank"
    work: "No self-employment earnings; skip"
  - printed: "54b"
    value: "blank"
    work: "Skip"
  - printed: "54c"
    value: "blank"
    work: "Skip"
  - printed: "54d"
    value: "blank"
    work: "Skip"
  - printed: "54e"
    value: "blank"
    work: "Skip"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "None"
  - printed: "58"
    value: "512.00"
    work: "512 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "18.85"
    work: "107688 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "18.85"
    work: "Smaller of 18.85 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "26.00"
    work: "FAGI in 100,001-150,000 row"
  - printed: "59"
    value: "0.00"
    work: "Filer owes no sales or use tax, so enter 0"
  - printed: "60"
    value: "0.00"
    work: "No contributions"
  - printed: "61"
    value: "1178.00"
    work: "666 + 512 + 0 + 0"
  - printed: "62"
    value: "1178.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No child under 17"
  - printed: "64"
    value: "0.00"
    work: "Not eligible"
  - printed: "65"
    value: "0.00"
    work: "AGI too high for federal EIC"
  - printed: "66"
    value: "0.00"
    work: "No support payments"
  - printed: "67"
    value: "0.00"
    work: "Not eligible"
  - printed: "68"
    value: "0.00"
    work: "No tuition paid"
  - printed: "(69) (ny_it201.stc_income)"
    value: "107688.00"
    work: "107688 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1, MFJ, income <= 250000"
  - printed: "69"
    value: "125.00"
    work: "Full-year NYC residents, MFJ"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: "28.45"
    work: "16638 x 0.00171"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "blank"
    work: "Taxable income not over 21600"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "blank"
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "blank"
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "blank"
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "28.45"
    work: "MFJ bracket 0-21600"
  - printed: "69a"
    value: "28.00"
    work: "28.45 rounded to whole dollars"
  - printed: "70"
    value: "0.00"
    work: "Not EIC eligible"
  - printed: "70a"
    value: "0.00"
    work: "FAGI 107688 > 91902 + 5000; not eligible"
  - printed: "71"
    value: "0.00"
    work: "None"
  - printed: "72"
    value: "0.00"
    work: "IT-2 shows 0"
  - printed: "73"
    value: "0.00"
    work: "IT-2 shows 0"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "153.00"
    work: "125 + 28 + 0 (line 75 = 0)"
  - printed: "(80)"
    value: "1025.00"
    work: "1178 - 153"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 AGI not over 150000, so 100% rule applies"
  - printed: "81"
    value: "0.00"
    work: "Prepayments 0 >= safe harbor 0; no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not late"
  - printed: "(77)"
    value: "0.00"
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: "0.00"
    work: "No overpayment"
  - printed: "79"
    value: "0.00"
    work: "No overpayment"
  - printed: "78"
    value: "0.00"
    work: "0 - 0"
  - printed: "78a"
    value: "0.00"
    work: "None"
  - printed: "78b"
    value: "0.00"
    work: "0 - 0"
  - printed: "80"
    value: "1025.00"
    work: "1178 - 153 + 0 + 0"
```
```

### classm.ny_it201.3

```yaml
```yaml
lines:
  - printed: "C"
    value: "yes"
    work: "Filer can be claimed as a dependent on another taxpayer's federal return"
  - printed: "H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "1"
    value: "40000.00"
    work: "Federal 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal 1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal 1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal 1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "None reported"
  - printed: "9"
    value: "0.00"
    work: "Federal 1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal 1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "None reported"
  - printed: "12"
    value: "0.00"
    work: "None reported"
  - printed: "13"
    value: "0.00"
    work: "None reported"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal 1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "17"
    value: "40000.00"
    work: "Sum of lines 1-11 and 13-16 = 40000"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "19"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(check)"
    value: "yes"
    work: "Line 19 of 40000 equals federal AGI 11a of 40000"
  - printed: "20"
    value: "0.00"
    work: "No out-of-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No IT-225 additions"
  - printed: "24"
    value: "40000.00"
    work: "40000 + 0"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund check included in AGI"
  - printed: "26"
    value: "0.00"
    work: "No government pension"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "No U.S. government bond interest"
  - printed: "29"
    value: "0.00"
    work: "No pension or annuity income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No IT-225 subtractions"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31"
  - printed: "33"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "Single, item C No row = 8000"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Single with item C Yes = 3100"
  - printed: "34"
    value: "3100.00"
    work: "Single, item C Yes, standard deduction (not itemizing)"
  - printed: "35"
    value: "36900.00"
    work: "40000 - 3100"
  - printed: "36"
    value: "0.00"
    work: "0 dependents x 1000"
  - printed: "37"
    value: "36900.00"
    work: "36900 - 0"
  - printed: "38"
    value: "36900.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "1865.00"
    work: "Given tax table amount for 36900"
  - printed: "(39) (ny_it201.tax_low)"
    value: "1865.00"
    work: "NY AGI is 107650 or less and taxable income is under 65000, so use the tax table"
  - printed: "(39) (ny_it201.tcw.top)"
    value: "4022.10"
    work: "36900 x 0.109"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not applicable: filing status is Single and NY AGI is 107650 or less"
  - printed: "(39) (ny_it201.tcw.single)"
    value: ""
    work: "Not applicable: NY AGI is 107650 or less"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not applicable: filing status is Single"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Not applicable: NY AGI is 107650 or less"
  - printed: "(39) (ny_it201.tax_high)"
    value: ""
    work: "Not applicable: NY AGI is 107650 or less"
  - printed: "39"
    value: "1865.00"
    work: "Tax table amount"
  - printed: "(Note 1)"
    value: "40000.00"
    work: "Line 19"
  - printed: "(column)"
    value: "1"
    work: "0 dependents + 1"
  - printed: "(table 2, column 1)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 1)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 2)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 2)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 3)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 3)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 4)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 4)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 5)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 5)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 6)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 6)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2, column 7)"
    value: "0.00"
    work: "AGI over 32000: no credit"
  - printed: "(table 5, column 7)"
    value: "0.00"
    work: "AGI over 22500: no credit"
  - printed: "(table 2)"
    value: "0.00"
    work: "Column 1 = 0"
  - printed: "(table 5)"
    value: "0.00"
    work: "Column 1 = 0"
  - printed: "(table 1)"
    value: "0.00"
    work: "AGI over 28000: no credit"
  - printed: "(table 4)"
    value: "0.00"
    work: "AGI over 12500: no credit"
  - printed: "(40)"
    value: "0.00"
    work: "Single uses table 1 = 0"
  - printed: "(48)"
    value: "0.00"
    work: "Single uses table 4 = 0"
  - printed: "40"
    value: "0.00"
    work: "Item C Yes, so not eligible"
  - printed: "41"
    value: "0.00"
    work: "No tax paid to other jurisdictions"
  - printed: "42"
    value: "0.00"
    work: "No other credits"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "1865.00"
    work: "1865 - 0"
  - printed: "45"
    value: "0.00"
    work: "No other taxes"
  - printed: "46"
    value: "1865.00"
    work: "1865 + 0"
  - printed: "47"
    value: "36900.00"
    work: "No Charitable Gifts Trust Fund contribution, so line 38 amount"
  - printed: "(47a)"
    value: "1312.00"
    work: "Given NYC tax table amount"
  - printed: "47a"
    value: "1312.00"
    work: "Line 47 under 65000, so NYC tax table"
  - printed: "48"
    value: "0.00"
    work: "Item C Yes, so not eligible"
  - printed: "49"
    value: "1312.00"
    work: "1312 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "None"
  - printed: "52"
    value: "1312.00"
    work: "1312 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "None"
  - printed: "54"
    value: "1312.00"
    work: "1312 - 0"
  - printed: "54a"
    value: "0.00"
    work: "No self-employment earnings"
  - printed: "54b"
    value: "0.00"
    work: "No self-employment earnings"
  - printed: "54c"
    value: "0.00"
    work: "0 x 0.006"
  - printed: "54d"
    value: "0.00"
    work: "0 x 0.0034"
  - printed: "54e"
    value: "0.00"
    work: "0 + 0"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "Not a part-year Yonkers resident"
  - printed: "58"
    value: "1312.00"
    work: "1312 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "7.00"
    work: "40000 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "7.00"
    work: "Smaller of 7 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "10.00"
    work: "AGI 40000 falls in 30001-50000 row"
  - printed: "59"
    value: "0.00"
    work: "Filer owes no sales or use tax, so enter 0"
  - printed: "60"
    value: "0.00"
    work: "No contributions"
  - printed: "61"
    value: "3177.00"
    work: "1865 + 1312 + 0 + 0"
  - printed: "62"
    value: "3177.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child"
  - printed: "64"
    value: "0.00"
    work: "No qualifying person"
  - printed: "65"
    value: "0.00"
    work: "Not claimed"
  - printed: "66"
    value: "0.00"
    work: "No child support payments through an SCU"
  - printed: "67"
    value: "0.00"
    work: "Filer does not qualify"
  - printed: "68"
    value: "0.00"
    work: "No tuition paid"
  - printed: "(69) (ny_it201.stc_income)"
    value: "40000.00"
    work: "40000 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1, Single"
  - printed: "69"
    value: "0.00"
    work: "Item C Yes, so not eligible"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: "63.10"
    work: "36900 x 0.00171"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "24900.00"
    work: "36900 - 12000"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "56.77"
    work: "24900 x 0.00228"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "21.00"
    work: "Single bracket base"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "77.77"
    work: "21 + 56.77"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "77.77"
    work: "Taxable income over 12000, so use the high bracket"
  - printed: "69a"
    value: "0.00"
    work: "Item C Yes, so not eligible"
  - printed: "70"
    value: "0.00"
    work: "Not claimed"
  - printed: "70a"
    value: "0.00"
    work: "No dependents, so not eligible"
  - printed: "71"
    value: "0.00"
    work: "None"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding = 0"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding = 0"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "0.00"
    work: "Sum of lines 63-75 = 0"
  - printed: "(80)"
    value: "3177.00"
    work: "3177 - 0"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 AGI not over 150000, so 100% = 0"
  - printed: "81"
    value: "0.00"
    work: "Prepayments of 0 are at least the safe harbor of 0, so no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not filing or paying late"
  - printed: "(77)"
    value: "0.00"
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: "0.00"
    work: "No overpayment"
  - printed: "79"
    value: "0.00"
    work: "No overpayment"
  - printed: "78"
    value: "0.00"
    work: "0 - 0"
  - printed: "78a"
    value: "0.00"
    work: "None"
  - printed: "78b"
    value: "0.00"
    work: "0 - 0"
  - printed: "80"
    value: "3177.00"
    work: "3177 + 0 penalty + 0 interest"
```
```

### classm.ny_it201.4

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer cannot be claimed as a dependent"
  - printed: "H (count)"
    value: "0"
    work: "Parent entry is marked 'Your dependent = no', so no dependents are listed in item H"
  - printed: "1"
    value: "20000.00"
    work: "Federal 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal 1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal 1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal 1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "None"
  - printed: "9"
    value: "0.00"
    work: "Federal 1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal 1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "None"
  - printed: "12"
    value: "0.00"
    work: "None"
  - printed: "13"
    value: "0.00"
    work: "None"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal 1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "17"
    value: "20000.00"
    work: "Sum of lines 1-11 and 13-16"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "19"
    value: "20000.00"
    work: "20000 - 0"
  - printed: "(check)"
    value: "yes"
    work: "Line 19 of 20000 equals federal AGI of 20000"
  - printed: "20"
    value: "0.00"
    work: "Answered no"
  - printed: "21"
    value: "0.00"
    work: "Answered no"
  - printed: "22"
    value: "0.00"
    work: "Answered no"
  - printed: "23"
    value: "0.00"
    work: "No IT-225 entries"
  - printed: "24"
    value: "20000.00"
    work: "Sum of lines 19-23"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund check"
  - printed: "26"
    value: "0.00"
    work: "None"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "None"
  - printed: "29"
    value: "0.00"
    work: "No pension income"
  - printed: "30"
    value: "0.00"
    work: "Answered no"
  - printed: "31"
    value: "0.00"
    work: "No IT-225 entries"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31"
  - printed: "33"
    value: "20000.00"
    work: "20000 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "11200.00"
    work: "Head of household"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Table amount for single, item C Yes"
  - printed: "34"
    value: "11200.00"
    work: "Standard deduction; not itemizing"
  - printed: "35"
    value: "8800.00"
    work: "20000 - 11200"
  - printed: "36"
    value: "0.00"
    work: "0 x 1000"
  - printed: "37"
    value: "8800.00"
    work: "8800 - 0"
  - printed: "38"
    value: "8800.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "352.00"
    work: "Given amount"
  - printed: "(39) (ny_it201.tax_low)"
    value: "352.00"
    work: "AGI <= 107650 and taxable income < 65000, so use the table"
  - printed: "(39) (ny_it201.tcw.top)"
    value: ""
    work: "Not applicable; AGI <= 107650"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.single)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tax_high)"
    value: ""
    work: "Not applicable; AGI <= 107650"
  - printed: "39"
    value: "352.00"
    work: "Tax table"
  - printed: "(Note 1)"
    value: "20000.00"
    work: "Line 19"
  - printed: "(column)"
    value: "1"
    work: "0 dependents + 1"
  - printed: "(table 2, column 1)"
    value: "60.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 1)"
    value: "15.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 2)"
    value: "75.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 2)"
    value: "30.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 3)"
    value: "90.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 3)"
    value: "45.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 4)"
    value: "105.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 4)"
    value: "60.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 5)"
    value: "120.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 5)"
    value: "75.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 6)"
    value: "135.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 6)"
    value: "90.00"
    work: "Row 17500-20000"
  - printed: "(table 2, column 7)"
    value: "150.00"
    work: "Row 7000-20000"
  - printed: "(table 5, column 7)"
    value: "105.00"
    work: "Row 17500-20000"
  - printed: "(table 2)"
    value: "60.00"
    work: "Column 1"
  - printed: "(table 5)"
    value: "15.00"
    work: "Column 1"
  - printed: "(table 1)"
    value: "45.00"
    work: "Row 7000-20000"
  - printed: "(table 4)"
    value: "0.00"
    work: "AGI is over 12500, so no credit"
  - printed: "(40)"
    value: "60.00"
    work: "Head of household uses table 2"
  - printed: "(48)"
    value: "15.00"
    work: "Head of household uses table 5"
  - printed: "40"
    value: "60.00"
    work: "Item C is No"
  - printed: "41"
    value: "0.00"
    work: "Answered no"
  - printed: "42"
    value: "0.00"
    work: "Answered no"
  - printed: "43"
    value: "60.00"
    work: "60 + 0 + 0"
  - printed: "44"
    value: "292.00"
    work: "352 - 60"
  - printed: "45"
    value: "0.00"
    work: "Answered no"
  - printed: "46"
    value: "292.00"
    work: "292 + 0"
  - printed: "47"
    value: "8800.00"
    work: "Line 38; no Charitable Gifts Trust Fund contribution"
  - printed: "(47a)"
    value: "271.00"
    work: "Given amount"
  - printed: "47a"
    value: "271.00"
    work: "NYC tax table"
  - printed: "48"
    value: "15.00"
    work: "Table 5"
  - printed: "49"
    value: "256.00"
    work: "271 - 15"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "None"
  - printed: "52"
    value: "256.00"
    work: "256 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "Answered no"
  - printed: "54"
    value: "256.00"
    work: "256 - 0"
  - printed: "54a"
    value: ""
    work: "Self-employment earnings not over 50000; skip"
  - printed: "54b"
    value: ""
    work: "Skip"
  - printed: "54c"
    value: ""
    work: "Skip"
  - printed: "54d"
    value: ""
    work: "Skip"
  - printed: "54e"
    value: ""
    work: "Skip"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers work"
  - printed: "57"
    value: "0.00"
    work: "Not applicable"
  - printed: "58"
    value: "256.00"
    work: "256 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "3.50"
    work: "20000 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Fixed cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "3.50"
    work: "Smaller of 3.50 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "6.00"
    work: "AGI 20000 falls in the 15001-30000 row"
  - printed: "59"
    value: "0.00"
    work: "Owes no sales or use tax, so enter 0"
  - printed: "60"
    value: "0.00"
    work: "Answered no"
  - printed: "61"
    value: "548.00"
    work: "292 + 256 + 0 + 0"
  - printed: "62"
    value: "548.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child under 17"
  - printed: "64"
    value: "0.00"
    work: "No qualifying care expenses"
  - printed: "65"
    value: "0.00"
    work: "No federal EIC claimed"
  - printed: "66"
    value: "0.00"
    work: "Answered no"
  - printed: "67"
    value: "0.00"
    work: "Answered no"
  - printed: "68"
    value: "0.00"
    work: "Answered no"
  - printed: "(69) (ny_it201.stc_income)"
    value: "20000.00"
    work: "20000 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1, head of household, income <= 250000"
  - printed: "69"
    value: "63.00"
    work: "Full-year NYC resident; item C No"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: "15.00"
    work: "8800 x 0.00171 = 15.05, rounded"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: ""
    work: "8800 is not over 14400"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: ""
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: ""
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: ""
    work: "Not applicable"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "15.00"
    work: "Head of household, low bracket"
  - printed: "69a"
    value: "15.00"
    work: "Rate reduction amount"
  - printed: "70"
    value: "0.00"
    work: "No federal EIC"
  - printed: "70a"
    value: "0.00"
    work: "No dependents claimed in item H"
  - printed: "71"
    value: "0.00"
    work: "Answered no"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "78.00"
    work: "63 + 15"
  - printed: "(80)"
    value: "470.00"
    work: "548 - 78"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% of 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% of 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 AGI not over 150000, so 100%"
  - printed: "81"
    value: "0.00"
    work: "Prepayments of 0 meet the safe harbor of 0"
  - printed: "82"
    value: "0.00"
    work: "Not late"
  - printed: "(77)"
    value: ""
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: ""
    work: "No overpayment"
  - printed: "79"
    value: ""
    work: "No overpayment"
  - printed: "78"
    value: ""
    work: "No overpayment"
  - printed: "78a"
    value: ""
    work: "No overpayment"
  - printed: "78b"
    value: ""
    work: "No overpayment"
  - printed: "80"
    value: "470.00"
    work: "470 + 0 penalty + 0 interest"
```
```

### classm.ny_it201.5

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer answered No: cannot be claimed as a dependent"
  - printed: "H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "1"
    value: "54325.00"
    work: "Federal Form 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal Form 1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal Form 1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal Form 1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "None reported"
  - printed: "9"
    value: "0.00"
    work: "Federal Form 1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal Form 1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "None reported"
  - printed: "12"
    value: "0.00"
    work: "None reported"
  - printed: "13"
    value: "0.00"
    work: "None reported"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal Form 1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1 line 9"
  - printed: "17"
    value: "54325.00"
    work: "Lines 1-11 and 13-16 = 54,325"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1 line 26"
  - printed: "19"
    value: "54325.00"
    work: "54,325 - 0"
  - printed: "(check)"
    value: "yes"
    work: "54,325 = federal AGI (line 11a)"
  - printed: "20"
    value: "0.00"
    work: "No out-of-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No IT-225 additions"
  - printed: "24"
    value: "54325.00"
    work: "54,325 + 0"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund included"
  - printed: "26"
    value: "0.00"
    work: "No government pensions"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "No U.S. bond interest"
  - printed: "29"
    value: "0.00"
    work: "No pension or annuity income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No IT-225 subtractions"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31 = 0"
  - printed: "33"
    value: "54325.00"
    work: "54,325 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "MFJ standard deduction"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Table row: Single, item C Yes"
  - printed: "34"
    value: "16050.00"
    work: "MFJ standard deduction (not itemizing)"
  - printed: "35"
    value: "38275.00"
    work: "54,325 - 16,050"
  - printed: "36"
    value: "0.00"
    work: "0 dependents x 1,000"
  - printed: "37"
    value: "38275.00"
    work: "38,275 - 0"
  - printed: "38"
    value: "38275.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "1773.00"
    work: "NYS Tax Table, MFJ, 38,275 (given)"
  - printed: "(39) (ny_it201.tax_low)"
    value: "1773.00"
    work: "AGI <= 107,650 and TI < 65,000, so Tax Table applies"
  - printed: "(39) (ny_it201.tcw.top)"
    value: "4172.00"
    work: "38,275 x 0.109 = 4,171.98"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: "1773.00"
    work: "Worksheet 1 (TI <= 161,550): line 4 1,773 + line 8 0 (no excess over 107,650)"
  - printed: "(39) (ny_it201.tcw.single)"
    value: "1773.00"
    work: "Worksheet 7 as given (shared computation)"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: "1773.00"
    work: "Worksheet 12 as given (shared computation)"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: "1773.00"
    work: "MFJ worksheet"
  - printed: "(39) (ny_it201.tax_high)"
    value: "1773.00"
    work: "Not used: AGI <= 107,650"
  - printed: "39"
    value: "1773.00"
    work: "Tax Table amount (AGI <= 107,650)"
  - printed: "(Note 1)"
    value: "54325.00"
    work: "Line 19"
  - printed: "(column)"
    value: "2"
    work: "0 dependents + you + spouse"
  - printed: "(table 2, column 1)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 1)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 2)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 2)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 3)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 3)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 4)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 4)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 5)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 5)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 6)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 6)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2, column 7)"
    value: "0.00"
    work: "FAGI over 32,000: no credit"
  - printed: "(table 5, column 7)"
    value: "0.00"
    work: "FAGI over 22,500: no credit"
  - printed: "(table 2)"
    value: "0.00"
    work: "Column 2: no credit"
  - printed: "(table 5)"
    value: "0.00"
    work: "Column 2: no credit"
  - printed: "(table 1)"
    value: "0.00"
    work: "FAGI over 28,000: no credit"
  - printed: "(table 4)"
    value: "0.00"
    work: "FAGI over 12,500: no credit"
  - printed: "(40)"
    value: "0.00"
    work: "MFJ uses table 2 = 0"
  - printed: "(48)"
    value: "0.00"
    work: "MFJ uses table 5 = 0"
  - printed: "40"
    value: "0.00"
    work: "No NYS household credit allowed"
  - printed: "41"
    value: "0.00"
    work: "No tax paid to another state"
  - printed: "42"
    value: "0.00"
    work: "No other credits"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "1773.00"
    work: "1,773 - 0"
  - printed: "45"
    value: "0.00"
    work: "No other NYS taxes"
  - printed: "46"
    value: "1773.00"
    work: "1,773 + 0"
  - printed: "47"
    value: "38275.00"
    work: "Line 38 amount (no Charitable Gifts Trust Fund)"
  - printed: "(47a)"
    value: "1292.00"
    work: "NYC Tax Table on 38,275 (given)"
  - printed: "47a"
    value: "1292.00"
    work: "Line 47 < 65,000, so NYC Tax Table applies"
  - printed: "48"
    value: "0.00"
    work: "FAGI over 22,500: no NYC household credit"
  - printed: "49"
    value: "1292.00"
    work: "1,292 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC residents"
  - printed: "51"
    value: "0.00"
    work: "No other NYC taxes"
  - printed: "52"
    value: "1292.00"
    work: "1,292 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "No NYC nonrefundable credits"
  - printed: "54"
    value: "1292.00"
    work: "1,292 - 0"
  - printed: "54a"
    value: "0.00"
    work: "No self-employment earnings over 50,000"
  - printed: "54b"
    value: "0.00"
    work: "No self-employment earnings over 50,000"
  - printed: "54c"
    value: "0.00"
    work: "0 x 0.0060"
  - printed: "54d"
    value: "0.00"
    work: "0 x 0.0034"
  - printed: "54e"
    value: "0.00"
    work: "0 + 0"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "Not a part-year Yonkers resident"
  - printed: "58"
    value: "1292.00"
    work: "1,292 + 0 + 0 + 0 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row: up to 15,000"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row: 15,001-30,000"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row: 30,001-50,000"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row: 50,001-75,000"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row: 75,001-100,000"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row: 100,001-150,000"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row: 150,001-200,000"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "9.51"
    work: "54,325 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "9.51"
    work: "Smaller of 9.51 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "15.00"
    work: "FAGI 54,325 is in the 50,001-75,000 row"
  - printed: "59"
    value: "0.00"
    work: "Filer owes no sales or use tax; enter 0"
  - printed: "60"
    value: "0.00"
    work: "No voluntary contributions"
  - printed: "61"
    value: "3065.00"
    work: "1,773 + 1,292 + 0 + 0"
  - printed: "62"
    value: "3065.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child"
  - printed: "64"
    value: "0.00"
    work: "No qualifying care expenses"
  - printed: "65"
    value: "0.00"
    work: "No federal EIC"
  - printed: "66"
    value: "0.00"
    work: "No child support paid through a Support Collection Unit"
  - printed: "67"
    value: "0.00"
    work: "Does not qualify"
  - printed: "68"
    value: "0.00"
    work: "No tuition paid"
  - printed: "(69) (ny_it201.stc_income)"
    value: "54325.00"
    work: "54,325 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1, MFJ, income <= 250,000"
  - printed: "69"
    value: "125.00"
    work: "Both spouses full-year NYC residents, item C No"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: "65.45"
    work: "38,275 x 0.00171"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "16675.00"
    work: "38,275 - 21,600"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "38.02"
    work: "16,675 x 0.00228"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "37.00"
    work: "MFJ base amount"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "75.02"
    work: "37 + 38.02"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "75.02"
    work: "NYC taxable income over 21,600, so the high formula applies"
  - printed: "69a"
    value: "75.00"
    work: "75.02 rounded to whole dollars"
  - printed: "70"
    value: "0.00"
    work: "No federal EIC"
  - printed: "70a"
    value: "0.00"
    work: "No dependents claimed; not eligible"
  - printed: "71"
    value: "0.00"
    work: "No other refundable credits"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding total"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding total"
  - printed: "74"
    value: "0.00"
    work: "No Yonkers withholding"
  - printed: "76"
    value: "200.00"
    work: "125 + 75 + 0 (line 75 = 0)"
  - printed: "(80)"
    value: "2865.00"
    work: "3,065 - 200"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "Withholding 0 + estimated payments 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 2024 tax of 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 NYAGI <= 150,000, so 100% applies"
  - printed: "81"
    value: "0.00"
    work: "Prepayments 0 >= safe harbor 0; no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not filing or paying late"
  - printed: "(77)"
    value: "0.00"
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: "0.00"
    work: "No overpayment"
  - printed: "79"
    value: "0.00"
    work: "No overpayment"
  - printed: "78"
    value: "0.00"
    work: "0 - 0"
  - printed: "78a"
    value: "0.00"
    work: "None"
  - printed: "78b"
    value: "0.00"
    work: "0 - 0"
  - printed: "80"
    value: "2865.00"
    work: "2,865 + penalty 0 + other 0"
```
```

### classm.ny_it201.6

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer cannot be claimed as a dependent on another taxpayer's return"
  - printed: "H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "1"
    value: "48000.00"
    work: "Federal Form 1040, line 1z"
  - printed: "2"
    value: "0.00"
    work: "Federal Form 1040, line 2b"
  - printed: "3"
    value: "0.00"
    work: "Federal Form 1040, line 3b"
  - printed: "4"
    value: "0.00"
    work: "Schedule 1, line 1"
  - printed: "5"
    value: "0.00"
    work: "Schedule 1, line 2a"
  - printed: "6"
    value: "0.00"
    work: "Schedule 1, line 3"
  - printed: "7"
    value: "0.00"
    work: "Federal Form 1040, line 7a"
  - printed: "8"
    value: "0.00"
    work: "None reported"
  - printed: "9"
    value: "0.00"
    work: "Federal Form 1040, line 4b"
  - printed: "10"
    value: "0.00"
    work: "Federal Form 1040, line 5b"
  - printed: "11"
    value: "0.00"
    work: "None reported"
  - printed: "12"
    value: "0.00"
    work: "None reported"
  - printed: "13"
    value: "0.00"
    work: "None reported"
  - printed: "14"
    value: "0.00"
    work: "Schedule 1, line 7"
  - printed: "15"
    value: "0.00"
    work: "Federal Form 1040, line 6b"
  - printed: "16"
    value: "0.00"
    work: "Schedule 1, line 9"
  - printed: "17"
    value: "48000.00"
    work: "Lines 1-11 + lines 13-16 = 48,000"
  - printed: "18"
    value: "0.00"
    work: "Schedule 1, line 26"
  - printed: "19"
    value: "48000.00"
    work: "48,000 - 0"
  - printed: "(check)"
    value: "yes"
    work: "Line 19 of 48,000 equals federal AGI of 48,000"
  - printed: "20"
    value: "0.00"
    work: "No out-of-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No Form IT-225 additions"
  - printed: "24"
    value: "48000.00"
    work: "Lines 19 through 23"
  - printed: "25"
    value: "0.00"
    work: "No inflation refund included"
  - printed: "26"
    value: "0.00"
    work: "No government pension"
  - printed: "27"
    value: "0.00"
    work: "From line 15"
  - printed: "28"
    value: "0.00"
    work: "No U.S. bond interest"
  - printed: "29"
    value: "0.00"
    work: "No pension or annuity income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No Form IT-225 subtractions"
  - printed: "32"
    value: "0.00"
    work: "Lines 25 through 31"
  - printed: "33"
    value: "48000.00"
    work: "48,000 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "8000.00"
    work: "Married filing separate return amount from the standard deduction table"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Table amount for Single with item C Yes; not used here"
  - printed: "34"
    value: "8000.00"
    work: "Standard deduction; filer does not itemize"
  - printed: "35"
    value: "40000.00"
    work: "48,000 - 8,000"
  - printed: "36"
    value: "0.00"
    work: "0 dependents x 1,000"
  - printed: "37"
    value: "40000.00"
    work: "40,000 - 0"
  - printed: "38"
    value: "40000.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "2036.00"
    work: "NYS Tax Table at 40,000 taxable income (given)"
  - printed: "(39) (ny_it201.tax_low)"
    value: "2036.00"
    work: "NY AGI 48,000 is $107,650 or less and taxable income is under 65,000, so use the Tax Table"
  - printed: "(39) (ny_it201.tcw.top)"
    value: ""
    work: "Not applicable; NY AGI is $107,650 or less"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.single)"
    value: ""
    work: "Not applicable; NY AGI is $107,650 or less"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Not applicable"
  - printed: "(39) (ny_it201.tax_high)"
    value: ""
    work: "Not applicable; NY AGI is not over 107,650"
  - printed: "39"
    value: "2036.00"
    work: "Tax Table amount"
  - printed: "(Note 1)"
    value: "48000.00"
    work: "Line 19; no code A6 entered"
  - printed: "(column)"
    value: "1"
    work: "0 dependents + 1 for you"
  - printed: "(table 2, column 1)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 1)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 2)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 2)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 3)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 3)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 4)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 4)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 5)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 5)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 6)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 6)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2, column 7)"
    value: "0.00"
    work: "AGI over 32,000; no credit"
  - printed: "(table 5, column 7)"
    value: "0.00"
    work: "AGI over 22,500; no credit"
  - printed: "(table 2)"
    value: "0.00"
    work: "Column 1; no credit"
  - printed: "(table 5)"
    value: "0.00"
    work: "Column 1; no credit"
  - printed: "(table 1)"
    value: "0.00"
    work: "AGI over 28,000; no credit"
  - printed: "(table 4)"
    value: "0.00"
    work: "AGI over 12,500; no credit"
  - printed: "(40)"
    value: "0.00"
    work: "Table 3 (MFS): own AGI 48,000 alone exceeds 32,000, so combined AGI does too; no credit"
  - printed: "(48)"
    value: "0.00"
    work: "Table 6 (MFS): own AGI 48,000 alone exceeds 22,500, so combined AGI does too; no credit"
  - printed: "40"
    value: "0.00"
    work: "No NYS household credit allowed"
  - printed: "41"
    value: "0.00"
    work: "No tax paid to another state"
  - printed: "42"
    value: "0.00"
    work: "No other nonrefundable credits"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "2036.00"
    work: "2,036 - 0"
  - printed: "45"
    value: "0.00"
    work: "No other NYS taxes"
  - printed: "46"
    value: "2036.00"
    work: "2,036 + 0"
  - printed: "47"
    value: "40000.00"
    work: "Line 38 amount; no Charitable Gifts Trust Fund deduction"
  - printed: "(47a)"
    value: "1431.00"
    work: "NYC Tax Table at 40,000 (given)"
  - printed: "47a"
    value: "1431.00"
    work: "Line 47 is under 65,000, so use the NYC Tax Table"
  - printed: "48"
    value: "0.00"
    work: "No NYC household credit allowed"
  - printed: "49"
    value: "1431.00"
    work: "1,431 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "No other NYC taxes"
  - printed: "52"
    value: "1431.00"
    work: "1,431 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "No NYC nonrefundable credits"
  - printed: "54"
    value: "1431.00"
    work: "1,431 - 0"
  - printed: "54a"
    value: ""
    work: "No self-employment earnings over 50,000; skip lines 54a-54e"
  - printed: "54b"
    value: ""
    work: "Skipped"
  - printed: "54c"
    value: ""
    work: "Skipped"
  - printed: "54d"
    value: ""
    work: "Skipped"
  - printed: "54e"
    value: ""
    work: "Skipped"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "Not a part-year Yonkers resident"
  - printed: "58"
    value: "1431.00"
    work: "1,431 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "8.40"
    work: "48,000 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Fixed cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "8.40"
    work: "Smaller of 8.40 or 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "10.00"
    work: "AGI 48,000 falls in the 30,001-50,000 row"
  - printed: "59"
    value: "0.00"
    work: "Filer owes no sales or use tax, so enter 0"
  - printed: "60"
    value: "0.00"
    work: "No voluntary contributions"
  - printed: "61"
    value: "3467.00"
    work: "2,036 + 1,431 + 0 + 0"
  - printed: "62"
    value: "3467.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child"
  - printed: "64"
    value: "0.00"
    work: "No dependent care"
  - printed: "65"
    value: "0.00"
    work: "Not claimed"
  - printed: "66"
    value: "0.00"
    work: "No child support paid through a Support Collection Unit"
  - printed: "67"
    value: "0.00"
    work: "Does not qualify"
  - printed: "68"
    value: "0.00"
    work: "No college tuition paid"
  - printed: "(69) (ny_it201.stc_income)"
    value: "48000.00"
    work: "48,000 - 0 IRA distributions"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "63.00"
    work: "Table 1, MFS, income $250,000 or less"
  - printed: "69"
    value: "63.00"
    work: "Full-year NYC resident, item C No"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "Not applicable; NYC taxable income is over 12,000"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "28000.00"
    work: "40,000 - 12,000"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "63.84"
    work: "28,000 x 0.00228"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "21.00"
    work: "Single/MFS base amount"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "84.84"
    work: "21 + 63.84"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "84.84"
    work: "MFS table, 12,000-500,000 bracket"
  - printed: "69a"
    value: "85.00"
    work: "84.84 rounded to whole dollars"
  - printed: "70"
    value: "0.00"
    work: "Not claimed"
  - printed: "70a"
    value: "0.00"
    work: "No dependents claimed, so not eligible"
  - printed: "71"
    value: "0.00"
    work: "No other refundable credits"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding of 0"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding of 0"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "148.00"
    work: "63 + 85 + 0 (estimated payments on line 75 are 0)"
  - printed: "(80)"
    value: "3319.00"
    work: "3,467 - 148"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 NY AGI not over 75,000, so 100% applies"
  - printed: "81"
    value: "0.00"
    work: "Prepayments of 0 meet the safe harbor of 0; no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not filing or paying late"
  - printed: "(77)"
    value: "0.00"
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: "0.00"
    work: "No overpayment"
  - printed: "79"
    value: "0.00"
    work: "No overpayment to apply"
  - printed: "78"
    value: "0.00"
    work: "0 - 0"
  - printed: "78a"
    value: "0.00"
    work: "None"
  - printed: "78b"
    value: "0.00"
    work: "0 - 0"
  - printed: "80"
    value: "3319.00"
    work: "3,319 + 0 penalty + 0 interest"
```
```

### classm.ny_it201.7

```yaml
```yaml
lines:
  - printed: "C"
    value: "no"
    work: "Filer cannot be claimed as a dependent"
  - printed: "H (count)"
    value: "0"
    work: "No dependents listed"
  - printed: "1"
    value: "81049.00"
    work: "Federal 1040 line 1z"
  - printed: "2"
    value: "0.00"
    work: "1040 line 2b"
  - printed: "3"
    value: "0.00"
    work: "1040 line 3b"
  - printed: "4"
    value: "0.00"
    work: "Sch 1 line 1"
  - printed: "5"
    value: "0.00"
    work: "Sch 1 line 2a"
  - printed: "6"
    value: "0.00"
    work: "Sch 1 line 3"
  - printed: "7"
    value: "0.00"
    work: "1040 line 7a"
  - printed: "8"
    value: "0.00"
    work: "None"
  - printed: "9"
    value: "0.00"
    work: "1040 line 4b"
  - printed: "10"
    value: "0.00"
    work: "1040 line 5b"
  - printed: "11"
    value: "0.00"
    work: "None"
  - printed: "12"
    value: "0.00"
    work: "None"
  - printed: "13"
    value: "0.00"
    work: "None"
  - printed: "14"
    value: "0.00"
    work: "Sch 1 line 7"
  - printed: "15"
    value: "0.00"
    work: "1040 line 6b"
  - printed: "16"
    value: "0.00"
    work: "Sch 1 line 9"
  - printed: "17"
    value: "81049.00"
    work: "Sum of lines 1-11 and 13-16"
  - printed: "18"
    value: "0.00"
    work: "Sch 1 line 26"
  - printed: "19"
    value: "81049.00"
    work: "81049 - 0"
  - printed: "(check)"
    value: "yes"
    work: "Equals federal AGI 81049 (1040 line 11a)"
  - printed: "20"
    value: "0.00"
    work: "No out-of-state bond interest"
  - printed: "21"
    value: "0.00"
    work: "Not a public employee"
  - printed: "22"
    value: "0.00"
    work: "No nonqualified 529 withdrawal"
  - printed: "23"
    value: "0.00"
    work: "No IT-225"
  - printed: "24"
    value: "81049.00"
    work: "Sum of lines 19-23"
  - printed: "25"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "26"
    value: "0.00"
    work: "None"
  - printed: "27"
    value: "0.00"
    work: "Line 15 is 0"
  - printed: "28"
    value: "0.00"
    work: "None"
  - printed: "29"
    value: "0.00"
    work: "No pension income"
  - printed: "30"
    value: "0.00"
    work: "No 529 activity"
  - printed: "31"
    value: "0.00"
    work: "No IT-225"
  - printed: "32"
    value: "0.00"
    work: "Sum of lines 25-31"
  - printed: "33"
    value: "81049.00"
    work: "81049 - 0"
  - printed: "(table) (ny_it201.std_deduction)"
    value: "16050.00"
    work: "Married filing jointly"
  - printed: "(table) (ny_it201.std_deduction_dependent)"
    value: "3100.00"
    work: "Table entry for single with item C Yes"
  - printed: "34"
    value: "16050.00"
    work: "Standard deduction (not itemizing)"
  - printed: "35"
    value: "64999.00"
    work: "81049 - 16050"
  - printed: "36"
    value: "0.00"
    work: "0 x 1000"
  - printed: "37"
    value: "64999.00"
    work: "64999 - 0"
  - printed: "38"
    value: "64999.00"
    work: "From line 37"
  - printed: "(39) (ny_it201.tax_table)"
    value: "3242.00"
    work: "NYS Tax Table, MFJ, 64999"
  - printed: "(39) (ny_it201.tax_low)"
    value: "3242.00"
    work: "Line 33 <= 107650 and line 38 < 65000, so use Tax Table"
  - printed: "(39) (ny_it201.tcw.top)"
    value: ""
    work: "Not used: NY AGI not over 107650"
  - printed: "(39) (ny_it201.tcw.mfj)"
    value: ""
    work: "Not used: NY AGI not over 107650"
  - printed: "(39) (ny_it201.tcw.single)"
    value: ""
    work: "Not used"
  - printed: "(39) (ny_it201.tcw.hoh)"
    value: ""
    work: "Not used"
  - printed: "(39) (ny_it201.tcw.by_status)"
    value: ""
    work: "Not used"
  - printed: "(39) (ny_it201.tax_high)"
    value: ""
    work: "Not used: NY AGI not over 107650"
  - printed: "39"
    value: "3242.00"
    work: "Tax Table amount"
  - printed: "(Note 1)"
    value: "81049.00"
    work: "Line 19"
  - printed: "(column)"
    value: "2"
    work: "0 dependents + you + spouse"
  - printed: "(table 2, column 1)"
    value: "0.00"
    work: "FAGI over 32000: no credit"
  - printed: "(table 5, column 1)"
    value: "0.00"
    work: "FAGI over 22500: no credit"
  - printed: "(table 2, column 2)"
    value: "0.00"
    work: "FAGI over 32000: no credit"
  - printed: "(table 5, column 2)"
    value: "0.00"
    work: "FAGI over 22500: no credit"
  - printed: "(table 2, column 3)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 3)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 4)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 4)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 5)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 5)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 6)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 6)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2, column 7)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 5, column 7)"
    value: "0.00"
    work: "No credit"
  - printed: "(table 2)"
    value: "0.00"
    work: "Column 2: no credit"
  - printed: "(table 5)"
    value: "0.00"
    work: "Column 2: no credit"
  - printed: "(table 1)"
    value: "0.00"
    work: "FAGI over 28000: no credit"
  - printed: "(table 4)"
    value: "0.00"
    work: "FAGI over 12500: no credit"
  - printed: "(40)"
    value: "0.00"
    work: "MFJ uses table 2"
  - printed: "(48)"
    value: "0.00"
    work: "MFJ uses table 5"
  - printed: "40"
    value: "0.00"
    work: "No household credit"
  - printed: "41"
    value: "0.00"
    work: "No tax paid to another state"
  - printed: "42"
    value: "0.00"
    work: "None"
  - printed: "43"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "44"
    value: "3242.00"
    work: "3242 - 0"
  - printed: "45"
    value: "0.00"
    work: "None"
  - printed: "46"
    value: "3242.00"
    work: "3242 + 0"
  - printed: "47"
    value: "64999.00"
    work: "Line 38 amount (no Charitable Gifts Trust Fund contribution)"
  - printed: "(47a)"
    value: "2309.00"
    work: "NYC Tax Table (given)"
  - printed: "47a"
    value: "2309.00"
    work: "Line 47 < 65000, so use NYC Tax Table"
  - printed: "48"
    value: "0.00"
    work: "No NYC household credit"
  - printed: "49"
    value: "2309.00"
    work: "2309 - 0"
  - printed: "50"
    value: "0.00"
    work: "Full-year NYC resident"
  - printed: "51"
    value: "0.00"
    work: "None"
  - printed: "52"
    value: "2309.00"
    work: "2309 + 0 + 0"
  - printed: "53"
    value: "0.00"
    work: "None"
  - printed: "54"
    value: "2309.00"
    work: "2309 - 0"
  - printed: "54a"
    value: ""
    work: "No self-employment earnings; skip lines 54a-54e"
  - printed: "54b"
    value: ""
    work: "Skip"
  - printed: "54c"
    value: ""
    work: "Skip"
  - printed: "54d"
    value: ""
    work: "Skip"
  - printed: "54e"
    value: ""
    work: "Skip"
  - printed: "55"
    value: "0.00"
    work: "Not a Yonkers resident"
  - printed: "56"
    value: "0.00"
    work: "No Yonkers wages"
  - printed: "57"
    value: "0.00"
    work: "Not applicable"
  - printed: "58"
    value: "2309.00"
    work: "2309 + 0"
  - printed: "(chart) (ny_it201.sut.b1)"
    value: "3.00"
    work: "Chart row 1"
  - printed: "(chart) (ny_it201.sut.b2)"
    value: "6.00"
    work: "Chart row 2"
  - printed: "(chart) (ny_it201.sut.b3)"
    value: "10.00"
    work: "Chart row 3"
  - printed: "(chart) (ny_it201.sut.b4)"
    value: "15.00"
    work: "Chart row 4"
  - printed: "(chart) (ny_it201.sut.b5)"
    value: "18.00"
    work: "Chart row 5"
  - printed: "(chart) (ny_it201.sut.b6)"
    value: "26.00"
    work: "Chart row 6"
  - printed: "(chart) (ny_it201.sut.b7)"
    value: "34.00"
    work: "Chart row 7"
  - printed: "(chart) (ny_it201.sut.top_product)"
    value: "14.18"
    work: "81049 x 0.000175"
  - printed: "(chart) (ny_it201.sut.cap)"
    value: "125.00"
    work: "Cap"
  - printed: "(chart) (ny_it201.sut.top)"
    value: "14.18"
    work: "Smaller of 14.18 and 125"
  - printed: "(chart) (ny_it201.sut.chart)"
    value: "18.00"
    work: "FAGI 81049 falls in 75001-100000 row"
  - printed: "59"
    value: "0.00"
    work: "No sales or use tax owed; enter 0"
  - printed: "60"
    value: "0.00"
    work: "No contributions"
  - printed: "61"
    value: "5551.00"
    work: "3242 + 2309 + 0 + 0"
  - printed: "62"
    value: "5551.00"
    work: "From line 61"
  - printed: "63"
    value: "0.00"
    work: "No qualifying child"
  - printed: "64"
    value: "0.00"
    work: "Not eligible"
  - printed: "65"
    value: "0.00"
    work: "Not eligible"
  - printed: "66"
    value: "0.00"
    work: "No child support payments"
  - printed: "67"
    value: "0.00"
    work: "Not eligible"
  - printed: "68"
    value: "0.00"
    work: "No tuition paid"
  - printed: "(69) (ny_it201.stc_income)"
    value: "81049.00"
    work: "81049 - 0"
  - printed: "(69) (ny_it201.stc_fixed_amount)"
    value: "125.00"
    work: "Table 1, MFJ, income <= 250000"
  - printed: "69"
    value: "125.00"
    work: "Full-year NYC residents, MFJ"
  - printed: "(69a) (ny_it201.stc_rr_low)"
    value: ""
    work: "Not used: city taxable income over 21600"
  - printed: "(69a) (ny_it201.stc_rr_excess)"
    value: "43399.00"
    work: "64999 - 21600"
  - printed: "(69a) (ny_it201.stc_rr_excess_product)"
    value: "98.95"
    work: "43399 x 0.00228"
  - printed: "(69a) (ny_it201.stc_rr_base)"
    value: "37.00"
    work: "MFJ base amount"
  - printed: "(69a) (ny_it201.stc_rr_high)"
    value: "135.95"
    work: "37 + 98.95"
  - printed: "(69a) (ny_it201.stc_rr)"
    value: "135.95"
    work: "MFJ table, 21600-500000 bracket"
  - printed: "69a"
    value: "136.00"
    work: "135.95 rounded to whole dollars"
  - printed: "70"
    value: "0.00"
    work: "Not eligible"
  - printed: "70a"
    value: "0.00"
    work: "No dependents; not eligible"
  - printed: "71"
    value: "0.00"
    work: "None"
  - printed: "72"
    value: "0.00"
    work: "IT-2 NYS withholding is 0"
  - printed: "73"
    value: "0.00"
    work: "IT-2 NYC withholding is 0"
  - printed: "74"
    value: "0.00"
    work: "None"
  - printed: "76"
    value: "261.00"
    work: "125 + 136"
  - printed: "(80)"
    value: "5290.00"
    work: "5551 - 261"
  - printed: "(81) (ny_it201.prepayments)"
    value: "0.00"
    work: "0 + 0 + 0 + 0"
  - printed: "(81) (ny_it201.safe_harbor_100)"
    value: "0.00"
    work: "100% x 0"
  - printed: "(81) (ny_it201.safe_harbor_110)"
    value: "0.00"
    work: "110% x 0"
  - printed: "(81) (ny_it201.safe_harbor)"
    value: "0.00"
    work: "2024 NY AGI not over 150000, so 100% applies"
  - printed: "81"
    value: "0.00"
    work: "Prepayments 0 >= required 0; no penalty"
  - printed: "82"
    value: "0.00"
    work: "Not late"
  - printed: "(77)"
    value: "0.00"
    work: "Line 76 is not more than line 62"
  - printed: "77"
    value: "0.00"
    work: "No overpayment"
  - printed: "79"
    value: "0.00"
    work: "None"
  - printed: "78"
    value: "0.00"
    work: "0 - 0"
  - printed: "78a"
    value: "0.00"
    work: "None"
  - printed: "78b"
    value: "0.00"
    work: "0 - 0"
  - printed: "80"
    value: "5290.00"
    work: "5290 + 0 + 0"
```
```
