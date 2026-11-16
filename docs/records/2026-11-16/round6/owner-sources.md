# Round 6, lane R1: source text for five owner questions

Lane R1. Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. The work was read-only: no builds,
engine runs or paid calls, and no edits to the repo or to any worktree. One curl to www.irs.gov
(`irs-drop/n-97-31.pdf`, see Q3) returned 404, and the HTML error page it saved was deleted.

**Conventions.**
- Quotes are verbatim from the archived extracted text, `sources/2025/<id>.cols.txt` unless another file is named.
- Page numbers are printed page numbers. For every document cited here they equal the PDF page; I checked this with
  `pdftotext -f N -l N` against the printed header or footer.
- [C] means checked against the artifact in this session. [I] means inferred. [R] means my recollection of a text that is
  not archived. An [R] is never relied on below; it only says what the owner should fetch.
- Main is `acde74b5`. The xint worktree (`.claude/worktrees/xint`) is at the same commit, plus the release-candidate
  forms that are not on main.

---

## Q1. `rental.div5` / `rental.div8`: are costs that serve only the rental divided by days?

**Decision at stake.** On a rental with personal-use days that was not used as a home, should advertising and
commissions (and similar costs of the rental activity alone) go to Schedule E in full, or be cut by
rental days ÷ total days?

**What the model does [C].** The form is `forms/2025/rental.yaml` on xint; it is not on main.
- The form note (lines 6-11) says: "Its expenses are divided by days when it had personal use but was not used as a
  home". It refuses "a home used personally and rented 15 days or more", so only the not-used-as-home case is computed.
- `rental.div5` (lines 517-529) is `prorate amount: rental.amt5_if_any, part: rental.fair_c, whole: rental.total_c`.
  `rental.line5` (lines 530-550) takes `div5` whenever `rental.personal_any` is true.
- `rental.div8` (lines 663-675) and `rental.line8` (lines 676-696) work the same way for commissions.
- Every other expense line has the same pattern: div7, div9 to div17, including management fees (`div11`, lines
  882-894).
- The division cite (`*id001`, lines 140-142) is "p527, p. 26, Dividing Expenses". The heading and its rule are on
  p. 25; the cottage example continues onto p. 26.
- Raised in `P/round5/personas.md:189-191`, which states the point as unchecked recollection ("A lead to check, not a
  finding").

**Source text.**

Pub. 527 (2025), "For use in preparing 2025 Returns". Chapter 5 opening, p. 25:
> If you have any personal use of a dwelling unit (including a vacation home) that you rent, you must divide your
> expenses between rental use and personal use. In general, your rental expenses will be no more than your total
> expenses multiplied by a fraction, the denominator of which is the total number of days the dwelling unit is used and
> the numerator of which is the total number of days actually rented at a fair rental price.

Pub. 527 (2025), p. 25, Dividing Expenses:
> If you use a dwelling unit for both rental and personal purposes, divide your expenses between the rental use and the
> personal use based on the number of days used for each purpose.

Pub. 527 (2025), p. 28, "Not used as a home." (the case the model computes):
> If you use a dwelling unit for personal purposes, but not as a home, report all the rental income in your income.
> Because you used the dwelling unit for personal purposes, you must divide your expenses between the rental use and
> the personal use, as described earlier in this chapter under Dividing Expenses. The expenses for personal use aren't
> deductible as rental expenses.

Pub. 527 (2025), pp. 23-24, chapter 4, Renting Part of Property. This is the space-based split, not the day-based one:
> You don't have to divide the expenses that belong only to the rental part of your property. For example, if you paint
> a room that you rent or pay premiums for liability insurance in connection with renting a room in your home, your
> entire cost is a rental expense.

Pub. 527 (2025), p. 24:
> How to divide expenses. If an expense is for both rental use and personal use, such as mortgage interest or heat for
> the entire house, you must divide the expense between rental use and personal use.

Pub. 527 (2025), Worksheet 5-1 (for a unit **used as a home**), Part II, p. 29:
> d. Enter direct rental expenses. See instructions
> e. Fully deductible rental expenses. Add lines 2a–2d. Enter here and on the appropriate lines on Schedule E.

The same worksheet, p. 29, line 4a:
> Enter the rental portion of expenses directly related to operating or maintaining the dwelling unit (such as repairs,
> insurance, and utilities)

Worksheet 5-1 Instructions, p. 30:
> Caution. Use the percentage determined in Part I, line F, to figure the rental portions to enter on lines 2a–2c, 4a–4c,
> and 6a–6b of Part II.

Worksheet 5-1 Instructions, p. 31, Line 2d:
> Enter the total of your rental expenses that are directly related only to the rental activity. These include interest
> on loans used for rental activities other than to buy, build, or improve the dwelling unit. Also, include rental agency
> fees, advertising, office supplies, and depreciation on office equipment used in your rental activity.

2025 Instructions for Schedule E (Form 1040), p. 5, Line 2 (the line's cite in the model):
> If you did not use the unit as a home, you can deduct all your expenses for the rental part, subject to the at-risk
> rules and the passive activity loss rules, explained earlier.
> …
> Regardless of whether you used the unit as a home, expenses related to days of personal use do not qualify as rental
> expenses. You must allocate your expenses based on the number of days of personal use to total use of the property.
> For example, you used your property for personal use for 7 days and rented it for 63 days. In most cases, 10% (7 ÷ 70)
> of your expenses are not rental expenses and cannot be deducted on Schedule E.

**Not archived.** IRC §280A(e) and Prop. Reg. §1.280A-3, the sources behind Worksheet 5-1's ordering. They are not on
www.irs.gov (uscode.house.gov; the Federal Register), so they were not fetched. [R] As I remember it, §280A(e)(1) limits
"expenses attributable to the rental of the unit" by the days fraction. Read literally, that wording could reach every
rental expense. I have not verified it.

**Reading. Moderate: rental-only costs are not divided.**
- No archived passage says, for the not-used-as-home case, that rental-only costs are left whole.
  - The general rules (pp. 25, 28) say "divide your expenses" with no carve-out.
  - The Schedule E example says "In most cases, 10% … of your expenses".
- Three passages point the other way, toward dividing only expenses that serve both uses:
  - Worksheet 5-1 line 2d puts "rental agency fees, advertising" in full ("Fully deductible", and not in the
    line-F list). It does this in the used-as-home case, which is the stricter regime. It would be odd for the more
    lenient case to divide them.
  - The Renting Part of Property rule: "don't have to divide the expenses that belong only to the rental part".
  - Schedule E's wording, "expenses related to days of personal use", which an advertising cost is not.
- Commissions paid to an agent who found a renter fit "rental agency fees" [I]. Management fees (`rental.div11`,
  xint `rental.yaml:882`) need the same check. Most of what management fees cover is upkeep of the unit, which the
  worksheet divides (line 4a).
- **What would change the reading:**
  - the text of §280A(e)(1) and Prop. Reg. §1.280A-3(d), if they require all rental expenses to be divided;
  - or an IRS statement that line 2d's treatment is confined to the used-as-home worksheet.

---

## Q2. `gift.unrelated_use` ("art or other belongings the charity will not use"): does it reach a thrift-store donor?

**Decision at stake.** Should the refusing item be confined to appreciated (capital gain) tangible property, so that a
donor of used clothing to a thrift store (FMV below cost) is not refused?

**What the model does [C].**
- **On main:** `forms/2025/gift.yaml:41-70` (`gift.special`) and `interview/2025/questions.yaml:366-389` list eight
  items. Neither has an unrelated-use item.
- **The item comes from the nightplan fix chain** (BUG-0818, `P/round4/lows-older.md:155-170`):
  - `P/scratch/b-chain/work/interview/2025/questions.yaml:975` has "it is art or other belongings the charity will not
    use for its charitable purpose".
  - `P/scratch/b-chain/work/forms/2025/gift.yaml:55,70` has "tangible personal property the charity puts to an
    unrelated use".
  - The cite at line 74 quotes p526 Exceptions.
- **The round-5 patch `P/patches/v4/tf-a-f1.patch`** splits it out as `gift.unrelated_use` (line 123), with the tick
  "Art or other belongings the charity will not use for its purpose" (line 381). A Yes refuses through `gift.special`.
- **Raised in** `P/round5/trimfollow.md:28-32`. It notes that the item is pre-existing in the chain and was not
  narrowed (N9).
- **The deduction itself is an input**, `gift.deduction` (`forms/2025/gift.yaml:10-28`): "after required
  valuation/basis reductions". The refusal exists so that the filer is not left to apply the basis rule.

**Source text.**

Pub. 526 (2025) (printed date 2026-02-05 per the manifest), p. 18, Giving Property That Has Decreased in Value:
> If you contribute property with an FMV that is less than your basis in it, your deduction is limited to its FMV. You
> can't claim a deduction for the difference between the property's basis and its FMV.
> …
> Common examples of property that decrease in value include clothing, furniture, appliances, and cars.

Pub. 526 (2025), p. 18, Giving Property That Has Increased in Value:
> If you contribute property with an FMV that is more than your basis in it, you may have to reduce the FMV by the
> amount of appreciation (increase in value) when you figure your deduction.

Pub. 526 (2025), p. 19, Capital Gain Property:
> Property is capital gain property if you would have recognized long-term capital gain had you sold it at FMV on the
> date of the contribution.
> …
> Amount of deduction—general rule. When figuring your deduction for a contribution of capital gain property, you can
> generally use the FMV of the property.
>
> Exceptions. However, in certain situations, you must reduce the FMV by any amount that would have been long-term
> capital gain if you had sold the property for its FMV. Generally, this means reducing the FMV to the property's cost or
> other basis. You must do this if:
> …
> 5. The contributed property is tangible personal property (defined earlier) that:
> a. Is put to an unrelated use (defined later) by the charity; or

Pub. 526 (2025), p. 20:
> Unrelated use. The term "unrelated use" means a use unrelated to the exempt purpose or function of the qualified
> organization. …
> Example. If a painting contributed to an educational institution is used by that organization for educational purposes
> by being placed in its library for display and study by art students, the use isn't an unrelated use. But if the
> painting is sold and the proceeds are used by the organization for educational purposes, the use is an unrelated use.

Pub. 526 (2025), p. 17, Used clothing:
> You should claim as the value the price that buyers of used items actually pay in used clothing stores, such as
> consignment or thrift shops.
> Example. You donated a coat to a thrift store operated by a place of worship. You paid $300 for the coat 3 years ago.
> Similar coats in the thrift store sell for $50. The FMV of the coat is $50. Your donation is limited to $50.

Instructions for Form 8283 (Rev. December 2025), pp. 3-4, Reductions to contribution:
> You usually may deduct gifts of capital gain property at their FMV. However, you must reduce your deduction amount by
> the amount of any appreciation if any of the following apply. … • The contributed property is tangible personal
> property that is put to an unrelated use (as defined in Pub. 526) by the charity.

**Not archived.** IRC §170(e)(1)(B)(i) is not on www.irs.gov. [R] As I remember it, the reduction there is the gain that
"would have been long-term capital gain", which agrees with Pub. 526. Not verified.

**Reading. Strong: the unrelated-use rule reduces only appreciation on capital gain property.**
- Pub. 526 and i8283 both place it under capital gain property as a reduction "by any amount that would have been
  long-term capital gain" / "by the amount of any appreciation".
- Used clothing worth less than it cost has no appreciation. Its deduction is already FMV (p. 18, p. 17 example), so
  the rule changes nothing.
- A thrift store's resale is plausibly an "unrelated use" under the p. 20 painting example. So a Goodwill donor can
  truthfully answer Yes to the current wording, and the refusal has no tax effect for them [I].
- Narrowing the item to "worth more than you paid, held over a year" would match the text. Ordinary income property
  (held a year or less, or self-created art) is already limited to basis by its own rule (p. 19).
- **Whether to narrow** is a design and N9 choice. The text supports it but does not require it.
- **What would change the reading:** a source extending the unrelated-use reduction to property without gain. I found
  none in p526, i8283 or i1040sca.

---

## Q3. Owner decision 8, `amb.2025.f8853c_line24_public`: are Medicaid or VA payments to the provider line 24 reimbursements?

**Decision at stake.** On Form 8853 Section C, line 24 lowers the per diem limit (line 25 = line 23 − line 24). Should
Medicaid or VA payments made straight to the nursing home or care provider count as "reimbursements"?

**What the model does [C].**
- **The form** is `forms/2025/f8853c.yaml` on xint; it is not on main.
- **Line 24** (lines 391-404) is an input: "The reimbursements you … received or expect to receive, through insurance or
  otherwise, … (payments made to repay costs, not the payments at a set rate)".
- **Line 24 prompt** (xint `interview/2025/questions.yaml:4227-4231`): "How much of those care costs was paid back to
  you, by insurance or otherwise?"
- **Line 22 help** (same file, 4221-4226): "Count what the care cost for those days, such as nursing home or home care
  bills, **whoever paid them**." So line 22 counts gross cost, including any part a public program paid.
- **The register entry** `amb.2025.f8853c_line24_public` is not on main or xint. It exists in the fix-chain patch
  `P/patches/v3/fix-round.patch:148-162` (also `P/patches/v2/inc-m34.patch`). It chooses "They are; they count on line
  24".
- **Framing:** `P/MORNING-REPORT.md:163-165` (decision 8, "Rec.: confirm"), `P/lane-briefs.md:379,820` (OD-6) and
  `P/med-income.md:275-305` (BUG-0873). The proposed wording deliberately does not name Medicaid or the VA.
- `P/round4/lows-inc.md` does not discuss line 24. Its 8853 items are BUG-0916 (line 22) and BUG-0917 (line 25).

**Source text.**

Instructions for Form 8853 (2025), p. 9, Line 24:
> Enter the reimbursements you received or expect to receive through insurance or otherwise for qualified LTC services
> provided for the insured for LTC periods in 2025. Box 3 of Form 1099-LTC should indicate if payments were made on a
> reimbursement basis.
>
> Caution: Generally, don't include on line 24 reimbursements for qualified LTC services you received under a contract
> issued before August 1, 1996. …

i8853 (2025), p. 9, Line 22:
> Qualified LTC services are necessary diagnostic, preventive, therapeutic, curing, treating, mitigating, and
> rehabilitative services, and maintenance or personal care services required to treat a chronically ill individual
> under a plan of care prescribed by a licensed health care practitioner.

i8853 (2025), p. 10, Example 1. This is the only worked case, and it uses insurance reimbursement:
> Alex incurred expenses for qualified LTC services of $150 per day ($54,750) and was reimbursed for one-half of those
> expenses ($27,375).

Form 8853 (2025), line 22 and lines 24-25:
> Costs incurred for qualified LTC services provided for the insured during the LTC period
> Reimbursements for qualified LTC services provided for the insured during the LTC period
> Per diem limitation. Subtract line 24 from line 23

Pub. 525 (2025), p. 19, Long-Term Care Insurance Contracts, Limit on exclusion:
> Under this limit, the excludable amount for any period is figured by subtracting any reimbursement received (through
> insurance or otherwise) for the cost of qualified long-term care services during the period from the larger of the
> following amounts. • The cost of qualified long-term care services during the period. • The dollar amount for the
> period ($420 per day for any period in 2025).

**Searched and absent [C].** "Medicaid" and "Veterans"/"VA" appear nowhere in i8853 or f8853. In p525 they appear only
in unrelated contexts: veterans' benefits exclusion (p. 525 lines 577-580), Medicaid waiver payments (line 1126).
p502 has no Medicaid passage.

**Not archived or not obtainable.**
- IRC §7702B(d) is not on www.irs.gov. [R] As I remember it, §7702B(d)(2)(B) reads "payments received as reimbursement
  (through insurance or otherwise)", the same phrase as Pub. 525. Not verified.
- IRS Notice 97-31 (guidance on qualified LTC contracts): `https://www.irs.gov/pub/irs-drop/n-97-31.pdf` returned 404.
  I do not know whether it addresses public programs.

**Reading. Moderate that the text reaches third-party payments of the costs counted on line 22. Weak on the specific
point of payments made straight to the provider.**
- "Through insurance or otherwise" is unrestricted, in i8853, Pub. 525 and (per [R]) the statute.
- The structure supports netting. Line 23 takes the larger of the $420/day amount and line 22's "costs incurred". If
  line 22 includes costs Medicaid or the VA paid (as the model's line 22 help says, "whoever paid them"), leaving those
  payments off line 24 inflates the cost-based limit [I].
- The counter-text is "you received or expect to receive". A payment made straight to the provider was not received by
  the filer. A reader could take line 22 to mean only costs the filer bore, and line 24 to mean only what came back to
  the filer.
- **The two lines must be read consistently:**
  - either both include the public-program payments (the v2 reading),
  - or neither does (line 22 net of them, line 24 without them).
  - Either pair gives the same line 25 whenever line 22 exceeds the $420/day figure.
  - They differ when line 21 ($420/day) is the larger: then counting the payments on line 24 lowers the limit, and not
    counting them does not.
- On the current xint wording the lines are inconsistent: line 22 is gross, while line 24 asks only what was "paid back
  to you".
- **What would change the reading:** the §7702B(d) text, Treasury regulations or IRS guidance on "reimbursement … or
  otherwise", or an IRS example with a public payer.

---

## Q4. S corporation K-1 box 17 codes A and B: do they need a twin of the partnership `f4952.k1_inv` refusal?

**Decision at stake.** k1block unit 6 refuses Form 4952 when a partnership K-1 shows box 20 A/B and investment interest
is claimed. S corporation box 17 A/B is neither refused nor carried. The question is whether to add a twin (O-1 in
`P/round5/k1block.md:378-383`, finding (b) at lines 47-49).

**What the model does [C].**
- **xint `forms/2025/k1s.yaml:921-932`:** `k1s.box17_other` asks "Does box 17 of this Schedule K-1 show any code other
  than A, B, V or AC?", so A and B pass with no question and no refusal. Its cite already quotes "Code A. Investment
  income. Report this amount on Form 4952, line 4a".
- **xint `k1s.yaml:1789-1795`:** a Yes on box 11 or box 12 refuses. Box 12 code H (investment interest expense) is
  therefore always refused for S corporation K-1s.
- **xint `forms/2025/f4952.yaml:161-173`:** `f4952.unsupported` refuses on, among other things, "any deductible
  investment expense other than interest (… or investment expenses on a Schedule K-1); or any other investment income or
  expense beyond interest, dividends and securities sales".
- **Partnership side:** xint `forms/2025/k1p.yaml:685-694` (`k1p.has_b20ab`). The refusal `f4952.k1_inv` exists only in
  the k1block unit 6 patch, not on xint.

**Source text.**

2025 Shareholder's Instructions for Schedule K-1 (Form 1120-S), p. 15, Box 17. Other Information:
> Code A. Investment income. Report this amount on Form 4952, line 4a.
> Code B. Investment expenses. Report this amount on Form 4952, line 5.

i1120ssk (2025), p. 11, Box 12, Code H:
> Code H. Investment interest expense. Report this amount on Form 4952, line 1. If the corporation has investment income
> or other investment expense, it will report your share of these items in box 17 of Schedule K-1 using codes A and B.
> Include investment income and expenses from other sources to figure how much of your total investment interest is
> deductible.

2025 Partner's Instructions for Schedule K-1 (Form 1065), p. 27 (the partnership counterpart):
> Code A. Investment income. Report this amount on Form 4952, Part II, line 4a.
> Code B. Investment expenses. Report this amount on Form 4952, Part II, line 5.

Form 4952 (2025), instructions p. 3, Line 4a:
> Include investment income reported to you on Schedule K-1 from a partnership or an S corporation.

Form 4952 (2025), instructions p. 4, Line 5:
> Investment expenses are your allowed deductions, other than interest expense, directly connected with the production
> of investment income. … Include investment expenses incurred directly by you or reported to you on Schedule K-1 from a
> partnership, or by an S corporation, but only if you are allowed a deduction on your return for the expense. …
> Don't include any miscellaneous itemized deductions, which aren't allowed deductions in tax years beginning after
> December 31, 2017, and before January 1, 2026.

**Reading.**
- **Strong** that the instructions route S-corp 17A/17B exactly as partnership 20A/20B: to Form 4952 lines 4a and 5.
  Form 4952 names both entity types together.
- **Moderate** that a twin is logically needed. Whatever made the partnership refusal necessary applies to box 17 A/B in
  the same way. Three facts change how much it matters:
  1. Box 12 H (S-corp investment interest) is already refused, so the gap reaches only filers with their own
     investment interest who also hold an S-corp K-1 with 17A/B.
  2. A missing 17A understates line 4a and so understates the deduction, which is against the filer. A missing 17B can
     overstate it. But line 5 takes only expenses "allowed" on the return, and miscellaneous itemized deductions are not
     allowed for 2025, so many 17B amounts contribute nothing [I: what 17B usually holds is not shown in the archived
     text].
  3. The existing `f4952.unsupported` question already names "investment expenses on a Schedule K-1" and "other
     investment income". A filer who reads it closely is refused there; the gap is one of recall, not of logic [I].
- **What would change the reading:** nothing in the text. The choice among O-1's (a), (b) and (c) is design.

---

## Q5. Form 8615 child AMT cap: which children does it reach?

**Decision at stake.** The f8615 patch caps the Form 6251 exemption at earned income + $9,550. Does the cap reach every
child who meets §1(g)(2)'s age, parent and joint-return tests (reading 1, chosen), or only children who file Form 8615
(unearned income over $2,700)? This is finding 2 at `P/round5/f8615.md:43-46`.

**What the model does [C].**
- **Not on main or xint.** It is only in `P/patches/v4/f8615-form.patch`:
  - `s2.amt_kiddie` at line 2485;
  - `f8615.child_1g` at line 1266;
  - `amb.2025.amt_kiddie_child` at line 139.
- **In the applied copy** `P/scratch/round5-f8615/form/b/`:
  - `forms/2025/s2.yaml:850-873`: `s2.amt_kiddie_over` is "line 4 at its largest > earned + $9,550"; then
    `s2.amt_kiddie` reads `f8615.child_1g`.
  - `forms/2025/f8615.yaml:174-196`: `child_1g` = under 24 and not joint, then `f8615.kid` (conditions 3 and 4).
  - `ambiguities/2025.yaml:2841-2857`: chosen "whatever the amount of unearned income".
- **Reach is narrower than the label [I, from `P/round5/f8615.md:116-119`].** The support, student and parent questions
  behind `f8615.kid` are "reached only by a filer under 24, not filing jointly, with more than $2,700 of line 1".
  - For a child at or below $2,700, `kid` may therefore rest on its gated default (false), whatever the register says.
  - I did not trace the gate default. Check it before the owner relies on reading 1 being in force.

**Source text.**

Rev. Proc. 2024-40, §3.12, p. 11 (archived `rp-2024-40.txt:408-416`):
> .12 Alternative Minimum Tax Exemption for a Child Subject to the "Kiddie Tax." For taxable years beginning in 2025,
> for a child to whom the § 1(g) "kiddie tax" applies, the exemption amount under §§ 55(d) and 59(j) for purposes of the
> alternative minimum tax under § 55 may not exceed the sum of (1) the child's earned income for the taxable year, plus
> (2) $9,550.

Instructions for Form 6251 (2025): **silent [C].**
- Neither i6251 nor f6251 (2025) contains "child", "kiddie", "1(g)", "8615" or "9,550" (checked with `pdftotext` and
  grep on both PDFs).
- The only child mention is the Form 8814 tax-exempt interest line.
- The Exemption Worksheet (i6251 p. 9) gives only $88,100 / $137,000 / $68,500, with the phase-out at $626,350 /
  $1,252,700.

Instructions for Form 8615 (2025), p. 2, Alternative Minimum Tax (AMT). This is the only AMT text in the 8615 sources:
> A child may be subject to AMT if the child has certain items given preferential treatment under the tax law. These
> items include accelerated depreciation and certain tax-exempt interest income.
> The AMT may also apply if you have passive activity losses or certain distributions from estates or trusts.
> For details, see Form 6251, Alternative Minimum Tax—Individuals, and its instructions.

i8615 (2025), p. 1, Who Must File:
> Form 8615 must be filed for any child who meets all of the following conditions.
> 1. The child had more than $2,700 of unearned income.
> 2. The child is required to file a tax return.
> 3. The child either:
> a. Was under age 18 at the end of 2025,
> b. Was age 18 at the end of 2025 and didn't have earned income that was more than half of the child's support, or
> c. Was a full-time student at least age 19 and under age 24 at the end of 2025 and didn't have earned income that was
> more than half of the child's support.
> …
> 4. At least one of the child's parents was alive at the end of 2025.
> 5. The child doesn't file a joint return for 2025.
> For these rules, the term "child" includes a legally adopted child and a stepchild. These rules apply whether or not
> the child is a dependent.

**Not archived.** IRC §1(g)(2) and §59(j) are not on www.irs.gov, so they were not fetched. [R] As I remember them:
- §59(j)(1) applies "[i]n the case of a child to whom section 1(g) applies", and caps the exemption at earned income
  (as §911(d)(2) defines it) plus an indexed $5,000.
- §1(g)(2) says the subsection "shall apply to any child" meeting the age/support, living-parent and no-joint-return
  tests, with no unearned-income amount.
- Not verified. This is the text that would decide the question.

**Reading. Moderate for reading 1** (every §1(g)(2) child, whatever the unearned income).
- The Rev. Proc. ties the cap to "a child to whom the § 1(g) 'kiddie tax' applies", not to a Form 8615 filer.
- i8615's $2,700 condition is a condition for *filing Form 8615*, listed separately from conditions 3 to 5.
- The 2025 IRS forms and instructions give a preparer no way to apply the cap at all, so they cannot settle the scope.
- Reading 1 also reaches non-dependent students aged 19 to 23 ("whether or not the child is a dependent").
- **What would change the reading:** the text of §1(g)(2) and §59(j). If §59(j) or §1(g) conditioned application on
  net unearned income exceeding the threshold, reading 2 would follow.

---

## Form 8615 sources: printed revision and locator (information only; manifest not edited)

Current manifest entries [C]:
- `f8615`, `sources/2025/manifest.json:1464`: revision "2025; created 2025-09-09 …", revision_locator
  `printed "Form 8615 (2025) Created 9/9/25"`.
- `i8615`, `sources/2025/manifest.json:3423`: revision "2025 …", revision_locator
  `printed "Instructions for Form 8615 (2025)"`.
- Both have revision_status "archived for form designations and purposes, not cleared for encoding".

Visible in the archived extracted text [C]:

| id | Printed revision / date | Locator (style of the cleared entries) |
|---|---|---|
| f8615 | 2025; created 9/9/25 | Page 1 heading, 2025 (`f8615.txt:6`); footer "Cat. No. 64113U Form 8615 (2025) Created 9/9/25" (`f8615.txt:59`, `f8615.cols.txt:73`). A one-page form. |
| i8615 | 2025; printed Oct 22, 2025 | Page 1 title, "2025 Instructions for Form 8615" (`i8615.txt:1-2`); page 1 footer, "Instructions for Form 8615 (2025) Catalog Number 28914R" and "Oct 22, 2025" (`i8615.txt:74-75`, `i8615.cols.txt:44-45`) |

Suggested text in the style of `f1120ssk` / `i1065sk1` [I]:
- `f8615`: revision_locator `Page 1 heading, 2025; "Form 8615 (2025) Created 9/9/25"`.
- `i8615`: revision `2025; printed date 2025-10-22`; revision_locator
  `Page 1 title, "2025 Instructions for Form 8615"; page 1 footer "Oct 22, 2025"`.

PDF metadata, for information:
- f8615.pdf: CreationDate 2026-01-13.
- i8615.pdf: CreationDate 2025-10-22, ModDate 2026-01-22.
- The printed dates above are the revision markers. The metadata dates reflect irs-prior re-posting [I].

Changing revision_status to cleared is a source-lane or owner action. It is outside this lane.
