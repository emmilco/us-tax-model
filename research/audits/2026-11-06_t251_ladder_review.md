# T-251 question ladder: independent soundness review

Reviewer: claude-opus-5-5, judgment class (independent soundness review). Branch head 204cc77.
Subject: `interview/topics-2025.yaml` (topics, `covers`, `parents`, `joint`, `screens`, `gates`, `uncovered`),
read against `forms/2025/*.yaml`, `forms/ny/2025/*.yaml`, `engine/src/ladder.ts`, `engine/src/interview.ts`
(`pendingOf`, gates) and the archived sources under `sources/2025/` and `sources/ny/2025/`.

Severity: **high** = a truthful "no" to the question as worded yields a wrong return value or a missed refusal;
**medium** = a plausible misreading has that effect, or the rule rests on a source not archived here;
**low** = wording or clarity. Page numbers are the printed page of the archived extract.
Where a finding rests on a rule whose source is not archived, it says so ("not archived").

## High

### L-1 (high) `installment_sale` is reachable only through a 2025 sale
- Topic/input: `installment_sale` (parent `securities_sales`, which asks "In 2025, did you ... sell or exchange");
  feeds `sd_screen` (`sd.other_forms`, Form 6252) and `s2_other_screen` (Schedule 2 lines 14 and 15).
- Scenario: a filer sold land in 2021 on a 10-year note and receives a 2025 payment. They truthfully answer no to
  `securities_sales` (no 2025 sale), so `installment_sale` is ruled out, `sd.other_forms` and `s2.other` are implied
  false, and the 2025 installment gain (Form 6252) and any section 453A interest are omitted.
- Source: i1040sd p. 5–6, Installment Sales, "you will receive a payment in a tax year after the year of sale, you must
  generally report the sale on the installment method"; i1040gi p. 113, Schedule 2 line 15, interest on the deferred
  tax under section 453A(c) (charged for each year the obligation is outstanding).
- Fix: make `installment_sale` top-level (less_common) worded "Did you sell property in 2025 or any earlier year for
  which you receive, or will receive, a payment after the year of sale?", or add it to `securities_sales`' prompt
  ("... or receive in 2025 a payment for property sold in an earlier year").

### L-2 (high) `form_2439` names only mutual funds and ETFs; REITs also issue Form 2439
- Topic/input: `form_2439` → `sd_screen` (Form 2439 gain), `s3_line14_screen` (Schedule 3 line 13a).
- Scenario: a REIT shareholder receives Form 2439 from the REIT and truthfully answers no to "Did a mutual fund or ETF
  send you a Form 2439". The undistributed gain (Schedule D line 11) and the tax credit (Schedule 3 line 13a) are lost.
- Source: i1040sd p. 6, Undistributed Capital Gains, "your share of the undistributed long-term capital gains of the
  regulated investment company (including a mutual fund) or real estate investment trust".
- Fix: "Did a fund, ETF or real estate investment trust (REIT) send you a Form 2439?" (or simply "Did you receive a Form
  2439?"). The `why` line ("only such funds issue it") is wrong as written.

### L-3 (high) `securities_sales` asks about sales and exchanges; Form 8949 also reports losses that are not sales
- Topic/input: `securities_sales` → `$sales: []`.
- Scenario: (a) stock that became worthless in 2025; (b) a personal loan to a friend that became uncollectible
  (nonbusiness bad debt); (c) property taken by condemnation. Each filer truthfully says they sold or exchanged
  nothing; the roster is implied empty and the loss or gain is omitted.
- Source: i8949 p. 1, "Use Form 8949 to report ... Nonbusiness bad debts. Worthlessness of a security. Gains from
  involuntary conversions (other than from casualty or theft) of capital assets"; p550 p. 54, Worthless Securities,
  "treated as though they were sold on the last day of the tax year".
- Fix: add to the prompt "... or have stock or other securities become worthless, or a loan you made become
  uncollectible". Condemnation can go in help.

### L-4 (high) `retirement_distributions` asks about payments; Form 1099-R also reports amounts not paid out
- Topic/input: `retirement_distributions` → `$retirement: []`, `person.ira_dist`, NY pension inputs.
- Scenario: an employee whose employer made designated Roth matching or nonelective contributions receives a Form
  1099-R for the taxable allocation but received no payment; they truthfully answer no, and taxable income is omitted.
  The same holds for a surrendered cash-value life insurance policy or charitable gift annuity (not "a pension, an
  annuity, a retirement plan or an IRA" to a lay reader), both reported on Form 1099-R.
- Source: i1099r p. 1, "Designated Roth nonelective contributions and designated Roth matching contributions must be
  reported on Form 1099-R for the year in which the contributions are allocated"; same page, Form 1099-R is filed for
  distributions from "insurance contracts ... charitable gift annuities".
- Fix: add "or did you receive any Form 1099-R" to the prompt (the `why` already treats the roster as one entry per
  Form 1099-R).

### L-5 (high) `partnership_audit` hangs under a 2025-only partnership question
- Topic/input: `partnership_audit` (parent `rental_passthrough`, "In 2025, did you have ... a share of a partnership")
  → `scope.credits`, `scope.other_line16` (Form 8978).
- Scenario: a filer who was a partner in 2021 and sold out in 2023 receives Form 8986 in 2025. They answer yes to
  `business` ("any earlier year") but truthfully no to `rental_passthrough`, so `partnership_audit` is ruled out and
  both screens are implied false: missed refusal.
- Source: i1040gi p. 116, Schedule 3 line 6l, Form 8978 "relating to partner's audit liability under section 6226";
  p. 34, line 16, "Tax from Form 8978". The reviewed-year partner rule is section 6226(b) (not archived).
- Fix: change `parents` to `business`.

### L-6 (high) `fractional_gift` hangs under a 2025 gift question; the recapture comes years later
- Topic/input: `fractional_gift` (parent `home_charity`: 2025 gifts or a carryover) → `s2_other_screen`
  (Schedule 2 line 17g; Schedule 1 line 8z recapture).
- Scenario: a filer gave a museum a 25% interest in a painting in 2015 and had not given the rest when the 10-year
  period ran out in 2025. No gifts in 2025 and no carryover: `home_charity` is truthfully no, `fractional_gift` is ruled out, `s2.other` is implied false, and the recapture, its interest and the
  10% additional tax are omitted.
- Source: p526 p. 13, Recapture of deduction (10 years after the initial contribution); i1040gi p. 92, line 8z,
  "Recapture of a charitable contribution deduction relating to the contribution of a fractional interest";
  p. 113–114, Schedule 2 line 17g.
- Fix: make it top-level (less_common), "Have you ever given a charity a fractional interest in art or other tangible
  property?", or remove the parent.

### L-7 (high) `foreign_assets` omits signature authority
- Topic/input: `foreign_assets` → (child) `foreign_accounts` → `sb.line7a`, `sb.fbar_required`, `sb.form8938`.
- Scenario: an employee with signature authority over her employer's account in London, with no assets abroad of her
  own, truthfully answers no to "did you have money, an account, investments or other assets outside the United
  States". `sb.line7a` is implied false; Schedule B line 7a must be "Yes" and the FBAR question follows.
- Source: i1040sb p. 2–3, Line 7a—Question 1, "Check the 'Yes' box if at any time during 2025 you had a financial
  interest in or signature authority over a financial account located in a foreign country ... even if you aren't
  required to file FinCEN Form 114."
- Fix: add "or signature authority over a foreign account (for example one held by your employer)" to the parent, as
  the child already has.

### L-8 (high) `foreign_assets` omits the grantor of an existing foreign trust
- Topic/input: `foreign_assets` → `foreign_trust` → `sb.line8`.
- Scenario: a filer created a foreign trust in 2015 and made no transfer and received nothing in 2025. "Receive
  anything from, or transfer anything to, a foreign trust" during 2025 is truthfully no; `sb.line8` is implied false.
- Source: i1040sb p. 1, General Instructions ("were a grantor of, or transferor to, a foreign trust"); p. 3, Line 8,
  "If you were the grantor of, or transferor to, a foreign trust that existed during 2025"; `sb.line8` label.
- Fix: parent wording "... or have you ever created, or transferred anything to, a foreign trust".

### L-9 (high) `retirement_accounts` misses current-employer and inherited employer plans (missed RMD)
- Topic/input: `retirement_accounts` ("an IRA ... or money in a retirement plan from a former employer") → `missed_rmd`
  → `x_other_screen` (`person.x_other`, Form 5329 Part IX).
- Scenarios: (a) a 5% owner aged 74 still working, who must take RMDs from the current employer's plan; (b) any
  employee over 73 whose plan requires RMDs while employed; (c) a beneficiary of a parent's 401(k) (not "a former
  employer" of the filer) with annual RMDs. Each truthfully answers no; `missed_rmd` is ruled out and a missed RMD's
  25%/10% tax is never asked.
- Source: p575 p. 32, Required beginning date and 5% owners ("your plan may require you to begin to receive
  distributions ... even if you haven't retired"); i5329 p. 9, Part IX, "your qualified retirement plan, including an
  IRA or an eligible section 457 deferred compensation plan".
- Fix: parent "Do you (or your spouse) have money in an IRA or in any employer retirement plan, including an account
  you inherited?" (present-tense issue: L-40).

### L-10 (high) `nol` can only be reached through a 2025 casualty or a business
- Topic/input: `nol` (parents `business`, `casualty`) → `scope.schedule1` (Schedule 1 line 8a), `line8_other_screen`.
- Scenario: a filer with no business ever whose home was destroyed in a 2023 federally declared disaster has an NOL
  carried into 2025. `casualty` asks "In 2025, did you have property damaged"; truthfully no, so `nol` is ruled out and
  the NOL deduction refusal is missed. Also: Armed Forces moving expenses (military) and an ordinary section 1244
  stock loss (L-16) can create NOLs.
- Source: i1040gi p. 91, line 8a, NOL "from an earlier year" (Form 172 instructions not archived); the topic's own
  `why` names casualty losses as a source.
- Fix: make `nol` top-level (less_common): "Do you have a net operating loss carried into 2025 from an earlier year?"
  It is already one plain fact.

### L-11 (high) `railroad` hangs under wages; a CT-2 employee representative has no Form W-2
- Topic/input: `railroad` (parent `wages`) → `person.rrta`, `f8959_screen`.
- Scenario: an employee representative of a railway labor organization reports RRTA compensation on Form CT-2, not on a
  W-2. Answering no to "work as an employee ... or receive any Form W-2" is plausible and arguably truthful; `railroad`
  is ruled out, `person.rrta` and `f8959.unsupported` are implied false, and Additional Medicare Tax on RRTA
  compensation (Form 8959 Part III) is omitted.
- Source: i8959 p. 3, Line 14, RRTA compensation for an employee "is reported on Form W-2, box 14"; "An employee
  representative ... should include the total compensation ... as reported on line 2 of Form CT-2".
- Fix: `parents: [wages, other_work_pay]` (the CT-2 representative is "paid for work in a way not shown on a W-2"), or
  top-level less_common.

### L-12 (high) `employer_other_pay` asks about payments; 409A and 457A taxes apply to amounts included, not paid
- Topic/input: `employer_other_pay` → `s2_other_screen` (Schedule 2 lines 17h, 17i), `line8_other_screen`.
- Scenario: an employee whose NQDC plan fails section 409A has the deferred amount included in income (W-2 box 12 code
  Z) though nothing was paid out. "Did a current or former employer pay you in 2025 from a nonqualified deferred
  compensation plan" is truthfully no; `s2.other` is implied false; the 20% tax and interest are omitted. Same for
  457A compensation includible in 2025.
- Source: i1040gi p. 114, line 17h, "income ... shown in box 12 of Form W-2 with code Z, or in box 15 of Form
  1099-MISC. The tax is 20% of the amount required to be included in income"; line 17i.
- Fix: "Did you have income in 2025 from a nonqualified deferred compensation plan or non-government 457 plan (paid or
  not), ..." or ask the W-2 fact "Does a Form W-2 show box 12 code K, M, N or Z?". The 1099-MISC/NEC (director)
  versions reach `s2.other` through `business` yes, so only the employee path is open.

### L-13 (high) `cfc_pfic` is asked in the present tense; a 2025 disposition is missed
- Topic/input: `cfc_pfic` ("Do you own ...") → `scope.other_line16` (Form 8621, line 16 "1291TAX").
- Scenario: a filer sold all shares of a foreign mutual fund in March 2025. `foreign_shares` ("Did you own") is yes;
  `cfc_pfic` ("Do you own", answered in 2026) is truthfully no; the excess-distribution tax and Form 8621 are not
  refused.
- Source: i1040gi p. 34, line 16, "Any tax from Form 8621, line 16e, relating to a section 1291 fund"; p. 114,
  line 17p, interest "relating to distributions from, and dispositions of, stock of a section 1291 fund".
- Fix: "At any time in 2025, did you own (or did you sell) ...".

### L-14 (high) Strike and lockout benefits (Form 1040 line 1h) reach no question
- Topic/input: `scope.other_income`, clause "other earned income (Form 1040 lines 1b to 1d and 1f to 1h)"; the
  line 1h residual.
- Scenario: a union member on strike received strike benefits. No topic whose yes implies `scope.other_income` names
  them (`other_work_pay` is pay for work; `other_income` has no `implies_yes`), so the screen is implied false and the
  benefits land, if anywhere, on the line 8z roster instead of line 1h (earned income for EIC and the dependent
  standard deduction).
- Source: i1040gi p. 24, Line 1h, "The following types of income must be included in the total on line 1h. Strike or
  lockout benefits (other than bona fide gifts)"; p525 p. 36, Strike and lockout benefits.
- Fix: add strike or lockout benefits to `other_work_pay`'s prompt (it already implies the screen). The rest of the
  line 1h list is mapped: excess elective deferrals (`workplace_plan` → `person.sav_excess`), disability pensions
  (`disability_pension`), corrective distributions on Form 1099-R (`retirement_distributions`; whether the roster
  routes codes 8/P to line 1h was not checked).

### L-15 (high) `ftc_1116` leaves out the election's passive-income condition
- Topic/input: `ftc_1116` → `scope.credits`.
- Scenario: a filer worked two weeks in Germany for a U.S. employer (foreign-source wages, no foreign tax) and has $40 of
  foreign tax on a 1099-DIV. All foreign tax is on Forms 1099 and under $300, so `ftc_1116` is truthfully no; but the
  election requires all foreign-source gross income to be passive, so Form 1116 is required and the credit is
  computed without the limitation.
- Source: i1116 p. 1, Election To Claim the Foreign Tax Credit Without Filing Form 1116, "All of your foreign source
  gross income was 'passive category income'".
- Fix: add a clause: "... or did you have income from work or a business outside the United States, or a foreign
  pension?". (Amounts are capped at $300/$600, so the error is small; the refusal is still missed.)

### L-16 (high) Section 1244 stock losses (Form 4797) are not reached by `business`
- Topic/input: `business` → `business_property_sale` (`scope.schedule1`, Schedule 1 line 4) and `sd_screen`
  (`sd.other_forms`, Form 4797).
- Scenario: a founder of a C corporation whose small business stock became worthless in 2025 has an ordinary loss on
  Form 4797. `business` names S corporations and partnerships, not C corporation stock; the founder truthfully answers
  no, and both screens are implied false.
- Source: i1040sd p. 6, Small Business (Section 1244) Stock, "Report an ordinary loss from the sale, exchange, or
  worthlessness of small business (section 1244) stock on Form 4797".
- Fix: fold into L-3's wording ("... including stock in a small corporation you helped found") with a child "Was it
  section 1244 small business stock?" implying both screens, or add to `business`.

## Medium

### L-17 (medium) Child questions and some top-level questions omit the spouse
- Topics: nearly every child (`wage_tips`, `workplace_plan`, `railroad`, `employer_other_pay`, `medicaid_care`,
  `performing_fee`, `direct_bonds`, `us_obligations`, `form_2439`, `govt_bond_funds`, `lump_sum_1936`,
  `disability_pension`, `section_1256`, `installment_sale`, `keogh`, `business_property_sale`, `business_carryover`,
  `foreign_accounts`, `foreign_trust`, `ftc_1116`, `recovery`, `clergy`, `casualty_gain`, `missed_rmd`, ...) and the
  top-level `dependents_care` ("apply to you") and `education` ("did you pay interest on a student loan").
- Scenario: on a joint return the parent was yes because of the spouse; the child asks "Did you ...". A filer who reads
  "you" literally answers no: e.g. the spouse's 401(k) → `w2.box12_any` false on the spouse's W-2 (Form 8880 line 2
  understated); spouse's box 10 benefits → `f2441.benefits` false; spouse's student loan interest → `sli.interest` 0.
- Source: the covered inputs are per person or per return (forms/2025/person.yaml, w2.yaml, f2441.yaml, sli.yaml);
  no wording convention says "you" includes the spouse (interview/README.md).
- Fix: "you (or your spouse)" in every child prompt on a joint return, or a stated convention shown once.

### L-18 (medium) `casualty` is 2025-only; theft losses are taken when discovered and gains when reimbursed
- Topic/input: `casualty` → `casualty_gain` (`scope.schedule1`), `sd_screen` (Form 4684), `nol`.
- Scenario: (a) an investment fraud from 2022 discovered in 2025; (b) insurance paid in 2025 for a 2024 fire, exceeding
  basis (a 2025 casualty gain). "In 2025, did you have property damaged, destroyed or stolen" is truthfully no.
- Source: the timing rules are in i4684 and Pub. 547 (not archived; section 165(e) and Reg. 1.165-1(d)).
- Fix: "... or in 2025, did you discover a theft, or receive insurance or other payment for property damaged or stolen
  in an earlier year?"

### L-19 (medium) `recovery` sits under `other_income`; refunds of deducted amounts are not perceived as income
- Topic/input: `recovery` → `scope.schedule1` (named clause). Parent `other_income` mentions recoveries only in help.
- Scenario: a filer who itemized in 2024 gets a 2025 refund of property tax or a medical reimbursement and answers no to
  "gambling winnings, a prize ... or any other taxable income". `recovery` is ruled out; missed refusal.
- Source: i1040gi p. 92, line 8z, first example "Reimbursements or other amounts received for items deducted in an
  earlier year"; p. 89, exception 2 (refunds "other than an income tax refund, such as a general sales tax or real
  property tax refund").
- Fix: make `recovery` top-level (it is one plain fact), or put it under a "Did you itemize deductions on an earlier
  return?" parent.

### L-20 (medium) `business_carryover` asks people to remember a QBI loss carryforward they rarely know about
- Topic/input: `business_carryover` → `qbi.carryforward` 0, `s179.line10` 0, `qbi_screen`.
- Scenario: a filer with a 2024 Schedule C loss used it against wages and does not know Form 8995 line 16 carried a
  qualified business loss into 2025. "Did a business leave you a loss ... carried into 2025" gets a sincere no;
  `qbi.carryforward` 0 overstates the 2025 QBI deduction.
- Source: i8995 p. 4–5, Line 3 and Line 16 (cited in `qbi.carryforward`).
- Fix: treat `qbi.carryforward` and `s179.line10` like `sd.carryover` (kind `prior_year`, asked from the 2024 return)
  whenever `business` is yes; keep `business_carryover` only for suspended passive/REIT/PTP losses in `qbi_screen`.

### L-21 (medium) `govt_bond_funds` says "bonds"; Treasury money market funds are the common case
- Topic/input: `govt_bond_funds` → `ny_us_obligation` (`ny_it201.ask.us_obligation_interest`).
- Scenario: a New Yorker holds a Treasury money market fund (bills and repos) and answers no to "a fund that invests in
  U.S. government bonds". The NY subtraction for qualifying fund dividends is lost.
- Source: ny_it201i p. 9, Line 28, "Dividends you received from a regulated investment company (mutual fund) that invests
  in obligations of the U.S. government and meet the 50% asset requirement each quarter qualify".
- Fix: "a fund (including a money market fund) that invests in U.S. Treasury or other U.S. government obligations".

### L-22 (medium) `us_obligations` names only Treasuries and savings bonds
- Topic/input: `us_obligations` → `ny_us_obligation`.
- Scenario: a filer holds bonds of a federal agency whose interest is exempt from state tax; "interest on U.S. Treasury
  bills, notes or bonds, or on U.S. savings bonds" is truthfully no; the NY subtraction is lost.
- Source: ny_it201i p. 9, Line 28, "interest income from U.S. government bonds or other U.S. government obligations".
  Which agency obligations qualify is not in the archived text.
- Fix: "... or other U.S. government obligations (some federal agency bonds)".

### L-23 (medium) `home_charity`: co-op owners pay their share of taxes and interest through maintenance
- Topic/input: `home_charity` → `sa.line5b`, `sa.line8a`, ...
- Scenario: a New York City co-op owner without a personal mortgage pays maintenance and receives the co-op's statement
  of their share of real estate tax and mortgage interest; they answer no to "pay home mortgage interest, real estate
  taxes". Deductions are lost if they itemize.
- Source: i1040sca p. 7, "A home can be a house, condominium, cooperative"; the tenant-stockholder rule (section 216)
  is not in the archived text.
- Fix: help "Co-op owners: count your share of the co-op's real estate taxes and mortgage interest."

### L-24 (medium) "own a share of ... an estate or a trust" misses beneficiaries
- Topics: `business`, `rental_passthrough`.
- Scenario: the beneficiary of a family trust receiving a Schedule K-1 (Form 1041) does not "own a share" of the trust
  and answers no. `scope.schedule1` (Schedule E/K-1, line 24k), `qbi_screen`, `s2_other` (line 17l) and the NY
  accumulation credit are all implied false.
- Source: i1040gi p. 100, line 24k, "Schedule K-1 (Form 1041)"; i1041sk1 (beneficiary's K-1).
- Fix: "... or were a beneficiary of an estate or trust (Schedule K-1 from Form 1041)".

### L-25 (medium) `other_income` names digital assets "as pay or rewards"; line 8v also covers forks and mining
- Topic/input: `other_income` → `line8_other_screen` (line 8v).
- Scenario: a filer received tokens from a hard fork or airdrop; "pay or rewards" is truthfully no.
- Source: i1040gi p. 92, Line 8v, "income from forks, staking, or mining".
- Fix: "digital assets received as pay, rewards, staking, mining, a fork or an airdrop".

### L-26 (medium) `household_employer` says "work in your home"; household work includes work around it
- Topic/input: `household_employer` → `s2_other_screen` (Schedule 2 line 9).
- Scenario: a filer pays a yard worker $3,000 cash; "work in your home" is read as no.
- Source: i1040gi p. 113, Line 9, "Household work includes work done in or around your home by babysitters, nannies,
  health aides, housekeepers, yard workers, and similar domestic workers".
- Fix: "in or around your home — a nanny, housekeeper, caregiver, yard worker or similar".

### L-27 (medium) Forms 1099-K for personal items sold at a loss, or in error, reach no question
- Topic/input: none; `securities_sales` help tells the filer such sales "do not count".
- Scenario: a filer receives a Form 1099-K for a couch sold at a loss. 2025 instructions require the amount in the entry
  space at the top of Schedule 1; the ladder asks nothing and `scope.schedule1` is implied false. No tax changes, but the
  filing omits a required entry and invites a matching notice.
- Source: i1040gi p. 88, Form(s) 1099-K, "for personal items that you sold at a loss ... enter the amount ... in the
  entry space at the top of Schedule 1".
- Fix: owner decision: a question "Did you receive a Form 1099-K?" (leading to a refusal or a supported entry), or
  accept as a known gap.

### L-28 (medium) Schedule 3 line 13z enumerated: one item has no parent in `s3_line14_screen`
- Topic/input: `s3_line14_screen` residual "line 13z".
- Finding: the instructions list three 13z items: the section 960(c) excess-limitation credit (reached by
  `foreign_shares`), Form 8689 U.S. Virgin Islands tax (needs USVI-source income; `abroad` is not in `when_no`), and
  the Form 1062 farmland installment election (farmland used as a farm for the prior 10 years, so `business`).
- Source: i1040gi p. 117, Line 13z.
- Fix: add `abroad` to `s3_line14_screen.when_no`; replace the residual with the mapping. USVI-source investment income
  of a non-resident (e.g. interest from a USVI bank) remains uncovered; accept or name it in `abroad`'s help.

### L-29 (medium) Section 965 items: S-corporation owners and post-disposition installments
- Topic/input: `foreign_shares` ("directly or through a partnership or trust") → `cfc_pfic`, `s2_other` (line 20),
  `s3_line14` (13d); `scope.other_line16` (line 16 box 3 "965INC").
- Scenario: (a) an S-corporation shareholder with a deferred 965(i) liability and a 2025 triggering event: the S
  corporation is not named, so `foreign_shares` is truthfully no and the line 16 tax is missed (no line-16 leaf maps
  965INC at all); (b) a filer paying the final 965(h) installment whose CFC shares were sold before 2025.
- Source: i1040gi p. 36, line 16, "Triggering event under section 965(i) ... enter '965INC'"; f1040s2 line 20,
  "Section 965 net tax liability installment from Form 965-A"; i1040gi p. 117, line 13d.
- Fix: add "S corporation" to `foreign_shares`; add a less_common question "Do you have a section 965 tax liability
  being paid in installments or deferred?" implying `scope.other_line16` and covering lines 20/13d.

### L-30 (medium) `clean_vehicle` is 2025-only; Schedule 2 line 1y recaptures an earlier refueling-property credit
- Topic/input: `clean_vehicle` → `s2_other_screen`.
- Finding: the line 1y list is enumerable: (1) recapture of the Form 8911 refueling property credit ("ARPCR"), (2)–(5)
  Form 4255/8933 amounts (business credits, reached by `business`). Item (1) concerns property placed in service in an
  earlier year; "In 2025, did you buy ... or install a vehicle charger" does not reach it.
- Source: i1040gi p. 111, Line 1y, items 1–5. The recapture conditions are in i8911 (not archived).
- Fix: widen to "since 2022"; replace the 1y residual with this mapping.

### L-31 (medium) `tax_credit_bonds` sits under `interest`; such bonds may pay no interest
- Topic/input: `tax_credit_bonds` (via `direct_bonds` under `interest`) → `scope.credits`.
- Scenario: a holder of a zero-coupon tax credit bond receives no interest and answers `interest` no. The child itself
  says "bonds that pay a tax credit instead of ... interest", which contradicts its placement.
- Source: i1040gi p. 116, line 6k, credit to holders of tax credit bonds (Form 8912, not archived).
- Fix: parent `direct_bonds` only after making `direct_bonds` top-level, or move to less_common.

### L-32 (medium) `child_investment_income` sits under `dependents_care`
- Topic/input: `child_investment_income` → `scope.other_line16` (Form 8814).
- Scenario: a remarried custodial parent filing jointly who released the dependency claim (Form 8332) to the other
  parent has no dependent and no HOH status, but is the parent who may elect Form 8814; the topic is ruled out.
- Source: i8814 is not archived; i1040gi p. 34 lists Form 8814 without a dependency condition. Inferred.
- Fix: make it top-level less_common, or add `young_filer`-style parent "Do you have a child under 24?".

### L-33 (medium) `ira_contributions` help invites self-employed SEP contributions
- Topic/input: `ira_contributions` → `person.ira_trad` (yes path).
- Scenario: "Count contributions you made yourself, including to a SEP IRA you fund yourself" — a sole proprietor
  funding their own SEP (an employer contribution, Schedule 1 line 16, supported via `person.sep_*`) counts it as a
  traditional IRA contribution.
- Source: i1040gi p. 93–94, Line 16 (SEP) vs line 20 (IRA deduction).
- Fix: "Count regular IRA contributions you made yourself, even if made to a SEP IRA account; do not count SEP or
  SIMPLE contributions made as an employer, including for your own business."

### L-34 (medium) "Foreign corporation reporting" in `sb.unsupported` is reached only through share ownership
- Topic/input: `sb_screen` (`foreign_shares` covers "foreign corporation reporting").
- Scenario: an officer or director of a foreign corporation with no shares (Form 5471 filer) answers `foreign_assets`
  no.
- Source: i1040sb p. 2, Part II tip, "You may have to file Form 5471 if, in 2025, you were an officer or director of a
  foreign corporation".
- Fix: add "or were an officer or director of a foreign company" to `foreign_shares` and `foreign_assets`, if that is
  what the `sb.unsupported` clause means (its label does not say).

## Low

### L-35 (low) Residuals the instructions close
- Schedule 1 line 24z: i1040gi p. 100, "Leave line 24z blank." Schedule 3 line 6z: p. 116, "Leave line 6z blank."
  Both residuals can be marked empty with the citation.
- Schedule 2 line 17z: p. 114 lists PWA penalties from Form 4255 (business credits; `business`) and the negative Form
  8978 adjustment (`business`, see L-5). Line 1y: L-30. Line 13z: L-28. Line 1h: L-14. Line 16 box 3: p. 34–36
  lists 8814, 4972, 962, ECR, 8621 (1291TAX), 8978, 965INC; all mapped except 965INC (L-29).
- Schedule B "other special treatment": i1040sb p. 1–2 lists seller-financed interest, accrued interest, OID, bond
  premium, savings bond exclusion, nominee; all mapped. Interest on frozen deposits (i1040gi p. 24) is unmapped; rare.
- Fix: replace `residual` entries with these mappings and citations.

### L-36 (low) Questions that still require scanning a list, a complement, or applying rules
- Long lists: `other_income` (eleven items plus "any other taxable income not asked about in the other questions",
  a complement), `business`, `home_energy`, `securities_sales`, `education` (four facts), `dependents_care` (three).
- Rule application, not a plain fact: `form_8615` ("Must you file"), `cfc_pfic` (PFIC status of a foreign company),
  `nonresident_alien` (Pub. 519 tests), `schedule_r` ("Do you want to claim", eligibility unknown to the filer),
  `keogh` ("Keogh" jargon).
- Single-filer wording: `citizenship` "was either of you".
- Fix: split `other_income`'s complement into named children; reword the rule questions as facts where possible.

### L-37 (low) `workplace_plan` reads as an exhaustive list
- "a 401(k), 403(b), 457(b), SIMPLE, SARSEP or the Thrift Savings Plan" omits 501(c)(18)(D) plans (its own child) and
  after-tax voluntary contributions to a pension plan (`person.sav_voluntary`; f8880 p. 2, Line 2). Fix: "for example".

### L-38 (low) Fee-basis officials are reached only through `wages`
- `performing_fee` (Schedule 1 line 12, i1040gi p. 93) is a child of `wages`; a fee-basis official paid fees without a
  W-2 may answer `wages` no. Whether such officials get Forms W-2 is not in the archived text. Fix: add
  `other_work_pay` as a parent.

### L-39 (low) Misreadings with help-text fixes
- `dividends`: money market fund earnings are dividends (1099-DIV) though many call them interest; name them in help.
- `foreign_tax`: fund holders with 1099-DIV box 7 amounts often do not know foreign tax was withheld; the help names box
  7, which suffices.

### L-40 (low) Tense
- `retirement_accounts` and `savings_accounts` ("Do you have") are answered in 2026 about 2025 facts: an IRA with an
  earlier excess closed in early 2026 reads as no. Use "At any time in 2025 or since".
- `wages` "receive any Form W-2" does not say "for 2025"; the ambiguity errs toward yes, so harmless.

### L-41 (low) MCTMT gate: verified, with one open point
- Verified: threshold $50,000 per individual ("exceed $50,000", "calculated on an individual basis, even if you file a
  joint income tax return", ny_it201i p. 15); `at_most: 5000000` cents; NESE is at most Schedule SE line 2 when no
  partnership or farm earnings (line 2 is before the 92.35% factor, so the gate is conservative); `pendingOf` applies it
  only when every `person.se_line2` is known and the `when_no` topics are no, recomputes each call, and throws if the
  implied value changes the line.
- Open: the base is "calculated separately for each source" (p. 15–16). If a loss from one Schedule C does not reduce
  another source's zone base, a filer with $70,000 profit and $30,000 loss (line 2 $40,000) passes the gate wrongly.
  The archived text does not say; check with the MTA-6 instructions or the owner.

### L-42 (low) Rare edges
- Schedule 3 line 6i (Form 8834, vehicles placed in service before 2007, passive carryforward) maps only to
  `clean_vehicle_credit` (a 2025 purchase); i1040gi p. 116.
- `military` "called to active duty since 2022": the reservist repayment window runs two years after active duty ends
  (i8606 p. 9; the window rule is not quoted there). A call before 2022 ending in 2023 is missed if the filer left the
  reserves.
- `adoption`: an adoption still pending, with expenses paid by the employer, may read as no; add "or are adopting".

### L-43 (low) Uncovered inputs (item 5)
- No input is wrongly classed. Candidates a fact or computed value could rule out: `ny_it201.ask.real_property_credit`
  (household gross income limit; a computed gate like MCTMT); `ny_it201.ask.other_credits` (claim-of-right part via
  `repayment`); `young_filer` and `elderly_disabled` duplicate facts already asked (`person.born_before_2001`,
  `person.age65`) and could be derived for their age parts.
- `sd.carryover` is `prior_year` while `qbi.carryforward`/`s179.line10` are covered by a memory question: see L-20.

## All-of rules (item 2), summary
- `f8959_screen`: parent set sound; fee-basis SE income (`performing_fee`) is absent but refused through
  `scope.schedule1`. Railroad: L-11.
- `qbi_screen`: sound given `sc` handles its own screens (Schedule C passive and Medicaid items are refused in
  `forms/2025/sc.yaml`); L-20, L-24.
- `s2_other_screen`: every Schedule 2 line checked against i1040gi pp. 111–114: 1b/1c clean_vehicle; 1d–1f, 16, 17a,
  17j, 17l, 17n, 19 business; 1y L-30; 5, 6 tips/other_work_pay; 9 household (L-26); 10 reserved; 13 tips and
  employer_other_pay; 14, 15 L-1; 17b agency_home; 17d hsa; 17e, 17f savings_accounts; 17g L-6; 17h, 17i L-12; 17k
  employer_other_pay or business; 17m equity_amt; 17o citizenship; 17p, 17q foreign_shares; 17z L-35; 20 L-29.
- `s3_line14_screen`: L-2, L-28. `sb_screen`: L-34, L-35. `sd_screen`: L-1, L-2, L-3, L-16, L-18. `x_other_screen`:
  L-9, L-40. `line8_other_screen`: lines 8a–8v mapped (i1040gi pp. 91–92); L-10, L-25. NY joints: L-21, L-22;
  `ny_city_credits` sound (part-year credit excluded by `city_resident` true).

## What was checked fully vs sampled
- Fully: every topic's prompt against its covered inputs' labels; every joint rule's parent set; the four screens'
  clause mapping against `scope.yaml`; Schedule 1 lines 8a–8z and 24a–24z, Schedule 2 lines 1a–21, Schedule 3 lines
  1–13z, Form 1040 line 1h and line 16 box 3 against i1040gi; the MCTMT gate against ny_it201i and `pendingOf`.
- Sampled: NY inputs (lines 20, 28, 53, 54 only); the `uncovered` list (read for misclassification, not each input's
  form text); i1040sb and i8949 lists.
- Not checked: Form 4136 nontaxable uses for `s3_line12_screen` (i4136 not archived); i4684, i6252, i8814, i8911,
  i8978, Pub. 536, Form CT-2 instructions (not archived; findings resting on them are marked); NY `special_code`,
  `it225`, `other_credits`, `other_taxes` lists; the engine's handling after a "yes" (e.g. whether 1099-R codes 8/P reach
  line 1h); fixture behaviour; the web UI.
