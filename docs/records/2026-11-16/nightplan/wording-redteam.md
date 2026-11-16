# Wording red-team of the four fix plans (lane wording-redteam)

claude-opus-5-5, judgment, year 2025, us and ny. Read only. Plans reviewed: `/tmp/nightplan/med-income.md`,
`med-older.md`, `med-k1sche.md`, `interview.md`. Tree read: `.claude/worktrees/xint` (paths below are relative to it).
**[C path:line]** = checked against that file in this session. **[I]** = my inference, not read in a source.
Word counts are by hand, whitespace split, frame included. No build, walk, engine or model call was run.

## Summary (findings that change a value first)

Fourteen proposals would give a wrong value or a wrong printed answer if a patch lane applies them as written, or keep
a wrong value that the fix touches. Three of them are clashes between plans (two lanes patching the same entry
differently). Corrected wording for each is in section A.

| # | Plan / entry | Wrong value | Who |
|---|---|---|---|
| A1 | k1sche BUG-0775 cost frame | rental deducts personal months; Sch A double counts | home that turned into a rental, or a rental that turned into a home |
| A2 | interview.md `rental.personal_any` help | vacation-home limit skipped, rental loss allowed | lived there, rented under 12 months |
| A3 | BUG-0907 in **two** plans | suspended passive loss deducted as NOL (k1sche text) / true rental NOL dropped (income text) | landlords |
| A4 | interview.md new heading "get either of these" | dividends dropped | long-time shareholder who bought nothing in 2025 |
| A5 | income BUG-0873 line 24 "anyone else" | taxable LTC per diem overstated | family or Medicaid paid the home |
| A6 | income BUG-0833 "latest Form 4952 filed" | investment interest carryover overstated | took the standard deduction in 2024 |
| A7 | older BUG-0815 help "box 14 or 19"; drops SUI | local tax counted twice; NJ/PA/AK SUI dropped | W-2 with city tax; NJ/PA workers |
| A8 | older BUG-0851 moves K-12 out of the prompt | NY line 22 addition missed | parent paying private-school tuition from NY 529 |
| A9 | income BUG-0806 keeps "restaurant, bar and hotel staff" | tips deduction allowed | restaurant or hotel manager |
| A10 | income BUG-0896 crypto help/prompt | wrong printed 1040 digital-asset answer | got crypto only as a gift |
| A11 | BUG-0790 in **two** plans | conflicting patches; k1sche version computes boats | boat owners |
| A12 | older BUG-0861 help | dependent's required filing missed, PTC overstated | dependent 65+ or blind with both kinds of income |
| A13 | income BUG-0904 help keeps "other person's own home" | Medicaid waiver pay taxed | caregiver living in the cared-for person's home |
| A14 | income BUG-0808 gambling help keeps "prizes such as a car" | contest prize on 8b, gambling losses offset it | contest winner with gambling losses |

Also: one more cross-plan clash in section B (k1s spouse wording), six misreading risks, and the N10 overruns. Section E
lists the proposals I checked and found sound, so the reader knows what was covered. Two factual corrections to the
plans: **p544 is archived** (med-income says it is not; its 0822 guard is confirmed, `sources/2025/p544.cols.txt:134`).
The i1040sca withholding sentence that med-older did not re-grep is confirmed (`sources/2025/i1040sca.cols.txt:84`).

---

## A. Wrong value or wrong printed answer (patch lanes: read these first)

### A1. BUG-0775 (med-k1sche): the cost frame says "from when you first rented it"

- **Defect in the proposal.** The frame reads "only the part for the time from when you first rented it or offered it
  for rent". `rental.days_personal` covers both directions: main-home days "before *or after* renting it out"
  [C forms/2025/rental.yaml:115-117]. For a rental that **became** the filer's home mid-2025, "from when you first
  rented it" runs to December 31 and includes the personal months. That is a wrong deduction. It also contradicts the
  plan's own amt12 and amt16 help, which says "for the time in 2025 it was rented or offered for rent".
- Source: "You can deduct as rental expenses only the part of the expense that is for the part of the year the
  property was used or held for rental purposes" [C sources/2025/p527.cols.txt:745].
- **Second defect: the Schedule A counterpart is required, not optional.** Once amt12 says "Interest for the time it
  was your home goes with your home mortgage interest", the Schedule A question still says "Add boxes 1 and 6 of each
  Form 1098" [C interview/2025/questions.yaml:1343-1344]. The filer enters the full box 1 there and the rental part on
  amt12, so the rental months are deducted twice. The plan calls it optional and claims the risk without it is only
  an understatement. The risk is an overstatement. The same applies to real estate tax (amt16 and the Schedule A
  property-tax amount) [I: the property-tax entry was not read].
- **Corrected (verbatim).**
  - Frame (heading help or first cost item): "If it was your home for part of 2025, enter for each yearly cost
    (insurance, taxes, mortgage interest and so on) only the part for the days in 2025 it was rented or offered for
    rent."
  - `sa.mortgage_interest` help, add (must land in the same lane or the same merge as amt12): "If this home was rented
    or offered for rent for part of 2025, count only the interest for the rest of the year; the rental part is asked
    with the rental."
  - The Schedule A property-tax amount help, add: "If the home was rented or offered for rent for part of 2025, count
    only the tax for the rest of the year."
  - Coverage row: also add the reverse case (rented January to May, then lived in), expecting 5/12 of the costs.

### A2. interview.md `rental.personal_any` help drops "for 12 months or more"

- **Defect.** The proposed help says: "Not personal use: … days it was your main home before or after renting it out."
  The current help says "… renting it out (or trying to) for 12 months or more" [C questions.yaml:6924-6926], and so
  does the child's source [C rental.yaml:115-117]. A filer who lived there and rented it for 4 months reads the new
  help and answers the **parent** No, so the child that carries the condition is never asked. Personal days become 0,
  and the more-than-14-days / 10% vacation-home limit is not applied, so a rental loss is allowed wrongly.
- Source: personal use includes "You or any other person who owns an interest in it … However, see Days used as a main
  home before or after renting" [C p527.cols.txt:870]; the 12-month rule is in the child's source, as cited.
- The plan's reason for dropping text ("the child now carries it") holds for the repair-days clause only.
- **Corrected (verbatim, 44 words; keep the 12-month clause and drop only the repairs clause):** "Family means a spouse,
  parent, grandparent, child, grandchild, brother or sister. Not personal use: family renting at a fair rent as their
  main home, and days it was your main home before or after renting it out (or trying to) for 12 months or more."
  (p527 also counts half-siblings [C p527.cols.txt:871]; add "half brothers and sisters count" only if the lane
  accepts about 49 words.)

### A3. BUG-0907: two plans patch `scope.nol` help differently

- med-k1sche (lane A) says "Fix: the entry's help text", and the entry names rentals and K-1 losses
  [C med-k1sche.md:333-338]. med-income (lane M2) rewrites it to drop "rentals" and adds an 8582 guard.
- **The k1sche version gives a wrong value.** A landlord whose rental losses are suspended on Form 8582 reads
  "rentals" and enters them on `s1.nol_amount`, which deducts a suspended passive loss on line 8a [I, from the 8582
  carryover rules].
- **The med-income version gives the opposite wrong value.** A true rental NOL, from a loss that was allowed and
  exceeded that year's income, now reads as No (its owner decision 6). i172 lists rental property as an NOL source
  [C per med-income, i172.cols.txt:16].
- **Corrected (verbatim, 41 words). It resolves owner decision 6 without a refusal:** "A loss bigger than that year's
  income, not yet used up, from a business, farm, rental or disaster; or a business loss held back by the yearly limit
  (Form 461). A loss still held back on Form 8582 is not one."
- `s1.nol_amount` help (as med-income): "Leave out losses held back on Form 8582 or by basis or at-risk limits."
- **Assign 0907 to one lane only** (M2 in med-income). Remove it from k1sche lane A.

### A4. interview.md: the new screen heading "get either of these" over "Shares or a fund"

- **Defect.** The proposed heading is "In 2025, did you (or, on a joint return, your spouse) get either of these?", and
  the `div.any` tick is "Shares or a fund outside a retirement account, or a Form 1099-DIV". The source of `div.any` is
  "**own** shares … or get a Form 1099-DIV" [C forms/2025/div.yaml:368]. "Did you get … shares" reads as "did you
  acquire shares in 2025". A holder of long standing whose broker did not send a separate 1099-DIV (or who has not
  opened it) answers No, and all dividends are dropped. 21% of returns have dividends [C per interview.md,
  gate_frequencies.yaml:184-207].
- **Corrected (verbatim):** heading "In 2025, did you (or, on a joint return, your spouse) have either of these?";
  `div.any` tick "Shares or funds owned outside a retirement account, or a 1099-DIV" (11 words); the
  `f1040.tax_exempt_any` tick unchanged, "Tax-exempt interest, such as from a city or state bond".
- Checked and sound in the same proposal: line 2a = TE + `div.box12` [C forms/2025/f1040.yaml:236-239], so the box-12
  routing in the tick help is right.

### A5. BUG-0873 (med-income): line 24 "paid by insurance or anyone else"

- **Defect.** i8853 line 24: "Enter the reimbursements you received or expect to receive through insurance or
  otherwise for qualified LTC services" [C sources/2025/i8853.cols.txt:275]. "Anyone else" invites a child who paid a
  parent's nursing home, or Medicaid or the VA, to be counted. Line 24 rises, the cost-based limit falls, and the
  taxable per diem on line 26 is overstated [I, from the line 26 arithmetic]. It also contradicts the plan's own
  decision to leave Medicaid and the VA unnamed until the owner rules ("anyone else" includes them).
- **Corrected (verbatim):** prompt "How much of those care costs was, or will be, paid back by insurance, to you or
  straight to the care provider? Leave out the payments at a set rate." (29 words); help, new: "Money family or friends
  gave toward the care is not counted." Medicaid and the VA stay with owner decision 3 (an ambiguity entry), as the
  plan intends.
- Also checked: pre-1996 help "Count a policy first issued then even if it was later exchanged or changed" is
  **wider** than the source, which says a contract "exchanged or modified after July 31, 1996, to increase per diem
  payments" is **not** excluded [C i8853.cols.txt:277]. Because a Yes refuses, this only loses cases; it is acceptable.

### A6. BUG-0833 (med-income): "line 7 of the latest one filed" and "could not be deducted"

- **Defect 1 (no source, value-changing).** Form 4952 line 2 is "Disallowed investment interest expense from 2024 Form
  4952, line 7" [C sources/2025/f4952.cols.txt:10]. p550: "You can carry over the amount of investment interest you
  could not deduct **because of this limit**" [C sources/2025/p550.cols.txt:1471]. In a 2024 standard-deduction year,
  the 2023 carryover became 2024 investment interest, and only its excess over 2024 net investment income carried on.
  "Latest one filed" carries all of it, which overstates the deduction [I: the reading of 1471 applied to a standard
  deduction year; no archived source addresses that year directly].
- **Defect 2.** The new prompt, "investment interest from before 2025 that could not be deducted and is still unused",
  invites a 2024 standard-deduction filer to report their own 2024 margin interest ("I could not deduct it").
- **Corrected.** Keep the current, source-faithful `f4952.carryover` prompt [C questions.yaml:651-652] and the
  current `prior_7` help. Do not ship "latest one filed". For the no-2024-form case, either (a) a refusing child,
  `f4952.carry_no_2024_form`: "Was investment interest carried into 2024 from an earlier year, with no Form 4952 filed
  for 2024?", help "A Yes ends the interview here." (model change; owner); or (b) an ambiguity entry with no wording
  change. The `f4952.line1` rewrite is sound (see E).

### A7. BUG-0815 (med-older): the other-state-tax help

- **Defect 1.** The proposed help keeps "(W-2 box 14 or 19)" (the current help has it too [C questions.yaml:1550-1552]).
  W-2 box 19 is local income tax, already counted in `sa`'s withheld-from-pay amount: "boxes 17 and 19 of each Form
  W-2" [C forms/2025/sa.yaml:514-518]. A filer with city tax reads "box 19" here and counts it again.
- **Defect 2.** The proposal says "disability or family leave fund" and drops the state **unemployment** fund. i1040sca
  lists "Mandatory contributions to the Alaska, California, New Jersey, or Pennsylvania state unemployment fund"
  [C i1040sca.cols.txt:85]. NJ and PA workers would answer No, which understates line 5a.
- **Defect 3 (prompt).** "Estimated payments" with no date. Only "estimated tax payments made during 2025" count
  [C i1040sca.cols.txt:84]. The January 2026 fourth payment is the classic mistake, and the federal help in BUG-0897
  tells the filer to count the January 2026 payment for **federal**.
- **Corrected (verbatim).** Help, 40 words: "Count tax taken out of a pension, IRA, unemployment pay, winnings, 1099-NEC or
  1099-MISC; a past refund applied to 2025; a required disability, unemployment or family leave fund from pay (SDI,
  SUI, FLI); territory tax; a charity tax credit applied." Prompt: "…such as estimated payments made in 2025
  (including an earlier year's refund applied to 2025) or a payment with a state return…". (The Washington
  supplemental workers' compensation fund [C i1040sca.cols.txt:85] is dropped by both versions; it is rare.)

### A8. BUG-0851 (med-older): NY 529 nonqualified prompt moves K-12 tuition into help

- **Defect.** The current prompt says "School tuition before college and a move to another state's plan count"
  [C interview/ny/2025/questions.yaml:150-151]. The plan moves "school tuition before college" to help. NY: a
  withdrawal for tuition "at elementary or secondary public, private, or religious schools" is nonqualified
  [C sources/ny/2025/ny_it201i.txt:472-478, right column]. A parent who paid private high-school tuition reads "anything
  but college … career training" and thinks "school is education", answers No, and the line 22 addition is missed.
- Also: student loans are qualified only for the beneficiary or a sibling, and credentialing only "at an eligible
  educational institution on or after July 4, 2025" [C ny_it201i.txt:515-521, left column].
- **Corrected (verbatim).** Keep the current prompt unchanged. Help, 41 words: "Career training is No only if paid to
  a college or other eligible school from July 4, 2025; loans only the student's or a sibling's. A Roth IRA or ABLE
  rollover, or money taken out after the student died or became disabled, is No." (The current sentence on transfers
  between family members' NY accounts can stay if about 55 words is accepted; the source supports it
  [C ny_it201i.txt:531-534].)

### A9. BUG-0806 (med-income): the tipped-occupation examples

- **Defect (from before tonight; the proposal keeps it).** "Restaurant, bar and hotel staff … are on it." The Treasury
  list has no manager or supervisor occupation (0 hits for "manager" or "supervis" in
  [C sources/2025/tipped-occupations.txt]). A restaurant or hotel manager who gets tip-outs answers Yes, then passes
  `tipjob.other_work` ("other work … not on that list") because they believe they are restaurant staff, and the tips
  are deducted on Schedule 1-A.
- **Corrected (verbatim, 39 words):** "Did you get any of these tips for work on the IRS list of jobs that customarily get
  tips? Servers, bartenders, cooks, hotel housekeepers and desk clerks, hairdressers, and taxi and delivery drivers are
  on it; managers are not." Each named job checked: [C tipped-occupations.txt:245-252, 272-273, 301, 321, 323].
  The plan's help (33 words) is sound.

### A10. BUG-0896 (med-income): the printed digital-asset answer

- **Defect (from before tonight; the fix is the place to correct it).** i1040gi: Yes if you "(a) received (as a reward,
  award, or payment for property or services); or (b) sold, exchanged, or otherwise disposed of" a digital asset
  [C sources/2025/i1040gi.cols.txt:291]. The prompt asks whether you "receive, sell, trade, spend or give away" crypto
  [C questions.yaml:3899-3900], so someone who only **received a gift** of crypto answers Yes, and Form 1040 prints
  the wrong answer. The proposed help does not say otherwise. That a gift recipient is a No is [I], read from the (a)
  definition.
- **Corrected (verbatim).**
  - Prompt (30 words, over the 25 aim; the current one has 23): "In 2025, did you (or, on a joint return, your spouse)
    get crypto or another digital asset as pay or a reward, or sell, trade, spend or give any away?"
  - Help (40 words): "Yes: paid in crypto, staking rewards, new coins from a fork or airdrop, or selling, swapping,
    spending or giving it away. No: buying it with dollars, holding it, getting it as a gift, or moving it between
    your own wallets."
  - The plan's `s1.digital_income` change (adding the airdrop; dropping "similar reward") is sound
    [C i1040gi.cols.txt:295].

### A11. BUG-0790: two plans patch `asset.listed` differently

- med-older recommends refusing every boat in `asset.kind_excluded`. med-k1sche recommends adding "a boat or other
  property used for transportation" to `asset.listed`, and claims the same entry for its lane A.
- The k1sche version computes a boat used more than 50% in business. That includes a yacht used to entertain clients,
  whose depreciation section 274 disallows [I: section 274 is not in the archive]. The med-older version only refuses.
- **Recommendation.** One lane, the med-older version. Prompt: "…property of a kind used for entertainment or
  recreation (such as photographic, sound, communication or video recording equipment)…". Kind tick: "A building,
  land, a vehicle or boat, an aircraft, a film or a recording" (12 words). p946 places boats under transportation
  [C per both plans, p946.cols.txt].

### A12. BUG-0861 (med-older): the 65-or-older or blind dependent

- **Defect.** The help gives only "$3,350 not from work, $17,750 of pay" for a dependent 65 or older or blind. It omits
  their gross-income test, "Your earned income (up to $15,300) plus $2,450" [C sources/2025/i1040gi.cols.txt:165-166].
  Example: $3,000 not from work and $1,000 of pay. That person must file, since $4,000 is more than $3,450, but both
  stated limits say No. The dependent's income then drops out of household income on Form 8962, and the PTC is
  overstated (rare).
- **Corrected help (verbatim, 36 words):** "With both kinds, they must file when the total is more than the larger of $1,350
  and their pay (up to $15,300) plus $450. If 65 or older or blind: $3,350, $17,750, and pay plus $2,450." The prompt
  figures are checked [C i1040gi.cols.txt:165].

### A13. BUG-0904 (med-income): "care in the other person's own home"

- **Defect (from before tonight; the proposal keeps it).** i1040gi: "caring for someone living in your home with you"
  [C i1040gi.cols.txt:8661, per the plan]. A caregiver who moved into a parent's house lives there, so it is their home
  too. The help sentence "Care in the other person's own home … is pay for work in someone's home" sends them to No,
  and the excludable pay is taxed. That shared living counts is [I]; IRS Notice 2014-7 Q&A is not archived.
- **Corrected help (verbatim, 40 words):** "Also called difficulty of care payments, often paid through an agency or care
  plan. A W-2 with code II in box 12 shows them. Pay for caring for someone who does not live with you is pay for work
  in someone's home."

### A14. BUG-0808 (med-income): "prizes such as a car" in the gambling amount help

- **Defect (from before tonight; the proposal keeps it).** Line 8b is gambling ("lotteries, raffles, a lump-sum payment
  from the sale of a right to receive future lottery payments") and 8i is "Prizes and awards"
  [C i1040gi.cols.txt:8611, 8634]. A contest or sweepstakes car entered as gambling lets gambling losses offset it.
- **Corrected (verbatim, about 40 words):** "Add box 1 of each Form W-2G to winnings with no form: lotteries (including a
  yearly installment or a sale of future payments), raffles, sports bets, fantasy sports, and goods won by gambling,
  such as a raffle car. Give 0 if none was gambling."

---

## B. Wrong refusal or acceptance; clashes with no direct value effect

- **B1. k1s spouse wording clash (interview.md vs BUG-0886).** interview.md's `k1s.past_years` rewrite says "(or, on a
  joint return, your spouse)". BUG-0886 replaces exactly that with "(or your spouse, whether or not you file jointly)".
  Source: participation by a spouse counts "whether or not you and your spouse file a joint return"
  [C sources/2025/i1040sc.cols.txt:90]. **Corrected:** "For this S corporation — Did you (or your spouse, whether or
  not you file jointly) materially participate in this business in at least 5 of the years 2015 to 2024 (any 3
  earlier years if it provides personal services)?" Effect: latent while `scope.k1` refuses.
- **B2. `scope.contractor_pay` full prompt (interview.md 2.4).** It drops "without taking out social security or
  Medicare tax" [C forms/2025/scope.yaml:503], and a Yes computes Form 8919 [C forms/2025/person.yaml:1040-1046]. On the
  CLI or "answer on its own" paths, a contractor whose firm withheld FICA, or who reports the pay on Schedule C, may
  answer Yes. **Corrected (29 words; owner judgment on the 25 aim):** "In 2025, did a firm pay you (or, on a joint
  return, your spouse) as a contractor, with no social security tax taken out, when you were really its employee?"
- **B3. BUG-0890 `royalty.amt19` (med-k1sche).** "…or taken out of your payments" double-deducts where the payer's
  1099 box 2 is already net of the costs it took [I]. **Corrected:** "Other costs of it (not depletion), paid in 2025,
  or taken out of your payments if the royalties you entered are before they were taken out; zero if none".
- **B4. Lane overlap on `scope.yaml`.** interview.md 2.4 rewrites the full prompts of `scope.tips_unreported`,
  `household_pay`, `contractor_pay` and `wages_no_form`, and med-income lane M2 owns `scope.yaml` (0904, 0905, 0906).
  Give these to M2, or merge them in sequence.

## C. Misreading risk (no value change found, or a lost case only)

- **C1. BUG-0897 help (med-income).** It drops the current "they are not tax taken out of your pay" (the heading still
  guards it [C questions.yaml:66-67]) and does not exclude a January 2025 payment for 2024. **Corrected (38 words):**
  "Payments you sent the IRS yourself for 2025, including the one due in January 2026 but not a January 2025 payment
  for 2024, and an overpayment from your 2024 return or an amended return applied to 2025."
- **C2. BUG-0789 heading (med-k1sche).** "Did you, or a tenant for you, pay …" invites a landlord to enter utilities the
  tenant pays for themselves under the lease (not counted in rent). **Corrected:** "In 2025, did you pay any of these
  for this rental, or did a tenant pay any in place of rent?" (amt17's "by a tenant in place of rent" is already right.)
- **C3. BUG-0899 `rec.two_returns` help (med-income).** "A state income tax refund counts." does not say counts as
  what. **Corrected:** "Count a state income tax refund as money back."
- **C4. `rprop.kind` residential choice (interview.md).** "mostly (80% or more)": 70% is "mostly". **Corrected:** "A
  building with 80% or more of its rent from homes or apartments, or an improvement to one" [C i4562.cols.txt:195].
- **C5. `rprop.basis` (interview.md).** "the smaller of its value then and your adjusted basis": "its value" may be read
  as including land, and "adjusted basis" is jargon (N6; also in the current source [C rprop.yaml:66-67]).
  **Corrected:** "For this building or improvement — Your share of what it cost, not counting the land. If you used it
  yourself before renting it, use the smaller of what the building was worth then and what you paid plus improvements,
  both without the land."
- **C6. `rec.has_other` and `scope.wages_no_form` full prompts (interview.md).** "something else" and "other wages"
  depend on the sibling boxes and break N6 ("never anything other than") on the paths where the prompt stands alone.
  Low; flagged for the owner's 25-word decision.
- **C7. `k1s.not_at_risk` help (interview.md).** "one someone guarantees for you": a third-party guarantee of your
  own loan does not protect *you* from loss (the source means "protected against loss by a guarantee"
  [C i1040se.cols.txt:48]). A Yes refuses, so this is over-refusal only.
- **C8. `asset.listed` "communication equipment".** A phone used 40% for business is refused. Over-refusal only.

## D. Norm breaches (N10 word limits; the current text is usually over as well)

- med-older: 0803 prompt 48 and help about 66 (plan offers a move); 0815 help 46 (A7's version is 40); 0796 help 45;
  0861 prompt 47; 0862 prompt 46 (a parent; aim 25); 0870 prompt 42.
- med-income: 0907 help 44 (A3's version is 41); 0830 help 41. All ticks are 12 words or fewer.
- interview.md: every rewrite meets its stated limit. `rental.personal_any` at 44 (A2) is the price of keeping the
  rule; N10 lets help run to "about 40".
- A10's prompt is 30 words for a parent: an N10 breach traded against a wrong printed answer. Owner's call.

## E. Checked and found sound (coverage)

med-income: 0806 structure (Yes then `other_work`) [C tipjob.yaml:39-64]; 0806 help; 0808 prompt, help and installment
or sale sentences [C i1040gi.cols.txt:8611]; 0810 option B, where every box refuses so no Yes can give a wrong value;
0822 tick, prompt and guard [C p544.cols.txt:134 "a loss … held for personal use is not deductible"; the collection
route ends at `sales.special`'s collectibles refusal, C sales.yaml:227]; 0830 help (boxes 9 and 10 exist,
C div.yaml:78-96, 435); 0833 `f4952.line1`; 0873 `others_paid` [C i8853.cols.txt:235, 279] and `periodic`
[C i8853.cols.txt:226]; 0896 `s1.digital_income`; 0897 tick and prompt [C i1040gi.cols.txt:900] with the joint-payment
dependency kept; 0899 `refund.itemized` (every `rec_kinds` box is an itemized item, C questions.yaml:4067-4086, so
dropping the qualifier is harmless); 0900 (refusal only); 0901 (refusal only; Schedule H and p926 are not archived);
0904 tick; 0905; 0906 (the strike and lockout guard against state unemployment pay is right).

med-older: 0793 (a Yes only asks the next question); 0796 panel tick "put in in 2024 or 2025" [C i5695.cols.txt:161-163,
the safe harbor treats a 2024 panel as 2025] and `line21a` [C i5695.cols.txt:62, 146]; 0797
[C i8862.txt:84-105, Form 8862 is required after a ban]; 0805 prompt; 0817(a); 0862; 0870 ("a 2025 deadline" fits
i5329); 0850 (wording unchanged; only refuses); 0803 apart from the treaty-charity owner decision.

med-k1sche: 0775 amt12 and amt16 help (with A1's counterpart); 0789 `rents` help and `amt17`; 0836 (arithmetic, not
wording); 0837; 0838 and 0886 spouse wording [C i1040sc.cols.txt:90]; 0841 ticks (all refuse); 0843 `re_pro` and
`dwelling` (refuse; reading "(or your spouse)" as combining hours only over-refuses); 0890 `expenses_any`.

interview.md: `f1040.tax_exempt_any` source and amount gating (apart from A4's heading); the `rprop_facts` ticks
(all refuse) [C rprop.yaml:71-95]; the QIP child; `rental.days_personal`; `rental.days_fair` (it includes overlap days,
as the model's `days_overlap` design expects [C rental.yaml:92-93, 127; p527.cols.txt:845]); `rental.not_at_risk` and
its side finding [C i1040se.cols.txt:48-49]; `person.f4137_under20`; `person.mw_not_box1` and `mw_box1`
[C person.yaml:1512-1548]; `s2.amt_business`; `k1p.not_at_risk`; `k1p.basis_short`; the 2.4 prompts for
`rental.part_home`, `sche.qbi_business` (refuses [C questions.yaml:7238-7243]), `royalty.business`, `f1116sb.*`,
`f1116.reduction`, `s1.nol_not_married`, `scope.tips_unreported`, `scope.household_pay`, `sd.qof`; the
`refund.you_born` derivation (born before January 2, 1960; ask only for birth year 1960); the `sales_rare` reorder
(bank only; its heading reads well before the sales).

## Not done

- No walk, build or review was run. Every misreading named is my judgment ([I]).
- Not read: the Schedule A property-tax amount entry (A1), IRS Notice 2014-7 (A13), section 274 (A11), p926 and
  i1040sh (not archived).
- The persona answer tables in interview.md section 3 are not wording, and were checked only for the `refund.you_born`
  rule.
