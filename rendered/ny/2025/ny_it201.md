# Form IT-201 (2025), Resident Income Tax Return — New York State and New York City

- Document: `ny_it201` (form, tax year 2025)

## (question) — `ny_it201.ask.state_resident`

- **Authored helper label:** Were you (and your spouse, on a joint return) a New York State resident for all of 2025: domiciled in New York State, or keeping a permanent place of abode in New York State for substantially all of the year and spending 184 days or more there?

  Answer No:
  - if, though domiciled in New York, you kept no permanent place of abode in New York, kept one outside New York all year and spent 30 days or less in New York, or met the 548-day foreign-presence test (Group A or B)
  - if you were in active military service
  - if your only New York residence was undergraduate student housing
- **Encoded (Bool):** Input — Were you (and your spouse, on a joint return) a New York State resident for all of 2025: domiciled in New York State, or keeping a permanent place of abode in New York State for substantially all of the year and spending 184 days or more there?

  Answer No:
  - if, though domiciled in New York, you kept no permanent place of abode in New York, kept one outside New York all year and spent 30 days or less in New York, or met the 548-day foreign-presence test (Group A or B)
  - if you were in active military service
  - if your only New York residence was undergraduate student housing
- Expr: `{"op":"input","source":"Were you (and your spouse, on a joint return) a New York State resident for all of 2025: domiciled in New York State, or keeping a permanent place of abode in New York State for substantially all of the year and spending 184 days or more there?\n\nAnswer No:\n- if, though domiciled in New York, you kept no permanent place of abode in New York, kept one outside New York all year and spent 30 days or less in New York, or met the 548-day foreign-presence test (Group A or B)\n- if you were in active military service\n- if your only New York residence was undergraduate student housing"}`
- Cite: [ny_it201i] p. 30, Resident, "You maintain a permanent place of abode in New York State for substantially all of the tax year and spend 184 days or more in New York State during the tax year" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.city_resident`

- **Authored helper label:** Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?
- **Encoded (Bool):** Input — Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?
- Expr: `{"op":"input","source":"Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?"}`
- Cite: [ny_it201i] p. 31, New York City and Yonkers, "substitute New York City or Yonkers in place of New York State" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.special_accrual`

- **Authored helper label:** Were you a New York City nonresident on December 31, 2024, or will you be a New York State or City nonresident on January 1, 2026, and do you have income fixed and determinable in one tax year but reported federally in another (accrued income)?
- **Encoded (Bool):** Input — Were you a New York City nonresident on December 31, 2024, or will you be a New York State or City nonresident on January 1, 2026, and do you have income fixed and determinable in one tax year but reported federally in another (accrued income)?
- Expr: `{"op":"input","source":"Were you a New York City nonresident on December 31, 2024, or will you be a New York State or City nonresident on January 1, 2026, and do you have income fixed and determinable in one tax year but reported federally in another (accrued income)?"}`
- Cite: [ny_it201i] p. 31, Special accruals, "you may have to use special accrual rules (see below) to calculate your New York State and New York City personal income tax for 2025" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.yonkers`

- **Authored helper label:** Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?
- **Encoded (Bool):** Input — Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?
- Expr: `{"op":"input","source":"Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?"}`
- Cite: [ny_it201i] p. 5, Item D2, "All IT-201 filers must complete item D2." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.special_code`

- **Authored helper label:** Does any New York special condition code apply to you (item G: for example A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1)?
- **Encoded (Bool):** Input — Does any New York special condition code apply to you (item G: for example A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1)?
- Expr: `{"op":"input","source":"Does any New York special condition code apply to you (item G: for example A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1)?"}`
- Cite: [ny_it201i] p. 5, Item G, "If you qualify for one or more of the special conditions below, enter the specified two-character code." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.decedent`

- **Authored helper label:** Is this return for a taxpayer (or spouse) who died after December 31, 2024?
- **Encoded (Bool):** Input — Is this return for a taxpayer (or spouse) who died after December 31, 2024?
- Expr: `{"op":"input","source":"Is this return for a taxpayer (or spouse) who died after December 31, 2024?"}`
- Cite: [ny_it201i] p. 4, Decedent information, "If the taxpayer whose name is listed first on the return died after December 31, 2024, and before you filed your return, enter the date of death" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.item_c`

- **Authored helper label:** Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C).
- **Encoded (Bool):** Input — Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C).
- Expr: `{"op":"input","source":"Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C)."}`
- Cite: [ny_it201i] p. 5, Item C, "If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.inflation_check`

- **Authored helper label:** Did you receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?
- **Encoded (Bool):** Input — Did you receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?
- Expr: `{"op":"input","source":"Did you receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?"}`
- Cite: [ny_it201i] p. 8, Line 25, "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.out_of_state_bond_interest`

- **Authored helper label:** Did you have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?
- **Encoded (Bool):** Input — Did you have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?
- Expr: `{"op":"input","source":"Did you have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?"}`
- Cite: [ny_it201i] p. 7, Line 20, "Do you have interest income from state and local bonds and obligations from states other than New York State or its local governments?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.414h`

- **Authored helper label:** Are you a public employee of New York State or its local governments with 414(h) retirement contributions shown on a Form W-2?
- **Encoded (Bool):** Input — Are you a public employee of New York State or its local governments with 414(h) retirement contributions shown on a Form W-2?
- Expr: `{"op":"input","source":"Are you a public employee of New York State or its local governments with 414(h) retirement contributions shown on a Form W-2?"}`
- Cite: [ny_it201i] p. 8, Line 21, "Are you a public employee of New York State or its local governments?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.529_nonqualified`

- **Authored helper label:** Did you make a nonqualified withdrawal during 2025 from an account under New York's 529 college savings program?
- **Encoded (Bool):** Input — Did you make a nonqualified withdrawal during 2025 from an account under New York's 529 college savings program?
- Expr: `{"op":"input","source":"Did you make a nonqualified withdrawal during 2025 from an account under New York's 529 college savings program?"}`
- Cite: [ny_it201i] p. 8, Line 22, "Did you make a nonqualified withdrawal during 2025 from an account established under New York’s 529 college savings program?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.it225`

- **Authored helper label:** Does any other New York addition or subtraction on Form IT-225 apply to you, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?
- **Encoded (Bool):** Input — Does any other New York addition or subtraction on Form IT-225 apply to you, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?
- Expr: `{"op":"input","source":"Does any other New York addition or subtraction on Form IT-225 apply to you, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?"}`
- Cite: [ny_it201i] p. 8, Line 23, "Use this line to report other additions that are not specifically listed on Form IT-201." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.gov_pension`

- **Authored helper label:** Did you or your spouse receive a pension or other distribution included in federal adjusted gross income from a New York State or local government pension plan or a federal government pension plan, including a return of your own contributions before retirement? Count the military, a U.S. territory or the District of Columbia, the MTA Police 20-Year Retirement Program, MABSTOA, the Long Island Rail Road, and the Optional Retirement Program of SUNY, CUNY or the State Education Department (for example an annuity paid by TIAA), whether received as an employee, as a beneficiary, or as a former spouse under a domestic relations order.
- **Encoded (Bool):** Input — Did you or your spouse receive a pension or other distribution included in federal adjusted gross income from a New York State or local government pension plan or a federal government pension plan, including a return of your own contributions before retirement? Count the military, a U.S. territory or the District of Columbia, the MTA Police 20-Year Retirement Program, MABSTOA, the Long Island Rail Road, and the Optional Retirement Program of SUNY, CUNY or the State Education Department (for example an annuity paid by TIAA), whether received as an employee, as a beneficiary, or as a former spouse under a domestic relations order.
- Expr: `{"op":"input","source":"Did you or your spouse receive a pension or other distribution included in federal adjusted gross income from a New York State or local government pension plan or a federal government pension plan, including a return of your own contributions before retirement? Count the military, a U.S. territory or the District of Columbia, the MTA Police 20-Year Retirement Program, MABSTOA, the Long Island Rail Road, and the Optional Retirement Program of SUNY, CUNY or the State Education Department (for example an annuity paid by TIAA), whether received as an employee, as a beneficiary, or as a former spouse under a domestic relations order."}`
- Cite: [ny_it201i] p. 9, Line 26, "Did you receive a pension or other distribution from a New York State or local government pension plan or federal government pension plan that was included in your federal adjusted gross income?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.us_obligation_interest`

- **Authored helper label:** Did you include interest from U.S. government bonds or other U.S. government obligations (for example Treasury bills, notes or bonds, or U.S. savings bonds), or dividends from a fund investing in them, in federal income?
- **Encoded (Bool):** Input — Did you include interest from U.S. government bonds or other U.S. government obligations (for example Treasury bills, notes or bonds, or U.S. savings bonds), or dividends from a fund investing in them, in federal income?
- Expr: `{"op":"input","source":"Did you include interest from U.S. government bonds or other U.S. government obligations (for example Treasury bills, notes or bonds, or U.S. savings bonds), or dividends from a fund investing in them, in federal income?"}`
- Cite: [ny_it201i] p. 9, Line 28, "Did you include interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.pension_exclusion`

- **Authored helper label:** Did you or your spouse have pension or annuity income or IRA distributions (periodic or lump-sum) included in federal adjusted gross income other than a government pension subtracted on line 26 (periodic distributions from a government section 457 deferred compensation plan count here), and was the person who received it 59 1/2 or older in 2025 (or did they receive it as a beneficiary)?
- **Encoded (Bool):** Input — Did you or your spouse have pension or annuity income or IRA distributions (periodic or lump-sum) included in federal adjusted gross income other than a government pension subtracted on line 26 (periodic distributions from a government section 457 deferred compensation plan count here), and was the person who received it 59 1/2 or older in 2025 (or did they receive it as a beneficiary)?
- Expr: `{"op":"input","source":"Did you or your spouse have pension or annuity income or IRA distributions (periodic or lump-sum) included in federal adjusted gross income other than a government pension subtracted on line 26 (periodic distributions from a government section 457 deferred compensation plan count here), and was the person who received it 59 1/2 or older in 2025 (or did they receive it as a beneficiary)?"}`
- Cite: [ny_it201i] p. 9, Line 29, "Did you enter an amount of pension income or annuity income, or both (generally reported on line 9 or 10) that was not from a New York State or local government pension plan or federal government pension plan?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.529_owner`

- **Authored helper label:** During 2025, did you, as an account owner, contribute to or withdraw from a New York 529 college savings account, or, as a beneficiary, receive a withdrawal included in federal adjusted gross income?
- **Encoded (Bool):** Input — During 2025, did you, as an account owner, contribute to or withdraw from a New York 529 college savings account, or, as a beneficiary, receive a withdrawal included in federal adjusted gross income?
- Expr: `{"op":"input","source":"During 2025, did you, as an account owner, contribute to or withdraw from a New York 529 college savings account, or, as a beneficiary, receive a withdrawal included in federal adjusted gross income?"}`
- Cite: [ny_it201i] p. 10, Line 30, "During 2025, did you, as an account owner, make contributions to or a withdrawal from one or more tuition savings accounts established under New York’s 529 college savings program?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.itemize`

- **Authored helper label:** Is your New York itemized deduction (Form IT-196) larger than your New York standard deduction, or are you married filing separately with a spouse who itemizes on their New York return?
- **Encoded (Bool):** Input — Is your New York itemized deduction (Form IT-196) larger than your New York standard deduction, or are you married filing separately with a spouse who itemizes on their New York return?
- Expr: `{"op":"input","source":"Is your New York itemized deduction (Form IT-196) larger than your New York standard deduction, or are you married filing separately with a spouse who itemizes on their New York return?"}`
- Cite: [ny_it201i] p. 10, Line 34, "You may take either the New York standard deduction or the New York itemized deduction." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.resident_credit`

- **Authored helper label:** Did you have income from sources outside New York State and pay income tax on it to another state, a local government of another state, the District of Columbia or a province of Canada?
- **Encoded (Bool):** Input — Did you have income from sources outside New York State and pay income tax on it to another state, a local government of another state, the District of Columbia or a province of Canada?
- Expr: `{"op":"input","source":"Did you have income from sources outside New York State and pay income tax on it to another state, a local government of another state, the District of Columbia or a province of Canada?"}`
- Cite: [ny_it201i] p. 13, Line 41: Resident credit, "Did you have income from sources outside New York State and pay income tax to another state, a local government of another state, the District of Columbia, or to a province of Canada?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.other_credits`

- **Authored helper label:** Are you claiming any other New York State nonrefundable or refundable credit on Form IT-201-ATT (for example long-term care insurance, investment, solar energy, farmers' school tax or claim of right)?
- **Encoded (Bool):** Input — Are you claiming any other New York State nonrefundable or refundable credit on Form IT-201-ATT (for example long-term care insurance, investment, solar energy, farmers' school tax or claim of right)?
- Expr: `{"op":"input","source":"Are you claiming any other New York State nonrefundable or refundable credit on Form IT-201-ATT (for example long-term care insurance, investment, solar energy, farmers' school tax or claim of right)?"}`
- Cite: [ny_it201i] p. 13, Line 42, "If you are claiming any nonrefundable credits, complete the appropriate credit forms and Form IT-201-ATT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.other_taxes`

- **Authored helper label:** Do you owe any other New York State or City tax on Form IT-201-ATT, for example the separate tax on a lump-sum distribution (Form IT-230)?
- **Encoded (Bool):** Input — Do you owe any other New York State or City tax on Form IT-201-ATT, for example the separate tax on a lump-sum distribution (Form IT-230)?
- Expr: `{"op":"input","source":"Do you owe any other New York State or City tax on Form IT-201-ATT, for example the separate tax on a lump-sum distribution (Form IT-230)?"}`
- Cite: [ny_it201i] p. 13, Line 45, "If you are subject to any other taxes, complete the appropriate forms and Part 2 of Form IT-201-ATT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.city_credits`

- **Authored helper label:** Can you claim the New York City unincorporated business tax credit, the New York City accumulation distribution credit, or the part-year resident New York City child and dependent care credit?
- **Encoded (Bool):** Input — Can you claim the New York City unincorporated business tax credit, the New York City accumulation distribution credit, or the part-year resident New York City child and dependent care credit?
- Expr: `{"op":"input","source":"Can you claim the New York City unincorporated business tax credit, the New York City accumulation distribution credit, or the part-year resident New York City child and dependent care credit?"}`
- Cite: [ny_it201i] p. 15, Line 53, "Can you claim the New York City unincorporated business tax (UBT) credit, the New York City accumulation distribution credit, or the part-year resident nonrefundable New York City child and dependent care credit?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.mctmt`

- **Authored helper label:** Did you or your spouse have net earnings from self-employment allocated to New York City (MCTD Zone 1) or to Zone 2 of more than $50,000?
- **Encoded (Bool):** Input — Did you or your spouse have net earnings from self-employment allocated to New York City (MCTD Zone 1) or to Zone 2 of more than $50,000?
- Expr: `{"op":"input","source":"Did you or your spouse have net earnings from self-employment allocated to New York City (MCTD Zone 1) or to Zone 2 of more than $50,000?"}`
- Cite: [ny_it201i] p. 15, Lines 54a through 54e, "Did you or your spouse have net earnings from self-employment allocated to Zone 1 or Zone 2, or both that exceed $50,000?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.owes_use_tax`

- **Authored helper label:** Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?
- **Encoded (Bool):** Input — Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?
- Expr: `{"op":"input","source":"Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?"}`
- Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "You owe sales or compensating use tax if you:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.use_tax_st141`

- **Authored helper label:** Do you owe use tax on an item or service costing $1,000 or more, or on purchases for a business, rental real estate or royalty activity, or do you want to calculate the exact amount (Form ST-141)?
- **Encoded (Bool):** Input — Do you owe use tax on an item or service costing $1,000 or more, or on purchases for a business, rental real estate or royalty activity, or do you want to calculate the exact amount (Form ST-141)?
- Expr: `{"op":"input","source":"Do you owe use tax on an item or service costing $1,000 or more, or on purchases for a business, rental real estate or royalty activity, or do you want to calculate the exact amount (Form ST-141)?"}`
- Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "You must use Form ST-141 to calculate your sales and use tax liability to be reported on this return if any of the following apply:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.contributions`

- **Authored helper label:** Do you want to make voluntary contributions to the funds listed on Form IT-227?
- **Encoded (Bool):** Input — Do you want to make voluntary contributions to the funds listed on Form IT-227?
- Expr: `{"op":"input","source":"Do you want to make voluntary contributions to the funds listed on Form IT-227?"}`
- Cite: [ny_it201i] p. 19, Line 60, "Do you want to make any voluntary contributions to the funds listed on Form IT-227?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.dependent_care`

- **Authored helper label:** Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you claimed it)?
- **Encoded (Bool):** Input — Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you claimed it)?
- Expr: `{"op":"input","source":"Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you claimed it)?"}`
- Cite: [ny_it201i] p. 19, Line 64, "Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you actually claimed it)?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.noncustodial`

- **Authored helper label:** Did you make child support payments payable through a New York State Support Collection Unit?
- **Encoded (Bool):** Input — Did you make child support payments payable through a New York State Support Collection Unit?
- Expr: `{"op":"input","source":"Did you make child support payments payable through a New York State Support Collection Unit?"}`
- Cite: [ny_it201i] p. 19, Line 66, "Did you make child support payments payable through a New York State Support Collection Unit?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.real_property_credit`

- **Authored helper label:** Might you qualify for the New York real property tax credit for homeowners and renters (Form IT-214)? It is limited to households with low income that paid real property taxes or rent; if unsure, read the Form IT-214 instructions before answering.
- **Encoded (Bool):** Input — Might you qualify for the New York real property tax credit for homeowners and renters (Form IT-214)? It is limited to households with low income that paid real property taxes or rent; if unsure, read the Form IT-214 instructions before answering.
- Expr: `{"op":"input","source":"Might you qualify for the New York real property tax credit for homeowners and renters (Form IT-214)? It is limited to households with low income that paid real property taxes or rent; if unsure, read the Form IT-214 instructions before answering."}`
- Cite: [ny_it201i] p. 19, Line 67, "Review the instructions for Form IT-214, Claim for Real Property Tax Credit for Homeowners and Renters, to see if you qualify for this credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.college_tuition`

- **Authored helper label:** Did you, your spouse or any dependent pay college tuition expenses during 2025?
- **Encoded (Bool):** Input — Did you, your spouse or any dependent pay college tuition expenses during 2025?
- Expr: `{"op":"input","source":"Did you, your spouse or any dependent pay college tuition expenses during 2025?"}`
- Cite: [ny_it201i] p. 19, Line 68, "Did you or your spouse or any dependents pay college tuition expenses during 2025?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.other_withholding`

- **Authored helper label:** Was any New York State, City or Yonkers tax withheld from a pension, annuity or IRA payment (Form 1099-R), unemployment or other government payment (Form 1099-G) or gambling winnings (Form W-2G)?
- **Encoded (Bool):** Input — Was any New York State, City or Yonkers tax withheld from a pension, annuity or IRA payment (Form 1099-R), unemployment or other government payment (Form 1099-G) or gambling winnings (Form W-2G)?
- Expr: `{"op":"input","source":"Was any New York State, City or Yonkers tax withheld from a pension, annuity or IRA payment (Form 1099-R), unemployment or other government payment (Form 1099-G) or gambling winnings (Form W-2G)?"}`
- Cite: [ny_it201i] p. 21, Lines 72, 73, and 74, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.refund_529`

- **Authored helper label:** Do you want part of a refund deposited into a New York 529 college savings account (Form IT-195)?
- **Encoded (Bool):** Input — Do you want part of a refund deposited into a New York 529 college savings account (Form IT-195)?
- Expr: `{"op":"input","source":"Do you want part of a refund deposited into a New York 529 college savings account (Form IT-195)?"}`
- Cite: [ny_it201i] p. 23, Line 78a, "Enter on line 78a the amount from Form IT-195, line 4." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.late_penalty`

- **Authored helper label:** Are you filing late or paying late, so that you owe a late filing or late payment penalty or interest?
- **Encoded (Bool):** Input — Are you filing late or paying late, so that you owe a late filing or late payment penalty or interest?
- Expr: `{"op":"input","source":"Are you filing late or paying late, so that you owe a late filing or late payment penalty or interest?"}`
- Cite: [ny_it201i] p. 24, Line 82, "If you owe a late filing penalty, late payment penalty, or interest:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.prior_agi_high`

- **Authored helper label:** Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?
- **Encoded (Bool):** Input — Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?
- Expr: `{"op":"input","source":"Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?"}`
- Cite: [ny_it201i] p. 23, Line 81, "if your 2024 New York adjusted gross income was more than $150,000 (or $75,000 if you are married filing separately for 2025)" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.abode_part_year`

- **Authored helper label:** Did you maintain a permanent place of abode in New York State for only part of 2025 (for sales and use tax purposes)?
- **Encoded (Bool):** Input — Did you maintain a permanent place of abode in New York State for only part of 2025 (for sales and use tax purposes)?
- Expr: `{"op":"input","source":"Did you maintain a permanent place of abode in New York State for only part of 2025 (for sales and use tax purposes)?"}`
- Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "If you maintained a permanent place of abode in New York State for sales and use tax purposes for only part of the year, multiply the tax amount from the chart by the number of months you maintained the permanent place of abode in New York State and divide the result by 12." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.prior_full_year`

- **Authored helper label:** Did you file a 2024 New York return covering a full 12 months?
- **Encoded (Bool):** Input — Did you file a 2024 New York return covering a full 12 months?
- Expr: `{"op":"input","source":"Did you file a 2024 New York return covering a full 12 months?"}`
- Cite: [ny_it201i] p. 23, Line 81, "In general, you are not subject to a penalty if your 2025 prepayments equal at least 100% of your 2024 New York income tax based on a 12-month return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.est_late`

- **Authored helper label:** Was any 2025 New York estimated tax installment paid late, or smaller than one quarter of the year's required payment?
- **Encoded (Bool):** Input — Was any 2025 New York estimated tax installment paid late, or smaller than one quarter of the year's required payment?
- Expr: `{"op":"input","source":"Was any 2025 New York estimated tax installment paid late, or smaller than one quarter of the year's required payment?"}`
- Cite: [ny_it201i] p. 23, Line 81, "if you underpaid your estimated tax liability for any payment period" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.spouse_resident`

- **Authored helper label:** On your joint return, was your spouse also a full-year New York State and New York City resident?
- **Encoded (Bool):** Input — On your joint return, was your spouse also a full-year New York State and New York City resident?
- Expr: `{"op":"input","source":"On your joint return, was your spouse also a full-year New York State and New York City resident?"}`
- Cite: [ny_it201i] p. 4, Item A, "One spouse is a New York State resident and the other is a nonresident or part-year resident." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.ask.prior_year_tax`

- **Authored helper label:** Your 2024 New York income tax (based on a 12-month return)
- **Encoded (NonNegDollars):** Input — What was your 2024 New York State and City income tax (the tax shown on your 2024 return, based on a 12-month return)?
- Expr: `{"op":"input","source":"What was your 2024 New York State and City income tax (the tax shown on your 2024 return, based on a 12-month return)?"}`
- Cite: [ny_it201i] p. 23, Line 81, "the amount of your 2024 New York income tax" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.part_year_state`

- **Authored helper label:** Not a New York State resident for all of 2025
- **Encoded (Bool):** helper "Were you (and your spouse, on a joint return) a New York State resident for all of 2025: domiciled in New York State, or keeping a permanent place of abode in New York State for substantially all of the year and spending 184 days or more there?" = false
- Expr: `{"eq":["ny_it201.ask.state_resident",{"const":false}],"op":"test"}`
- Cite: [ny_it201i] p. 3, New York State full-year residents: Who must file?, "If you were a New York State resident for only part of the year, do not file Form IT-201." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.part_year_city`

- **Authored helper label:** Not a New York City resident for all of 2025
- **Encoded (Bool):** helper "Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?" = false
- Expr: `{"eq":["ny_it201.ask.city_resident",{"const":false}],"op":"test"}`
- Cite: [ny_it201i] p. 14, Line 50: Part-year New York City resident tax, "If you were a New York City resident for only part of 2025, complete Form IT-360.1, Change of City Resident Status." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.spouse_nonresident`

- **Authored helper label:** A joint return with a spouse who was not a full-year New York State and City resident
- **Encoded (Bool):** f1040 line Filing Status = 'mfj' and helper "On your joint return, was your spouse also a full-year New York State and New York City resident?" = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["ny_it201.ask.spouse_resident",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 4, Item A, "One spouse is a New York State resident and the other is a nonresident or part-year resident." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.special_accrual`

- **Authored helper label:** Special accrual rules apply
- **Encoded (Bool):** helper "Were you a New York City nonresident on December 31, 2024, or will you be a New York State or City nonresident on January 1, 2026, and do you have income fixed and determinable in one tax year but reported federally in another (accrued income)?" = true
- Expr: `{"eq":["ny_it201.ask.special_accrual",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 31, Special accruals, "If you are subject to the special accrual rules, see the instructions for Form IT-225, addition modification number A-115 and subtraction modification number S-129." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.yonkers`

- **Authored helper label:** Yonkers living quarters or Yonkers wages
- **Encoded (Bool):** helper "Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?" = true
- Expr: `{"eq":["ny_it201.ask.yonkers",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 5, Item D2, "If you or your spouse (if married filing jointly) maintained or had use of an apartment or living quarters in Yonkers during any part of 2025" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.special_code`

- **Authored helper label:** A special condition code applies
- **Encoded (Bool):** helper "Does any New York special condition code apply to you (item G: for example A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1)?" = true
- Expr: `{"eq":["ny_it201.ask.special_code",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 5, Item G, "If you qualify for one or more of the special conditions below, enter the specified two-character code." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.decedent`

- **Authored helper label:** A decedent's return
- **Encoded (Bool):** helper "Is this return for a taxpayer (or spouse) who died after December 31, 2024?" = true
- Expr: `{"eq":["ny_it201.ask.decedent",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 4, Decedent information, "enter the date of death in the box labeled Taxpayer’s date of death" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## C — `ny_it201.item_c`

- **IRS:** Can you be claimed as a dependent on another taxpayer's federal return?
- **Encoded (Bool):** Enter the amount from helper "Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C).".
- Interpretation: amb.ny.2025.item_c
- Expr: `{"from":"ny_it201.ask.item_c","op":"copy"}`
- Cite: [ny_it201i] p. 5, Item C, "If you can be claimed as a dependent on another taxpayer’s federal return, you must mark an X in the Yes box." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## H (count) — `ny_it201.item_h_count`

- **IRS:** Number of dependents listed in item H
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Your dependent" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.claimed",{"const":true}],"op":"test"}}`
- Cite: [ny_it201i] p. 6, Item H, "Enter the required information for each dependent you claimed on federal Form 1040. Also enter the required information for any dependent you were entitled to claim on your federal return but chose not to" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 1 — `ny_it201.line1`

- **IRS:** Wages, salaries, tips, etc.
- **Encoded (NonNegDollars):** Round f1040 line 1z to the nearest multiple of (half up) $1.
- **Refusal:** when ny_it201.gate.part_year_state is true, cannot complete Form IT-203, Nonresident and Part-Year Resident Income Tax Return. This tool prepares Form IT-201 for a full-year New York State and New York City resident only; a nonresident or part-year resident files Form IT-203. Cite: [ny_it201i] p. 3, New York nonresidents and part-year residents, "you must file Form IT-203, Nonresident and Part-Year Resident Income Tax Return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.part_year_city is true, cannot complete Form IT-360.1, Change of City Resident Status. This tool computes the New York City resident tax for a full-year City resident only. Cite: [ny_it201i] p. 14, Line 50: Part-year New York City resident tax, "complete Form IT-360.1, Change of City Resident Status" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.spouse_nonresident is true, cannot complete Separate New York returns, or a joint return taxing both as residents. When one spouse was not a full-year New York State and City resident, New York requires separate returns or a joint return as if both were residents; this tool does neither. Cite: [ny_it201i] p. 3, Separate returns are required for some married taxpayers who file a joint federal return, "If one of you was a New York State resident and the other was a nonresident or part-year resident, you must each file a separate New York return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.special_accrual is true, cannot complete Form IT-225 (special accrual modifications A-115 and S-129). The special accrual rules for a change of residence are outside this tool. Cite: [ny_it201i] p. 31, Special accruals, "see the instructions for Form IT-225, addition modification number A-115 and subtraction modification number S-129" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.yonkers is true, cannot complete Yonkers lines 55 to 57 (Form Y-203 or IT-360.1). Yonkers resident surcharge and nonresident earnings tax are outside this tool. Cite: [ny_it201i] p. 5, Item D2, "you may be considered a resident or part-year resident for Yonkers income tax purposes" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.special_code is true, cannot complete Item G special condition codes. A special condition (for example Build America Bond interest, which changes the household credit income) is outside this tool. Cite: [ny_it201i] p. 13, Note 1, "if on Form IT-201 you entered special condition code A6 (for Build America Bond interest), your federal adjusted gross income is the line 19 amount minus any Build America Bond interest" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.decedent is true, cannot complete A deceased taxpayer's return. Returns for a taxpayer who died are outside this tool. Cite: [ny_it201i] p. 31, Deceased taxpayers, "the taxpayer’s spouse or personal representative may have to file and sign a return for that taxpayer" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line1z","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Wages, salaries, tips, etc." (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 2 — `ny_it201.line2`

- **IRS:** Taxable interest income
- **Encoded (Dollars):** Round f1040 line 2b to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line2b","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Taxable interest income" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 3 — `ny_it201.line3`

- **IRS:** Ordinary dividends
- **Encoded (NonNegDollars):** Round f1040 line 3b to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line3b","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Ordinary dividends" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 4 — `ny_it201.line4`

- **IRS:** Taxable refunds, credits, or offsets of state and local income taxes (also enter on line 25)
- **Encoded (NonNegDollars):** Round s1 line 1 to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line1","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Taxable refunds, credits, or offsets of state and local income taxes" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 5 — `ny_it201.line5`

- **IRS:** Alimony received
- **Encoded (NonNegDollars):** Round s1 line 2a to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line2a","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Alimony received" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 6 — `ny_it201.line6`

- **IRS:** Business income or loss (submit a copy of federal Schedule C, Form 1040)
- **Encoded (Dollars):** Round s1 line 3 to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line3","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Business income or loss" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 7 — `ny_it201.line7`

- **IRS:** Capital gain or loss (if required, submit a copy of federal Schedule D, Form 1040)
- **Encoded (Dollars):** Round f1040 line 7a to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line7a","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Capital gain or loss" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 8 — `ny_it201.line8`

- **IRS:** Other gains or losses (submit a copy of federal Form 4797)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Always zero for this tool, which refuses Form 4797 on the federal return (scope.schedule1).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Other gains or losses" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 9 — `ny_it201.line9`

- **IRS:** Taxable amount of IRA distributions
- **Encoded (NonNegDollars):** Round f1040 line 4b to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line4b","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Taxable amount of IRA distributions" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 10 — `ny_it201.line10`

- **IRS:** Taxable amount of pensions and annuities
- **Encoded (NonNegDollars):** Round f1040 line 5b to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line5b","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Taxable amount of pensions and annuities" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 11 — `ny_it201.line11`

- **IRS:** Rental real estate, royalties, partnerships, S corporations, trusts, etc.
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Always zero for this tool, which refuses Schedule E on the federal return (scope.schedule1).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Rental real estate, royalties, partnerships, S corporations, trusts, etc." (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 12 — `ny_it201.line12`

- **IRS:** Rental real estate included in line 11
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Rental real estate included in line 11" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 13 — `ny_it201.line13`

- **IRS:** Farm income or loss
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Always zero for this tool, which refuses Schedule F on the federal return (scope.schedule1).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Farm income or loss" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 14 — `ny_it201.line14`

- **IRS:** Unemployment compensation
- **Encoded (NonNegDollars):** Round s1 line 7 to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line7","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Unemployment compensation" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 15 — `ny_it201.line15`

- **IRS:** Taxable amount of Social Security benefits (also enter on line 27)
- **Encoded (NonNegDollars):** Round f1040 line 6b to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line6b","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Taxable amount of Social Security benefits" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 16 — `ny_it201.line16`

- **IRS:** Other income
- **Encoded (Dollars):** Round s1 line 9 to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line9","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Other income" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 17 — `ny_it201.line17`

- **IRS:** Add lines 1 through 11 and 13 through 16
- **Encoded (Dollars):** Add line 1, line 2, line 3, line 4, line 5, line 6, line 7, line 8, line 9, line 10, line 11, line 13, line 14, line 15, and line 16.
- Expr: `{"of":["ny_it201.line1","ny_it201.line2","ny_it201.line3","ny_it201.line4","ny_it201.line5","ny_it201.line6","ny_it201.line7","ny_it201.line8","ny_it201.line9","ny_it201.line10","ny_it201.line11","ny_it201.line13","ny_it201.line14","ny_it201.line15","ny_it201.line16"],"op":"sum"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Add lines 1 through 11 and 13 through 16" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 18 — `ny_it201.line18`

- **IRS:** Total federal adjustments to income
- **Encoded (NonNegDollars):** Round s1 line 26 to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"s1.line26","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Total federal adjustments to income" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 19 — `ny_it201.line19`

- **IRS:** Federal adjusted gross income (subtract line 18 from line 17)
- **Encoded (Dollars):** Subtract line 18 from line 17.
- Expr: `{"from":"ny_it201.line17","op":"subtract","take":"ny_it201.line18"}`
- Cite: [ny_it201] p. 2, Federal income and adjustments, "Federal adjusted gross income ( subtract line 18 from line 17 )" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (helper) — `ny_it201.fagi_rounded`

- **Authored helper label:** Federal adjusted gross income (Form 1040 line 11a) rounded to the whole dollar
- **Encoded (Dollars):** Round f1040 line 11a to the nearest multiple of (half up) $1.
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"of":"f1040.line11a","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it201i] p. 7, Lines 1 through 19: Federal income tax return information, "including your income and federal adjustments to income" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (check) — `ny_it201.line19_agrees`

- **Authored helper label:** Line 19 equals federal adjusted gross income rounded to the whole dollar
- **Encoded (Bool):** line 19 = helper "Federal adjusted gross income (Form 1040 line 11a) rounded to the whole dollar"
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"eq":["ny_it201.line19","ny_it201.fagi_rounded"],"op":"test"}`
- Cite: [ny_it201i] p. 7, Lines 1 through 19: Federal income tax return information, "The calculation of your New York State, New York City, and Yonkers income tax is based on the information you reported on your federal income tax return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.line20`

- **Authored helper label:** Out-of-state municipal bond interest
- **Encoded (Bool):** helper "Did you have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?" = true
- Expr: `{"eq":["ny_it201.ask.out_of_state_bond_interest",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 7, Line 20, "If Yes, enter any such interest income that you received or that was credited to you during 2025 that was not included in your federal adjusted gross income." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 20 — `ny_it201.line20`

- **IRS:** Interest income on state and local bonds and obligations (but not those of NYS or its local governments)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line20 is true, cannot complete Form IT-201 line 20 (addition for other states' bond interest). This addition is not computed by this tool (decision B4). Cite: [ny_it201i] p. 7, Line 20, "enter any such interest income that you received or that was credited to you during 2025 that was not included in your federal adjusted gross income" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York additions, "Interest income on state and local bonds and obligations" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.line21`

- **Authored helper label:** Public employee 414(h) contributions
- **Encoded (Bool):** helper "Are you a public employee of New York State or its local governments with 414(h) retirement contributions shown on a Form W-2?" = true
- Expr: `{"eq":["ny_it201.ask.414h",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 8, Line 21, "If Yes, enter the amount of 414(h) retirement contributions, if shown on any federal Form W-2" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 21 — `ny_it201.line21`

- **IRS:** Public employee 414(h) retirement contributions from your wage and tax statements
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line21 is true, cannot complete Form IT-201 line 21 (414(h) contributions). This addition is not computed by this tool (decision B4). Cite: [ny_it201i] p. 8, Line 21, "enter the amount of 414(h) retirement contributions, if shown on any federal Form W-2" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York additions, "Public employee 414(h) retirement contributions" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.line22`

- **Authored helper label:** A nonqualified New York 529 withdrawal
- **Encoded (Bool):** helper "Did you make a nonqualified withdrawal during 2025 from an account under New York's 529 college savings program?" = true
- Expr: `{"eq":["ny_it201.ask.529_nonqualified",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 8, Line 22, "If Yes, the withdrawal is a nonqualified withdrawal and you must complete the Line 22 worksheet." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 22 — `ny_it201.line22`

- **IRS:** New York’s 529 college savings program distributions
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line22 is true, cannot complete Form IT-201 line 22 and its worksheet. This addition is not computed by this tool (decision B4). Cite: [ny_it201i] p. 8, Line 22, "you must complete the Line 22 worksheet" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York additions, "New York’s 529 college savings program distributions" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.it225`

- **Authored helper label:** Other New York additions or subtractions (Form IT-225)
- **Encoded (Bool):** helper "Does any other New York addition or subtraction on Form IT-225 apply to you, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?" = true
- Expr: `{"eq":["ny_it201.ask.it225",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 7, Step 4, "See below and Form IT-225, New York State Modifications, and its instructions." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 23 — `ny_it201.line23`

- **IRS:** Other (Form IT-225, line 9)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.it225 is true, cannot complete Form IT-225, New York State Modifications. Other New York additions and subtractions are not computed by this tool. Cite: [ny_it201i] p. 8, Line 23, "Enter on line 23 the amount from Form IT-225, line 9. Submit Form IT-225 with your return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York additions, "Other (Form IT-225, line 9)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 24 — `ny_it201.line24`

- **IRS:** Add lines 19 through 23
- **Encoded (Dollars):** Add line 19, line 20, line 21, line 22, and line 23.
- Expr: `{"of":["ny_it201.line19","ny_it201.line20","ny_it201.line21","ny_it201.line22","ny_it201.line23"],"op":"sum"}`
- Cite: [ny_it201] p. 2, New York additions, "Add lines 19 through 23" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.line25`

- **Authored helper label:** Line 4 is more than zero or an inflation refund check was included in federal AGI
- **Encoded (Bool):** (line 4 > $0 or helper "Did you receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?" = true)
- Expr: `{"any":[{"gt":["ny_it201.line4",{"const":0}],"op":"test"},{"eq":["ny_it201.ask.inflation_check",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 8, Line 25, "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 25 — `ny_it201.line25`

- **IRS:** Taxable refunds, credits, or offsets of state and local income taxes (from line 4)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line25 is true, cannot complete Form IT-201 line 25. Whether line 25 is the line 4 amount (the form) or only an inflation refund check (the 2025 instructions) is unsettled; this tool refuses either case (decision B1). Cite: [ny_it201i] p. 8, Line 25, "then enter that amount on line 25" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Interpretation: amb.ny.2025.line25
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Taxable refunds, credits, or offsets of state and local income taxes (from line 4)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (helper) — `ny_it201.no`

- **Authored helper label:** No
- **Encoded (Bool):** Enter false (ny.false).
- Expr: `{"op":"param","ref":"ny.false"}`
- Cite: [ny_it201i] p. 9, Line 26, "If No, go to line 27." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.has_pension_income`

- **Authored helper label:** Is there taxable IRA, pension or annuity income on line 9 or 10?
- **Encoded (Bool):** (line 9 > $0 or line 10 > $0)
- Note: Within this tool, pension, annuity and IRA income in federal adjusted gross income is on federal lines 4b and 5b (IT-201 lines 9 and 10): the federal screens refuse a disability pension reported as wages (retirement.special, scope.other_income) and a pension from a nonqualified plan or a nongovernmental section 457 plan on Schedule 1 line 8t (s1.line8_other).
- Expr: `{"any":[{"gt":["ny_it201.line9",{"const":0}],"op":"test"},{"gt":["ny_it201.line10",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 9, Line 29, "Did you enter an amount of pension income or annuity income, or both (generally reported on line 9 or 10)"; p. 9, Line 26, "Did you receive a pension or other distribution from a New York State or local government pension plan or federal government pension plan that was included in your federal adjusted gross income?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.line26`

- **Authored helper label:** A New York or federal government pension
- **Encoded (Bool):** Choose — [helper "Is there taxable IRA, pension or annuity income on line 9 or 10?" = true → helper "Did you or your spouse receive a pension or other distribution included in federal adjusted gross income from a New York State or local government pension plan or a federal government pension plan, including a return of your own contributions before retirement? Count the military, a U.S. territory or the District of Columbia, the MTA Police 20-Year Retirement Program, MABSTOA, the Long Island Rail Road, and the Optional Retirement Program of SUNY, CUNY or the State Education Department (for example an annuity paid by TIAA), whether received as an employee, as a beneficiary, or as a former spouse under a domestic relations order."] [helper "Is there taxable IRA, pension or annuity income on line 9 or 10?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.has_pension_income",{"const":true}],"op":"test"},"then":"ny_it201.ask.gov_pension"},{"guard":{"eq":["ny_it201.has_pension_income",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 9, Line 26, "If Yes, enter the amount of any pension you received" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 26 — `ny_it201.line26`

- **IRS:** Pensions of NYS and local governments and the federal government
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line26 is true, cannot complete Form IT-201 line 26. This subtraction is not computed by this tool (decision B4). Cite: [ny_it201i] p. 9, Line 26, "enter the amount of any pension you received" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Pensions of NYS and local governments and the federal government" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 27 — `ny_it201.line27`

- **IRS:** Taxable amount of Social Security benefits (from line 15)
- **Encoded (Dollars):** Enter the amount from line 15.
- Expr: `{"from":"ny_it201.line15","op":"copy"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Taxable amount of Social Security benefits (from line 15)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.has_line28_income`

- **Authored helper label:** Is there an amount on line 2, 3, 6 or 11 (interest, dividends, business income, or partnership and similar income)?
- **Encoded (Bool):** (line 2 ≠ $0 or line 3 ≠ $0 or line 6 ≠ $0 or line 11 ≠ $0)
- Expr: `{"any":[{"ne":["ny_it201.line2",{"const":0}],"op":"test"},{"ne":["ny_it201.line3",{"const":0}],"op":"test"},{"ne":["ny_it201.line6",{"const":0}],"op":"test"},{"ne":["ny_it201.line11",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 9, Line 28, "Did you include interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11?" and "Dividends you received from a regulated investment company (mutual fund) that invests in obligations of the U.S. government and meet the 50% asset requirement each quarter qualify for this subtraction." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.line28`

- **Authored helper label:** Interest on U.S. government obligations
- **Encoded (Bool):** Choose — [helper "Is there an amount on line 2, 3, 6 or 11 (interest, dividends, business income, or partnership and similar income)?" = true → helper "Did you include interest from U.S. government bonds or other U.S. government obligations (for example Treasury bills, notes or bonds, or U.S. savings bonds), or dividends from a fund investing in them, in federal income?"] [helper "Is there an amount on line 2, 3, 6 or 11 (interest, dividends, business income, or partnership and similar income)?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.has_line28_income",{"const":true}],"op":"test"},"then":"ny_it201.ask.us_obligation_interest"},{"guard":{"eq":["ny_it201.has_line28_income",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 9, Line 28, "If Yes, enter the amount of interest income you earned from bonds or other obligations of the U.S. government." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 28 — `ny_it201.line28`

- **IRS:** Interest income on U.S. government bonds
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line28 is true, cannot complete Form IT-201 line 28. This subtraction is not computed by this tool (decision B4); it would lower your New York tax. Cite: [ny_it201i] p. 9, Line 28, "enter the amount of interest income you earned from bonds or other obligations of the U.S. government" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Interest income on U.S. government bonds" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.line29`

- **Authored helper label:** Pension and annuity income exclusion may apply
- **Encoded (Bool):** Choose — [helper "Is there taxable IRA, pension or annuity income on line 9 or 10?" = true → helper "Did you or your spouse have pension or annuity income or IRA distributions (periodic or lump-sum) included in federal adjusted gross income other than a government pension subtracted on line 26 (periodic distributions from a government section 457 deferred compensation plan count here), and was the person who received it 59 1/2 or older in 2025 (or did they receive it as a beneficiary)?"] [helper "Is there taxable IRA, pension or annuity income on line 9 or 10?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.has_pension_income",{"const":true}],"op":"test"},"then":"ny_it201.ask.pension_exclusion"},{"guard":{"eq":["ny_it201.has_pension_income",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 9, Line 29, "If Yes, and you were 59½ before January 1, 2025, enter the qualifying pension and annuity income included in your 2025 federal adjusted gross income, but not more than $20,000." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 29 — `ny_it201.line29`

- **IRS:** Pension and annuity income exclusion
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line29 is true, cannot complete Form IT-201 line 29. This subtraction is not computed by this tool (decision B4). Cite: [ny_it201i] p. 9, Line 29, "but not more than $20,000" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Pension and annuity income exclusion" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.line30`

- **Authored helper label:** New York 529 contributions or withdrawals
- **Encoded (Bool):** helper "During 2025, did you, as an account owner, contribute to or withdraw from a New York 529 college savings account, or, as a beneficiary, receive a withdrawal included in federal adjusted gross income?" = true
- Expr: `{"eq":["ny_it201.ask.529_owner",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 10, Line 30, "as an account owner, made contributions, enter the amount up to $5,000 ($10,000 for married taxpayers filing a joint return) on line 1 of the Line 30 worksheet" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 30 — `ny_it201.line30`

- **IRS:** New York’s 529 college savings program deduction/earnings
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.line30 is true, cannot complete Form IT-201 line 30 and its worksheet. This subtraction is not computed by this tool (decision B4). Cite: [ny_it201i] p. 10, Line 30, "on line 1 of the Line 30 worksheet" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "New York’s 529 college savings program deduction/earnings" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 31 — `ny_it201.line31`

- **IRS:** Other (Form IT-225, line 18)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.it225 is true, cannot complete Form IT-225, New York State Modifications. Other New York additions and subtractions are not computed by this tool. Cite: [ny_it201i] p. 10, Line 31, "Enter on line 31 the amount from Form IT-225, line 18. Submit Form IT-225 with your return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Other ( Form IT-225, line 18)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 32 — `ny_it201.line32`

- **IRS:** Add lines 25 through 31
- **Encoded (Dollars):** Add line 25, line 26, line 27, line 28, line 29, line 30, and line 31.
- Expr: `{"of":["ny_it201.line25","ny_it201.line26","ny_it201.line27","ny_it201.line28","ny_it201.line29","ny_it201.line30","ny_it201.line31"],"op":"sum"}`
- Cite: [ny_it201] p. 2, New York subtractions, "Add lines 25 through 31" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 33 — `ny_it201.line33`

- **IRS:** New York adjusted gross income (subtract line 32 from line 24)
- **Encoded (Dollars):** Subtract line 32 from line 24.
- Expr: `{"from":"ny_it201.line24","op":"subtract","take":"ny_it201.line32"}`
- Cite: [ny_it201] p. 2, New York subtractions, "New York adjusted gross income (subtract line 32 from line 24)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.itemize`

- **Authored helper label:** Itemizing on the New York return
- **Encoded (Bool):** helper "Is your New York itemized deduction (Form IT-196) larger than your New York standard deduction, or are you married filing separately with a spouse who itemizes on their New York return?" = true
- Expr: `{"eq":["ny_it201.ask.itemize",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 11, Line 34, "To calculate your New York itemized deduction, use Form IT-196" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.dependent_single`

- **Authored helper label:** Single and item C Yes
- **Encoded (Bool):** f1040 line Filing Status = 'single' and line C = true
- Expr: `{"all":[{"eq":["f1040.status",{"const":"single"}],"op":"test"},{"eq":["ny_it201.item_c",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i-html] New York State standard deduction table, "① Single and you marked item C Yes", "$3,100" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table) — `ny_it201.std_deduction`

- **Authored helper label:** New York State standard deduction for the filing status
- **Encoded (NonNegDollars):** Enter single $8,000; mfj $16,050; mfs $8,000; hoh $11,200; qss $16,050 (ny.std_deduction).
- Expr: `{"op":"param","ref":"ny.std_deduction"}`
- Cite: [ny_it201i-html] New York State standard deduction table, "Standard deduction (enter on line 34)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table) — `ny_it201.std_deduction_dependent`

- **Authored helper label:** Single and you marked item C Yes
- **Encoded (NonNegDollars):** Enter $3,100 (ny.std_deduction.dependent_single).
- Expr: `{"op":"param","ref":"ny.std_deduction.dependent_single"}`
- Cite: [ny_it201i-html] New York State standard deduction table, "① Single and you marked item C Yes" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 34 — `ny_it201.line34`

- **IRS:** Enter your standard deduction
- **Encoded (NonNegDollars):** Choose — [helper "Single and item C Yes" = true → column (table) (ny_it201.std_deduction_dependent)] [helper "Single and item C Yes" = false → column (table) (ny_it201.std_deduction)]
- **Refusal:** when ny_it201.gate.itemize is true, cannot complete Form IT-196, New York Resident, Nonresident, and Part-Year Resident Itemized Deductions. This tool takes the New York standard deduction only. Cite: [ny_it201i] p. 11, Notes, "If you choose the itemized deduction, you must submit Form IT-196 with your return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.dependent_single",{"const":true}],"op":"test"},"then":"ny_it201.std_deduction_dependent"},{"guard":{"eq":["ny_it201.dependent_single",{"const":false}],"op":"test"},"then":"ny_it201.std_deduction"}],"op":"choose"}`
- Cite: [ny_it201i] p. 11, New York State standard deduction table, "Standard deduction" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 35 — `ny_it201.line35`

- **IRS:** Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
- **Encoded (NonNegDollars):** Subtract line 34 from line 33. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line33","op":"subtract_floor0","take":"ny_it201.line34"}`
- Cite: [ny_it201] p. 2, Standard deduction or itemized deduction, "Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (helper) — `ny_it201.exemption`

- **Authored helper label:** The value of each New York State dependent exemption
- **Encoded (NonNegDollars):** Enter $1,000 (ny.dependent_exemption).
- Expr: `{"op":"param","ref":"ny.dependent_exemption"}`
- Cite: [ny_it201i] p. 11, Line 36: Dependent exemption amount, "The value of each New York State dependent exemption is $1,000." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 36 — `ny_it201.line36`

- **IRS:** Dependent exemption amount (multiply the number of dependents listed in item H by 1,000)
- **Encoded (NonNegDollars):** Multiply helper "The value of each New York State dependent exemption" by the number on line H (count).
- Expr: `{"amount":"ny_it201.exemption","count":"ny_it201.item_h_count","op":"multiply_count"}`
- Cite: [ny_it201i] p. 11, Line 36: Dependent exemption amount, "Multiply the number of your dependents listed on Form IT-201, item H" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 37 — `ny_it201.line37`

- **IRS:** Taxable income (subtract line 36 from line 35)
- **Encoded (NonNegDollars):** Subtract line 36 from line 35. If zero or less, enter -0-.
- Note: The instructions say "If line 36 is more than line 35, leave line 37 and line 38 blank"; a blank is read as zero.
- Expr: `{"from":"ny_it201.line35","op":"subtract_floor0","take":"ny_it201.line36"}`
- Cite: [ny_it201i] p. 11, Lines 37 and 38: Taxable income, "Subtract line 36 from line 35. The result is your taxable income." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 38 — `ny_it201.line38`

- **IRS:** Taxable income (from line 37 on page 2)
- **Encoded (NonNegDollars):** Enter the amount from line 37.
- Expr: `{"from":"ny_it201.line37","op":"copy"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Taxable income (from line 37 on page 2)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.agi_table_range`

- **Authored helper label:** Is line 33 (your New York adjusted gross income) $107,650 or less?
- **Encoded (Bool):** line 33 ≤ $107,650 (ny.table.agi_limit)
- Expr: `{"le":["ny_it201.line33",{"param":"ny.table.agi_limit"}],"op":"test"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "Is line 33 (your New York adjusted gross income) $107,650 or less?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.ti_table_range`

- **Authored helper label:** Is line 38 less than $65,000?
- **Encoded (Bool):** line 38 < $65,000 (ny.table.limit)
- Expr: `{"lt":["ny_it201.line38",{"param":"ny.table.limit"}],"op":"test"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "or if line 38 is $65,000 or more, use the New York State tax rate schedule below" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (39) — `ny_it201.tax_table`

- **Authored helper label:** New York State tax from the 2025 New York State Tax Table
- **Encoded (NonNegDollars):** Use 2025 New York State Tax Table at line 38 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.line38","op":"table_lookup","status":"f1040.status","table":"ny_tax_table"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "find your New York State tax using the 2025 New York State Tax Table" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (39) — `ny_it201.tax_schedule`

- **Authored helper label:** New York State tax from the New York State tax rate schedule
- **Encoded (NonNegDollars):** Enter "tax" of New York State tax rate schedule with amount = line 38 and status = f1040 line Filing Status.
- Expr: `{"from":{"bind":{"amount":"ny_it201.line38","status":"f1040.status"},"def":"ny_rs","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "use the New York State tax rate schedule below" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (39) — `ny_it201.tax_low`

- **Authored helper label:** Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable income, the rate schedule at $65,000 or more
- **Encoded (NonNegDollars):** Choose — [helper "Is line 38 less than $65,000?" = true → column (39) (ny_it201.tax_table)] [helper "Is line 38 less than $65,000?" = false → column (39) (ny_it201.tax_schedule)]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.ti_table_range",{"const":true}],"op":"test"},"then":"ny_it201.tax_table"},{"guard":{"eq":["ny_it201.ti_table_range",{"const":false}],"op":"test"},"then":"ny_it201.tax_schedule"}],"op":"choose"}`
- Cite: [ny_it201i] p. 32, How to calculate your 2025 New York State tax, "NYS taxable income is $65,000 or more (line 38)" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (39) — `ny_it201.tcw.w1`

- **Authored helper label:** Tax computation worksheet 1
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650) with agi = line 33, rate = 55/1000 (ny.tcw.first.rate), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","rate":{"param":"ny.tcw.first.rate"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw_first","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w7`

- **Authored helper label:** Tax computation worksheet 7
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650) with agi = line 33, rate = 6% (0.06) (ny.tcw.first.rate6), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","rate":{"param":"ny.tcw.first.rate6"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw_first","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 7, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w12`

- **Authored helper label:** Tax computation worksheet 12
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650) with agi = line 33, rate = 6% (0.06) (ny.tcw.first.rate6), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","rate":{"param":"ny.tcw.first.rate6"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw_first","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 12, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w2`

- **Authored helper label:** Tax computation worksheet 2
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $807 (ny.tcw.mfj.w2.incremental), recapture = $333 (ny.tcw.mfj.w2.recapture), start = $161,550 (ny.tcw.mfj.w2.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.mfj.w2.incremental"},"recapture":{"param":"ny.tcw.mfj.w2.recapture"},"start":{"param":"ny.tcw.mfj.w2.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w3`

- **Authored helper label:** Tax computation worksheet 3
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $2,747 (ny.tcw.mfj.w3.incremental), recapture = $1,140 (ny.tcw.mfj.w3.recapture), start = $323,200 (ny.tcw.mfj.w3.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.mfj.w3.incremental"},"recapture":{"param":"ny.tcw.mfj.w3.recapture"},"start":{"param":"ny.tcw.mfj.w3.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 3, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w4`

- **Authored helper label:** Tax computation worksheet 4
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $60,350 (ny.tcw.mfj.w4.incremental), recapture = $3,887 (ny.tcw.mfj.w4.recapture), start = $2,155,350 (ny.tcw.mfj.w4.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.mfj.w4.incremental"},"recapture":{"param":"ny.tcw.mfj.w4.recapture"},"start":{"param":"ny.tcw.mfj.w4.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 4, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w5`

- **Authored helper label:** Tax computation worksheet 5
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $32,500 (ny.tcw.mfj.w5.incremental), recapture = $64,237 (ny.tcw.mfj.w5.recapture), start = $5,000,000 (ny.tcw.mfj.w5.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.mfj.w5.incremental"},"recapture":{"param":"ny.tcw.mfj.w5.recapture"},"start":{"param":"ny.tcw.mfj.w5.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 5, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w8`

- **Authored helper label:** Tax computation worksheet 8
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $1,831 (ny.tcw.single.w8.incremental), recapture = $568 (ny.tcw.single.w8.recapture), start = $215,400 (ny.tcw.single.w8.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.single.w8.incremental"},"recapture":{"param":"ny.tcw.single.w8.recapture"},"start":{"param":"ny.tcw.single.w8.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 8, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w9`

- **Authored helper label:** Tax computation worksheet 9
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $30,172 (ny.tcw.single.w9.incremental), recapture = $2,399 (ny.tcw.single.w9.recapture), start = $1,077,550 (ny.tcw.single.w9.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.single.w9.incremental"},"recapture":{"param":"ny.tcw.single.w9.recapture"},"start":{"param":"ny.tcw.single.w9.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 9, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w10`

- **Authored helper label:** Tax computation worksheet 10
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $32,500 (ny.tcw.single.w10.incremental), recapture = $32,571 (ny.tcw.single.w10.recapture), start = $5,000,000 (ny.tcw.single.w10.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.single.w10.incremental"},"recapture":{"param":"ny.tcw.single.w10.recapture"},"start":{"param":"ny.tcw.single.w10.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 10, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w13`

- **Authored helper label:** Tax computation worksheet 13
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $2,289 (ny.tcw.hoh.w13.incremental), recapture = $787 (ny.tcw.hoh.w13.recapture), start = $269,300 (ny.tcw.hoh.w13.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.hoh.w13.incremental"},"recapture":{"param":"ny.tcw.hoh.w13.recapture"},"start":{"param":"ny.tcw.hoh.w13.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 13, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w14`

- **Authored helper label:** Tax computation worksheet 14
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $45,261 (ny.tcw.hoh.w14.incremental), recapture = $3,076 (ny.tcw.hoh.w14.recapture), start = $1,616,450 (ny.tcw.hoh.w14.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.hoh.w14.incremental"},"recapture":{"param":"ny.tcw.hoh.w14.recapture"},"start":{"param":"ny.tcw.hoh.w14.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 14, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.w15`

- **Authored helper label:** Tax computation worksheet 15
- **Encoded (NonNegDollars):** Enter "tax" of Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650) with agi = line 33, incremental = $32,500 (ny.tcw.hoh.w15.incremental), recapture = $48,337 (ny.tcw.hoh.w15.recapture), start = $5,000,000 (ny.tcw.hoh.w15.start), status = f1040 line Filing Status, and ti = line 38.
- Expr: `{"from":{"bind":{"agi":"ny_it201.line33","incremental":{"param":"ny.tcw.hoh.w15.incremental"},"recapture":{"param":"ny.tcw.hoh.w15.recapture"},"start":{"param":"ny.tcw.hoh.w15.start"},"status":"f1040.status","ti":"ny_it201.line38"},"def":"ny_tcw","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 15, "then you must calculate your tax using this worksheet" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.top`

- **Authored helper label:** Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.9%
- **Encoded (NonNegDollars):** Multiply line 38 by 109/1000 (ny.tcw.top_rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"ny_it201.line38","op":"multiply_rate","rate":{"param":"ny.tcw.top_rate"},"unit":100}`
- Cite: [ny_it201i-html] Tax computation worksheet 6, "Multiply line 1 by 10.9% (0.109)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.mfj`

- **Authored helper label:** Married filing jointly and qualifying surviving spouse: the worksheet for the taxable income
- **Encoded (NonNegDollars):** Choose — [line 38 ≥ $0 and line 38 ≤ $161,550 (ny.tcw.mfj.w1.ti_limit) → column (39) (ny_it201.tcw.w1)] [line 38 > $161,550 (ny.tcw.mfj.w1.ti_limit) and line 38 ≤ $323,200 (ny.tcw.mfj.w2.ti_limit) → column (39) (ny_it201.tcw.w2)] [line 38 > $323,200 (ny.tcw.mfj.w2.ti_limit) and line 38 ≤ $2,155,350 (ny.tcw.mfj.w3.ti_limit) → column (39) (ny_it201.tcw.w3)] [line 38 > $2,155,350 (ny.tcw.mfj.w3.ti_limit) and line 38 ≤ $5,000,000 (ny.tcw.mfj.w4.ti_limit) → column (39) (ny_it201.tcw.w4)] [line 38 > $5,000,000 (ny.tcw.mfj.w4.ti_limit) → column (39) (ny_it201.tcw.w5)]
- Interpretation: amb.ny.2025.recapture_selection
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.line38",{"const":0}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.mfj.w1.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w1"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.mfj.w1.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.mfj.w2.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w2"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.mfj.w2.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.mfj.w3.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w3"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.mfj.w3.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.mfj.w4.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w4"},{"guard":{"gt":["ny_it201.line38",{"param":"ny.tcw.mfj.w4.ti_limit"}],"op":"test"},"then":"ny_it201.tcw.w5"}],"op":"choose"}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.single`

- **Authored helper label:** Single and married filing separately: the worksheet for the taxable income
- **Encoded (NonNegDollars):** Choose — [line 38 ≥ $0 and line 38 ≤ $215,400 (ny.tcw.single.w1.ti_limit) → column (39) (ny_it201.tcw.w7)] [line 38 > $215,400 (ny.tcw.single.w1.ti_limit) and line 38 ≤ $1,077,550 (ny.tcw.single.w8.ti_limit) → column (39) (ny_it201.tcw.w8)] [line 38 > $1,077,550 (ny.tcw.single.w8.ti_limit) and line 38 ≤ $5,000,000 (ny.tcw.single.w9.ti_limit) → column (39) (ny_it201.tcw.w9)] [line 38 > $5,000,000 (ny.tcw.single.w9.ti_limit) → column (39) (ny_it201.tcw.w10)]
- Interpretation: amb.ny.2025.recapture_selection
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.line38",{"const":0}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.single.w1.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w7"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.single.w1.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.single.w8.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w8"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.single.w8.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.single.w9.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w9"},{"guard":{"gt":["ny_it201.line38",{"param":"ny.tcw.single.w9.ti_limit"}],"op":"test"},"then":"ny_it201.tcw.w10"}],"op":"choose"}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.hoh`

- **Authored helper label:** Head of household: the worksheet for the taxable income
- **Encoded (NonNegDollars):** Choose — [line 38 ≥ $0 and line 38 ≤ $269,300 (ny.tcw.hoh.w1.ti_limit) → column (39) (ny_it201.tcw.w12)] [line 38 > $269,300 (ny.tcw.hoh.w1.ti_limit) and line 38 ≤ $1,616,450 (ny.tcw.hoh.w13.ti_limit) → column (39) (ny_it201.tcw.w13)] [line 38 > $1,616,450 (ny.tcw.hoh.w13.ti_limit) and line 38 ≤ $5,000,000 (ny.tcw.hoh.w14.ti_limit) → column (39) (ny_it201.tcw.w14)] [line 38 > $5,000,000 (ny.tcw.hoh.w14.ti_limit) → column (39) (ny_it201.tcw.w15)]
- Interpretation: amb.ny.2025.recapture_selection
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.line38",{"const":0}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.hoh.w1.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w12"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.hoh.w1.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.hoh.w13.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w13"},{"guard":{"all":[{"gt":["ny_it201.line38",{"param":"ny.tcw.hoh.w13.ti_limit"}],"op":"test"},{"le":["ny_it201.line38",{"param":"ny.tcw.hoh.w14.ti_limit"}],"op":"test"}],"op":"test"},"then":"ny_it201.tcw.w14"},{"guard":{"gt":["ny_it201.line38",{"param":"ny.tcw.hoh.w14.ti_limit"}],"op":"test"},"then":"ny_it201.tcw.w15"}],"op":"choose"}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tcw.by_status`

- **Authored helper label:** The tax computation worksheet for the filing status
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → column (39) (ny_it201.tcw.single)] [f1040 line Filing Status = 'mfj' → column (39) (ny_it201.tcw.mfj)] [f1040 line Filing Status = 'qss' → column (39) (ny_it201.tcw.mfj)] [f1040 line Filing Status = 'mfs' → column (39) (ny_it201.tcw.single)] [f1040 line Filing Status = 'hoh' → column (39) (ny_it201.tcw.hoh)]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"ny_it201.tcw.single"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"ny_it201.tcw.mfj"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"ny_it201.tcw.mfj"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"ny_it201.tcw.single"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"ny_it201.tcw.hoh"}],"op":"choose"}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (gate) — `ny_it201.agi_top`

- **Authored helper label:** Is line 33 more than $25,000,000?
- **Encoded (Bool):** line 33 > $25,000,000 (ny.tcw.agi_top)
- Expr: `{"gt":["ny_it201.line33",{"param":"ny.tcw.agi_top"}],"op":"test"}`
- Cite: [ny_it201i-html] Tax computation worksheet 6, "If your New York adjusted gross income (line 33) is more than $25,000,000, then you must calculate your tax using this worksheet." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (39) — `ny_it201.tax_high`

- **Authored helper label:** Tax for New York AGI of more than $107,650: the tax computation worksheets
- **Encoded (NonNegDollars):** Choose — [helper "Is line 33 more than $25,000,000?" = true → column (39) (ny_it201.tcw.top)] [helper "Is line 33 more than $25,000,000?" = false → column (39) (ny_it201.tcw.by_status)]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.agi_top",{"const":true}],"op":"test"},"then":"ny_it201.tcw.top"},{"guard":{"eq":["ny_it201.agi_top",{"const":false}],"op":"test"},"then":"ny_it201.tcw.by_status"}],"op":"choose"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "If No, see Tax computation – New York adjusted gross income of more than $107,650 below." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 39 — `ny_it201.line39`

- **IRS:** NYS tax on line 38 amount
- **Encoded (NonNegDollars):** Choose — [helper "Is line 33 (your New York adjusted gross income) $107,650 or less?" = true → column (39) (ny_it201.tax_low)] [helper "Is line 33 (your New York adjusted gross income) $107,650 or less?" = false → column (39) (ny_it201.tax_high)]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.agi_table_range",{"const":true}],"op":"test"},"then":"ny_it201.tax_low"},{"guard":{"eq":["ny_it201.agi_table_range",{"const":false}],"op":"test"},"then":"ny_it201.tax_high"}],"op":"choose"}`
- Cite: [ny_it201i] p. 12, Line 39 – New York State tax, "Is line 33 (your New York adjusted gross income) $107,650 or less?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (Note 1) — `ny_it201.hh_agi`

- **Authored helper label:** Federal adjusted gross income for the household credit tables (line 19; a negative amount is in the first row)
- **Encoded (NonNegDollars):** Subtract $0 from line 19. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line19","op":"subtract_floor0","take":{"const":0}}`
- Cite: [ny_it201i] p. 13, Use these notes for New York State household credit tables 1 through 3, "Note 1 For most taxpayers, federal adjusted gross income is the amount from Form IT-201, line 19.", "Note 2 This amount could be 0 or a negative amount." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (helper) — `ny_it201.one`

- **Authored helper label:** One for you
- **Encoded (Count):** Enter 1 (ny.one).
- Expr: `{"op":"param","ref":"ny.one"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "plus one for you (and one for your spouse if Married filing joint return) is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (helper) — `ny_it201.spouse_count`

- **Authored helper label:** One for your spouse if married filing joint return
- **Encoded (Count):** Find the entry in Household credit tables: one for your spouse if married filing joint return for status f1040 line Filing Status.
- Expr: `{"keys":["f1040.status"],"op":"keyed_lookup","table":"ny_hh_spouse_count"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "(and one for your spouse if Married filing joint return)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (column) — `ny_it201.hh_people`

- **Authored helper label:** The number of dependents listed in item H, plus one for you (and one for your spouse if married filing joint return)
- **Encoded (Count):** Add line H (count), helper "One for you", and helper "One for your spouse if married filing joint return".
- Expr: `{"of":["ny_it201.item_h_count","ny_it201.one","ny_it201.spouse_count"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "And the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return) is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 1) — `ny_it201.hh_state_p1`

- **Authored helper label:** New York State household credit table 2, column 1
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 1 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p1"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 1) — `ny_it201.hh_city_p1`

- **Authored helper label:** New York City household credit table 5, column 1
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 1 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p1"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 2) — `ny_it201.hh_state_p2`

- **Authored helper label:** New York State household credit table 2, column 2
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 2 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p2"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 2) — `ny_it201.hh_city_p2`

- **Authored helper label:** New York City household credit table 5, column 2
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 2 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p2"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 3) — `ny_it201.hh_state_p3`

- **Authored helper label:** New York State household credit table 2, column 3
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 3 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p3"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 3) — `ny_it201.hh_city_p3`

- **Authored helper label:** New York City household credit table 5, column 3
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 3 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p3"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 4) — `ny_it201.hh_state_p4`

- **Authored helper label:** New York State household credit table 2, column 4
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 4 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p4"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 4) — `ny_it201.hh_city_p4`

- **Authored helper label:** New York City household credit table 5, column 4
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 4 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p4"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 5) — `ny_it201.hh_state_p5`

- **Authored helper label:** New York State household credit table 2, column 5
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 5 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p5"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 5) — `ny_it201.hh_city_p5`

- **Authored helper label:** New York City household credit table 5, column 5
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 5 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p5"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 6) — `ny_it201.hh_state_p6`

- **Authored helper label:** New York State household credit table 2, column 6
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 6 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p6"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 6) — `ny_it201.hh_city_p6`

- **Authored helper label:** New York City household credit table 5, column 6
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 6 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p6"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2, column 7) — `ny_it201.hh_state_p7`

- **Authored helper label:** New York State household credit table 2, column 7
- **Encoded (NonNegDollars):** Use New York State household credit table 2 (Filing status ②, ④ and ⑤), column 7 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t2_p7"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5, column 7) — `ny_it201.hh_city_p7`

- **Authored helper label:** New York City household credit table 5, column 7
- **Encoded (NonNegDollars):** Use New York City household credit table 5 (Filing status ②, ④ and ⑤), column 7 at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t5_p7"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "Enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 2) — `ny_it201.hh_state_t2`

- **Authored helper label:** New York State household credit table 2 for the number of people (column 7 for 7 or more)
- **Encoded (NonNegDollars):** Choose — [column (column) ≥ 0 (a count) and column (column) ≤ 1 (a count) → column (table 2, column 1)] [column (column) > 1 (a count) and column (column) ≤ 2 (a count) → column (table 2, column 2)] [column (column) > 2 (a count) and column (column) ≤ 3 (a count) → column (table 2, column 3)] [column (column) > 3 (a count) and column (column) ≤ 4 (a count) → column (table 2, column 4)] [column (column) > 4 (a count) and column (column) ≤ 5 (a count) → column (table 2, column 5)] [column (column) > 5 (a count) and column (column) ≤ 6 (a count) → column (table 2, column 6)] [column (column) > 6 (a count) → column (table 2, column 7)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.hh_people",{"const":0,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p1"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":1,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p2"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":2,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p3"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":3,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":4,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p4"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":4,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":5,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p5"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":5,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":6,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_state_p6"},{"guard":{"gt":["ny_it201.hh_people",{"const":6,"type":"Count"}],"op":"test"},"then":"ny_it201.hh_state_p7"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York State household credit table 2—Filing status ②, ④, and ⑤, "And the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return) is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 5) — `ny_it201.hh_city_t5`

- **Authored helper label:** New York City household credit table 5 for the number of people (column 7 for 7 or more)
- **Encoded (NonNegDollars):** Choose — [column (column) ≥ 0 (a count) and column (column) ≤ 1 (a count) → column (table 5, column 1)] [column (column) > 1 (a count) and column (column) ≤ 2 (a count) → column (table 5, column 2)] [column (column) > 2 (a count) and column (column) ≤ 3 (a count) → column (table 5, column 3)] [column (column) > 3 (a count) and column (column) ≤ 4 (a count) → column (table 5, column 4)] [column (column) > 4 (a count) and column (column) ≤ 5 (a count) → column (table 5, column 5)] [column (column) > 5 (a count) and column (column) ≤ 6 (a count) → column (table 5, column 6)] [column (column) > 6 (a count) → column (table 5, column 7)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.hh_people",{"const":0,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p1"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":1,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p2"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":2,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p3"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":3,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":4,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p4"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":4,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":5,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p5"},{"guard":{"all":[{"gt":["ny_it201.hh_people",{"const":5,"type":"Count"}],"op":"test"},{"le":["ny_it201.hh_people",{"const":6,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ny_it201.hh_city_p6"},{"guard":{"gt":["ny_it201.hh_people",{"const":6,"type":"Count"}],"op":"test"},"then":"ny_it201.hh_city_p7"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York City household credit table 5—Filing status ②, ④, and ⑤, "And the number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return) is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 1) — `ny_it201.hh_state_t1`

- **Authored helper label:** New York State household credit table 1 (single)
- **Encoded (NonNegDollars):** Use New York State household credit table 1 (Filing status ① only, Single) at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_state_t1"}`
- Cite: [ny_it201i-html] New York State household credit table 1—Filing status ① only (Single), "enter on Form IT-201, line 40:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (table 4) — `ny_it201.hh_city_t4`

- **Authored helper label:** New York City household credit table 4 (single)
- **Encoded (NonNegDollars):** Use New York City household credit table 4 (Filing status ① only, Single) at column (Note 1) for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.hh_agi","op":"table_lookup","status":"f1040.status","table":"ny_hh_city_t4"}`
- Cite: [ny_it201i-html] New York City household credit table 4—Filing status ① only (Single), "enter on Form IT-201, line 48:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (helper) — `ny_it201.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201i] p. 12, Line 40: New York State household credit, "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for this credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.hh_state_in_range`

- **Authored helper label:** Is federal AGI within the state household credit tables' credit rows?
- **Encoded (Bool):** line 19 ≤ $32,000 (ny.hh.state.limit)
- Expr: `{"le":["ny_it201.line19",{"param":"ny.hh.state.limit"}],"op":"test"}`
- Cite: [ny_it201i-html] New York State household credit table 3, "No credit is allowed; do not make an entry on Form IT-201, line 40." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (gate) — `ny_it201.gate.hh_state_mfs`

- **Authored helper label:** Married filing separately with federal AGI within the state credit rows (both returns' AGI and dependents are needed)
- **Encoded (Bool):** f1040 line Filing Status = 'mfs' and helper "Is federal AGI within the state household credit tables' credit rows?" = true and line C = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["ny_it201.hh_state_in_range",{"const":true}],"op":"test"},{"eq":["ny_it201.item_c",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Note 4, "If your spouse was not required to file a New York State return, use your spouse’s federal adjusted gross income as reported on their federal return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.hh_state_over7`

- **Authored helper label:** More than 7 people for the state household credit with federal AGI within the credit rows
- **Encoded (Bool):** f1040 line Filing Status ≠ 'single' and column (column) > 7 (ny.hh.max_people) and helper "Is federal AGI within the state household credit tables' credit rows?" = true and line C = false
- Expr: `{"all":[{"ne":["f1040.status",{"const":"single"}],"op":"test"},{"gt":["ny_it201.hh_people",{"param":"ny.hh.max_people"}],"op":"test"},{"eq":["ny_it201.hh_state_in_range",{"const":true}],"op":"test"},{"eq":["ny_it201.item_c",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Use these notes for New York State household credit tables 1 through 3, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (40) — `ny_it201.hh_state_by_status`

- **Authored helper label:** The state household credit table for the filing status
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → column (table 1)] [f1040 line Filing Status = 'mfj' → column (table 2)] [f1040 line Filing Status = 'hoh' → column (table 2)] [f1040 line Filing Status = 'qss' → column (table 2)] [f1040 line Filing Status = 'mfs' → helper "Zero"]
- Note: Married filing separately (tables 3 and 6) is zero here because the line refuses it wherever those tables allow a credit.
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"ny_it201.hh_state_t1"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"ny_it201.hh_state_t2"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"ny_it201.hh_state_t2"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"ny_it201.hh_state_t2"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"ny_it201.zero"}],"op":"choose"}`
- Cite: [ny_it201i] p. 12, Line 40: New York State household credit, "If you marked No, use the appropriate table (1, 2, or 3) and the notes below to determine the amount to enter on line 40." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.hh_city_in_range`

- **Authored helper label:** Is federal AGI within the city household credit tables' credit rows?
- **Encoded (Bool):** line 19 ≤ $22,500 (ny.hh.city.limit)
- Expr: `{"le":["ny_it201.line19",{"param":"ny.hh.city.limit"}],"op":"test"}`
- Cite: [ny_it201i-html] New York City household credit table 6, "No credit is allowed; do not make an entry on Form IT-201, line 48." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (gate) — `ny_it201.gate.hh_city_mfs`

- **Authored helper label:** Married filing separately with federal AGI within the city credit rows (both returns' AGI and dependents are needed)
- **Encoded (Bool):** f1040 line Filing Status = 'mfs' and helper "Is federal AGI within the city household credit tables' credit rows?" = true and line C = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["ny_it201.hh_city_in_range",{"const":true}],"op":"test"},{"eq":["ny_it201.item_c",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Note 4, "If your spouse was not required to file a New York State return, use your spouse’s federal adjusted gross income as reported on their federal return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.hh_city_over7`

- **Authored helper label:** More than 7 people for the city household credit with federal AGI within the credit rows
- **Encoded (Bool):** f1040 line Filing Status ≠ 'single' and column (column) > 7 (ny.hh.max_people) and helper "Is federal AGI within the city household credit tables' credit rows?" = true and line C = false
- Expr: `{"all":[{"ne":["f1040.status",{"const":"single"}],"op":"test"},{"gt":["ny_it201.hh_people",{"param":"ny.hh.max_people"}],"op":"test"},{"eq":["ny_it201.hh_city_in_range",{"const":true}],"op":"test"},{"eq":["ny_it201.item_c",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Use these notes for New York State household credit tables 1 through 3, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (48) — `ny_it201.hh_city_by_status`

- **Authored helper label:** The city household credit table for the filing status
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → column (table 4)] [f1040 line Filing Status = 'mfj' → column (table 5)] [f1040 line Filing Status = 'hoh' → column (table 5)] [f1040 line Filing Status = 'qss' → column (table 5)] [f1040 line Filing Status = 'mfs' → helper "Zero"]
- Note: Married filing separately (tables 3 and 6) is zero here because the line refuses it wherever those tables allow a credit.
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"ny_it201.hh_city_t4"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"ny_it201.hh_city_t5"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"ny_it201.hh_city_t5"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"ny_it201.hh_city_t5"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"ny_it201.zero"}],"op":"choose"}`
- Cite: [ny_it201i] p. 13, Line 48: New York City household credit (NYC residents only), "If you marked No, use the appropriate table (4, 5, or 6) and accompanying notes to determine the amount to enter on line 48." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 40 — `ny_it201.line40`

- **IRS:** NYS household credit
- **Encoded (NonNegDollars):** Choose — [line C = true → helper "Zero"] [line C = false → column (40)]
- **Refusal:** when ny_it201.gate.hh_state_mfs is true, cannot complete New York State household credit table 3 (married filing separately). The table for married filing separately needs your spouse's federal AGI and both returns' dependents; this tool refuses it where a credit is allowed. Cite: [ny_it201i] p. 13, Note 4, "use your spouse’s federal adjusted gross income as reported on their federal return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.hh_state_over7 is true, cannot complete New York State household credit, more than 7 people (Note 3). More than seven people in the household credit count is outside this tool where a credit is allowed. Cite: [ny_it201i] p. 13, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.item_c",{"const":true}],"op":"test"},"then":"ny_it201.zero"},{"guard":{"eq":["ny_it201.item_c",{"const":false}],"op":"test"},"then":"ny_it201.hh_state_by_status"}],"op":"choose"}`
- Cite: [ny_it201i] p. 12, Line 40: New York State household credit, "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for this credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.resident_credit`

- **Authored helper label:** Tax paid to another state or province
- **Encoded (Bool):** helper "Did you have income from sources outside New York State and pay income tax on it to another state, a local government of another state, the District of Columbia or a province of Canada?" = true
- Expr: `{"eq":["ny_it201.ask.resident_credit",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Line 41: Resident credit, "If Yes, complete Form IT-112-R, New York State Resident Credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 41 — `ny_it201.line41`

- **IRS:** Resident credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.resident_credit is true, cannot complete Form IT-112-R, New York State Resident Credit (and IT-112-C). The resident credit is not computed by this tool. Cite: [ny_it201i] p. 13, Line 41: Resident credit, "complete Form IT-112-R, New York State Resident Credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Resident credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.other_credits`

- **Authored helper label:** Other New York credits on Form IT-201-ATT
- **Encoded (Bool):** helper "Are you claiming any other New York State nonrefundable or refundable credit on Form IT-201-ATT (for example long-term care insurance, investment, solar energy, farmers' school tax or claim of right)?" = true
- Expr: `{"eq":["ny_it201.ask.other_credits",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Line 42, "If you are claiming any nonrefundable credits, complete the appropriate credit forms and Form IT-201-ATT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 42 — `ny_it201.line42`

- **IRS:** Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.other_credits is true, cannot complete Form IT-201-ATT, Other Tax Credits and Taxes. Other New York credits are not computed by this tool. Cite: [ny_it201i] p. 13, Line 42, "Transfer the total amount of nonrefundable credits to line 42." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Other NYS nonrefundable credits (Form IT-201-ATT, line 7)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 43 — `ny_it201.line43`

- **IRS:** Add lines 40, 41, and 42
- **Encoded (NonNegDollars):** Add line 40, line 41, and line 42.
- Expr: `{"of":["ny_it201.line40","ny_it201.line41","ny_it201.line42"],"op":"sum"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Add lines 40, 41, and 42" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 44 — `ny_it201.line44`

- **IRS:** Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
- **Encoded (NonNegDollars):** Subtract line 43 from line 39. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line39","op":"subtract_floor0","take":"ny_it201.line43"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.other_taxes`

- **Authored helper label:** Other New York State or City taxes on Form IT-201-ATT
- **Encoded (Bool):** helper "Do you owe any other New York State or City tax on Form IT-201-ATT, for example the separate tax on a lump-sum distribution (Form IT-230)?" = true
- Expr: `{"eq":["ny_it201.ask.other_taxes",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Line 45: Net other New York State taxes, "If you are subject to any other taxes, complete the appropriate forms and Part 2 of Form IT-201-ATT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 45 — `ny_it201.line45`

- **IRS:** Net other NYS taxes (Form IT-201-ATT, line 30)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.other_taxes is true, cannot complete Form IT-201-ATT, Part 2 (and Form IT-230). Other New York State taxes are not computed by this tool. Cite: [ny_it201i] p. 13, Line 45: Net other New York State taxes, "Transfer the total amount from Form IT-201-ATT, line 30 Net other New York State taxes, to line 45." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Net other NYS taxes (Form IT-201-ATT, line 30)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 46 — `ny_it201.line46`

- **IRS:** Total New York State taxes (add lines 44 and 45)
- **Encoded (NonNegDollars):** Add line 44 and line 45.
- Expr: `{"of":["ny_it201.line44","ny_it201.line45"],"op":"sum"}`
- Cite: [ny_it201] p. 3, Tax calculation, credits, and other taxes, "Total New York State taxes (add lines 44 and 45)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 47 — `ny_it201.line47`

- **IRS:** NYC taxable income
- **Encoded (NonNegDollars):** Enter the amount from line 38.
- Note: The Line 47 worksheet applies only with an itemized deduction for a Charitable Gifts Trust Fund contribution; itemizing is refused (line 34).
- Expr: `{"from":"ny_it201.line38","op":"copy"}`
- Cite: [ny_it201i] p. 13, Line 47: New York City taxable income (NYC full-year residents only; part-year residents, see line 50), "If No, enter the line 38 amount on line 47." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.city_table_range`

- **Authored helper label:** Is line 47 (your New York City taxable income) less than $65,000?
- **Encoded (Bool):** line 47 < $65,000 (ny.city.table.limit)
- Expr: `{"lt":["ny_it201.line47",{"param":"ny.city.table.limit"}],"op":"test"}`
- Cite: [ny_it201i] p. 13, Line 47a: New York City resident tax (NYC full-year residents only; part-year residents, see line 50), "Is line 47 (your New York City taxable income) less than $65,000?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (47a) — `ny_it201.city_tax_table`

- **Authored helper label:** New York City resident tax from the 2025 New York City Tax Table
- **Encoded (NonNegDollars):** Use 2025 New York City Tax Table at line 47 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"ny_it201.line47","op":"table_lookup","status":"f1040.status","table":"ny_city_tax_table"}`
- Cite: [ny_it201i] p. 13, Line 47a, "If Yes, find your New York City resident tax using the 2025 New York City Tax Table." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (47a) — `ny_it201.city_tax_schedule`

- **Authored helper label:** New York City resident tax from the New York City tax rate schedule
- **Encoded (NonNegDollars):** Enter "tax" of New York City tax rate schedule with amount = line 47 and status = f1040 line Filing Status.
- Expr: `{"from":{"bind":{"amount":"ny_it201.line47","status":"f1040.status"},"def":"ny_city_rs","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i] p. 13, Line 47a, "If No, find your New York City resident tax using the New York City tax rate schedule below." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 47a — `ny_it201.line47a`

- **IRS:** NYC resident tax on line 47 amount
- **Encoded (NonNegDollars):** Choose — [helper "Is line 47 (your New York City taxable income) less than $65,000?" = true → column (47a) (ny_it201.city_tax_table)] [helper "Is line 47 (your New York City taxable income) less than $65,000?" = false → column (47a) (ny_it201.city_tax_schedule)]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.city_table_range",{"const":true}],"op":"test"},"then":"ny_it201.city_tax_table"},{"guard":{"eq":["ny_it201.city_table_range",{"const":false}],"op":"test"},"then":"ny_it201.city_tax_schedule"}],"op":"choose"}`
- Cite: [ny_it201i] p. 13, Line 47a, "Is line 47 (your New York City taxable income) less than $65,000?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 48 — `ny_it201.line48`

- **IRS:** NYC household credit
- **Encoded (NonNegDollars):** Choose — [line C = true → helper "Zero"] [line C = false → column (48)]
- **Refusal:** when ny_it201.gate.hh_city_mfs is true, cannot complete New York City household credit table 6 (married filing separately). The table for married filing separately needs your spouse's federal AGI and both returns' dependents; this tool refuses it where a credit is allowed. Cite: [ny_it201i] p. 14, Note 4, "use your spouse’s federal adjusted gross income as reported on their federal return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.hh_city_over7 is true, cannot complete New York City household credit, more than 7 people (Note 3). More than seven people in the household credit count is outside this tool where a credit is allowed. Cite: [ny_it201i] p. 14, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.item_c",{"const":true}],"op":"test"},"then":"ny_it201.zero"},{"guard":{"eq":["ny_it201.item_c",{"const":false}],"op":"test"},"then":"ny_it201.hh_city_by_status"}],"op":"choose"}`
- Cite: [ny_it201i] p. 13, Line 48: New York City household credit (NYC residents only), "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for this credit and should go to line 49." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 49 — `ny_it201.line49`

- **IRS:** Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
- **Encoded (NonNegDollars):** Subtract line 48 from line 47a. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line47a","op":"subtract_floor0","take":"ny_it201.line48"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Subtract line 48 from line 47a" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 50 — `ny_it201.line50`

- **IRS:** Part-year NYC resident tax (Form IT-360.1)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Zero: a part-year City resident is refused (line 1).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Part-year NYC resident tax (Form IT-360.1)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 51 — `ny_it201.line51`

- **IRS:** Other NYC taxes (Form IT-201-ATT, line 34)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.other_taxes is true, cannot complete Form IT-201-ATT, Part 3 (and Form IT-230). Other New York City taxes are not computed by this tool. Cite: [ny_it201i] p. 14, Line 51: Other New York City taxes, "Enter the total amount of other New York City taxes from Form IT-201-ATT, Part 3, line 34." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Other NYC taxes (Form IT-201-ATT, line 34)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 52 — `ny_it201.line52`

- **IRS:** Add lines 49, 50, and 51
- **Encoded (NonNegDollars):** Add line 49, line 50, and line 51.
- Expr: `{"of":["ny_it201.line49","ny_it201.line50","ny_it201.line51"],"op":"sum"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Add lines 49, 50, and 51" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.city_credits`

- **Authored helper label:** New York City nonrefundable credits
- **Encoded (Bool):** helper "Can you claim the New York City unincorporated business tax credit, the New York City accumulation distribution credit, or the part-year resident New York City child and dependent care credit?" = true
- Expr: `{"eq":["ny_it201.ask.city_credits",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 15, Line 53, "If Yes, complete Section C of Form IT-201-ATT and enter the amount from Form IT-201-ATT, line 10, on line 53." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 53 — `ny_it201.line53`

- **IRS:** NYC nonrefundable credits (Form IT-201-ATT, line 10)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.city_credits is true, cannot complete Form IT-201-ATT, Section C. New York City nonrefundable credits are not computed by this tool. Cite: [ny_it201i] p. 15, Line 53, "complete Section C of Form IT-201-ATT" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "NYC nonrefundable credits (Form IT-201-ATT, line 10)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 54 — `ny_it201.line54`

- **IRS:** Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
- **Encoded (NonNegDollars):** Subtract line 53 from line 52. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line52","op":"subtract_floor0","take":"ny_it201.line53"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Subtract line 53 from line 52" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (helper) — `ny_it201.mctmt_people`

- **Authored helper label:** Number of persons with more than one Schedule C, or with Schedule C net profit over $50,000
- **Encoded (Count):** Add person.one over every confirmed person entry for which (helper "Number of Schedules C for this person" > 1 (a count) or helper "This person's Schedule C net profit or loss (all businesses)" > $50,000 (ny.mctmt.threshold)), within the current person when parent-bound. An unanswered roster is unknown.
- Note: A person with one Schedule C has one source, whose net earnings from self-employment (Schedule SE line 6) are at most its net profit, so a profit of $50,000 or less cannot exceed the threshold in either zone. With two or more Schedules C, whether a loss from one source reduces another is not settled here, so the question is asked. Self-employment income other than Schedule C (a partnership, farm or other source) is refused by the federal screens (scope.schedule1, person.se_screen).
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"any":[{"gt":["person.sc_count",{"const":1,"type":"Count"}],"op":"test"},{"gt":["person.sc_total",{"param":"ny.mctmt.threshold"}],"op":"test"}],"op":"test"}}`
- Cite: [ny_it201i] p. 15, Lines 54a through 54e, "The $50,000 threshold is calculated on an individual basis, even if you file a joint income tax return." and "You must calculate your MCTMT net earnings base separately for each source of self-employment income that has business activity in one or both zones."; p. 16, "Net earnings from self-employment generally is the amount reported on federal Schedule SE (Form 1040), Part 1, line 6, derived from the source of self-employment income." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.mctmt_possible`

- **Authored helper label:** Can you or your spouse have net earnings from self-employment over $50,000 in a zone?
- **Encoded (Bool):** helper "Number of persons with more than one Schedule C, or with Schedule C net profit over $50,000" > 0 (a count)
- Expr: `{"gt":["ny_it201.mctmt_people",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [ny_it201i] p. 15, Lines 54a through 54e, "If an individual’s net earnings from self-employment allocated to either zone exceed $50,000 for the tax year, then you are subject to the MCTMT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.mctmt`

- **Authored helper label:** Self-employment earnings over $50,000 in an MCTD zone
- **Encoded (Bool):** Choose — [helper "Can you or your spouse have net earnings from self-employment over $50,000 in a zone?" = true → helper "Did you or your spouse have net earnings from self-employment allocated to New York City (MCTD Zone 1) or to Zone 2 of more than $50,000?"] [helper "Can you or your spouse have net earnings from self-employment over $50,000 in a zone?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.mctmt_possible",{"const":true}],"op":"test"},"then":"ny_it201.ask.mctmt"},{"guard":{"eq":["ny_it201.mctmt_possible",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 15, Lines 54a through 54e, "If Yes, you are subject to MCTMT. Go to lines 54a and 54b, as applicable." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 54a — `ny_it201.line54a`

- **IRS:** MCTMT net earnings base for Zone 1
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.mctmt is true, cannot complete Form IT-201 lines 54a to 54e (MCTMT). The metropolitan commuter transportation mobility tax is not computed by this tool (decision B5). Cite: [ny_it201i] p. 15, Lines 54a through 54e, "If an individual’s net earnings from self-employment allocated to either zone exceed $50,000 for the tax year, then you are subject to the MCTMT." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "MCTMT net earnings" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 54b — `ny_it201.line54b`

- **IRS:** MCTMT net earnings base for Zone 2
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.mctmt is true, cannot complete Form IT-201 lines 54a to 54e (MCTMT). The metropolitan commuter transportation mobility tax is not computed by this tool (decision B5). Cite: [ny_it201i] p. 15, Lines 54a through 54e, "Zone 2- Enter the amount of net earnings from self-employment allocated to Zone 2 for the tax year on line 54b." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Note: Zero when the MCTMT does not apply; refused with line 54a when it does.
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "MCTMT net earnings" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 54c — `ny_it201.line54c`

- **IRS:** MCTMT for Zone 1
- **Encoded (NonNegDollars):** Multiply line 54a by 60/10000 (ny.mctmt.zone1), rounded to the nearest multiple of $1 (half up).
- Expr: `{"amount":"ny_it201.line54a","op":"multiply_rate","rate":{"param":"ny.mctmt.zone1"},"unit":100}`
- Cite: [ny_it201i] p. 17, Line 54c: MCTMT for Zone 1, "Multiply the amount on line 54a by 0.60% (0.0060)." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 54d — `ny_it201.line54d`

- **IRS:** MCTMT for Zone 2
- **Encoded (NonNegDollars):** Multiply line 54b by 34/10000 (ny.mctmt.zone2), rounded to the nearest multiple of $1 (half up).
- Expr: `{"amount":"ny_it201.line54b","op":"multiply_rate","rate":{"param":"ny.mctmt.zone2"},"unit":100}`
- Cite: [ny_it201i] p. 17, Line 54d: MCTMT for Zone 2, "Multiply the amount on line 54b by 0.34% (0.0034)." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 54e — `ny_it201.line54e`

- **IRS:** Total MCTMT (add lines 54c and 54d)
- **Encoded (NonNegDollars):** Add line 54c and line 54d.
- Expr: `{"of":["ny_it201.line54c","ny_it201.line54d"],"op":"sum"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Total MCTMT (add lines 54c and 54d)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 55 — `ny_it201.line55`

- **IRS:** Yonkers resident income tax surcharge
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Zero: Yonkers is refused (line 1, item D2).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Yonkers resident income tax surcharge" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 56 — `ny_it201.line56`

- **IRS:** Yonkers nonresident earnings tax (Form Y-203)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Zero: Yonkers is refused (line 1, item D2).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Yonkers nonresident earnings tax" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 57 — `ny_it201.line57`

- **IRS:** Part-year Yonkers resident income tax surcharge (Form IT-360.1)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Zero: Yonkers is refused (line 1, item D2).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Part-year Yonkers resident income tax surcharge" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 58 — `ny_it201.line58`

- **IRS:** Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through 57)
- **Encoded (NonNegDollars):** Add line 54, line 54e, line 55, line 56, and line 57.
- Expr: `{"of":["ny_it201.line54","ny_it201.line54e","ny_it201.line55","ny_it201.line56","ny_it201.line57"],"op":"sum"}`
- Cite: [ny_it201] p. 3, New York City and Yonkers taxes, credits, and surcharges, and MCTMT, "Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through 57)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (chart) — `ny_it201.sut.b1`

- **Authored helper label:** Sales and use tax chart, row 1
- **Encoded (NonNegDollars):** Enter $3 (ny.sut.b1.amount).
- Expr: `{"op":"param","ref":"ny.sut.b1.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b2`

- **Authored helper label:** Sales and use tax chart, row 2
- **Encoded (NonNegDollars):** Enter $6 (ny.sut.b2.amount).
- Expr: `{"op":"param","ref":"ny.sut.b2.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b3`

- **Authored helper label:** Sales and use tax chart, row 3
- **Encoded (NonNegDollars):** Enter $10 (ny.sut.b3.amount).
- Expr: `{"op":"param","ref":"ny.sut.b3.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b4`

- **Authored helper label:** Sales and use tax chart, row 4
- **Encoded (NonNegDollars):** Enter $15 (ny.sut.b4.amount).
- Expr: `{"op":"param","ref":"ny.sut.b4.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b5`

- **Authored helper label:** Sales and use tax chart, row 5
- **Encoded (NonNegDollars):** Enter $18 (ny.sut.b5.amount).
- Expr: `{"op":"param","ref":"ny.sut.b5.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b6`

- **Authored helper label:** Sales and use tax chart, row 6
- **Encoded (NonNegDollars):** Enter $26 (ny.sut.b6.amount).
- Expr: `{"op":"param","ref":"ny.sut.b6.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.b7`

- **Authored helper label:** Sales and use tax chart, row 7
- **Encoded (NonNegDollars):** Enter $34 (ny.sut.b7.amount).
- Expr: `{"op":"param","ref":"ny.sut.b7.amount"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "Enter on line 59:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.top_product`

- **Authored helper label:** 0.0175% (0.000175) of income
- **Encoded (NonNegDollars):** Multiply column (Note 1) by 175/1000000 (ny.sut.top_rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"ny_it201.hh_agi","op":"multiply_rate","rate":{"param":"ny.sut.top_rate"},"unit":100}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "200,001 and greater", "0.0175% (0.000175)" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.cap`

- **Authored helper label:** $125
- **Encoded (NonNegDollars):** Enter $125 (ny.sut.cap).
- Expr: `{"op":"param","ref":"ny.sut.cap"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "or $125, whichever amount is smaller" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.top`

- **Authored helper label:** 0.0175% (0.000175) of income, or $125, whichever amount is smaller
- **Encoded (NonNegDollars):** Enter the smaller of column (chart) (ny_it201.sut.top_product) or column (chart) (ny_it201.sut.cap).
- Expr: `{"of":["ny_it201.sut.top_product","ny_it201.sut.cap"],"op":"smaller_of"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "of income, or $125, whichever amount is smaller" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (chart) — `ny_it201.sut.chart`

- **Authored helper label:** The sales and use tax chart amount for federal adjusted gross income (line 19; zero or a negative amount is in the first row)
- **Encoded (NonNegDollars):** Choose — [column (Note 1) ≥ $0 and column (Note 1) ≤ $15,000 (ny.sut.b1.upper) → column (chart) (ny_it201.sut.b1)] [column (Note 1) > $15,000 (ny.sut.b1.upper) and column (Note 1) ≤ $30,000 (ny.sut.b2.upper) → column (chart) (ny_it201.sut.b2)] [column (Note 1) > $30,000 (ny.sut.b2.upper) and column (Note 1) ≤ $50,000 (ny.sut.b3.upper) → column (chart) (ny_it201.sut.b3)] [column (Note 1) > $50,000 (ny.sut.b3.upper) and column (Note 1) ≤ $75,000 (ny.sut.b4.upper) → column (chart) (ny_it201.sut.b4)] [column (Note 1) > $75,000 (ny.sut.b4.upper) and column (Note 1) ≤ $100,000 (ny.sut.b5.upper) → column (chart) (ny_it201.sut.b5)] [column (Note 1) > $100,000 (ny.sut.b5.upper) and column (Note 1) ≤ $150,000 (ny.sut.b6.upper) → column (chart) (ny_it201.sut.b6)] [column (Note 1) > $150,000 (ny.sut.b6.upper) and column (Note 1) ≤ $200,000 (ny.sut.b7.upper) → column (chart) (ny_it201.sut.b7)] [column (Note 1) > $200,000 (ny.sut.b7.upper) → column (chart) (ny_it201.sut.top)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ny_it201.hh_agi",{"const":0}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b1.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b1"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b1.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b2.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b2"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b2.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b3.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b3"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b3.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b4.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b4"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b4.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b5.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b5"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b5.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b6.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b6"},{"guard":{"all":[{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b6.upper"}],"op":"test"},{"le":["ny_it201.hh_agi",{"param":"ny.sut.b7.upper"}],"op":"test"}],"op":"test"},"then":"ny_it201.sut.b7"},{"guard":{"gt":["ny_it201.hh_agi",{"param":"ny.sut.b7.upper"}],"op":"test"},"then":"ny_it201.sut.top"}],"op":"choose"}`
- Cite: [ny_it201i] p. 18, Sales and use tax chart, "If your federal adjusted gross income (line 19) is:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.use_tax_abode`

- **Authored helper label:** Use tax owed with a New York abode for only part of the year (the chart amount is prorated by months)
- **Encoded (Bool):** helper "Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?" = true and helper "Did you maintain a permanent place of abode in New York State for only part of 2025 (for sales and use tax purposes)?" = true
- Expr: `{"all":[{"eq":["ny_it201.ask.owes_use_tax",{"const":true}],"op":"test"},{"eq":["ny_it201.ask.abode_part_year",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "multiply the tax amount from the chart by the number of months you maintained the permanent place of abode in New York State and divide the result by 12" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.use_tax_st141`

- **Authored helper label:** Use tax that must be calculated on Form ST-141
- **Encoded (Bool):** helper "Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?" = true and helper "Do you owe use tax on an item or service costing $1,000 or more, or on purchases for a business, rental real estate or royalty activity, or do you want to calculate the exact amount (Form ST-141)?" = true
- Expr: `{"all":[{"eq":["ny_it201.ask.owes_use_tax",{"const":true}],"op":"test"},{"eq":["ny_it201.ask.use_tax_st141",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "You must use Form ST-141 to calculate your sales and use tax liability to be reported on this return if any of the following apply:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 59 — `ny_it201.line59`

- **IRS:** Sales or use tax (do not leave blank)
- **Encoded (NonNegDollars):** Choose — [helper "Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?" = false → helper "No sales or use tax owed"] [helper "Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?" = true → column (chart) (ny_it201.sut.chart)]
- **Refusal:** when ny_it201.gate.use_tax_abode is true, cannot complete Line 59 for a part-year abode. The chart amount prorated by months of a New York abode is not computed by this tool. Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "Count any period you maintained the abode for more than one-half of a month as one month." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- **Refusal:** when ny_it201.gate.use_tax_st141 is true, cannot complete Form ST-141, Individual Purchaser's Periodic Report of Sales and Use Tax. An exact use tax calculation, an item of $1,000 or more, or business purchases are outside this tool (decision B3). Cite: [ny_it201i] p. 18, Line 59: Sales or use tax, "You must use Form ST-141 to calculate your sales and use tax liability to be reported on this return if any of the following apply:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.ask.owes_use_tax",{"const":false}],"op":"test"},"then":"ny_it201.zero_sut"},{"guard":{"eq":["ny_it201.ask.owes_use_tax",{"const":true}],"op":"test"},"then":"ny_it201.sut.chart"}],"op":"choose"}`
- Cite: [ny_it201i] p. 19, Line 59, "If you do not owe any sales or use tax, you must enter 0 on line 59. Do not leave line 59 blank." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (helper) — `ny_it201.zero_sut`

- **Authored helper label:** No sales or use tax owed
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201i] p. 19, Line 59, "If you do not owe any sales or use tax, you must enter 0 on line 59." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.contributions`

- **Authored helper label:** Voluntary contributions
- **Encoded (Bool):** helper "Do you want to make voluntary contributions to the funds listed on Form IT-227?" = true
- Expr: `{"eq":["ny_it201.ask.contributions",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 60, "If Yes, complete Form IT-227 and enter the amount from Part 2, line 1." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 60 — `ny_it201.line60`

- **IRS:** Voluntary contributions (Form IT-227, Part 2, line 1)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.contributions is true, cannot complete Form IT-227, Voluntary Contributions. Voluntary contributions are outside this tool (decision B11). Cite: [ny_it201i] p. 19, Line 60, "complete Form IT-227 and enter the amount from Part 2, line 1" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 3, Voluntary contributions, "Voluntary contributions (Form IT-227, Part 2, line 1)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 61 — `ny_it201.line61`

- **IRS:** Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and voluntary contributions (add lines 46, 58, 59, and 60)
- **Encoded (NonNegDollars):** Add line 46, line 58, line 59, and line 60.
- Expr: `{"of":["ny_it201.line46","ny_it201.line58","ny_it201.line59","ny_it201.line60"],"op":"sum"}`
- Cite: [ny_it201] p. 3, Voluntary contributions, "voluntary contributions (add lines 46, 58, 59, and 60)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 62 — `ny_it201.line62`

- **IRS:** Enter amount from line 61
- **Encoded (NonNegDollars):** Enter the amount from line 61.
- Expr: `{"from":"ny_it201.line61","op":"copy"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Enter amount from line 61" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (helper) — `ny_it201.under17_count`

- **Authored helper label:** Dependents under 17 at the end of 2025
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Your dependent" = true and helper "Under age 17 at the end of 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"all":[{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"eq":["dependent.under_ctc_age",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [ny_it201i] p. 19, Line 63: Empire State child credit, "(A qualifying child must be less than 17 years old on December 31st of the tax year.)" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.child_credit`

- **Authored helper label:** A dependent under 17 (the Empire State child credit may apply)
- **Encoded (Bool):** helper "Dependents under 17 at the end of 2025" > 0 (a count)
- Expr: `{"gt":["ny_it201.under17_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 63: Empire State child credit, "Do you have at least one qualifying child?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 63 — `ny_it201.line63`

- **IRS:** Empire State child credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.child_credit is true, cannot complete Form IT-213, Claim for Empire State Child Credit. The Empire State child credit is not computed by this tool. Cite: [ny_it201i] p. 19, Line 63: Empire State child credit, "review the instructions for Form IT-213, Claim for Empire State Child Credit, to see if you qualify for this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Empire State child credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.federal_care`

- **Authored helper label:** Did you (or your spouse) have care expenses for a qualifying person so you (and your spouse) could work or look for work, or receive dependent care benefits (federal Form 2441)?
- **Encoded (Bool):** (f2441 helper "Did you pay for the care of a qualifying person so you could work or look for work?" = true or f2441 helper "Did you receive dependent care benefits?" = true)
- Note: The federal credit and the New York credit both need care expenses for a qualifying person so you could work or look for work (i2441 p. 2, Who Can Take the Credit or Exclude Dependent Care Benefits?, items 2 and 3). Dependent care benefits count too, since care paid through them is a care expense (Form IT-216 Worksheet 1).
- Expr: `{"any":[{"eq":["f2441.care",{"const":true}],"op":"test"},{"eq":["f2441.benefits",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [ny_it216i] p. 1, Who qualifies, "If you qualify to claim the federal child and dependent care credit, you can claim the New York State credit (whether you actually claim the federal credit or not)." and "The care was provided so you (and your spouse, if you were married) could work or look for work." and "Caution: Taxpayers who receive dependent care benefits from their employer must complete Worksheet 1 – Dependent care benefits." (2025; sha256 e9ff8282)

## (gate) — `ny_it201.gate.dependent_care`

- **Authored helper label:** The child and dependent care credit may apply
- **Encoded (Bool):** Choose — [helper "Did you (or your spouse) have care expenses for a qualifying person so you (and your spouse) could work or look for work, or receive dependent care benefits (federal Form 2441)?" = true → helper "Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you claimed it)?"] [helper "Did you (or your spouse) have care expenses for a qualifying person so you (and your spouse) could work or look for work, or receive dependent care benefits (federal Form 2441)?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.federal_care",{"const":true}],"op":"test"},"then":"ny_it201.ask.dependent_care"},{"guard":{"eq":["ny_it201.federal_care",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 19, Line 64, "If Yes, complete Form IT-216, Claim for Child and Dependent Care Credit, to determine your New York State child and dependent care credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 64 — `ny_it201.line64`

- **IRS:** NYS/NYC child and dependent care credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.dependent_care is true, cannot complete Form IT-216, Claim for Child and Dependent Care Credit. The New York child and dependent care credits are not computed by this tool. Cite: [ny_it201i] p. 19, Line 64, "complete Form IT-216, Claim for Child and Dependent Care Credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "NYS/NYC child and dependent care credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.eic`

- **Authored helper label:** The federal earned income credit was claimed, or federal AGI is below its income limit
- **Encoded (Bool):** (f1040 line 27a > $0 or f1040 line 11a < eic helper "Step 1 and Step 5 limit for the filing status and the number of qualifying children with valid SSNs")
- Expr: `{"any":[{"gt":["f1040.line27a",{"const":0}],"op":"test"},{"lt":["f1040.line11a","eic.limit"],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 65, "Did you claim the federal earned income credit for 2025 on your federal income tax return, or could you have claimed it based on your federal adjusted gross income?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 65 — `ny_it201.line65`

- **IRS:** NYS earned income credit (EIC)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.eic is true, cannot complete Form IT-215, Claim for Earned Income Credit. The New York State earned income credit is not computed by this tool (decision B9). Cite: [ny_it201i] p. 19, Line 65, "review the instructions for Form IT-215, Claim for Earned Income Credit, to see if you qualify for this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Interpretation: amb.ny.2025.eic_could_claim
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "NYS earned income credit (EIC)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.noncustodial`

- **Authored helper label:** Child support paid through a Support Collection Unit
- **Encoded (Bool):** helper "Did you make child support payments payable through a New York State Support Collection Unit?" = true
- Expr: `{"eq":["ny_it201.ask.noncustodial",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 66, "If Yes, review the instructions for Form IT-209 to see if you qualify for this credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 66 — `ny_it201.line66`

- **IRS:** NYS noncustodial parent EIC
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.noncustodial is true, cannot complete Form IT-209, Claim for Noncustodial Parent New York State Earned Income Credit. This credit is not computed by this tool. Cite: [ny_it201i] p. 19, Line 66, "complete Form IT-209 and transfer the credit amount to the appropriate line of Form IT-201" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "NYS noncustodial parent EIC" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.real_property`

- **Authored helper label:** The real property tax credit may apply
- **Encoded (Bool):** helper "Might you qualify for the New York real property tax credit for homeowners and renters (Form IT-214)? It is limited to households with low income that paid real property taxes or rent; if unsure, read the Form IT-214 instructions before answering." = true
- Expr: `{"eq":["ny_it201.ask.real_property_credit",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 67, "If you qualify, complete Form IT-214 and transfer the amount from Form IT-214 to Form IT-201, line 67." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 67 — `ny_it201.line67`

- **IRS:** Real property tax credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.real_property is true, cannot complete Form IT-214, Claim for Real Property Tax Credit for Homeowners and Renters. This credit is not computed by this tool. Cite: [ny_it201i] p. 19, Line 67, "complete Form IT-214" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Real property tax credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.college_tuition`

- **Authored helper label:** College tuition paid
- **Encoded (Bool):** helper "Did you, your spouse or any dependent pay college tuition expenses during 2025?" = true
- Expr: `{"eq":["ny_it201.ask.college_tuition",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 19, Line 68, "Did you or your spouse or any dependents pay college tuition expenses during 2025?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 68 — `ny_it201.line68`

- **IRS:** College tuition credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.college_tuition is true, cannot complete Form IT-272, Claim for College Tuition Credit or Itemized Deduction. The college tuition credit is not computed by this tool. Cite: [ny_it201i] p. 19, Line 68, "complete Form IT-272, Claim for" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "College tuition credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (69) — `ny_it201.stc_income`

- **Authored helper label:** Income for the school tax credit: federal AGI (line 19) minus IRA distributions included in it (line 9)
- **Encoded (Dollars):** Subtract line 9 from line 19.
- Expr: `{"from":"ny_it201.line19","op":"subtract","take":"ny_it201.line9"}`
- Cite: [ny_it201i] p. 20, Line 69, "Income, for purposes of determining your New York City school tax credit, means your federal adjusted gross income from Form IT-201, line 19, minus distributions from an individual retirement account and an individual retirement annuity, from Form IT-201, line 9, if they were included in your federal adjusted gross income." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.stc_fixed_eligible`

- **Authored helper label:** Item C No and income of $250,000 or less
- **Encoded (Bool):** line C = false and column (69) (ny_it201.stc_income) ≤ $250,000 (ny.stc.fixed.limit)
- Expr: `{"all":[{"eq":["ny_it201.item_c",{"const":false}],"op":"test"},{"le":["ny_it201.stc_income",{"param":"ny.stc.fixed.limit"}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 20, Line 69, "or your income (see below) is more than $250,000, you do not qualify for this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (69) — `ny_it201.stc_fixed_amount`

- **Authored helper label:** Table 1 - Full-year New York City residents: the credit for the filing status
- **Encoded (NonNegDollars):** Enter single $63; mfj $125; mfs $63; hoh $63; qss $125 (ny.stc.fixed).
- Expr: `{"op":"param","ref":"ny.stc.fixed"}`
- Cite: [ny_it201i-html] Table 1 - Full-year New York City residents, "$63", "$125" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 69 — `ny_it201.line69`

- **IRS:** NYC school tax credit (fixed amount)
- **Encoded (NonNegDollars):** Choose — [helper "Item C No and income of $250,000 or less" = true → column (69) (ny_it201.stc_fixed_amount)] [helper "Item C No and income of $250,000 or less" = false → helper "No school tax credit"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.stc_fixed_eligible",{"const":true}],"op":"test"},"then":"ny_it201.stc_fixed_amount"},{"guard":{"eq":["ny_it201.stc_fixed_eligible",{"const":false}],"op":"test"},"then":"ny_it201.zero_stc"}],"op":"choose"}`
- Cite: [ny_it201i] p. 20, Line 69, "determine your credit using Table 1 below if you were a full-year resident" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (helper) — `ny_it201.zero_stc`

- **Authored helper label:** No school tax credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201i] p. 20, Line 69, "you do not qualify for this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.stc_rr_income`

- **Authored helper label:** Line 69a: income or New York City taxable income more than $500,000
- **Encoded (Bool):** line C = false and (column (69) (ny_it201.stc_income) > $500,000 (ny.stc.rr.limit) or line 47 > $500,000 (ny.stc.rr.limit))
- Expr: `{"all":[{"eq":["ny_it201.item_c",{"const":false}],"op":"test"},{"any":[{"gt":["ny_it201.stc_income",{"param":"ny.stc.rr.limit"}],"op":"test"},{"gt":["ny_it201.line47",{"param":"ny.stc.rr.limit"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 20, Line 69a, "or your income (see below) is more than $500,000, you do not qualify to claim this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (69a) — `ny_it201.stc_rr_low`

- **Authored helper label:** 0.171% of taxable income
- **Encoded (NonNegDollars):** Multiply line 47 by 171/100000 (ny.stc.rr.low_rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"ny_it201.line47","op":"multiply_rate","rate":{"param":"ny.stc.rr.low_rate"},"unit":100}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③, "0.171% of taxable income" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (69a) — `ny_it201.stc_rr_excess`

- **Authored helper label:** The excess of New York City taxable income over the bracket amount
- **Encoded (NonNegDollars):** Subtract single $12,000; mfj $21,600; mfs $12,000; hoh $14,400; qss $21,600 (ny.stc.rr.over) from line 47. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line47","op":"subtract_floor0","take":{"param":"ny.stc.rr.over"}}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③, "plus 0.228% of the excess over $12,000" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (69a) — `ny_it201.stc_rr_excess_product`

- **Authored helper label:** 0.228% of the excess
- **Encoded (NonNegDollars):** Multiply column (69a) (ny_it201.stc_rr_excess) by 228/100000 (ny.stc.rr.high_rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"ny_it201.stc_rr_excess","op":"multiply_rate","rate":{"param":"ny.stc.rr.high_rate"},"unit":100}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤, "plus 0.228% of the excess over $21,600" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (69a) — `ny_it201.stc_rr_base`

- **Authored helper label:** The bracket's base amount ($21, $37 or $25)
- **Encoded (NonNegDollars):** Enter single $21; mfj $37; mfs $21; hoh $25; qss $37 (ny.stc.rr.base).
- Expr: `{"op":"param","ref":"ny.stc.rr.base"}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for head of household ④, "$25" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (69a) — `ny_it201.stc_rr_high`

- **Authored helper label:** The base amount plus 0.228% of the excess
- **Encoded (NonNegDollars):** Add column (69a) (ny_it201.stc_rr_base) and column (69a) (ny_it201.stc_rr_excess_product).
- Expr: `{"of":["ny_it201.stc_rr_base","ny_it201.stc_rr_excess_product"],"op":"sum"}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for head of household ④, "plus 0.228% of the excess over $14,400" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (gate) — `ny_it201.stc_rr_low_band`

- **Authored helper label:** Is New York City taxable income not over the bracket amount ($12,000, $21,600 or $14,400)?
- **Encoded (Bool):** line 47 ≤ single $12,000; mfj $21,600; mfs $12,000; hoh $14,400; qss $21,600 (ny.stc.rr.over)
- Expr: `{"le":["ny_it201.line47",{"param":"ny.stc.rr.over"}],"op":"test"}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③, "If city taxable income is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (69a) — `ny_it201.stc_rr`

- **Authored helper label:** The rate reduction amount from the table for the filing status
- **Encoded (NonNegDollars):** Choose — [helper "Is New York City taxable income not over the bracket amount ($12,000, $21,600 or $14,400)?" = true → column (69a) (ny_it201.stc_rr_low)] [helper "Is New York City taxable income not over the bracket amount ($12,000, $21,600 or $14,400)?" = false → column (69a) (ny_it201.stc_rr_high)]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.stc_rr_low_band",{"const":true}],"op":"test"},"then":"ny_it201.stc_rr_low"},{"guard":{"eq":["ny_it201.stc_rr_low_band",{"const":false}],"op":"test"},"then":"ny_it201.stc_rr_high"}],"op":"choose"}`
- Cite: [ny_it201i-html] Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤, "If city taxable income is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 69a — `ny_it201.line69a`

- **IRS:** NYC school tax credit (rate reduction amount)
- **Encoded (NonNegDollars):** Choose — [line C = true → helper "No school tax credit"] [line C = false → column (69a) (ny_it201.stc_rr)]
- **Refusal:** when ny_it201.gate.stc_rr_income is true, cannot complete Form IT-201 line 69a above $500,000. Whether the $500,000 limit applies to income or to New York City taxable income is unsettled; this tool refuses either above it (decision B7). Cite: [ny_it201i] p. 20, Line 69a, "or your income (see below) is more than $500,000, you do not qualify to claim this credit" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Interpretation: amb.ny.2025.school_credit_income
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.item_c",{"const":true}],"op":"test"},"then":"ny_it201.zero_stc"},{"guard":{"eq":["ny_it201.item_c",{"const":false}],"op":"test"},"then":"ny_it201.stc_rr"}],"op":"choose"}`
- Cite: [ny_it201i] p. 21, Line 69a, "If you were a city resident for all of 2025, use the amount from Form IT-201, line 47." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 70 — `ny_it201.line70`

- **IRS:** NYC earned income credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.eic is true, cannot complete Form IT-215, Claim for Earned Income Credit. The New York City earned income credit is not computed by this tool (decision B9). Cite: [ny_it201i] p. 21, Line 70, "If you qualify, complete either Form IT-215 or Form IT-209" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Interpretation: amb.ny.2025.eic_could_claim
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "NYC earned income credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.it270`

- **Authored helper label:** Dependents claimed and federal AGI within $5,000 of the highest NYC income tax elimination credit threshold
- **Encoded (Bool):** line H (count) > 0 (a count) and line 19 ≤ single $93,361; mfj $96,902; mfs $93,361; hoh $93,361; qss $96,902 (ny.it270.max_threshold_plus)
- Expr: `{"all":[{"gt":["ny_it201.item_h_count",{"const":0,"type":"Count"}],"op":"test"},{"le":["ny_it201.line19",{"param":"ny.it270.max_threshold_plus"}],"op":"test"}],"op":"test"}`
- Cite: [ny_it270i] p. 1, General information, "you claimed one or more dependents on Form IT-201, item H or Form IT-203, item I," (Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit, for tax year 2025 (no printed edition line; address /pdf/2025/inc/, PDF metadata Title '... Tax Year 2025'); PDF modified 2025-10-27; sha256 1f8f971a)

## 70a — `ny_it201.line70a`

- **IRS:** NYC income tax elimination credit
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.it270 is true, cannot complete Form IT-270, New York City Income Tax Elimination Credit. This credit is not computed by this tool (decision B10); with no dependent on item H it does not apply. Cite: [ny_it201i] p. 21, Line 70a: New York City income tax elimination credit, "Review the instructions for Form IT-270, New York City Income Tax Elimination Credit, to see if you qualify for this credit." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "NYC income tax elimination credit" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 71 — `ny_it201.line71`

- **IRS:** Other refundable credits (Form IT-201-ATT, line 18)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.other_credits is true, cannot complete Form IT-201-ATT, Section D. Other refundable credits are not computed by this tool. Cite: [ny_it201i] p. 21, Line 71, "Enter the total amount of other refundable credits from Form IT-201-ATT, Part 1, Section D, line 18." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Other refundable credits (Form IT-201-ATT, line 18)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.other_withholding`

- **Authored helper label:** New York withholding on a form other than Form W-2
- **Encoded (Bool):** helper "Was any New York State, City or Yonkers tax withheld from a pension, annuity or IRA payment (Form 1099-R), unemployment or other government payment (Form 1099-G) or gambling winnings (Form W-2G)?" = true
- Expr: `{"eq":["ny_it201.ask.other_withholding",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 21, Lines 72, 73, and 74, "Form IT-1099-R, Summary of Federal Form 1099-R Statements" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 72 — `ny_it201.line72`

- **IRS:** Total New York State tax withheld
- **Encoded (NonNegDollars):** Add ny_it2.state_whole over every confirmed ny_it2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when ny_it201.gate.other_withholding is true, cannot complete Form IT-1099-R (and New York withholding on Forms 1099-G and W-2G). New York withholding on forms other than Form W-2 is outside this tool (decision B2). Cite: [ny_it201i] p. 21, Lines 72, 73, and 74, "If you had New York State, New York City, or Yonkers tax withheld from annuities, pensions, retirement pay, or IRA payments, you must complete Form IT-1099-R" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"collection":"ny_it2","field":"ny_it2.state_whole","op":"sum_over"}`
- Cite: [ny_it201i] p. 21, Lines 72, 73, and 74: Total New York State, New York City, and Yonkers tax withheld, "Complete Form IT-2, Summary of W-2 Statements, for all federal Forms W-2 (or W-2c) you received." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 73 — `ny_it201.line73`

- **IRS:** Total New York City tax withheld
- **Encoded (NonNegDollars):** Add ny_it2.city_whole over every confirmed ny_it2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when ny_it201.gate.other_withholding is true, cannot complete Form IT-1099-R (and New York withholding on Forms 1099-G and W-2G). New York withholding on forms other than Form W-2 is outside this tool (decision B2). Cite: [ny_it201i] p. 21, Lines 72, 73, and 74, "you must complete Form IT-1099-R, Summary of Federal Form 1099-R Statements" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"collection":"ny_it2","field":"ny_it2.city_whole","op":"sum_over"}`
- Cite: [ny_it201i] p. 21, Lines 72, 73, and 74: Total New York State, New York City, and Yonkers tax withheld, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 74 — `ny_it201.line74`

- **IRS:** Total Yonkers tax withheld
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- Note: Zero: Yonkers is refused (line 1, item D2), and a W-2 record with Yonkers withholding is refused (ny_it2).
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Total Yonkers tax withheld" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 75 — `ny_it201.line75`

- **IRS:** Total estimated tax payments and amount paid with Form IT-370
- **Encoded (NonNegDollars):** Input — The total of your (and, on a joint return, your spouse's) 2025 New York State, New York City, Yonkers and MCTMT estimated tax payments (including the last installment even if paid in 2026), any 2024 overpayment applied to 2025 estimated tax (as adjusted by the Tax Department), any estimated tax allocated to you by an estate or trust, and any amount paid with Form IT-370; do not include New York City unincorporated business tax payments
- Expr: `{"op":"input","source":"The total of your (and, on a joint return, your spouse's) 2025 New York State, New York City, Yonkers and MCTMT estimated tax payments (including the last installment even if paid in 2026), any 2024 overpayment applied to 2025 estimated tax (as adjusted by the Tax Department), any estimated tax allocated to you by an estate or trust, and any amount paid with Form IT-370; do not include New York City unincorporated business tax payments"}`
- Cite: [ny_it201i] p. 22, Line 75: Total estimated tax payments and amount paid with Form IT-370, "your 2025 estimated tax payments for New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 76 — `ny_it201.line76`

- **IRS:** Total payments (add lines 63 through 75)
- **Encoded (NonNegDollars):** Add line 63, line 64, line 65, line 66, line 67, line 68, line 69, line 69a, line 70, line 70a, line 71, line 72, line 73, line 74, and line 75.
- Expr: `{"of":["ny_it201.line63","ny_it201.line64","ny_it201.line65","ny_it201.line66","ny_it201.line67","ny_it201.line68","ny_it201.line69","ny_it201.line69a","ny_it201.line70","ny_it201.line70a","ny_it201.line71","ny_it201.line72","ny_it201.line73","ny_it201.line74","ny_it201.line75"],"op":"sum"}`
- Cite: [ny_it201] p. 4, Payments and refundable credits, "Total payments (add lines 63 through 75)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (80) — `ny_it201.tax_due`

- **Authored helper label:** If line 76 is less than line 62, subtract line 76 from line 62
- **Encoded (NonNegDollars):** Subtract line 76 from line 62. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line62","op":"subtract_floor0","take":"ny_it201.line76"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "subtract line 76 from line 62" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (81) — `ny_it201.prepayments`

- **Authored helper label:** Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 72 to 75)
- **Encoded (NonNegDollars):** Add line 72, line 73, line 74, and line 75.
- Expr: `{"of":["ny_it201.line72","ny_it201.line73","ny_it201.line74","ny_it201.line75"],"op":"sum"}`
- Cite: [ny_it201i] p. 23, Line 81, "the total amount of your 2025 prepayments (the amount of withholding and estimated tax payments you have already made or which were paid on your behalf by a partnership or S corporation for 2025)" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (81) — `ny_it201.safe_harbor_100`

- **Authored helper label:** 100% of your 2024 New York income tax
- **Encoded (NonNegDollars):** Multiply helper "Your 2024 New York income tax (based on a 12-month return)" by 1/1 (ny.est.prior_rate), rounded to the nearest multiple of $1 (half up).
- Expr: `{"amount":"ny_it201.ask.prior_year_tax","op":"multiply_rate","rate":{"param":"ny.est.prior_rate"},"unit":100}`
- Cite: [ny_it201i] p. 23, Line 81, "In general, you are not subject to a penalty if your 2025 prepayments equal at least 100% of your 2024 New York income tax based on a 12-month return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (81) — `ny_it201.safe_harbor_110`

- **Authored helper label:** 110% of your 2024 New York income tax
- **Encoded (NonNegDollars):** Multiply helper "Your 2024 New York income tax (based on a 12-month return)" by 110% (1.10) (ny.est.prior_rate_high), rounded to the nearest multiple of $1 (half up).
- Expr: `{"amount":"ny_it201.ask.prior_year_tax","op":"multiply_rate","rate":{"param":"ny.est.prior_rate_high"},"unit":100}`
- Cite: [ny_it201i] p. 23, Line 81, "your 2025 prepayments must equal at least 110% of your 2024 New York income tax based on a 12-month return" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (81) — `ny_it201.safe_harbor`

- **Authored helper label:** The prepayments required to be safe from the estimated tax penalty
- **Encoded (NonNegDollars):** Choose — [helper "Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?" = false → column (81) (ny_it201.safe_harbor_100)] [helper "Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?" = true → column (81) (ny_it201.safe_harbor_110)]
- Note: The farmer or fisherman exception is not asked; for one the 110% amount is required, which can only refuse more often.
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.ask.prior_agi_high",{"const":false}],"op":"test"},"then":"ny_it201.safe_harbor_100"},{"guard":{"eq":["ny_it201.ask.prior_agi_high",{"const":true}],"op":"test"},"then":"ny_it201.safe_harbor_110"}],"op":"choose"}`
- Cite: [ny_it201i] p. 23, Line 81, "However, if your 2024 New York adjusted gross income was more than $150,000 (or $75,000 if you are married filing separately for 2025) and you are not a farmer or a fisherman, your 2025 prepayments must equal at least 110% of your 2024 New York income tax based on a 12-month return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.estimated_penalty`

- **Authored helper label:** An estimated tax penalty may be owed: a balance due with prepayments below the safe harbor or no full-year 2024 return, or a late or short estimated installment
- **Encoded (Bool):** (column (80) > $0 and (column (81) (ny_it201.prepayments) < column (81) (ny_it201.safe_harbor) or helper "Did you file a 2024 New York return covering a full 12 months?" = false) or line 75 > $0 and helper "Was any 2025 New York estimated tax installment paid late, or smaller than one quarter of the year's required payment?" = true)
- Expr: `{"any":[{"all":[{"gt":["ny_it201.tax_due",{"const":0}],"op":"test"},{"any":[{"lt":["ny_it201.prepayments","ny_it201.safe_harbor"],"op":"test"},{"eq":["ny_it201.ask.prior_full_year",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"},{"all":[{"gt":["ny_it201.line75",{"const":0}],"op":"test"},{"eq":["ny_it201.ask.est_late",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [ny_it201i] p. 23, Line 81: Penalty for underpaying your tax (estimated tax penalty), "You may owe an estimated tax penalty if you did not have enough tax withheld from your wages or did not make enough estimated tax payments on other income you earned during the year." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 81 — `ny_it201.line81`

- **IRS:** Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.estimated_penalty is true, cannot complete Form IT-2105.9, Underpayment of Estimated Tax by Individuals and Fiduciaries. With a balance due and prepayments below 100% (110% above $150,000 of 2024 New York AGI) of your 2024 New York tax, an estimated tax penalty may be owed; this tool does not compute it (decision B6). Cite: [ny_it201i] p. 23, Line 81, "For more information, see Form IT-2105.9, Underpayment of Estimated Tax by Individuals and Fiduciaries, and its instructions." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "Estimated tax penalty" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (gate) — `ny_it201.gate.late`

- **Authored helper label:** Late filing or payment penalties or interest
- **Encoded (Bool):** helper "Are you filing late or paying late, so that you owe a late filing or late payment penalty or interest?" = true
- Expr: `{"eq":["ny_it201.ask.late_penalty",{"const":true}],"op":"test"}`
- Cite: [ny_it201i] p. 24, Line 82, "If you owe a late filing penalty, late payment penalty, or interest:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 82 — `ny_it201.line82`

- **IRS:** Other penalties and interest
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.late is true, cannot complete Form IT-201 line 82 (late filing or payment penalties and interest). Late penalties and interest are outside this tool (decision B11). Cite: [ny_it201i] p. 24, Line 82, "Calculate the penalty and interest using the Penalty and Interest Calculator" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "Other penalties and interest" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## (77) — `ny_it201.overpaid_before_penalty`

- **Authored helper label:** If line 76 is more than line 62, subtract line 62 from line 76
- **Encoded (NonNegDollars):** Subtract line 62 from line 76. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line76","op":"subtract_floor0","take":"ny_it201.line62"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "Amount overpaid (if line 76 is more than line 62, subtract line 62 from line 76)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 77 — `ny_it201.line77`

- **IRS:** Amount overpaid
- **Encoded (NonNegDollars):** Subtract line 81 from column (77). If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.overpaid_before_penalty","op":"subtract_floor0","take":"ny_it201.line81"}`
- Cite: [ny_it201i] p. 22, Line 77: Amount overpaid, "If you have to pay an estimated tax penalty (see line 81 instructions), subtract the penalty from the overpayment and enter the net overpayment on line 77." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.has_overpayment`

- **Authored helper label:** Is there an overpayment on line 77?
- **Encoded (Bool):** line 77 > $0
- Expr: `{"gt":["ny_it201.line77",{"const":0}],"op":"test"}`
- Cite: [ny_it201i] p. 23, Line 79: Estimated tax, "Enter the amount of overpayment from line 77 that you want applied to your New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax estimated tax for 2026." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (question) — `ny_it201.line79_amount`

- **Authored helper label:** Amount of line 77 that you want applied to your 2026 estimated tax
- **Encoded (NonNegDollars):** Input — How much of your overpayment (line 77) do you want applied to your 2026 estimated tax for New York State, New York City, Yonkers and the metropolitan commuter transportation mobility tax? (0 for none)
- Expr: `{"op":"input","source":"How much of your overpayment (line 77) do you want applied to your 2026 estimated tax for New York State, New York City, Yonkers and the metropolitan commuter transportation mobility tax? (0 for none)"}`
- Cite: [ny_it201i] p. 23, Line 79: Estimated tax, "Enter the amount of overpayment from line 77 that you want applied to your New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax estimated tax for 2026." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 79 — `ny_it201.line79`

- **IRS:** Amount of line 77 that you want applied to your 2026 estimated tax
- **Encoded (NonNegDollars):** Choose — [helper "Is there an overpayment on line 77?" = true → helper "Amount of line 77 that you want applied to your 2026 estimated tax"] [helper "Is there an overpayment on line 77?" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.has_overpayment",{"const":true}],"op":"test"},"then":"ny_it201.line79_amount"},{"guard":{"eq":["ny_it201.has_overpayment",{"const":false}],"op":"test"},"then":"ny_it201.zero"}],"op":"choose"}`
- Cite: [ny_it201i] p. 23, Line 79: Estimated tax, "Enter the amount of overpayment from line 77 that you want applied to your New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax estimated tax for 2026." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.line79_over`

- **Authored helper label:** Line 79 is more than line 77
- **Encoded (Bool):** line 79 > line 77
- Expr: `{"gt":["ny_it201.line79","ny_it201.line77"],"op":"test"}`
- Cite: [ny_it201i] p. 23, Line 79: Estimated tax, "The total of lines 78a through 79 should equal the amount on line 77." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 78 — `ny_it201.line78`

- **IRS:** Amount of line 77 available for refund (subtract line 79 from line 77)
- **Encoded (NonNegDollars):** Subtract line 79 from line 77. If zero or less, enter -0-.
- **Refusal:** when ny_it201.gate.line79_over is true, cannot complete Line 79 more than the overpayment. The amount applied to 2026 estimated tax cannot be more than the overpayment on line 77; correct line 79. Cite: [ny_it201i] p. 23, Line 79: Estimated tax, "The total of lines 78a through 79 should equal the amount on line 77." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"from":"ny_it201.line77","op":"subtract_floor0","take":"ny_it201.line79"}`
- Cite: [ny_it201i] p. 23, Line 78: Amount of line 77 available for refund, "Subtract the amount on line 79 (estimated tax) from line 77." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.has_refund`

- **Authored helper label:** Is there an amount available for refund on line 78?
- **Encoded (Bool):** line 78 > $0
- Expr: `{"gt":["ny_it201.line78",{"const":0}],"op":"test"}`
- Cite: [ny_it201i] p. 23, Line 78a: NYS 529 account deposit, "You may directly deposit all or a portion of your refund in up to three NYS 529 college savings accounts." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (gate) — `ny_it201.gate.refund_529`

- **Authored helper label:** A refund deposit into a New York 529 account
- **Encoded (Bool):** Choose — [helper "Is there an amount available for refund on line 78?" = true → helper "Do you want part of a refund deposited into a New York 529 college savings account (Form IT-195)?"] [helper "Is there an amount available for refund on line 78?" = false → helper "No"]
- Expr: `{"alternatives":[{"guard":{"eq":["ny_it201.has_refund",{"const":true}],"op":"test"},"then":"ny_it201.ask.refund_529"},{"guard":{"eq":["ny_it201.has_refund",{"const":false}],"op":"test"},"then":"ny_it201.no"}],"op":"choose"}`
- Cite: [ny_it201i] p. 23, Line 78a: NYS 529 account deposit, "You may directly deposit all or a portion of your refund in up to three NYS 529 college savings accounts." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 78a — `ny_it201.line78a`

- **IRS:** Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195, line 4)
- **Encoded (NonNegDollars):** Enter $0 (ny.zero).
- **Refusal:** when ny_it201.gate.refund_529 is true, cannot complete Form IT-195, Allocation of Refund. Depositing a refund into a 529 account is outside this tool (decision B11). Cite: [ny_it201i] p. 23, Line 78a: NYS 529 account deposit, "Use Form IT-195, Allocation of Refund" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"param","ref":"ny.zero"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "Amount of line 78 that you want to deposit into a NYS 529 account" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 78b — `ny_it201.line78b`

- **IRS:** Total refund after NYS 529 account deposit (subtract line 78a from line 78)
- **Encoded (NonNegDollars):** Subtract line 78a from line 78. If zero or less, enter -0-.
- Expr: `{"from":"ny_it201.line78","op":"subtract_floor0","take":"ny_it201.line78a"}`
- Cite: [ny_it201] p. 4, Your refund, amount you owe, and account information, "Total refund after NYS 529 account deposit (subtract line 78a from line 78)" (Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12; sha256 cfe63039)

## 80 — `ny_it201.line80`

- **IRS:** Amount you owe
- **Encoded (NonNegDollars):** Add column (80), line 81, and line 82.
- Expr: `{"of":["ny_it201.tax_due","ny_it201.line81","ny_it201.line82"],"op":"sum"}`
- Cite: [ny_it201i] p. 23, Line 80: Amount you owe, "Enter on line 80 the amount of tax you owe plus any estimated tax penalty you owe (see line 81 instructions) and any other penalties and interest you owe (see line 82 instructions)." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
