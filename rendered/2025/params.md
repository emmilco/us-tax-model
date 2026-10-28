# Parameters, tax year 2025

## Enums

- `asset_class`: c00_11, c00_12, c00_13, c00_21, c00_22, c00_23, c00_241, c00_242, c00_25, c00_26, c00_27, c00_28, c00_3, c00_4, c01_1, c01_11, c01_21, c01_221, c01_222, c01_223, c01_224, c01_225, c01_23, c01_24, c01_3, c01_4, c10_0, c13_0, c13_1, c13_2, c13_3, c15_0, c20_1, c20_2, c20_3, c20_4, c20_5, c21_0, c22_1, c22_2, c22_3, c22_4, c22_5, c23_0, c24_1, c24_2, c24_3, c24_4, c26_1, c26_2, c27_0, c28_0, c30_1, c30_11, c30_2, c30_21, c31_0, c32_1, c32_11, c32_2, c32_3, c33_2, c33_21, c33_3, c33_4, c34_0, c34_01, c35_0, c36_0, c36_1, c37_11, c37_12, c37_2, c37_31, c37_32, c37_33, c37_41, c37_42, c39_0, c40_1, c40_2, c40_3, c40_4, c40_51, c40_52, c40_53, c40_54, c41_0, c42_0, c44_0, c45_0, c45_1, c46_0, c48_11, c48_12, c48_121, c48_13, c48_14, c48_2, c48_31, c48_32, c48_33, c48_34, c48_35, c48_36, c48_37, c48_38, c48_39, c48_41, c48_42, c48_43, c48_44, c48_45, c49_11, c49_12, c49_121, c49_13, c49_14, c49_15, c49_21, c49_221, c49_222, c49_223, c49_23, c49_24, c49_25, c49_3, c49_4, c49_5, c50_0, c51_0, c57_0, c57_1, c79_0, c80_0, cA_personal, cA_1245real, cB_qte, cC_research, cDEF_energy, cqip — [p946] Appendix B, Tables B-1 and B-2 (the asset classes, pp. 99-108), the lettered paragraphs of Certain Property for Which Recovery Periods Assigned (p. 108), and qualified improvement property (Table 4-1); the description of each value is in tables/2025/class_lives.enum.json (For use in preparing 2025 returns; sha256 07fadfb2)
- `bonus_choice`: full, forty, none — [i4562] pp. 5–6, Line 14, the 100% special depreciation allowance and the election "to take a 40% special depreciation allowance"; p. 7, Election out (2025; sha256 5c1c95b7)
- `carloan_kind`: original, refinanced, death — [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4) (refinancing of an SPVL) and (d)(5) (whether the SPVL was incurred by the taxpayer; change in obligor by reason of death) (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)
- `catchup_age`: under50, age50, age60_63 — [p560] chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)
- `dc_tin_kind`: tin, tax_exempt, lafcp, see_statement, employer — [i2441] p. 3, Column (c), "If the care provider is an individual, enter their SSN or individual taxpayer identification number (ITIN). Otherwise, enter the provider's employer identification number (EIN). If the provider is a tax-exempt organization, enter “Tax-Exempt” in column (c)" and "enter “LAFCP” (Living Abroad Foreign Care Provider)"; p. 3, Due Diligence, "Enter “See Attached Statement” in the columns for which you don't have the information"; p. 3, Columns (a) and (b), "If you were covered by your employer's dependent care plan and your employer furnished the care ... leave column (c) blank" (2025; sha256 86f0669e)
- `dependent_relationship`: child, sibling, sibling_descendant, parent, parent_relative, in_law, household_member, other — [i1040gi] pp. 17 and 19, Who Qualifies as Your Dependent, Steps 1 and 4: child is a son, daughter, stepchild, foster child or a descendant of any of them; sibling is a brother, sister, stepbrother, stepsister, half brother or half sister, or a son or daughter of a brother, sister, half brother or half sister (Step 4 lists step siblings but not their children); sibling_descendant is any other descendant of a sibling, including a step sibling's child (a qualifying child relationship under Step 1, and a Step 4 relative only as a household member who lived with you all year); parent is a father or mother; parent_relative is an ancestor or sibling of a parent (a Step 4 relative, but not the parent of Head of Household Test 1); in_law is a step-parent or an in-law; household_member is any other person who lived with you all year (2025; printed date 2026-02-25; sha256 482e9c48)
- `filing_status`: single, mfj, mfs, hoh, qss — [f1040] Form 1040, Filing Status (checkboxes) (2025; created 2025-09-05; sha256 3d31c226)
- `hsa_allocation`: equal, agreed — [i8889] p. 7, Line 6, "divide the amount on line 5 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)" (2025; sha256 da6f2f58)
- `hsa_coverage`: none, self_only, family — [i8889] p. 4, Line 3, rules 2 and 4(b), and p. 6, Line 3 Limitation Chart: the type of HDHP coverage (self-only or family) on the first day of a month, or not an eligible individual that day (2025; sha256 da6f2f58)
- `ltc_age`: to40, to50, to60, to70, over70 — [f7206] Form 7206 (2025), line 2(b), the ages 40 or younger, 41 to 50, 51 to 60, 61 to 70, and 71 or older (2025; created 2025-10-02; sha256 822203c9)
- `macrs_convention`: hy, mq1, mq2, mq3, mq4 — [i4562] p. 11, Column (e)—Convention, half-year convention and mid-quarter convention by quarter placed in service (2025; sha256 5c1c95b7)
- `macrs_period`: y3, y5, y7, y10, y15, y20, y15sl, outside — [i4562] p. 10, Lines 19a Through 19j, Column (a) and Column (d), the recovery periods of 3- to 20-year property; Column (f), "15- and 20-year property ... 150% declining balance"; y15sl is qualified improvement property, 15-year straight line (p946 Appendix A, Tables A-8 to A-12); outside is a class this tool refuses (p946 Appendix B) (2025; sha256 5c1c95b7)
- `other_income_kind`: rtaa, kickbacks, insurance_dividends, recovery, corrective_distribution, charitable_recapture, disaster_relief, education_distribution, other — [i1040gi] p. 92, Line 8z, "Examples of income to report on line 8z include the following": recoveries, RTAA payments, corrective distributions, insurance dividends, charitable recaptures, disaster relief payments and Coverdell ESA or QTP distributions; p525 p. 34, Kickbacks; other is any other line 8z income (2025; printed date 2026-02-25; sha256 482e9c48)
- `overtime_method`: employer_reported, premium, total_time_and_half, premium_double, total_double, other — [i1040gi] pp. 106-107, Schedule 1-A, "Determining the amount of qualified overtime compensation for 2025": an amount the employer provides (Form W-2 box 14 or on request), methods 1 to 4; method 5, adjustments and other overtime rates are refused (2025; printed date 2026-02-25; sha256 482e9c48)
- `person_role`: taxpayer, spouse — [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial" (2025; created 2025-09-05; sha256 3d31c226)
- `placed_year`: y2005, y2006, y2007, y2008, y2009, y2010, y2011, y2012, y2013, y2014, y2015, y2016, y2017, y2018, y2019, y2020, y2021, y2022, y2023, y2024, y2025 — [p946] p. 39, Using the MACRS Percentage Tables; the example of property placed in service on July 2, 2023, for which 2025 is "the third recovery year" (For use in preparing 2025 returns; sha256 07fadfb2)
- `quarter`: q1, q2, q3, q4 — [p946] p. 41, Using the Applicable Convention, Mid-quarter convention, "A calendar year is divided into the following quarters" (January to March, April to June, July to September, October to December) (For use in preparing 2025 returns; sha256 07fadfb2)
- `retire_plan`: none, sep, simple — [p560] chapter 2, Simplified Employee Pension (SEP); chapter 3, SIMPLE IRA Plan (For use in preparing 2025 returns; sha256 1f1f7abe)
- `retirement_account`: traditional_ira, roth_ira, plan — [f1099r] Instructions for Recipient: traditional IRA or traditional SIMPLE IRA (the IRA/SEP/SIMPLE box), Roth IRA or Roth SIMPLE IRA, and qualified plans, section 403(b) and governmental 457(b) plans (pensions and annuities); i1040gi pp. 26-28, lines 4a, 4b, 5a and 5b (2025 (calendar-year form); sha256 d6b7be48)
- `retirement_code`: normal_7, death_4, early_exception_2, direct_rollover_G, qualified_roth_Q, other — [f1099r] Instructions for Recipient, Box 7: 7 normal distribution; 4 death; 2 early distribution, exception applies; G direct rollover to a qualified plan, 403(b), governmental 457(b) or IRA; Q qualified distribution from a Roth IRA; every other code or combination is 'other' (2025 (calendar-year form); sha256 d6b7be48)
- `sales_box`: A, B, C, D, E, F, G, H, I, J, K, L — [f8949] Parts I and II, checkbox classifications (2025; created 2025-05-05; sha256 27451389)
- `sales_code`: none, B, W, BW, other — [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)
- `sales_route`: detail, aggregate — [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)
- `simple_formula`: match, nonelective — [p560] chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)
- `vehicle_method`: standard, actual — [i1040sc] p. 6, Line 9, "You can deduct the actual expenses of operating your car or truck or take the standard mileage rate" (2025; sha256 b5536db9)

## Values

| Parameter | Type | Value | Cite |
| --- | --- | --- | --- |
| `actc.earned_floor` | NonNegDollars | $2,500 | [f1040s8812] Schedule 8812 (2025), line 19, "Is the amount on line 18a more than $2,500?" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.per_child` | NonNegDollars | $1,700 | [f1040s8812] Schedule 8812 (2025), line 16b, "x $1,700" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.rate` | Rate | 15% (0.15) | [f1040s8812] Schedule 8812 (2025), line 20, "Multiply the amount on line 19 by 15% (0.15)" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.three_children` | NonNegDollars | $5,100 | [f1040s8812] Schedule 8812 (2025), after line 20, "On line 16b, is the amount $5,100 or more?" (2025; created 2025-07-30; sha256 6936462d) |
| `clcw.prior_limit` | NonNegDollars | $3,000 | [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6) |
| `clcw.prior_limit_mfs` | NonNegDollars | $1,500 | [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6) |
| `ctc.age_limit` | Count | 17 | [i1040gi] p. 18, Step 3, "Was the child under age 17 at the end of 2025?" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ctc.per_child` | NonNegDollars | $2,200 | [f1040s8812] Schedule 8812 (2025), line 5, "Multiply line 4 by $2,200" (2025; created 2025-07-30; sha256 6936462d) |
| `ctc.phaseout_rate` | Rate | 5% (0.05) | [f1040s8812] Schedule 8812 (2025), line 11, "Multiply line 10 by 5% (0.05)" (2025; created 2025-07-30; sha256 6936462d) |
| `ctc.threshold` | NonNegDollars | single $200,000; mfj $400,000; mfs $200,000; hoh $200,000; qss $200,000 | [f1040s8812] Schedule 8812 (2025), line 9, "Married filing jointly—$400,000; All other filing statuses—$200,000" (2025; created 2025-07-30; sha256 6936462d) |
| `dc.child_age` | Count | 13 | [i2441] p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13" (2025; sha256 86f0669e) |
| `dc.exclusion_max` | NonNegDollars | $5,000 | [i2441] p. 5, Line 21, "For 2025, the maximum amount that can be excluded from your income through a dependent care assistance program is $5,000" (2025; sha256 86f0669e) |
| `dc.limit_one` | NonNegDollars | $3,000 | [f2441] Form 2441 (2025), lines 3 and 27 (2025; created 2025-03-18; sha256 6c3c2d19) |
| `dc.limit_two` | NonNegDollars | $6,000 | [f2441] Form 2441 (2025), lines 3 and 27 (2025; created 2025-03-18; sha256 6c3c2d19) |
| `dc.one` | Count | 1 | [i2441] p. 2, Line 1, "Complete columns (a) through (e) for each person or organization that provided the care" (2025; sha256 86f0669e) |
| `dc.persons_two` | Count | 2 | [f2441] Form 2441 (2025), lines 3 and 27 (2025; created 2025-03-18; sha256 6c3c2d19) |
| `dc.providers_listed` | Count | 3 | [i2441] p. 2, Line 1, "If you have more than three care providers, check the box above line 1 and attach a statement to your return with the required information" (2025; sha256 86f0669e) |
| `dependent.one` | Count | 1 | [f1040s8812] Schedule 8812 (2025), lines 4 and 6, "Number of qualifying children" and "Number of other dependents" (2025; created 2025-07-30; sha256 6936462d) |
| `eic.earned_amount0` | NonNegDollars | $8,490 | [rp-2024-40] section 3.06(1), Earned Income Amount, none (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount1` | NonNegDollars | $12,730 | [rp-2024-40] section 3.06(1), Earned Income Amount, one qualifying child (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount2` | NonNegDollars | $17,880 | [rp-2024-40] section 3.06(1), Earned Income Amount, two qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount3` | NonNegDollars | $17,880 | [rp-2024-40] section 3.06(1), Earned Income Amount, three or more qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.investment_limit` | NonNegDollars | $11,950 | [i1040gi] p. 40, Step 2, question 2, "Is your investment income more than $11,950?" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit0.joint` | NonNegDollars | $26,214 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($26,214 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit0.other` | NonNegDollars | $19,104 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "No children ... less than $19,104" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit1.joint` | NonNegDollars | $57,554 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($57,554 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit1.other` | NonNegDollars | $50,434 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "1 child ... less than $50,434" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit2.joint` | NonNegDollars | $64,430 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($64,430 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit2.other` | NonNegDollars | $57,310 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "2 children ... less than $57,310" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit3.joint` | NonNegDollars | $68,675 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($68,675 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit3.other` | NonNegDollars | $61,555 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "3 or more children ... less than $61,555" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.maximum0` | NonNegDollars | $649 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, none (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum1` | NonNegDollars | $4,328 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, one qualifying child (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum2` | NonNegDollars | $7,152 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, two qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum3` | NonNegDollars | $8,046 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, three or more qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.table_start` | NonNegDollars | $1 | [i1040gi] p. 49, 2025 Earned Income Credit (EIC) Table, first row "At least 1 But less than 50" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold0.joint` | NonNegDollars | $17,730 | [i1040gi] p. 46, Worksheet A, line 5, "($17,730 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold0.other` | NonNegDollars | $10,620 | [i1040gi] p. 46, Worksheet A, line 5, "No qualifying children ... less than $10,620" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold1.joint` | NonNegDollars | $30,470 | [i1040gi] p. 46, Worksheet A, line 5, "($30,470 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold1.other` | NonNegDollars | $23,350 | [i1040gi] p. 46, Worksheet A, line 5, "1 or more qualifying children ... less than $23,350" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `f5695.annual_max` | NonNegDollars | $1,200 | [f5695] Form 5695 (2025), line 28, "Enter the smaller of line 27 or $1,200"; i5695 p. 2, Energy Efficient Home Improvement Credit (Part II), "A total combined credit limit of $1,200 for qualified energy property" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.audit_max` | NonNegDollars | $150 | [f5695] Form 5695 (2025), line 26c, "Do not enter more than $150"; i5695 p. 3, Energy Efficient Home Improvement Credit (Part II), "A credit limit of $150 for home energy audits" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.door_max` | NonNegDollars | $250 | [f5695] Form 5695 (2025), line 19c, "Do not enter more than $250"; i5695 p. 3, Energy Efficient Home Improvement Credit (Part II), "A credit limit of $250 for any qualifying exterior door" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.doors_max` | NonNegDollars | $500 | [f5695] Form 5695 (2025), line 19h, "Do not enter more than $500"; i5695 p. 3, Energy Efficient Home Improvement Credit (Part II), "$500 total for all qualifying exterior doors" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.eehi_rate` | Rate | 30% (0.30) | [f5695] Form 5695 (2025), lines 18b to 29h, "Multiply ... by 30% (0.30)"; i5695 p. 1, Reminders, "A 30% credit, up to a maximum of $1,200, may be allowed for" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.heat_pump_max` | NonNegDollars | $2,000 | [f5695] Form 5695 (2025), line 29h, "Do not enter more than $2,000"; i5695 p. 3, Energy Efficient Home Improvement Credit (Part II), "A combined credit limit of $2,000 for heat pump and heat pump water heaters; biomass stoves and boilers" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.insulation_max` | NonNegDollars | $1,200 | [f5695] Form 5695 (2025), line 18b, "Do not enter more than $1,200"; i5695 p. 5, Lines 18a and 18b, "Don't enter more than $1,200 on line 18b" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.item_max` | NonNegDollars | $600 | [f5695] Form 5695 (2025), lines 22d, 23d, 24d and 25e, "Do not enter more than $600"; i5695 p. 2, Energy Efficient Home Improvement Credit (Part II), "A credit limit of $600 for any qualified energy property item" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.rce_rate` | Rate | 30% (0.30) | [f5695] Form 5695 (2025), line 6b, "Multiply line 6a by 30% (0.30)"; i5695 p. 1, Reminders, "The credit rate for property placed in service in 2022 through 2025 is 30%" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `f5695.windows_max` | NonNegDollars | $600 | [f5695] Form 5695 (2025), line 20d, "Do not enter more than $600"; i5695 p. 2, Energy Efficient Home Improvement Credit (Part II), "A combined credit limit of $600 for all exterior windows and skylights" (2025; created 2025-03-20; sha256 e2ac6a5c) |
| `ftc.limit` | NonNegDollars | single $300; mfj $600; mfs $300; hoh $300; qss $300 | [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c) |
| `hsa.additional` | NonNegDollars | $1,000 | [i8889] p. 7, Additional Contribution Amount Worksheet, line 1, "$1,000 × number of months eligible" (2025; sha256 da6f2f58) |
| `hsa.additional_rate` | Rate | 20% (0.20) | [f8889] Form 8889 (2025), line 17b, "Enter 20% (0.20) of the distributions included on line 16 that are subject to the additional 20% tax" (2025; created 2025-03-28; sha256 15ed4587) |
| `hsa.family` | NonNegDollars | $8,550 | [i8889] p. 6, Line 3 Limitation Chart, family coverage, "Enter $8,550 on the line below for the month" (2025; sha256 da6f2f58) |
| `hsa.family_55` | NonNegDollars | $9,550 | [i8889] p. 6, Line 3 Limitation Chart, family coverage, "If, at the end of 2025, you were unmarried and age 55 or older, enter $9,550 for the month" (2025; sha256 da6f2f58) |
| `hsa.half` | Rate | 1/2 | [i8889] p. 7, Line 6, "divide the amount on line 5 equally between you and your spouse"; Step 2, "Divide the refigured contribution limit from Step 1 equally between you and your spouse" (2025; sha256 da6f2f58) |
| `hsa.no_months` | Count | 0 | [i8889] p. 4, Line 3, rule 2, "You are treated as having the same HDHP coverage for the entire year as you had on the first day of the last month of your tax year" (2025; sha256 da6f2f58) |
| `hsa.self_only` | NonNegDollars | $4,300 | [i8889] p. 6, Line 3 Limitation Chart, self-only coverage, "Enter $4,300 on the line below for the month" (2025; sha256 da6f2f58) |
| `hsa.self_only_55` | NonNegDollars | $5,300 | [i8889] p. 6, Line 3 Limitation Chart, self-only coverage, "If you were age 55 or older at the end of 2025, enter $5,300 for the month" (2025; sha256 da6f2f58) |
| `hsa.twelfth` | Rate | 1/12 | [i8889] p. 6, Line 3 Limitation Chart and Worksheet, "Limitation. Divide the total by 12" (2025; sha256 da6f2f58) |
| `hsa.two` | Count | 2 | [i8889] p. 7, Line 6, "Spouses who have separate HSAs" (two Forms 8889, one for each spouse) (2025; sha256 da6f2f58) |
| `hsa.year_months` | Count | 12 | [i8889] p. 4, Line 3, rule 2, "If the last-month rule ... applies, you are considered an eligible individual for the entire year. You are treated as having the same HDHP coverage for the entire year as you had on the first day of the last month of your tax year" (2025; sha256 da6f2f58) |
| `ira.full_joint` | NonNegDollars | $20,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.full_narrow` | NonNegDollars | $10,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "and the result is $10,000 or more" and "($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.kbh_both` | NonNegDollars | $16,000 | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "$16,000 if both spouses are age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.kbh_none` | NonNegDollars | $14,000 | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "If married filing jointly and line 10 is less than $14,000" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.kbh_one` | NonNegDollars | $15,000 | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "($15,000 if one spouse is age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.limit` | NonNegDollars | $7,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$7,000 if under age 50 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.limit_50` | NonNegDollars | $8,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.line2` | NonNegDollars | single $89,000; mfj $146,000; mfs $10,000; hoh $89,000; qss $146,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Single, head of household, or married filing separately and you lived apart from your spouse for all of 2025, enter $89,000", "Qualifying surviving spouse, enter $146,000", "Married filing jointly, enter $146,000 in both columns" and "Married filing separately and you lived with your spouse at any time in 2025, enter $10,000" (a separate return is refused, scope.ready) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.line2_not_covered` | NonNegDollars | $246,000 | [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.min` | NonNegDollars | $200 | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "But if it is less than $200, enter $200" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.rate_35` | Rate | 35% (0.35) | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.rate_40` | Rate | 40% (0.40) | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 40% (0.40)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.rate_70` | Rate | 70% (0.70) | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 70% (0.70)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ira.rate_80` | Rate | 80% (0.80) | [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 80% (0.80)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `medicare.additional_rate` | Rate | 9/1000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `medicare.regular_rate` | Rate | 145/10000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `medicare.threshold` | NonNegDollars | single $200,000; mfj $250,000; mfs $125,000; hoh $200,000; qss $200,000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `niit.rate` | Rate | 38/1000 | [i8960] p. 2, Application to Individuals, the applicable threshold amounts; Form 8960 line 17 (2025; printed date 2026-02-04; sha256 b10fbb23) |
| `niit.threshold` | NonNegDollars | single $200,000; mfj $250,000; mfs $125,000; hoh $200,000; qss $250,000 | [i8960] p. 2, Application to Individuals, the applicable threshold amounts; Form 8960 line 17 (2025; printed date 2026-02-04; sha256 b10fbb23) |
| `odc.per_dependent` | NonNegDollars | $500 | [f1040s8812] Schedule 8812 (2025), line 7, "Multiply line 6 by $500" (2025; created 2025-07-30; sha256 6936462d) |
| `ordinary.table_boundary` | Dollars | $100,000 | [i1040gi] Instructions for Form 1040, line 16 (Tax Table or Tax Computation Worksheet) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `person.one` | Count | 1 | [f1040] Form 1040 (2025), page 1, one entry for you and, if joint return, one for your spouse (2025; created 2025-09-05; sha256 3d31c226) |
| `qbi.rate` | Rate | 1/5 | [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2) |
| `qbi.threshold` | NonNegDollars | single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $197,300 | [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2) |
| `qc.age_limit` | Count | 19 | [i1040gi] p. 17, Step 1, "Under age 19 at the end of 2025 and younger than you" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qc.student_age_limit` | Count | 24 | [i1040gi] p. 17, Step 1, "Under age 24 at the end of 2025, a full-time student" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.fifteen_rate_ceiling` | Dollars | single $533,400; mfj $600,050; mfs $300,000; hoh $566,700; qss $600,050 | [i1040gi] QDCGT worksheet, line 13 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.rate_15` | Rate | 15% (0.15) | [i1040gi] QDCGT worksheet, line 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.rate_20` | Rate | 20% (0.20) | [i1040gi] QDCGT worksheet, line 21 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.zero_rate_ceiling` | Dollars | single $48,350; mfj $96,700; mfs $48,350; hoh $64,750; qss $96,700 | [i1040gi] QDCGT worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qr.gross_income_limit` | NonNegDollars | $5,200 | [i1040gi] p. 19, Step 4, "Who had gross income of less than $5,200 in 2025" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `refund.box_married` | NonNegDollars | $1,550 | [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `refund.box_unmarried` | NonNegDollars | $1,950 | [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "($1,950 if your 2024 filing status was single or head of household)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `refund.std_hoh` | NonNegDollars | $21,900 | [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Head of household—$21,900" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `refund.std_joint` | NonNegDollars | $29,200 | [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Married filing jointly or qualifying surviving spouse—$29,200" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `refund.std_single` | NonNegDollars | $14,600 | [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Single or married filing separately—$14,600" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ret.comp_limit` | NonNegDollars | $350,000 | [p560] chapter 5, Deduction Worksheet for Self-Employed, Step 6, "Multiply $350,000"; chapter 3, "Only $350,000 of the employee's compensation can be taken into account" (For use in preparing 2025 returns; sha256 1f1f7abe) |
| `ret.match_rate` | Rate | 3% (0.03) | [p560] chapter 3, Employer matching contributions, "up to 3% of the employee's compensation" (For use in preparing 2025 returns; sha256 1f1f7abe) |
| `ret.nonelective_rate` | Rate | 2% (0.02) | [p560] chapter 3, Nonelective contributions, "nonelective contributions of 2% of compensation" (For use in preparing 2025 returns; sha256 1f1f7abe) |
| `ret.sep_dollar_limit` | NonNegDollars | $70,000 | [p560] chapter 5, Deduction Worksheet for Self-Employed, Step 8, "Contribution dollar limit $70,000" (For use in preparing 2025 returns; sha256 1f1f7abe) |
| `ret.simple_limit` | NonNegDollars | $16,500 | [p560] chapter 3, Salary reduction contributions, "can't be more than $16,500 for 2025" (For use in preparing 2025 returns; sha256 1f1f7abe) |
| `s1.ebl_threshold` | NonNegDollars | single $313,000; mfj $626,000; mfs $313,000; hoh $313,000; qss $313,000 | [rp-2024-40] section 3.32, Threshold for Excess Business Loss, "the amount under § 461(l)(3)(A)(ii)(II) is $313,000 ($626,000 for joint returns)" (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `s1.educator_max` | NonNegDollars | $300 | [i1040gi] p. 93, Schedule 1, line 11, "up to $300 of qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `s179.max` | NonNegDollars | $2,500,000 | [i4562] p. 4, Worksheet 1, line 2, "The maximum section 179 deduction limitation for 2025 ... $2,500,000" (2025; sha256 5c1c95b7) |
| `s179.mfs_share` | Rate | 50% (0.50) | [i4562] p. 5, Line 5, "multiply the total limitation that you would otherwise enter on line 5 by 50% (0.50)" (2025; sha256 5c1c95b7) |
| `s179.suv_limit` | NonNegDollars | $31,300 | [i4562] p. 16, Column (i), "You cannot elect to expense more than $31,300 of the cost of any SUVs and certain other vehicles" (2025; sha256 5c1c95b7) |
| `s179.threshold` | NonNegDollars | $4,000,000 | [i4562] p. 4, Worksheet 1, line 6, "$4,000,000" (2025; sha256 5c1c95b7) |
| `s1a.base_joint` | NonNegDollars | $300,000 | [f1040s1a] Schedule 1-A (2025), lines 9 and 17, "Enter $150,000 ($300,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.base_other` | NonNegDollars | $150,000 | [f1040s1a] Schedule 1-A (2025), lines 9 and 17, "Enter $150,000 ($300,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.car_base_joint` | NonNegDollars | $200,000 | [f1040s1a] Schedule 1-A (2025), line 26, "Enter $100,000 ($200,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.car_base_other` | NonNegDollars | $100,000 | [f1040s1a] Schedule 1-A (2025), line 26, "Enter $100,000 ($200,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.car_max` | NonNegDollars | $10,000 | [f1040s1a] Schedule 1-A (2025), line 24, "Enter the smaller of the amount on line 23 or $10,000" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.hundred_per_thousand` | Rate | 1/10 | [f1040s1a] Schedule 1-A (2025), lines 11-12 and 19-20: the whole number of $1,000 units times $100 (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.ot_half` | Rate | 1/2 | [n-25-69] pp. 22–25, Section III.B.2, method (C), "if overtime is paid at a rate of two times the regular rate, the appropriate fraction is one-half" (Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page); sha256 e405c12d) |
| `s1a.ot_max_joint` | NonNegDollars | $25,000 | [f1040s1a] Schedule 1-A (2025), line 15, "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.ot_max_other` | NonNegDollars | $12,500 | [f1040s1a] Schedule 1-A (2025), line 15, "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.ot_quarter` | Rate | 1/4 | [n-25-69] pp. 22–25, Section III.B.2, method (D), "if overtime is paid at a rate of two times the regular rate, the appropriate fraction is one-fourth" (Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page); sha256 e405c12d) |
| `s1a.ot_third` | Rate | 1/3 | [i1040gi] pp. 106–107, Schedule 1-A, method 2, "you can divide the total amount by three (3)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `s1a.senior_amount` | NonNegDollars | $6,000 | [f1040s1a] Schedule 1-A (2025), lines 33 and 35, "enter $6,000 on line 35" and "Subtract line 34 from $6,000" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.senior_base_joint` | NonNegDollars | $150,000 | [f1040s1a] Schedule 1-A (2025), line 32, "Enter $75,000 ($150,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.senior_base_other` | NonNegDollars | $75,000 | [f1040s1a] Schedule 1-A (2025), line 32, "Enter $75,000 ($150,000 if married filing jointly)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.senior_rate` | Rate | 6% (0.06) | [f1040s1a] Schedule 1-A (2025), line 34, "Multiply line 33 by 6% (0.06)" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.tips_max` | NonNegDollars | $25,000 | [f1040s1a] Schedule 1-A (2025), line 7, "Enter the smaller of the amount on line 6 or $25,000" (2025; created 2025-11-04; sha256 64f97b38) |
| `s1a.two_hundred_per_thousand` | Rate | 1/5 | [f1040s1a] Schedule 1-A (2025), lines 28-29: the whole number of $1,000 units, rounded up, times $200 (2025; created 2025-11-04; sha256 64f97b38) |
| `sa.half` | Rate | 1/2 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.medical_rate` | Rate | 75/1000 | [f1040sa] Schedule A (2025), line 3 (2025; created 2025-11-20; sha256 c14acf34) |
| `sa.salt_base` | NonNegDollars | $40,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_floor` | NonNegDollars | $10,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_rate` | Rate | 3/10 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_threshold` | NonNegDollars | single $500,000; mfj $500,000; mfs $250,000; hoh $500,000; qss $500,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.standard_base` | NonNegDollars | single $15,750; mfj $31,500; mfs $15,750; hoh $23,625; qss $31,500 | [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sa.standard_extra` | NonNegDollars | single $2,000; mfj $1,600; mfs $1,600; hoh $2,000; qss $1,600 | [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sales.one` | Count | 1 | [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c) |
| `sales.zero` | NonNegDollars | $0 | [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c) |
| `savers.agi_limit` | Dollars | single $39,500; mfj $79,000; mfs $39,500; hoh $59,250; qss $39,500 | [f8880] p. 1, Caution, "The amount on Form 1040, 1040-SR, or 1040-NR, line 11a, is more than $39,500 ($59,250 if head of household; $79,000 if married filing jointly)"; Form 8880 (2025), line 9 table, the last band "$79,000 --- 0.0 0.0 0.0" (2025; created 2025-11-04; sha256 ba2b2877) |
| `savers.cap` | NonNegDollars | $2,000 | [f8880] Form 8880 (2025), line 6, "In each column, enter the smaller of line 5 or $2,000" (2025; created 2025-11-04; sha256 ba2b2877) |
| `sc.bonus_rate_40` | Rate | 40% (0.40) | [i4562] pp. 5–6, Line 14, "is limited to a special depreciation allowance of 40% of the depreciable basis" (2025; sha256 5c1c95b7) |
| `sc.conv_hy` | Enum(macrs_convention) | hy | [i4562] p. 11, Column (e)—Convention, Half-year convention (2025; sha256 5c1c95b7) |
| `sc.count2` | Count | 2 | [p946] p. 34, Which Convention Applies?, Mid-quarter convention, "more than 40%" (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.count5` | Count | 5 | [p946] p. 34, Which Convention Applies?, Mid-quarter convention, "more than 40%" (compared as five times the fourth-quarter bases against two times all bases) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.fifty_cents` | NonNegDollars | $0.50 | [i4562] pp. 13–14, Lines 26 and 27, "more than 50% in a qualified business use" (2025; sha256 5c1c95b7) |
| `sc.ho_max_sqft` | Count | 300 | [i1040sc] p. 12, Simplified Method Worksheet, line 2, "Don't enter more than 300 square feet" (2025; sha256 b5536db9) |
| `sc.ho_rate` | NonNegDollars | $5 | [i1040sc] p. 12, Simplified Method Worksheet, line 3a, Maximum allowable amount, "$5" (2025; sha256 b5536db9) |
| `sc.hundred_cents` | NonNegDollars | $1 | [i4562] p. 11, Column (c), the percentage of business/investment use (100%) (2025; sha256 5c1c95b7) |
| `sc.meals_rate` | Rate | 50% (0.50) | [i1040sc] p. 10, Line 24b, Amount of deduction, "In most cases, you can deduct only 50% of your business meal expenses" (2025; sha256 b5536db9) |
| `sc.meals_rate_dot` | Rate | 80% (0.80) | [i1040sc] p. 10, Line 24b, Amount of deduction, "for individuals subject to the Department of Transportation (DOT) hours of service limits, the percentage is increased to 80%" (2025; sha256 b5536db9) |
| `sc.mileage_rate` | NonNegDollars | $0.70 | [n-25-05] Section 3, "The standard mileage rate for transportation or travel expenses for 2025 is 70 cents per mile for all miles of business use" (Notice 2025-5; sha256 aac49246) |
| `sc.one` | Count | 1 | [i1040sc] p. 3, Line A, "complete a separate Schedule C for each business" (2025; sha256 b5536db9) |
| `sc.one_cent` | NonNegDollars | $0.01 | [i4562] p. 11, Column (c), the percentage of business/investment use (a percentage carried as cents of 100) (2025; sha256 5c1c95b7) |
| `sc.period_y5` | Enum(macrs_period) | y5 | [i4562] pp. 9–10, Lines 19a Through 19j, Column (a), "5-year property includes the following. Automobiles. Light general purpose trucks" (2025; sha256 5c1c95b7) |
| `sc.year1` | Count | 1 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.year2` | Count | 2 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.year3` | Count | 3 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.year4` | Count | 4 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.year5` | Count | 5 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sc.year6` | Count | 6 | [p946] p. 61, Deductions After the Recovery Period (the years of a 5-year recovery period) (For use in preparing 2025 returns; sha256 07fadfb2) |
| `sd.loss_limit` | Dollars | single -$3,000; mfj -$3,000; mfs -$1,500; hoh -$3,000; qss -$3,000 | [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b) |
| `sdtw.ordinary_ceiling` | NonNegDollars | single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $394,600 | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate15` | Rate | 15% (0.15) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate20` | Rate | 20% (0.20) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate25` | Rate | 25% (0.25) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate28` | Rate | 28% (0.28) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `se.floor` | NonNegDollars | $400 | [f1040sse] Schedule SE (2025), line 4c, "If less than $400, stop" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `se.rate_029` | Rate | 29/1000 | [f1040sse] Schedule SE (2025), line 11, "2.9% (0.029)" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `se.rate_124` | Rate | 124/1000 | [f1040sse] Schedule SE (2025), line 10, "12.4% (0.124)" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `se.rate_50` | Rate | 50% (0.50) | [f1040sse] Schedule SE (2025), line 13, "Multiply line 12 by 50% (0.50)" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `se.rate_9235` | Rate | 9235/10000 | [f1040sse] Schedule SE (2025), line 4a, "multiply line 3 by 92.35% (0.9235)" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `se.wage_base` | NonNegDollars | $176,100 | [f1040sse] Schedule SE (2025), line 7, "$176,100" (2025; created 2025-05-07; sha256 05bc2b3e) |
| `sli.base_joint` | NonNegDollars | $170,000 | [i1040gi] p. 99, Student Loan Interest Deduction Worksheet, line 5, "Married filing jointly—$170,000" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sli.base_other` | NonNegDollars | $85,000 | [i1040gi] p. 99, Student Loan Interest Deduction Worksheet, line 5, "Single, head of household, or qualifying surviving spouse—$85,000" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sli.divisor_joint` | NonNegDollars | $30,000 | [i1040gi] p. 99, Student Loan Interest Deduction Worksheet, line 7, "($30,000 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sli.divisor_other` | NonNegDollars | $15,000 | [i1040gi] p. 99, Student Loan Interest Deduction Worksheet, line 7, "Divide line 6 by $15,000" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sli.max` | NonNegDollars | $2,500 | [i1040gi] p. 99, Student Loan Interest Deduction Worksheet, line 1, "Don't enter more than $2,500" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table1_160` | Rate | 1/160 | [i1040gi] p. 29, Simplified Method Worksheet, Table 1, age 71 or older, annuity starting date after November 18, 1996: 160 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table1_210` | Rate | 1/210 | [i1040gi] p. 29, Simplified Method Worksheet, Table 1, age 66-70, annuity starting date after November 18, 1996: 210 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table1_260` | Rate | 1/260 | [i1040gi] p. 29, Simplified Method Worksheet, Table 1, age 61-65, annuity starting date after November 18, 1996: 260 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table1_310` | Rate | 1/310 | [i1040gi] p. 29, Simplified Method Worksheet, Table 1, age 56-60, annuity starting date after November 18, 1996: 310 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table1_360` | Rate | 1/360 | [i1040gi] p. 29, Simplified Method Worksheet, Table 1, age 55 or under, annuity starting date after November 18, 1996: 360 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table2_210` | Rate | 1/210 | [i1040gi] p. 29, Simplified Method Worksheet, Table 2, combined ages 141 or older: 210 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table2_260` | Rate | 1/260 | [i1040gi] p. 29, Simplified Method Worksheet, Table 2, combined ages 131-140: 260 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table2_310` | Rate | 1/310 | [i1040gi] p. 29, Simplified Method Worksheet, Table 2, combined ages 121-130: 310 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table2_360` | Rate | 1/360 | [i1040gi] p. 29, Simplified Method Worksheet, Table 2, combined ages 111-120: 360 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `smw.table2_410` | Rate | 1/410 | [i1040gi] p. 29, Simplified Method Worksheet, Table 2, combined ages 110 or under: 410 (line 4 divides line 2 by it) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.base` | NonNegDollars | $176,100 | [i1040gi] p. 117, Schedule 3 line 11; independently confirmed iw2w3 p. 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.limit` | NonNegDollars | $10,918.20 | [i1040gi] p. 117, Schedule 3 line 11; independently confirmed iw2w3 p. 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.one` | Count | 1 | [i1040gi] p. 117, Schedule 3 line 11, more than one employer (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.zero` | NonNegDollars | $0 | [i1040gi] p. 117, Schedule 3 line 11, amount withheld in excess (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.adjust_joint` | NonNegDollars | $12,000 | [i1040gi] p. 32, Social Security Benefits Worksheet, line 10, $12,000 if married filing jointly (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.adjust_single` | NonNegDollars | $9,000 | [i1040gi] p. 32, Social Security Benefits Worksheet, line 10, $9,000 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.base_joint` | NonNegDollars | $32,000 | [i1040gi] p. 32, Social Security Benefits Worksheet, line 8, $32,000 if married filing jointly (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.base_single` | NonNegDollars | $25,000 | [i1040gi] p. 32, Social Security Benefits Worksheet, line 8, $25,000 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.half` | Rate | 1/2 | [i1040gi] p. 32, Social Security Benefits Worksheet, lines 2 and 13, 50% (0.50) and one-half (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ssb.rate85` | Rate | 85% (0.85) | [i1040gi] p. 32, Social Security Benefits Worksheet, lines 15, 16 and 17, 85% (0.85) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section D, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.subtract` | Dollars | $6,825 | [i1040gi] TCW Section D, row 1 (subtraction amount $6,825.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section D, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section D, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.subtract` | Dollars | $8,892 | [i1040gi] TCW Section D, row 2 (subtraction amount $8,892.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section D, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section D, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.subtract` | Dollars | $24,676 | [i1040gi] TCW Section D, row 3 (subtraction amount $24,676.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.upper` | Dollars | $250,500 | [i1040gi] TCW Section D, row 3 (not over $250,500) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section D, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.subtract` | Dollars | $32,191 | [i1040gi] TCW Section D, row 4 (subtraction amount $32,191.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.upper` | Dollars | $626,350 | [i1040gi] TCW Section D, row 4 (not over $626,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section D, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b5.subtract` | Dollars | $44,718 | [i1040gi] TCW Section D, row 5 (subtraction amount $44,718.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section B, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.subtract` | Dollars | $10,172 | [i1040gi] TCW Section B, row 1 (subtraction amount $10,172.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.upper` | Dollars | $206,700 | [i1040gi] TCW Section B, row 1 (not over $206,700) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section B, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.subtract` | Dollars | $14,306 | [i1040gi] TCW Section B, row 2 (subtraction amount $14,306.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.upper` | Dollars | $394,600 | [i1040gi] TCW Section B, row 2 (not over $394,600) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section B, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.subtract` | Dollars | $45,874 | [i1040gi] TCW Section B, row 3 (subtraction amount $45,874.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.upper` | Dollars | $501,050 | [i1040gi] TCW Section B, row 3 (not over $501,050) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section B, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.subtract` | Dollars | $60,905.50 | [i1040gi] TCW Section B, row 4 (subtraction amount $60,905.50) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.upper` | Dollars | $751,600 | [i1040gi] TCW Section B, row 4 (not over $751,600) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section B, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b5.subtract` | Dollars | $75,937.50 | [i1040gi] TCW Section B, row 5 (subtraction amount $75,937.50) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section C, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.subtract` | Dollars | $5,086 | [i1040gi] TCW Section C, row 1 (subtraction amount $5,086.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section C, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section C, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.subtract` | Dollars | $7,153 | [i1040gi] TCW Section C, row 2 (subtraction amount $7,153.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section C, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section C, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.subtract` | Dollars | $22,937 | [i1040gi] TCW Section C, row 3 (subtraction amount $22,937.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.upper` | Dollars | $250,525 | [i1040gi] TCW Section C, row 3 (not over $250,525) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section C, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.subtract` | Dollars | $30,452.75 | [i1040gi] TCW Section C, row 4 (subtraction amount $30,452.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.upper` | Dollars | $375,800 | [i1040gi] TCW Section C, row 4 (not over $375,800) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section C, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b5.subtract` | Dollars | $37,968.75 | [i1040gi] TCW Section C, row 5 (subtraction amount $37,968.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section A, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.subtract` | Dollars | $5,086 | [i1040gi] TCW Section A, row 1 (subtraction amount $5,086.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section A, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section A, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.subtract` | Dollars | $7,153 | [i1040gi] TCW Section A, row 2 (subtraction amount $7,153.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section A, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section A, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.subtract` | Dollars | $22,937 | [i1040gi] TCW Section A, row 3 (subtraction amount $22,937.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.upper` | Dollars | $250,525 | [i1040gi] TCW Section A, row 3 (not over $250,525) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section A, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.subtract` | Dollars | $30,452.75 | [i1040gi] TCW Section A, row 4 (subtraction amount $30,452.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.upper` | Dollars | $626,350 | [i1040gi] TCW Section A, row 4 (not over $626,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section A, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b5.subtract` | Dollars | $42,979.75 | [i1040gi] TCW Section A, row 5 (subtraction amount $42,979.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
