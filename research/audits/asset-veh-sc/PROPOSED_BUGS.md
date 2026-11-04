# Proposed bug entries (package asset-veh-sc: T-178, T-179, T-182, T-183 sc/scveh/asset parts)

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1 — Form 4562 line 2 counted land improvements and excepted property as section 179 property (T-182)

- **Caught by:** owner question 3 of the A-backlog session (2026-11-02; owner decision A3: an engineering defect) and sc completeness claim 8 (BUG-0326); confirmed by evaluation in this package.
- **Source:** p946 p. 17, "Land and land improvements do not qualify as section 179 property" and "Even if the requirements explained earlier under What Property Qualifies? are met, you cannot elect the section 179 deduction for the following property" (noncorporate lessors, use outside the United States, tax-exempt organizations, governmental units and foreign persons); i4562 p. 2, "Property held for investment (section 212 property)"; p. 3, "for taxpayers other than a corporation, this election does not apply to any section 179 property you purchased and leased to others unless"; p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year".
- **Symptom:** `asset.is_section179` was true for every class other than qualified improvement property, so the business cost of any asset placed in service in 2025 and used more than 50% in the business went into Form 4562 line 2. Evaluated on the old tree: furniture of $2,000,000 fully elected, a paved parking area (class 00.3) of $2,400,000 and a $400,000 carryover gave line 2 $4,400,000, line 5 $2,100,000, line 12 $2,100,000, line 13 $300,000 and Schedule C line 13 $2,220,000. The source gives line 2 $2,000,000, line 12 $2,400,000 and Schedule C line 13 $2,520,000. The tax changes only when line 2 exceeds $4,000,000. Then line 11 (the smaller of business income or line 5) can cut a carryover or the deduction, or the election is refused as above line 5. At that income Form 1040 line 24 is refused anyway for Form 8995-A, but Schedule C line 13 and the printed Form 4562 lines 2, 4, 5 and 11 to 13 were wrong. Nothing stopped a section 179 election on such property either. The `asset.s179` question only told the filer to enter zero.
- **Fix:** new input `asset.not179`: a land improvement, investment property, property a noncorporate lessor purchased and leases to others (unless the two exceptions apply), or property used by a tax-exempt organization, a governmental unit or a foreign person or entity (with the source's exceptions). `asset.is_section179` requires it to be No. `asset.s179_bad` adds it, so an election above zero on such property refuses at `asset.after179`; the refusal form and remedy name it. `asset.s179` adds the tax-exempt, governmental and foreign-user items to its zero list. The question is read only for a 2025 asset used more than 50% in the business, or one with an election. It is not asked for qualified improvement property with no election (evaluated).
- **Fix lines:** `asset.not179`, `asset.is_section179`, `asset.s179_bad`, `asset.after179`, `asset.s179`
- **Siblings checked:**
  - `asset.cost179_real`, `asset.cost179_2025`, `asset.cost179`, `sc.cost179_a`, `sc.cost179`, `person.cost179`, `s179.line2`, `s179.line4`, `s179.line5`, `s179.line11`, `s179.line12`, `s179.over_limit`, `asset.f26i`, `asset.on_19`, `sc.f6`, `s179.line6`.
  - `scveh.cost179_o` and `scveh.s179_elect` are not changed. A vehicle used by a governmental unit or leased to others by a noncorporate lessor is still counted on line 2. That is rare for a car-and-truck entry, and a regular business of leasing passenger automobiles is screened. Recorded as a new-row proposal.
  - The trade-in rule (p946 p. 17, "its cost for purposes of the section 179 deduction includes only the cash you paid") is stated in `asset.s179` but not applied to line 2, which uses the whole business cost. Also a new-row proposal.
  - Lodging property, named in the parent's brief, is not in the 2025 list (p946 p. 17). It was not added.
- **Regression predictions:**
  - `stage14.s179.land_improvement` (the witness above, with `not179` Yes on the parking area): line 2 $2,000,000; line 4 $0; line 5 $2,500,000; line 9 $2,000,000; line 11 $2,500,000; line 12 $2,400,000; line 13 $0; Schedule C line 13 $2,520,000 ($2,400,000 plus 5.00% of $2,400,000 from Pub. 946 Table A-1, 15-year, year 1). Matched.
  - `stage14.asset.refuse_s179_not179` (the $3,000 computer of `stage14.asset.hy_5yr`, fully elected, `not179` Yes): refuses at `asset.after179` with gate `asset.s179_bad`. Matched.
  - `stage14.asset.refuse_s179_over` and `stage14.asset.refuse_s179_half` quote the refusal and follow its new wording.
- **Validation:** fixtures 1,446/1,446; evaluator witness before and after; GPT-6 Astra second reading (receipt `research/audits/asset-veh-sc/receipts/gpt-6-astra.168k9_line2.*`) also excludes all three kinds of property from line 2 and the threshold under sections 179(d)(1), 50(b) and 179(d)(5).
- **Tags:** amount-affecting (printed lines; tax above $4,000,000); eligibility; new-input; existing-form-pass; fixed

## PENDING-2 — Owner decisions A1, A2 and A4: used property and section 168(k)(9) property for the special allowance; employee-used vehicles (T-178)

- **Caught by:** A-backlog owner questions 1, 2 and 4 (2026-11-02); owner decisions A1, A2, A4.
- **Source:**
  - i4562 p. 6, "Qualified property can be either new property or certain used property".
  - p946 p. 31, "Original use means the first use to which the property is put, whether or not by you", and "Property containing used parts will not be treated as reconditioned or rebuilt if the cost of the used parts is not more than 20% of the total cost of the property".
  - i4562 p. 7, Exceptions, "Property described in section 168(k)(9)(A) or 168(k)(9)(B)". The plain description restates IRC 168(k)(9) and 163(j)(7)(A)(iv), (j)(9), which are not archived.
  - i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes if the value of personal use is included in the employees’ gross income, or the employees reimburse the employer for the personal use".
- **Symptom:**
  - A1: nothing asked whether 2025 property claiming the special allowance was used property, for assets or for vehicles (`scveh.bonus_choice` had the same defect).
  - A2: the asset screen named section 168(k)(9)(A)/(B) by number only, and vehicles were not asked about it at all.
  - A4: "your employees use it" sat in `scveh.screen`, which only `scveh.cost` reads. A leased vehicle on actual expenses, or the operating expenses of an owned one, was figured from the filer's miles with employees' personal use (premise from the A-backlog evaluation, rechecked by reading the dependency: `scveh.screen` → `scveh.screened` → `scveh.cost` only).
- **Fix:**
  - `asset.screen` and `scveh.screen` add two items, each conditional on claiming a special depreciation allowance in 2025: original use did not begin with you (with the definition and the reconditioned-property 20% rule); and section 168(k)(9)(A)/(B) property, described in plain words. The asset screen's earlier unconditional 168(k)(9) item is replaced by the conditional one.
  - New input `scveh.employee_use` (do your employees use this vehicle for personal purposes) and gate `scveh.employee_bad`, refused on `scveh.operating_business`, which every actual-expense vehicle reads, owned or leased. The employee item is removed from `scveh.screen`. New gate placed in `tools/coverage/tree.json` (196 gates placed).
- **Fix lines:** `asset.screen`, `scveh.screen`, `scveh.employee_use`, `scveh.employee_bad`, `scveh.operating_business`
- **Siblings checked:** `asset.bonus_choice`, `asset.bonus`, `asset.bonus_fullcase`, `scveh.bonus_choice`, `scveh.claims_bonus`, `scveh.bonus_2025`, `scveh.cost`, `scveh.screened`, `scveh.line9`, `scveh.line9_actual`, `scveh.lease_business`, `scveh.line20a`, `scveh.smr_amount` (the standard rate path does not read the employee question; the owner decision named operating expenses and leases), `scveh.over_half`, `asset.pct` (vehicles use miles; the 100% rule is a vehicle rule).
- **Regression predictions:**
  - `stage14.veh.refuse_employee_use_lease`: the leased vehicle of `stage14.veh.refuse_lease_smr_before`, without the earlier standard rate, with `employee_use` Yes, refuses at line 9 with gate `scveh.employee_bad`. Matched; line 20a still evaluates ($3,000), but Schedule C line 9 and Form 1040 line 24 refuse.
  - `stage14.veh.refuse_employee_use_owned` (the same vehicle, owned): the same refusal. Matched.
  - The screen items are wording on screens whose Yes already refuses; no fixture.
- **Validation:** fixtures 1,446/1,446; GPT-6 Astra second reading of the 168(k)(9) restatement (it found the floor plan vehicle definition and the 163(j)(1)(C) reference missing from the first draft; both added).
- **Tags:** eligibility; owner-decision; new-input; existing-form-pass; fixed

## PENDING-3 — Pub. 538 archived; the small business capitalization exemption settled (T-179; closes the T-174 claim 11 remainder and scveh completeness claim 2 of BUG-0326)

- **Caught by:** BUG-0311 claim 11 and BUG-0326 (scveh, capitalized vehicle costs); owner decision A5.
- **Source:** p538 (Rev. January 2022, the current edition, archived as `sources/2025/p538`) p. 17, Uniform Capitalization Rules, "The uniform capitalization rules do not apply to the following" and "A small business taxpayer that meets the gross receipts test under section 448(c) and that is not a tax shelter"; i1040sc p. 6, "A small business taxpayer (defined later under Part III) is not required to capitalize certain expenses to inventory or other property"; p. 15, the $31 million test.
- **Symptom:** i1040sc's "certain expenses" left open whether a small business taxpayer still had to capitalize some vehicle costs.
- **Fix:** none to an expression. Pub. 538 exempts a small business taxpayer from the uniform capitalization rules altogether, so "certain expenses" leaves nothing for one. `sc.method_other` already refuses a business that is not a small business taxpayer (gross receipts over $31 million, or a tax shelter). Its locator now cites p538 p. 17. The creative-property exception only widens the exemption for freelance artists, authors and photographers; any of them above $31 million is refused (accepted over-refusal).
- **Fix lines:** `sc.method_other` (citation only)
- **Siblings checked:** `sc.screened`, `sc.line1`, `scveh.line9`, `scveh.line20a`, `sc.inventory_other`, `sc.line35` to `sc.line42`.
- **Regression predictions:** none; no evaluated value changes.
- **Validation:** source reading; `fetch_sources.py` verifies 157 documents offline; `check_extraction.py` 122 PDFs, 0 failing.
- **Tags:** source-archive; owner-decision; closed-on-premise

## PENDING-4 — BUG-0326, Schedule C, vehicle and asset parts: the questions state or refuse the rules (T-183, except Schedule A)

- **Caught by:** BUG-0326, recorded open; this entry closes its sc, scveh and asset claims because the inventory is append-only. The Schedule A claims belong to another package.
- **Source:**
  - i1040sc:
    - p. 6: NIL income, "However, report royalties and other NIL income that is not self-employment income on Schedule E instead"; Installment sales.
    - p. 9: Line 22, "You can also deduct the cost of books, professional instruments, equipment, etc., if you normally use them within a year"; Line 23, "But some licenses, such as liquor licenses, may have to be amortized"; Line 24a, the $5-a-day incidental expense method, and "Other rules apply to luxury water travel".
  - p463 p. 12, Luxury Water Travel.
  - i1040gi p. 94, "A qualified small employer health reimbursement arrangement (QSEHRA) is considered to be a subsidized health plan maintained by an employer".
  - i4562:
    - p. 8, "Computer software. Use the straight line method over 36 months"; p. 9, "However, MACRS does not apply to films, videotapes, and sound recordings".
    - p. 10, the utility clearing and grading land improvements; p. 11, the credits and deductions that reduce the basis for depreciation; p. 12, the property that must be depreciated under ADS.
    - p. 14, "allocate the use based on the most appropriate unit of time the property is actually used".
  - p946 p. 17, section 179 excepted property (PENDING-1).
- **Symptom:** as recorded in BUG-0326.
- **Premise checks:**
  - sc claim 0 (line 9) holds no gap. `scveh.smr_ok` asks the first-year, whole-lease and five-vehicle rules, and `scveh.lease_smr_before` the leased-vehicle rule. Depreciation, section 179 and the special allowance are guarded by `scveh.is_actual_owned`, and line 20a is zero on the standard rate (inspected; `stage14.veh.standard` completes with line 31 equal to receipts less line 9). The Part IV statement is presentation.
  - sc claim 6 (home depreciation with the simplified method) holds no gap. A home is real property, which `asset.screen` refuses, and nothing else feeds line 13 from the home.
  - sc claim 7 (section 179 limits): fixed by PENDING-1. The like-kind exchange is screened, the SUV cap is `scveh.s179_bad`, and the trade-in limit is stated (line 2 remainder: new-row proposal).
  - scveh claim 2 is PENDING-3.
- **Fix:**
  - `asset.screen`:
    - replaces "you depreciate it under ADS" with the required-ADS cases (executive-order imports, the 263A(d)(3) election, QIP of an electing real property trade or business, 10-year or longer property of an electing farming business) or an ADS election;
    - adds films, videotapes and sound recordings; computer software unless placed in service in 2025 and fully deducted through section 179 and the special allowance; utility clearing and grading land improvements; and basis reduced by a credit or deduction (the p. 11 list).
  - `asset.pct` states the time-used rule for listed property.
  - `sc.special` replaces "installment sales of timeshares or residential lots" with any income reported under the installment method (including those sales), and adds licenses or other costs you must amortize, and luxury water travel.
  - Wording: `sc.line1` (NIL income that is not self-employment income goes on Schedule E); `sc.line22` (books and instruments used within a year; not longer-lived items); `sc.line23` (not licenses you must amortize); `sc.line24a` (incidental expenses, actual or $5 a day on a day with no meal expenses and no standard meal allowance); `sc.f7206_line1` (QSEHRA eligibility counts as an employer-subsidized plan).
- **Fix lines:** `asset.screen`, `asset.pct`, `sc.special`, `sc.line1`, `sc.line22`, `sc.line23`, `sc.line24a`, `sc.f7206_line1`
- **Siblings checked:** `asset.screened`, `asset.cost`, `asset.done`, `asset.class`, `asset.basis`, `asset.listed`, `asset.listed_low`, `sc.screened`, `sc.line28`, `sc.meals_50`, `sc.line24b`, `sc.hi_screen`, `sc.hi_screened`, `sc.f7206_line3`, `scveh.over_half`.
- **Regression predictions:** no evaluated value changes and no fixture added. Each new refusal is an item of a screen whose Yes already refuses (`stage14.refuse.special`, the asset screen fixtures).
- **Validation:** fixtures 1,446/1,446; `citations.py --strict` 0 findings.
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed
