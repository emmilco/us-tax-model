# Completeness review A: IT-201 (2025), full-year NYC resident, NY standard deduction

Scope: IT-201-I pp. 2-25 and 30-41 (`sources/ny/2025/ny_it201i.cols.txt`, layout text and web edition for tables),
IT-270-I, against `forms/ny/2025/*.yaml`, `params/ny/2025.yaml`, `tables/ny/2025/*.yaml`, `ambiguities/ny/2025.yaml`.
Lines 1-18 are out of scope. Rules the encoding computes, asks about or refuses are not listed. Personal data (name,
address, county, school district, bank account, designee, signature) is left out by owner decision B11 and is not
listed.

Counts: high 3, medium 1, low 5.

---

## H1 (high). Estimated tax penalty: a refund return, late installments, or no 12-month 2024 return are never screened

- Rules:
  - ny_it201i p. 23, "You may owe a penalty: • if line 80 is $300 or more and represents more than 10% of the income tax shown on your 2025 return; or • if you underpaid your estimated tax liability for any payment period."
  - ny_it201i p. 24, "It is possible for you to owe an estimated tax penalty and also be due a refund. In that case: 1. Subtract the estimated tax penalty amount from the overpayment. 2. Enter the net result on line 77."
  - ny_it201i p. 23, "In general, you are not subject to a penalty if your 2025 prepayments equal at least 100% of your 2024 New York income tax based on a 12-month return."
- What the encoding does: `ny_it201.gate.estimated_penalty` fires only when `ny_it201.tax_due` > 0 **and** the 2025
  prepayments total (`ny_it201.prepayments`) is below 100%/110% of the typed 2024 tax. Otherwise `ny_it201.line81` is 0.
  So:
  1. On a refund return (`tax_due` = 0) with estimated payments (`ny_it201.line75` > 0) made late or unevenly, an
     underpayment for an earlier payment period is never asked about; line 81 is 0 and `ny_it201.line77` is overstated.
  2. Even with a balance due, the safe harbor is tested on annual totals only; a total that meets 100%/110% of 2024
     tax but was paid in late installments passes. (Withholding alone is not affected, since it is treated as paid
     evenly; estimated payments are.)
  3. `ny_it201.ask.prior_year_tax` says "based on a 12-month return" but nothing asks whether there was one. A filer
     with no 2024 New York return (or a short-year one) types 0, so `ny_it201.safe_harbor` is 0, the gate never
     fires, and a balance due of $300 or more that is over 10% of the 2025 tax gets no penalty and no refusal.
- Suggested fix: refuse (cite p. 23 "for any payment period" and p. 24 "owe an estimated tax penalty and also be due a
  refund") whenever `ny_it201.line75` > 0 and the filer does not confirm that each installment was paid on time in
  the required amount, whatever the balance. Add a Bool question "Did you file a 2024 New York return covering 12
  months?" and, when the answer is No, refuse whenever `ny_it201.tax_due` ≥ `ny.est.min_due` (the parameter exists but
  nothing reads it), or simply whenever `tax_due` > 0.

## H2 (high). Line 75 question leaves out amounts the instructions put on line 75, and does not exclude NYC UBT

- Rules (ny_it201i p. 22, Line 75):
  - "your 2025 estimated tax payments for New York State, New York City, Yonkers, and metropolitan commuter transportation mobility tax (include your last installment even if paid in 2026). If you marked filing status ② but made separate 2025 estimated tax payments (Form IT-2105, Estimated Tax Payment Voucher for Individuals), enter your combined total estimated tax paid;"
  - "any amount of overpayment from your 2024 personal income tax return that you applied to your 2025 estimated tax (if this amount was adjusted by the Tax Department, use the adjusted amount)"
  - "If you marked filing status ② but you and your spouse filed separate Forms IT-370, enter the total amount you and your spouse paid."
  - "Do not include any amounts you paid for the New York City unincorporated business tax."
  - "If you are a beneficiary of an estate or trust and are claiming your portion of any payment of estimated taxes allocated to you by the estate or trust, include your amount on line 75"
- What the encoding does: `ny_it201.line75` asks for "Your 2025 New York State and City estimated tax payments
  (including the last installment even if paid in 2026), any 2024 overpayment applied to 2025 estimated tax, and any
  amount paid with Form IT-370". Read as written, it excludes MCTMT and Yonkers estimated payments (an MCTMT estimate
  paid by a self-employed filer who ends up at or below $50,000 is not refused by `ny_it201.gate.mctmt` and is lost),
  does not say to combine a spouse's separate vouchers or IT-370 payment on a joint return, does not say to use the
  Department-adjusted carryover, does not exclude NYC UBT estimates (a self-employed NYC filer may count them as "City"
  payments), and does not mention estate/trust allocations. Each changes line 75 and so lines 76-80.
- Suggested fix: reword the source text to the instructions' list: New York State, New York City, Yonkers and MCTMT
  estimates (both spouses' on a joint return, including separate vouchers and separate IT-370 payments), the 2024
  overpayment as adjusted by the Department, estate/trust allocations; "do not include NYC unincorporated business tax
  payments". Optionally refuse when an estate/trust allocation is claimed (it needs the notification copy).

## H3 (high). Line 59 chart amount is not prorated for a part-year permanent place of abode

- Rule: ny_it201i p. 18, "If you maintained a permanent place of abode in New York State for sales and use tax purposes for only part of the year, multiply the tax amount from the chart by the number of months you maintained the permanent place of abode in New York State and divide the result by 12. (Count any period you maintained the abode for more than one-half of a month as one month.)"
- What the encoding does: `ny_it201.line59` enters `ny_it201.sut.chart` unprorated whenever
  `ny_it201.ask.owes_use_tax` is Yes. `ny_it201.ask.state_resident` accepts a domiciliary ("domiciled in New York
  State, or keeping a permanent place of abode..."), so a full-year income-tax resident who kept no New York abode for
  part of 2025 (domicile unchanged, for example a temporary assignment abroad) is completed with the full-year amount.
  The effect is at most the chart amount (≤ $125), but it is a wrong line 59.
- Suggested fix: ask "Did you maintain a permanent place of abode in New York State for all of 2025?" when
  `owes_use_tax` is Yes; refuse on No (or ask the month count and prorate per p. 18, rounding to the dollar).

## M1 (medium). Residency question does not carry the domiciliary exceptions (Groups A and B), the military, or the undergraduate-student rule

- Rules (ny_it201i p. 30, Resident / Permanent place of abode):
  - "Your domicile is New York State. However, even if your domicile is New York, you are not a resident if you meet all three of the conditions in either Group A or Group B as follows:" (Group A: no New York abode, an abode outside New York all year, 30 days or less in New York; Group B: 450 days abroad in 548 consecutive days, etc.)
  - "spend 184 days or more in New York State during the tax year*; whether or not you were domiciled in New York State (unless you were in active service in the military)"
  - "a residence maintained by a full-time student enrolled at an institution of higher education in an undergraduate degree program ... is not a permanent place of abode with respect to that student."
- What the encoding does: `ny_it201.ask.state_resident` (and `ny_it201.ask.city_resident`, "by the same test")
  asks "domiciled in New York State, or keeping a permanent place of abode ... and spending 184 days or more there?".
  A New York domiciliary who meets Group A or B is a nonresident (Form IT-203) but answers Yes on "domiciled" and gets
  a completed IT-201; a nondomiciled undergraduate in a dorm, or a nondomiciled servicemember, answers Yes on the
  statutory test and is treated as a resident.
- Suggested fix: add to the question "...unless you were domiciled in New York but met all three conditions of Group
  A or Group B (p. 30)", and exclude from the abode test an undergraduate's school residence and a servicemember in
  active service; or ask a separate Yes/No on the Group A/B exceptions and refuse (Form IT-203) on Yes.

## L1 (low). Return items the instructions require are not produced

- Rules:
  - ny_it201i p. 5, Item B, "If you itemized your deductions on your 2025 federal income tax return, mark an X in the Yes box. If you claimed the standard deduction on your federal return, mark an X in the No box."
  - ny_it201i p. 5, Item D1, "If you marked Yes on federal Schedule B (Form 1040), Interest and Ordinary Dividends, Part III then mark an X in the Yes box."
  - ny_it201i p. 5, Item D2, "All IT-201 filers must complete item D2."
  - ny_it201i p. 5, Item F, "New York City residents and part-year residents only: Enter in the applicable box the number of months you and your spouse (if filing a joint return) lived in New York City during 2025."
  - ny_it201i p. 11, Line 34, "mark an X in the appropriate box, Standard or Itemized."
  - ny_it201i p. 7, "Write each type of income and each adjustment and its amount in the Identify areas on lines 16 and 18."
- What the encoding does: only `ny_it201.item_c` and `ny_it201.item_h_count` exist; there is no line for items B, D1,
  D2 (the Yonkers answer is a screen, `ny_it201.ask.yonkers`, not an item entry), F (always 12 for the target), the
  Standard box, or the line 16/18 identify text. None changes an amount.
- Suggested fix: add output lines `ny_it201.item_b` (from the federal itemize choice), `item_d1` (federal Schedule B
  Part III answer), `item_d2_1`/`item_d2_4` (No, from the Yonkers screen), `item_f` (12), `line34_box` (Standard), and
  carry the federal line 8/24 descriptions to the identify areas, or list them in the reminder of fields to fill.

## L2 (low). Lines 37 and 38 shown as 0 where the instructions say to leave them blank

- Rule: ny_it201i p. 11, "If line 36 is more than line 35, leave line 37 and line 38 blank."
- What the encoding does: `ny_it201.line37` is `subtract_floor0`, so it prints 0 (and `ny_it201.line38` copies it).
  Amounts downstream are unaffected.
- Suggested fix: render 0 on lines 37/38 as blank when line 36 > line 35 (a presentation flag), or record the choice.

## L3 (low). Item A exceptions to the federal filing status are not asked

- Rule: ny_it201i p. 5, "You are unable to file a joint New York return because: – your spouse refuses to sign a joint New York return; ... In this case, you may file a separate New York return using filing status ③." (also the "address or whereabouts of your spouse is unknown" exception, same page)
- What the encoding does: every status-dependent line reads `f1040.status`; a federal joint filer whose spouse will
  not sign the New York return gets a joint IT-201. The joint return is not wrong in amount, but it cannot be filed in
  that case. (The resident/nonresident-spouse exception on p. 4 is already refused by `ny_it201.gate.spouse_nonresident`.)
- Suggested fix: on a joint federal return, ask whether the spouse will sign the New York joint return; refuse on No
  (a status ③ return with item H completed "as if you filed separate federal returns", p. 6).

## L4 (low). Form IT-2 foreign income record not covered

- Rule: ny_it201i p. 21, "If you received foreign income but did not receive a federal Form W-2, you must complete Form IT-2."
- What the encoding does: `ny_it2` has one record per federal W-2 only; foreign earned income without a W-2 produces
  no IT-2 entry. No IT-201 amount changes (lines 72-73 are unaffected).
- Suggested fix: ask whether any foreign income was received without a W-2 and refuse (or add the IT-2 foreign income
  record to the reminders).

## L5 (low). The Form IT-225 screen does not name subtractions the instructions point ordinary filers to

- Rules:
  - ny_it201i p. 32, Members of the armed forces, "However, see the instructions for Form IT-225, subtraction modification number S-118 for information on New York’s tax treatment of certain combat pay."
  - ny_it201i p. 7, "If you filed federal Form 4970, Tax on Accumulation Distribution of Trusts: ... do include on your Form IT-225, line 5 the amount of income you reported on Form 4970, line 1"
- What the encoding does: `ny_it201.ask.it225` is asked (so these are not unhandled in principle), but its examples
  name only pass-through modifications; a servicemember with combat pay has no prompt to answer Yes. The combat zone
  code C7 in `ny_it201.ask.special_code` covers only the filing extension.
- Suggested fix: add "military combat pay (S-118)" and "an accumulation distribution reported on federal Form 4970"
  to the question's examples.

---

## Checked and not reported

Item C, item H and line 36; standard deduction table; tax table / rate schedule / worksheets 1-16 selection; household
credit tables 1, 2, 4, 5 with negative AGI in the first row (tables 3 and 6, over-7, A6 refused); line 47 (Charitable
Gifts Trust Fund needs IT-196, refused by itemizing); line 47a joint-return rule (refused by the spouse screen); lines
50, 55-57 (refused by the NYC and Yonkers screens); MCTMT threshold; line 59 ST-141 cases; lines 60, 63-68, 70, 70a
(IT-270 conditions), 71-74, 78a, 79, 82; line 69/69a eligibility, income definition and rate reduction; NYC child care
credit for a child under 4 (any such child is under 17, so line 63's screen already refuses); filing-status exceptions
for a nonresident spouse; decedents; special accruals; SCRA elections (item G); NOL limitation (federal line 8a is
refused federally); the 110% safe harbor's farmer/fisherman exception (the encoding over-refuses, which is safe).
