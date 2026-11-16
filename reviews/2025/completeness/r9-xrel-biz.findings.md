# Completeness review, release sample (xrel, family biz): adjudication of 42 claims

Ruled by the biz fork (claude-opus-5-5, judgment) with eight sub-lanes (L1 to L8), each checking quotes against `sources/2025/*.cols.txt`, the form YAML, the interview wording and, where an amount mattered, engine evals on fixture copies under `/tmp/xrel/biz/`. The fork merged duplicates (one bug per defect), checked a sample of rulings (s179.mfs still refuses a separate-return election; the home equity part of the interest finding is refused by sa.mortgage_other_use and was removed from BUG-0777), and filed the pending bugs. Fragments: `/tmp/xrel/frag/biz.<tool>.json`; `xrel.py merge` (validate only) prints no REFUSED line. `rulings.json` was not edited.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| asset | 2 | 0 | 0 | 2 | 0 | 0 |
| carloan | 1 | 0 | 0 | 0 | 1 | 0 |
| f4562 | 10 | 0 | 2 | 7 | 1 | 0 |
| rental | 10 | 8 | 1 | 1 | 0 | 0 |
| rf4562 | 4 | 0 | 0 | 4 | 0 | 0 |
| s179 | 4 | 0 | 0 | 4 | 0 | 0 |
| sc | 4 | 0 | 1 | 2 | 1 | 0 |
| scveh | 3 | 0 | 0 | 2 | 1 | 0 |
| se | 3 | 0 | 0 | 3 | 0 | 0 |
| u1250 | 1 | 0 | 0 | 1 | 0 | 0 |
| total | 42 | 8 | 4 | 26 | 4 | 0 |

Real gaps cite pending ids; they fail the gate until the numbered-bug pass (accepted for tonight). rental#1.1 cites the existing BUG-0836 (the MFS-lived-together special allowance).

## asset

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| asset#1.1 | out of scope | rprop.personal | i4562 p. 10, 5-year property, "Appliances, carpets, furniture, etc., used in a rental real estate activity." (quote checked in sources/2025/i4562). An asset entry belongs to a Schedule C business (f4562 collection parent sc), and Schedule C refuses a rental … |
| asset#1.2 | out of scope | scope.farm | p946 p. 35, Depreciation Methods for Farm Property, "If you place personal property in service in a farming business after 1988, and before 2018, you must generally depreciate it under GDS using the 150% declining balance method"; i4562 p. 12 (quotes checked … |

## carloan

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| carloan#1.1 | presentation |  | i1040gi pp. 109-110, "In order to take the QPVLI deduction, you must include the vehicle identification number (VIN) ... on your tax return", substitute VIN for a lemon-law replacement, "Enter the VIN(s) of the APV(s) on line 22, column (i)", attached … |

## f4562

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| f4562#1.1 | covered | s179.line12 | i4562 p. 5, Lines 5 to 12. f4562.line12 copies sc.s179_allowed, the business's share of the return's Part I (s179): s179.line5 with the married-filing-separately 50% share (s179.line5_mfs) and a refusal of any section 179 election or carryover on a separate … |
| f4562#1.2 | out of scope | asset.screened | i4562 p. 9, Line 17, partial dispositions and "Prior years' depreciation, plus current year's depreciation, can never exceed the depreciable basis" (checked). A disposal of part of the asset in 2025 is refused by asset.ended_this_year ('did you sell, give … |
| f4562#1.3 | out of scope | asset.screened | i4562 pp. 9, 11-12 (quotes checked). What is encoded: the business-use basis (asset.basis from asset.cost x asset.pct), section 179 and the allowance before MACRS (asset.after179, asset.ub), and the mid-quarter 40% test (form mq, mq.applies, with … |
| f4562#1.4 | out of scope | asset.screened | i4562 p. 11 (quotes checked). Trees and vines bearing fruits or nuts are farm property: their class is outside in class_lives (asset.outside, 'Certain Property for Which Recovery Periods Assigned' and agricultural classes) and farm income is refused by … |
| f4562#1.5 | out of scope | asset.screened | i4562 pp. 11-13, ADS and real property (quotes checked). asset.kind_excluded refuses buildings and their parts and land ('Is this a building or part of one, land, ...'); asset.ads_required refuses property that must use ADS and asset.method_other an ADS … |
| f4562#1.6 | out of scope | asset.screened | i4562 pp. 13-14, Line 25 (quotes checked). Listed property whose qualified business use is 50% or less is refused (asset.qbu_low in asset.screen; asset.listed_low; scveh.qbu_low for vehicles), so no allowance is taken on it; aircraft are refused by … |
| f4562#1.7 | out of scope | scveh.screened | i4562 pp. 14-15, Lines 26 and 27 (quotes checked). Encoded for vehicles in scveh: business miles excluding commuting (scveh.miles_business, scveh.miles_commuting), the 50% test (scveh.over_half), the passenger-automobile limits (tables auto_limit, … |
| f4562#1.8 | out of scope | asset.listed_low | i4562 pp. 14-15, line 27 (quotes checked). Listed property used 50% or less in a qualified business use is refused: asset.listed_low gates asset.basis ('Listed property used 50% or less for business is depreciated under ADS and is outside this tool') and … |
| f4562#1.9 | covered | scveh.line10 | i4562 pp. 13, 15 (quotes checked). Section 179 on listed property other than vehicles: asset.s179_bad refuses an election on property not used more than 50% in the business, and asset.listed_low refuses listed property at 50% or less. Vehicles: scveh refuses … |
| f4562#1.10 | presentation |  | i4562 p. 13, Part V, Form 2106 and Schedule C Part IV (quotes checked). Where the vehicle information is reported changes no amount. Form 2106 is an employee form, not a Schedule C business; a Schedule C vehicle on the standard mileage rate is reported in … |

## rental

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| rental#1.1 | real gap | BUG-0836 | Two cases. (1) Real estate professional (i1040se p. 3; i8582 p. 3): refused, not a gap. sche.re_pro ('Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all your work time?', tick in the rental_return … |
| rental#1.2 | real gap | BUG-0779 | i8582 p. 3: 'The rental of property is incidental to an activity of holding property for investment if the main purpose of holding the property is to realize a gain from its appreciation and the gross rental income is less than 2% of the smaller of the … |
| rental#1.3 | real gap | BUG-0775 | p527 p. 27, Days used as a main home before or after renting: main-home days are not personal-use days for the home test, 'However, this special rule doesn't apply when dividing expenses between rental and personal use. See Property Changed to Rental Use in … |
| rental#1.4 | covered | rental.rents | i1040se p. 5, Line 3: FMV of services or property received as rent, and other rental income, go on line 3. rental.rents asks the rent received 'including advance rent and expenses a tenant paid for you', with help 'Include a security deposit you kept and … |
| rental#1.5 | real gap | BUG-0776 | i1040se p. 6, Line 10: 'Do not deduct legal fees paid or incurred to defend or protect title to property, to recover property, or to develop or improve property. Instead, you must capitalize these fees and add them to the property's basis.' rental.amt10 asks … |
| rental#1.6 | real gap | BUG-0777 | i1040se p. 6, Lines 12 and 13: 'you must have records to show how the proceeds of each debt were used'; 'In general, you allocate interest on a loan the same way you allocate the loan proceeds.' rental.amt12 asks 'Mortgage interest on it shown on Form 1098 … |
| rental#1.7 | out of scope | rental.part_home | i1040se p. 7, Line 17: 'the base rate ... for local telephone service for the first telephone line into your residence is a personal expense'. A rental that is part of the filer's residence is refused (rental.part_home, 'Is it part of a property you also live … |
| rental#1.8 | real gap | BUG-0776 | i1040se p. 6, Lines 5 Through 21: 'Do not deduct the value of your own labor or amounts paid for capital investments or capital improvements.' Own labor: every cost question asks an amount 'paid in 2025', which excludes the value of one's own labor (no gap). … |
| rental#1.9 | real gap | BUG-0781 | i1040se p. 3, At-Risk Rules: not at risk are amounts 'protected against loss by a guarantee, stop-loss agreement, or other similar arrangement' and 'Amounts borrowed for use in the activity from a person who has an interest in the activity (other than as a … |
| rental#1.10 | real gap | BUG-0778 | p527 p. 28, Limit on deductions: 'The excess expenses that can't be used to offset income from other sources are carried forward to the next year and treated as rental expenses for the same property. ... This limitation will apply to expenses carried forward … |

## rf4562

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| rf4562#1.1 | out of scope | rprop.screen | i1040se p. 7, Line 18: Form 4562 is needed for listed property, a section 179 deduction or amortization beginning in 2025. Each case is refused before rf4562.needed matters: a vehicle at rental.vehicle ('Car, truck or travel costs for it', refuses at … |
| rf4562#1.2 | out of scope | rprop.screen | i1040se p. 7; i4562 p. 9, Line 17. rprop.screen refuses 'you sold, gave away or stopped renting it in 2025' (use ended, partial disposition) and 'its basis changed after you began depreciating it, other than by depreciation', and ADS or other methods. Prior … |
| rf4562#1.3 | out of scope | sd.other_forms | i1040se p. 7; i4562 p. 9. Land: rprop.basis asks 'what you paid for the building or improvement, not the land', with help 'the price (with closing costs) less the part for the land; your property tax bill's split of land and building may be used' (covered). … |
| rf4562#1.4 | out of scope | sd.other_forms | Same as rf4562#1.3, for line 19j (nonresidential real property placed in service in 2025): land excluded by rprop.basis and its help; placed-in-service date asked as first ready and available for rent (rprop.month/rprop.year); a 2025 like-kind exchange or … |

## s179

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| s179#1.1 | out of scope | asset.screened | p946 pp. 17-18; i4562 p. 5. Checked per property: a trade-in, like-kind exchange, involuntary conversion or purchase from a related person is asset.got_other ('Did you get it with a trade-in, in an exchange, ... from a relative or a business you control'), … |
| s179#1.2 | out of scope |  | p946 pp. 18-19, Joint return after filing separate returns: 'If you and your spouse elect to amend your separate returns by filing a joint return after the due date'. That joint return replaces separate returns already filed, an amended return (Form 1040-X); … |
| s179#1.3 | out of scope | sc.screened | i4562 p. 5; p946 p. 19, active conduct means meaningful participation. s179.income_sc sums person.income179, i.e. Schedule C line 31 before section 179 only. Every Schedule C is asked sc.passive (line G: 'did you yourself do all or most of the work of this … |
| s179#1.4 | out of scope | sc.ho_both_limits | p946 p. 19, the eight steps 'if you have a taxable income limit for some other deduction'. The steps are needed only when each limit depends on the other. i4562 p. 5, Line 11: business income is 'computed without regard to any section 179 expense deduction, … |

## sc

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| sc#1.1 | out of scope | sc.ho_screened | p587 p. 3; i1040sc p. 13. The principal case of failing the principal-place-of-business test is a business with another fixed location. sc.ho_other asks 'some of the income of this business was earned at another place of business' and refuses through … |
| sc#1.2 | covered | sc.line23 | i1040sc p. 9, Line 23, 'Do not deduct ... Estate and gift taxes. Taxes assessed to pay for improvements, such as paving and sewers.' The interview help of sc.line23 says 'Leave out ... charges for improvements such as paving or sewers' (the claim read only … |
| sc#1.3 | out of scope | person.mw_business_if_1099 | i1040sc p. 6, Medicaid waiver payments (Notice 2014-7). Medicaid waiver payments are asked of every return (scope.medicaid_waiver, 'Medicaid pay for caring for someone who lives in your home'); the amount on Form 1099-MISC or 1099-NEC is person.mw_1099, and … |
| sc#1.4 | presentation |  | i1040sc p. 5, Line 1: 'If the total amounts that were reported in box 1 of Forms 1099-NEC are more than the total you are reporting on line 1, attach a statement explaining the difference.' The statement is filing information and changes no amount. As the … |

## scveh

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| scveh#1.1 | out of scope | BUG-0780 | i1040sc p. 8, Line 20a, 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; p946 p. 59; p463 (2025), Inclusion Amounts, the amount applies if the vehicle's FMV when the lease began was more … |
| scveh#1.2 | out of scope | sc.screened | i1040sc p. 6, Capitalizing costs; 'A small business taxpayer ... is not required to capitalize certain expenses to inventory or other property.' sc.method_other (line F) asks whether the business has 'a tax shelter; or receipts averaging more than $31 million … |
| scveh#1.3 | presentation |  | i4562 p. 16, Part V Section B lines 30-36; i1040sc p. 7. Lines 30-36 (off-duty availability, other vehicle available, written evidence) are reporting entries that change no amount. The facts that change an amount are asked: miles on scveh.miles_business, … |

## se

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| se#1.1 | out of scope | scope.other_income | i1040sse p. 2, U.S. Citizens Employed by Foreign Governments. Pay from a foreign government or international organization comes without a Form W-2. Every return is asked scope.pay_no_w2 ('Wages, tips or strike benefits that are not on a W-2') and then … |
| se#1.2 | out of scope | scope.other_income | i1040sse p. 2, Chapter 11 Bankruptcy Cases. Every return is asked scope.chapter11 ('At any time in 2025, were you (or, on a joint return, your spouse) in a chapter 11 bankruptcy case?', interview tick 'In a chapter 11 bankruptcy case at some time in 2025'); a … |
| se#1.3 | out of scope | person.se_screened | i1040sse p. 2, Form 4029 and the social security agreements. person.se_screen, asked of each person with a business, names 'an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029)' and 'earnings exempt under a social … |

## u1250

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| u1250#1.1 | out of scope | sales.special | i1040sd p. 13, Line 10 of the Unrecaptured Section 1250 Gain Worksheet. Every sale is asked sales.special, whose interview list includes 'your share of a partnership, an S corporation or a trust that owns collectibles or depreciated buildings'; a Yes refuses … |

## Pending bugs filed by this fork

| id | severity | title |
|---|---|---|
| BUG-0775 | medium | rental: a home converted to a rental in 2025 deducts the whole year's expenses, because main-home days are left out of the expense division |
| BUG-0776 | low | rental cost questions do not exclude capitalized legal fees and capital purchases |
| BUG-0777 | low | rental mortgage interest is not allocated by the use of the loan proceeds |
| BUG-0778 | low | rental: a Worksheet 5-1 carryover from an earlier year is neither asked nor refused |
| BUG-0779 | low | rental: Form 8582 exceptions 3 to 6 (incidental rentals, business-hours use) and dealer property are not screened |
| BUG-0780 | low | sc.special names the lease inclusion amount only by its official term |
| BUG-0781 | low | Rental at-risk question reaches only nonrecourse loans from non-lenders |
| BUG-0782 | low | Part-of-property refusal misses a part the filer uses otherwise or lived in earlier in 2025 |
| BUG-0783 | low | Rental 10% ownership test: no 'at any time' in 2025, and not asked for the year a held-back loss arose |
| BUG-0784 | low | Rental services question can be answered No when a manager provides the services |
| BUG-0785 | low | Held-back rental loss question omits the spouse's separate earlier return and a grouped activity |
| BUG-0786 | low | rental expenses ask only what was paid in 2025; an accrual-method landlord's expenses incurred for 2025 are not asked |
| BUG-0787 | low | rental insurance: the 2025 part of a premium prepaid in an earlier year is excluded by the gate and the amount question |
| BUG-0788 | low | rental citations name Line 8, Line 9 (and Line 15) instructions that i1040se does not have |
| BUG-0789 | medium | Rental expenses a tenant paid are counted in rent but not asked as expenses |
| BUG-0790 | medium | asset.listed: the redraft prompt narrows listed entertainment property to camera and recording "equipment", so a boat or communication equipment used 50% or less is depreciated instead of refused |
| BUG-0791 | low | asset.industry asks about the business, so item-defined property (reuse and recycling equipment, a gas gathering line, transmission property, a race track) owned outside the named businesses skips the asset.industry_item refusal |
| BUG-0792 | low | The earlier-year low-use question does not prorate the business use of the year a vehicle was converted from personal use |
