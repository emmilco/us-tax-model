# Schedule A — supported itemized deductions and standard comparison

- Document: `sa` (form, tax year 2025)
- Note: Income and deduction eligibility are explicit supplied facts. Charity valuation, substantiation and income-limit screening are not computed; an affirmative limitation answer is refused. The SALT formula follows the printed 2025 worksheet, including its MFS halving step.

## (helper) — `sa.unsupported`

- **Authored helper label:** A Schedule A item this tool does not compute: mortgage interest or points not on Form 1098 or subject to the debt or use limits; the sales-tax election; a foreign tax deduction; or a deduction from the Schedule A line 16 list other than gambling losses
- **Encoded (Bool):** (helper "Asked only where it can apply (sa.mortgage_unreported)" = true or helper "The home mortgage debt is over the limit for the filing status ($750,000 or $1,000,000; $375,000 or $500,000 if married filing separately) or over the home's value (no when no mortgage interest was paid)" = true or helper "Asked only where it can apply (sa.mortgage_other_use)" = true or helper "Do you elect to deduct state and local general sales taxes instead of state and local income taxes?" = true or helper "Asked only where it can apply (sa.foreign_tax_deduct)" = true or helper "Do you (or, on a joint return, your spouse) have a deduction for federal estate tax on income in respect of a decedent?" = true or helper "Do you (or, on a joint return, your spouse) have a deduction for amortizable bond premium (for example, a bond premium carryforward, or premium on bonds acquired before October 23, 1986)?" = true or helper "Do you (or, on a joint return, your spouse) have an ordinary loss attributable to a contingent payment debt instrument or an inflation-indexed debt instrument (for example, a Treasury Inflation-Protected Security)?" = true or helper "Is there an unrecovered investment in a pension to deduct (the after-tax contributions of a person who died before recovering them)?" = true or helper "Do you (or, on a joint return, your spouse) have impairment-related work expenses of a disabled person?" = true)
- Expr: `{"any":[{"eq":["sa.mortgage_unreported_if_home",{"const":true}],"op":"test"},{"eq":["sa.mortgage_over_limit_if_interest",{"const":true}],"op":"test"},{"eq":["sa.mortgage_other_use_if_interest",{"const":true}],"op":"test"},{"eq":["sa.sales_tax_wish",{"const":true}],"op":"test"},{"eq":["sa.foreign_tax_deduct_if_tax",{"const":true}],"op":"test"},{"eq":["sa.estate_tax_income",{"const":true}],"op":"test"},{"eq":["sa.bond_premium",{"const":true}],"op":"test"},{"eq":["sa.debt_instrument_loss",{"const":true}],"op":"test"},{"eq":["sa.pension_unrecovered",{"const":true}],"op":"test"},{"eq":["sa.impairment_work",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "Your deduction for home mortgage interest is subject to a number of limits"; p. 8, Line 8b, "If you paid home mortgage interest to a recipient who didn’t provide you a Form 1098, report your deductible mortgage interest on line 8b"; p. 3, Line 5a, "You can elect to deduct state and local general sales taxes instead of state and local income taxes"; p. 7, Other Taxes, "Include on this line income taxes you paid to a foreign country"; pp. 11–12, Other Itemized Deductions, "Only the expenses listed next can be deducted on line 16" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.gifts`

- **Authored helper label:** Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:

  - money given to a charity by cash, check, card or payroll deduction, including money put into a donor-advised fund
  - a payment to a charity that got you something back (such as a fundraising dinner, an auction item or a membership), or that earned you a state or local tax credit
  - property given to a charity, such as clothing, household items, a vehicle or stock, or property sold to a charity for less than its value
  - out-of-pocket costs of volunteer work for a charity, such as mileage, parking, supplies or uniforms, or unreimbursed costs of hosting a student or a foster child placed by a charitable organization
  - a charitable contribution shown on a Schedule K-1 from a partnership, S corporation, estate or trust
  - expenses you paid as a whaling captain for Native Alaskan subsistence bowhead whale hunting

  A charity here is any organization that is religious, charitable, educational, scientific or literary in purpose (such as a church, a school, a nonprofit hospital, a veterans' group or a fraternal order's charitable work), one that works to prevent cruelty to children or animals, or a federal, state, local or Indian tribal government receiving a gift for public purposes; nonprofit cemetery companies and other qualified organizations count too.
- **Encoded (Bool):** Input — Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:

  - money given to a charity by cash, check, card or payroll deduction, including money put into a donor-advised fund
  - a payment to a charity that got you something back (such as a fundraising dinner, an auction item or a membership), or that earned you a state or local tax credit
  - property given to a charity, such as clothing, household items, a vehicle or stock, or property sold to a charity for less than its value
  - out-of-pocket costs of volunteer work for a charity, such as mileage, parking, supplies or uniforms, or unreimbursed costs of hosting a student or a foster child placed by a charitable organization
  - a charitable contribution shown on a Schedule K-1 from a partnership, S corporation, estate or trust
  - expenses you paid as a whaling captain for Native Alaskan subsistence bowhead whale hunting

  A charity here is any organization that is religious, charitable, educational, scientific or literary in purpose (such as a church, a school, a nonprofit hospital, a veterans' group or a fraternal order's charitable work), one that works to prevent cruelty to children or animals, or a federal, state, local or Indian tribal government receiving a gift for public purposes; nonprofit cemetery companies and other qualified organizations count too.
- Expr: `{"op":"input","source":"Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:\n\n- money given to a charity by cash, check, card or payroll deduction, including money put into a donor-advised fund\n- a payment to a charity that got you something back (such as a fundraising dinner, an auction item or a membership), or that earned you a state or local tax credit\n- property given to a charity, such as clothing, household items, a vehicle or stock, or property sold to a charity for less than its value\n- out-of-pocket costs of volunteer work for a charity, such as mileage, parking, supplies or uniforms, or unreimbursed costs of hosting a student or a foster child placed by a charitable organization\n- a charitable contribution shown on a Schedule K-1 from a partnership, S corporation, estate or trust\n- expenses you paid as a whaling captain for Native Alaskan subsistence bowhead whale hunting\n\nA charity here is any organization that is religious, charitable, educational, scientific or literary in purpose (such as a church, a school, a nonprofit hospital, a veterans' group or a fraternal order's charitable work), one that works to prevent cruelty to children or animals, or a federal, state, local or Indian tribal government receiving a gift for public purposes; nonprofit cemetery companies and other qualified organizations count too."}`
- Cite: [i1040sca] p. 9, Gifts to Charity, "You can deduct contributions or gifts you gave to organizations that are religious, charitable, educational, scientific, or literary in purpose", "Certain whaling captains may be able to deduct expenses paid in 2025 for Native Alaskan subsistence bowhead whale hunting activities" and "Federal, state, and local governments if the gifts are solely for public purposes"; p. 9, Gifts from which you benefit, "If you made a gift and received a benefit in return"; p. 9, Amounts You Can Deduct, "Contributions can be in cash, property, or out-of-pocket expenses you paid to do volunteer work"; p. 11, Line 13, "You may have contributions that you couldn't deduct in an earlier year because they exceeded the limits on the amount you could deduct" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.no`

- **Authored helper label:** Year parameter sa.no (no)
- **Encoded (Bool):** Enter false (sa.no).
- Expr: `{"op":"param","ref":"sa.no"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.charity_limited`

- **Authored helper label:** Are any of the 2025 charitable deductions reduced by income limits? Determine under Publication 526 before answering.
- **Encoded (Bool):** Input — Are any of the 2025 charitable deductions reduced by income limits? Determine under Publication 526 before answering.
- Expr: `{"op":"input","source":"Are any of the 2025 charitable deductions reduced by income limits? Determine under Publication 526 before answering."}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.charity_limited_if_gifts`

- **Authored helper label:** The 2025 charitable deductions are reduced by income limits (no when you and your spouse gave nothing to charity in 2025)
- **Encoded (Bool):** Choose — [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = true → helper "Are any of the 2025 charitable deductions reduced by income limits? Determine under Publication 526 before answering."] [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.gifts",{"const":true}],"op":"test"},"then":"sa.charity_limited"},{"guard":{"eq":["sa.gifts",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 10, Limit on the amount you can deduct, "See Pub. 526 to figure the amount of your deduction if any of the following applies"; p. 11, Line 13, "You may have contributions that you couldn't deduct in an earlier year because they exceeded the limits on the amount you could deduct" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.gift_carryover`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have a charitable contribution carried over from an earlier year, one that was more than you could deduct in the year you made it?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have a charitable contribution carried over from an earlier year, one that was more than you could deduct in the year you made it?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have a charitable contribution carried over from an earlier year, one that was more than you could deduct in the year you made it?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.gift_carryover_if_no_gifts`

- **Authored helper label:** A charitable contribution is carried over from an earlier year (asked of every filer, whether or not they gave in 2025)
- **Encoded (Bool):** Enter the amount from helper "Do you (or, on a joint return, your spouse) have a charitable contribution carried over from an earlier year, one that was more than you could deduct in the year you made it?".
- Expr: `{"from":"sa.gift_carryover","op":"copy"}`
- Cite: [i1040sca] p. 11, Line 13, "You may have contributions that you couldn't deduct in an earlier year because they exceeded the limits on the amount you could deduct" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.excluded_income`

- **Authored helper label:** Do you (or, on a joint return, your spouse) file Form 2555 or Form 4563, or exclude income from sources within Puerto Rico?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) file Form 2555 or Form 4563, or exclude income from sources within Puerto Rico?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) file Form 2555 or Form 4563, or exclude income from sources within Puerto Rico?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.dependent`

- **Authored helper label:** Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)
- **Encoded (Bool):** Input — Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)
- Expr: `{"op":"input","source":"Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.spouse_extra`

- **Authored helper label:** Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?
- **Encoded (Bool):** Input — Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?
- Expr: `{"op":"input","source":"Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?"}`
- Cite: [i1040gi] p. 33, Line 12d, "you can check the appropriate box(es) on line 12d if your spouse had no income, isn't filing a return, and can't be claimed as a dependent on another person's return"; p. 34, Exception 2—Spouse itemizes on a separate return, "your standard deduction is zero, even if you were born before January 2, 1961, or were blind" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `sa.mfs_spouse_extra`

- **Authored helper label:** Married filing separately and claiming age or blindness boxes for your spouse (asked only when the spouse is not itemizing on a separate return; otherwise no)
- **Encoded (Bool):** Choose — [helper "Married filing separately with a spouse who is not itemizing deductions on a separate return" = true → helper "Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?"] [helper "Married filing separately with a spouse who is not itemizing deductions on a separate return" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs_spouse_not_itemizing",{"const":true}],"op":"test"},"then":"sa.spouse_extra"},{"guard":{"eq":["sa.mfs_spouse_not_itemizing",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 33, Line 12d, "If your filing status is married filing separately and your spouse was born before January 2, 1961, or was blind at the end of 2025, you can check the appropriate box(es) on line 12d if your spouse had no income, isn't filing a return, and can't be claimed as a dependent on another person's return"; p. 34, Exception 2—Spouse itemizes on a separate return, "your standard deduction is zero, even if you were born before January 2, 1961, or were blind" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.mfs_spouse_not_itemizing`

- **Authored helper label:** Married filing separately with a spouse who is not itemizing deductions on a separate return
- **Encoded (Bool):** helper "Married filing separately" = true and helper "MFS with spouse itemizing" = false
- Expr: `{"all":[{"eq":["sa.mfs",{"const":true}],"op":"test"},{"eq":["sa.mfs_spouse_itemizes",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 34, Exception 2—Spouse itemizes on a separate return, "your standard deduction is zero, even if you were born before January 2, 1961, or were blind" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.age65_count`

- **Authored helper label:** Your entry, if the answer is yes
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Born before January 2, 1961" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.age65",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sa] i1040gi p. 35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind, "You were born before January 2, 1961", "Enter the total number of boxes checked" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.age65`

- **Authored helper label:** Were you born before January 2, 1961?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["sa.age65_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f1040sa] i1040gi p. 35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind, "You were born before January 2, 1961", "Enter the total number of boxes checked" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.spouse_itemizes`

- **Authored helper label:** Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard deduction?
- **Encoded (Bool):** Input — Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard deduction?
- Interpretation: amb.2025.sa_mfs_spouse_itemizes
- Expr: `{"op":"input","source":"Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard deduction?"}`
- Cite: [i1040gi] p. 33, Line 12b, "If your filing status is married filing separately and your spouse itemizes deductions on their return, check the box on line 12b"; p. 14, Married Filing Separately, "You also can’t take the standard deduction if your spouse itemizes deductions"; p. 34, Exception 2—Spouse itemizes on a separate return, "If you checked the box on line 12b, your standard deduction is zero" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.elect_itemize`

- **Authored helper label:** Elect to itemize even if the standard deduction is larger?
- **Encoded (Bool):** Input — Elect to itemize even if the standard deduction is larger?
- Expr: `{"op":"input","source":"Elect to itemize even if the standard deduction is larger?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.agi`

- **Authored helper label:** Form 1040 line 11b adjusted gross income
- **Encoded (Dollars):** Enter the amount from f1040 line 11b.
- Expr: `{"from":"f1040.line11b","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.medical_any`

- **Authored helper label:** In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?
- **Encoded (Bool):** Input — In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?
- Expr: `{"op":"input","source":"In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.medical_premiums`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) pay for health insurance with money that had already been taxed, such as Medicare premiums, a Marketplace plan, COBRA or long-term care insurance, rather than through a deduction from pay at a job?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) pay for health insurance with money that had already been taxed, such as Medicare premiums, a Marketplace plan, COBRA or long-term care insurance, rather than through a deduction from pay at a job?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) pay for health insurance with money that had already been taxed, such as Medicare premiums, a Marketplace plan, COBRA or long-term care insurance, rather than through a deduction from pay at a job?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.medical_premiums_if_not_large`

- **Authored helper label:** Paid for health insurance with money already taxed (asked only when medical and dental costs were not said to be more than 7.5% of income)
- **Encoded (Bool):** Choose — [helper "In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?" = false → helper "In 2025, did you (or, on a joint return, your spouse) pay for health insurance with money that had already been taxed, such as Medicare premiums, a Marketplace plan, COBRA or long-term care insurance, rather than through a deduction from pay at a job?"] [helper "In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?" = true → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.medical_any",{"const":false}],"op":"test"},"then":"sa.medical_premiums"},{"guard":{"eq":["sa.medical_any",{"const":true}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 1, Medical and Dental Expenses, "Insurance premiums for medical and dental care", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.medical_asked`

- **Authored helper label:** Medical and dental costs may be deductible (they were more than 7.5% of income, or health insurance was paid for with money already taxed)
- **Encoded (Bool):** (helper "In 2025, were the medical and dental costs you (or, on a joint return, your spouse) paid yourselves, after anything insurance paid, more than 7.5% of your income?" = true or helper "Paid for health insurance with money already taxed (asked only when medical and dental costs were not said to be more than 7.5% of income)" = true)
- Expr: `{"any":[{"eq":["sa.medical_any",{"const":true}],"op":"test"},{"eq":["sa.medical_premiums_if_not_large",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 1, Medical and Dental Expenses, "You can deduct only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line1`

- **Authored helper label:** Unreimbursed eligible medical and dental expenses
- **Encoded (NonNegDollars):** Input — Unreimbursed eligible medical and dental expenses paid in 2025 (Pub. 502 lists what counts) for these people:

  - yourself
  - your spouse
  - your dependents
  - your child whom you do not claim only because of the rules for children of divorced or separated parents
  - anyone you could have claimed as a dependent except that the person had gross income of $5,200 or more or filed a joint return, or that you (or your spouse, if filing jointly) can be claimed as a dependent on someone else's 2025 return

  Reduce them by payments from insurance or other sources, but do not reduce them by a 2025 reimbursement of expenses paid in an earlier year.

  Leave out:
  - amounts equal to tax-free distributions from a health savings account (HSA) or an Archer MSA
  - insurance premiums paid by a pretax reduction of your pay, and premiums and other medical and dental expenses paid by an employer-sponsored health plan (cafeteria plan) unless they are included in box 1 of your Form W-2
  - premiums for someone on your policy who is not one of the people listed above (for example a nondependent child under age 27), unless you had family coverage when you added that person and your premiums did not increase
  - if you are a retired public safety officer, premiums to the extent paid with a tax-free distribution from your retirement plan
  - the housework part of pay to someone who did both nursing and housework (only the nursing help counts)
  - meals while away from home for medical care, other than hospital care, which includes its meals and lodging (other lodging for medical care counts at no more than $50 a night for each person who meets the Pub. 502 lodging requirements)

  Leave out health insurance entered for a business's self-employed health insurance deduction (Form 7206, lines 1 and 2); the part of it not deducted on Schedule 1 (Form 1040), line 17 is added to line 1 separately.

  For Marketplace coverage on a Form 1095-A, include the total premiums (including the part paid by advance payments of the premium tax credit), minus the premium tax credit allowed on Form 8962, line 24, and minus any excess advance payments you do not have to repay because of the repayment limit (Form 8962, line 27 minus line 29); advance payments you do repay count as premiums you paid.

  Include qualified long-term care insurance premiums only up to the limit for the age at the end of 2025 of the person for whom they were paid:

  - $480 if 40 or under
  - $900 if 41 to 50
  - $1,800 if 51 to 60
  - $4,810 if 61 to 70
  - $6,020 if 71 or older

  On the final return of a person who died in 2025, include the medical expenses paid out of that person's estate that Pub. 502 allows on the final return.
- Expr: `{"op":"input","source":"Unreimbursed eligible medical and dental expenses paid in 2025 (Pub. 502 lists what counts) for these people:\n\n- yourself\n- your spouse\n- your dependents\n- your child whom you do not claim only because of the rules for children of divorced or separated parents\n- anyone you could have claimed as a dependent except that the person had gross income of $5,200 or more or filed a joint return, or that you (or your spouse, if filing jointly) can be claimed as a dependent on someone else's 2025 return\n\nReduce them by payments from insurance or other sources, but do not reduce them by a 2025 reimbursement of expenses paid in an earlier year.\n\nLeave out:\n- amounts equal to tax-free distributions from a health savings account (HSA) or an Archer MSA\n- insurance premiums paid by a pretax reduction of your pay, and premiums and other medical and dental expenses paid by an employer-sponsored health plan (cafeteria plan) unless they are included in box 1 of your Form W-2\n- premiums for someone on your policy who is not one of the people listed above (for example a nondependent child under age 27), unless you had family coverage when you added that person and your premiums did not increase\n- if you are a retired public safety officer, premiums to the extent paid with a tax-free distribution from your retirement plan\n- the housework part of pay to someone who did both nursing and housework (only the nursing help counts)\n- meals while away from home for medical care, other than hospital care, which includes its meals and lodging (other lodging for medical care counts at no more than $50 a night for each person who meets the Pub. 502 lodging requirements)\n\nLeave out health insurance entered for a business's self-employed health insurance deduction (Form 7206, lines 1 and 2); the part of it not deducted on Schedule 1 (Form 1040), line 17 is added to line 1 separately.\n\nFor Marketplace coverage on a Form 1095-A, include the total premiums (including the part paid by advance payments of the premium tax credit), minus the premium tax credit allowed on Form 8962, line 24, and minus any excess advance payments you do not have to repay because of the repayment limit (Form 8962, line 27 minus line 29); advance payments you do repay count as premiums you paid.\n\nInclude qualified long-term care insurance premiums only up to the limit for the age at the end of 2025 of the person for whom they were paid:\n\n- $480 if 40 or under\n- $900 if 41 to 50\n- $1,800 if 51 to 60\n- $4,810 if 61 to 70\n- $6,020 if 71 or older\n\nOn the final return of a person who died in 2025, include the medical expenses paid out of that person's estate that Pub. 502 allows on the final return."}`
- Cite: [i1040sca] p. 1, Medical and Dental Expenses, "If you received a distribution from a health savings account or a medical savings account in 2025, see Pub. 969 to figure your deduction", "Certain medical expenses paid out of a deceased taxpayer's estate can be claimed on the deceased taxpayer's final return", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation", "If you are a retired public safety officer, you can't include any premiums you paid to the extent they were paid for with a tax-free distribution from your retirement plan", "If you paid someone to do both nursing and housework, you can deduct only the cost of the nursing help", "Hospital care (including meals and lodging), clinic costs, and lab fees", "Lodging expenses (but not meals) while away from home to receive medical care"; p. 2, "Don't deduct more than $50 a night for each person who meets the requirements in Pub. 502 under Lodging", "Limit on long-term care premiums you can include. The amount you can include for qualified long-term care insurance contracts (as defined in Pub. 502) depends on the age at the end of 2025 of the person for whom the premiums were paid", Line 1 Medical and Dental Expenses, "Enter the total of your medical and dental expenses after you reduce these expenses by any payments received from insurance or other sources", "If advance payments of the premium tax credit were made or you think you may be eligible to claim a premium tax credit, fill out Form 8962 before filling out Schedule A, line 1", "self-employed health insurance deduction on Schedule 1 (Form 1040), line 17, reduce the premiums by the amount on line 17", "You can include medical and dental bills you paid in 2025 for anyone who was one of the following either when the services were provided or when you paid for them", "Your child whom you don't claim as a dependent because of the rules for children of divorced or separated parents", "Any person you could have claimed as a dependent on your return except that person received $5,200 or more of gross income or filed a joint return", "You can't deduct any premiums attributable to this individual unless this individual is a person described under Whose medical and dental expenses can you include, earlier", "However, if you had family coverage when you added this individual to your policy and your premiums didn't increase, you can enter on line 1 the full amount of your medical and dental insurance premiums", "If you received a reimbursement in 2025 for prior year medical or dental expenses, don't reduce your 2025 expenses by this amount", "don’t include on line 1 insurance premiums paid by an employer-sponsored health insurance plan (cafeteria plan) unless the premiums are included in box 1 of your Form(s) W-2", "Also, don't include any other medical and dental expenses paid by the plan unless the amount paid is included in box 1 of your Form(s) W-2"; p502 p. 12, Premium Tax Credit, "You can’t include in medical expenses the amount of health insurance premiums paid by or through the premium tax credit", "You also can’t include in medical expenses any amount of advance payments of the premium tax credit made that you did not have to pay back", "However, any amount of advance payments of the premium tax credit that you did have to pay back can be included in medical expenses", "You are treated as paying $5,100 ($8,700 less the allowed premium tax credit of $3,600)"; i8962 p. 2, "You cannot deduct the portion of your health insurance premium on your tax return that is paid for by the PTC or APTC (after you determine how much of any excess APTC you must repay)"; p969 p. 9, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your HSA"; p969 p. 13, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your Archer MSA" (2025; printed date 2025-12-08; sha256 b0999b12)

## (gate) — `sa.line1_if_medical`

- **Authored helper label:** Medical and dental expenses (zero when your costs were not more than 7.5% of income and you paid for no health insurance with money already taxed)
- **Encoded (NonNegDollars):** Choose — [helper "Medical and dental costs may be deductible (they were more than 7.5% of income, or health insurance was paid for with money already taxed)" = true → helper "Unreimbursed eligible medical and dental expenses"] [helper "Medical and dental costs may be deductible (they were more than 7.5% of income, or health insurance was paid for with money already taxed)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.medical_asked",{"const":true}],"op":"test"},"then":"sa.line1"},{"guard":{"eq":["sa.medical_asked",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 1, Medical and Dental Expenses, "If you received a distribution from a health savings account or a medical savings account in 2025, see Pub. 969 to figure your deduction", "Certain medical expenses paid out of a deceased taxpayer's estate can be claimed on the deceased taxpayer's final return", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation", "If you are a retired public safety officer, you can't include any premiums you paid to the extent they were paid for with a tax-free distribution from your retirement plan", "If you paid someone to do both nursing and housework, you can deduct only the cost of the nursing help", "Hospital care (including meals and lodging), clinic costs, and lab fees", "Lodging expenses (but not meals) while away from home to receive medical care"; p. 2, "Don't deduct more than $50 a night for each person who meets the requirements in Pub. 502 under Lodging", "Limit on long-term care premiums you can include. The amount you can include for qualified long-term care insurance contracts (as defined in Pub. 502) depends on the age at the end of 2025 of the person for whom the premiums were paid", Line 1 Medical and Dental Expenses, "Enter the total of your medical and dental expenses after you reduce these expenses by any payments received from insurance or other sources", "If advance payments of the premium tax credit were made or you think you may be eligible to claim a premium tax credit, fill out Form 8962 before filling out Schedule A, line 1", "self-employed health insurance deduction on Schedule 1 (Form 1040), line 17, reduce the premiums by the amount on line 17", "You can include medical and dental bills you paid in 2025 for anyone who was one of the following either when the services were provided or when you paid for them", "Your child whom you don't claim as a dependent because of the rules for children of divorced or separated parents", "Any person you could have claimed as a dependent on your return except that person received $5,200 or more of gross income or filed a joint return", "You can't deduct any premiums attributable to this individual unless this individual is a person described under Whose medical and dental expenses can you include, earlier", "However, if you had family coverage when you added this individual to your policy and your premiums didn't increase, you can enter on line 1 the full amount of your medical and dental insurance premiums", "If you received a reimbursement in 2025 for prior year medical or dental expenses, don't reduce your 2025 expenses by this amount", "don’t include on line 1 insurance premiums paid by an employer-sponsored health insurance plan (cafeteria plan) unless the premiums are included in box 1 of your Form(s) W-2", "Also, don't include any other medical and dental expenses paid by the plan unless the amount paid is included in box 1 of your Form(s) W-2"; p502 p. 12, Premium Tax Credit, "You can’t include in medical expenses the amount of health insurance premiums paid by or through the premium tax credit", "You also can’t include in medical expenses any amount of advance payments of the premium tax credit made that you did not have to pay back", "However, any amount of advance payments of the premium tax credit that you did have to pay back can be included in medical expenses", "You are treated as paying $5,100 ($8,700 less the allowed premium tax credit of $3,600)"; i8962 p. 2, "You cannot deduct the portion of your health insurance premium on your tax return that is paid for by the PTC or APTC (after you determine how much of any excess APTC you must repay)"; p969 p. 9, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your HSA"; p969 p. 13, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your Archer MSA" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.sehi_unused`

- **Authored helper label:** Health insurance of the return's businesses not deducted on Schedule 1, line 17 (Form 7206, line 3 minus line 14)
- **Encoded (NonNegDollars):** Add person.sehi_unused over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.sehi_unused","op":"sum_over"}`
- Cite: [i7206] p. 2, "any medical insurance payments not deductible on Schedule 1 (Form 1040), line 17, can be included as medical expenses on Schedule A (Form 1040) if you itemize deductions" (2025; sha256 9cbf92b3)

## 1 — `sa.line1_total`

- **IRS:** Medical and dental expenses, including health insurance of a business not deducted on Schedule 1, line 17
- **Encoded (NonNegDollars):** Add helper "Medical and dental expenses (zero when your costs were not more than 7.5% of income and you paid for no health insurance with money already taxed)" and helper "Health insurance of the return's businesses not deducted on Schedule 1, line 17 (Form 7206, line 3 minus line 14)".
- Expr: `{"of":["sa.line1_if_medical","sa.sehi_unused"],"op":"sum"}`
- Cite: [i1040sca] p. 2, Line 1 Medical and Dental Expenses, "Enter the total of your medical and dental expenses after you reduce these expenses by any payments received from insurance or other sources", "self-employed health insurance deduction on Schedule 1 (Form 1040), line 17, reduce the premiums by the amount on line 17"; i7206 p. 2, "any medical insurance payments not deductible on Schedule 1 (Form 1040), line 17, can be included as medical expenses on Schedule A (Form 1040) if you itemize deductions" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.state_tax_any`

- **Authored helper label:** In 2025, was state or local income tax taken out of your (or, on a joint return, your spouse's) pay?
- **Encoded (Bool):** Input — In 2025, was state or local income tax taken out of your (or, on a joint return, your spouse's) pay? Boxes 17 and 19 of a Form W-2 show it.
- Expr: `{"op":"input","source":"In 2025, was state or local income tax taken out of your (or, on a joint return, your spouse's) pay? Boxes 17 and 19 of a Form W-2 show it."}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.state_tax_other_any`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) pay state or local income tax other than tax withheld from pay: tax withheld from other income, estimated payments, tax paid for an earlier year, a mandatory contribution to a state disability, unemployment, workers compensation or family leave fund, income tax of a U.S. territory, or a state or local tax credit you received for a gift to charity and applied to your tax?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) pay state or local income tax other than tax withheld from pay: tax withheld from other income, estimated payments, tax paid for an earlier year, a mandatory contribution to a state disability, unemployment, workers compensation or family leave fund, income tax of a U.S. territory, or a state or local tax credit you received for a gift to charity and applied to your tax?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) pay state or local income tax other than tax withheld from pay: tax withheld from other income, estimated payments, tax paid for an earlier year, a mandatory contribution to a state disability, unemployment, workers compensation or family leave fund, income tax of a U.S. territory, or a state or local tax credit you received for a gift to charity and applied to your tax?"}`
- Cite: [i1040sca] p. 3, Line 5a, "State and local estimated tax payments made during 2025", "Mandatory contributions to state family leave programs", Safe harbor for certain charitable contributions made in exchange for a state or local tax credit, "to the extent you apply the state or local tax credit to this or a prior year's state or local tax liability, you may include this amount on line 5a, 5b, or 5c, whichever is appropriate" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line5a`

- **Authored helper label:** State and local income tax withheld from your (or, on a joint return, your spouse's) pay in 2025 (Form W-2, boxes 17 and 19)
- **Encoded (NonNegDollars):** Input — State and local income tax withheld from your (or, on a joint return, your spouse's) pay in 2025: boxes 17 and 19 of each Form W-2.

  Do not count withholding you deduct on another form, such as Schedule C, E or F.

  Do not count here state or local income tax paid any other way (tax withheld from other income such as a pension, estimated payments, tax paid for an earlier year, mandatory contributions to a state disability, unemployment or family leave fund, U.S. territory income tax, or a state or local tax credit received for a charitable contribution); that is the amount of state and local income tax paid other than tax withheld from pay, entered separately.

  Do not reduce the amount by a state or local income tax refund or credit you expect for 2025, or by a refund or credit of prior-year state and local income taxes received in 2025.
- Expr: `{"op":"input","source":"State and local income tax withheld from your (or, on a joint return, your spouse's) pay in 2025: boxes 17 and 19 of each Form W-2.\n\nDo not count withholding you deduct on another form, such as Schedule C, E or F.\n\nDo not count here state or local income tax paid any other way (tax withheld from other income such as a pension, estimated payments, tax paid for an earlier year, mandatory contributions to a state disability, unemployment or family leave fund, U.S. territory income tax, or a state or local tax credit received for a charitable contribution); that is the amount of state and local income tax paid other than tax withheld from pay, entered separately.\n\nDo not reduce the amount by a state or local income tax refund or credit you expect for 2025, or by a refund or credit of prior-year state and local income taxes received in 2025."}`
- Cite: [i1040sca] p. 3, Line 5a, "State and local income taxes withheld from your salary during 2025. Your Form(s) W-2 will show these amounts", "don't include on line 5a any withheld taxes you deducted on other forms, such as Schedule C, E, or F", "State or local income tax refund or credit you expect to receive for 2025", "Refund of or credit for prior year state and local income taxes you actually received in 2025"; fw2 p. 4, Copy B, "17 State income tax", "19 Local income tax" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line5a_if_state_tax`

- **Authored helper label:** State and local income taxes withheld from pay (zero when none was withheld)
- **Encoded (NonNegDollars):** Choose — [helper "In 2025, was state or local income tax taken out of your (or, on a joint return, your spouse's) pay?" = true → helper "State and local income tax withheld from your (or, on a joint return, your spouse's) pay in 2025 (Form W-2, boxes 17 and 19)"] [helper "In 2025, was state or local income tax taken out of your (or, on a joint return, your spouse's) pay?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.state_tax_any",{"const":true}],"op":"test"},"then":"sa.line5a"},{"guard":{"eq":["sa.state_tax_any",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 3, Line 5a, "State and local income taxes withheld from your salary during 2025. Your Form(s) W-2 will show these amounts", "don't include on line 5a any withheld taxes you deducted on other forms, such as Schedule C, E, or F" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.state_tax_other`

- **Authored helper label:** State and local income taxes paid in 2025 other than tax withheld from pay
- **Encoded (NonNegDollars):** Input — State and local income taxes you (or, on a joint return, your spouse) paid in 2025 other than tax withheld from pay (Form W-2, boxes 17 and 19, entered separately).

  Include state and local income tax withheld from other income, such as a pension, unemployment pay or gambling winnings (but not withholding you deducted on another form, such as Schedule C), estimated payments made in 2025 (including a prior-year refund credited to 2025), and taxes paid in 2025 for a prior year, but not penalties or interest.

  Include mandatory contributions to:
  - the California, New Jersey or New York Nonoccupational Disability Benefit Fund
  - the Rhode Island Temporary Disability Benefit Fund
  - the Washington State Supplemental Workmen's Compensation Fund
  - the Alaska, California, New Jersey or Pennsylvania state unemployment fund
  - state family leave programs (such as New Jersey Family Leave Insurance or California Paid Family Leave)

  Do not reduce the amount by a state or local income tax refund or credit you expect for 2025, or by a refund or credit of prior-year state and local income taxes received in 2025.

  If you made a cash charitable contribution in return for a state or local tax credit and reduced your charitable deduction by that credit, you may include here (or on line 5b or 5c, whichever tax the credit offsets) the part of the credit you applied to your 2025 or an earlier year's state or local tax liability.

  Include income taxes imposed by a U.S. territory here (not as foreign taxes), except territory taxes allocable to excluded income and territory taxes you take as a credit instead of a deduction.
- Expr: `{"op":"input","source":"State and local income taxes you (or, on a joint return, your spouse) paid in 2025 other than tax withheld from pay (Form W-2, boxes 17 and 19, entered separately).\n\nInclude state and local income tax withheld from other income, such as a pension, unemployment pay or gambling winnings (but not withholding you deducted on another form, such as Schedule C), estimated payments made in 2025 (including a prior-year refund credited to 2025), and taxes paid in 2025 for a prior year, but not penalties or interest.\n\nInclude mandatory contributions to:\n- the California, New Jersey or New York Nonoccupational Disability Benefit Fund\n- the Rhode Island Temporary Disability Benefit Fund\n- the Washington State Supplemental Workmen's Compensation Fund\n- the Alaska, California, New Jersey or Pennsylvania state unemployment fund\n- state family leave programs (such as New Jersey Family Leave Insurance or California Paid Family Leave)\n\nDo not reduce the amount by a state or local income tax refund or credit you expect for 2025, or by a refund or credit of prior-year state and local income taxes received in 2025.\n\nIf you made a cash charitable contribution in return for a state or local tax credit and reduced your charitable deduction by that credit, you may include here (or on line 5b or 5c, whichever tax the credit offsets) the part of the credit you applied to your 2025 or an earlier year's state or local tax liability.\n\nInclude income taxes imposed by a U.S. territory here (not as foreign taxes), except territory taxes allocable to excluded income and territory taxes you take as a credit instead of a deduction."}`
- Cite: [i1040sca] p. 3, U.S. territory taxes, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c", "However, don't include any U.S. territory taxes you paid that are allocable to excluded income", "You may want to take a credit for U.S. territory tax instead of a deduction", Line 5a, "Forms W-2G, 1099-G, 1099-R, 1099-MISC, and 1099-NEC may also show state and local income taxes withheld", "don't include on line 5a any withheld taxes you deducted on other forms, such as Schedule C, E, or F", "State and local estimated tax payments made during 2025, including any part of a prior year refund that you chose to have credited to your 2025 state or local income taxes", "State and local income taxes paid in 2025 for a prior year, such as taxes paid with your 2024 state or local income tax return. Don't include penalties or interest.", "Mandatory contributions you made to the California, New Jersey, or New York Nonoccupational Disability Benefit Fund", "Mandatory contributions to the Alaska, California, New Jersey, or Pennsylvania state unemployment fund", "Mandatory contributions to state family leave programs", "Refund of or credit for prior year state and local income taxes you actually received in 2025", Safe harbor for certain charitable contributions made in exchange for a state or local tax credit, "If you meet these conditions and to the extent you apply the state or local tax credit to this or a prior year's state or local tax liability, you may include this amount on line 5a, 5b, or 5c, whichever is appropriate"; p. 7, Line 6, "Don't include taxes you paid to a U.S. territory on this line; instead, include U.S. territory taxes on the appropriate state and local tax line" (2025; printed date 2025-12-08; sha256 b0999b12)

## (gate) — `sa.state_tax_other_if_any`

- **Authored helper label:** State and local income taxes paid other than by withholding from pay (zero when there were none)
- **Encoded (NonNegDollars):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) pay state or local income tax other than tax withheld from pay: tax withheld from other income, estimated payments, tax paid for an earlier year, a mandatory contribution to a state disability, unemployment, workers compensation or family leave fund, income tax of a U.S. territory, or a state or local tax credit you received for a gift to charity and applied to your tax?" = true → helper "State and local income taxes paid in 2025 other than tax withheld from pay"] [helper "In 2025, did you (or, on a joint return, your spouse) pay state or local income tax other than tax withheld from pay: tax withheld from other income, estimated payments, tax paid for an earlier year, a mandatory contribution to a state disability, unemployment, workers compensation or family leave fund, income tax of a U.S. territory, or a state or local tax credit you received for a gift to charity and applied to your tax?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.state_tax_other_any",{"const":true}],"op":"test"},"then":"sa.state_tax_other"},{"guard":{"eq":["sa.state_tax_other_any",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 3, Line 5a, "State and local income taxes paid in 2025 for a prior year", "State and local estimated tax payments made during 2025" (2025; printed date 2025-12-08; sha256 b0999b12)

## 5a — `sa.line5a_total`

- **IRS:** Add sa.line5a_if_state_tax, sa.state_tax_other_if_any
- **Encoded (NonNegDollars):** Add helper "State and local income taxes withheld from pay (zero when none was withheld)" and helper "State and local income taxes paid other than by withholding from pay (zero when there were none)".
- Expr: `{"of":["sa.line5a_if_state_tax","sa.state_tax_other_if_any"],"op":"sum"}`
- Cite: [i1040sca] p. 3, Line 5a, "include on line 5a the state and local income taxes listed next" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.home_owner`

- **Authored helper label:** At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?
- **Encoded (Bool):** Input — At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?
- Expr: `{"op":"input","source":"At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.home_other`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) pay interest on a loan secured by a boat, a camper or a mobile home that has sleeping, cooking and toilet facilities, or on a mortgage on a home that is in another person's name?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) pay interest on a loan secured by a boat, a camper or a mobile home that has sleeping, cooking and toilet facilities, or on a mortgage on a home that is in another person's name?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) pay interest on a loan secured by a boat, a camper or a mobile home that has sleeping, cooking and toilet facilities, or on a mortgage on a home that is in another person's name?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.home_other_if_not_owner`

- **Authored helper label:** Paid interest on a loan secured by a boat, camper or mobile home, or on a mortgage on a home in the name of another person (asked only when you owned no home or other real estate)
- **Encoded (Bool):** Choose — [helper "At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?" = false → helper "In 2025, did you (or, on a joint return, your spouse) pay interest on a loan secured by a boat, a camper or a mobile home that has sleeping, cooking and toilet facilities, or on a mortgage on a home that is in another person's name?"] [helper "At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?" = true → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.home_owner",{"const":false}],"op":"test"},"then":"sa.home_other"},{"guard":{"eq":["sa.home_owner",{"const":true}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Line 8, "A home can be a house, condominium, cooperative, mobile home, boat, or similar property", "It must provide basic living accommodations including sleeping space, toilet, and cooking facilities" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.home_asked`

- **Authored helper label:** You owned a home or other real estate, or paid interest on a loan secured by a home
- **Encoded (Bool):** (helper "At any time in 2025, did you (or, on a joint return, your spouse) own a home or other real estate?" = true or helper "Paid interest on a loan secured by a boat, camper or mobile home, or on a mortgage on a home in the name of another person (asked only when you owned no home or other real estate)" = true)
- Expr: `{"any":[{"eq":["sa.home_owner",{"const":true}],"op":"test"},{"eq":["sa.home_other_if_not_owner",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 6, Line 5b, "Enter on line 5b the state and local taxes you paid on real estate you own"; p. 8, Line 8, "A home mortgage is any loan that is secured by your main home or second home" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line5b`

- **Authored helper label:** Deductible state/local real estate taxes
- **Encoded (NonNegDollars):** Input — Deductible state/local real estate taxes on real estate you (or, on a joint return, your spouse) own that was not used for business, only if the taxes are assessed uniformly at a like rate on all real property in the community and used for general community or governmental purposes.

  Leave out:
  - foreign real estate taxes
  - itemized charges for services to specific property or persons (for example trash collection, water use or mowing charges)
  - charges for improvements that tend to increase the property's value (for example an assessment to build a new sidewalk), except a charge used only to maintain an existing public facility (for example to repair an existing sidewalk)

  If your mortgage payments include real estate taxes, include only what the mortgage company actually paid to the taxing authority in 2025.

  Reduce the amount by a 2025 refund or rebate of real estate taxes paid in 2025, and by real estate tax charged to the buyer if you sold your home in 2025 (settlement statement, Form 1099-S box 6); do not reduce it by a refund of taxes paid in an earlier year.

  Only taxes paid in 2025 and assessed before 2026 count (state or local law determines when a tax is assessed, generally when you become liable for it), so leave out a prepayment of 2026 property tax not assessed before 2026.

  Include real estate taxes imposed by a U.S. territory, except those allocable to excluded income.
- Expr: `{"op":"input","source":"Deductible state/local real estate taxes on real estate you (or, on a joint return, your spouse) own that was not used for business, only if the taxes are assessed uniformly at a like rate on all real property in the community and used for general community or governmental purposes.\n\nLeave out:\n- foreign real estate taxes\n- itemized charges for services to specific property or persons (for example trash collection, water use or mowing charges)\n- charges for improvements that tend to increase the property's value (for example an assessment to build a new sidewalk), except a charge used only to maintain an existing public facility (for example to repair an existing sidewalk)\n\nIf your mortgage payments include real estate taxes, include only what the mortgage company actually paid to the taxing authority in 2025.\n\nReduce the amount by a 2025 refund or rebate of real estate taxes paid in 2025, and by real estate tax charged to the buyer if you sold your home in 2025 (settlement statement, Form 1099-S box 6); do not reduce it by a refund of taxes paid in an earlier year.\n\nOnly taxes paid in 2025 and assessed before 2026 count (state or local law determines when a tax is assessed, generally when you become liable for it), so leave out a prepayment of 2026 property tax not assessed before 2026.\n\nInclude real estate taxes imposed by a U.S. territory, except those allocable to excluded income."}`
- Cite: [i1040sca] p. 3, U.S. territory taxes, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c", "However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, Line 5b, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025", "State or local law determines whether and when a property tax is assessed, which is generally when the taxpayer becomes liable for the property tax imposed", "Enter on line 5b the state and local taxes you paid on real estate you own that wasn't used for business, but only if the taxes are assessed uniformly at a like rate on all real property throughout the community, and the proceeds are used for general community or governmental purposes", "Foreign taxes you paid on real estate", "Itemized charges for services to specific property or persons", "Charges for improvements that tend to increase the value of your property", "However, a charge is deductible if it is used only to maintain an existing public facility in service", "If your mortgage payments include your real estate taxes, you can include only the amount the mortgage company actually paid to the taxing authority in 2025", "any real estate tax charged to the buyer should be shown on your settlement statement and in box 6 of any Form 1099-S you received", "This amount is considered a refund of real estate taxes", "If you received a refund or rebate in 2025 of real estate taxes you paid in 2025, reduce your deduction by the amount of the refund or rebate", "If you received a refund or rebate in 2025 of real estate taxes you paid in an earlier year, don't reduce your deduction by this amount" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line5b_if_home_owner`

- **Authored helper label:** State and local real estate taxes (zero when you owned no home or other real estate)
- **Encoded (NonNegDollars):** Choose — [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = true → helper "Deductible state/local real estate taxes"] [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.home_asked",{"const":true}],"op":"test"},"then":"sa.line5b"},{"guard":{"eq":["sa.home_asked",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 3, U.S. territory taxes, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c", "However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, Line 5b, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025", "State or local law determines whether and when a property tax is assessed, which is generally when the taxpayer becomes liable for the property tax imposed", "Enter on line 5b the state and local taxes you paid on real estate you own that wasn't used for business, but only if the taxes are assessed uniformly at a like rate on all real property throughout the community, and the proceeds are used for general community or governmental purposes", "Foreign taxes you paid on real estate", "Itemized charges for services to specific property or persons", "Charges for improvements that tend to increase the value of your property", "However, a charge is deductible if it is used only to maintain an existing public facility in service", "If your mortgage payments include your real estate taxes, you can include only the amount the mortgage company actually paid to the taxing authority in 2025", "any real estate tax charged to the buyer should be shown on your settlement statement and in box 6 of any Form 1099-S you received", "This amount is considered a refund of real estate taxes", "If you received a refund or rebate in 2025 of real estate taxes you paid in 2025, reduce your deduction by the amount of the refund or rebate", "If you received a refund or rebate in 2025 of real estate taxes you paid in an earlier year, don't reduce your deduction by this amount" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.property_tax_other_any`

- **Authored helper label:** Does the real estate tax amount you entered include any amount that is not deductible: tax on real estate outside the United States, an itemized charge for services, a charge for an improvement, tax charged to the buyer on a sale, a refund or rebate of 2025 tax, or tax not assessed before 2026?
- **Encoded (Bool):** Input — Does the real estate tax amount you entered include any amount that is not deductible: tax on real estate outside the United States, an itemized charge for services, a charge for an improvement, tax charged to the buyer on a sale, a refund or rebate of 2025 tax, or tax not assessed before 2026?
- Expr: `{"op":"input","source":"Does the real estate tax amount you entered include any amount that is not deductible: tax on real estate outside the United States, an itemized charge for services, a charge for an improvement, tax charged to the buyer on a sale, a refund or rebate of 2025 tax, or tax not assessed before 2026?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.property_tax_other_if_home`

- **Authored helper label:** The real estate tax amount includes an amount that is not deductible (asked only of an owner of real estate)
- **Encoded (Bool):** Choose — [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = true → helper "Does the real estate tax amount you entered include any amount that is not deductible: tax on real estate outside the United States, an itemized charge for services, a charge for an improvement, tax charged to the buyer on a sale, a refund or rebate of 2025 tax, or tax not assessed before 2026?"] [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.home_asked",{"const":true}],"op":"test"},"then":"sa.property_tax_other_any"},{"guard":{"eq":["sa.home_asked",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 6, Line 5b, "Don't include the following amounts on line 5b", "Foreign taxes you paid on real estate" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.property_tax_leave_out`

- **Authored helper label:** The part of the real estate tax amount that is not deductible
- **Encoded (NonNegDollars):** Input — The part of the real estate tax amount that is not deductible
- Expr: `{"op":"input","source":"The part of the real estate tax amount that is not deductible"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.property_tax_leave_out_if_any`

- **Authored helper label:** The part of the real estate tax amount that is not deductible (zero when there is none)
- **Encoded (NonNegDollars):** Choose — [helper "The real estate tax amount includes an amount that is not deductible (asked only of an owner of real estate)" = true → helper "The part of the real estate tax amount that is not deductible"] [helper "The real estate tax amount includes an amount that is not deductible (asked only of an owner of real estate)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.property_tax_other_if_home",{"const":true}],"op":"test"},"then":"sa.property_tax_leave_out"},{"guard":{"eq":["sa.property_tax_other_if_home",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 6, Line 5b, "Don't include the following amounts on line 5b", "Itemized charges for services to specific property or persons" (2025; printed date 2025-12-08; sha256 b0999b12)

## 5b — `sa.line5b_net`

- **IRS:** Subtract sa.property_tax_leave_out_if_any from sa.line5b_if_home_owner; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract helper "The part of the real estate tax amount that is not deductible (zero when there is none)" from helper "State and local real estate taxes (zero when you owned no home or other real estate)". If zero or less, enter -0-.
- Expr: `{"from":"sa.line5b_if_home_owner","op":"subtract_floor0","take":"sa.property_tax_leave_out_if_any"}`
- Cite: [i1040sca] p. 6, Line 5b, "Enter on line 5b the state and local taxes you paid on real estate you own that wasn't used for business", "Don't include the following amounts on line 5b" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.personal_property_tax_any`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.line5c`

- **Authored helper label:** Deductible state/local personal property taxes
- **Encoded (NonNegDollars):** Input — Deductible state/local personal property taxes: only taxes based on value alone and imposed on a yearly basis (for a yearly car registration fee based partly on value, only the part based on value), paid in 2025 and assessed before 2026. Include personal property taxes imposed by a U.S. territory, except those allocable to excluded income.
- Expr: `{"op":"input","source":"Deductible state/local personal property taxes: only taxes based on value alone and imposed on a yearly basis (for a yearly car registration fee based partly on value, only the part based on value), paid in 2025 and assessed before 2026. Include personal property taxes imposed by a U.S. territory, except those allocable to excluded income."}`
- Cite: [i1040sca] p. 3, U.S. territory taxes, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c", "However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, Line 5c, "Enter on line 5c the state and local personal property taxes you paid, but only if the taxes were based on value alone and were imposed on a yearly basis", "You can deduct only the part of the fee that was based on the car's value"; p. 7, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025" (2025; printed date 2025-12-08; sha256 b0999b12)

## 5c — `sa.line5c_if_taxed`

- **IRS:** State and local personal property taxes (zero when you paid none)
- **Encoded (NonNegDollars):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?" = true → helper "Deductible state/local personal property taxes"] [helper "In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.personal_property_tax_any",{"const":true}],"op":"test"},"then":"sa.line5c"},{"guard":{"eq":["sa.personal_property_tax_any",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 3, U.S. territory taxes, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c", "However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, Line 5c, "Enter on line 5c the state and local personal property taxes you paid, but only if the taxes were based on value alone and were imposed on a yearly basis", "You can deduct only the part of the fee that was based on the car's value"; p. 7, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_interest`

- **Authored helper label:** Home mortgage interest and points reported to you on Form 1098 for a loan secured by your main home or second home (only your share of a loan shared with someone other than your spouse; not reduced by a refund of overpaid interest)
- **Encoded (NonNegDollars):** Input — Home mortgage interest and points reported to you on Form 1098 (boxes 1 and 6) in 2025 for loans secured by your main home or second home. Where you and someone other than your spouse on a joint return were both liable for and paid the interest, count only your share. Do not reduce the amount by a refund of overpaid interest the Form 1098 shows. Leave out interest paid in 2025 for a period after 2025. The debt and use limits are asked separately.
- Expr: `{"op":"input","source":"Home mortgage interest and points reported to you on Form 1098 (boxes 1 and 6) in 2025 for loans secured by your main home or second home. Where you and someone other than your spouse on a joint return were both liable for and paid the interest, count only your share. Do not reduce the amount by a refund of overpaid interest the Form 1098 shows. Leave out interest paid in 2025 for a period after 2025. The debt and use limits are asked separately."}`
- Cite: [i1040sca] p. 8, Interest You Paid, "In general, if you paid interest in 2025 that applies to any period after 2025, you can deduct only amounts that apply for 2025"; Line 8, Home Mortgage Interest, "A home mortgage is any loan that is secured by your main home or second home"; Line 8a, "Enter on line 8a mortgage interest and points reported to you on Form 1098 unless one or more of the limits on home mortgage interest apply to you", "Refund of overpaid interest. If your Form 1098 shows any refund of overpaid interest, don't reduce your deduction by the refund", "More than one borrower" and "If the shared interest was reported on the Form 1098 you received, deduct only your share of the interest on line 8a" (2025; printed date 2025-12-08; sha256 b0999b12)

## 8a — `sa.line8a`

- **IRS:** Home mortgage interest and points reported to you on Form 1098 (zero when you owned no home or other real estate and paid no interest on a mortgage secured by a home)
- **Encoded (NonNegDollars):** Choose — [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = true → helper "Home mortgage interest and points reported to you on Form 1098 for a loan secured by your main home or second home (only your share of a loan shared with someone other than your spouse; not reduced by a refund of overpaid interest)"] [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.home_asked",{"const":true}],"op":"test"},"then":"sa.mortgage_interest"},{"guard":{"eq":["sa.home_asked",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Line 8a, "Enter on line 8a mortgage interest and points reported to you on Form 1098 unless one or more of the limits on home mortgage interest apply to you" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.has_mortgage_interest`

- **Authored helper label:** Home mortgage interest is entered on line 8a
- **Encoded (Bool):** line 8a > $0
- Expr: `{"gt":["sa.line8a",{"const":0}],"op":"test"}`
- Cite: [i1040sca] p. 8, Line 8a, "Enter on line 8a mortgage interest and points reported to you on Form 1098" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_unreported`

- **Authored helper label:** Did you (or, on a joint return, your spouse) pay home mortgage interest or points in 2025 that are not reported to you on Form 1098?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) pay home mortgage interest or points in 2025 that are not reported to you on Form 1098?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) pay home mortgage interest or points in 2025 that are not reported to you on Form 1098?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.mortgage_unreported_if_home`

- **Authored helper label:** Asked only where it can apply (sa.mortgage_unreported)
- **Encoded (Bool):** Choose — [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = true → helper "Did you (or, on a joint return, your spouse) pay home mortgage interest or points in 2025 that are not reported to you on Form 1098?"] [helper "You owned a home or other real estate, or paid interest on a loan secured by a home" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.home_asked",{"const":true}],"op":"test"},"then":"sa.mortgage_unreported"},{"guard":{"eq":["sa.home_asked",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Line 8b, "If you paid home mortgage interest to a recipient who didn’t provide you a Form 1098, report your deductible mortgage interest on line 8b"; p. 9, Line 8c, "Points Not Reported on Form 1098" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_over_limit`

- **Authored helper label:** Is your home mortgage interest limited because the mortgage debt is more than $750,000 (more than $1,000,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?
- **Encoded (Bool):** Input — Is your home mortgage interest limited because the mortgage debt is more than $750,000 (more than $1,000,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?
- Expr: `{"op":"input","source":"Is your home mortgage interest limited because the mortgage debt is more than $750,000 (more than $1,000,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.mortgage_interest_not_mfs`

- **Authored helper label:** Home mortgage interest paid, on a return that is not married filing separately
- **Encoded (Bool):** helper "Home mortgage interest is entered on line 8a" = true and helper "Married filing separately" = false
- Expr: `{"all":[{"eq":["sa.has_mortgage_interest",{"const":true}],"op":"test"},{"eq":["sa.mfs",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "deduct home mortgage interest on up to $750,000 ($375,000 if you are married filing separately) of that debt" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_interest_mfs`

- **Authored helper label:** Home mortgage interest paid, on a married filing separately return
- **Encoded (Bool):** helper "Home mortgage interest is entered on line 8a" = true and helper "Married filing separately" = true
- Expr: `{"all":[{"eq":["sa.has_mortgage_interest",{"const":true}],"op":"test"},{"eq":["sa.mfs",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "deduct home mortgage interest on up to $750,000 ($375,000 if you are married filing separately) of that debt" (2025; printed date 2025-12-08; sha256 b0999b12)

## (gate) — `sa.mortgage_over_limit_if_joint_limits`

- **Authored helper label:** The home mortgage debt is over the $750,000 or $1,000,000 limit or the home's value, asked only where mortgage interest was paid on a return that is not married filing separately (otherwise no)
- **Encoded (Bool):** Choose — [helper "Home mortgage interest paid, on a return that is not married filing separately" = true → helper "Is your home mortgage interest limited because the mortgage debt is more than $750,000 (more than $1,000,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?"] [helper "Home mortgage interest paid, on a return that is not married filing separately" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mortgage_interest_not_mfs",{"const":true}],"op":"test"},"then":"sa.mortgage_over_limit"},{"guard":{"eq":["sa.mortgage_interest_not_mfs",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "you can only deduct home mortgage interest on up to $1,000,000", "deduct home mortgage interest on up to $750,000", "If the total amount of all mortgages is more than the fair market value of the home" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_over_limit_mfs`

- **Authored helper label:** Is your home mortgage interest limited because the mortgage debt is more than $375,000 (more than $500,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?
- **Encoded (Bool):** Input — Is your home mortgage interest limited because the mortgage debt is more than $375,000 (more than $500,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?
- Interpretation: amb.2025.sa_mfs_mortgage_limit
- Expr: `{"op":"input","source":"Is your home mortgage interest limited because the mortgage debt is more than $375,000 (more than $500,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "you can only deduct home mortgage interest on up to $1,000,000 ($500,000 if you are married filing separately) of that debt", "deduct home mortgage interest on up to $750,000 ($375,000 if you are married filing separately) of that debt", "If the total amount of all mortgages is more than the fair market value of the home" (2025; printed date 2025-12-08; sha256 b0999b12)

## (gate) — `sa.mortgage_over_limit_mfs_if_mfs`

- **Authored helper label:** The home mortgage debt is over the $375,000 or $500,000 limit or the home's value, asked only where mortgage interest was paid on a married filing separately return (otherwise no)
- **Encoded (Bool):** Choose — [helper "Home mortgage interest paid, on a married filing separately return" = true → helper "Is your home mortgage interest limited because the mortgage debt is more than $375,000 (more than $500,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?"] [helper "Home mortgage interest paid, on a married filing separately return" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mortgage_interest_mfs",{"const":true}],"op":"test"},"then":"sa.mortgage_over_limit_mfs"},{"guard":{"eq":["sa.mortgage_interest_mfs",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "deduct home mortgage interest on up to $750,000 ($375,000 if you are married filing separately) of that debt" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_over_limit_if_interest`

- **Authored helper label:** The home mortgage debt is over the limit for the filing status ($750,000 or $1,000,000; $375,000 or $500,000 if married filing separately) or over the home's value (no when no mortgage interest was paid)
- **Encoded (Bool):** (helper "The home mortgage debt is over the $750,000 or $1,000,000 limit or the home's value, asked only where mortgage interest was paid on a return that is not married filing separately (otherwise no)" = true or helper "The home mortgage debt is over the $375,000 or $500,000 limit or the home's value, asked only where mortgage interest was paid on a married filing separately return (otherwise no)" = true)
- Expr: `{"any":[{"eq":["sa.mortgage_over_limit_if_joint_limits",{"const":true}],"op":"test"},{"eq":["sa.mortgage_over_limit_mfs_if_mfs",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 8, Limits on home mortgage interest, "you can only deduct home mortgage interest on up to $1,000,000 ($500,000 if you are married filing separately) of that debt", "deduct home mortgage interest on up to $750,000 ($375,000 if you are married filing separately) of that debt", "If the total amount of all mortgages is more than the fair market value of the home" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mortgage_other_use`

- **Authored helper label:** Were any of the proceeds of a loan secured by your home used for something other than to buy, build or substantially improve that home?
- **Encoded (Bool):** Input — Were any of the proceeds of a loan secured by your home used for something other than to buy, build or substantially improve that home?
- Expr: `{"op":"input","source":"Were any of the proceeds of a loan secured by your home used for something other than to buy, build or substantially improve that home?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.mortgage_other_use_if_interest`

- **Authored helper label:** Asked only where it can apply (sa.mortgage_other_use)
- **Encoded (Bool):** Choose — [helper "Home mortgage interest is entered on line 8a" = true → helper "Were any of the proceeds of a loan secured by your home used for something other than to buy, build or substantially improve that home?"] [helper "Home mortgage interest is entered on line 8a" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.has_mortgage_interest",{"const":true}],"op":"test"},"then":"sa.mortgage_other_use"},{"guard":{"eq":["sa.has_mortgage_interest",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 8, Line 8, "Interest paid on home mortgage proceeds used for other purposes isn’t deductible on lines 8a or 8b" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.sales_tax_wish`

- **Authored helper label:** Do you elect to deduct state and local general sales taxes instead of state and local income taxes?
- **Encoded (Bool):** Input — Do you elect to deduct state and local general sales taxes instead of state and local income taxes?
- Expr: `{"op":"input","source":"Do you elect to deduct state and local general sales taxes instead of state and local income taxes?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.foreign_tax_deduct`

- **Authored helper label:** Do you choose to take your foreign income taxes as an itemized deduction (Schedule A, line 6) instead of as a credit?
- **Encoded (Bool):** Input — Do you choose to take your foreign income taxes as an itemized deduction (Schedule A, line 6) instead of as a credit?
- Expr: `{"op":"input","source":"Do you choose to take your foreign income taxes as an itemized deduction (Schedule A, line 6) instead of as a credit?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.foreign_tax_deduct_if_tax`

- **Authored helper label:** Asked only where it can apply (sa.foreign_tax_deduct)
- **Encoded (Bool):** Choose — [ftc helper "Positive foreign taxes" = true → helper "Do you choose to take your foreign income taxes as an itemized deduction (Schedule A, line 6) instead of as a credit?"] [ftc helper "Positive foreign taxes" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"sa.foreign_tax_deduct"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 7, Line 6, "Include on this line income taxes you paid to a foreign country", "You may want to take a credit for the foreign tax instead" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.estate_tax_income`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have a deduction for federal estate tax on income in respect of a decedent?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have a deduction for federal estate tax on income in respect of a decedent?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have a deduction for federal estate tax on income in respect of a decedent?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.bond_premium`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have a deduction for amortizable bond premium (for example, a bond premium carryforward, or premium on bonds acquired before October 23, 1986)?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have a deduction for amortizable bond premium (for example, a bond premium carryforward, or premium on bonds acquired before October 23, 1986)?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have a deduction for amortizable bond premium (for example, a bond premium carryforward, or premium on bonds acquired before October 23, 1986)?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.debt_instrument_loss`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have an ordinary loss attributable to a contingent payment debt instrument or an inflation-indexed debt instrument (for example, a Treasury Inflation-Protected Security)?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have an ordinary loss attributable to a contingent payment debt instrument or an inflation-indexed debt instrument (for example, a Treasury Inflation-Protected Security)?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have an ordinary loss attributable to a contingent payment debt instrument or an inflation-indexed debt instrument (for example, a Treasury Inflation-Protected Security)?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.pension_unrecovered`

- **Authored helper label:** Is there an unrecovered investment in a pension to deduct (the after-tax contributions of a person who died before recovering them)?
- **Encoded (Bool):** Input — Is there an unrecovered investment in a pension to deduct (the after-tax contributions of a person who died before recovering them)?
- Expr: `{"op":"input","source":"Is there an unrecovered investment in a pension to deduct (the after-tax contributions of a person who died before recovering them)?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.impairment_work`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have impairment-related work expenses of a disabled person?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have impairment-related work expenses of a disabled person?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have impairment-related work expenses of a disabled person?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.line11`

- **Authored helper label:** Gifts to charity in cash or by check, card or payroll deduction, including out-of-pocket volunteer costs, less the value of benefits received and the amounts that can't be deducted
- **Encoded (NonNegDollars):** Input — Gifts you (or, on a joint return, your spouse) made to charity in 2025 in money (cash, check, card or payroll deduction), including out-of-pocket costs of volunteer work (the actual cost of gas and oil or 14 cents a mile, plus parking and tolls).

  Count only what you paid above the value of any benefit you received in return, and only gifts for which you keep a bank record or a written record from the charity (and, for a gift of $250 or more, the charity's written acknowledgment). Membership benefits received for an annual payment of $75 or less, and an item of token value that the charity says need not be subtracted, are not subtracted.

  Leave out: the part of a gift for which you received a state or local tax credit; political contributions; raffle, bingo or lottery tickets; tuition; dues to clubs, lodges or similar groups; payments for the right to buy college athletic tickets; gifts to individuals or to groups run for profit or to lobby; gifts to foreign organizations (a gift to a U.S. organization that transfers funds to a foreign charity is not left out); travel away from home with a significant element of personal pleasure; the value of your time; and amounts repaid to you.
- Expr: `{"op":"input","source":"Gifts you (or, on a joint return, your spouse) made to charity in 2025 in money (cash, check, card or payroll deduction), including out-of-pocket costs of volunteer work (the actual cost of gas and oil or 14 cents a mile, plus parking and tolls).\n\nCount only what you paid above the value of any benefit you received in return, and only gifts for which you keep a bank record or a written record from the charity (and, for a gift of $250 or more, the charity's written acknowledgment). Membership benefits received for an annual payment of $75 or less, and an item of token value that the charity says need not be subtracted, are not subtracted.\n\nLeave out: the part of a gift for which you received a state or local tax credit; political contributions; raffle, bingo or lottery tickets; tuition; dues to clubs, lodges or similar groups; payments for the right to buy college athletic tickets; gifts to individuals or to groups run for profit or to lobby; gifts to foreign organizations (a gift to a U.S. organization that transfers funds to a foreign charity is not left out); travel away from home with a significant element of personal pleasure; the value of your time; and amounts repaid to you."}`
- Cite: [i1040sca] p. 9, Amounts You Can Deduct, "Contributions can be in cash, property, or out-of-pocket expenses you paid to do volunteer work", "14 cents a mile", "But don't deduct any amounts that were repaid to you", Gifts from which you benefit, "you can generally only deduct the amount that is more than the value of the benefit. But this rule doesn't apply to certain membership benefits provided in return for an annual payment of $75 or less or to certain items or benefits of token value", Gifts of $250 or more; p526 p. 5, Membership fees or dues, "Both you and the organization can disregard the following membership benefits if you get them in return for an annual payment of $75 or less"; p526 p. 6, Token items, "You don’t have to reduce your contribution by the value of any benefit you receive if both of the following are true"; p. 10, Amounts You Can't Deduct, "Political contributions", "Cost of raffle, bingo, or lottery tickets", "Cost of tuition", "Value of your time or services", "Gifts to foreign organizations. However, you may be able to deduct gifts to certain U.S. organizations that transfer funds to foreign charities"; Line 11, "Enter on line 11 the total value of gifts you made in cash or by check (including out-of-pocket expenses)", Recordkeeping, "you must maintain as a record of the contribution a bank record (such as a canceled check or credit card statement) or a written record from the charity" (2025; printed date 2025-12-08; sha256 b0999b12)

## 11 — `sa.line11_if_gifts`

- **IRS:** Gifts by cash or check (zero when you and your spouse gave nothing to charity)
- **Encoded (NonNegDollars):** Choose — [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = true → helper "Gifts to charity in cash or by check, card or payroll deduction, including out-of-pocket volunteer costs, less the value of benefits received and the amounts that can't be deducted"] [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.gifts",{"const":true}],"op":"test"},"then":"sa.line11"},{"guard":{"eq":["sa.gifts",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [f1040sa] p. 1, Gifts to Charity, line 11, "Gifts by cash or check"; i1040sca p. 10, Line 11, "Enter on line 11 the total value of gifts you made in cash or by check (including out-of-pocket expenses)" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.agi_floor`

- **Authored helper label:** Form 1040 line 11b adjusted gross income, but not less than zero
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Form 1040 line 11b adjusted gross income". If zero or less, enter -0-.
- Interpretation: amb.2025.sa_medical_negative_agi
- Expr: `{"from":"sa.agi","op":"subtract_floor0","take":"sa.zero"}`
- Cite: [i1040sca] p. 1, Medical and Dental Expenses, "You can deduct only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income on Form 1040 or 1040-SR, line 11b" (2025; printed date 2025-12-08; sha256 b0999b12)

## 2 — `sa.line2`

- **IRS:** Amount from sa.agi_floor
- **Encoded (NonNegDollars):** Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".
- Interpretation: amb.2025.sa_medical_negative_agi
- Expr: `{"from":"sa.agi_floor","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 3 — `sa.line3`

- **IRS:** Multiply sa.line2 by sa.medical_rate
- **Encoded (NonNegDollars):** Multiply line 2 (sa.line2) by 75/1000 (sa.medical_rate).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.line2","op":"multiply_rate","rate":{"param":"sa.medical_rate"}}`
- Cite: [f1040sa] p. 1, Medical and Dental Expenses, line 3, "Multiply line 2 by 7.5% (0.075)" (2025; created 2025-11-20; sha256 c14acf34)

## 4 — `sa.line4`

- **IRS:** Subtract sa.line3 from sa.line1_total; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract line 3 (sa.line3) from line 1. If zero or less, enter -0-.
- Expr: `{"from":"sa.line1_total","op":"subtract_floor0","take":"sa.line3"}`
- Cite: [f1040sa] p. 1, Medical and Dental Expenses, line 4, "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-" (2025; created 2025-11-20; sha256 c14acf34)

## 5d — `sa.line5d`

- **IRS:** Add sa.line5a_total, sa.line5b_net, sa.line5c_if_taxed
- **Encoded (NonNegDollars):** Add line 5a, line 5b, and line 5c.
- Expr: `{"of":["sa.line5a_total","sa.line5b_net","sa.line5c_if_taxed"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Taxes You Paid, line 5d, "d Add lines 5a through 5c" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltbase`

- **Authored helper label:** Year parameter sa.salt_base
- **Encoded (NonNegDollars):** Enter $40,000 (sa.salt_base).
- Expr: `{"op":"param","ref":"sa.salt_base"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltfloor`

- **Authored helper label:** Year parameter sa.salt_floor
- **Encoded (NonNegDollars):** Enter $10,000 (sa.salt_floor).
- Expr: `{"op":"param","ref":"sa.salt_floor"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltthreshold`

- **Authored helper label:** Year parameter sa.salt_threshold
- **Encoded (NonNegDollars):** Enter single $500,000; mfj $500,000; mfs $250,000; hoh $500,000; qss $500,000 (sa.salt_threshold).
- Expr: `{"op":"param","ref":"sa.salt_threshold"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltexcess`

- **Authored helper label:** Subtract sa.saltthreshold from sa.agi; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sa.salt_threshold" from helper "Form 1040 line 11b adjusted gross income". If zero or less, enter -0-.
- Expr: `{"from":"sa.agi","op":"subtract_floor0","take":"sa.saltthreshold"}`
- Cite: [f1040sa] i1040sca p. 7, State and Local Tax Deduction Worksheet, "Enter $500,000 ($250,000 if married filing separately)", "Is the amount on line 4 more than the amount on line 5?", "Subtract line 5 from line 4" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltreduction`

- **Authored helper label:** Multiply sa.saltexcess by sa.salt_rate
- **Encoded (NonNegDollars):** Multiply helper "Subtract sa.saltthreshold from sa.agi; if zero or less, enter zero" by 3/10 (sa.salt_rate).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltexcess","op":"multiply_rate","rate":{"param":"sa.salt_rate"}}`
- Cite: [f1040sa] i1040sca p. 7, State and Local Tax Deduction Worksheet, "Multiply line 6 by 30% (0.30)" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltremaining`

- **Authored helper label:** Subtract sa.saltreduction from sa.saltbase; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract helper "Multiply sa.saltexcess by sa.salt_rate" from helper "Year parameter sa.salt_base". If zero or less, enter -0-.
- Expr: `{"from":"sa.saltbase","op":"subtract_floor0","take":"sa.saltreduction"}`
- Cite: [f1040sa] i1040sca p. 7, State and Local Tax Deduction Worksheet, "Subtract line 7 from line 1", "Enter $40,000" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltfloor_applied`

- **Authored helper label:** Larger of remaining ceiling and $10,000
- **Encoded (NonNegDollars):** Enter the larger of helper "Subtract sa.saltreduction from sa.saltbase; if zero or less, enter zero" or helper "Year parameter sa.salt_floor".
- Expr: `{"of":["sa.saltremaining","sa.saltfloor"],"op":"larger_of"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.salthalf`

- **Authored helper label:** Multiply sa.saltfloor_applied by sa.half
- **Encoded (NonNegDollars):** Multiply helper "Larger of remaining ceiling and $10,000" by 1/2 (sa.half).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltfloor_applied","op":"multiply_rate","rate":{"param":"sa.half"}}`
- Cite: [f1040sa] i1040sca p. 7, State and Local Tax Deduction Worksheet, "State and local tax deduction. Enter the smaller of the amount on line 9 (half the amount on line 9 if married filing separately) or the amount from Schedule A, line 5d" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.mfs`

- **Authored helper label:** Married filing separately
- **Encoded (Bool):** f1040 line Filing Status = 'mfs'
- Expr: `{"eq":["f1040.status",{"const":"mfs"}],"op":"test"}`
- Cite: [f1040sa] i1040sca p. 7, State and Local Tax Deduction Worksheet, "(half the amount on line 9 if married filing separately)" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltlimit`

- **Authored helper label:** Half the worksheet ceiling if married filing separately
- **Encoded (NonNegDollars):** Choose — [helper "Married filing separately" = true → helper "Multiply sa.saltfloor_applied by sa.half"] [helper "Married filing separately" = false → helper "Larger of remaining ceiling and $10,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs",{"const":true}],"op":"test"},"then":"sa.salthalf"},{"guard":{"eq":["sa.mfs",{"const":false}],"op":"test"},"then":"sa.saltfloor_applied"}],"op":"choose"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## 5e — `sa.line5e`

- **IRS:** Smaller of sa.line5d, sa.saltlimit
- **Encoded (NonNegDollars):** Enter the smaller of line 5d or helper "Half the worksheet ceiling if married filing separately".
- Expr: `{"of":["sa.line5d","sa.saltlimit"],"op":"smaller_of"}`
- Cite: [f1040sa] p. 1, Taxes You Paid, line 5e, "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately)"; i1040sca p. 7, Line 5e, "If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, complete the State and Local Tax Deduction Worksheet to figure the amount to enter on line 5e" (2025; created 2025-11-20; sha256 c14acf34)

## 6 — `sa.line6`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8b — `sa.line8b`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8c — `sa.line8c`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 13 — `sa.line13`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.gift_carryover_if_no_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 15 — `sa.line15`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [i1040sca] p. 11, Line 15, "Complete and attach Form 4684 to figure the amount of your loss. Only enter the amount from Form 4684, line 18, on line 15" (zero here: a casualty or theft loss is refused by sd.casualty through sd.other_forms, the refusal Schedule D additional source forms) (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.gambling_losses`

- **Authored helper label:** Gambling losses you had during 2025
- **Encoded (NonNegDollars):** Input — Your gambling losses during 2025 (you and, on a joint return, your spouse), including the cost of nonwinning bingo, lottery and raffle tickets, in full, whether or not more than your winnings, but not losses of a trade or business of gambling, which go on Schedule C; zero if none
- Expr: `{"op":"input","source":"Your gambling losses during 2025 (you and, on a joint return, your spouse), including the cost of nonwinning bingo, lottery and raffle tickets, in full, whether or not more than your winnings, but not losses of a trade or business of gambling, which go on Schedule C; zero if none"}`
- Cite: [i1040sca] p. 11, Other Itemized Deductions, "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets)"; p525 p. 33, Gambling winnings, "If you’re in the trade or business of gambling, use Schedule C (Form 1040)" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.line16_gambling`

- **Authored helper label:** Gambling losses, but only to the extent of gambling winnings reported on Schedule 1, line 8b
- **Encoded (NonNegDollars):** Enter the smaller of helper "Gambling losses you had during 2025" or s1 line 8b.
- Interpretation: amb.2025.gambling_losses
- Expr: `{"of":["sa.gambling_losses","s1.line8b"],"op":"smaller_of"}`
- Cite: [i1040sca] p. 11, Other Itemized Deductions, "but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b"; p525 p. 33, Gambling winnings, "If you itemize your deductions on Schedule A (Form 1040), you can deduct gambling losses you had during the year, but only up to the amount of your winnings" (2025; printed date 2025-12-08; sha256 b0999b12)

## 16 — `sa.line16`

- **IRS:** Other—from list in instructions. List type and amount:
- **Encoded (NonNegDollars):** Choose — [s1 helper "Any gambling winnings" = true → helper "Gambling losses, but only to the extent of gambling winnings reported on Schedule 1, line 8b"] [s1 helper "Any gambling winnings" = false → helper "Year parameter sales.zero"]
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_gambling",{"const":true}],"op":"test"},"then":"sa.line16_gambling"},{"guard":{"eq":["s1.has_gambling",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [f1040sa] Schedule A (2025), line 16; i1040sca p. 11, Other Itemized Deductions, "Only the expenses listed next can be deducted on line 16" (2025; created 2025-11-20; sha256 c14acf34)

## 7 — `sa.line7`

- **IRS:** Add sa.line5e, sa.line6
- **Encoded (NonNegDollars):** Add line 5e and line 6.
- Expr: `{"of":["sa.line5e","sa.line6"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Taxes You Paid, line 7, "Add lines 5e and 6" (2025; created 2025-11-20; sha256 c14acf34)

## 8e — `sa.line8e`

- **IRS:** Add sa.line8a, sa.line8b, sa.line8c
- **Encoded (NonNegDollars):** Add line 8a, line 8b, and line 8c.
- Expr: `{"of":["sa.line8a","sa.line8b","sa.line8c"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Interest You Paid, line 8e, "e Add lines 8a through 8c" (2025; created 2025-11-20; sha256 c14acf34)

## 9 — `sa.line9`

- **IRS:** Amount from f4952.line8
- **Encoded (NonNegDollars):** Enter the amount from f4952 line 8.
- Expr: `{"from":"f4952.line8","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 10 — `sa.line10`

- **IRS:** Add sa.line8e, sa.line9
- **Encoded (NonNegDollars):** Add line 8e and line 9.
- Expr: `{"of":["sa.line8e","sa.line9"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Interest You Paid, line 10, "Add lines 8e and 9" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.line12_noncash`

- **Authored helper label:** Total supported noncash donations before income limits
- **Encoded (NonNegDollars):** Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"gift","field":"gift.allowed","op":"sum_over"}`
- Cite: [f1040sa] p. 1, Gifts to Charity, line 12, "Other than by cash or check. If you made any gift of $250 or more, see instructions" (2025; created 2025-11-20; sha256 c14acf34)

## 12 — `sa.line12`

- **IRS:** Total supported noncash donations before income limits (zero when you and your spouse gave nothing to charity)
- **Encoded (NonNegDollars):** Choose — [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = true → helper "Total supported noncash donations before income limits"] [helper "Did you or your spouse make any charitable contribution in 2025? Answer Yes if any of these applies:" = false → helper "Year parameter sales.zero"]
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"alternatives":[{"guard":{"eq":["sa.gifts",{"const":true}],"op":"test"},"then":"sa.line12_noncash"},{"guard":{"eq":["sa.gifts",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [f1040sa] p. 1, Gifts to Charity, line 12, "Other than by cash or check. If you made any gift of $250 or more, see instructions"; i1040sca p. 10, Line 12, "Enter on line 12 the total value of your contributions of property other than by cash or check" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.form8283`

- **Authored helper label:** Noncash total exceeds $500; Form 8283 attachment required
- **Encoded (Bool):** line 12 > $500
- Expr: `{"gt":["sa.line12",{"const":50000}],"op":"test"}`
- Cite: [f1040sa] p. 1, Gifts to Charity, line 12, "You must attach Form 8283 if over $500" (2025; created 2025-11-20; sha256 c14acf34)

## 14 — `sa.line14`

- **IRS:** Add sa.line11, sa.line12, sa.line13
- **Encoded (NonNegDollars):** Add line 11, line 12, and line 13.
- Expr: `{"of":["sa.line11_if_gifts","sa.line12","sa.line13"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Gifts to Charity, line 14, "Add lines 11 through 13" (2025; created 2025-11-20; sha256 c14acf34)

## 17 — `sa.line17`

- **IRS:** Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
- **Encoded (NonNegDollars):** Add line 4, line 7, line 10, line 14, line 15, and line 16.
- **Refusal:** when sa.charity_limited_if_gifts is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"of":["sa.line4","sa.line7","sa.line10","sa.line14","sa.line15","sa.line16"],"op":"sum"}`
- Cite: [f1040sa] p. 1, Total Itemized Deductions, line 17, "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.standardbase`

- **Authored helper label:** Year parameter sa.standard_base
- **Encoded (NonNegDollars):** Enter single $15,750; mfj $31,500; mfs $15,750; hoh $23,625; qss $31,500 (sa.standard_base).
- Expr: `{"op":"param","ref":"sa.standard_base"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.extra`

- **Authored helper label:** Year parameter sa.standard_extra
- **Encoded (NonNegDollars):** Enter single $2,000; mfj $1,600; mfs $1,600; hoh $2,000; qss $1,600 (sa.standard_extra).
- Expr: `{"op":"param","ref":"sa.standard_extra"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.boxes_age65`

- **Authored helper label:** Number of boxes checked for born before January 2, 1961 (you, and your spouse if filing jointly), not counting a person who died in 2025 before reaching 65
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Born before January 2, 1961, and not a person who died in 2025 before reaching 65 (a box checked for age)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.age65_box",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.extra_age65`

- **Authored helper label:** Additional standard deduction for each box checked for age
- **Encoded (NonNegDollars):** Multiply helper "Year parameter sa.standard_extra" by the number on helper "Number of boxes checked for born before January 2, 1961 (you, and your spouse if filing jointly), not counting a person who died in 2025 before reaching 65".
- Expr: `{"amount":"sa.extra","count":"sa.boxes_age65","op":"multiply_count"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.boxes_blind`

- **Authored helper label:** Number of boxes checked for blindness (you, and your spouse if filing jointly)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Were you blind at the end of 2025 (totally blind, or partly blind with a statement certified by your eye doctor)?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.blind",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.extra_blind`

- **Authored helper label:** Additional standard deduction for each box checked for blindness
- **Encoded (NonNegDollars):** Multiply helper "Year parameter sa.standard_extra" by the number on helper "Number of boxes checked for blindness (you, and your spouse if filing jointly)".
- Expr: `{"amount":"sa.extra","count":"sa.boxes_blind","op":"multiply_count"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.standardraw`

- **Authored helper label:** Add sa.standardbase, sa.extra_age65, sa.extra_blind
- **Encoded (NonNegDollars):** Add helper "Year parameter sa.standard_base", helper "Additional standard deduction for each box checked for age", and helper "Additional standard deduction for each box checked for blindness".
- Expr: `{"of":["sa.standardbase","sa.extra_age65","sa.extra_blind"],"op":"sum"}`
- Cite: [f1040sa] i1040gi pp. 34–35, Line 12e Standard Deduction or Itemized Deductions, "Exception 4—Born before January 2, 1961, or blind", "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind", "If born before January 2, 1961, or blind, multiply the number on line 1 by $1,600 ($2,000 if single or head of household)" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.dep_earned_sum`

- **Authored helper label:** Earned income for the Standard Deduction Worksheet for Dependents, before Schedule 1 line 15 (Form 1040 line 1z and Schedule 1 lines 3 and 8r)
- **Encoded (Dollars):** Add f1040 line 1z, s1 line 3, and s1 line 8r.
- Interpretation: amb.2025.sa_dep_earned
- Expr: `{"of":["f1040.line1z","s1.line3","s1.line8r"],"op":"sum"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, "Generally, your earned income is the total of the amount(s) you reported on Form 1040 or 1040-SR, line 1z, and Schedule 1, lines 3, 6, 8r, 8t, and 8u minus the amount, if any, on Schedule 1, line 15" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.dep_earned`

- **Authored helper label:** Earned income for the Standard Deduction Worksheet for Dependents (zero if none)
- **Encoded (NonNegDollars):** Subtract s1 line 15 from helper "Earned income for the Standard Deduction Worksheet for Dependents, before Schedule 1 line 15 (Form 1040 line 1z and Schedule 1 lines 3 and 8r)". If zero or less, enter -0-.
- Interpretation: amb.2025.sa_dep_earned
- Expr: `{"from":"sa.dep_earned_sum","op":"subtract_floor0","take":"s1.line15"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, "Generally, your earned income is the total of the amount(s) you reported on Form 1040 or 1040-SR, line 1z, and Schedule 1, lines 3, 6, 8r, 8t, and 8u minus the amount, if any, on Schedule 1, line 15"; p501 p. 26, Table 8, line 1, "Enter your earned income (defined below). If none, enter -0-." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.dep_add`

- **Authored helper label:** Year parameter sa.dep_add ($450)
- **Encoded (NonNegDollars):** Enter $450 (sa.dep_add).
- Expr: `{"op":"param","ref":"sa.dep_add"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 2, "Yes. Add $450 to your earned income. Enter the total" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.dep_plus`

- **Authored helper label:** Earned income plus $450
- **Encoded (NonNegDollars):** Add helper "Earned income for the Standard Deduction Worksheet for Dependents (zero if none)" and helper "Year parameter sa.dep_add ($450)".
- Expr: `{"of":["sa.dep_earned","sa.dep_add"],"op":"sum"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 2, "Yes. Add $450 to your earned income. Enter the total" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.dep_min`

- **Authored helper label:** Year parameter sa.dep_min ($1,350)
- **Encoded (NonNegDollars):** Enter $1,350 (sa.dep_min).
- Expr: `{"op":"param","ref":"sa.dep_min"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 2, "No. Enter $1,350" (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `sa.dep_line2`

- **IRS:** Is your earned income more than $900? Yes: add $450 to your earned income and enter the total. No: enter $1,350
- **Encoded (NonNegDollars):** Enter the larger of helper "Earned income plus $450" or helper "Year parameter sa.dep_min ($1,350)".
- Expr: `{"of":["sa.dep_plus","sa.dep_min"],"op":"larger_of"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 2, "Is your earned income* more than $900?", "Yes. Add $450 to your earned income. Enter the total", "No. Enter $1,350"; p501 p. 24, Standard Deduction for Dependents, "generally limited to the greater of: 1. $1,350, or 2. The individual's earned income for the year plus $450" (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `sa.dep_line3`

- **IRS:** Enter the amount shown for your filing status: single or married filing separately, $15,750; married filing jointly, $31,500; head of household, $23,625
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sa.standard_base".
- Expr: `{"from":"sa.standardbase","op":"copy"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 3, "Enter the amount shown below for your filing status" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4a — `sa.dep_line4a`

- **IRS:** Enter the smaller of line 2 or line 3
- **Encoded (NonNegDollars):** Enter the smaller of line 2 (sa.dep_line2) or line 3 (sa.dep_line3).
- Expr: `{"of":["sa.dep_line2","sa.dep_line3"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 4a, "Enter the smaller of line 2 or line 3" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4b — `sa.dep_line4b`

- **IRS:** If born before January 2, 1961, or blind, multiply the number on line 1 by $1,600 ($2,000 if single or head of household)
- **Encoded (NonNegDollars):** Add helper "Additional standard deduction for each box checked for age" and helper "Additional standard deduction for each box checked for blindness".
- Expr: `{"of":["sa.extra_age65","sa.extra_blind"],"op":"sum"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 4b, "If born before January 2, 1961, or blind, multiply the number on line 1 by $1,600 ($2,000 if single or head of household)" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4c — `sa.dep_line4c`

- **IRS:** Add lines 4a and 4b. Enter the total here and on Form 1040 or 1040-SR, line 12e
- **Encoded (NonNegDollars):** Add line 4a and line 4b.
- Expr: `{"of":["sa.dep_line4a","sa.dep_line4b"],"op":"sum"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 4c, "Add lines 4a and 4b. Enter the total here and on Form 1040 or 1040-SR, line 12e" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `sa.dep_qss`

- **Authored helper label:** Someone can claim you as a dependent and your filing status is qualifying surviving spouse
- **Encoded (Bool):** helper "Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = true and f1040 line Filing Status = 'qss'
- Interpretation: amb.2025.sa_dep_qss
- Expr: `{"all":[{"eq":["sa.dependent",{"const":true}],"op":"test"},{"eq":["f1040.status",{"const":"qss"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 3, "Enter the amount shown below for your filing status" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.standard_amount`

- **Authored helper label:** Standard deduction before a spouse's itemizing on a separate return is applied (the Standard Deduction Worksheet for Dependents when someone can claim you, or your spouse if filing jointly, as a dependent)
- **Encoded (NonNegDollars):** Choose — [helper "Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = true → line 4c] [helper "Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false → helper "Add sa.standardbase, sa.extra_age65, sa.extra_blind"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.dependent",{"const":true}],"op":"test"},"then":"sa.dep_line4c"},{"guard":{"eq":["sa.dependent",{"const":false}],"op":"test"},"then":"sa.standardraw"}],"op":"choose"}`
- Cite: [i1040gi] p. 34, Line 12e, "Exception 1—Dependent. Line 12a. If you checked a box on line 12a, use the Standard Deduction Worksheet for Dependents to figure your standard deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.standard`

- **Authored helper label:** Standard deduction, zero when MFS spouse itemizes
- **Encoded (NonNegDollars):** Choose — [helper "MFS with spouse itemizing" = true → helper "Year parameter sales.zero"] [helper "MFS with spouse itemizing" = false → helper "Standard deduction before a spouse's itemizing on a separate return is applied (the Standard Deduction Worksheet for Dependents when someone can claim you, or your spouse if filing jointly, as a dependent)"]
- **Refusal:** when sa.dep_qss is true, cannot complete Standard Deduction Worksheet for Dependents, line 3, for a qualifying surviving spouse. The Standard Deduction Worksheet for Dependents gives no amount for a qualifying surviving spouse whom someone else can claim as a dependent, so this tool does not figure that standard deduction. Cite: [i1040gi] p. 35, Standard Deduction Worksheet for Dependents—Line 12e, line 3, "Enter the amount shown below for your filing status" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when sa.mfs_spouse_extra is true, cannot complete Standard Deduction Chart spouse boxes on a separate return. Checking age or blindness boxes for your spouse on a married filing separately return is outside this tool. Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},"then":"sa.zero"},{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":false}],"op":"test"},"then":"sa.standard_amount"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.itemizes`

- **Authored helper label:** Itemize if elected, required, or itemized total exceeds standard
- **Encoded (Bool):** (helper "Elect to itemize even if the standard deduction is larger?" = true or helper "MFS with spouse itemizing" = true or line 17 > helper "Standard deduction, zero when MFS spouse itemizes")
- Expr: `{"any":[{"eq":["sa.elect_itemize",{"const":true}],"op":"test"},{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},{"gt":["sa.line17","sa.standard"],"op":"test"}],"op":"test"}`
- Cite: [f1040sa] p. 1, Total Itemized Deductions, line 18, "If you elect to itemize deductions even though they are less than your standard deduction, check this box"; i1040gi p. 34, Line 12e Standard Deduction or Itemized Deductions, "In most cases, your federal income tax will be less if you take the larger of your standard deduction or itemized deductions", "If you checked the box on line 12b, your standard deduction is zero" (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.deduction`

- **Authored helper label:** Deduction selected for Form 1040 line 12e
- **Encoded (NonNegDollars):** Choose — [helper "Itemize if elected, required, or itemized total exceeds standard" = true → line 17] [helper "Itemize if elected, required, or itemized total exceeds standard" = false → helper "Standard deduction, zero when MFS spouse itemizes"]
- **Refusal:** when sa.mfs_joint_paid_if_itemizing is true, cannot complete Schedule A on a separate return, expenses paid jointly with the spouse (Pub. 504, Table 1). On a married filing separately return, itemized deductions paid from money held with your spouse, or state income tax on a joint state return, are divided between you under Pub. 504; that is outside this tool. Cite: [i1040sca] p. 1, "If you and your spouse paid expenses jointly and are filing separate returns for 2025, see Pub. 504 to figure the portion of joint expenses that you can claim as itemized deductions" (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"alternatives":[{"guard":{"eq":["sa.itemizes",{"const":true}],"op":"test"},"then":"sa.line17"},{"guard":{"eq":["sa.itemizes",{"const":false}],"op":"test"},"then":"sa.standard"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.mfs_joint_paid`

- **Authored helper label:** Was any amount you entered for these deductions paid from an account you hold with your husband or wife, or do the two of you file a joint 2025 state income tax return?
- **Encoded (Bool):** Input — Was any amount you entered for these deductions paid from an account you hold with your husband or wife, or do the two of you file a joint 2025 state income tax return?
- Expr: `{"op":"input","source":"Was any amount you entered for these deductions paid from an account you hold with your husband or wife, or do the two of you file a joint 2025 state income tax return?"}`
- Cite: [i1040sca] p. 1, "If you and your spouse paid expenses jointly and are filing separate returns for 2025, see Pub. 504 to figure the portion of joint expenses that you can claim as itemized deductions"; p504 p. 5, Table 1, medical expenses "paid with funds deposited in a joint checking account in which you and your spouse have an equal interest", "half of the total medical expenses, subject to certain limits, unless you can show that you alone paid the expenses"; p504 p. 5, Table 1, state income tax, "file a joint state income tax return and you’re liable for only your own share of state income tax" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mfs_itemizing`

- **Authored helper label:** Married filing separately and itemizing deductions
- **Encoded (Bool):** helper "Married filing separately" = true and helper "Itemize if elected, required, or itemized total exceeds standard" = true
- Expr: `{"all":[{"eq":["sa.mfs",{"const":true}],"op":"test"},{"eq":["sa.itemizes",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sca] p. 1, "If you and your spouse paid expenses jointly and are filing separate returns for 2025, see Pub. 504" (2025; printed date 2025-12-08; sha256 b0999b12)

## (gate) — `sa.mfs_joint_paid_if_itemizing`

- **Authored helper label:** Itemized expenses paid jointly with the spouse, asked only on a married filing separately return that itemizes (otherwise no)
- **Encoded (Bool):** Choose — [helper "Married filing separately and itemizing deductions" = true → helper "Was any amount you entered for these deductions paid from an account you hold with your husband or wife, or do the two of you file a joint 2025 state income tax return?"] [helper "Married filing separately and itemizing deductions" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs_itemizing",{"const":true}],"op":"test"},"then":"sa.mfs_joint_paid"},{"guard":{"eq":["sa.mfs_itemizing",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040sca] p. 1, "If you and your spouse paid expenses jointly and are filing separate returns for 2025, see Pub. 504" (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.mfs_spouse_itemizes`

- **Authored helper label:** MFS with spouse itemizing
- **Encoded (Bool):** Choose — [helper "Married filing separately" = true → helper "Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard deduction?"] [helper "Married filing separately" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs",{"const":true}],"op":"test"},"then":"sa.spouse_itemizes"},{"guard":{"eq":["sa.mfs",{"const":false}],"op":"test"},"then":"sa.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 34, Exception 2—Spouse itemizes on a separate return, "If you checked the box on line 12b, your standard deduction is zero" (2025; printed date 2026-02-25; sha256 482e9c48)
