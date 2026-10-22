> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: `scope.other_income` refuses passive activity income while tools/coverage/categories.json lists only `scope.schedule1` for the Schedule E categories (both confirmed in the files).
> **Verified after Stage 15:** see `stage17-schedule-e.verification.md` (12 errors, 5 items out of date), which supersedes this map where they differ.

# Stage 17 premise map — Schedule E (rental and royalty income, partnerships, S corporations, estates and trusts)

Read-only research for spec 2.4 roadmap item 3, coverage group `schedule_e`. Written by a research agent (Claude Code) on 2026-10-22 from the archived snapshots in `sources/2025/` and the repository at commit fcd2c26. It is testimony for the Stage 17 authoring, not a verified encoding: every claim about a form carries a locator, and every line must be checked again against its cited text when it is encoded. Stage 15 (Forms 8880, 2441, 5695) and Stage 16 (roadmap item 2, the remaining Schedule 1 items) are assumed to land first; where this stage depends on what Stage 16 does to `scope.schedule1`, that is said.

Locator convention (PROJECT_INDEX): `doc p. N, heading, "quote"`, where page N is the N-th form-feed chunk of `<doc>.cols.txt`. Forms are cited by line (`f1040se line 21`) with their page. Quotes are verbatim; `...` marks an omission. Proposed interview wording and project YAML are in single quotes or backticks, never double quotes, so the quote check reads only source text.

---

## 1. Scope

### 1.1 What the stage retires

`tools/coverage/categories.json` puts three categories in group `schedule_e`, each with the single gate `scope.schedule1`:

| Category id | Label | IRS returns (2023) | Share | Cells (soi-23in14ar, "All returns" row) |
|---|---|---|---|---|
| `rental_royalty` | Rental and royalty income or loss | 9,542,639 | 5.9% | col 63 total rental and royalty net income 6,346,357 + col 65 net loss 3,196,282 |
| `partnership_scorp` | Partnership or S corporation income or loss | 5,554,014 | 3.5% | max of (partnership 3,266,345 + 2,103,634; S corporation 4,138,040 + 1,415,974), a lower bound |
| `estate_trust` | Estate or trust income or loss | 685,175 | 0.4% | col 75 net income 648,583 + col 77 net loss 36,592 |

`reports/2025/filer_coverage.md`: the group is step 3, `79.9% (+6.8)` after steps 1 and 2, `+4.3` if covered alone now. The estimator counts the group as retired once `scope.schedule1` no longer refuses it; whatever this stage still refuses becomes new gates that the estimator does not measure (no IRS count). The coverage reached is therefore lower than 79.9% by the share of the residual refusals.

Measured detail that bears on the scope (soi-23in14ar, checked by reading the archived XLS with the estimator's header test, numbers of returns):

| Column | Header | Returns |
|---|---|---|
| 51 | Rent, net income | 4,886,466 |
| 53 | Rent, net loss (includes nondeductible loss) | 4,336,173 |
| 55 / 57 | Royalty, net income / net loss | 1,798,063 / 76,508 |
| 59 / 61 | Farm rental (Form 4835), net income / net loss | 325,953 / 67,356 |
| 67 / 69 | Partnership, net income / net loss | 3,266,345 / 2,103,634 |
| 71 / 73 | S corporation, net income / net loss | 4,138,040 / 1,415,974 |
| soi-23in14acg 55 / 57 | Net short-term gain / loss from partnership, S corporation | 495,780 / 560,758 |
| soi-23in14acg 111 / 113 | Net long-term gain / loss from partnership, S corporation | 1,219,800 / 766,861 |

Inference (not measured): about 4.3 million returns report a rental loss before limitation, against 3.2 million with a net rental-and-royalty loss after it, so loss handling (passive limits) touches a large part of the rental group, not a corner of it. Losses are also common among partners (2.1 million of 5.4 million). The archived SOI tables have no Form 8582, Form 6198, Form 7203 or real-estate-professional count, so the share each proposed refusal costs cannot be measured from the archive.

Gates that refuse these situations now (checked in `forms/2025/scope.yaml`):

- `scope.schedule1` asks about `rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F)` among other Schedule 1 items, and refuses at `scope.ready`, `f1040.line8`, `s8812.eiw_4` and `eic.step2_other`.
- `scope.other_income` also asks about `income or loss from a passive activity (including gain on selling an interest in one)`. `categories.json` does not list it as a gate of the `schedule_e` categories, so the estimator would count rentals as covered while this screen still refuses them (inferred risk): the stage must narrow it too.
- Downstream screens that also refuse pieces of a Schedule E return: `person.se_screen` (partnership SE income, Schedule K-1 box 14 code A), `qbi.unsupported` (QBI other than Schedule C and section 199A dividends), `f8960.unsupported` (`Any annuity, rental, royalty, business or pass-through income`), `sd.other_forms` (`capital gains or losses on a Schedule K-1`), `sc.passive` (rental activity on Schedule C), `eic.step2_other` (Schedule E sends the EIC to Pub. 596 Worksheet 1).

### 1.2 Recommended first scope

The owner's Stage 15 pattern was to compute the common situations and refuse the rare and hard ones. Applied here:

**Compute.**

1. Schedule E Part I for rental real estate (property types 1 to 4, and 8 with a description) and royalties (type 6): lines 1a to 26 per property, the personal-use days test and the division of expenses, the 'used as a home and rented under 15 days' exclusion, and a used-as-a-home property with a net profit (no Worksheet 5-1 needed).
2. Depreciation (line 18): residential rental property (27.5 years) and nonresidential real property (39 years) by Pub. 946 Tables A-6 and A-7a, mid-month convention, placed in service in any year from 1987; and appliances, carpets, furniture and land improvements (5, 7 and 15-year property) by the existing GDS tables with the special depreciation allowance, through a Form 4562 per property when one is required. No section 179 for rental property.
3. Passive activity loss: Form 8582 Parts I to IV and VI to VIII, with prior-year unallowed losses per activity, the $25,000 special allowance and its phase-out between $100,000 and $150,000 of modified AGI; Part V for passive activities that are not actively participated rentals (passive Schedule K-1 business or rental activities), including their losses and prior-year unallowed losses. The filing exception (no Form 8582) is the same arithmetic and is shown as a filing note, not a separate path.
4. Schedule E Part II from Schedules K-1 (Form 1065) and (Form 1120-S): ordinary business income or loss (box 1), net rental real estate and other rental income or loss (boxes 2, 3), guaranteed payments (1065 box 4), with the material-participation and active-participation questions per K-1; portfolio boxes carried to their Form 1040 lines (interest, dividends, royalties, net short- and long-term capital gain, 28% and unrecaptured section 1250 gain from the partnership's business assets); partnership self-employment earnings (1065 box 14 code A) to Schedule SE line 2; section 199A information to Form 8995 below the threshold; tax-exempt interest, investment income and expenses, distributions as information.
5. Schedule E Part III from Schedules K-1 (Form 1041) with income only (no net loss from an activity), boxes 1 to 8, 9 (deductions not exceeding the activity's income), 13 A and B, 14 A, E, H and I.
6. The interplay: Schedule 1 line 5, Form 8960 lines 4a and 4b (and line 7 for estates and trusts), Form 8995 rows for qualifying rentals and K-1 trades or businesses, Schedule SE and the earned-income readers, the excess business loss gate, Schedule 8812's Earned Income Worksheet line 2b.

**Refuse (each a cited gate).** Form 6198 (any amount not at risk with a loss); basis limitations (partner basis exceeded, prior-year basis or at-risk losses, line 27 'Yes'); Form 7203 situations unless the owner adopts it (see decision D6); publicly traded partnerships; K-1 with more than one activity (box 22 or 23, 1120-S boxes 18 or 19); real estate professionals (line 43); Worksheet 5-1 (dwelling used as a home with a net loss); short-term or service rentals that are not "rental activities" (average stay 7 days or less, or 30 days or less with significant services); self-rental (type 7); not-for-profit rentals; depletion; section 179 (K-1 box 12, rental property); vehicles in a rental unless decision D9 adopts the standard mileage rate; Form 8582 Part IX (an activity's losses on two forms), dispositions, former passive activities, commercial revitalization deductions; Form 8582-CR (passive credits); Form 4797 items (K-1 box 10 and sales of rental property); Form 8990; Form 461 (excess business loss); REMICs (Part IV); farm rental (Form 4835, line 40) and farming K-1 codes; K-1 other-income and other-deduction codes outside a short list; K-1 credits; K-1 foreign taxes; estate or trust net losses and final-year deductions; the EIC for any Schedule E filer (Pub. 596 Worksheet 1 is not archived) unless decision D15 archives and encodes it.

**Why this cut.** The rental group is the largest single category on the roadmap (5.9%) and a large part of it has losses; refusing every rental loss that needs Form 8582 would refuse the high-income rental owners, who are the ones above the $100,000 modified AGI line or carrying suspended losses (inferred from the shape of the rule, not measured). Form 8582 is one arithmetic chain (Parts I to III) plus a pro rata allocation (Parts VI to VIII) that the `prorate` atom can express; Part IX and the special cases are what is hard. The K-1 refusals are the ones the instructions themselves route to other forms or worksheets that the project does not have (Forms 6198, 7203, 4797, 8582-CR, 8990, 461).

**A smaller alternative** if the stage must be cut: Part I and Part II with the Form 8582 filing exception only (i1040se p. 4, Exception for Certain Rental Real Estate Activities): compute every return with only rental real estate passive activities, no prior-year unallowed losses, and, with a net loss, active participation, a loss of $25,000 or less and modified AGI of $100,000 or less; refuse Form 8582. This is a strict subset of the recommended arithmetic, so it can be the first commit of the stage.

---

## 2. Sources

### 2.1 Archived and used

`f1040se`, `i1040se` (Nov 12, 2025); `f8582`, `i8582` (Nov 26, 2025); `f6198`, `i6198` (Rev. November 2025); `p527` (2025); `p925` (2025); `f1065sk1`, `i1065sk1` (Dec 17, 2025); `f1120ssk`, `i1120ssk` (Jan 6, 2026); `f1041sk1`, `i1041sk1` (Mar 13, 2025); `f4562`, `i4562`; `p946` (Appendix A Tables A-6, A-7, A-7a on pp. 73-74); `f8995`, `i8995`, `i8995-correction`; `f8960`, `i8960`; `f1040sse`, `i1040sse`; `f1040s1`; `i1040gi` (EIC Step 2); `i1040s8812` (Earned Income Worksheet); `soi-23in14ar`, `soi-23in14acg`.

The archived `f1065sk1` and `f1120ssk` have one text page each (the second form-feed chunk is empty), so the code lists are taken from the partner's and shareholder's instructions; `f1041sk1` page 2 holds its code list with "Report on" destinations.

### 2.2 Needed and not archived (do not fetch; listed for the owner)

| Document | Why | URL |
|---|---|---|
| Pub. 596 (2025), Earned Income Credit | EIC Step 2 question 4 sends every Schedule E filer to its Worksheet 1 | https://www.irs.gov/pub/irs-pdf/p596.pdf |
| Form 7203 and its instructions | Required "If you report a loss, receive a distribution, dispose of stock, or receive a loan repayment from an S corporation" | https://www.irs.gov/pub/irs-pdf/f7203.pdf, https://www.irs.gov/pub/irs-pdf/i7203.pdf |
| Rev. Proc. 2019-38 | The rental real estate safe harbor for QBI, named in i8995 | https://www.irs.gov/pub/irs-drop/rp-19-38.pdf |
| Form 4797 and instructions | K-1 box 10 (1120-S box 9), sales of rental property, Form 8582 Part IX | https://www.irs.gov/pub/irs-pdf/f4797.pdf, https://www.irs.gov/pub/irs-pdf/i4797.pdf |
| Form 8582-CR and instructions | Passive credits (K-1 box 15 rental credits) | https://www.irs.gov/pub/irs-pdf/f8582cr.pdf, https://www.irs.gov/pub/irs-pdf/i8582cr.pdf |
| Form 461 and instructions | Excess business loss including Schedule E losses | https://www.irs.gov/pub/irs-pdf/f461.pdf, https://www.irs.gov/pub/irs-pdf/i461.pdf |
| Form 8990 and instructions | Business interest of a rental trade or business | https://www.irs.gov/pub/irs-pdf/f8990.pdf, https://www.irs.gov/pub/irs-pdf/i8990.pdf |
| Form 4835 | Farm rental (line 40) | https://www.irs.gov/pub/irs-pdf/f4835.pdf |
| Pub. 541, Partnerships | Partner basis (named by i1040se and i6198) | https://www.irs.gov/pub/irs-pdf/p541.pdf |
| Pub. 534 | Property placed in service before 1987 | https://www.irs.gov/pub/irs-pdf/p534.pdf |

Only Pub. 596 and Form 7203 are needed by the recommended scope (and only if decisions D15 and D6 choose to compute); the rest back refusals, which can cite the archived text that names them.

---

## 3. Line map

### 3.0 Encoding frame (project facts this map relies on, checked against the files)

- Collections: `person` (one entry per person); `sc` under `person`; `asset`, `scveh`, `ltc` and the implicit `f4562` under `sc` (`forms/2025/asset.yaml` `collection.parent: sc`, `f4562.yaml` `parent: sc, implicit: form`). `asset` reads enclosing-entry lines of `sc` (`sc.one_cent`, `sc.hundred_cents`, `sc.fifty_cents`, `sc.bonus_rate_40`, `sc.conv_hy`), so it cannot be reused under another parent as it stands.
- `asset.screen` refuses `real property (a building or a structural component, other than qualified improvement property) or land` and property `placed in service before 2005`; `macrs_period` is `[y3, y5, y7, y10, y15, y20, y15sl, outside]`; `placed_year` is `y2005` to `y2025`; there is no month placed in service; `tables/2025/macrs_gds.yaml` holds Tables A-1 to A-5 and the 15-year column of A-8 to A-12 only (its header says so). Tables A-6, A-7 and A-7a are not encoded.
- `mq.yaml` sums `person.mq_q4` and `person.mq_total` over Schedule C property only.
- Count lines can be compared but not multiplied by a rate; `multiply_count` multiplies cents by a count exactly, so 'personal days more than 10% of rental days' is exact as `test gt (multiply_count 10 cents × personal days) (multiply_count 1 cent × rental days)`.
- `choose` returns money only; ratios between amounts go through `prorate` (ratio rounded half-up to stated places and kept in [0, 1]).
- `f1040.line8` copies `s1.line10`; `s1.line10` is `sum(s1.line3, s1.line7)` today; Schedule 1 line 5 does not exist.

Proposed new collections (decision D1):

| Collection | Parent | One entry per | Notes |
|---|---|---|---|
| `rental` | none (return) | Schedule E Part I property (rental or royalty) | MFJ: either spouse's or joint property, no owner field (Schedule E is one per return; QJV interests are separate entries) |
| `rasset` | `rental` | depreciable item of a rental property | real property MM, or 5/7/15-year property |
| `rf4562` | `rental` (implicit) | Form 4562 of a property that needs one | as `f4562` is to `sc` |
| `k1p` | `person` | Schedule K-1 (Form 1065) or (Form 1120-S) | entity type enum; SE and QBI are per person |
| `k1e` | `person` | Schedule K-1 (Form 1041) | |

### 3.1 Schedule E Part I (f1040se p. 1, i1040se pp. 4-8)

Per `rental` entry unless stated. "Return" means a return-level line.

| Line | Printed text (f1040se p. 1) | Computes | Existing supply | New inputs |
|---|---|---|---|---|
| A | "Did you make any payments in 2025 that would require you to file Form(s) 1099?" | display | — | return Bool |
| B | "If “Yes,” did you or will you file required Form(s) 1099?" | display | — | return Bool |
| 1a | "Physical address of each property (street, city, state, ZIP code)" | display only (no strings in the data model) | — | none (the values sheet names entries by key) |
| 1b | "Type of Property" (list "1 Single Family Residence ... 8 Other (describe)") | enum gate | — | `rental.type` ∈ {sfr, multi, vacation, commercial, land, royalty, self_rental, other} |
| 2 | "For each rental real estate property listed above, report the number of fair rental and personal use days." | days test, division of expenses (§4.3) | — | Count inputs (see open question Q1): days rented at a fair rental price; days of personal use; days of personal use that fell on fair-rental days |
| 2 (QJV) | f1040se p. 1, "Check the QJV box only if you meet the requirements to file as a qualified joint venture." | display | — | Bool; each spouse's share is a separate entry (i1040se p. 2, QJV) |
| 3 | "Rents received" | input, zero for royalty type, zero if excluded (§4.3) | — | NonNeg |
| 4 | "Royalties received" | input, only for type royalty | — | NonNeg (1099-MISC box 2; K-1 1065 box 7 and 1120-S box 6 also go here, decision D12) |
| 5 | "Advertising" | input × rental share (§4.3) | — | NonNeg |
| 6 | "Auto and travel (see instructions)" | travel input; vehicles per decision D9 | `sc.mileage_rate` (70 cents) | NonNeg; vehicle miles if D9 |
| 7 | "Cleaning and maintenance" | as line 5 | — | NonNeg |
| 8 | "Commissions" | as line 5 | — | NonNeg |
| 9 | "Insurance" | as line 5 | — | NonNeg |
| 10 | "Legal and other professional fees" | as line 5 | — | NonNeg |
| 11 | "Management fees" | as line 5 | — | NonNeg |
| 12 | "Mortgage interest paid to banks, etc. (see instructions)" | as line 5 | — | NonNeg (Form 1098 for the rental) |
| 13 | "Other interest" | as line 5 | — | NonNeg |
| 14 | "Repairs" | as line 5 | — | NonNeg |
| 15 | "Supplies" | as line 5 | — | NonNeg |
| 16 | "Taxes" | as line 5 | — | NonNeg |
| 17 | "Utilities" | as line 5 | — | NonNeg |
| 18 | "Depreciation expense or depletion" | sum over `rasset` of the 2025 deduction × rental share; depletion refused | new `rasset` lines | per asset (§3.2) |
| 19 | "Other (list)" | input × rental share | — | NonNeg |
| 20 | "Total expenses. Add lines 5 through 19" | `sum` | — | — |
| 21 | "Subtract line 20 from line 3 (rents) and/or 4 (royalties). If result is a (loss), see instructions to find out if you must file Form 6198" | `subtract` (Dollars); refusal when a loss and not all at risk | — | Bool at risk (as `sc.at_risk`) |
| 22 | "Deductible rental real estate loss after limitation, if any, on Form 8582 (see instructions)" | rental types only: the Form 8582 allowed loss for the activity (Part VIII column (c)) when the activity has a loss or a prior-year unallowed loss; line 21 when the loss is not passive (used as a home); blank otherwise | Form 8582 lines (§3.3) | prior-year unallowed loss input (Form 8582 Part IV column (c)) |
| 23a | "Total of all amounts reported on line 3 for all rental properties" | return `sum_over rental` | — | — |
| 23b | "Total of all amounts reported on line 4 for all royalty properties" | return `sum_over` | — | — |
| 23c | "Total of all amounts reported on line 12 for all properties" | return `sum_over` | — | — |
| 23d | "Total of all amounts reported on line 18 for all properties" | return `sum_over` | — | — |
| 23e | "Total of all amounts reported on line 20 for all properties" | return `sum_over` | — | — |
| 24 | "Income. Add positive amounts shown on line 21. Do not include any losses" | return `sum_over` of the positive part of line 21 | — | — |
| 25 | "Losses. Add royalty losses from line 21 and rental real estate losses from line 22. Enter total losses here" | return `sum_over` of royalty negative line 21 and rental line 22 (sign: Q16) | — | — |
| 26 | "Total rental real estate and royalty income or (loss). Combine lines 24 and 25." | return | — | — |

Supporting text:

- Part interests: i1040se p. 4, Income or Loss From Rental Real Estate and Royalties, "If you own a part interest in a rental real estate property, report only your part of the income and expenses on Schedule E."
- Royalty rows: i1040se p. 4, "For royalty property, enter code “6” on line 1b and leave lines 1a and 2 blank for that property."; i1040se p. 6, Line 4, "Report on line 4 royalties from oil, gas, or mineral properties (not including operating interests); copyrights; name, image, and likeness (NIL) rights".
- Totals even for one property: i1040se p. 6, General Instructions for Lines 5 Through 21, "Enter your total expenses for mortgage interest (line 12), depreciation expenses and depletion (line 18), and total expenses (line 20) on lines 23c through 23e, respectively, even if you have only one property."
- Line 12 versus 13: i1040se p. 7, Lines 12 and 13, "If the recipient was not a financial institution or you did not receive a Form 1098 from the recipient, report your deductible mortgage interest on line 13."
- Line 6 vehicles: i1040se p. 6, Line 6, "If you take the standard mileage rate, multiply the number of miles driven in connection with your rental activities by 70 cents a mile." and "If you claim any auto expenses (actual or the standard mileage rate), you must complete Part V of Form 4562 and attach Form 4562 to your tax return."
- Line 21: i1040se p. 7, Line 21, "If you have amounts for which you are not at risk, use Form 6198 to determine the amount of your deductible loss."
- Line 22: i1040se p. 8, Line 22, "Do not complete line 22 if the amount on line 21 is from royalty properties."; "If your rental real estate loss is not from a passive activity or you meet the exception for certain rental real estate activities (explained earlier), you do not have to complete Form 8582. Enter the (loss) from line 21 on line 22."; "If you have an unallowed rental real estate loss from a prior year that after completing Form 8582 you can include this year, include that loss on line 22."
- Line 22 with a profit: i8582 p. 15, Schedule E, Part I, "An activity that has net profit for the year and prior-year unallowed losses will have net profit on line 21 and the allowed loss on line 22."
- Line 26 destination: f1040se p. 1, line 26, "If Parts II, III, and IV, and line 40 on page 2 do not apply to you, also enter this amount on Schedule 1 (Form 1040), line 5."

### 3.2 Depreciation of rental property (line 18; Form 4562 per property)

When Form 4562 is needed: i1040se p. 7, Line 18, "You must complete and attach Form 4562 only if you are claiming: • Depreciation on property first placed in service during 2025;" (the other bullets: listed property including a vehicle, a section 179 deduction or amortization that began in 2025). p527 p. 18, Form 4562, "Otherwise, figure your depreciation on your own worksheet." So property placed in service before 2025 enters line 18 directly; a property with 2025 property gets a Form 4562 whose line 17 carries the earlier property (f4562 p. 1, line 17, "MACRS deductions for assets placed in service in tax years beginning before 2025").

Per `rasset` entry:

| Item | Text | Computes | New inputs |
|---|---|---|---|
| class | i4562 p. 10, "Residential rental property is a building in which 80% or more of the total rent is from dwelling units." | enum: residential (27.5), nonresidential (39), or a Pub. 946 Appendix B class as in `asset.class` | `rasset.kind` |
| (b) month and year | i4562 p. 11, Column (b), "For lines19i and 19j, enter the month and year you placed the property in service." and "If you converted property held for personal use to use in a trade or business or for the production of income, treat the property as being placed in service on the conversion date." | recovery year = 2025 − year + 1 (Count); month key | month enum m1-m12; `placed_year` extended back to y1987 for real property |
| (c) basis | i1040se p. 7, Line 18, "If you buy buildings and your cost includes the cost of the land on which they stand, you must divide the cost between the land and the buildings to figure the basis for depreciation of the buildings." | building basis only; land not depreciable | NonNeg basis of the building (or improvement) |
| (e) convention | i4562 p. 11, Column (e), "This convention applies only to residential rental property (line 19i), nonresidential real property (line 19j), and railroad gradings and tunnel bores." | MM for real property; HY or MQ for the rest (existing `mq` test, extended) | — |
| (f) method | i4562 p. 12, Column (f), "Water utility property, residential rental property, nonresidential real property, or any railroad grading or tunnel bore. The only applicable method is the straight line method." | S/L | — |
| (g) rate | p946 p. 73, Table A-6, "Residential Rental Property Mid-Month Convention Straight Line—27.5 Years"; p946 p. 74, "Table A-7a. Nonresidential Real Property Mid-Month Convention Straight Line—39 Years" | `keyed_lookup` (period, month, recovery year) → Rate; `multiply_rate` basis | new table `tables/2025/macrs_mm.yaml` (extractor and second transcription, as Stage 14's tables) |
| rental share | p527 p. 25, Personal Use of Dwelling Unit, "In general, your rental expenses will be no more than your total expenses multiplied by a fraction" | depreciation × rental share for mixed-use property (§4.3) | — |

Example values to check the table against (class A-like evidence from the publication): p527 p. 17, Table 2-2d, "the depreciation percentage for property placed in service in February of Year 1 is 3.182%" (deduction "$5,091 ($160,000 x 3.182% (0.03182))"); p527 p. 21, "For Year 6, the rate is 3.636%" with "Depreciation ($120,000 x 3.636% (0.03636))" giving $4,363 and a net rental loss of $213 ("Form 4562 isn’t required"). These two worked examples are candidate fixtures for Part I.

Rental personal property: i4562 p. 10, 5-year property, "Appliances, carpets, furniture, etc., used in a rental real estate activity."; p527 p. 13, Property Classes Under GDS, "This class also includes appliances, carpeting, and furniture used in a residential rental real estate activity." No section 179: p946 p. 16, Property Acquired for Business Use, "Property you acquire only for the production of income, such as investment property, rental property (if renting property is not your trade or business), and property that produces royalties, does not qualify." Bonus applies (p527 p. 12, Special Depreciation Allowance, "For 2025, some properties used in connection with residential real property activities may qualify for a special depreciation allowance.").

Refuse within depreciation: ADS (election or required: i4562 p. 12, "Any nonresidential real property, residential rental property, or qualified improvement property held by an electing real property trade or business"), 31.5-year nonresidential property (p946 p. 74, Table A-7, placed in service before May 13, 1993; decision D8), property placed in service before 1987 (Pub. 534, not archived), basis adjustments, dispositions, cooperative stock (p527 p. 22, Cooperatives, Depreciation), depletion.

Existing lines that change: `mq.q4` and `mq.total` (the mid-quarter test is per taxpayer, so rental personal property placed in service in 2025 must join it: i4562 p. 11, Column (e), "In determining whether the mid-quarter convention applies, do not take into account the following. • Property that is being depreciated under a method other than MACRS. • Any residential rental property, nonresidential real property, or railroad gradings and tunnel bores."), and the `macrs_period`, `macrs_convention` and `placed_year` enums in `params/2025.yaml`.

### 3.3 Form 8582 (f8582 pp. 1-3, i8582 pp. 9-15)

Return-level lines, fed by per-activity lines in `rental` (Part IV rentals with active participation) and `k1p`/`k1e` (Part IV or Part V).

| Line | Printed text (f8582 p. 1) | Computes |
|---|---|---|
| 1a | "Activities with net income (enter the amount from Part IV, column (a))" | sum of Part IV (a) over `rental` and `k1p` |
| 1b | "Activities with net loss (enter the amount from Part IV, column (b))" | sum of Part IV (b) |
| 1c | "Prior years’ unallowed losses (enter the amount from Part IV, column (c))" | sum of Part IV (c) inputs |
| 1d | "Combine lines 1a, 1b, and 1c" | sum (signed) |
| 2a-2d | the same for Part V | Part V sums |
| 3 | "Combine lines 1d and 2d and subtract any prior year unallowed CRD. See instructions. If this line is zero or more, stop here" | sum; CRD refused |
| 4 | "Enter the smaller of the loss on line 1d or the loss on line 3" | `smaller_of` of the two losses as positive amounts (gate: line 3 and line 1d both losses) |
| 5 | "Enter $150,000. If married filing separately, see instructions" | `param pal.phaseout_end` |
| 6 | "Enter modified adjusted gross income, but not less than zero. See instructions" | `subtract_floor0` of the MAGI build (§4.5) |
| 7 | "Subtract line 6 from line 5" | `subtract_floor0` |
| 8 | "Multiply line 7 by 50% (0.50). Do not enter more than $25,000. If married filing separately, see instructions" | `multiply_rate`, then `smaller_of` with `pal.special_max` |
| 9 | "Enter the smaller of line 4 or line 8. If line 3 includes any CRD, see instructions" | `smaller_of`; zero when Part II is skipped (line 1d not a loss) |
| 10 | "Add the income, if any, on lines 1a and 2a and enter the total" | `sum` |
| 11 | "Total losses allowed from all passive activities for 2025. Add lines 9 and 10." | `sum` |

Per activity (Part IV columns, f8582 p. 1, Part IV headings): (a) net income (line 1a), (b) net loss (line 1b), (c) unallowed loss from prior years (line 1c), (d) gain, (e) loss; overall gain or loss in (d) and (e) combines (a) to (c) (i8582 p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity, and either enter the overall gain for the activity in column (d) or enter the overall loss for the activity in column (e).").

- Column (c) source: i8582 p. 10, Part IV, Column (c), "You find these amounts in Part VII, column (c), of your 2024 Form 8582." and "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year."
- Part VI (only if line 9 is not zero): i8582 p. 12, Part VI, Column (b), "Divide each of the individual losses shown in column (a) by the total of all the losses in column (a)"; Column (c), "Multiply each ratio in column (b) by the amount on Part II, line 9"; Column (d), "Subtract column (c) from column (a) and enter the results in column (d)." Encoding: per activity with an overall loss (Part IV (e)), `prorate(amount = line 9, part = activity overall loss, whole = total overall losses)`, then subtract.
- Part VII: i8582 p. 12, Column (a), "Enter the amounts, if any, from column (d) of Part VI (from column (e) of Part IV and any prior-year unallowed CRD included in Part I, line 3, if you didn’t have to complete Part VI). Also enter the losses, if any, from column (e) of Part V."; i8582 p. 13, Column (c), "A. Enter as a positive amount Part I, line 3, of Form 8582", "B. Enter Part II, line 9, of Form 8582", "C. Subtract line B from line A", "Multiply each ratio in column (b) by the amount on line C above".
- Part VIII: i8582 p. 13, Column (a), "For each activity entered in Part VIII, enter the net loss plus the prior-year unallowed loss for the activity."; Column (b), "These are your unallowed losses for 2025. Keep a record of these amounts"; Column (c), "Subtract column (b) from column (a). These amounts are the losses allowed for 2025 under the passive loss rules."
- Where the allowed loss goes: i8582 p. 15, "Schedule E, Part I. Enter the allowed loss from the part on line 22 of Schedule E."; "Schedule E, Parts II and III. Any item of income shown on your Schedule K-1 that’s passive income must be entered as passive income in the appropriate column of Schedule E, Part II or III. Enter the passive loss allowed from Part VIII or IX of Form 8582 in the appropriate column for passive losses."
- Line 3 not a loss: i8582 p. 14, "If Part I, line 3, of Form 8582 shows net income or zero, all the losses in columns (b) and (c) of Parts IV and V and any prior-year unallowed CRD included in line 3 are allowed in full under the passive loss rules."

The 2025 form has no separate Worksheets 1 to 7 (they are Parts IV to IX of the form itself); the archived i8582 has no worksheet beyond the CRD worksheet (checked by reading pp. 9-16). Part IX (an activity's losses on two or more forms) is refused; with Form 4797 refused, a Schedule E activity's losses are on Schedule E only, except a K-1 activity with a passive capital loss (decision D11).

New per-activity outputs (display): the 2026 carryforward, Part VIII column (b).

### 3.4 Schedule E Part II (f1040se p. 2; i1040se pp. 8-10; i1065sk1; i1120ssk)

Line 28 per `k1p` entry; line 29 totals return-level over `person` then `k1p`.

| Item | Printed text (f1040se p. 2) | Computes |
|---|---|---|
| 27 | "Are you reporting any loss not allowed in a prior year due to the at-risk or basis limitations, a prior year unallowed loss from a passive activity (if that loss was not reported on Form 8582), or unreimbursed partnership expenses?" | return Bool; "Yes" refused except a passive prior-year loss reported on Form 8582 (which this stage always files when it applies) |
| 28 (b) | "Enter P for partnership; S for S corporation" | entity enum |
| 28 (c) | "Check if foreign partnership" | refuse (Form 8865 questions, foreign items) or display (decision D13) |
| 28 (e) | 'Check if basis computation is required' (printed in two broken columns, f1040se p. 2) | S corporation: loss, distribution, disposition or loan repayment (Form 7203) |
| 28 (f) | 'Check if any amount is not at risk' (same) | refused when there is a loss |
| 28 (g) | "Passive loss allowed (attach Form 8582 if required)" | passive items: the Form 8582 Part VIII (c) allowed loss of the K-1 activity |
| 28 (h) | "Passive income from Schedule K-1" | passive items with net income |
| 28 (i) | "Nonpassive loss allowed (see Schedule K-1)" | nonpassive losses (box 1 materially participated; within basis and at risk) |
| 28 (j) | "Section 179 expense deduction from Form 4562" | zero (K-1 box 12 refused) |
| 28 (k) | "Nonpassive income from Schedule K-1" | nonpassive income and guaranteed payments |
| 30 | "Add columns (h) and (k) of line 29a" | |
| 31 | "Add columns (g), (i), and (j) of line 29b" | sign per Q16 |
| 32 | "Total partnership and S corporation income or (loss). Combine lines 30 and 31" | |

Order of limitations (i1065sk1 p. 3, Limitations on Losses, Deductions, and Credits): "These limitations and the order in which you must apply them are as follows: the basis limitations, the at-risk limitations, the passive activity limitations, and the excess business loss limitations." The same sentence is in i1120ssk p. 2.

Schedule K-1 (Form 1065) boxes (f1065sk1 p. 1; destinations from i1065sk1):

| Box | Text | Destination (locator) | Recommendation |
|---|---|---|---|
| 1 | "Ordinary business income (loss)" | i1065sk1 p. 14, Box 1, "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28." Not materially participated: income column (h); loss "follow the Instructions for Form 8582" | compute; per-K-1 material participation input; loss within basis (screen) |
| 2 | "Net rental real estate income (loss)" | i1065sk1 p. 14, Box 2, "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners." Loss: column (g) after Form 8582; Part IV when actively participated (general partner), else Part V | compute; refuse the real-estate-professional route |
| 3 | "Other net rental income (loss)" | i1065sk1 p. 14, Box 3, "The amount in box 3 is a passive activity amount for all partners." (Part V; no special allowance) | compute |
| 4a, 4b, 4c | "Guaranteed payments for services", "Guaranteed payments for capital", "Total guaranteed payments" | i1065sk1 p. 15, Box 4a, "Generally, amounts on this line aren’t passive income, and you should report them in column (k) of Schedule E (Form 1040), line 28"; Box 4b, "Amounts on this line should be reported in column (k)" | compute (column (k)); not QBI (i8995 p. 3, "Amounts received as guaranteed payments.") |
| 5 | "Interest income" | i1065sk1 p. 15, Box 5, "Report interest income on Form 1040 or 1040-SR, line 2b." | compute into `sb.line2` (decision D12) |
| 6a, 6b, 6c | "Ordinary dividends", "Qualified dividends", "Dividend equivalents" | i1065sk1 p. 15, Box 6a, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b."; Box 6b, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a."; Box 6c, "Dividend equivalents aren’t reported on Form 1040 or 1040-SR." | compute 6a, 6b; 6c display; PTEP refused |
| 7 | “Royalties” | i1065sk1 p. 15, Box 7, "Report royalties on Schedule E (Form 1040), line 4." | compute (Part I royalty row, D12) |
| 8 | "Net short-term capital gain (loss)" | i1065sk1 p. 15, Box 8, "Report the net short-term capital gain (loss) on Schedule D (Form 1040), line 5." | compute: `sd.line5` |
| 9a | "Net long-term capital gain (loss)" | i1065sk1 p. 15, Box 9a, "Report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12." | compute: `sd.line12` |
| 9b | "Collectibles (28%) gain (loss)" | i1065sk1 p. 16, Box 9b, "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet—Line 18" | compute gains: `g28.line4`; refuse a loss |
| 9c | "Unrecaptured section 1250 gain" | i1065sk1 p. 16, Box 9c, "Report unrecaptured section 1250 gain from the sale or exchange of the partnership’s business assets on line 5." (lines 10 and 11 for the other two types, by attached statement) | compute line 5; refuse the statement types |
| 10 | "Net section 1231 gain (loss)" | i1065sk1 p. 16, Box 10, "report it in column (g) of Form 4797, line 2" | refuse (Form 4797) |
| 11 | "Other income (loss)" | codes A to ZZ (i1065sk1 p. 33) | refuse every code in the first scope (decision D14) |
| 12 | "Section 179 deduction" | i1065sk1 p. 18, Box 12, "Use this amount, along with the total cost of section 179 property placed in service during the year from other sources, to complete Part I of Form 4562" | refuse |
| 13 | "Other deductions" | codes A-G charitable (Schedule A lines 11, 12), H investment interest (Form 4952), AB (Schedule 1 line 18), Z itemized | refuse except as decision D14 |
| 14 | "Self-employment earnings (loss)" | i1065sk1 p. 22, Code A, "If you’re a general partner, reduce this amount before entering it on Schedule SE (Form 1040) by any section 179 expense deduction claimed, unreimbursed partnership expenses claimed, and depletion claimed on oil and gas properties." | compute code A to `person.se_line2`; refuse B (farming) and C (nonfarm optional method) |
| 15 | “Credits” | i1065sk1 p. 22, Box 15, "If you have credits that are passive activity credits to you, you must complete Form 8582-CR" | refuse (except code O backup withholding into `f1040.line25c`, D14) |
| 16 | f1065sk1 p. 1, "Schedule K-3 is attached if checked" | i1065sk1 p. 24, Box 16 | display; refuse foreign taxes (box 21) |
| 17 | "Alternative minimum tax (AMT) items" | i1065sk1 p. 24, Box 17, "Use the information reported in box 17 ... to prepare your Form 6251" | covered by the existing `s2` AMT screen; help text |
| 18 | "Tax-exempt income and nondeductible expenses" | i1065sk1 p. 25, Code A, "Individual partners include this amount on Form 1040 or 1040-SR, line 2a." | compute 18A into line 2a; B, C information |
| 19 | "Distributions" | i1065sk1 p. 25, Box 19, Code A, gain "To the extent the cash and the FMV of the securities ... received exceed the adjusted basis of your partnership interest" | information; refuse a distribution above basis (screen) |
| 20 | "Other information" | Code A, "Report this amount on Form 4952, Part II, line 4a."; Code B, "Report this amount on Form 4952, Part II, line 5." (i1065sk1 p. 27); Code Z, Section 199A (p. 29) | A, B into Form 4952 if D14; Z into QBI; N, AJ information; others refuse |
| 21 | "Foreign taxes paid or accrued" | i1065sk1 p. 32, Box 21, "Don’t use this amount to complete your Form 1116" | refuse when nonzero |
| 22, 23 | f1065sk1 p. 1, "More than one activity for at-risk purposes*", "More than one activity for passive activity purposes*" | i1065sk1 p. 32, Box 23, "When the partnership has more than one activity for passive activity purposes, it’ll check this box and attach a statement." | refuse (decision D10) |
| D | f1065sk1 p. 1, "Check if this is a publicly traded partnership (PTP)" | i1065sk1 p. 11, Item D, "If the box in item D is checked, you’re a partner in a PTP and must follow the rules discussed earlier under Publicly traded partnerships." | refuse (decision D10) |
| G | f1065sk1 p. 1, "General partner or LLC member-manager" / "Limited partner or other LLC member" | limited partners: no active participation (i1065sk1 p. 11, "Limited partners can’t actively participate unless future regulations provide an exception."), material participation only by tests 1, 5 or 6 (i1065sk1 p. 9) | input enum |
| K1-K3 | partner's share of liabilities | at-risk screen help | — |

Schedule K-1 (Form 1120-S), labels as printed on f1120ssk p. 1: box 1 “Ordinary business income (loss)”, 2 “Net rental real estate income (loss)”, 3 “Other net rental income (loss)”, 4 “Interest income”, 5a “Ordinary dividends”, 5b “Qualified dividends”, 6 “Royalties”, 7 “Net short-term capital gain (loss)”, 8a “Net long-term capital gain (loss)”, 8b “Collectibles (28%) gain (loss)”, 8c “Unrecaptured section 1250 gain”, 9 “Net section 1231 gain (loss)”, 10 “Other income (loss)”, 11 “Section 179 deduction”, 12 “Other deductions”, 13 “Credits”, 14 K-3, 15 “Alternative minimum tax (AMT) items”, 16 “Items affecting shareholder basis”, 17 “Other information”, 18 and 19 more than one activity. Destinations (i1120ssk pp. 6-8 and 15-17) are the same as the partnership boxes of the same name:

- i1120ssk p. 6, Box 1, "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28."
- i1120ssk p. 7, Box 3, "The amount in box 3 is a passive activity amount for all shareholders."; Box 4, "Report interest income on Form 1040 or 1040-SR, line 2b."; Box 6, "Report royalties on Schedule E (Form 1040), line 4."
- No self-employment tax: i1120ssk p. 1, "Your share of S corporation income isn’t self-employment income and it isn’t subject to self-employment tax." (and i1040se p. 10, S Corporations, "Your share of the net income of an S corporation is not subject to self-employment tax.").
- Box 16: i1120ssk p. 15, Code A, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a."; Code D, "If these distributions exceed the basis of your stock, the excess is treated as capital gain from the sale or exchange of property and is reported on Form 8949 and Schedule D (Form 1040)."
- Box 17: i1120ssk p. 15, Code A, "Report this amount on Form 4952, line 4a."; i1120ssk p. 17, Code V, "Use Form 8995, Qualified Business Income Deduction Simplified Computation, if: a. You have QBI, section 199A dividends, or PTP income (defined below); b. Your 2025 taxable income before the QBI deduction is equal to or less than $197,300 ($394,600 if married filing jointly)".
- Distributions are not on the K-1 as dividends: i1120ssk p. 1, "Schedule K-1 doesn’t show actual dividend distributions the corporation made to you." and i1040se p. 9, S Corporations, "Distributions of prior-year accumulated earnings and profits of S corporations are dividends and are reported on Form 1040 or 1040-SR, line 3b."

S corporation basis: i1040se p. 8, Basis rules for S corporations, "If you are claiming a deduction for your share of an aggregate loss (or you receive a distribution, dispose of stock, or receive a loan repayment from an S corporation), check the box on the appropriate line in Part III, column (e), and attach Form 7203 to your return." (The printed text says Part III; the box is in Part II, line 28 column (e), per f1040se p. 2, "you must check the box in column (e) on line 28 and attach the required basis computation". An erratum, recorded here as testimony.) The adjustments are in i1120ssk pp. 2-3 (stock basis increased by income items, decreased by distributions, nondeductible expenses, then losses and deductions; loans: "Distributions don’t reduce loan basis").

### 3.5 Schedule E Part III (f1040se p. 2; f1041sk1 p. 2; i1041sk1 pp. 1-5)

Per `k1e` entry: line 33 columns "(c) Passive deduction or loss allowed (attach Form 8582 if required)", "(d) Passive income from Schedule K-1", "(e) Deduction or loss from Schedule K-1", "(f) Other income from Schedule K-1"; 35 "Add columns (d) and (f) of line 34a"; 36 "Add columns (c) and (e) of line 34b"; 37 "Total estate and trust income or (loss). Combine lines 35 and 36".

| Box (f1041sk1 p. 2) | "Report on" (f1041sk1 p. 2) | Recommendation |
|---|---|---|
| 1 Interest income | "Form 1040 or 1040-SR, line 2b" | compute |
| 2a / 2b dividends | line 3b / line 3a | compute |
| 3 Net short-term capital gain | "Schedule D, line 5" | compute |
| 4a Net long-term capital gain | "Schedule D, line 12" | compute |
| 4b 28% rate gain | "28% Rate Gain Worksheet, line 4 (Schedule D instructions)" | compute |
| 4c Unrecaptured section 1250 gain | "Unrecaptured Section 1250 Gain Worksheet, line 11 (Schedule D instructions)" | compute `u1250.line11` |
| 5 Other portfolio and nonbusiness income | "Schedule E, line 33, column (f)" | compute (column (f)) |
| 6, 7, 8 business, rental real estate, other rental | "Schedule E, line 33, column (d) or (f)" | compute income only; passive (column (d)) per Q12 |
| 9 Directly apportioned deductions (A depreciation, B depletion, C amortization) | "Form 8582; or Schedule E, line 33, column (c) or (e)" | compute A and C when the activity's box 6-8 income is at least the deduction; refuse B and a resulting net loss |
| 10 Estate tax deduction | "Schedule A, line 16" | refuse (Schedule A line 16 not in scope) |
| 11 Final year deductions | Schedule 1 line 24k, Schedule A, Schedule D carryovers, NOL | refuse |
| 12 AMT | Form 6251 | existing `s2` screen |
| 13 A credit for estimated taxes | f1041sk1 p. 2, "Form 1040 or 1040-SR, line 26" | compute into `f1040.line26` (now a supplied total: help text, or a sum) |
| 13 B backup withholding | f1041sk1 p. 2, "Form 1040 or 1040-SR, line 25c" | compute into `f1040.line25c` |
| 13 others | credit forms | refuse |
| 14 A tax-exempt interest | "Form 1040 or 1040-SR, line 2a" | compute |
| 14 B foreign taxes | "Schedule 3 (Form 1040), line 1; or Schedule A, line 6" | refuse in the first scope |
| 14 E net investment income | "Form 4952, line 4a" | compute if Form 4952 is reached |
| 14 F gross farm and fishing income | "Schedule E, line 42" | display on line 42 (no tax effect) or refuse with farming (D14) |
| 14 H adjustment for section 1411 | f1041sk1 p. 2, "Form 8960, line 7 (also see the beneficiary’s instructions)" | compute `f8960.line7` |
| 14 I section 199A information | "See the beneficiary’s instructions" | compute to Form 8995 |

Supporting text: i1041sk1 p. 2, Boxes 6 Through 8, "The rules for applying these limitations to beneficiaries haven't yet been issued."; Box 5, "The amount reported in this box is your distributive share of royalties, annuities, and other income that isn't subject to the passive activity rules."; i1040se p. 11, Part III, "enter “ES payment claimed” and the amount on the dotted line next to line 37. Do not include this amount in the total on line 37."

### 3.6 Parts IV and V

- Part IV (REMIC residual holder): refuse. i1040se p. 11, Part IV, "REMIC income or loss is not income or loss from a passive activity." The excess inclusion floor on taxable income is a further reason ("This is the smallest amount you are allowed to report as your taxable income").
- Line 40 (Form 4835): refuse (farm group, Form 4835 not archived).
- Line 41: "Total income or (loss). Combine lines 26, 32, 37, 39, and 40. Enter the result here and on Schedule 1 (Form 1040), line 5" (f1040se p. 2) → new `s1.line5`.
- Line 42: display, zero when farming codes are refused.
- Line 43: refuse (real estate professionals); f1040se p. 2, line 43, "Reconciliation for real estate professionals."

### 3.7 Schedule 1 and Form 1040

- New `s1.line5`, printed "Rental real estate, royalties, partnerships, S corporations, trusts, etc. Attach Schedule E" (f1040s1 p. 1, line 5) = Schedule E line 41.
- `s1.line10` (now `sum(s1.line3, s1.line7)`) adds `s1.line5` (plus Stage 16's lines).

---

## 4. Rules

### 4.1 Passive activities, rental activities, material and active participation

- Definition: i1040se p. 3, Passive Activity, "A passive activity is any business activity in which you did not materially participate and any rental activity, except as explained later."; i8582 p. 3, Rental Activities, "A rental activity is a passive activity even if you materially participated in the activity (unless it’s a rental real estate activity in which you materially participated and you were a real estate professional)."
- Not rental activities (i8582 p. 3, Exceptions): "1. The average period of customer use is: a. 7 days or less, or b. 30 days or less and significant personal services were provided in making the rental property available for customer use." (refuse: decision D7).
- Dwelling used as a home: i8582 p. 3, item 4, "The rental of a dwelling unit you used as a residence if section 280A(c)(5) applies."; i1040se p. 4, Other activities, "The rental of a dwelling unit that you used as a home is not subject to the passive loss limitation rules."
- Royalties: i1040se p. 4, "Royalty income not derived in the ordinary course of a trade or business reported on Schedule E in most cases is not considered income from a passive activity."
- Material participation tests: i8582 p. 5, Tests for individuals, "You materially participated for the tax year in an activity if you satisfy at least one of the following tests. 1. You participated in the activity for more than 500 hours." (seven tests; spouse counts: "Participation by your spouse during the tax year in an activity you own may be counted as your participation in the activity").
- Active participation: i1040se p. 4, Active participation, "But you must have participated in making management decisions or arranging for others to provide services (such as repairs) in a significant and bona fide sense." and "You are not considered to actively participate if, at any time during the tax year, your interest (including your spouse’s interest) in the activity was less that 10% by value of all interests in the activity." (the source prints "less that").
- Real estate professionals (refused): i1040se p. 3, "You performed more than 750 hours of services during the year in real property trades or businesses in which you materially participated." and p. 4, "If you were a real estate professional for 2025, complete Schedule E, line 43."
- Grouping: i8582 p. 6, "Once you choose a grouping under these rules, you must continue using that grouping in later tax years". Proposed reading: each Part I property is one activity and each K-1 one activity; a grouping election is refused (open question Q19).
- Recharacterization (refuse the listed sources): i8582 p. 8, Recharacterization of Passive Income, "Rental of property if less than 30% of the unadjusted basis of the property is subject to depreciation." and "Rental of property to a nonpassive activity."; land rental (type 5) with net income would be recharacterized (p925 p. 16, Rental of Nondepreciable Property, "you treat the net passive income as nonpassive income"), which matters only when Form 8582 has a loss to offset (decision D7).

### 4.2 The special allowance and the filing exception

- i8582 p. 4, Special Allowance, "If you actively participated in a passive rental real estate activity, you may be able to deduct up to $25,000 of loss from the activity from your nonpassive income."
- Phase-out: i8582 p. 4, Modified adjusted gross income limitation, "If your modified adjusted gross income is more than $100,000 ($50,000 if married filing separately) but less than $150,000 ($75,000 if married filing separately), your special allowance is limited to 50% of the difference between $150,000 ($75,000 if married filing separately) and your modified adjusted gross income."
- Married filing separately: refused project-wide (`s3.mfs` at `scope.ready`); the MFS amounts are kept in the parameters so the data stays complete (i8582 p. 11, Line 5, "Married persons filing separate returns who lived apart from their spouses at all times during the year must enter $75,000 on line 5 instead of $150,000.").
- The filing exception: i8582 p. 1, Exception, "Rental real estate activities with active participation were your only passive activities." ... "You have no prior-year unallowed losses from these (or any other passive) activities." ... "Your total loss from the rental real estate activities wasn’t more than $25,000 ($12,500 if married filing separately)." ... "Your modified adjusted gross income (see the instructions for line 6, later) was not more than $100,000 ($50,000 if married filing separately)." ... "You don’t hold any interest in a rental real estate activity as a limited partner or as a beneficiary of an estate or a trust." Under these conditions Form 8582 Part II gives line 9 = line 4 (the whole loss), so the exception changes what is filed, not what is allowed (inferred from the arithmetic, §3.3). Proposed: compute Form 8582 always and mark it `shown_when` it is required.
- K-1 partners: i1040se p. 9, "But if you are a general partner or an S corporation shareholder reporting your share of a partnership or an S corporation loss from a rental real estate activity and you meet all of the conditions listed earlier under Exception for Certain Rental Real Estate Activities, you do not have to complete Form 8582."

### 4.3 Personal use of a dwelling unit (Pub. 527 chapter 5; i1040se Line 2)

- Home test: i1040se p. 5, Line 2, "You used the unit as a home if your personal use of the unit was more than the greater of: • 14 days, or • 10% of the total days it was rented to others at a fair rental price." Pub. 527 says the same (p527 p. 26, Dwelling Unit Used as a Home).
- Personal-use day: i1040se p. 5, "A day of personal use is any day, or part of a day, that the unit was used by: • You for personal purposes;" (and co-owners, family unless at a fair rental as a main home, anyone paying less than a fair rental price, exchange arrangements). Not personal: repair days and "Any days you used the unit as your main home before or after renting it or offering it for rent, if you rented or tried to rent it for at least 12 consecutive months".
- Fewer than 15 days: i1040se p. 5, "If you did use the unit as a home and rented the unit out for fewer than 15 days in 2025, do not report the rental income and do not deduct any rental expenses." Proposed: the entry computes to zero on every line and a notice names p527 p. 28, "Used as a home but rented less than 15 days".
- Division: i1040se p. 5, "You must allocate your expenses based on the number of days of personal use to total use of the property. For example, you used your property for personal use for 7 days and rented it for 63 days. In most cases, 10% (7 ÷ 70) of your expenses are not rental expenses and cannot be deducted on Schedule E." Pub. 527 counts a fair-rental day as rental use even with personal use that day, for the division only: p527 p. 26, "Any day that the unit is rented at a fair rental price is a day of rental use even if you used the unit for personal purposes that day. (This rule doesn’t apply when determining whether you used the unit as a home.)" Example: p527 p. 26, "Your rental expenses are 85/99 (86%) of the cottage expenses." (a fixture for the division and the home test together).
- Used as a home, rented 15 days or more: p527 p. 28, "If you had a net profit from renting the dwelling unit for the year (that is, if your rental income is more than the total of your rental expenses, including depreciation), deduct all of your rental expenses. You don’t need to use Worksheet 5-1. However, if you had a net loss from renting the dwelling unit for the year, your deduction for certain rental expenses is limited." Recommendation: compute the profit case, refuse the loss case (Worksheet 5-1, p527 p. 29, with its Schedule A interplay on p. 30: "If you are claiming the standard deduction, do not report an amount on line 2a; instead, report the rental portion of your mortgage interest on line 4b.") — decision D5.
- Not rented for profit (refuse): p527 p. 24, Not Rented for Profit, "Report your not-for-profit rental income on Schedule 1 (Form 1040), line 8j."
- Significant services (refuse, Schedule C): i1040se p. 5, Line 3, "if you provided significant services to the renter, such as maid service, report the rental activity on Schedule C, not on Schedule E."
- Self-rental (refuse): i1040se p. 5, Line 1b, "Enter code “7” for self-rental if you rent property to a trade or business in which you materially participated."
- Personal property rentals (outside Schedule E): i1040se p. 5, "Do not use Schedule E to report income and expenses from the rental of personal property, such as equipment or vehicles."

### 4.4 At-risk rules (Form 6198)

- i1040se p. 3, At-Risk Rules, "In most cases, you must complete Form 6198 to figure your loss if you have: • A loss from an activity carried on as a trade or business or for the production of income, and • Amounts in the activity for which you are not at risk."
- Qualified nonrecourse financing is at risk: i1040se p. 3, "Qualified nonrecourse financing is treated as an amount at risk if it is secured by real property used in an activity of holding real property subject to the at-risk rules." A rental financed by a bank mortgage is at risk (inferred from the definition: "Loaned or guaranteed by any federal, state, or local government, or borrowed by you from a qualified person.").
- Pre-1987: i1040se p. 3, "However, the at-risk rules do not apply to losses from an activity of holding real property placed in service before 1987."
- Order: i1040se p. 3, "Losses from passive activities may be subject first to the at-risk rules. Losses deductible under the at-risk rules are then subject to the passive activity loss rules."
- Recommendation: one screen per Part I property with a loss and per K-1 with a loss, worded like `sc.at_risk`; 'not all at risk' refuses with i6198 p. 1, Who Must File, "File Form 6198 if during the tax year you, a partnership in which you were a partner, or an S corporation in which you were a shareholder had any amounts not at risk (see Amounts Not at Risk, later) invested in an at-risk activity (defined below) that incurred a loss." No Form 6198 lines are computed.

### 4.5 Modified AGI for Form 8582 line 6

- i8582 p. 11, Line 6, "To figure modified adjusted gross income, combine all the amounts used to figure adjusted gross income, except don’t take into account: • Any passive activity loss as defined in section 469(d) (1), • Any rental real estate loss allowed to real estate professionals" ... "• The taxable amount of social security and tier 1 railroad retirement benefits, • Deductible contributions to traditional individual retirement accounts (IRAs) and section 501(c)(18) pension plans, • The deduction allowed for the deductible part of self-employment taxes," ... "• The student loan interest deduction,". Example: "Your modified adjusted gross income is $86,500 ($92,000 – $5,500)."
- p925 p. 6 lists the same items and adds "Passive activity income or loss included on Form 8582." (see Q4).
- Encoding consequence (inferred): MAGI cannot be AGI minus pieces, because AGI contains the allowed passive loss, which depends on MAGI; it must be built from the income and adjustment lines with the passive Schedule E amounts left out: Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a, Schedule 1 additional income except the passive part of line 5 (keeping royalties, nonpassive K-1 amounts, a home-used dwelling's rental), less the Schedule 1 adjustments other than lines 15 (SE tax), 20 (IRA, after Stage 16), 21 (student loan interest) and 24f (501(c)(18)). Taxable social security (line 6b) is left out, which also removes the only path by which the allowed loss would feed back (the Social Security Benefits Worksheet reads `f1040.line8`). Form 8815 and adoption exclusions are outside the project.

### 4.6 Qualified business income (Forms 8995, 8995-A)

- Rentals: i8995 p. 1, "Also, Rev. Proc. 2019-38 provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business for purposes of the QBI deduction."; i8995 p. 2, "meet the requirements of the safe harbor may still be treated as a trade or business for purposes of the QBI deduction if it’s a section 162 trade or business." Proposed per-property question; the safe harbor's conditions cannot be quoted from the archive (Rev. Proc. 2019-38 not archived).
- Suspended losses are not QBI: i8995 p. 3, "Losses or deductions from a qualified trade or business that are suspended by other provisions of the Internal Revenue Code are not qualified losses or deductions and, therefore, are not included in your QBI for the year. Such Code provisions include, but aren’t limited to, sections 163(j), 179, 461(l), 465, 469, 704(d), and 1366(d)."
- Partial allowance: i8995 p. 3, "If a loss or deduction is partially suspended, only the portion of the allowed loss or deduction attributable to QBI must be considered when determining QBI from the trade or business in the year the loss or deduction is incurred."
- Prior-year losses allowed now: i8995 p. 3, "When losses or deductions previously suspended by other Code provisions are allowed in calculating taxable income, the qualified portion of the loss or deduction allowed under each provision is treated as a qualified net loss carryforward from a separate trade or business when calculating the current year’s QBI deduction." With the FIFO "QBI Loss Tracking Worksheet" (i8995 p. 8). Recommendation: refuse a QBI trade or business (rental or K-1) whose allowed loss includes a prior-year unallowed loss (decision D11).
- Not QBI: i8995 p. 3, "Amounts received as guaranteed payments."
- K-1 QBI is not automatic: i8995 p. 3, "ordinary business income or loss is generally included in QBI if it was used in computing your taxable income, not excluded, suspended, or disallowed under any other section of the Code."
- Threshold: i1065sk1 p. 29, Code Z, "Your 2025 taxable income before the QBI deduction is equal to or less than $197,300 ($394,600 if married filing jointly)." Above it, Form 8995-A with business income stays refused (`qbi.business_any`, Stage 14).
- More than five rows: i8995 p. 4, Line 2, "If you have more than five trades or businesses, attach a statement with the name and taxpayer identification number of the trade(s) or business(es) and include the income and loss from those trade(s) or business(es) in the total for line 2."

### 4.7 Net investment income tax (Form 8960)

- i8960 p. 8, Line 4a, "Enter the following amount from your properly completed return. • Schedule 1 (Form 1040), line 3. • Schedule 1 (Form 1040), line 5. • Schedule 1 (Form 1040), line 6."
- i8960 p. 8, Line 4b, "Net income or loss from a section 162 trade or business that’s not a passive activity and isn’t engaged in a trade or business of trading financial instruments or commodities." and "Net income or loss from a section 1411 trade or business that’s taken into account in determining self-employment income." (entered as the negative of net income).
- Rentals: i8960 p. 4, Passive Activity, "A passive activity also includes any rental activity, regardless of whether you materially participate." Self-rental and grouped rentals are excluded (p. 4, Special Rules for Certain Rental Income), which the refusal of self-rental avoids.
- Estates and trusts: i8960 p. 8, "Any income from an estate or trust reported in Part III of Schedule E (Form 1040) that excluded NII is taken into account on line 7. Don’t report those adjustments on line 4b." (K-1 1041 box 14 code H).
- Self-employment: i8960 p. 7, Special Rule for Self-employed Individuals, "NII doesn’t include any item taken into account in determining self-employment income subject to tax under section 1401(b) for the tax year."
- Partnership or S corporation interest sales stay refused (Form 8960 line 5c).

### 4.8 Self-employment tax from partnerships

- f1040sse p. 1, line 2, "Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming)."
- i1040sse p. 3, Partnership Income or Loss, "Limited partners should include only guaranteed payments for services actually rendered to or on behalf of the partnership." and "If you were married and both you and your spouse were partners in a partnership, each of you must report your net earnings from self-employment from the partnership."
- Rentals are not SE income: i1040sse p. 4, "Income from real estate rentals if you didn’t receive the income in the course of a trade or business as a real estate dealer. Report this income on Schedule E."

### 4.9 Excess business loss

- i1040se p. 1, Reminders, "If you report a loss on line 26, 32, 37, or 39 of your Schedule E (Form 1040), you may be subject to a business loss limitation." Form 461 is not archived. Proposed: extend `s1.ebl` conservatively to count Schedule E losses with the Schedule C losses (decision D16).

---

## 5. Ordering and existing lines that change

### 5.1 Order of computation

Part I lines 3 to 21 per property → depreciation (per `rasset`, `rf4562`) feeds line 18 → K-1 items classified passive or nonpassive → Form 8582 Parts IV/V per activity → MAGI build (§4.5, no allowed loss in it) → Form 8582 Parts I to III → Parts VI to VIII per activity → line 22 and line 28 (g) → lines 24 to 41 → Schedule 1 line 5 → Form 1040 line 8 → AGI and everything that reads it. Schedule SE (with K-1 box 14 code A) is independent of the passive chain except through the allowed-loss question for a partnership SE loss (refused when limited).

### 5.2 Existing lines that must change (ids checked in `forms/2025/`)

| Line | Now | Change |
|---|---|---|
| `scope.schedule1` | asks about Schedule E and K-1 among others | drop the Schedule E / K-1 clause (coordinate with Stage 16, which is likely to rewrite the whole screen) |
| `scope.other_income` | asks about "income or loss from a passive activity" | narrow to passive activities outside Schedule E (Schedule C passive is refused by `sc.passive`) |
| `s1.line10` | `sum(s1.line3, s1.line7)` | add new `s1.line5` |
| `f1040.line8` | refuses on `scope.schedule1` | unchanged in form, narrower screen |
| `f1040.line2a` / `f1040.tax_exempt_interest` | 1099-INT/OID + `div.box12` | add K-1 1065 18A, 1120-S 16A, 1041 14A |
| `sb.line2` | `sum_over interest` | add K-1 interest (1065 box 5, 1120-S box 4, 1041 box 1), listed on Schedule B Part I (decision D12) |
| `sb.line6` / `f1040.line3b`, `f1040.line3a` | supplied totals | add K-1 6a/5a/2a and 6b/5b/2b, or instruct the filer to include them (D12) |
| `sd.other_forms` | refuses `capital gains or losses on a Schedule K-1` | narrow: K-1 boxes 8/9a (7/8a, 3/4a) computed; 1231, 11S and others still refused |
| `sd.line5`, `sd.line12` | zero behind `sd.other_forms` | sums of K-1 short-term and long-term amounts |
| `g28.line4` | `div.box2d` | add K-1 9b (8b, 4b) gains |
| `u1250.line5`, `u1250.line11` | `div.screen`, `div.box2b` | add K-1 9c (8c) and 1041 4c |
| `person.se_screen` | refuses `net earnings from self-employment from a partnership (Schedule K-1, box 14, code A)` | drop that clause; keep the others |
| `person.se_line2` | copies `person.sc_total` | `sum(person.sc_total, sum_over k1p box 14A)` |
| `person.eic_part1`, `person.eic_se_has`, `person.eic_se` | Schedule C only | use Schedule SE line 3, include partners (moot while the EIC is refused for Schedule E filers, D15) |
| `s8812.eiw_2b` | copies `s1.line3` | add K-1 1065 box 14 code A (i1040s8812 p. 8, line 2b, "Enter any net profit or (loss) from Schedule C, line 31, and Schedule K-1 (Form 1065), box 14, code A (other than farming).") |
| `person.positive_profits`, `sc.qbi_se`, `sc.qbi_plan`, the Form 7206 prorations in `sc` | share of the person's SE deduction by Schedule C profits | include K-1 SE earnings in the denominator (extends `amb.2025.qbi_attribution`; Q10) |
| `person.sep_s1`, `person.sep_s2`, `person.simple_comp` | Schedule C profit, the whole SE deduction, Schedule SE line 4 | refuse SEP/SIMPLE for a person who also has partnership SE earnings, or attribute (Q10) |
| `s1.ebl_total`, `s1.ebl_loss` | Schedule C only | add Schedule E losses (D16) |
| `s1.sc_1a` | Schedule C tips/overtime | add a K-1 screen: tips or overtime in a partnership or S corporation trade or business (i1040gi p. 104 names "the total of Schedule E, line 28(g) through 28(k)") — refuse |
| `qbi.unsupported` | refuses QBI other than Schedule C and 199A dividends | narrow to: PTP, cooperative patrons, carryforwards of suspended losses, 8995-A |
| `f8995.line2` | `sum_over person person.qbi` | add rental QBI (return) and K-1 QBI (person) |
| `f8995.line6` | `qbi.eligible` | add 199A dividends from K-1 statements |
| `f8960.unsupported` | refuses rental, royalty, business or pass-through income | narrow |
| `f8960.line4a` | copies zero, typed NonNegDollars | `sum(s1.line3, s1.line5)`, retyped Dollars (a Schedule E or C loss makes it negative) |
| `f8960.line4b` | copies zero, typed NonNegDollars | negative of nonpassive trade-or-business amounts (Schedule C, K-1 nonpassive box 1, guaranteed payments for services), retyped Dollars; `f8960.line4c` retyped too |
| `f8960.line7` | copies zero, typed NonNegDollars, refused by `f8960.unsupported` | K-1 1041 box 14 code H (signed), retyped Dollars |
| `mq.q4`, `mq.total` | Schedule C property | add rental personal property placed in service in 2025 |
| `f1040.line25c`, `f1040.line26` | supplied totals | help text (or sums) for K-1 backup withholding and 1041 13A |
| Schedule A mortgage interest and real estate tax inputs (`sa.yaml`) | Form 1098 interest | help text: the rental's interest and taxes go to Schedule E; for a mixed-use property only the personal part (D5) |
| `eic.step2_other` | refuses Schedule E (Pub. 596 Worksheet 1) | unchanged unless D15 |
| `tools/coverage/categories.json` | `schedule_e` gates `scope.schedule1` | the new gates (unmeasured) |

Downstream readers of AGI that change by value only (no definition change): `sa.agi` (medical floor, SALT phase-down), `sli` (reads `f1040.line9`), `ssb` (reads `f1040.line8`), `s8812` (reads `f1040.line11a`), `s1a` (reads `f1040.line11b`), the EIC AGI tests, Stage 15's credits (Form 8880 line 8, Form 2441 line 7), `qbi.taxable_before`, Form 8960 line 13.

---

## 6. Refuse-or-compute candidates

| # | Situation | Why it is hard | Recommendation |
|---|---|---|---|
| R1 | Rental loss under the filing exception | none: line 22 = line 21 | compute |
| R2 | Rental loss with MAGI over $100,000, loss over $25,000, prior-year unallowed losses, or passive K-1 activities | Form 8582 Parts I-III and the pro rata Parts VI-VIII; per-activity carryforward | compute (D2) |
| R3 | An activity's losses on two forms (Part IX) | per-form allocation, 28% split | refuse |
| R4 | Dwelling used as a home with a net loss | Worksheet 5-1 and its Schedule A interplay (line 2a/2b steps depend on itemizing and the SALT limit) | refuse (D5) |
| R5 | Mixed-use property not used as a home | expense division by days | compute |
| R6 | Used as a home and rented under 15 days | nothing reported | compute (exclusion with notice) |
| R7 | Average stay 7 days or less, or 30 days with significant services | not a rental activity; material participation decides passive status; Schedule C if services are substantial | refuse (D7) |
| R8 | Self-rental, land rental with net income, other recharacterized income | recharacterization; NIIT exclusion | refuse self-rental; compute land rental unless Form 8582 has a loss to offset (D7) |
| R9 | Real estate professional | per-property material participation, election, line 43, NIIT safe harbor | refuse (D7) |
| R10 | Not-for-profit rental | Schedule 1 line 8j | refuse |
| R11 | Amounts not at risk with a loss | Form 6198 | refuse |
| R12 | Real property depreciation | new table A-6/A-7a, month placed in service | compute (D8) |
| R13 | Section 179 on rental property or from a K-1 | not allowed for rental; K-1 box 12 joins Form 4562 Part I and its income limit | refuse |
| R14 | Vehicles in a rental | Form 4562 Part V for a non-Schedule C form | D9 |
| R15 | Depletion (royalties) | percentage depletion and its limits (Pub. 535, not archived) | refuse |
| R16 | Partner loss over basis, or distribution over basis | partner basis worksheet (i1065sk1 pp. 6-7) | refuse by screen |
| R17 | S corporation with a loss, distribution, disposition or loan repayment | Form 7203 required | D6 |
| R18 | PTP (item D) | separate per-PTP limitation, 751 items | refuse (D10) |
| R19 | K-1 with more than one activity | per-activity statements | refuse (D10) |
| R20 | K-1 box 10 / 1120-S box 9 (section 1231) | Form 4797 | refuse |
| R21 | K-1 credits, foreign taxes, other income codes, most other deductions | other forms | refuse (D14) |
| R22 | QBI business with prior-year suspended losses allowed now | QBI loss tracking | refuse (D11) |
| R23 | Estate or trust net loss, final-year deductions | rules for beneficiaries not issued; Schedule 1 line 24k | refuse |
| R24 | REMIC, Form 4835, farming codes | other forms | refuse |
| R25 | EBL over the threshold including Schedule E | Form 461 | refuse (D16) |
| R26 | EIC with Schedule E | Pub. 596 Worksheet 1 (not archived) | keep refusing (D15) |
| R27 | Business interest limit (Form 8990) | rental trade or business | refuse by screen (i1040se p. 7, "If your rental real estate activity is a trade or business, you must file Form 8990 to deduct any interest expenses of that rental real estate activity unless you meet one of the filing exceptions in the Instructions for Form 8990.") |
| R28 | QJV | none beyond two entries | compute |
| R29 | Property converted from personal use in 2025 | part-year expenses; basis lesser of FMV or adjusted basis (p527 p. 22, Property Changed to Rental Use) | compute (filer enters rental-period expenses; basis input) |

---

## 7. Parameters for `params/2025.yaml` (cents)

| Id | Value | Locator |
|---|---|---|
| `pal.special_max` | single, hoh, qss, mfj 2500000; mfs 1250000 | i8582 p. 4, "$25,000 for single individuals and married individuals filing a joint return for the tax year." and "$12,500 for married individuals who file separate returns for the tax year and lived apart from their spouses at all times during the tax year." |
| `pal.phaseout_end` | single, hoh, qss, mfj 15000000; mfs 7500000 | f8582 p. 1, line 5, "Enter $150,000. If married filing separately, see instructions"; i8582 p. 11, Line 5 ($75,000) |
| `pal.rate` | 1/2 | f8582 p. 1, line 8, "Multiply line 7 by 50% (0.50)." |
| `pal.exception_magi` | 10000000; mfs 5000000 | i8582 p. 1, Exception, "was not more than $100,000 ($50,000 if married filing separately)" (only if the exception is encoded as its own gate) |
| `pal.exception_loss` | 2500000; mfs 1250000 | i8582 p. 1, Exception, "wasn’t more than $25,000 ($12,500 if married filing separately)" (same) |
| `home.days` | 14 (Count) | i1040se p. 5, Line 2, "• 14 days, or" |
| `home.tenth` | 10 cents and 1 cent (two money params for the exact 10% comparison, §3.0), or a Rate 1/10 if a Count comparison atom is preferred | i1040se p. 5, Line 2, "10% of the total days it was rented to others at a fair rental price" |
| `home.min_rental_days` | 15 (Count) | i1040se p. 5, "fewer than 15 days in 2025" |
| `sc.mileage_rate` (existing, 70) | reuse for line 6 if D9 | i1040se p. 1, What's New, "increased to 70 cents a mile for 2025" |
| `qbi.threshold`, `s1.ebl_threshold`, `niit.threshold`, `se.*` (existing) | unchanged | — |

No parameter is needed for the 10% active-participation interest (an input), the 750-hour test (refused) or the at-risk rules (a screen).

---

## 8. Open questions the text leaves undecided

- **Q1. What goes on line 2.** Line 2 asks for "fair rental and personal use days" (f1040se p. 1); Pub. 527 counts a fair-rental day with personal use as rental for dividing expenses but as personal for the home test (p527 p. 26). Reading A: ask three counts (fair-rental days, personal days, overlap days) and print fair-rental days less overlap and personal days plus overlap on line 2 (the home-test view); reading B: print the division view. The amounts differ only for overlap days.
- **Q2. Exactness of the 10% test.** Pub. 527's examples round 10% down ("10% of the total days rented to others at a fair rental price is 27 days" for 273 days, p527 p. 27). Comparing personal days × 10 with rental days is exact and agrees with every example (inferred); rounding 10% to a whole day would differ at, for example, 275 rental days and 28 personal days.
- **Q3. Places of the rental-use ratio.** p527 p. 26 shows “85/99 (86%)” and Worksheet 5-1 line F (p527 p. 29) "Divide line C by line E" with no places. The `prorate` atom needs a number of places (Student Loan worksheet precedent: three; QBI attribution: six).
- **Q4. Modified AGI and passive income.** i8582 p. 11, Line 6, excludes "Any passive activity loss as defined in section 469(d) (1)"; p925 p. 6 excludes "Passive activity income or loss included on Form 8582". With a passive K-1 with income and a larger rental loss the two readings give the same MAGI (the income is inside the net loss); they differ if a passive activity's income is reported but not on Form 8582 (inferred). Proposed: build MAGI without any Part IV/V amounts.
- **Q5. Rounding residue in Parts VI and VII.** Each activity's share is a rounded product; the totals "must be the same as Part II, line 9" (i8582 p. 12) and may miss by cents with three or more activities. Readings: accept the residue (each line cited), or round the ratio to many places and record the reading. The `prorate` atom cannot assign a remainder to the last entry (no ordering).
- **Q6. Showing Form 8582 when nothing is limited.** i8582 p. 1 says the form "is filed by individuals, estates, and trusts who have passive activity deductions (including prior year unallowed losses)" and f8582 p. 1, line 3, says "stop here and include this form with your return". With rentals in net income and no carryovers, is the form shown? Proposed: shown when any activity has a loss or a carryover, or a Part V activity exists; hidden under the exception.
- **Q7. Condition f of the exception with net income.** i1040se p. 4 nests "You do not hold any interest in a rental real estate activity as a limited partner or as a beneficiary of an estate or a trust" under "All of the following apply if you have an overall net loss"; i8582 p. 1 lists it with the other conditions for everyone. Arithmetic is unaffected; only whether Form 8582 is shown (Q6).
- **Q8. K-1 royalties on Part I.** i1065sk1 p. 15 sends box 7 to "Schedule E (Form 1040), line 4". As its own royalty row (type 6) or added to an existing royalty property? Proposed: one Part I royalty row per K-1 with royalties, computed from the K-1 entry (a line may not read another collection's entry, so this needs the K-1 royalty to be carried at return level and a synthetic row, or the K-1 royalty kept on the K-1 entry and added into line 23b, 24 and 25 sums).
- **Q9. Schedule A side of a mixed-use property.** The personal part of mortgage interest and taxes may belong on Schedule A; the project's Schedule A inputs are supplied amounts. Reading: the filer enters Schedule A amounts without the rental part, with help text; or the tool carries the personal part.
- **Q10. Attribution of the SE deduction with partnership earnings.** The SE deduction is per person (Schedule SE line 13); QBI, Form 7206 and SEP worksheets attribute it per business. With K-1 box 14 code A, which share belongs to the partnership, and does the part from guaranteed payments (not QBI, i8995 p. 3) reduce QBI? Extends `amb.2025.qbi_attribution`.
- **Q11. Guaranteed payments for capital and the NIIT.** i8960 is silent; box 4b is not SE income and not passive. Readings: NII (include in line 4a, no 4b adjustment) or excluded with box 4a. Proposed: refuse box 4b when Form 8960 applies.
- **Q12. Beneficiary income character.** f1041sk1 p. 2 sends boxes 6-8 to "Schedule E, line 33, column (d) or (f)" and i1041sk1 p. 2 says the passive rules for beneficiaries "haven't yet been issued". Readings: ask the filer, or treat rental boxes 7-8 as passive and box 6 by a material participation answer.
- **Q13. Prior-year unallowed loss with active participation in only one year.** i8582 p. 10 sends such a loss to Part V. Ask a per-property question, or refuse.
- **Q14. Prior-year property depreciation.** Compute every pre-2025 item from cost, month and year with the tables (Stage 14's choice for Schedule C), or accept the filer's own figure for property placed in service before 2025 (allowed without Form 4562: p527 p. 18, "figure your depreciation on your own worksheet"). Computing can disagree with a preparer's earlier schedule that used the formula instead of the table ("The deduction is substantially the same both ways", p527 p. 15).
- **Q15. Table A-6 for years 10 to 28.** The table alternates 3.636 and 3.637 by month group and year parity (p946 p. 73); the reading-order extraction of that page is scrambled (checked), so the extractor and the second transcription must read it from the layout; any reading of the alternation must be pinned by the table check.
- **Q16. Signs of lines 22, 25, 31 and 36.** The form prints them in parentheses. Hold losses negative (combining by `sum`) or positive (subtracting); T-004 records the same question for Schedule D.
- **Q17. Partner losses and Schedule SE.** i1065sk1 p. 22: "If the amount in this box is a loss, enter only the deductible amount on Schedule SE (Form 1040)." With limited losses refused, a box 14 code A loss is entered as reported; confirm.
- **Q18. Line 27 with a passive prior-year loss on Form 8582.** If the stage always files Form 8582 when a prior-year unallowed loss exists, line 27's passive clause ("if that loss was not reported on Form 8582") is always "No". Confirm that reading.
- **Q19. Grouping.** One activity per property and per K-1 (no grouping election). A filer who grouped activities in earlier years must keep the grouping (i8582 p. 6); refuse a grouping, or ask.

---

## 9. Draft owner decision batch

Each with the recommended answer first, then the alternative.

- **D1. Collections.** Recommended: `rental` at return level (one entry per Part I property), `rasset` and an implicit `rf4562` under it, `k1p` (1065 and 1120-S, with an entity enum) and `k1e` under `person`. Alternative: separate `k1p` and `k1s` collections (printed box numbers differ), or rentals under `person`.
- **D2. Passive losses.** Recommended: Form 8582 Parts I-IV and VI-VIII with prior-year unallowed losses and Part V activities (losses included), Part IX refused. Alternative: the filing exception only (refuse every return that needs Form 8582), as the stage's first commit or for good.
- **D3. MAGI build.** Recommended: bottom-up from the income and adjustment lines, leaving out every Form 8582 amount (Q4). Alternative: AGI less pieces, which the evaluators would reject as a cycle.
- **D4. Personal-use days.** Recommended: three Count inputs (Q1 reading A), the exact 10% comparison by `multiply_count` (Q2), the ratio to six places (Q3). Alternative: two inputs as printed and a whole-day rounding.
- **D5. Mixed-use property.** Recommended: compute the division and the profit case; refuse a dwelling used as a home with a net loss (Worksheet 5-1); Schedule A amounts stay supplied by the filer, with help text (Q9). Alternative: refuse any property with personal-use days.
- **D6. S corporations.** Recommended: archive Form 7203 and its instructions and compute Part I (stock basis) for distributions and losses within stock basis; refuse debt basis and Part III limitations. Alternative: refuse every S corporation K-1 with a loss, distribution, disposition or loan repayment (keeps only income-only shareholders with no distributions, likely few).
- **D7. Rentals that are not plain rentals.** Recommended: refuse average stays of 7 days or less (or 30 with significant services), self-rental, real estate professionals, not-for-profit rentals; compute land rental (refuse a land rental with net income when Form 8582 has a loss). Alternative: compute short-term rentals with a material participation question.
- **D8. Real property depreciation.** Recommended: add Tables A-6 and A-7a (extractor, second transcription, table check), month placed in service, years from 1987 (27.5) and May 13, 1993 (39); refuse 31.5-year property and pre-1987 property. Alternative: also Table A-7; or accept a filer figure for prior-year real property (Q14).
- **D9. Vehicles in rentals.** Recommended: standard mileage only, with the Form 4562 Part V lines a standard-mileage vehicle needs, as a small per-property vehicle entry. Alternative: refuse vehicles (travel without a vehicle only), or generalize `scveh`.
- **D10. K-1 structure refusals.** Recommended: refuse PTPs, more than one activity, foreign partnerships with Form 8865 questions. Alternative: compute PTPs with income only.
- **D11. QBI.** Recommended: K-1 QBI from the filer's reading of the section 199A statement (one input: the QBI items allowed this year), rentals as QBI only on a yes to the trade-or-business question, current-year partial allowance by the i8995 ratio, refuse a QBI business with prior-year suspended losses allowed now. Alternative: refuse QBI from rentals entirely (Rev. Proc. 2019-38 not archived).
- **D12. K-1 portfolio items.** Recommended: computed from the K-1 entries into Schedule B, lines 2b, 3a, 3b and Schedule D lines 5 and 12; K-1 royalties as a Part I row (Q8). Alternative: the filer adds them to the existing payer entries and supplied totals.
- **D13. Codes and boxes allowed.** Recommended allow-list: 1065 boxes 1-9c, 14A, 18A-C, 19 (within basis), 20 A, B, N, Z, AJ; 1120-S boxes 1-8c, 16 A-D, 17 A, B, V, AC; 1041 boxes 1-9 (A, C), 13 A-B, 14 A, E, H, I; everything else refused by name. Alternative: also 1065 13 A-G charitable into Schedule A and 13H/20A into Form 4952.
- **D14. Form 8582 display.** Recommended: compute always; show it when a loss or carryover exists or a Part V activity exists (Q6, Q7). Alternative: show whenever Schedule E has a passive activity.
- **D15. EIC.** Recommended: keep refusing the EIC for Schedule E filers (Pub. 596 not archived); update the EIC and 8812 earned-income readers for partners anyway. Alternative: archive Pub. 596 and encode Worksheet 1 in this stage.
- **D16. Excess business loss.** Recommended: extend `s1.ebl` to Schedule C plus Schedule E lines 26, 32, 37 losses, refusing over the threshold. Alternative: archive Form 461 and compute.
- **D17. Prior-year depreciation.** Recommended: compute from the tables (Q14). Alternative: accept the filer's figure for property placed in service before 2025.
- **D18. Signs.** Recommended: hold Schedule E losses negative and print parentheses (Q16). Alternative: positive amounts subtracted.

Eighteen decisions; D2, D5, D6 and D8 decide most of the coverage and most of the work.

---

## 10. Verified versus inferred

Checked against the archived text (quotes searched in the cited pages' text; page numbers are form-feed chunks): every quoted passage above; the f1040se line labels of Parts I to V; the f8582 Part I to III lines and Part IV headings; the i8582 Exception, Line 6, Part IV, VI, VII and VIII instructions and the How To Report Allowed Losses passages; the i1040se Exception, Line 2, Lines 21 and 22, Part II and III instructions; the K-1 box destinations quoted from i1065sk1, i1120ssk and f1041sk1; the p527 home test, division example, Worksheet 5-1 conditions and the two depreciation examples; Table A-6's year-1 rate for February (3.182%) in p946 and p527; i4562 Column (b), (e) and (f) text; the i8960 line 4a and 4b instructions; f1040sse line 2; i1040s8812 Earned Income Worksheet line 2b; i1040gi EIC Step 2 question 4.

Checked in the repository: the `schedule_e` categories and their gates (`tools/coverage/categories.json`); the measured shares (`reports/2025/filer_coverage.md`) and the SOI cells (read from the archived XLS with the estimator's header test); `scope.schedule1` and `scope.other_income` wording; `s1.line10`, `f1040.line8`; `asset.yaml` parent, screen and enum limits; `macrs_gds.yaml` coverage; `mq.yaml`; `person.se_screen`, `person.se_line2`, `person.eic_part1`, `person.sep_s1`, `person.simple_comp`, `person.positive_profits`; `sc.at_risk`, `sc.passive`; `qbi.unsupported`, `qbi.business_any`, `f8995.line2`, `f8995.line6`; `f8960.unsupported`, `f8960.line4a`, `f8960.line4b`, `f8960.line7` (all three copy zero and are typed NonNegDollars); `sd.other_forms`, `sd.line5`, `sd.line12`; `g28.line4`, `u1250.line5/10/11`; `s8812.eiw_2b`; `eic.step2_other`; `f1040.line25c`, `f1040.line26` (supplied totals); `sc.mileage_rate` (70 cents); the parameter names listed in §7 as existing.

Not checked or inferred:

- The share of the group that each refusal costs (no archived count for Form 8582, 6198, 7203 or real estate professionals); the statement that loss handling touches a large part of the group rests on the SOI net-loss columns only.
- That the Form 8582 exception and the full Form 8582 give the same allowed loss (inferred from the arithmetic of lines 4 to 9, not from a text that says so).
- That a bank mortgage on a rental is qualified nonrecourse financing in the usual case (inferred from the definition).
- How Stage 16 will restructure `scope.schedule1` (assumed rewritten; this map names only the clause to remove).
- The 2025 K-1 (Form 1065) and (Form 1120-S) PDFs' second pages: the archived text has one page each; whether the IRS PDF has a code-list page that the fetch did not capture was not checked.
- Pub. 596, Form 7203, Rev. Proc. 2019-38, Forms 4797, 8582-CR, 461, 8990, 4835 and Pubs. 541, 534: not archived, so their content is not mapped.
- The Table A-6 alternation for years 10 to 28 was not transcribed here (the extraction of that page is out of reading order).
