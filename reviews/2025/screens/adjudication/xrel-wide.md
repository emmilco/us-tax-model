# Screen and false-no adjudication, xrel lane, family wide (2025, us)

Sampled release screen and false-no reviews (claude-opus-5-5) of the wide family's units, ruled 2026-11-15 in the xint tree. Rulings are in `/tmp/xrel/frag/wide.screens.json` and `/tmp/xrel/frag/wide.false_no.json`. Each finding was checked against the gate's current question and help (`interview/2025/questions.yaml`), the gated lines (`forms/2025/`) and the quoted source. `xw-NN` stands for the pending entry xrelwide-NN, numbered at integration in order: xw-01 is BUG-0893 and xw-15 is BUG-0907.

## Screens

Samples: 29. Findings: 83. Classes: defect 22, covered 22, accepted WIDE 19, accepted residual 18, model error 2.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:f1040.digital_assets#1` | 0: defect (xw-04); 1: accepted WIDE | defect: the gate help treats a holder credited with staking or fork coins as a No (BUG-0896) |
| `gate:f1040.estimated_any#1` | 0: defect (xw-05); 1: defect (xw-05); 2: defect (xw-05) | defect: amended-return overpayment and joint payments sent by a former spouse are outside the gate wording (BUG-0897) |
| `gate:f1040.withheld_other_any#1` | 0: defect (xw-06); 1: defect (xw-06) | defect (low): the help does not name Forms 8805 and 8288-A (BUG-0898) |
| `gate:rec.has_mortgage_if_path#1` | 0: accepted residual; 1: covered | no gate defect; a form pointer and the spouse reading |
| `gate:rec.has_other_if_path#1` | 0: covered; 1: covered; 2: covered | no gate defect; earlier years and sales tax are refused, reimbursements are named |
| `gate:rec.has_property_tax_if_path#1` | 0: covered | no gate defect; the question asks about tax deducted for 2024 |
| `gate:rec.joint_any#1` | 0: covered; 1: accepted residual | no gate defect; state income tax refunds take the refund path, which has its own separate-returns question |
| `gate:rec.path#1` | 0: defect (xw-07); 1: accepted residual; 2: accepted residual; 3: accepted WIDE | defect: the joint-return whose-return case (BUG-0899); the rest residual or accepted WIDE |
| `gate:refund.worksheet#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect |
| `gate:s2.amt_pab_ask#1` | 0: covered; 1: accepted WIDE | no gate defect; fund private activity bond dividends are refused through Form 1099-DIV box 13 |
| `gate:s2.options_any#1` | 0: accepted residual; 1: model error; 2: accepted residual; 3: accepted WIDE | no gate defect; line 8k is gated by the outer question itself |
| `gate:scope.artist_official_if_w2#1` | 0: covered; 1: accepted WIDE | no gate defect; a fee-basis official without a W-2 is refused through the pay or self-employment screens |
| `gate:scope.business_before#1` | 0: covered; 1: covered; 2: accepted residual | no gate defect; a 2025 interest is handled by its own K-1 entry |
| `gate:scope.foreign_shares#1` | 0: defect (xw-13); 1: defect (xw-13); 2: defect (xw-13); 3: accepted WIDE | defect: options or warrants, foreign ETFs and foreign-incorporated U.S.-listed stock (BUG-0905) |
| `gate:scope.has_w2#1` | 0: accepted residual; 1: accepted residual; 2: covered; 3: covered; 4: covered; 5: covered; 6: covered; 7: accepted residual; 8: accepted WIDE | no gate defect; the no-W-2 cases are refused by other screens |
| `gate:scope.household_pay_if_pay#1` | 0: defect (xw-11); 1: covered; 2: accepted WIDE | defect (low): a driver or groundskeeper reads as a No (BUG-0903) |
| `gate:scope.medicaid_waiver#1` | 0: defect (xw-12); 1: defect (xw-12) | defect: pay through an agency or fiscal agent, and the present tense (BUG-0904) |
| `gate:scope.nol#1` | 0: defect (xw-15); 1: defect (xw-15) | defect: help limits the carried loss (BUG-0907) |
| `gate:scope.recovery#1` | 0: defect (xw-16); 1: covered; 2: accepted residual; 3: accepted residual; 4: accepted residual | defect (low): the help ties the standard-deduction test to 2024 (BUG-0908); other findings covered or residual |
| `gate:scope.religious_work#1` | 0: defect (xw-17); 1: accepted WIDE | defect (low): members of a religious order are not named (BUG-0909) |
| `gate:scope.rental#1` | 0: defect (xw-18); 1: accepted WIDE | defect (low): 'anything you own' misses a leased item sublet (BUG-0910) |
| `gate:scope.strike_pay_if_pay#1` | 0: defect (xw-14); 1: defect (xw-14); 2: accepted residual | defect: lockout benefits and non-union strike funds (BUG-0906) |
| `gate:scope.unearned_2700_if_under24#1` | 0: accepted residual; 1: accepted WIDE; 2: accepted WIDE; 3: accepted WIDE | no gate defect |
| `rec.nonitemized#1` | 0: covered; 1: accepted residual; 2: accepted WIDE; 3: accepted WIDE | no screen defect |
| `rec.not_2024#1` | 0: covered; 1: accepted WIDE; 2: accepted residual | no screen defect |
| `rec.sales_tax#1` | 0: accepted WIDE; 1: accepted residual | no screen defect |
| `rec.two_returns#1` | 0: defect (xw-07) | defect: a state refund of the other spouse's separate 2024 return is not counted (BUG-0899, extended) |
| `refund.exc_tax#1` | 0: model error | no screen defect |
| `refund.exc_who#1` | 0: covered; 1: defect (xw-03); 2: accepted WIDE | defect (low): a 2024 dual-status filer (BUG-0895) |

## False-no

Samples: 31. Findings: 158. Classes: accepted residual 58, defect 57, covered 41, model error 2.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:f1040.digital_assets#1` | 0: defect (xw-04); 1: defect (xw-04); 2: accepted residual; 3: defect (xw-04) | defect: airdrops not named in the gated question and passive rewards read as holding (BUG-0896) |
| `gate:f1040.estimated_any#1` | 0: defect (xw-05); 1: defect (xw-05); 2: defect (xw-05); 3: defect (xw-05); 4: defect (xw-05); 5: accepted residual; 6: defect (xw-02) | defect: gate wording misses amended-return credits and joint payments by a spouse or former spouse (BUG-0897); separate-return share BUG-0894 |
| `gate:f1040.withheld_other_any#1` | 0: defect (xw-06); 1: defect (xw-06); 2: covered; 3: covered; 4: covered; 5: accepted residual; 6: covered | defect (low): Forms 8805 and 8288-A not named (BUG-0898); the other findings are covered by the help |
| `gate:rec.has_medical_if_path#1` | 0: defect (xw-07); 1: covered; 2: accepted residual; 3: accepted residual; 4: covered; 5: model error | defect: on a joint 2025 return with separate 2024 returns, the itemizing question does not say whose return (BUG-0899); the other findings are covered or residual |
| `gate:rec.has_mortgage_if_path#1` | 0: defect (xw-07); 1: accepted residual; 2: covered; 3: covered; 4: covered | defect: the joint-return whose-return case (BUG-0899); the rest covered or residual |
| `gate:rec.has_other_if_path#1` | 0: covered; 1: defect (xw-07); 2: covered; 3: covered; 4: accepted residual | defect: the joint-return whose-return case (BUG-0899); the rest covered or residual |
| `gate:rec.has_property_tax_if_path#1` | 0: defect (xw-07); 1: accepted residual; 2: covered; 3: accepted residual; 4: covered | defect: the joint-return whose-return case (BUG-0899); the rest covered or residual |
| `gate:rec.joint_any#1` | 0: covered; 1: defect (xw-07); 2: covered; 3: accepted residual; 4: accepted residual; 5: accepted residual | defect: whose-return wording on a joint return (BUG-0899); earlier years refused; the rest covered or residual |
| `gate:rec.path#1` | 0: covered; 1: covered; 2: defect (xw-07); 3: accepted residual; 4: accepted residual; 5: accepted residual; 6: accepted residual | defect: the joint-return whose-return case (BUG-0899); earlier years and sales tax refused; the rest residual |
| `gate:refund.two_returns_if_joint#1` | 0: covered; 1: accepted residual; 2: accepted residual; 3: accepted residual | no gate defect; other-year refunds are refused, the rest residual |
| `gate:refund.worksheet#1` | 0: covered; 1: covered; 2: covered; 3: covered; 4: covered | no gate defect; other-year refunds and the both-returns case are refused |
| `gate:s2.amt_boat_ask#1` | 0: defect (xw-08); 1: defect (xw-08); 2: defect (xw-08); 3: defect (xw-08) | defect: the help rules out a house or condominium used on a transient basis (BUG-0900) |
| `gate:s2.amt_pab_ask#1` | 0: covered; 1: covered; 2: covered; 3: accepted residual | no gate defect; fund dividends and K-1 amounts are refused elsewhere; a missing box 9 is a low residual |
| `gate:s2.household_help#1` | 0: defect (xw-09); 1: defect (xw-09); 2: defect (xw-09); 3: defect (xw-09); 4: accepted residual | defect: payroll service, registry, driver and January pay readings (BUG-0901); paid relatives a low residual |
| `gate:s2.options_any#1` | 0: covered; 1: model error; 2: accepted residual; 3: accepted residual; 4: accepted residual | no gate defect; ISO vesting is asked by s2.iso_vested; the rest model error or residual |
| `gate:scope.armed_forces#1` | 0: defect (xw-10); 1: defect (xw-10) | defect (low): surviving spouse and Coast Guard readings (BUG-0902) |
| `gate:scope.artist_official_if_w2#1` | 0: covered; 1: accepted residual; 2: accepted residual; 3: accepted residual | no gate defect; the no-W-2 cases are refused elsewhere; occupation readings are low residuals |
| `gate:scope.business_before#1` | 0: covered; 1: accepted residual; 2: accepted residual; 3: accepted residual; 4: accepted residual | no gate defect; current-year interests are entered as K-1s; reading residuals low |
| `gate:scope.foreign_shares#1` | 0: defect (xw-13); 1: defect (xw-13); 2: defect (xw-13); 3: defect (xw-13); 4: accepted residual; 5: accepted residual | defect: gate wording (BUG-0905); K-1 foreign items and early-year sales are low residuals |
| `gate:scope.has_w2#1` | 0: covered; 1: covered; 2: covered; 3: covered; 4: covered; 5: covered; 6: covered; 7: accepted residual; 8: covered | no gate defect; each no-W-2 case is refused by another screen |
| `gate:scope.household_pay_if_pay#1` | 0: defect (xw-11); 1: covered; 2: defect (xw-11); 3: accepted residual; 4: accepted residual | defect (low): driver and shared-home readings (BUG-0903); the rest covered or residual |
| `gate:scope.medicaid_waiver#1` | 0: defect (xw-12); 1: defect (xw-12); 2: defect (xw-12); 3: accepted residual; 4: accepted residual | defect: agency-paid waiver pay, the code II test and the present tense (BUG-0904) |
| `gate:scope.nol#1` | 0: defect (xw-15); 1: defect (xw-15); 2: defect (xw-15); 3: accepted residual; 4: accepted residual | defect: help limits the carried loss (BUG-0907); estate and former-spouse cases low residuals |
| `gate:scope.noncitizen#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual | no gate defect; the question asks about any time in 2025 |
| `gate:scope.pay_no_w2#1` | 0: defect (xw-14); 1: defect (xw-14); 2: defect (xw-14); 3: defect (xw-14); 4: defect (xw-14); 5: defect (xw-14); 6: defect (xw-14); 7: accepted residual | defect: lockout, noncash and small tips, code H, and no-W-2 employers (BUG-0906) |
| `gate:scope.recovery#1` | 0: defect (xw-16); 1: covered; 2: accepted residual; 3: accepted residual; 4: accepted residual; 5: defect (xw-16); 6: defect (xw-16) | defect (low): help wording (BUG-0908); other findings covered or residual |
| `gate:scope.religious_work#1` | 0: accepted residual; 1: defect (xw-17); 2: defect (xw-17); 3: defect (xw-17); 4: accepted residual | defect (low): order members, in-kind pay, other titles (BUG-0909); the rest residual |
| `gate:scope.rental#1` | 0: defect (xw-18); 1: accepted residual; 2: covered; 3: accepted residual | defect (low): leased property sublet (BUG-0910); the rest covered or residual |
| `gate:scope.strike_pay_if_pay#1` | 0: defect (xw-14); 1: defect (xw-14); 2: accepted residual; 3: accepted residual | defect: non-union funds and lockout (BUG-0906); gifts and in-kind support residual |
| `gate:scope.tips_unreported_if_pay#1` | 0: defect (xw-14); 1: defect (xw-14) | defect: noncash tips behind the not-on-a-W-2 parent (BUG-0906) |
| `gate:scope.unearned_2700_if_under24#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual; 3: accepted residual; 4: accepted residual | no gate defect; the question asks about all income that is not pay for work |

## Defects (pending)

- BUG-0893 (low): Wages earned while an inmate that are in W-2 box 1 are counted twice, on line 1a and on Schedule 1 line 8u. Proposed fix: Ask, after s1.inmate_amount, how much of it is in box 1 of a W-2 entered here, and subtract that part from line 1a (a helper on f1040.line1a), or refuse when any of it is in W-2 box 1; at least say in the help of s1.inmate_amount that W-2 wages for this work are entered here and not with the W-2.
- BUG-0894 (low): On a separate return, the estimated tax question does not say how to divide joint estimated payments. Proposed fix: On a separate return, add to the help (or a separate-return variant of the prompt): 'If you and your spouse made joint estimated payments, enter only your share: any split you both agree on, or, if you do not agree, the part in proportion to each of your separate 2025 taxes.' Alternatively refuse a ...
- BUG-0895 (low): The state refund worksheet is used for a filer who was a dual-status alien for 2024 and so had no standard deduction. Proposed fix: Add a limb to refund.exc_who: 'you were a nonresident alien for any part of 2024 (a dual-status year), whichever form you filed'; the same Pub. 525 route then applies.
- BUG-0896 (medium): Digital asset questions: staking or fork coins credited while only holding read as a No, and airdrops are not named for line 8v. Proposed fix: Gate help: 'Holding is a No only if nothing new was added to your account: staking or earn rewards, coins from a fork and tokens dropped into your wallet (an airdrop) are a Yes even if you did nothing.' Gated question: 'receive any crypto from staking, from mining that is not a business, from a ...
- BUG-0897 (medium): Estimated tax gate misses an amended-return overpayment and joint payments sent by a spouse or former spouse. Proposed fix: Prompt: 'Were estimated tax payments made for 2025 by you, your spouse, or jointly with a spouse or former spouse (whoever sent them), or was an overpayment from your 2024 return or an amended return applied to your 2025 tax?' Help: count payments made by mail, online or card, including the one due ...
- BUG-0898 (low): Other withholding gate help does not name Forms 8805 and 8288-A. Proposed fix: Help: 'Tax withheld on a Schedule K-1 or on Form 1042-S, 8805 or 8288-A counts too, even if no money was paid to you.'
- BUG-0899 (medium): Recoveries on a joint return: the 2024 itemizing question does not say whose return when only the spouse itemized on a separate 2024 return. Proposed fix: Add to rec.two_returns the help refund.two_returns has: 'If only one of you got money back, answer No; the questions that follow are then about that person's own 2024 return.' On a joint return word refund.itemized 'Did you (or, if only your spouse got money back, your spouse) itemize deductions on ...
- BUG-0900 (medium): AMT mortgage interest question: its help rules out a house or condominium used on a transient basis. Proposed fix: Prompt: 'Is any of the mortgage interest you deduct for a home that was not your main home and was a boat, motor home, camper, travel trailer or other recreational vehicle, or a house, apartment, condominium, mobile home or timeshare used on a transient basis (such as short-term or rental-pool ...
- BUG-0901 (medium): Household employee gate: a nanny paid through a payroll service or registry, a private driver, and January pay for 2024 work read as a No. Proposed fix: Help: 'Count a worker you direct even if a payroll service, agency or registry handles the pay; do not count a business that supplies and directs its own staff, such as a cleaning company or daycare center. Count a private driver or other household worker who works away from the home, and pay made ...
- BUG-0902 (low): Armed forces gate: a surviving spouse moving under orders after a member's death, and Coast Guard members. Proposed fix: Prompt: 'Since the start of 2022, did you or your spouse (including a spouse who has died) serve in the U.S. armed forces (including the Coast Guard), the reserves or the National Guard?'
- BUG-0903 (low): Household pay question: a driver or groundskeeper, and a live-in carer in a home the worker shares, read as a No. Proposed fix: Prompt: 'were you (or, on a joint return, your spouse) paid by a household, with no W-2, for work in or around its home or for its members, such as a nanny, carer, housekeeper, gardener or private driver, including a home you live in?'
- BUG-0904 (medium): Medicaid waiver gate asks whether a state program paid the filer, missing pay that runs through an agency or fiscal agent. Proposed fix: Prompt: 'In 2025, were you (or, on a joint return, your spouse) paid under a Medicaid waiver program, directly or through an agency, plan or fiscal agent, to care for someone who lived in your home with you? Answer Yes also if any W-2 shows code II in box 12.'
- BUG-0905 (medium): Foreign shares gate: options or warrants, foreign-incorporated stock or ADRs bought in the U.S., foreign ETFs, and holdings through an estate or foreign pension. Proposed fix: Prompt: 'In 2025, did you ... own, at any time, shares or units of a company or fund set up outside the United States, or options or warrants to buy them, other than through a mutual fund or ETF set up in the United States?' Help: 'Count stock or ADRs traded on a U.S. exchange if the company is ...
- BUG-0906 (medium): Pay-not-on-a-W-2 gate: lockout benefits, strike funds that are not a union, noncash or small tips, and wages from an employer that issues no W-2. Proposed fix: Prompt: 'wages, tips, or strike or lockout benefits that are not on a W-2?' Help: 'Such as pay for work in someone's home, tips you did not report to your employer for any reason (including small amounts) and tips that were not money, such as tickets or passes (never on a W-2), pay from an employer ...
- BUG-0907 (medium): Net operating loss gate: a disallowed excess business loss, a first-year carryforward, and rental or K-1 losses read as a No. Proposed fix: Help: 'A loss bigger than that year's income that is carried into 2025, including a 2024 loss not yet used on any return and a business loss limited on Form 461 (an excess business loss), whatever its source: a business or farm (including a K-1 share), rentals, or a federally declared disaster.'
- BUG-0908 (low): Recovery gate help: the standard-deduction test is tied to 2024 rather than to the year of the deduction, and nonitemized, credit and sales tax recoveries are not given as examples. Proposed fix: Help: 'If you took the standard deduction for the year you deducted it, money back for something you could deduct only by itemizing is not income. Count also a repaid bad debt or refunded business expense you deducted, a rebate on something you took a credit for, and a refund of sales tax you ...
- BUG-0909 (low): Religious work gate does not name members of a religious order, pay in housing or offerings, or officiants paid by families. Proposed fix: Prompt: 'In 2025, were you (or, on a joint return, your spouse) paid for work by a church or other religious body, or paid in any form (money, housing, offerings) for work as clergy of any title or as a member of a religious order, whoever paid you?'
- BUG-0910 (low): Rental gate asks about renting out 'anything you own', missing property the filer leases and sublets. Proposed fix: Prompt: 'rent out, or offer for rent, anything you own or lease, such as a house, a room, land, a vehicle or equipment, or receive royalties?'

Model errors: `gate:s2.options_any` (screen 1, false-no 1) read a line label as an inner exercise helper; `s1.stock_options_if_options` guards on `s2.options_any` itself. `refund.exc_tax` applied the Pub. 525 capital-gains refiguring paragraph to the Form 1040 worksheet route. `rec.has_medical_if_path` finding 5 assumed `rec.path` tests whether Worksheet 2 is needed.

Covered by refusals elsewhere (not defects): Form 1099-DIV box 13 (`div.amt`), K-1 box 17 (k1p), solo 401(k) (`person.plan_screen`), 409A and golden parachute taxes (`s2.other_tax`), earlier-year recoveries (`rec.not_2024`), sales tax refunds (`rec.sales_tax`), other-year state refunds (`refund.other_year`), wages with no W-2 (`scope.wages_no_form_if_pay`), ISO vesting (`s2.iso_vested`).
