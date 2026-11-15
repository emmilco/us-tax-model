# The map: the whole interview redrafted by topic

Written by the architect agent on 2026-11-13 for the lanes of the provisional redraft. Read `NORMS.md` first; a lane
then needs its own section of Part 3, the rows of Part 2 that name it, and Part 4. Nothing here is built yet.

**What was read and what was inferred.** Read: `NORMS.md`, the three owner documents, `interview/README.md` (Question
data, Blocks), `TASKS.md` T-284 to T-289, the prompt of every one of the 619 questions in
`canonical/2025/interview-full.json` (the long ones in full, per-month repeats of Form 1095-A and the cost lines of Form
5695 by their first line), `interview/2025/gate_frequencies.yaml`, the printed lines of Schedule 1 and Schedule 2
(`sources/2025/f1040s1.txt`, `f1040s2.txt`), and a walk of the minimal return through the built engine. Every statement
below that a question **refuses** comes from the `refuses:` entries of `forms/2025/*.yaml`, indexed by
`docs/provisional/map_work/refs.py` ("direct" = the input is itself a `when`; "via" = a derived line that reads it is a
`when`). "Asked of everyone" means asked in the minimal return's walk (`map_work/minimal_walk.tsv`: 82 questions, 6,799
prompt words, single filer with nothing). **Not read:** the form instructions; the body of most form YAML beyond gates
and refusals; the engine source beyond what the README says. Costs and shares marked *est.* are my estimates on the
owner's scale (1, 5, 20); shares marked *gf* are from `gate_frequencies.yaml`. Part 5 lists each inference that matters.

Scratch tools a lane may reuse (`docs/provisional/map_work/`): `walk.mjs` (the minimal walk), `show.py <form...>` (the
questions of a form with their gates), `refs.py <input...>` (who reads an input and what it refuses), `line.py <line...>`
(a form line without its text), `assign.py` (the topic and lane of every question, as tabled below). Run `node docs/provisional/map_work/cards.mjs`
and `python3 docs/provisional/map_work/refs.py` first: they write the two index files the others read (`cards.json`,
`refs.json`, not committed).

---

## Part 1. The topic order

Each topic has a **range of order numbers** of its own. A lane gives each sub-block inside its range one order number
and a `seq` to every question of it (an order number is all block or none). No lane uses a number outside its ranges.
Order numbers 0 to 31 are today's; a question still carrying one has not been placed.

| Order | Topic (plain name) | What belongs to it | Opening question (the off-ramp) | Why here | Lane |
|---|---|---|---|---|---|
| 100–109 | Who this return is for | `$person`, `f1040.status`, `household.*` (not `credit_disallowed`) | `$person` (approved) | First: every later wording depends on it | 1 |
| 110–119 | About you | `person.under16`, `age65`, `blind`, `died_before_65`; `sa.dependent`; `sa.excluded_income`; `s3.disability_retired`; from Part 2: citizenship, chapter 11, armed forces, under 24 | None: seven facts known at once, each asked of everyone | Facts about the person go with who the return is for (rule 1); three of them refuse (N11) | 1 (wording), 9 (new items) |
| 120–129 | Children and other dependents | `$dependent`, `dependent.*` tests, `s3.adoption*`; from Part 2: a child's investment income | `$dependent`, reworded as a plain question; an empty list skips the topic | Family comes before money | 2a |
| 130–139 | Income this tool cannot prepare | New, from `scope.schedule1` and `scope.other_income`: rental and royalties, Schedule K-1, farming and fishing, passive activity | Each is its own refusing question | The largest refusal in the interview (12% *gf* `scope_schedule1`) told before any figures are typed (N11); lowest cost per chance of leaving (1 ÷ 0.10) | 9 |
| 140–149 | Your jobs | `$w2`, `w2.box1`–`box7`, `person.rrta`, `person.educator_*`; from Part 2: pay not on a W-2, special marks on a W-2, religious work, Medicaid waiver pay, other earned income | `$w2` per person; an empty list skips the boxes | 79% have wages (*gf*) | 3; 9 and 7b (new items); 4b (educator) |
| 150–154 | Tips and overtime | `s1a.tips`, `s1a.overtime`, `$tipjob`, `tipjob.*`, `$otjob`, `otjob.*` | `s1a.tips`, `s1a.overtime` reworded | Follows the W-2s it reads from | 3 |
| 155–159 | Care for a child or dependent, and help in the home | `f2441.*`, `$dcprov`, `dcprov.*`, `dependent.dc_*`, `w2.box10*`; from Part 2: household employment tax, care benefits outside box 10 | `f2441.care`, `f2441.benefits` reworded | Needs the dependents and the W-2s, both now entered | 2b |
| 160–169 | Other money you received | `s1.*`, `$oi8z`, `oi8z.*`, `refund.*`; from Part 2: recoveries, long-term care payouts | One plain parent per kind (Part 2, `s1.line8_other`) | "Other income" of N7; state refunds are common (40% *gf*) | 7b (`s1`, `oi8z`), 7a (`refund`) |
| 170–177 | Retirement money you received | `$retirement`, `retirement.*` (not `sav_*`); from Part 2: disaster distributions | `$retirement` per person | 24% (*gf*) | 4a |
| 178–179 | Social security | `ssb.*` | New parent over `ssb.benefits` | 20% (*gf*) | 4a |
| 180–189 | Saving for retirement | `person.sav_trad`, `person.ira_*`, `person.x_*`, `ira.*`; from Part 2: excess 401(k) deferrals | `person.sav_trad` reworded; new parent over `person.x_other` | After retirement income, which its limits read | 4b |
| 190–194 | Health savings accounts | `$f8889`, `f8889.*`, `person.x_hsa_value` (redesigned; order only); from Part 2: Archer MSA | `$f8889` (done) | Health | 8a (order only) |
| 195–199 | Marketplace health insurance | `$f1095a`, `f1095a.*`, `f8962.*`, `dependent.ptc_*` | `$f1095a` reworded as a plain question | Health | 8a |
| 200–219 | Your home, taxes you paid, gifts and medical bills | `sa.*` (not the two in 110), `$gift`, `gift.*`, `s3.mcc` | New plain parents (Part 2, Schedule A) | "Home" of N7; asked of everyone today at 1,400 words | 7a |
| 220–224 | A loan for a new car | `s1a.carloan`, `$carloan`, `carloan.*` | `s1a.carloan` reworded | 3% (*gf*) | 3 |
| 225–229 | Electric vehicles and home fuel | `s3.ev*`, `s3.kerosene*` (redesigned; order only) | `s3.ev`, `s3.kerosene` (done) | Things bought for the home | 7b (order only) |
| 230–239 | Home energy improvements | `f5695.*` | One new parent replacing `part1_any` and `part2_any` | 2.5% (*gf*) | 8b |
| 240–249 | Education and student loans | `f8863.*`, `person.edu*`, `dependent.edu*`, `sli.interest`; from Part 2: recapture of an education credit | `f8863.paid` reworded; new parent over `sli.interest` | N7 | 8b |
| 250–254 | Your own business | `$sc`, `sc.*` | `$sc` per person, reworded | 19% (*gf*) | 6a |
| 255–256 | Business vehicles | `$scveh`, `scveh.*` | `$scveh` | Beneath the business | 6b |
| 257–258 | Business equipment | `$asset`, `asset.*`, `s179.*` | `$asset`; `s179.line10` beneath a parent | Beneath the business | 6b |
| 259–269 | The owner's own plan, insurance and deduction | `$ltc`, `ltc.*`, `person.plan*`, `sep_*`, `simple_*`, `se_screen`, `qbi.unsupported`, `qbi.carryforward`; from Part 2: solo 401(k) | `qbi.unsupported` moves beneath `$sc` | Beneath the business | 6a |
| 270–271 | Interest | `$interest`, `interest.*`, `sb.unsupported`, `f1040.tax_exempt_interest` | `$interest` reworded | 34% (*gf*) | 5a |
| 272–273 | Dividends | `div.*`, `sb.ordinary_dividends`, `sd.distributions`, `f1040.line3a`, `qbi.dividends` | `div.any` reworded short | 21% (*gf*) | 5a |
| 274–275 | Sales of investments | `$sales`, `sales.*`, `sd.other_forms` | New plain parent before `$sales` | 13% (*gf*) | 5b |
| 276 | A loss carried from 2024 | `sd.carryover`, `clcw.*`, `clcw26.*`, `f8960.prior_2i` | `sd.carryover` reworded | 4.5% (*gf*) | 5b |
| 277 | Borrowing to invest | `f4952.*` | `f4952.has_interest` reworded short | 1% (*gf*) | 5b |
| 278 | Tax on investment income of high earners | `f8960.*` | Reached only above the income threshold (computed) | Rare | 5b |
| 279–284 | Tax paid to another country | `ftc.*`, `s3.foreign_any` and its three children | `s3.foreign_any` (done); `ftc.taxes` beneath a paper cue | 7% (*gf*) | 5a |
| 285–289 | Accounts and assets outside the United States | `sb.foreign_any`, `sb.line7a`, `sb.line8`, `sb.form5471`, `sb.form8938`, `sb.fbar_required`; from Part 2: foreign funds and companies | `sb.foreign_any` cut to a short parent | 2.5% (*gf*) | 5a |
| 290–299 | Rare situations | `s2.*`, `s3.credit_bond`, `s3.farmland*`, `s3.repaid_income`, `s3.prior_*`; from Part 2: the items with no home | Each its own question | The rare things last (N7) | 7b |
| 300–309 | Tax you already paid, and your refund | `f1040.line25b`, `line25c_other`, `line26`, `s3.line10`, `f1040.line35a`, `line36` | New parents over the three amounts | The end of the story | 1 |
| 310–319 | Last checks for credits | `eic.*`, `s8812.*`, `household.credit_disallowed`, `person.tin`, `work_ssn`, `itin_applied`, `eic_ssn`, `born_*`, `dependent.eic_ssn`, `us_half`, `person.sav_*` (not `sav_trad`), `retirement.sav_*`, `w2.box12*`, `w2.g_*`, `s3.elderly_credit` | None: each is reached only when the income already entered allows the credit | Their gates are computed from income, so they cannot be asked earlier; kept from interrupting another topic | 2b; 4b (`sav_*`); 3 (`w2.box12*`) |

33 topics (the business and investments are several short topics each, asked in a row). The four parts already redesigned keep their questions; only their order numbers move (opening to 100,
adoption to 120, the other credits questions to 110, 225, 279, 290 and 310, health savings accounts to 190).

### Where today's order numbers go

| Today | Goes to (topic: questions) |
|---|---|
| 0 | 100: `$person`, `f1040.status`. The three `scope.*` screens are dissolved (Part 2) |
| 1 | 150: `$otjob`, `$tipjob`. 170: `$retirement`. 195: `$f1095a`. 220: `$carloan`. 274: `$sales` |
| 2 | 100: `household.*` (8). 110: `person.under16`. 120: `$dependent`, `dependent.*` (22), `s3.adoption*` (4). 150: `otjob.*` (4), `tipjob.*` (2). 170: `retirement.*` (15). 195: `f1095a.*` (42), `dependent.ptc_*` (2). 220: `carloan.*` (10). 274: `sales.box`. 310: `person.tin`, `person.work_ssn` |
| 3 | 120: `dependent.*` (7). 140: `w2.box1`, `box2`, `box4`. 170: `retirement.*` (3). 274: `sales.special`. 310: `person.itin_applied` |
| 4 | 140: `w2.box3`, `box5`, `box6`, `box7`. 170: `retirement.exc_amount`. 274: `sales.code` |
| 5 | 140: `$w2`. 200: `sa.gifts`, `$gift`. 274: `sales.route` |
| 8 | 270: `$interest` |
| 9 | 190: `$f8889`, `f8889.*` (31), `person.x_hsa_value` |
| 10 | 110: `person.age65`, `blind`, `died_before_65`, `sa.dependent`, `sa.excluded_income`, `s3.disability_retired`. 140: `f8959.unsupported`, `person.rrta`, `person.educator_*` (2). 150: `s1a.tips`, `s1a.overtime`. 160: `s1.*` (18), `$oi8z`, `oi8z.*`, `refund.*` (16). 178: `ssb.*` (4). 180: `person.x_other`. 195: `f8962.*` (6). 200: `sa.*` (11), `gift.*` (3), `s3.mcc`. 220: `s1a.carloan`. 225: `s3.ev*`, `s3.kerosene*` (7). 240: `f8863.paid`, `sli.interest`. 259: `qbi.unsupported`. 270: `interest.*` (2), `sb.unsupported`. 272: `div.any`, `sb.ordinary_dividends`, `sd.distributions`, `f1040.line3a`, `qbi.dividends`. 274: `sales.*` (5), `sd.other_forms`. 276: `sd.carryover`, `clcw.*` (6). 277: `f4952.*` (7). 278: `f8960.*` (3). 279: `ftc.*` (6), `s3.foreign_any`, `section960c`, `section965`, `virgin_islands`. 285: `sb.*` (6). 290: `s2.*` (2), `s3.credit_bond`, `farmland*`, `repaid_income`, `prior_*` (7). 300: `f1040.line25b`, `line25c_other`, `line26`, `s3.line10`. 310: `s3.elderly_credit` |
| 11 | 160: `s1.gambling_pro`. 195: `f8962.alien_below`, `estimate_100`. 200: `sa.gambling_losses`. 250: `$sc`. 255: `$scveh`. 257: `$asset`. 276: `f8960.prior_2i` |
| 12 | 220: `carloan.col_ii_input`. 250: `sc.*` (48). 255: `scveh.*` (24). 257: `asset.*` (15), `s179.line10`. 259: `$ltc`, `ltc.*`, `person.plan*`, `sep_*`, `simple_*`, `se_screen` (9), `qbi.carryforward` |
| 15 | 257: `s179.wc_interest`. 272: `div.box*` (10). 276: `clcw26.final_return` |
| 20 | 155: `f2441.benefits`, `f2441.care`. 300: `f1040.line35a`, `line36`. 310: `household.credit_disallowed`, `s8812.*` (2) |
| 21 | 155: `dependent.dc_*` (4), `f2441.*` (4), `w2.box10*` (2). 240: `dependent.edu*` (13), `person.edu*` (12) |
| 22 | 155: `f2441.*` (6). 180: `person.sav_trad`, `person.ira_trad` |
| 23 | 155: `$dcprov`, `dcprov.*`. 180: `ira.se_capital`, `ira.special`, `person.ira_age50`, `ira_work_plan` |
| 24–27 | 230: `f5695.*` (56). 180: `person.ira_excess`, `ira_basis`, `ira_basis_adjusted`, `ira_dist`. 310: `person.sav_*` (9), `retirement.sav_*` (3), `w2.box12*`, `w2.g_*` (13) |
| 28 | 180: `ira.deduct_less` |
| 30 | 178: `ssb.lived_apart`. 270: `f1040.tax_exempt_interest`. 272: `div.box12`. 310: `eic.*` (5), `person.eic_ssn`, `born_*`, `dependent.eic_ssn`, `us_half` |
| 31 | 180: `person.x_births`, `x_prior09`. 240: `person.edu_*` (6), `dependent.edu_over`, `f8863.ban` |

---

## Part 2. Every catch-all taken apart

**How to read the tables.** *Refuses today*: yes means a Yes to the catch-all refuses the return (read from the form
YAML). *Destination*: the topic's order range, then the question that asks the item. A name in `code` that does not
exist today is a **new input, with the id fixed here** so that other lanes can refer to it; "parent" marks a new plain
question that refuses nothing itself. *Already caught by*: an existing question that every filer with the item reaches
and that refuses the same situation; the item's wording is then deleted from the catch-all and nothing new is built.
*Lane*: who builds it. Where a destination sits beneath a parent, the last column of the scope tables says who could
wrongly answer the parent No.

**The model rule behind every table (Part 4.1 states it in full).** An item moves in the *interview* (its order, its
parent, its words). Its *input* is declared in the form file that refuses on it today, by the lane that owns that file,
and the old catch-all id stays as a derived line (true when any of its items is true), so that the lines of other
forms that refuse on it are not edited by anyone.

### 2.1 `scope.schedule1` (293 words, asked of everyone, refuses: direct at `scope.ready`, `f1040.line8`, `f1040.line10`, `ssb.line6`, `s8812.eiw_3`, `s8812.eiw_4`, `s1a.line5_calc`, `s1a.line14b_calc`, `eic.clergy`, `eic.step2_other`, `eic.step5_line1`). Lane 9.

| # | Item | Refuses today | Destination | Who could wrongly say No to the parent |
|---|---|---|---|---|
| 1 | Statutory-employee wages | yes | 140: `scope.statutory_employee`, "Is the box 'Statutory employee' ticked in box 13 of any of your W-2s?"; asked only when a W-2 is listed (Part 4.6) | No one: a statutory employee has a W-2 by definition |
| 2 | Income as a minister, a member of a religious order, a Christian Science practitioner | yes | 140: parent `scope.religious_work` ("In 2025, were you paid for work by a church or religious body, or as a minister, priest, rabbi, imam or other clergy?"), child `scope.clergy` | Clergy paid by a hospital, the military or a school: the parent names the work as well as the payer |
| 3 | Church employee income (church exempt from social security and Medicare) | yes | 140: child `scope.church_exempt_wages` beneath `scope.religious_work`, with the paper cue (boxes 4 and 6 of that W-2 are empty) | A lay employee of a church-controlled organization that is not called a church (a school, a hospital): the parent's help names them |
| 4 | A refund or recovery of an amount deducted in an earlier year, other than a state income tax refund (sales, real estate or personal property tax; mortgage interest, Form 1098 box 4; medical reimbursement; bad debt) | yes | 160, next to the state refund: `scope.recovery`, a question of its own | No parent |
| 5 | Sales of business property (Form 4797) | yes | **Already caught by** `sd.other_forms` (direct refusal, asked of everyone). Lane 5b's split of that question carries it (2.8) | n/a |
| 6 | A net operating loss deduction | yes | 290: child `scope.nol` beneath parent `scope.business_before` ("In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or S corporation?") | A loss from a casualty with no business ever: rare; the parent's help names it |
| 7 | Rental real estate, royalties | yes | 130: `scope.rental`, refuses on the fact ("In 2025, did you rent out anything you own, such as a house, a room, land, a vehicle or equipment, or receive royalties?") | No parent |
| 8 | Partnerships, S corporations, estates, trusts (Schedule E or a Schedule K-1) | yes | 130: `scope.k1`, refuses on the fact ("In 2025, did you have income or a loss from a partnership, an S corporation, an estate or a trust? It is reported to you on a Schedule K-1.") | No parent |
| 9 | Rental of personal property | yes | 130: the same `scope.rental` (its examples name a vehicle and equipment) | No parent |
| 10 | Farm income (Schedule F) | yes | 130: parent `scope.farm_fishing` ("In 2025, did you have income from farming or from fishing as your business?"), child `scope.farm` | A landowner who only receives farm rent or conservation payments: the child's words; the parent's help names them |
| 11 | An exclusion of Medicaid waiver payments (line 8s) | yes | 140: `scope.medicaid_waiver` ("Did a state Medicaid program pay you to care for someone who lives in your home?"); one input for this item and item 3 of 2.2 | No parent |
| 12 | Other retirement plans for the self-employed (solo 401(k), Keogh) | yes | 259: `scope.se_plan_other`, asked only when a business is listed (Part 4.6) | A partner with a Keogh plan and no Schedule C: already refused at `scope.k1` |
| 13 | Schedule 1 line 12: expenses of reservists | yes | 110: parent `scope.armed_forces` ("Since the start of 2022, did you serve in the U.S. armed forces, the reserves or the National Guard?"), child `scope.reservist_expenses` | No one who served in 2025 |
| 14 | Line 12: expenses of performing artists; of fee-basis state or local officials | yes | 140: two questions of their own, `scope.performing_artist`, `scope.fee_official`, asked only when a W-2 is listed | Both are employees, so both have a W-2 |
| 15 | Line 14: moving expenses of members of the armed forces | yes | 110: child `scope.military_move` beneath `scope.armed_forces` | No one |
| 16 | Line 23: Archer MSA deduction | yes | 190: `scope.archer_msa`, a question of its own with a gloss (`f8889.archer` is reached only by a person with a health savings account) | No parent |
| 17 | "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately": the lines the question does not name | yes | The printed Schedule 1 is a closed list (read from `sources/2025/f1040s1.txt`). Lines 8a to 8v are in 2.6. Line 24: 24b (personal property rental expenses) at `scope.rental`; 24c (Olympic medals) with 8m in 2.6; 24d reforestation, 290: `scope.reforestation` ("Did you plant or replant trees for timber on land you own?"); 24e, **already caught by** `s1.uc_unsupported`; 24f (section 501(c)(18)(D) plan), 140: beneath the W-2 by its box 12 code H, `scope.code_h_deduction`; 24g (chaplain's 403(b) contributions), 140: child `scope.chaplain_403b` beneath `scope.religious_work`; 24h and 24i (attorney fees for a discrimination or whistleblower award), 290: parent `scope.lawsuit_award` ("In 2025, did you receive money from a lawsuit, a settlement or a whistleblower award?"), child `scope.attorney_fees`; 24j (Form 2555 housing), **already caught by** `sa.excluded_income`; 24k (estate or trust excess deductions) at `scope.k1`; 24z (write-in), 290: `scope.other_adjustment`, the one residual question (Part 5, question 5) | `scope.lawsuit_award`: no one; a plain fact |

The list "The ones this tool asks about separately" is not an item: it disappears.

### 2.2 `scope.other_income` (188 words, asked of everyone, refuses: direct at `scope.ready`, `f1040.line8`, `eic.step1_resident`, `eic.step5_line2`). Lane 9. Destinations as the owner agreed in the walk notes.

| # | Item | Refuses today | Destination | Who could wrongly say No to the parent |
|---|---|---|---|---|
| 1 | Nonresident alien for any part of 2025 (you or your spouse) | yes | 110: parent `scope.citizen` ("Were you a U.S. citizen for all of 2025?", per the spouse phrase), child `scope.nonresident` (green card held all year, or resident all year, with the gloss) | No one: a citizen is not a nonresident alien |
| 2 | Wages or tips not on a Form W-2 | yes | 140, after the W-2 list: `scope.pay_no_w2` ("In 2025, were you paid as an employee in a way no W-2 shows: cash wages, tips you did not report to your employer, or pay from a firm that called you a contractor although you were its employee?") | No parent. It must not sit beneath `$w2`: a household worker may have no W-2 at all |
| 3 | Medicaid waiver payments | yes | 140: `scope.medicaid_waiver` (2.1 item 11) | No parent |
| 4 | Adoption benefits | yes | 120: child `scope.adoption_benefits` beneath the existing `s3.adoption_any` ("Did an employer pay or repay any of the adoption costs? Box 12 of the W-2 shows it with code T.") | An employee whose employer paid every cost and whose adoption is not final may answer the parent No ("did you ... pay costs"). Lane 2a adds to the help of `s3.adoption_any`: "Count costs your employer paid." |
| 5 | Dependent care benefits other than those in box 10 of a W-2 | yes | 155: child `scope.care_benefits_other` beneath the existing `f2441.benefits` | Anyone whose benefits are not in box 10, as `f2441.benefits` is worded today. **Coupled change:** lane 2b rewords `f2441.benefits` to "Did an employer, or your own business, help pay for the care of your child or dependent in 2025 (for example a dependent care account at work)?" |
| 6 | Other earned income (Form 1040 lines 1b to 1d and 1f to 1h) | yes | 1b, 1c and 1g are `scope.pay_no_w2`; 1d is `scope.medicaid_waiver`; 1f is `scope.adoption_benefits`; 1h, 140: `scope.other_earned`, a question of its own with a gloss ("for example strike benefits"). Lane 9 reads the line 1h instructions and names in the gloss each kind no other question catches (Part 5, inference 3) | No parent |
| 7 | Income or loss from a passive activity (including gain on selling an interest) | yes | 290: child `scope.passive` beneath `scope.business_before` (2.1 item 6), with a gloss. A passive activity begun in 2025 is a rental or a K-1 (refused at 130) or a business the filer does not run (`sc.passive`, refuses via `sc.screened`) | A person whose first passive interest was acquired and sold within 2025 with no K-1: not found; the K-1 question catches a final K-1 |
| 8 | The 2025 part of a qualified disaster recovery distribution of 2023 or 2024, or a 2025 repayment (Form 8915-F) | yes | 170: `scope.disaster_distribution`, a question of its own. **Not** beneath `$retirement`: the filer may have no Form 1099-R for 2025 | No parent |
| 9 | A repayment to an IRA of a qualified reservist distribution | yes | 110: child `scope.reservist_repaid` beneath `scope.armed_forces` | A reservist whose service ended before 2022: the repayment window is two years after active duty ends, which the parent's "since the start of 2022" covers for a 2025 repayment (inference 4) |
| 10 | A chapter 11 bankruptcy case open in 2025 | yes | 110: `scope.chapter11` ("At any time in 2025, were you in a chapter 11 bankruptcy case?") | No parent |

The six "kinds this question is not about" disappear.

### 2.3 `scope.other_line16` (182 words, asked of everyone, refuses: direct at `scope.ready`, `f1040.line16`, `eic.step2_other`). Lane 9.

| # | Item | Refuses today | Destination | Who could wrongly say No to the parent |
|---|---|---|---|---|
| 1 | Form 8814 (a child's interest and dividends on the parent's return) | yes | 120: parent `scope.child_investment_income` ("In 2025, did a child of yours have more than $1,350 of interest, dividends or other investment income?"), child `scope.f8814` ("Are you putting that income on your own return instead of filing a return for the child?") | No one: the election needs such income. Asked whether or not a dependent is listed (the child of divorced parents) |
| 2 | Form 8615 (five conditions) | yes | 110: parent `scope.under24` ("Were you under 24 at the end of 2025?"; reached only when not filing jointly, and not when born before 1961), child `scope.unearned_2700` ("more than $2,700 of income that was not pay for work"), child `scope.f8615` (the remaining conditions, precisely) | No one |
| 3 | A section 962 election | yes | 285: child `scope.sec962` beneath `scope.foreign_shares` (row 5) | See row 5 |
| 4 | Form 8621 | yes | 285: child `scope.pfic` beneath `scope.foreign_shares` | See row 5 |
| 5 | Stock, owned directly or indirectly, in a controlled foreign corporation or a passive foreign investment company, even with nothing to include | yes | 285: parent `scope.foreign_shares` ("Do you own shares of a company or an investment fund set up outside the United States? Shares of foreign companies held inside a U.S. mutual fund or ETF do not count."), children `scope.pfic` (a foreign fund) and `scope.cfc` (a foreign company mostly owned by U.S. persons). **Not** beneath `sb.foreign_any`: a foreign fund held in a U.S. brokerage account is outside that question | An indirect holder through a foreign trust or partnership: refused at `scope.k1` or `sb.line8` |
| 6 | Form 4972 (lump-sum distribution) | yes | **Already caught by** `retirement.special` (direct refusal, asked of every Form 1099-R), which lane 4a splits (2.9) | n/a |
| 7 | A Form 8978 amount | yes | 290: child `scope.f8978` beneath `scope.business_before` ("Did a partnership you are or were in send you a Form 8986 about an audit?") | No one: a partner of an earlier year answers the parent Yes |
| 8 | Recapture of an education credit | yes | 240: `scope.education_recapture`, a question of its own ("In 2025, were you refunded tuition for which an education credit was claimed in an earlier year?"). Not beneath `f8863.paid`: there may be no 2025 expenses | No parent |
| 9 | Income averaging of farming or fishing income (Schedule J), if chosen | yes | 130: child `scope.income_averaging` beneath `scope.farm_fishing`; refuses on the wish, with the remedy "answer No to go on without it" | No one |

### 2.4 `s2.other` (124 words) and `s2.amt` (17 words), both asked of everyone, both refuse directly at `s2.line2`, `s2.line3`, `s2.line21`; `s2.other` also at `s8812.line22`, `tipjob.col_c`, `s1a.line4b_calc`. Lane 7b.

`s2.other` lists seven examples "for example"; the printed Schedule 2 is a closed list (read from `sources/2025/f1040s2.txt`), so every line is placed.

| Schedule 2 line | Item | Named in the question | Destination |
|---|---|---|---|
| 1a | Excess advance premium tax credit | no (the tool figures it) | Not an item |
| 1b, 1c | Repayment of a clean vehicle credit a dealer took off the price | yes | A 2025 purchase: **already caught by** `s3.ev_dealer` (refuses via `s3.ev_dealer_if_ev`). A 2024 purchase repaid on this return: 225, `s2.ev_repayment`, a question of its own ("Did a dealer take a federal tax credit off the price of a vehicle you bought in 2024, and was your 2024 income over the limit for it?") |
| 1d, 1e, 1f, 19 | Elective-payment recapture (Form 4255) | no | 259: `s2.business_credit_recapture`, asked only when a business is listed; one question with 16 and 17a ("Must you pay back a business tax credit taken in an earlier year?") |
| 1y, 17z | Other additions, other taxes (write-in) | no | 290: `s2.other_tax`, the residual question (Part 5, question 5) |
| 2 | Alternative minimum tax | yes, and `s2.amt` | 290: `s2.amt` kept, its children built from the "Who must file" list of the Form 6251 instructions, which I did not read (Part 5, question 6). First child by a paper cue: `s2.iso` ("Did you exercise incentive stock options in 2025 and keep the shares? Your employer sends Form 3921.") |
| 5 | Tax on unreported tips (Form 4137) | yes | **Already caught by** `scope.pay_no_w2` (tips not reported) once lane 9 has built it; allocated tips in box 8 go to the W-2 marks question below |
| 6 | Uncollected tax on wages (Form 8919) | no | **Already caught by** `scope.pay_no_w2` |
| 8 | Form 5329 beyond what the tool figures | no (named as figured) | `person.x_other` (2.8) |
| 9 | Household employment taxes | yes | 155: `s2.household_employee` ("In 2025, did you pay one person $2,800 or more to work in your home, such as a nanny, a carer or a housekeeper?"), a question of its own; `dcprov.household` stays as the per-provider question |
| 13 | Uncollected social security, Medicare or RRTA tax on tips or group-term life insurance (W-2 box 12 codes A, B, M, N) | yes | 140: `s2.w2_marks`, asked only when a W-2 is listed: "Look at your W-2s. Does any have an amount in box 8, or one of the letters A, B, M or N in box 12?" One subject: tax the employer did not collect. Children are not needed: any Yes refuses |
| 14, 15 | Interest on deferred tax (installment sales) | yes | **Already caught by** `sd.other_forms` (Form 6252), split by lane 5b |
| 16, 17a, 17b | Recapture of the low-income housing credit, of other credits, of a federal mortgage subsidy | no | 16 and 17a with 1d above. 17b, 200: `s2.mortgage_subsidy` beneath the home parent, by lane 7b in `s2.yaml`, gated on lane 7a's existing `sa.line8a` being above zero (as `s3.mcc` is): "Did you sell a home in 2025 that you bought with a state or local subsidized mortgage?" |
| 17c | Additional tax on HSA distributions | no (figured) | Not an item |
| 17d | Additional tax on an HSA not kept as an eligible individual (Form 8889 Part III) | yes | **Already caught by** `f8889.testing_prior` and `f8889.ira_prior` for a person with an account in 2025. For a person with no account in 2025: 190, `s2.hsa_testing` beneath the No of `$f8889` ("Did you have a health savings account in 2024?" then the testing question). Reach to be checked by lane 7b against `f8889.yaml` |
| 17e, 17f | Additional tax on Archer or Medicare Advantage MSA distributions | no | **Already caught by** `scope.archer_msa`; lane 9 words it to include a Medicare Advantage MSA |
| 17g | Recapture of a charitable deduction (fractional interest) | no | **Already caught by** `oi8z.kind` = `charitable_recapture` (refuses via `oi8z.additional_tax`) |
| 17h, 17i | Nonqualified deferred compensation failing section 409A or 457A (W-2 box 12 code Z, Form 1099-MISC box 15) | no | 140: second question on the W-2 marks, `s2.w2_code_z` ("letter Z in box 12") |
| 17j, 17k, 17m | Excess benefits tax; golden parachute (W-2 box 12 code K); insider stock compensation | no | 17k with `s2.w2_code_z` (codes K and Z in one paper check); 17j and 17m, 290: `s2.rare_excise`, one question of its own (two subjects no filer meets without being told by the payer; Part 5, question 5) |
| 17l | Accumulation distribution of a trust | no | Refused at `scope.k1` or `sb.line8`; not asked again |
| 17n | Look-back interest (Forms 8697, 8866) | no | 259: `s2.lookback`, asked only when a business is listed |
| 17o | Tax for the part of the year as a nonresident alien | no | **Already caught by** `scope.nonresident` |
| 17p, 17q | Interest from Form 8621 | no | **Already caught by** `scope.pfic` |
| 20 | Section 965 installment | no | **Already caught by** `s3.section965` |

### 2.5 `f8959.unsupported` (67 words, one sentence, asked of everyone, refuses directly at seven `f8959` lines). Lane 7b.

| # | Item | Destination |
|---|---|---|
| 1 | Church employee income | **Already caught by** `scope.church_exempt_wages` |
| 2 | Other self-employment income outside Schedule SE as the tool prepares it | **Already caught by** `person.se_screen` (refuses via `person.se_screened`) for a person with a business; for one without, by `scope.k1`, `scope.farm`, `scope.clergy`. Lane 7b checks no kind is left (director's fees with no Schedule C) and keeps a child `f8959.other_se` if one is |
| 3 | RRTA compensation | **Already caught by** `person.rrta` (direct refusal, asked of every person) |
| 4 | Tips not reported to the employer, or allocated tips in box 8 (Form 4137) | `scope.pay_no_w2`; box 8 in `s2.w2_marks` |
| 5 | Form 8919 wages | `scope.pay_no_w2` |
| 6 | Uncollected Medicare tax, box 12 codes B or N | `s2.w2_marks` |
| 7 | Medicare wages on a wage statement from a U.S. territory (Form 499R-2/W-2PR) | 140: `f8959.territory_w2` ("Is any of your wage statements from Puerto Rico or another U.S. territory?"), asked only when a W-2 is listed |

After this the question has no item of its own and is removed; `f8959.unsupported` stays as a derived line.

### 2.6 `s1.line8_other` (189 words, asked of everyone, refuses directly at `s1.line9`). Lane 7b. The printed line 8 is a closed list.

| Line | Item | Destination |
|---|---|---|
| 8a | Net operating loss | **Already caught by** `scope.nol` |
| 8d | Foreign earned income or housing exclusion (Form 2555) | **Already caught by** `sa.excluded_income` (direct refusal, asked of everyone; moved to 110 and reworded by lane 1) |
| 8e | Income from Form 8853 | Archer and Medicare Advantage MSA: `scope.archer_msa`. Long-term care payouts: 160, `s1.ltc_payout` ("Were you paid benefits from a long-term care insurance policy, or part of a life insurance death benefit early? Form 1099-LTC reports it.") |
| 8k | Stock options | 140: `s1.stock_options`, asked only when a W-2 is listed ("Did you get income from employer stock options that is not in box 1 of your W-2?") |
| 8l | Rental of personal property | **Already caught by** `scope.rental` |
| 8m | Olympic and Paralympic medals, USOC prize money | 160: child beneath the prizes parent (below), `s1.olympic` |
| 8n, 8o | Section 951(a), 951A(a) inclusions | **Already caught by** `scope.cfc` |
| 8p | Excess business loss adjustment | 259: `s1.excess_business_loss`, asked only when a business is listed and reworded as a fact the model may already know (a loss over $313,000, or $626,000 jointly; lane 7b checks the figure) |
| 8q | Taxable ABLE distributions | **Already caught by** `person.x_other` item 1 |
| 8s | Nontaxable Medicaid waiver payments | **Already caught by** `scope.medicaid_waiver` |
| 8t | Nonqualified deferred compensation pension, nongovernmental 457 plan | 170: `s1.nqdc_pension` ("Were you paid from a former employer's deferred compensation plan that is not a regular pension? It comes on a W-2, box 11.") |
| 8u | Wages earned while incarcerated | 140: `s1.inmate_wages` ("Were you paid for work while in a jail or prison?") |
| 8v | Digital assets received as ordinary income | 274, with sales of investments: `s1.digital_income` ("Did you receive crypto or other digital assets as pay, a reward, or from mining or staking?") |
| 8b, 8c, 8g, 8h, 8i, 8j, 8r, 8z | Asked item by item today | Each amount asked of everyone becomes a yes or no parent with the amount beneath (Part 3, lane 7b) |

The nine-line list of what the question is not about disappears. Four new questions are asked of everyone and one more with a W-2; with tick-boxes (T-285) they would be one screen.

### 2.7 One fact, one asker

The same situation is asked in several catch-alls today. One question keeps it (the **asker**); each other lane deletes
the words from its own catch-all (N8) and builds nothing. The deletion is right only when the asker refuses in every
case the deleted words refused and every filer who reached the deleted words reaches the asker; the lane states that
check in its notes. The askers marked *exists* are on this branch now, so the deletion does not wait for another lane.

| Fact | Asker | Words deleted from |
|---|---|---|
| Clergy, church employee income | `scope.clergy`, `scope.church_exempt_wages` (9) | `f8959.unsupported`; `person.se_screen` items 1, 2 (keep "an approved Form 4361 or Form 4029" there) |
| Schedule K-1, partnership, S corporation, estate, trust | `scope.k1` (9) | `person.se_screen` item 3 (K-1 part); `sd.other_forms` (K-1 gains); `f8960.unsupported` (pass-through); `f4952.has_interest` and `f4952.unsupported` (K-1 items); `sa.gifts` and `gift.special` (K-1 gifts); `div.any` (K-1 dividends); `qbi.unsupported` (other business income) |
| Rental, royalties | `scope.rental` (9) | `f8960.unsupported` (rental, royalty); `f4952.unsupported` (royalties) |
| Farm | `scope.farm` (9) | `person.se_screen` item 4 |
| Chapter 11 | `scope.chapter11` (9) | `person.se_screen` item 6; `sc.special` item 6 |
| Medicaid waiver payments | `scope.medicaid_waiver` (9) | `sc.special` item 9; `s1.line8_other` 8s |
| Form 4137, Form 8919 | `scope.pay_no_w2` (9) | `person.se_screen` item 9; `f8959.unsupported`; `s2.other` |
| Railroad retirement | `person.rrta` (*exists*) | `f8959.unsupported` |
| Form 2555, Form 4563, Puerto Rico exclusion | `sa.excluded_income` (*exists*; lane 1 rewords) | `ssb.pub915`; `sc.hi_screen`; `f8960.unsupported` (section 911); `s1.line8_other` 8d |
| Nonresident or dual-status alien | `scope.nonresident` (9) | `sa.dependent` ("or are you a dual-status alien") |
| Adoption benefits | `scope.adoption_benefits` (9) | `ssb.pub915` |
| Form 8915-F: the 2025 part of a distribution of 2023 or 2024, or a repayment | `scope.disaster_distribution` (9) | Nothing: a disaster distribution taken in 2025 is a different fact and stays a child beneath its Form 1099-R (`retirement.special` item 19, `retirement.early_screen` item 1; lane 4a makes them one child) |
| Reservist repayment | `scope.reservist_repaid` (9) | `ira.special` |
| Net operating loss | `scope.nol` (9) | `f8960.unsupported` (section 1411 net operating loss); `s1.line8_other` 8a |
| Controlled foreign corporation, passive foreign investment company | `scope.cfc`, `scope.pfic` (9) | `f8960.unsupported`; `s1.line8_other` 8n, 8o |
| Form 8814 | `scope.f8814` (9) | `sb.foreign_any` (the bullet on a child's accounts) |
| Form 4797, 6252, 4684, 6781, 8824, 2439 | `sd.other_forms` (*exists*; lane 5b splits) | `scope.schedule1` item 5; `sc.ho_other` (Form 4797 or 8949 gain); `s2.other` (deferred tax interest); `sa.unsupported` (casualty or theft: `sd.other_forms` says "a casualty or theft of property whether you held the property directly or through an entity", so it refuses every casualty today) |
| Archer MSA, Form 8853 | `scope.archer_msa` (9) | `person.x_other` item 3 (Archer part); `s1.line8_other` 8e |
| Excess contributions to a health savings account from an earlier year | `person.x_other` item 4 (*exists*; lane 4b) | Not asked again in the health savings block (T-288 notes the overlap) |
| A death in 2025 | Not settled: asked in six places, in five files (Part 5, question 4) | |
| Married filing separately | `f1040.status` (*exists*; `s3.mfs` refuses) | Every question reached only on a separate return is never asked (N8): `sa.spouse_itemizes`, `sa.spouse_extra`, `ssb.lived_apart` stay in the model and are not reworded (`refund.mfs_spouse_itemized` is about the 2024 status and is still asked) |

### 2.8 The other catch-alls and long questions asked of everyone

All are in the minimal walk. "Direct" and "via" are how the YAML refuses on them.

| Question (words; refusal) | Items | Destination: plain parent, then children | Lane |
|---|---|---|---|
| `person.x_other` (136; direct), per person | (1) taxable distribution from a Coverdell account, a 529 plan or an ABLE account; (2) excess IRA contributions of an earlier year still in the IRA; (3) excess contributions to a Coverdell account, an Archer MSA, an ABLE account; (4) excess HSA contributions of an earlier year; (5) a required minimum distribution not taken in full | 240: parent `person.x_edu_account` ("Did you take money out of, or put money into, a 529 plan, a Coverdell education account or an ABLE account?"), children for (1) and (3). 180: (2) is the same fact as `person.ira_excess` item 3: one child beneath a parent `person.ira_owner` ("Do you have an IRA of any kind?", 33% *gf*). 190: (4) `person.x_hsa_prior_excess`, a question of its own beside the account question. 170: parent `person.rmd_due` ("Did you have to take a minimum yearly withdrawal from a retirement account in 2025: aged 73 or over, or an inherited account?"), child `person.rmd_missed`. Archer MSA: `scope.archer_msa` | 4b |
| `sd.other_forms` (48; direct) | Form 4797 (business or rental property sold); 2439 (a fund's undistributed gains); 6252 (installment sale); 4684 (casualty or theft); 6781 (section 1256 contracts); 8824 (like-kind exchange); capital gains on a K-1 | 274: parent `sd.sold_other` ("In 2025, did you sell or trade real estate, business property, or anything you are being paid for over more than one year?"), children for 4797, 6252, 8824. Questions of their own: `sd.f2439` (paper cue: "Did a fund or REIT send you a Form 2439?"), `sd.sec1256` (paper cue: "an amount in boxes 8 to 11 of a Form 1099-B (futures and index options)"), 200: `sd.casualty` ("In 2025, was property of yours damaged, destroyed or stolen, with a loss insurance did not cover?"). K-1: `scope.k1` | 5b |
| `qbi.unsupported` (76; direct) | (1) other qualified business or PTP income or loss; (2) a REIT or PTP loss carried from an earlier year; (3) losses suspended earlier and allowed now; (4) patron of an agricultural or horticultural cooperative (Form 1099-PATR) | (1) is a K-1 or a rental: `scope.k1`, `scope.rental`. (2) and `qbi.carryforward` (30 words, also asked of everyone): one parent by the paper, `qbi.prior_form` ("Does your 2024 return include Form 8995 or 8995-A?"), then the two amounts from its last lines; a REIT or PTP amount refuses. (3) 259: child asked only when a business is listed. (4) 259: `qbi.coop_patron`, by the paper | 6a |
| `s179.line10` (77; via `s179.orphan`, `s179.mfs`) | An amount: the section 179 carryover from the last Form 4562 | 257: parent `s179.prior_form` ("Does your 2024 return, or the last one you filed with a business, include Form 4562 with an amount on line 13?"), amount beneath. Not beneath `$sc`: a carryover with no business in 2025 refuses today (`s179.orphan`) and must stay reachable | 6b |
| `sa.unsupported` (71; direct) | Casualty or theft loss; a Schedule A line 16 deduction other than gambling losses; a foreign tax deduction; a generation-skipping tax deduction; mortgage interest or points not on Form 1098; mortgage debt over the limit or used for something other than the home; the sales-tax election | Casualty: `sd.casualty`. Line 16: a closed list in the Schedule A instructions, which lane 7a reads and places item by item beneath the itemizing parent. Foreign tax deduction: 279, a wish child beneath `ftc.taxes` (lane 7a declares it in `sa.yaml`, gated on the existing `ftc.taxes` above zero). Mortgage items: 200, three children beneath the mortgage parent. Sales-tax election: 200, a wish child beneath the state-tax question, remedy "answer No to deduct income tax instead" | 7a |
| `sa.dependent` (48; direct) | Someone can claim you or your spouse as a dependent; dual-status alien | 110: "Can a parent or anyone else claim you as a dependent on their 2025 return?" (bank wording only; the exception for a claimant who does not file goes in a second sentence). Dual-status: `scope.nonresident` | 1 |
| `sa.excluded_income` (20; direct; names forms only) | Form 2555; Form 4563; income excluded as a resident of Puerto Rico | 110: bank wording only: "In 2025, did you live or work abroad, in Puerto Rico or in American Samoa, and leave that income out of this return?" (form numbers in parentheses) | 1 |
| `sb.foreign_any` (827; via its four children) | Nine bullets: foreign accounts and signature authority (three bullets); territory institutions, payment and crypto platforms abroad; other foreign assets; a child's accounts (Form 8814); foreign trusts and foundations (two bullets); officer, director or 10% owner of a foreign corporation | 285: the parent is cut into four short parents, each directly above the child it gates today: `sb.account_any` ("At any time in 2025, did you have, or could you sign for, a bank or other financial account outside the United States?") above `sb.line7a` and `sb.fbar_required`; `sb.asset_any` (other things of value held abroad) above `sb.form8938`; `sb.trust_any` above `sb.line8`; `sb.company_any` above `sb.form5471`. Each bullet's precision becomes a child of its parent ("Count an account in Puerto Rico or Guam", "Count an account of your employer you can sign for"), asked only after a No where the wrong No is likely. `sb.foreign_any` stays as a derived line | 5a |
| `div.any` (217) | Seven bullets saying what counts as a dividend | 272: "In 2025, did you own shares of a company or a fund (stocks, mutual funds, ETFs, a money market fund) outside a retirement account?" Asking what the person owns is wider than asking what they received, so the bullets on reinvested, nominee and constructive dividends become children of Yes | 5a |
| `ftc.taxes` (17; an amount in form words) | Foreign tax paid | 279: beneath the existing `s3.foreign_any`, with the paper cue (box 7 of Form 1099-DIV, box 6 of Form 1099-INT). Wrong No: an investor whose fund paid foreign tax and who does not know it; lane 5a adds the paper cue to the parent's help or keeps a separate paper question (Part 5, inference 5) | 5a |
| `f4952.has_interest` (204), `f4952.line4g` (83; via `f4952.bad_election`) | Investment interest; the election amount, asked of everyone though it needs investment interest | 277: "In 2025, did you pay interest on money borrowed to buy investments, such as a margin loan?"; the carryover by the 2024 paper (`f4952.carryover` exists); `line4g` gated beneath a Yes | 5b |
| `sd.carryover` (29) | A 2024 capital loss | 276: unchanged in substance; one sentence shorter | 5b |
| `f5695.part1_any` (143), `part2_any` (141) | Six kinds of clean energy property and a carryforward; twelve kinds of improvement | 230: one parent `f5695.any` ("In 2025, did you have work done on your home to save or make energy: solar panels, a battery, a heat pump, insulation, new windows or doors, a new furnace, boiler, water heater or air conditioner, or an energy audit?"), then the two existing questions as children, then theirs. The carryforward by the 2024 paper (Form 5695 line 16), a question of its own | 8b |
| `sli.interest` (244; an amount) | The amount, with what a qualified loan is | 240: parent `sli.any` ("Did you pay interest on a student loan in 2025?"), the amount beneath (box 1 of Form 1098-E), the qualifying rules as children | 8b |
| `f2441.care` (120; via `f2441.nondependent_gate`) | Three kinds of qualifying person | 155: "In 2025, did you pay someone to look after your child under 13, or a spouse or relative who could not care for themselves, so that you could work?" The third kind (not your dependent) is the existing child `f2441.nondependent` | 2b |
| `person.educator_expenses` (104; an amount asked of every person before `person.eligible_educator`) | The amount | 140: the order is turned round: `person.eligible_educator` first, in plain words ("Did you work in a school, kindergarten to grade 12, as a teacher, counselor, principal or aide?"), the amount beneath | 4b |
| `person.rrta` (23; direct), per person | Railroad retirement compensation; Form CT-2 | 140: "Did you work for a railroad in 2025?" | 3 |
| `s1.alimony` (95) | Alimony under a pre-2019 agreement; recapture | 160: parent `s1.alimony_any` ("In 2025, did you pay or receive alimony?"), child on the date of the agreement, then today's questions | 7b |
| `s1.uc_paid`, `gambling_winnings`, `line8g`, `8h`, `8i`, `8j`, `8r` (25 to 78 each; amounts), `refund.received` (62) | Amounts asked of everyone "zero if none" | 160: each becomes a yes or no parent in a person's words with the amount beneath (`s1.cod_any` is the pattern) | 7b; 7a (`refund`) |
| `f1040.line25b` (35), `line25c_other` (29), `line26` (15) | Withholding on Forms 1099; other withholding; estimated payments | 300: three plain parents, the amounts beneath | 1 |
| `household.married` (217) | Seven paragraphs on what counts as married | 100: 2.9, lane 1 | 1 |
| `person.blind` (119), per person | The definition | 110: one sentence and one parenthesis (Part 4.4, example 5) | 1 |
| `person.sav_trad` (52), per person | IRA contributions | 180: "Did you put money into a traditional IRA for 2025?" | 4b |
| `ssb.benefits` (15; an amount in form words) | Social security | 178: parent `ssb.any` ("Did you get social security or railroad retirement benefits in 2025?") | 4a |
| `sa.line1` (429), `line5a` (237), `line5b` (232), `line5c` (55), `line8a` (17), `sa.gifts` (292) | The amounts of Schedule A, asked of everyone | 200: see 2.10 | 7a |

### 2.9 Catch-alls inside one topic

The items stay in the lane that owns the question; the table gives the plain parents under which the lane puts them,
so that every item is named. A lane may regroup, but may not drop an item. "Per entry" questions are asked once for
each entry of a list. *Paper* means the item is asked as a box or code of the paper in hand.

| Question (words; refusal) | Asked of | Items, grouped under the plain parent each goes beneath | Lane |
|---|---|---|---|
| `household.married` (217; via the status conflict) | Everyone today, a couple included (T-286), though a couple's first answer already records the joint status: not asked of a couple (N8) | Parent "Were you married on December 31, 2025?". After a No: `household.ever_married` ("Have you ever been married?"); a No there ends the chain. After that Yes: divorced or separated by a final decree, annulled, or widowed. Children of the first Yes or of doubt: common-law marriage; a foreign or tribal marriage; a divorce not yet final; a registered domestic partnership (not a marriage); divorced only to file as unmarried | 1 |
| `household.unmarried` (318; via) | Head of household only | Parent "Were you unmarried on December 31, 2025?" (already known from the chain above: do not ask again). The considered-unmarried test as five children: lived apart the last six months; separate return; paid over half the cost of the home; the home was the child's main home over half the year; can claim the child (or the noncustodial exception). A nonresident alien spouse: a child of its own | 1 |
| `household.qss_eligible` (370; via) | Qualifying surviving spouse only | Five tests, each a question: the year of the death and no remarriage; a child or stepchild you can claim (with the three exceptions as children); the child lived with you all year (absences, birth, death, kidnapping as children); over half the cost of the home (the same child as `household.home_cost`); could have filed jointly in the year of the death | 1 |
| `household.home_cost` (118) | Head of household | "Did you pay more than half of what it cost to run your home in 2025?"; what counts and what does not, in a child asked on "not sure" (Part 4.5) | 1 |
| `dependent.relationship` (297; an enum of 8) | Per dependent | Plain labels for the eight values (`value_labels`); the adopted, foster and "in your care" rules as children of `child`; the two closing paragraphs as children of `household_member` and `other` | 2a |
| `dependent.supported` (559), `dependent.self_support` (240) | Per dependent, by relationship | Parent in one line ("Did you pay for more than half of this person's living costs in 2025?"). Children, asked only where the answer is not plain: income of their own; lodging and its value; public assistance; a foster child; a home for the aged; capital items; military allotments; social security spent on support; a scholarship. Ask the cheap exits first (N4): a child with no income who lived with you all year needs none of them | 2a |
| `dependent.months` (178), `qr_all_year` (156), `us_half` (155), `part_year_home`, `absence_no_return` | Per dependent | Parent "Did this person live with you all of 2025?"; a No asks the months; temporary absences, a birth, a death, an adoption, a kidnapping each a child (`dependent.born_died`, `placed`, `kidnapped` exist and move up as the parents of these rules) | 2a |
| `dependent.parent_home_paid` (170) | A parent listed for head of household | One line; the cost list shared with `household.home_cost` | 2a |
| `dependent.student` (136), `disabled` (56), `married` (62; direct), `joint_return`, `divorced_rule` (107; direct), `multiple_support`, `other_claimant` (via), `other_nontaxpayer` (89), `kidnapped` (74; via) | Per dependent | Each one subject already; reworded short. `married` joins two questions (married; on a joint return): split, the second being `joint_return`. `divorced_rule`: parent "Do this child's parents live apart?", child on the release (Form 8332), which refuses | 2a |
| `dependent.dc_paid` (529; an amount) | Per person cared for | Parent amount in one line ("What did you pay in 2025 for this person's care so that you could work?"). Children by yes or no: care paid for another year; overnight camp, school or tutoring; a provider who is your spouse, your child under 19 or your dependent; household services and meals; reimbursements; part-year work. Model change in `dependent.yaml`, so built by lane 2a at lane 2b's request (Part 3) | 2b words, 2a builds |
| `f2441.nondependent` (114; via), `student_disabled` (55; direct), `paid_2026` (86), `dcprov.related` (78), `dcprov.tin_kind` (107), `dcprov.household` (54) | Care topic | `student_disabled` joins two subjects (student; unable to care for oneself): two questions. `dcprov.related` lists four kinds of provider: plain labels or four children. `tin_kind`: plain labels | 2b |
| `household.credit_disallowed` (71) | Reached with the child credits or the EIC | Parent "Has the IRS ever reduced or refused your child tax credit or earned income credit, other than for an arithmetic error?"; the years and the ban as children | 2b |
| `otjob.method` (158; via), `otjob.statement` (126), `otjob.flsa`, `special_rule` | Per employer with overtime | Parent by the paper: "Does box 14 of this W-2, or a statement from this employer, show your qualified overtime?"; the three ways of figuring it as children of a No | 3 |
| `tipjob.qualified` (72; via), `tipjob.amount` (72) | Per employer with tips | Four tests in one sentence (listed occupation; cash; voluntary; not negotiated): four children, the occupation first | 3 |
| `carloan.requirements` (174), `vehicle` (86), `refi_whole` (95; via), `kind` (72), `mixed`, `down` | Per loan | Five tests in one sentence, each a child, cheapest exit first: bought new in 2025 (not leased); for personal use; the lender is not a relative; first lien; then the refinancing and inheritance cases as children of `kind` | 3 |
| `retirement.special` (411; direct), `early_screen` (101; via), `code_screen` (90; via) | Per Form 1099-R | **Paper:** an amount in box 6 (employer securities); a Form RRB-1099-R; box 7 codes that the `code` choice "other" already refuses (corrective distributions, returned contributions, a plan loan offset, a nonqualified annuity). **Where the money went** ("Did any of it go into a Roth account?": conversion, Roth rollover, recharacterization; "straight to a charity or into a health savings account?"; rolled-over property other than cash and a domestic-relations rollover as children of `retirement.rollover` above zero; an IRS levy returned). **Why it was paid:** disability (children of code 3: before minimum retirement age; a terrorist attack; a military disability pension); death (children of code 4: death benefit exclusion; beneficiary of an employee who died before retiring, guaranteed payments, a shared annuity). **Who you are:** a retired public safety officer paying insurance premiums from the pension; born before January 2, 1936 (the lump-sum Form 4972); a federal civil service annuity under the alternative option. **The IRA's history:** nondeductible contributions ever made (asked only of an IRA). **The annuity:** a lump payment at or after the start; a start before November 19, 1996, or the General Rule (children of `retirement.annuity`). **A disaster:** one child. **`early_screen`:** modified equal payments; an annuity or endowment contract; repaying a birth, illness, abuse or emergency distribution; a second emergency distribution; a long-term care distribution at year end; more than one exception: children of an early code only. **`code_screen`:** two children of code 2 and of codes 7 and 4 | 4a |
| `retirement.exception` (409; an enum), `exc_amount` (141) | Early distributions | Plain labels for the exceptions, the common ones first (separated from service at 55; disability; medical; education; first home; birth or adoption); each exception's conditions a child of choosing it | 4a |
| `retirement.rollover` (239), `annuity` (141), `months` (60) | Per Form 1099-R | Parent "Did you put any of this money back into a retirement account within 60 days?"; the amount; the exclusions as children. `annuity`: four tests, by the paper first (an amount in box 9b) | 4a |
| `ssb.pub915` (62; direct), `terror_disability` (61; direct), `lump_sum` | With benefits | `pub915` has six items: IRA contribution with a workplace plan (a fact the IRA questions already ask: read it from them, N8, or ask after them); repayments over benefits (paper: box 4 over box 3); Form 2555 or 4563 and Puerto Rico (`sa.excluded_income`); Form 8815 (a child beneath savings-bond interest in lane 5a's `sb.unsupported`); adoption benefits (`scope.adoption_benefits`) | 4a |
| `person.ira_excess` (110; via), `ira_basis_adjusted` (82; via), `ira_dist` (50; via), `ira.special` (93; via) | IRA contributors | `ira_excess`: three items (over the limit and not withdrawn; recharacterized; an earlier excess, shared with `x_other`). `ira_basis_adjusted`: four items, each a child beneath "Have you ever filed Form 8606?". `ira.special`: deferred compensation (paper: W-2 box 11 or code Z), graduate fellowship not on a W-2, reservist repayment (`scope.reservist_repaid`), difficulty-of-care payments | 4b |
| `person.sav_prior_joint` (131), `sav_prior_other` (145), `sav_student` (71), `sav_able`, `sav_excess` (47; via) | Saver's credit, computed gate | Parent "Did you take money out of a retirement account in 2023, 2024, 2025 or early 2026?"; the nine exclusions as children of Yes | 4b |
| `sb.unsupported` (45; via) | With interest income | Nine items, by the paper where one exists: nominee interest; original issue discount not as on Form 1099-OID; accrued interest paid on a bond bought between payments; bond premium (Form 1099-INT boxes 11 to 13); market discount; a contingent payment debt instrument; seller-financed mortgage interest ("Did you sell a home and lend the buyer the money?"); the savings bond exclusion for education (Form 8815); "other special treatment" (residual: lane 5a closes it from the Schedule B instructions). Parent: "Do you own bonds, or did you lend money to a person?"; a No skips all but nominee interest | 5a |
| `sb.line8` (204; via), `sb.form5471` (109; via) | After the foreign parents | Each joins several roles (received from, set up, gave to a foreign trust; officer, director, 10% owner): one child per role | 5a |
| `sales.special` (171; direct), `sales.code` (106; via), `sales.box` (689; via), `aggregate_eligible` | Per sale | `special`: five items, as one parent ("Was this sale of something other than ordinary shares, fund units, bonds or crypto?") and children: collectibles (including a gold or silver fund); qualified small business stock; real estate that was depreciated; an interest in a partnership, S corporation or trust; a qualified opportunity fund. `code`: plain labels. `box`: see 2.10 | 5b |
| `f4952.unsupported` (87; direct) | With investment interest | Seven items: interest tied to royalties, a business, a passive activity, tax-exempt income, an activity not at risk; another deductible investment expense; other investment income. The first, second and third are `scope.rental`, `$sc`, `scope.passive`; the rest three children | 5b |
| `f8960.unsupported` (152; direct), `f8960.refund` | Above the income threshold | Thirteen items; nine are deleted as already asked (2.7: rental, royalty, business, pass-through, CFC, PFIC, section 911, net operating loss; `retirement.special` for employer securities; `sb.unsupported` for Form 8815). Left as children: a life insurance contract surrendered or sold; ESOP dividends; another investment expense; an annuity (not from a retirement plan); the carryforward adjustment (`f8960.prior_2i` exists) | 5b |
| `clcw.spouse_screen` (69; direct) | With a 2024 loss | Two items: the 2024 return was joint and this one is not with the same spouse; both spouses had separate 2024 losses | 5b |
| `sc.special` (267; via `sc.screened`) | Per business | Twenty items. Deleted as already asked: chapter 11; Medicaid waiver payments; not a business or a hobby (`s1.line8j` asks hobby income; keep one child "Is this a real business run for profit?"). **Employees** (beneath "Did this business have employees?", which also gates `sc.line14`, `19`, `26`, `37`): employment credits; a dependent care plan for yourself. **What the business does** (plain facts, each a child of a parent "Is this business in any of these lines: mining, oil, gas or timber; building owner; recording; shipping or fishing with a construction fund; export?"): depletion; commercial building deduction; sound recording costs; capital construction fund; extraterritorial income. **Unusual accounting:** installment method; research costs capitalized; licenses to amortize; business interest limited (Form 8990). **History:** recapture of depreciation or section 179, lease inclusion; passive losses of earlier years (a child of `sc.passive`); services to a former employer. **Other:** Form 1099-PATR amounts (paper); luxury water travel (a child of `sc.line24a` above zero); an LLC taxed as a corporation | 6a |
| `sc.hi_screen` (92; via), `ho_other` (105; via), `method_other` (78; via), `at_risk` (126; via), `passive` (100; via), `inventory_other` (45; direct) | Per business | `hi_screen`: six items; Marketplace insurance is known from `$f1095a` (N8); Form 2555 deleted; S corporation shareholder is `scope.k1`; the others three children. `ho_other`: eight items, each a child of `sc.ho_uses` = Yes. `method_other`: five items; the cheap parent is "cash or accrual, unchanged in 2025?". `at_risk`: parent "Did you borrow to fund this business from someone with a stake in it, or on terms that protect you from loss?" | 6a |
| `person.se_screen` (146; via), `plan_screen` (99; via) | Per person with a business | `se_screen`: nine items; five deleted (2.7); left: an approved Form 4361 or 4029; director's or fiduciary fees not on a Schedule C; the optional method; exempt income (a foreign social security agreement or a foreign government employer). Community income on a separate return cannot occur (separate returns are refused): deleted (N8). `plan_screen`: seven items, reached only with a SEP or SIMPLE: kept as one question in shorter words, bank only (a split needs `person.yaml`, lane 4b) | 6a |
| `scveh.screen` (732; via) | Per vehicle | **How you got it:** a trade-in or from a relative; an exchange or involuntary conversion; acquired before September 28, 2017; not new to you, with the special allowance. **Before 2025** (children of a year before 2025 in `scveh.placed`, which already refuses a year before 2019: that item and "an electric vehicle before 2007" are deleted): a special allowance earlier; the mileage rate earlier; business use 50% or less in an earlier year; a substantial improvement; basis reduced by a credit, a deduction or a casualty; a short tax year. **In 2025:** sold or disposed of; converted to or from personal use. **How it is used:** for investment; carrying people or goods for hire; leased to others or a leasing business; used by a tax-exempt body, a government or a foreign person; mostly outside the United States (ADS); qualified business use 50% or less (four excluded uses as children). **Records:** no adequate record of business use. **Special allowance:** the electricity and floor-plan exclusions, children of claiming it | 6b |
| `asset.screen` (843; via), `asset.not179` (149; via), `asset.listed` (81; via) | Per item of property | **What it is** (most settled by `asset.class`; make these values or children of the class): a building; a vehicle; film or recording; software; land clearing; recycling property; long-production property or aircraft; the six named special classes; listed property used 50% or less. **How you got it:** exchange or involuntary conversion; before September 28, 2017; not new to you, with the special allowance. **The method:** ADS required (four cases as children) or elected; another method; a general asset account; amortized. **History** (children of a year before 2025 in `asset.placed`, which already bounds 2005 to 2025: "before 2005" is deleted): disposed of or converted; basis changed other than by depreciation; basis reduced by one of seven credits or deductions; business use changed; a short tax year. **Where and by whom:** mostly outside the United States; tax-exempt use | 6b |
| `asset.s179` (271), `asset.class` (198), `scveh.suv` (87), `scveh.passenger` (57), `smr_ok` (62) | Per entry | `s179`: the amount in one line; what qualifies is already asked by `asset.not179` (N8): delete the repeated lists. `class`: plain labels, the common classes first (computer, office furniture, tools and machinery) | 6b |
| `gift.special` (140; direct), `gift.deduction` (75), `gift.public_securities` (86) | Per group of property given | Nine items: over $5,000; through a K-1 (deleted); vehicles; pass-through interests; intellectual property; inventory; conservation or partial interests; restricted property; clothing or household item over $500 not in good condition. Parent: "Is this group ordinary used clothing or household goods worth $5,000 or less in all?"; a Yes skips them | 7a |
| `refund.exc_tax` (109; direct), `exc_who` (57; direct), `not_2024` (63; direct), `box8` (48; direct) | With a refund, after itemizing in 2024 | `exc_tax`: four items read from the 2024 return (alternative minimum tax; unused credits; no tax on line 16; refund over the deduction), each by its line. `exc_who`: three items (a dependent in 2024; Form 1040-NR in 2024; a joint state return with someone else). `not_2024`: two. Ask `refund.itemized` **before** the amount (90% leave there) | 7a |
| `s1.alimony_unsupported` (158; direct), `cod_unsupported` (150; direct), `uc_unsupported` (70; direct), `oi8z.kind` (183; via) | After their parents | `alimony_unsupported`: three items (more than one agreement or person; recapture; partly child support, home payments or payments after death). `cod_unsupported`: seven items; the cheap parent is "Was it a credit card or personal loan you alone owed, canceled without bankruptcy?". `uc_unsupported`: two (contributions to a state fund; repaid benefits of an earlier year). `oi8z.kind`: plain labels | 7b |
| `f8962.other` (357; direct), `alloc` (65; direct), `premium_adjust` (108; direct), `married_in_2025` | With a Form 1095-A | `other`: eight items. Parent for the largest: "In any month of Marketplace coverage, could anyone covered have had other health coverage: a job's plan, Medicare, Medicaid, CHIP, TRICARE or veterans' care?" (nine kinds as children). Questions of their own: not lawfully present; a QSEHRA or individual-coverage HRA (paper: W-2 box 12 code FF); premiums unpaid; advance payments for someone in no tax family; a Medicaid finding reversed; incarceration. `alloc`: two items (a policy shared with someone outside the family; divorced during the year) | 8a |
| `f1095a.uniform` (198), `b_counted` (74), the 36 monthly amounts | Per Form 1095-A | `uniform` ("are the twelve months the same?") is the off-ramp for the monthly questions: cut to one line; the column B corrections become children | 8a |
| `f5695.joint_occupancy` (120; direct), `construction_later` (46; direct), `line5a` (128), `line26a` (131), `business_use` | With home energy work | Each one subject; the conditions repeated from the parent are deleted (N8) | 8b |
| `person.edu_inst`, `dependent.edu_inst` (157 each), `edu_1098t` (98), `f8863.ban` (80; via) | Per student | The amount by the paper (Form 1098-T box 1, corrected); the nine exclusions as children. Twins: the same change to both, in one commit, in the bank only | 8b |

### 2.10 Long questions that are definitions, not lists of refusals

These ask one thing and then define it at length. The remedy is the same for each (N4, N10): the first line asks the
thing in a person's words; the answer most people give needs nothing more; each rule a rare answer needs becomes a
child reached from that answer, never help text.

| Question (words) | Asked of | The first line, and what goes beneath | Lane |
|---|---|---|---|
| Schedule A: `sa.line1` (429), `line5a` (237), `line5b` (232), `line5c` (55), `line8a` (17), `sa.gifts` (292), `sa.elect_itemize` | Everyone, about 1,400 words | Four plain parents in this order (cost per chance of leaving): `sa.home_owner` ("Did you own your home in 2025?"; a Yes asks mortgage interest by the paper, Form 1098 box 1, and property tax; `s3.mcc` and `s2.mortgage_subsidy` hang here); state income tax (a parent that names the paper: W-2 box 17 and any estimated payments); `sa.gifts` in one line ("Did you give money or things to a charity in 2025?"); `sa.medical_any` ("Did you pay medical or dental bills in 2025 that insurance did not cover and that came to more than 7.5% of your income?", the amount and its 16 rules beneath). Whether the whole block can sit beneath one question is Part 5, question 1 | 7a |
| `sales.correct_basis` (906), `sales.box` (689), `sales.wash_loss` (346), `sales.proceeds` (118) | Per sale | By the paper first: "Does a Form 1099-B report this sale?", then its box (A, B, D, E), which settles `box` for most sales; "Is the basis the form shows right?" (a Yes skips `correct_basis` entirely); "Does the form show a wash sale loss (box 1g)?". The rules on gifts, inheritances, trades, options, short sales and bonds are children of "How did you get what you sold?" (bought it; a gift; an inheritance; from a spouse; for work; another way) | 5b |
| `s1.alimony_paid` (297), `alimony_received` (289) | Pre-2019 alimony | The amount in one line; two lists of ten rules as children of "Was all of it paid in money straight to your former spouse?" | 7b |
| `ltc.payments` (250), `sc.f7206_line1` (112), `sc.hi_uses` (86) | A business with health or long-term care insurance | The amount in one line; the five tests of a qualified contract as a child of a No to "Is it a policy sold as tax-qualified long-term care insurance?" | 6a |
| `sc.line24a` (214), `meals_100` (173), `meals_50` (135), `meals_80` (73), `line23` (145), `line21`, `line22`, `line16b`, `line1` (93) | Per business | The 30 expense amounts are asked of every business. Three parents cut them for the common sole proprietor: "Did this business have employees?" (lines 14, 19, 26, 37, `meals_100`'s employee parts); "Did it buy or make goods to sell?" (lines 35 to 41, `inventory_other`); "Did you travel overnight or pay for business meals?" (24a and the three meals lines). Each remaining amount keeps one line; its exclusions are children of an amount above zero | 6a |
| `f8889.medical` (166) | Redesigned topic | Not reopened (T-288) | none |
| `person.edu_a2025` (78), `edu_line24` (54), `edu_half_support` (71) and their twins | Per student | One line each; rules as children | 8b |
| `otjob.statement` (126), `carloan.down` (63), `w2.box2` (40) | Per entry | One line each. `w2.box2`: the territory rule becomes a child of `f8959.territory_w2` | 3 |
| `f1095a.in_b_*`, `mo_b` (101 to 109) | Per form and month | One line; the correction rule once, as a child of "Is column B blank or wrong for any month?" | 8a |

**Counts.** Part 2 covers 184 of today's questions (25,814 of the 42,600 prompt words), 72 of them over 120
words. The seven questions of 2.1 to 2.6 have 80 rows of items; 22 rows are already caught by another question, and
the rest name 47 new `scope.*` inputs and 21 new inputs in lane 7b's files. 2.7 gives 21 facts one asker each. The rows of 2.9 name every item of
their questions by a keyword; the lanes confirm each row against the full text (Part 5, inference 8).

---

## Part 3. The lanes

Nine lanes, six of them in two halves: fifteen units of work, no two of which own the same form file. Each half is
sized for one agent in one session (the limit taken from the earlier lanes: about 30 questions with model changes).
If only nine agents run, one agent takes both halves of a lane and works the two ranked lists as one, the *a* half
first; it will not finish the tail, and the lists are ranked so that the tail is what matters least.

**Owning a form file** means being the only lane that edits it. **Owning a bank entry** means being the only lane
that edits that question's `order`, `seq`, `prompt`, `help` and labels in `interview/2025/questions.yaml`. The two
differ for a few questions, listed under "bank only": the lane rewrites the words in the bank and leaves the model to
the file's owner.

**Every lane's first two steps, before its ranked list** (they are cheap and they are what makes the order whole):
(a) give every one of its bank entries its new `order` (Part 1) and a `seq`; (b) delete the help "Married filing
separately and unsupported items are refused with citations." wherever it stands (213 questions carry it; T-266).

Sizes are today's: questions, prompt words, questions over 120 words, and how many of the lane's questions the minimal
return is asked (with their words).

| Lane | Form files owned | Bank entries | Size today |
|---|---|---|---|
| 1 Who, household, payments | `household`, `f1040` | Those files' (not `f1040.line3a`, `tax_exempt_interest`, `household.credit_disallowed`); bank only: `person.under16`, `age65`, `blind`, `died_before_65`, `sa.dependent`, `sa.excluded_income` | 21 q, 1,509 w, 3 long; 13 asked of everyone (568 w) |
| 2a Dependents | `dependent` | `$dependent`, `dependent.*` except `dc_*`, `edu*`, `ptc_*` (31) | 31 q, 3,174 w, 8 long; 1 of everyone |
| 2b Care, and the credits for a family | `f2441`, `dcprov`, `s8812`, `eic` | Those files'; bank only: `dependent.dc_*` (4), `w2.box10`, `box10_wages`, `household.credit_disallowed`, `person.tin`, `work_ssn`, `itin_applied`, `eic_ssn`, `born_after_1960`, `born_before_2001` | 37 q, 2,189 w, 2 long; 3 of everyone (239 w) |
| 3 Jobs, tips, overtime, the car loan | `w2`, `tipjob`, `otjob`, `s1a`, `carloan` | Those files' except `w2.box10*`; bank only: `person.rrta` | 45 q, 1,800 w, 3 long; 5 of everyone (189 w) |
| 4a Retirement income, social security | `retirement`, `ssb` | Those files' | 28 q, 2,212 w, 5 long; 2 of everyone |
| 4b Saving for retirement; `person.yaml` | `person`, `ira`, `f5329`, `f8606`, `f8880` | `person.ira_*`, `sav_*`, `x_*` (not `x_hsa_value`), `educator_expenses`, `eligible_educator`, `ira.*` | 26 q, 1,492 w, 3 long; 3 of everyone (292 w) |
| 5a Interest, dividends, foreign tax and accounts | `interest`, `div`, `sb`, `ftc` | Those files'; bank only: `f1040.line3a`, `f1040.tax_exempt_interest`, `qbi.dividends` | 32 q, 1,850 w, 3 long; 4 of everyone (1,080 w) |
| 5b Sales, carryovers, investment interest | `sales`, `sd`, `sdtw`, `u1250`, `g28`, `clcw`, `clcw26`, `f4952`, `f8960`, `qdcg` | Those files' | 31 q, 3,481 w, 6 long; 5 of everyone (391 w) |
| 6a The business | `sc`, `ltc`, `qbi`, `se`, `f8995`, `f8995a` | Those files' except `qbi.dividends`; bank only: `person.plan`, `plan_screen`, `se_screen`, `sep_*`, `simple_*` (9) | 63 q, 4,020 w, 8 long; 3 of everyone (154 w) |
| 6b Business vehicles and equipment | `scveh`, `asset`, `s179`, `f4562`, `mq` | Those files' | 43 q, 3,716 w, 5 long; 1 of everyone (77 w) |
| 7a Home, deductions, the state refund | `sa`, `gift`, `refund` | Those files' except `sa.dependent`, `sa.excluded_income` | 33 q, 2,316 w, 5 long; 9 of everyone (1,405 w) |
| 7b Other income, other taxes | `s1`, `oi8z`, `s2`, `f8959` | Those files'; order only: `s3.*` (26, redesigned) | 25 q, 2,150 w, 6 long; 14 of everyone (862 w) |
| 8a Marketplace insurance | `f1095a`, `f8962` | Those files'; bank only: `dependent.ptc_files`, `ptc_magi`; order only: `$f8889`, `f8889.*`, `person.x_hsa_value` (32, redesigned) | 53 q, 3,686 w, 3 long; 1 of everyone (45 w) |
| 8b Education, student loans, home energy | `f8863`, `aqee`, `sli`, `f5695` | Those files'; bank only, both twins in one commit: `person.edu*` (18), `dependent.edu*` (14) | 91 q, 4,475 w, 8 long; 4 of everyone (565 w) |
| 9 The scope screens | `scope` | `scope.*` and every new `scope.*` question of 2.1 to 2.3 | 3 q, 663 w, 3 long; 3 of everyone (663 w); 47 new inputs |

Form files with no question (`tcw`, `tax_on_amount`) and the two redesigned files `s3` and `f8889` have no owner: no
lane edits them. A change one of them needs is a request to the coordinator.

### Order numbers inside a shared range

No two lanes use the same order number (a block's `seq` belongs to one lane). Where a topic's range holds several
lanes' questions, these are the slots; a lane that needs more asks the coordinator.

| Range | Slots |
|---|---|
| 110–119 | 110–112 lane 1; 113–117 lane 9; 118 lane 7b (`s3.disability_retired`) |
| 120–129 | 120–125 lane 2a; 126 lane 7b (`s3.adoption*`, order only); 127–128 lane 9 |
| 140–149 | 140–143 lane 3; 144 lane 4b (educator); 145–147 lane 9; 148–149 lane 7b |
| 155–159 | 155–157 lane 2b; 158 lane 9; 159 lane 7b |
| 160–169 | 160–164 lane 7b; 165–167 lane 7a (`refund`); 168 lane 9 |
| 170–177 | 170–174 lane 4a; 175 lane 9; 176 lane 7b; 177 lane 4b |
| 180–189 | 180–186 lane 4b; 187 lane 9 |
| 190–194 | 190 lane 8a (order only); 191 lane 9; 192 lane 4b; 193 lane 7b |
| 200–219 | 200–214 lane 7a; 215 lane 7b (`s3.mcc`, `s2.mortgage_subsidy`); 216 lane 5b |
| 240–249 | 240–246 lane 8b; 247 lane 4b; 248 lane 9 |
| 259–269 | 259–264 lane 6a; 265–266 lane 9; 267–269 lane 7b |
| 274–278 | 274, 276, 277, 278 lane 5b; 275 lane 7b |
| 279–284 | 279 lane 7b (`s3.foreign_any` and its children, order only: it must come before `ftc.taxes`); 280–283 lane 5a; 284 lane 7a |
| 285–289 | 285–286 lane 5a; 287–289 lane 9 |
| 290–299 | 290–294 lane 7b; 295–299 lane 9 |
| 300–309 | 300–304 lane 1; 305 lane 7b (`s3.line10`) |
| 310–319 | 310–313 lane 2b; 314 lane 2a; 315 lane 4b; 316 lane 3; 317 lane 4a; 318 lane 7b (`s3.elderly_credit`) |

Every other range belongs to the one lane Part 1 names.

### `person.yaml` and `dependent.yaml`

- **`person.yaml` belongs to lane 4b**, which has the most model work in it (`x_other`, the IRA and saver's credit
  questions, the educator pair). The other lanes' needs in it are met **without editing it**: lanes 1, 2b, 3, 6a and
  8b reword their `person.*` questions in the bank (`prompt` overrides the line's label; the label stays as the
  source-faithful statement, as the credits lane did for `s3.ev`). Lane 6a shrinks `person.se_screen` by deleting
  items already asked (2.7), which is also bank only. New per-person facts that lanes 1 and 9 need are asked per
  return with the spouse phrase and declared in their own files, not in `person.yaml`.
- **`dependent.yaml` belongs to lane 2a.** Lane 2b rewords `dependent.dc_*` and lane 8a `dependent.ptc_*` in the
  bank. The one model change another lane needs is the split of `dependent.dc_paid`: lane 2b writes the wanted parent
  and children in its notes, and lane 2a builds them as the last item of its list.
- **The twins** (`person.edu*` and `dependent.edu*`; `tools/check_twins.py`, `reviews/2025/twins.json`): lane 8b
  changes both bank entries of a pair in one commit, with identical `prompt`, `help` and `seq` and the same `order`;
  neither form file changes, so lanes 4b and 2a must leave the `edu*` lines of their files untouched. A model change
  to a twin is not made in this redraft.

### Ranked work lists

Each row: the change, the share of filers who meet the question (*gf* or *est.*), and my estimate of today's and the
proposed cost of the typical answer on the owner's scale. The dozen that matter most across the whole interview are
marked ★ with their rank.

**Lane 1.** Receives: nothing to build from Part 2 (the new facts of topic 110 are lane 9's inputs, placed in lane 1's
range, in the slots tabled above; lane 1 reads their words for register).

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★8 | `household.married` (217 w): never asked of a couple; for the others the three-step chain of 2.9 (`household.ever_married` is the married-at-some-time fact T-286 and BUG-0618 need) | 63% not joint (*gf* `married`) | 10 → 2 |
| 2 | `sa.excluded_income` and `sa.dependent` reworded and moved to 110 | 100% | 20 + 5 → 2 + 1 |
| 3 | `f1040.line25b`, `line25c_other`, `line26`: a plain parent over each ("Was federal tax taken out of any payment other than wages: a pension, social security, unemployment, interest or gambling winnings?"); placed at 300 | 100%; 21%, small, 6.6% say yes (*gf*) | 3 × 3 → 3 × 1 |
| 4 | `person.blind` (119 w), `age65`, `under16`, `died_before_65` in the register of Part 4.4 | 100% | 5 → 1 |
| 5 | `household.unmarried` (318 w), `qss_eligible` (370 w), `home_cost` (118 w) split as 2.9; a filer entitled to head of household who chose "None of these" is told (T-286) | 14% est. (head of household, surviving spouse) | 20 → 6 |
| 6 | `household.community_property`, `cp_married`, `rdp`: one line each | 63% | 2 → 1 |

**Lane 2a.** Receives: `scope.child_investment_income` and `scope.adoption_benefits` are placed in 120 by lane 9; add "Count costs your employer paid." to the help of
`s3.adoption_any` by request to the coordinator (`s3` has no owner); `dependent.dc_paid` split for lane 2b.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 | `$dependent` as a plain question ("Did children, or anyone else you support, live with you or depend on you in 2025? List each one.") | 100%; 29% list someone (*gf*) | 5 → 1 |
| 2 | The order of the tests so that the ordinary child (your own child, under 17, lived with you all year, no income) leaves after relationship, age and "lived with you all year": N4 | 29% | per child 30 → 6 |
| 3 | `dependent.relationship` (297 w): plain labels, rules as children | 29% | 5 → 1 |
| 4 | `dependent.supported` (559 w), `self_support` (240 w): one line, children | A relative or an older child: 8% est. | 15 → 3 |
| 5 | `dependent.months` (178), `qr_all_year` (156), `us_half` (155), `parent_home_paid` (170), `student` (136) | 29%, in part | 5 each → 1 each |
| 6 | `divorced_rule`, `married`, `other_claimant`, `other_nontaxpayer`, `kidnapped`, `tin`, `work_ssn` short | 29% | 3 each → 1 each |
| 7 | The `dependent.dc_paid` children for lane 2b | 4.5% (*gf* `care_expenses`) | 15 → 3 |

**Lane 2b.** Receives: `scope.care_benefits_other` beneath `f2441.benefits` (lane 9 builds it; lane 2b **must** widen
the words of `f2441.benefits` as 2.2 item 5 says); `s2.household_employee` is placed in 155 by lane 7b.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 | `f2441.care` (120 w) and `f2441.benefits` (41 w) as the plain parents of 2.8 | 100%; 4.5% and 1.2% say yes (*gf*) | 5 + 3 → 1 + 1 |
| 2 | `person.eic_ssn` (78 w), `dependent.eic_ssn`, `person.tin`, `work_ssn`, `itin_applied`: by the paper ("Does your social security card say 'Not valid for employment'?") | Low earners: 15% est. | 5 → 1 |
| 3 | `dependent.dc_paid` (529 w) parent line; `dc_under13`, `dc_incapable`, `dc_over12_care` short | 4.5% | 15 → 3 |
| 4 | `dcprov.*`, `f2441.nondependent`, `student_disabled`, `paid_2026`, `line13`, `line14`, `plan_max` | 4.5% | 3 each → 1 each |
| 5 | `eic.*`, `s8812.*`, `household.credit_disallowed` in a person's words | 15% est. | 3 each → 1 each |

**Lane 3.** Receives: lane 9's and lane 7b's W-2 questions (`scope.statutory_employee`, `scope.pay_no_w2`,
`scope.religious_work`, `scope.medicaid_waiver`, `scope.other_earned`, `scope.performing_artist`,
`scope.fee_official`, `scope.code_h_deduction`, `s2.w2_marks`, `s2.w2_code_z`, `f8959.territory_w2`,
`s1.stock_options`, `s1.inmate_wages`) are placed in 140 after the W-2 boxes, in the slots tabled above. The educator pair is lane 4b's, at 144.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 | `s1a.tips` (52 w), `s1a.overtime` (42 w), `s1a.carloan` (40 w): ask the fact ("Did you get tips at work in 2025?", "Were you paid overtime?", "Did you take out a loan in 2025 to buy a new car?"), the wish to deduct beneath | 100% asked; 2%, 15%, 3% say yes (*gf*) | 5 + 5 + 3 → 1 + 1 + 1 |
| 2 | `$w2` (32 w, help 84 w): "Which employers gave you a W-2 for 2025?"; the box questions named by box and plain label ("Box 5, Medicare wages") | 79% (*gf*) | 5 → 2 |
| 3 | `person.rrta`: "Did you work for a railroad in 2025?" | 100% | 5 → 1 |
| 4 | `otjob.method` (158 w), `otjob.statement` (126 w): by the paper, as 2.9 | 15% | 15 → 4 |
| 5 | `tipjob.qualified`, `tipjob.amount` | 2% | 10 → 4 |
| 6 | `w2.box12_any` and the ten code amounts: one question that names the codes on the paper, placed at 310 | Saver's credit candidates: 20% est. | 5 → 3 |
| 7 | `carloan.*` (12 questions; `requirements` 174 w) | 3% | 20 → 8 |

**Lane 4a.** Receives: `scope.disaster_distribution` and `s1.nqdc_pension` are placed in 170 by lanes 9 and 7b;
`person.rmd_due` by lane 4b. Form 4972 (2.3 item 6) is now asked only here.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★10 | `retirement.special` (411 w, per form) split as 2.9; an ordinary pension or IRA payment meets three or four short questions | 24% (*gf*), about 1.5 forms each | 15 → 4 per form |
| 2 | `ssb.benefits` beneath `ssb.any`; `ssb.pub915` split (four of six items are asked elsewhere) | 100%; 20% say yes (*gf*) | 3 → 1; 15 → 3 |
| 3 | `$retirement` as a question ("Did you take money from a pension, an annuity, a 401(k) or an IRA in 2025? A Form 1099-R reports it.") and `account`, `code` with plain labels | 100%; 24% | 3 → 1; 5 → 2 |
| 4 | `retirement.rollover` (239 w), `annuity` (141 w) and the Simplified Method questions by the paper (box 9b) | 24%; annuity 8% est. | 10 → 3 |
| 5 | `retirement.exception` (409 w), `exc_amount`, `early_screen`, `code_screen` | Early distributions: 3% est. | 20 → 6 |

**Lane 4b.** Receives: `scope.reservist_repaid` and (if lane 9 finds it in the line 1h instructions) an excess
401(k) deferral question are placed in 180 by lane 9. Does the model edits of `person.yaml` that this map asks for
and no others.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★6 | `person.x_other` (136 w, per person) split as 2.8: `person.ira_owner`, `person.x_edu_account`, `person.rmd_due` as the parents | 100% | 15 → 4 |
| 2 | The educator pair turned round (2.8); placed at 144 | 100%; 2.4% (*gf*) | 5 → 1 |
| 3 | `person.sav_trad` (52 w) and `ira_trad` (73 w) in one line each; `ira_work_plan` by the paper (W-2 box 13) | 100%; 8% (*gf*) | 2 → 1 |
| 4 | `person.ira_excess`, `ira_basis`, `ira_basis_adjusted`, `ira_dist`, `ira.special`, `ira.deduct_less` beneath `person.ira_owner` and the contribution | 8% | 10 → 4 |
| 5 | `person.sav_*` (11) and `retirement.sav_*` words; the parent of 2.9 over the two prior-distribution amounts | 20% est. | 10 → 4 |

**Lane 5a.** Receives: the bullet on a child's accounts leaves `sb.foreign_any` (2.7); `scope.foreign_shares` and its
children are placed in 285 by lane 9 after lane 5a's four parents (lane 5a uses 285 and 286; 287 to 289 are lane 9's).

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★3 | `sb.foreign_any` (827 w) into four short parents (2.8) | 100%; 2.5% (*gf*) | 20 → 5 |
| 2 ★11 | `div.any` (217 w) as the ownership question; `ftc.taxes` beneath `s3.foreign_any` | 100%; 21% (*gf*) | 5 + 5 → 1 + 0 |
| 3 | `$interest` (help 104 w): "Which banks or others paid you interest in 2025?"; `sb.unsupported` beneath "Do you own bonds, or did you lend money to a person?" | 100%; 34% | 3 → 1; 20 → 2 |
| 4 | The 1099-DIV box questions named by box and plain label; `div.basis_reconciled` (84 w) | 21% | 3 each → 1 each |
| 5 | `sb.line8` (204 w), `sb.form5471` (109 w), `fbar_required`, `form8938`, `ftc.*` | 2.5% | 20 → 8 |

**Lane 5b.** Receives: Form 4797 and the installment-interest items are now asked only here (2.1 item 5, 2.4);
`s1.digital_income` is placed in 274 by lane 7b; `sd.casualty` is placed at 216.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★5 | `sd.other_forms` (48 w, names six forms) split as 2.8; `f4952.has_interest` (204 w) in one line; `f4952.line4g` (83 w) beneath it | 100% | 20 + 5 + 20 → 3 + 1 + 0 |
| 2 | A plain parent before `$sales` ("In 2025, did you sell stocks, bonds, fund shares or crypto?"); today the list is asked last of all (walk position 68 of 82) | 100%; 13% (*gf*) | 5 → 1 |
| 3 | Per sale, by the paper (2.10): `box` (689 w), `correct_basis` (906 w), `wash_loss` (346 w), `proceeds` | 13%, several sales each | 40 → 8 per sale |
| 4 | `sd.carryover` and `clcw.*` by the 2024 paper; `clcw.spouse_screen` | 100%; 4.5% | 5 → 2 |
| 5 | `sales.special`, `sales.code`, `route`, `aggregate_eligible`; `f4952.unsupported`; `f8960.unsupported` | 13%; 1%; 4% est. | 10 → 4 |

**Lane 6a.** Receives: `scope.se_plan_other`, `s2.business_credit_recapture`, `s2.lookback`,
`s1.excess_business_loss` are placed in 259 by lanes 9 and 7b (lane 6a uses 250 to 254 and 259 to 264; 265 to 269 are
theirs).

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★7 | `qbi.unsupported` (76 w) and `qbi.carryforward` (30 w), asked of everyone, as 2.8 | 100% | 20 + 5 → 2 |
| 2 | `$sc` (48 w) as a question ("In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own?") | 100% per person; 19% (*gf*) | 5 → 1 |
| 3 | The three parents over the expense amounts (employees; goods for sale; travel and meals), 2.10 | 19% | 35 amounts → about 20 |
| 4 | `sc.special` (267 w), `method_other`, `at_risk`, `passive`, `inventory_other` as 2.9 | 19% | 30 → 8 |
| 5 | `sc.ho_uses`, `ho_other`, `hi_uses`, `hi_screen`, `f7206_line1`, `$ltc`, `ltc.*` | 5% est. | 15 → 5 |
| 6 | `person.se_screen` (146 w) cut to four items; `person.plan` with plain labels; `plan_screen` shorter | 19% | 10 → 3 |
| 7 | The words of the remaining `sc.line*` amounts | 19% | 3 each → 1 each |

**Lane 6b.** Receives: nothing.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★7 | `s179.line10` (77 w) beneath `s179.prior_form` | 100% | 10 → 2 |
| 2 | `scveh.screen` (732 w) as 2.9: a vehicle bought in an ordinary way and first used in 2025 meets about five questions | 10% est. | 20 → 5 |
| 3 | `asset.screen` (843 w), `asset.not179`, `asset.s179` (271 w), `asset.class` labels | 6% est. | 20 → 6 |
| 4 | `scveh.method` first, then only what the method needs (the mileage method needs no cost or depreciation question): check the gates | 10% | 10 → 4 |
| 5 | The rest of `scveh.*` and `asset.*` in a person's words | 10% | 3 each → 1 each |

**Lane 7a.** Receives: `scope.recovery` is placed in 160 beside the refund questions by lane 9; `s2.mortgage_subsidy`
(lane 7b) and `sd.casualty` (lane 5b) in 200; the casualty words leave `sa.unsupported` (2.7).

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★2 | The Schedule A block (2.10): four plain parents over `line8a`, `5b`, `5a`, `5c`, `gifts`, `line1`; `sa.unsupported` split (2.8) | 100%; 60% have a mortgage, property tax or gifts (*gf* `home_or_charity`) | 50 → 6 with nothing, 15 with a home |
| 2 | `refund.itemized` asked before `refund.received` (2.9) | 100%; 40% had a refund (*gf*), about 10% itemized | 5 → 1 |
| 3 | `sa.gifts` (292 w) in one line; `$gift`, `gift.special` (140 w), `gift.deduction`, `charity_limited` | 40% (*gf*) | 5 → 1; 15 → 4 |
| 4 | `refund.exc_tax`, `exc_who`, `not_2024`, `box8` and the 2024 figures by the paper | 4% est. | 20 → 8 |
| 5 | `sa.line1` (429 w) beneath `sa.medical_any` | 100% | 10 → 1 |

**Lane 7b.** Receives from 2.4 to 2.6 its own items; deletes the words 2.7 lists; sets the `order` of the 26 `s3`
entries (118, 126, 215, 225, 279, 290, 305 and 318, as the slot table says) without changing them.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★4 | `s2.amt`, `s2.other` (2.4) and `f8959.unsupported` (2.5) | 100% | 20 + 20 + 20 → about 12 (with a W-2: the paper check, 5) |
| 2 ★4 | `s1.line8_other` (189 w) as 2.6 | 100% | 20 → 7 |
| 3 ★9 | The eight amounts asked of everyone become yes or no parents; `s1.alimony` (95 w) as the chain of 2.8 | 100% | 30 → 9 |
| 4 | `$oi8z`, `oi8z.kind` (183 w) labels; `s1.cod_unsupported` (150 w), `uc_unsupported`, `alimony_unsupported`, `alimony_paid`, `alimony_received` | 5%, 0.6%, 3%, 0.3% (*gf*) | 15 → 5 |

**Lane 8a.** Receives: sets the `order` of the 32 health savings account entries to 190, keeping their `seq`;
`scope.archer_msa`, `person.x_hsa_prior_excess`, `s2.hsa_testing` are placed at 191 to 193 by lanes 9, 4b and 7b.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 | `$f1095a` (45 w) as a question ("Did you, or anyone on this return, have health insurance through HealthCare.gov or a state Marketplace in 2025?"), the form list beneath; it is the eighth question today | 100%; 8.5% (*gf*) | 5 → 1 |
| 2 | `f1095a.uniform` (198 w) in one line, so that twelve equal months are one answer | 8.5% | 36 amounts → 3 |
| 3 | `f8962.other` (357 w), `alloc`, `premium_adjust` as 2.9 | 8.5% | 20 → 6 |
| 4 | `f1095a.void`, `b_counted`, the column B correction rule; `f8962.fpl_table` labels; `dependent.ptc_*` | 8.5% | 5 each → 2 each |

**Lane 8b.** Receives: `scope.education_recapture` and `person.x_edu_account` are placed at 248 and 247 by lanes 9 and 4b.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 1 ★12 | `f5695.part1_any` (143 w), `part2_any` (141 w) beneath one parent; `sli.interest` (244 w) beneath `sli.any`; `f8863.paid` (37 w) shorter | 100%; 2.5%, 8%, 9% say yes (*gf*) | 5 + 5 + 5 + 2 → 1 + 1 + 1 |
| 2 | The student questions (twins): `edu_inst` (157 w), `edu_1098t` (98 w), `edu_a2025` (78 w) by the paper, Form 1098-T | 9% | 20 → 8 |
| 3 | Form 5695 after its parents: the cost lines share 224 words of help; one question on subsidies and rebates replaces it; `joint_occupancy`, `line5a`, `line26a` | 2.5% | 30 → 10 |
| 4 | `person.edu_born_*`, `edu_parent`, `edu_half_support`, `edu_fulltime`, `f8863.ban` | Students filing their own return: 3% est. | 10 → 4 |

**Lane 9.** Builds every `scope.*` input of 2.1 to 2.3 in `scope.yaml`, words it in the bank, and places it in the
topic Part 2 names, in the order slots the receiving lanes leave free. The three old ids stay as derived lines.

| # | Change | Share | Cost today → proposed |
|---|---|---|---|
| 0 | First hour: prove the derived-line technique on one item (Part 4.1) and report to the coordinator; everything else depends on it | | |
| 1 ★1 | Topic 130: `scope.rental`, `scope.k1`, `scope.farm_fishing` and its two children. These alone let the coordinator cut the largest items out of `scope.schedule1` | 100%; 12% refuse here (*gf*) | part of 60 → 3 |
| 2 ★1 | Topic 110: `scope.citizen`, `scope.nonresident`, `scope.chapter11`, `scope.armed_forces` and its three children, `scope.under24` and its two | 100% | part of 60 → 4 |
| 3 ★1 | Topic 140: `scope.pay_no_w2`, `scope.medicaid_waiver`, `scope.religious_work` and its three children, `scope.statutory_employee`, `scope.other_earned`, the two expense questions, `scope.code_h_deduction` | 100% | part of 60 → 8 |
| 4 | The rest of 2.1 to 2.3: topics 120, 155, 160, 170, 190, 240, 259, 285, 290 | 100% | part of 60 → 12 |
| 5 | Coverage rows (`interview/2025/coverage/scope.yaml`, T-287): one row for each row of 2.1 to 2.3, each ending in the refusal it ends in today | | |

When items 1 to 4 are done the three screens (663 words, my estimate 60) are 21 questions asked of everyone at
about 27 in all, and four more asked with a W-2. That is twice what the owner accepted for the credits screen (nine).
It is the price of having no tick-box question: see Part 5, question 2.

### The dozen changes ranked highest

My estimates throughout; the owner rates costs himself. "Saving" is today's less the proposed cost of the typical
answer, times the share who meet the question.

| Rank | Change | Lane | Share who meet it | Today | Proposed | Saving |
|---|---|---|---|---|---|---|
| 1 | The three scope screens taken apart | 9 | 100% | 60 | 27 | 33 |
| 2 | The Schedule A block beneath four plain parents | 7a | 100% | 50 | 6 to 15 | about 40 |
| 3 | `sb.foreign_any` into four short parents | 5a | 100% | 20 | 5 | 15 |
| 4 | `s2.amt`, `s2.other`, `f8959.unsupported`, `s1.line8_other` | 7b | 100% | 80 | 19 to 24 | about 58 |
| 5 | `sd.other_forms`, `f4952.has_interest`, `f4952.line4g` | 5b | 100% | 45 | 4 | 41 |
| 6 | `person.x_other` | 4b | 100%, per person | 15 | 4 | 11 |
| 7 | `qbi.unsupported`, `qbi.carryforward`, `s179.line10` | 6a, 6b | 100% | 35 | 4 | 31 |
| 8 | `household.married`; `sa.excluded_income`; `sa.dependent` | 1 | 63%; 100% | 10; 25 | 2; 3 | 27 |
| 9 | The eight "zero if none" amounts and `s1.alimony` | 7b | 100% | 30 | 9 | 21 |
| 10 | `retirement.special`, per Form 1099-R | 4a | 24% × 1.5 forms | 15 | 4 | 4 |
| 11 | `div.any`, `ftc.taxes` | 5a | 100% | 10 | 1 | 9 |
| 12 | The two home-energy parents, `sli.interest`, `f8863.paid` | 8b | 100% | 17 | 3 | 14 |

Rank 4 saves more than ranks 1 and 3 by this arithmetic; it stands fourth because its proposed cost is the least
certain (the alternative minimum tax question has no plain form yet). The per-entry screens (`scveh.screen`,
`asset.screen`, the sale questions, the dependents' tests) cost more per filer who meets them than anything above,
and rank lower only because fewer filers meet them.

---

## Part 4. Shared decisions

### 4.1 Where a new input is declared, and what happens to the old one

1. **The lane that owns the form file where the catch-all is declared builds every item of it,** wherever in the
   interview the item is then asked. Lane 9 builds the `scope.*` items that are asked among lane 3's W-2 questions;
   lane 3 builds nothing for them. This is what lets fifteen agents work at once.
2. **The old id stays, as a derived line.** `scope.schedule1` stops being an input and becomes a Bool line that is
   true when any of its item lines is true. Every line of every form that refuses `when: scope.schedule1` is left as
   it is, so the refusal is the same line with the same `form` text as today, and no lane edits another's file. The
   old id leaves the bank; its fixture inputs are rewritten (a fixture that had the catch-all true gets the item that
   describes its facts true, the others default to false in `fixtures/2025/defaults.json`).
   *This technique is inferred from the gate conventions, not tried* (the credits lane removed `scope.credits` and
   edited its seven readers instead, which parallel lanes cannot do). Each lane tries it on its first catch-all. If
   the build refuses it, the lane keeps the old input, rewords it in the bank to hold only the items not yet moved,
   and reports; the coordinator then does the reader edits after the merge.
3. **A refusing child refuses through the old id's line**, not through a new `refuses:` entry of its own, unless it
   covers a situation today's question does not (then the lane notes say so: it is a scope change, which this redraft
   does not make without the coordinator).
4. **Deleting an item because another question asks it (2.7)** needs no model change: the words leave the bank
   `prompt`. The form line's `label` keeps the full source-faithful statement.

### 4.2 Names

| Thing | Name | Example |
|---|---|---|
| A plain parent that asks whether something exists | `<form>.<noun>_any`, or the plain noun where `_any` reads badly | `ssb.any`, `sli.any`, `sb.account_any`, `scope.rental` |
| A child input | Its own plain name in the same form | `scope.clergy` |
| The gate line of a child | `<child>_if_<condition>`, the child marked `gated_by` (docs/2026-11-06_formal_gates_design.md, Model conventions) | `scope.clergy_if_religious_work` |
| The form's constant for "not asked" | The form's existing false constant, or a new `<form>.no` | `s3.no` |
| A question that reads a paper | Named for the paper's box or code | `s2.w2_marks`, `sd.f2439` |

Ids fixed in Part 2 are used as written, so that another lane's notes and coverage rows can name them. A lane that
needs a different id says so in its notes under "Ids changed from the map".

A parent is declared in the same form as its children. Where the children are in two lanes' forms, the parent is
declared by the lane named in Part 2 and the other lane gates on it only if it exists on this branch today;
otherwise that lane asks its child ungated and lists it under "Requests to other lanes" for the stitch after the
merge.

### 4.3 How a refusing child is worded

- It asks **the fact**, in the past tense, about 2025: "Did a dealer take the credit off the price?" It asks **the
  wish** only where the return is right without the thing wished for (a credit or an election the filer may leave
  out); then the refusal's remedy ends "To go on without it, answer No."
- It never says "this tool" and never lists what the tool does not do. The last sentence of its help says what a
  Yes does: "A return with this is outside what this tool prepares; a Yes ends the interview here."
- Where a term cannot be avoided, the plain description comes first and the term after it in quotation marks or
  parentheses: "a business or rental you own a share of but do not run (a 'passive activity')".
- A refusing parent and a refusing child are never joined by "or". Two facts that both refuse are two questions,
  unless they are one subject on one paper ("box 12 shows A, B, M or N").

### 4.4 Register, with five worked examples

Second person, past tense, the year named once ("In 2025, did you ..."). A parent under 25 words, a child under 40.
No form, schedule or line number as the name of the thing asked about; a box or code of a paper only when the filer
is holding that paper and has just been asked about it. The spouse phrase, exactly as `interview/README.md` gives it,
in every once-per-return question where the spouse's item counts; per-person questions say "you" and are shown by
the frame rule. Amounts say where to read them. A question ends with a question mark, an amount with its source.

**1. A catch-all (`scope.schedule1`, 293 words, items 7 to 10).**
Today: "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including
any of the following? ... rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E
or a Schedule K-1) ... rental of personal property ... farm income (Schedule F) ..."
Proposed, three questions at 130:
- `scope.rental`: "In 2025, did you (or, on a joint return, your spouse) rent out anything you own, such as a house,
  a room, land, a vehicle or equipment, or receive royalties?"
- `scope.k1`: "In 2025, did you (or, on a joint return, your spouse) have income or a loss from a partnership, an S
  corporation, an estate or a trust? It is reported to you on a paper called Schedule K-1."
- `scope.farm_fishing`: "In 2025, did you (or, on a joint return, your spouse) have income from farming, or from
  fishing as your business?"

**2. A long per-entry screen (`retirement.special`, 411 words, asked for every Form 1099-R).**
Today: "Does this distribution involve any of these?" and 23 items.
Proposed, for a traditional IRA with code 7: "Did any of this money go into a Roth IRA or another Roth account?";
"Did any of it go straight from the IRA to a charity, or into a health savings account?"; "Have you ever put money
into a traditional IRA that you did not deduct?"; "Is there an amount in box 6 of this form?" (asked only of a plan).
Each of the other 19 items is reached only from the answer that makes it possible (a code 3 or 4, a rollover, an
annuity, a birth before 1936).

**3. An amount (`sa.line5b`, 232 words, asked of everyone).**
Today: "Deductible state/local real estate taxes on real estate you (or, on a joint return, your spouse) own that
was not used for business, only if the taxes are assessed uniformly at a like rate ..." and nine paragraphs.
Proposed, beneath `sa.home_owner` = Yes: "How much property tax did you pay in 2025 on your home and any other land
or buildings you own that are not used for business? (If the mortgage company pays it for you, Form 1098 box 10 or
your year-end statement shows it.)" Then a child: "Does that amount include charges for services, such as trash
collection or a sewer, or for improvements such as a new sidewalk?"; a Yes asks the part to leave out. The rules on
foreign property, on a sale during the year and on taxes of other years are children of "Did you buy or sell the
property in 2025, or is it outside the United States?"

**4. A yes or no asked of everyone (`sa.excluded_income`, 20 words, cost 20 by the owner's second example).**
Today: "Do you (or, on a joint return, your spouse) file Form 2555 or Form 4563, or have income excluded as a bona
fide resident of Puerto Rico?"
Proposed at 110: "In 2025, did you (or, on a joint return, your spouse) live or work abroad, in Puerto Rico or in
American Samoa, and leave the income you earned there out of this return?" Help: "This is the foreign earned income
exclusion (Form 2555) and the exclusions for residents of American Samoa (Form 4563) and Puerto Rico. If you lived
in the 50 states all year, the answer is No."

**5. A per-person question (`person.blind`, 119 words).**
Today: "For this person (you, or your spouse on a joint return) — Were you blind at the end of 2025?" and four
paragraphs.
Proposed: "Were you blind on December 31, 2025? (Partly blind counts only with an eye doctor's statement that you
see no better than 20/200 in your better eye with glasses, or have a field of vision of 20 degrees or less.)"
Shown for a spouse as "About your spouse — Was your spouse blind on ..." by the frame rule; a lane reads its framed
questions in `reports/2025/person_wording.md` before committing.

### 4.5 What goes in help

Help is for the filer who is unsure, and is at most about 40 words. It may hold: where on a paper the thing is found;
one example that settles a common doubt; what to answer when unsure (for a gate: "If you are not sure, answer Yes");
for a refusing question, the sentence of 4.3. It may not hold a rule the typical answer needs, a list of what the
question is not about, the name of the form line, or text moved out of a long prompt (N10: that goes into children).
The boilerplate help is deleted, not replaced. Where a parent's No is the wrong-No risk named in Part 2, the guard
is a child or a second question, and the lane's notes name it.

### 4.6 "Asked only when a W-2 (a business, a Form 1099-R) is listed"

Several new questions are worth asking only of a filer who listed an entry. The model already derives such facts
(`person.sc_count`, `s1.has_sc`). A lane that needs one derives it **in its own form** from lines that exist today,
and gates on that. No lane adds a line to another lane's file for this. If the derivation is not possible from
existing lines, the question is asked ungated and the lane records the gate as a request.

### 4.7 Files every lane touches

| File | Rule |
|---|---|
| `interview/2025/questions.yaml` | A lane edits only its own entries (Part 3). A new entry is inserted next to the existing entries of the same form, never at the end of the file, so that merges do not collide. Lane 9's new entries go after `scope.other_line16`'s place |
| `fixtures/2025/defaults.json` | The same: a new default next to its form's |
| Fixtures' inputs | A lane edits an input only for an id it owns; expected values and refusals are never edited (NORMS section 5) |
| `interview/2025/coverage/<lane>.yaml` | One file per lane (`scope.yaml`, `home.yaml`, ...); the three existing files are edited only where a moved question changes their answers, by the lane that moved it |
| `interview/2025/full.yaml` (the targets) | Not edited by lanes. A lane whose topic comes apart because a question is not reachable when its topic is asked writes the target it needs in its notes; the order agent adds it |
| `reviews/2025/twins.json` | Lane 8b only |
| `docs/provisional/lanes/<lane>.md` | The lane's notes, with the cost and share table of NORMS section 3 in the columns of Part 3's lists |

### 4.8 What is needed first, from a tooling agent

1. **From the order agent (T-284); the need, not the design.** (a) A child is asked directly after its parent is
   answered, whatever refusal entries stand before its own on a line (cause 2 of T-284); without this every parent
   in this map is separated from its children. (b) Within one order number that mixes once-per-return questions,
   per-person questions and per-entry questions, `seq` alone decides the sequence, with all of one entry's questions
   asked before the next entry's; or a stated rule the lanes can follow. (c) A question whose gate is computed from
   income (the saver's credit, the earned income credit, the tax on investment income) does not interrupt another
   topic when it becomes reachable: it waits for its own order number (310 and 278). (d) A report, for the minimal
   return and for any fixture, of the questions asked in order with their order numbers, so that a lane sees its
   topic asked together (`map_work/walk.mjs` prints it for the minimal return). (e) The direct targets a topic
   needs in `full.yaml` (4.7). (f) A check that fails when a bank entry still has an order number below 100.
2. **A page heading per topic** (the plain names of Part 1), shown when the order range changes. The owner's third
   example says a question's cost depends on the context built before it; the heading is that context. Optional.
3. **Tick-all-that-apply (T-285)** is not requested of the lanes. Part 5, question 2 asks the coordinator to assign
   it; the flat questions it would gather are marked in Part 3 (lane 9's 21, lane 7b's 9).
4. **A gate on a listed entry** (4.6), if the order agent finds lanes cannot derive it themselves.
5. Nothing in the profiles beyond the targets; nothing in the engine for wording (the spouse phrase and the frame
   rule already cover the new questions, provided the phrase is written exactly).

---

## Part 5. What I could not settle

### Open questions, each with a recommendation

1. **May the whole of Schedule A sit beneath one question?** Every filer is asked for medical bills, state taxes,
   property tax, mortgage interest and gifts (about 1,400 words), and about nine in ten then take the standard
   deduction. Four plain parents (2.10) cut the reading but still ask a renter four questions and still ask most wage
   earners to type their state tax. One question would spare them: "Your standard deduction is about $15,750 (single)
   or $31,500 (joint). Did your mortgage interest, state and local taxes (counted up to the limit), gifts to charity
   and large medical bills together come to more than that, or are you not sure?" A wrong No gives a correct return
   with more tax than necessary, since itemizing is a choice; but the same facts would then no longer always give
   the same return, which N9 forbids as written, and the amounts in the question are mine, not read from the
   parameters. **Recommendation:** build the four parents now; put the one question to the owner as a change of
   rule, not of wording.
2. **Without a tick-box question the redraft trades long screens for many short ones.** After lanes 9 and 7b a
   filer with nothing unusual answers about 30 new one-line questions asked of everyone (eight more with a W-2), where the owner rejected 14
   for the credits and accepted 9. By my estimates the cost still falls (140 to about 50 for those two lanes), but
   the count is what he objected to. **Recommendation:** assign T-285 now, in parallel; the lanes build single
   questions, each already one fact recorded separately, and a later pass groups them on tick-box screens without a
   model change.
3. **Fifteen units of work, not nine.** **Recommendation:** fifteen agents. If nine: pair the halves (Part 3) and
   accept that the tails of lanes 2, 6 and 8 are not reached.
4. **A death in 2025 is asked in six places in five files** (`household.spouse_died_2025`, `f2441.spouse_died`,
   `eic.died_2025`, `clcw26.final_return`, `person.died_before_65`, and in the health savings block). One fact asked
   once in topic 110 is right (N8), but it needs one input read by five lanes' files. **Recommendation:** not in
   the parallel pass. Each lane words its own question the same way ("Did your husband or wife die in 2025?");
   the coordinator makes them one fact after the merge.
5. **Three residual questions remain that no plain parent leads to:** `scope.other_adjustment` (a write-in on
   Schedule 1 line 24z), `s2.other_tax` (write-ins on Schedule 2 lines 1y and 17z) and `s2.rare_excise` (lines 17j
   and 17m). Today's catch-alls cover them only by the words "any other". They cost 20 as worded by line number.
   **Recommendation:** lanes 9 and 7b read the instructions for those lines; where the instructions name the kinds,
   ask the kinds; where they do not, keep one question at the very end of topic 290 worded by the paper ("Has the
   IRS, a court or a payer told you in writing to add a tax or a deduction to your return that you have not been
   asked about?"), and tell the owner it is there.
6. **The alternative minimum tax (`s2.amt`)** is asked of everyone in form words and refuses. It has no plain
   equivalent I could ground: the triggers are in the Form 6251 instructions, which I did not read. **Recommendation:**
   lane 7b reads "Who Must File" there, asks each trigger a person can recognize (incentive stock options first), and
   keeps the form-worded question as the last child only if a trigger remains that only a computation can find.
7. **One umbrella over investments** ("Do you own any stocks, bonds, funds or crypto outside a retirement
   account?") would spare seven in ten filers the dividend, sale, carryover and investment-interest parents, but
   its gates lie in both halves of lane 5 and its wrong No (shares from an employer, a loss carried over with
   nothing held now) is likely. **Recommendation:** not now; lane 5a's ownership question for dividends is the first
   half of it, and the stitch can extend it.
8. **Tax withheld on Forms 1099 is asked as one total at the end** (`f1040.line25b`), though each amount is a box of
   a paper asked about earlier (Form 1099-R box 4, SSA-1099 box 6). Asking it at each paper is right by N5 and is a
   model change in four lanes' files. **Recommendation:** lane 1 builds the plain parent now; the per-paper amounts
   wait for the stitch.
9. **Whether the redesigned parts break a norm.** The credits questions are asked of everyone in a flat run of nine
   (question 2 applies to them too); `s3.prior_other_forms` is a good paper parent that four other lanes' carryover
   questions could sit beneath (the 2024 return as a paper: Schedule D, Form 4562, Form 8995, Form 4952, Form 5695,
   Schedule A). **Recommendation:** leave the three parts as they are; consider a topic "From your 2024 return"
   after the merge.

### Where I inferred instead of reading

1. **The derived-line technique (4.1)** is inferred from the README and the gate design. Not built. Lane 9's item 0
   tests it.
2. **"Asked of everyone"** is the minimal single return's walk. A question asked of every couple but not of a single
   filer, or only with wages, is not in that list; lanes should rerun `walk.mjs` with their own background answers.
3. **Form 1040 line 1h** ("other earned income", 2.2 item 6): I named strike benefits from memory of the
   instructions and did not read them. Lane 9 reads the line 1a to 1h instructions before wording
   `scope.other_earned` and `scope.pay_no_w2`.
4. **The reservist repayment window** (2.2 item 9, "two years after active duty ends") is from memory. If it is
   longer, the parent's "since the start of 2022" is too narrow; lane 9 checks Pub. 590-A.
5. **The wrong-No analyses** are mine, made from the question texts. The project's rule is an adversarial review of
   every gate (formal gates design, rule 7), which this redraft does not run; each is review debt. The ones I think
   most likely to fail: `s3.foreign_any` as the gate of `ftc.taxes` (a fund's foreign tax the filer does not know
   of); `f2441.benefits` as the gate of `scope.care_benefits_other`; `scope.business_before` as the gate of
   `scope.passive`.
6. **Dollar figures in proposed wordings** ($1,350, $2,700, $2,800, $313,000, the standard deduction) are recalled
   or copied from today's prompts where they appear there; a lane takes each from the form YAML or `params/`, never
   from this map.
7. **What a question gates** is read from the YAML for every refusal named, and from the built gate descriptions
   (`cards.json`) for parents and children; I did not trace reachability through `choose` expressions, so "asked
   only when" for a question the cards call "asked only in some cases" is from its wording.
8. **Items of the per-entry screens (2.9)** were read in full for `retirement.special`, `sc.special`,
   `f8962.other`, `sb.foreign_any` and the person questions, and from the first fourteen words of each bullet for
   `scveh.screen`, `asset.screen`, `sales.box`, `sales.correct_basis` and `dependent.supported`. The lanes own those
   texts and confirm that no item is missing from their row.
9. **Shares marked est.** are my judgment; the others are `gate_frequencies.yaml`, many of which are themselves
   recorded there as judgments.
10. **Schedule 2 and Schedule 1 line lists** were read from the archived form text (`sources/2025/`), not from the
    instructions; what each line covers is from its printed label.
