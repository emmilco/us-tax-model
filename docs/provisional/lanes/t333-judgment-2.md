# Lane note t333-judgment-2: T-333 judgment records, part 2 (married filing separately, dependent filers, Schedule 1 other income, pay not on a W-2)

Written 2026-11-22 by scout claude-opus-5-5 (judgment, tax year 2025, jurisdiction us), carried into this note by lane
left (claude-sonnet-5-5, mechanical, 2025, us; worktree `.claude/worktrees/left`, branch `lane-left`, from `next`
9a2b3e9c). These are the judgment records that T-333 asks for, for the lanes mfs-l1 to mfs-l4, x2-dep, x2-s1o and
x2-paynow2. This is a record of what the scout judged on that date, not guidance (`docs/provisional/README.md`).
The scout read the `integrate-1` worktree (HEAD 870cc146 plus its staged changes).

**What lane left changed.** Only citations: every `(order/seq)` pair of an input named in the records was compared with
`interview/2025/questions.yaml` in this tree and all 47 agree (the group ranges 161/28-30, 165/21-24, 258/11-14 and 146/20-24 and the roster `$f8853c`, 161/16, were checked too); two code citations were corrected
(`engine/src/build.ts:239` to `:287`, the line that derives a stored prompt from the form line's source; and
`person.yaml:1025` to `forms/2025/person.yaml:1026`, the only reader of `f8919firm.wages`; `engine/src/integration.ts:233`
holds the cited assertion). The judgments, shares, costs and findings F1 to F6 are the scout's, unchanged.

**What the recheck found about the tree.** The records quote the `integrate-1` wording. Quoted wording not found in this
tree: section D2 (`scope.household_pay`). Here its tick reads "Pay from a household for home, garden or driving work,
no W-2", its prompt "In 2025, were you (or, on a joint return, your spouse) paid by a household, with no W-2, for work
in or around its home or for its members?", and its help ends "... A household that pays you less than $2,800 in a
year need not give you a W-2." (`interview/2025/questions.yaml:1946-1952`); the remedy text about BUG-0903's
widened label refers to the `integrate-1` change, and BUG-0903 is open here (`BUG_INVENTORY.md:10985`). The proposed
wordings quoted under the findings are proposals, not tree text. `f8919firm.reason` is still read by no form line
(finding F6 holds in this tree: `forms/2025/f8919firm.yaml:9` defines it, `interview/2025/questions.yaml:1990`
banks it, and `forms/2025/person.yaml:1026` reads only `f8919firm.wages`). Bug status written as fixed in
`integrate-1` (BUG-0864, BUG-0904) is open here. Every other string of 20 or more characters quoted from the question
bank was found in this tree. Ids renamed since 2026-11-15 (`s1.nol_before_limit_date`, `s1.nol_not_married`,
`s1.nol_was_joint`) exist here (`interview/2025/questions.yaml:2175-2195`).

## How to read this

- **Questions are quoted from `interview/2025/questions.yaml` in int1.** Where the bank stores no prompt, the text is the
  form line's `expr.source`, which is what the build shows (`engine/src/build.ts:287`). For a box on a tick-box screen,
  the filer reads the **tick label** on the screen, not the prompt; both are given.
- **Ids in the lane notes are testimony.** Several have changed since 2026-11-15: `s1.nol_pre2018` is now
  `s1.nol_before_limit_date`; `s1.nol_marital` is split into `s1.nol_not_married` and `s1.nol_was_joint`. Inmate pay
  (line 8u) was put back to a refusal at integration XINT (BUG_INVENTORY entry quoting i1040gi p. 23, fixed as "lane
  x2-s1o's computing of Schedule 1 line 8u is reverted"; TASKS T-336), so `s1.inmate_wages` has no children and is
  left out. Every gate and who-is-asked statement below was read from the int1 form YAML.
- **"Parent"** means a question whose answer opens or closes other questions. Questions that existed before
  2026-11-15 but became parents then (a refusal turned into a computation with questions beneath it) are included and
  marked "existing, now a parent". New questions that are not parents get a one-line guard note in a table at the
  end of each area; the protocol does not ask for a full record of them.
- **Source pages** are pages of the archived text (`sources/2025/<doc>.cols.txt`, split at form feeds). Where a YAML
  cite gives a page for the same passage, the two agreed (i1040gi p. 33, p501 p. 17, i8962 p. 7, i1040sca p. 8,
  i8889 p. 7).
- **Costs** use the owner's effort scale of construction protocol 1.1 (1 = known at once; 20 = must find out what is
  asked and look up a paper). Every cost is this scout's judgment. **Shares** say where they come from: `soi` and
  `microdata` from `interview/2025/gate_frequencies.yaml` or `reports/2025/filer_coverage.md` (IRS 2023 counts);
  `judgment` from the same file where it holds one; "no data" where neither has the situation. Shares are of all
  returns unless the column says "of those asked".
- **Rule of 1.1 "when a parent pays"**: a parent of cost g, answered No by a share q of those asked, in front of
  children costing C, pays when g < q·C.

---

## A. Married filing separately (lanes mfs-l1 to mfs-l4)

Who reaches this area: married filing separately returns, 2.6% of all returns (`filer_coverage.md`, "Married filing
separately", 4,139,858 IRS returns, 2023). Every question below is gated on `household.mfs` (`f1040.status` = mfs)
and on a further fact, so a filer on any other status meets none of them. The community property refusal
(`household.mfs_community_property`) sits before all of them; it is not new and is not recorded here.

### A1. `sa.spouse_itemizes` (200/86) — existing, now a parent

- **Asked:** every MFS return (`sa.mfs_spouse_itemizes` chooses on `sa.mfs`). Before 2026-11-15 an MFS return was
  refused at `s3.mfs` before it got here.
- **Question:** "Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard
  deduction?" Help: "If they itemize, your standard deduction is zero and your own deductions are listed instead. Ask
  them if you do not know."
- **Child:** a No opens `sa.spouse_extra` (200/87, refuses on Yes): "Did your husband or wife have no income in 2025,
  with no 2025 return filed for them, and were they born before January 2, 1961, or blind at the end of 2025?"
- **Source:** i1040gi p. 33, Line 12b: "If your filing status is married filing separately and your spouse itemizes
  deductions on their return, check the box on line 12b." p. 34, Exception 2: "If you checked the box on line 12b, your
  standard deduction is zero, even if you were born before January 2, 1961, or were blind."
- **Who could answer No wrongly:** a filer who files before the spouse has decided, or who does not speak to the
  spouse (the separated filer the area is mostly for). Guard: the help ("Ask them if you do not know"); nothing else.
  Cost: a $15,750 standard deduction taken where it should be zero; tax understated by about the deduction times the
  marginal rate, and a notice when the spouse's return is matched. There is no better guard available: the fact lives
  with the other spouse.
- **Who could answer Yes wrongly:** a filer who assumes a homeowner spouse itemizes. Cost: the filer loses the
  standard deduction and itemizes whatever they have; over-taxed by up to the deduction times the rate. No guard.
- **N4 (weak structure, finding F1):** the typical MFS answer is No (the spouse takes the standard deduction), and the
  No is the longer path: it brings `sa.spouse_extra`, a three-part conjunction about the spouse that almost every
  filer answers No and must read whole. That is the shape N4 names: "A guard question asked only after a No is a
  violation." Lane mfs-l2 kept it knowingly ("the same two questions as before"). Remedy within the norms: a box on
  the same screen, or gate `sa.spouse_extra` on a fact already given (none exists today: no spouse birth year is asked
  on a separate return).

| Parent | Reached (all returns) | q = No share of those asked | g | C (children) | Pays? |
|---|---|---|---|---|---|
| `sa.spouse_itemizes` | 2.6% (soi, MFS) | no data; judgment 0.8 to 0.9 (itemizers are a minority of filers) | 3 (must know the spouse's choice) | `sa.spouse_extra`, 6 | Not a layering parent: the child is on the No side, so q·C counts the wrong branch. The parent exists because it is a fact the return needs, not to spare questions. |

### A2. `f8962.mfs_exception` (196/8) — new parent

- **Asked:** MFS with a Form 1095-A (`f8962.mfs_ask` = `household.mfs` and `f8962.any`).
- **Question:** "Do you live apart from your husband or wife now, and are you unable to file a joint return with them
  because they abused you or abandoned you?" Help: "Abuse can be physical, psychological, sexual or emotional,
  including efforts to control, isolate, humiliate or intimidate you; abuse of your child or a relative living with you
  can count. Abandoned: you cannot find them despite reasonable effort. Send no proof."
- **Child:** a Yes opens `f8962.mfs_three_years` (196/9): "Did you take the premium tax credit on a separate return
  under this exception for each of 2022, 2023 and 2024?"
- **Source:** i8962 p. 7, Exception 2: "If you are a victim of domestic abuse or spousal abandonment, you can file a
  return as married filing separately and take the PTC for 2025 if all of the following apply to you. • You are living
  apart from your spouse at the time you file your 2025 tax return. • You are unable to file a joint return because you
  are a victim of domestic abuse (described next) or spousal abandonment"; "3-year limit for Exception 2. You cannot
  claim the PTC using this exception for more than 3 consecutive years." And "Married filing separately. If you file as
  married filing separately and are not a victim of domestic abuse or spousal abandonment ... you cannot take the PTC."
- **Who could answer No wrongly:** a filer controlled or intimidated by the spouse who does not think of it as
  "abuse"; a filer whose spouse disappeared and who thinks "abandoned" needs a court finding. Guard: the help names
  psychological and controlling abuse and defines abandonment in a person's words. Cost: the whole premium tax credit
  lost and the advance payments repaid (limited by Table 5, i8962 p. 18, Line 28); for a marketplace family that can
  be thousands of dollars.
- **Who could answer Yes wrongly:** an estranged filer who simply will not file jointly, or whose spouse can be found.
  Guard: the conjunction in the question ("unable to file a joint return with them because ...") and the help's
  "cannot find them despite reasonable effort". Cost: the credit taken where barred (understated tax). The IRS asks
  for no proof (the help says so, following the instructions), so the question is the only guard there can be.
- **Child `f8962.mfs_three_years`, wrong No:** a filer who does not remember using the exception in all three earlier
  years. Guard: help "at most 3 years in a row". Cost: credit taken where barred. Rare.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `f8962.mfs_exception` | about 0.2% if independent: MFS 2.6% (soi) × marketplace 8.5% (judgment) [inferred product; no count of the intersection] | no data; judgment 0.9 | 5 (a sensitive question; the help may be read) | `mfs_three_years`, 3 | Not a layering parent: it is the legal fact itself; the child sits on the rare Yes. Typical answer (No) is the cheap one (N4 met). |

### A3. `dependent.other_only_spouse` (120/17) — new parent, head of a three-question chain

- **Asked:** per dependent, on MFS, only after a Yes to the existing `dependent.other_claimant` (120/13) ("did this
  person live for more than half of 2025 with another relative who could claim them"; help now adds "On a separate
  return, your husband or wife counts."). The gate `dependent.other_only_spouse_if_mfs` chooses on `household.mfs`;
  the line is read only from the Yes branch of `dependent.qc_tiebreak_claimant` (lane mfs-l4 note, section 2; the gate
  expressions confirm the chain).
- **Question:** "Is your husband or wife the only relative, besides you, who lived with this child for more than half
  of 2025 and could claim them?" Help: "Answer No if a grandparent, aunt, uncle, grown brother or sister, or a parent
  other than you and your husband or wife also lived with the child over half of 2025. A No may end the interview here."
- **Children:** Yes opens `dependent.spouse_claims` (120/18), "Will your husband or wife claim this child on their own
  2025 return?" (Yes refuses); its No opens `dependent.filer_parent` (120/19), "Are you this child's parent by birth or
  by adoption?" (No falls back to the old refusing test).
- **Source:** p501 p. 17, Example 6, separated parents: "Your child is a qualifying child of both you and your spouse
  because your child lived with each of you for more than half the year"; and (Example 6 continued, as quoted in
  BUG-0864) "if your spouse doesn't claim your child as a qualifying child, you can claim this child". p501 p. 15,
  tiebreaker: "the term 'parent' means a biological or adoptive parent of an individual. It does not include a
  stepparent or foster parent unless that person has adopted the individual. • If only one of the persons is the
  child's parent, the child is treated as the qualifying child of the parent."
- **Who could answer No wrongly:** a filer whose own parent stayed with the family part of the year and who counts the
  grandparent although the grandparent did not live with the child over half the year. Guard: the question's "for
  more than half of 2025". Cost: a refusal (over-refusal), not a wrong value. The earlier wording that told a filer to
  answer No because the spouse is "another parent" (BUG-0864) is fixed in int1.
- **Who could answer Yes wrongly:** a filer whose child also lived with a grandparent over half the year. Cost: small.
  Under the p. 15 tiebreaker a parent who claims wins over a non-parent, so the filer's claim is still right unless the
  grandparent's AGI rule applies, which needs the parents not to claim; the chain then still asks `spouse_claims` and
  `filer_parent`. Judgment: the cost of this wrong Yes is near zero.
- **`dependent.spouse_claims`, wrong No:** a filer who has not agreed with the spouse; both claim, the IRS applies the
  tiebreaker (p501 p. 17, "Subject to these tiebreaker rules, you and the other person may be able to choose which of
  you claims the child"), and the filer may lose the child tax credit and earned income credit on notice. Guard: help
  "agree which of you will". The question asks a future act of another person; it cannot be guarded better.
- **`dependent.filer_parent`, wrong Yes:** a stepparent who has raised the child. Guard: help "A stepparent, foster
  parent or grandparent who has not adopted the child answers No." Cost: the child claimed by a non-parent whose AGI
  was never compared (i1040gi p. 21 rule the lane cites); understated tax.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `dependent.other_only_spouse` | no data: MFS 2.6% (soi) × dependents 29.4% (microdata) × the share answering `other_claimant` Yes (no data) | no data; judgment 0.2 (most separated parents' other claimant is the spouse) | 4 | `spouse_claims` 3 + `filer_parent` 1 | The chain is a refusal-narrowing ladder, not an off-ramp: every step's typical answer moves toward computing. Each question is asked only where it can change the result (N4 met). |

### A4. New MFS questions that are not parents (guard notes)

| Question (bank) | Asked | Wrong answer, guard, cost |
|---|---|---|
| `household.mfs_living` (102/4) "In 2025, when did your husband or wife live with you?" (three answers) | MFS, only when a line reads it: benefits (line 6d), EIC with a child, a traditional IRA contribution while not covered, Form 2441 line A or 19 | Wrong "together" by a separated filer: loses Form 2441's considered-unmarried path and EIC (i2441 p. 2, "You lived apart from your spouse during the last 6 months of 2025"); wrong "apart" by a filer whose spouse was away temporarily: understated tax on benefits and IRA. Guard: help, "Time away for work, school, medical care or military service, when you expected to come back, counts as living together. So does time you shared a home, even if you were separated" (i1040gi p. 15). Adequate. Note: Form 8582's use of the lived-with-spouse fact is BUG-0933 (its status not checked here). |
| `ira.mfs_spouse_covered` (180/21) | MFS, traditional contribution, filer not covered, lived together some time | Wrong No by a filer who cannot see the spouse's W-2 box 13: full deduction where the $10,000 phase-out applies (p590a p. 14 table, "married filing separately"). Guard: help names box 13. No route for "I cannot find out"; residual. |
| `sa.mortgage_over_limit_mfs` (200/33), refuses | MFS with mortgage interest | Wrong No by a filer counting half a joint loan; guard: help "the whole of a loan you owe with your husband or wife" (i1040sca p. 8, "$375,000 if you are married filing separately"). Conservative (over-refuses). |
| `f2441.mfs_spouse_deemed` (156/7), refuses; `f2441.mfs_spouse_earned` (156/8) | MFS not considered unmarried, read by line 19 (benefits) | Siblings on the same gate (`f2441.mfs_married`), not parent and child. A student spouse with no pay entered as 0 earnings is caught by the deemed question asked first (i2441 p. 5, Line 19, "If you or your spouse was a full-time student or disabled in 2025, see the instructions for lines 4 and 5"). |
| `f8889.mfs_spouse_hsa` (190/37), refuses | MFS treated as having family HDHP coverage | Wrong No for a spouse's empty HSA; guard: help "even if nothing was put into it" (i8889 p. 7, "Spouses who have separate HSAs and had family coverage"). The stored prompt carries the per-person frame; the engine strips it on a one-person return (`engine/src/integration.ts:233`). |

---

## B. Dependent filers (lane x2-dep)

**No new parent question.** Lane x2-dep added no input (its note: "this lane adds no input, so it has no defaults
patch"); confirmed in int1: the new lines (`sa.dep_*`, `sa.standard_amount`, `f8962.dependent_filer`) are computed or
gates. The record the protocol asks for therefore covers the one existing question whose consequences changed.

### B1. `sa.dependent` (111/1) — existing; its Yes changed from a refusal to a computation

- **Asked:** every filer.
- **Question:** "Can a parent or anyone else claim you (or, on a joint return, your spouse) as a dependent on their
  2025 return?" Help: "Yes even if they did not. At 19 or older (24 if a full-time student): only if your income was
  under $5,200 or you were disabled. No if they need not file and file none, or only for a refund." (x2-dep removed
  "A Yes ends the interview here.")
- **Children:** none in the bank. A Yes now sets the Standard Deduction Worksheet for Dependents, bars EIC without a
  child, bars claiming dependents, and refuses only at `sa.dep_qss` (QSS) and `f8962.dependent_filer` (Form 1095-A).
- **Source:** i1040gi p. 33, Line 12a: "If you or your spouse (if you are married and filing a joint return) can be
  claimed as a dependent on someone else's return, check the appropriate box(es) on line 12a." p. 34, Exception 1:
  "If you checked a box on line 12a, use the Standard Deduction Worksheet for Dependents".
- **Who could answer No wrongly:** a student of 19 to 23 with a part-time job whose parents claim them, who thinks a
  pay cheque makes them independent; a teenager filing for a refund. Guard: the help only. There is no cross-check
  with the birth year, though `household.birth_year` already tells the tool which filers are 16 to 23. Cost: the full
  $15,750 standard deduction in place of earned income plus $450, and an education credit the parents also take; for
  a student earning $8,000, about $730 of tax plus up to $2,500 of credit. **This risk predates x2-dep** (the old
  refusal guarded only the Yes side), but the record must name it: finding F5.
- **Who could answer Yes wrongly:** an adult living with parents who thinks "they could claim me". Guard: the help's
  $5,200 rule. Cost, new since x2-dep (before, a refusal): for a filer with earned income of $15,300 or more, none (the
  worksheet gives the full basic amount); for a low earner, a smaller deduction; for a young single parent, the loss of
  dependents, head of household and EIC, which can be thousands of dollars.

| Parent | Reached | Yes share | g | C | Pays? |
|---|---|---|---|---|---|
| `sa.dependent` | all returns | 4.69% (soi, Table 1.7 dependent returns, 7,525,664; a floor, per its note) | 4 (needs the age and income rule for older filers) | none asked | Not a layering parent; a fact the return needs. |

---

## C. Schedule 1 other income (lane x2-s1o; forms s1, oi8z, rec, f8853c)

### C1. `scope.recovery` (161/6, box on screen `money_b`) — existing, now a parent

- **Asked:** every filer (screen "Did any of these happen to you (or, on a joint return, your spouse)?").
- **Tick label (what the screen shows):** "Money back for a deduction or credit (not state/local income tax refund)".
  Prompt: "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an
  earlier year's return lowered your tax, other than a state or local income tax refund?" Help: "For example a refund
  of property tax, sales tax or mortgage interest (Form 1098 box 4), or medical costs or a deducted bad debt paid back.
  Not counted if deductible only by itemizing and you did not itemize that year."
- **Children:** screen `rec_rare` (161/28 to 30: before 2024, deduction taken without itemizing or a credit, sales tax;
  each refuses) at once; `rec.two_returns` (161/31) on a joint return; then, after `refund.itemized` (165/7) Yes,
  screen `rec_kinds` (165/21 to 24) and its amounts, and `rec.ti_positive` (165/31).
- **Source:** p525 p. 24, Recoveries: "A recovery is a return of an amount you deducted or took a credit for in an
  earlier year. The most common recoveries are refunds, reimbursements, and rebates of itemized deductions."
  "Deductions not itemized. If you didn't itemize deductions for the year for which you received the recovery of an
  expense that was deductible only if you itemized, don't include any of the recovery amount in your income."
- **Who could answer No wrongly:** a 2024 itemizer whose county refunded property tax, whose lender refunded overpaid
  interest (Form 1098 box 4), or whose insurer repaid medical bills deducted in 2024. The examples that would make them
  recognize it are in the help only; the tick label says "a deduction or credit", tax vocabulary (N6), and a screen box
  is meant to be passed over at a glance (technique 3.6: "for each box, name who could wrongly pass over it and word
  the label for them"). Cost: the taxable part of the recovery left off line 8z (understated tax; usually hundreds of
  dollars). Finding F4 (low).
- **Who could answer Yes wrongly:** a filer who took the standard deduction for 2024 and got a property tax refund.
  Guard: the help's last sentence, then `refund.itemized` No, which taxes nothing. Cost: one extra screen
  (`rec_rare`, which comes before `refund.itemized`) and the itemizing question; no wrong value. A non-itemizer who
  ticks `rec.nonitemized` there is refused; over-refusal only.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `scope.recovery` | all returns | no data (SOI has no recovery count; line 8z 4.85% soi is an upper bound that holds other items) ; judgment q > 0.98 | 1 (a box) | `rec_rare` 3, `refund.itemized` 1, `rec_kinds` 3, amounts 2 to 6, `ti_positive` 1: about 12 | Yes, easily (1 < 0.98 × 12). |

### C2. `rec_kinds` boxes (165/21 to 24) and `rec.ti_positive` (165/31) — new parents

- **Asked:** `rec_kinds` when `rec.path` (`scope.recovery` Yes and `refund.itemized` Yes); `rec.ti_positive` on the
  same path.
- **Screen:** "Was any of the money paid back for any of these 2024 deductions?" Boxes: "Real estate or personal
  property tax"; "Mortgage interest (Form 1098 box 4)"; "Medical or dental bills, repaid by insurance or someone else";
  "Something else you itemized for 2024". Each Yes opens its amount (and, for medical and other, the amount deducted).
- **`rec.ti_positive`:** "Does line 15 of your 2024 Form 1040 show an amount above zero?" Help: "Line 15 is taxable
  income. Most people who itemized have an amount there." A No opens `rec.agi_prior` (line 11) and `rec.ded_prior`
  (line 14).
- **Source:** p525 p. 24 (above); Worksheet 2 lines as cited in `forms/2025/rec.yaml`.
- **Who could pass over a box wrongly:** a filer who put the state income tax refund under "Something else"; guard:
  help on `rec.has_other`, "Not state or local income tax; that refund is asked on its own." The filer reached this
  screen by saying Yes to money back, so a None here is self-correcting only if nothing applies; no further guard.
  Cost: the recovery untaxed.
- **`rec.ti_positive`, wrong answer:** a filer reading line 15 of the wrong form. It names a line, which N6 allows
  here only because the filer is holding the 2024 return (they have just given its Schedule A lines 5d, 5e and 17).
  Cost: wrong Worksheet 2 line 10; small.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `rec_kinds` (one screen) | no data | no data | 2 | amounts 1 to 2 each | One screen; each box spares its amounts. |
| `rec.ti_positive` | no data | judgment: q (No) about 0.05, per its own help | 3 | 2 amounts, 6 | Yes for the typical answer: the Yes is cheap and ends the branch (N4 met). |

### C3. `scope.nol` (258/2, box on screen `before_2025`) — existing, now a parent

- **Asked:** every filer (screen "Before 2025, did you (or, on a joint return, your spouse) have either of these?").
- **Tick label:** "A loss still being carried into 2025 (a 'net operating loss')". Prompt: "Are you (or, on a joint
  return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction?" Help: "A
  loss bigger than that year's income, not yet used up, from a business, farm, rental or disaster, or a business loss
  held back by the yearly limit (Form 461). Not a loss still held back on Form 8582."
- **Children:** `s1.nol_amount` (258/10), "How much of that loss is still unused and carried into 2025?", and screen
  `nol_facts` (258/11 to 14, each refusing): before 2018; excess business loss; not married to each other in its
  years (joint); a joint return in its years (not joint).
- **Source:** i1040gi p. 91, Line 8a: "Enter any deduction for an NOL from an earlier year ... See the Instructions for
  Form 172 for details." i172 p. 3, Change in Marital Status: "only the spouse who had the loss can take the NOL
  deduction."
- **Who could answer No wrongly:** a filer whose 2024 preparer carried an NOL forward and who does not know the term;
  a filer with a casualty-loss NOL. Guard: the label's plain half ("A loss still being carried into 2025") and the help
  (BUG-0907's wording is fixed in int1). Cost: the deduction missed (over-taxed).
- **Who could answer Yes wrongly, and this is the weak guard (finding F2, medium):** a filer carrying a **capital loss**
  from 2024. The tick label "A loss still being carried into 2025" describes a capital loss carryover exactly, and
  only the term in quotes, which this filer does not know, says otherwise. The help excludes Form 8582 losses but not
  capital losses. The capital loss question (`sd.carryover`, 276/1) is asked later (order 276 after 258), so nothing
  already said catches it. Scale: capital loss carryovers are on about 4.5% of returns (judgment, from SOI long- and
  short-term carryover counts), NOLs on 0.63% (IRS count, 1,019,019 returns): about seven capital-loss filers for each
  NOL filer reach this box. Cost: the filer enters the capital loss as an NOL on line 8a, deducted in full against
  ordinary income with no $3,000 limit, and probably again on Schedule D when `sd.carryover` is answered; understated
  tax of up to the whole carryover times the rate. Remedy within the norms: say in the label "from a business, farm,
  rental or disaster (not a loss from selling investments)"; or ask `scope.nol` only after `scope.business_before`
  (258/1) Yes plus a disaster route, which would also make it a child that pays.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `scope.nol` | all returns | 0.994 (IRS: NOL deduction 0.6% of returns) | 1 (box), but see F2 | `nol_amount` 3 + `nol_facts` screen 3: 6 | Yes (1 < 0.994 × 6). |

### C4. `s1.ltc_payout` (161/3, box on `money_b`) and `f8853c.periodic` (161/17) — existing parent; new parent

- **Asked:** `s1.ltc_payout`, every filer. `f8853c.periodic`, per person named in the roster `$f8853c` (161/16) after a
  Yes.
- **Tick label:** "A long-term care insurance payout, or life insurance paid early, in 2025". Help: "The insurer sends
  Form 1099-LTC. Count payments the policy sent straight to a nursing home or care agency. Payments that only repaid
  care costs are usually not taxed; payments at a set daily or monthly rate may be."
- **`f8853c.periodic`:** "Were any payments a set amount per day, week, month or other period, whatever the care cost
  (box 3 of Form 1099-LTC shows "Per diem")?" Help: "... Payments that only repaid care costs are not taxed: answer No
  and nothing more is asked for this person." A Yes opens lines 17 to 26 and four refusing guards.
- **Source:** i8853 p. 1: "You (or your spouse, if filing jointly) were a policyholder who received payments under an
  LTC insurance contract or received any accelerated death benefits from a life insurance policy on a per diem or other
  periodic basis in 2025. See the instructions for Section C"; p525 p. 24, "To claim an exclusion for accelerated death
  benefits made on a per diem or other periodic basis, you must file Form 8853".
- **Who could answer No wrongly:** a policyholder whose policy paid the nursing home directly and who never saw money;
  guard: the help (BUG-0923 is fixed). Cost: small; per diem payments are taxable only above the larger of the care
  costs and $420 a day.
- **Who could answer Yes wrongly:** a filer thinking of health insurance or Medicare; guard: `f8853c.periodic` No ends
  it. Cost: the roster and one question.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `s1.ltc_payout` | all returns | no data (no SOI count of Form 1099-LTC recipients); judgment q > 0.99 | 1 | roster 2, `periodic` 1, lines 17 to 26 about 10 | Yes. |
| `f8853c.periodic` | no data | judgment 0.5 (reimbursement policies are common) | 2 | about 10 | Yes. |

### C5. `s1.stock_options` (146/13) — existing, now a parent

- **Asked:** after `s2.options_any` Yes (screen `other_pay`).
- **Question:** "Did you (or, on a joint return, your spouse) have income in 2025 from those options or shares that is
  not in box 1 of a W-2?" Help: "For example when shares from an incentive stock option or a purchase plan were sold
  early and the employer did not add the income to a W-2." Child: `s1.options_amount` (146/14), "How much income ...
  that is not in box 1 of a W-2?"
- **Who could answer Yes wrongly:** a filer whose nonqualified option income is already in box 1 (the usual case).
  Guard: "not in box 1 of a W-2" in the question and again in the amount. Cost: the income taxed twice.
- **Who could answer No wrongly:** an employee who sold purchase-plan shares early where the employer left the income
  off the W-2. Guard: the help's example. Cost: income omitted.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `s1.stock_options` | no data (`s2.options_any` has no entry in `gate_frequencies.yaml`) | judgment 0.9 | 3 (must check box 1) | 1 amount | Marginal on the frame (3 vs 0.9 × 1); kept because it is the legal fact and the typical No is right without the amount. |

### C6. `oi8z.kind` = "Taxable damages or a settlement" (294/2) — existing question, new value that opens a child

- Child `oi8z.injury` (294/4), refusing: "Was any of it paid in a case about a physical injury or a physical
  sickness?" Wrong No by a filer with a mixed settlement: guard, the help ("punitive damages in such a case are [income];
  splitting them is outside this tool"). Cost: excludable damages taxed or the reverse; low share (no data).

---

## D. Pay not on a W-2 (lane x2-paynow2; scope.pay_no_w2, f4137, f8919, otjob)

Who reaches it: everyone sees the screen `other_pay` (146): "In 2025, did you (or, on a joint return, your spouse) have
any of these kinds of work or pay?". The category is 0.8% of returns (IRS: "Wages or tips not on Form W-2 ... other
earned income", 1,267,621; `pay_outside_w2` 0.79% soi, high end 1.41%).

### D1. `scope.pay_no_w2` (146/1, box on `other_pay`) — existing, now a parent

- **Tick label:** "Wages, tips, or strike or lockout pay not on a W-2". Prompt: "In 2025, did you (or, on a joint
  return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" Help: "Such as pay for
  work in someone's home, tips not reported in full to your employer, tips given as tickets or goods, or pay from a
  firm that wrongly treated you as a contractor. A Yes asks which."
- **Children:** screen `pay_kinds` (146/20 to 24), "Which of these were you (or, on a joint return, your spouse) paid in
  2025?", each box a parent of per-person questions (D2 to D5); the fifth box, `scope.wages_no_form`, refuses.
- **Source:** i1040gi p. 24, Lines 1b, 1c, 1g, 1h ("Line 1b Household Employee Wages Not Reported on Form(s) W-2";
  "Line 1c Tip Income Not Reported on Line 1a"; "Line 1g Wages From Form 8919, Line 6"; "Line 1h ... Strike or lockout
  benefits (other than bona fide gifts)").
- **Who could answer No wrongly:** a nanny or cleaner paid in cash who thinks of it as "cash work", not "wages"; a
  worker paid on a Form 1099-NEC who believes they were an employee but does not call it "wages". Guard: the help's
  examples. Cost: for household pay, income omitted (or reported as a business, see F3); for a misclassified worker,
  Schedule C with the full self-employment tax (over-taxed by the employer's half, 7.65% of the pay).
- **Who could answer Yes wrongly:** a tipped worker whose tips are all on the W-2 (box 7). Guard: the tips box
  "not reported in full" and the roster's reported-tips column, which subtracts; no wrong value. Cost: one screen.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `scope.pay_no_w2` | all returns | 0.99 (soi 0.79%, high 1.41%) | 1 (box) | `pay_kinds` screen 3, then 2 to 6 per kind | Yes. |

### D2. `scope.household_pay` (146/20, box on `pay_kinds`) — new parent (weak guard, finding F3)

- **Tick label:** "Household pay for home, garden or driving work, not on a W-2". Prompt: "In 2025, were you (or, on a
  joint return, your spouse) paid by a household for work in or around its home or for its members, and not all of it
  on a W-2 from that household?" Help: "Such as a nanny, carer, cleaner, gardener or private driver, even in a home you
  share. Count cash beyond what a household's W-2 shows. A household that pays you less than $2,800 in a year need not
  give you a W-2." Child: `person.household_wages` (147/1), the amount, entered on line 1b.
- **Source:** i1040gi p. 24, Line 1b: "Enter the total of your wages received as a household employee that was not
  reported on Form(s) W-2." p926 p. 3: "The worker is your employee if you can control not only what work is done, but
  how it is done." p926 p. 4: "A self-employed worker usually provides their own tools and offers services to the
  general public in an independent business. ... Example. You made an agreement with a worker to care for your lawn.
  The worker runs a lawn care business and offers their services to the general public. ... Neither the worker nor
  their helpers are your employees."
- **Who could answer Yes wrongly (the weak guard):** a cleaner, gardener or lawn-care worker who runs their own
  business for many households. Line 1b is for a **household employee**; the label and prompt say only "paid by a
  household", and the help's examples ("cleaner, gardener") name exactly the trades p926 p. 4 shows as usually
  self-employed. Nothing beneath the box asks whether the household controlled how the work was done. Cost: business
  income entered as wages on line 1b, so no Schedule SE: self-employment tax of about 15.3% of net earnings omitted
  (about $2,800 on $20,000); or the same pay counted twice if the filer also reports it as a business. BUG-0903's fix
  (int1) widened the label to "home, garden or driving work", which widens this risk. Remedy: a child asked on Yes,
  "Did that household decide how the work was done, rather than you running your own business that offers this work to
  anyone?", with business pay sent to Schedule C (or refused); or the word "employee" in the label in plain form ("as
  their worker, not as your own business").
- **Who could answer No wrongly:** a live-in carer paid by the family, who reads "household pay" as a business's pay;
  guard: help "even in a home you share". Cost: wages omitted.

### D3. `scope.contractor_pay` (146/21) — new parent (guard missing, finding F6)

- **Tick label:** "Pay from a firm that wrongly treated you as a contractor". Prompt: "In 2025, did a firm pay you (or,
  on a joint return, your spouse) as a contractor, with no social security tax taken out, when you were really its
  employee?" Help: "Yes only if you believe you were the firm's employee, it took out no social security or Medicare
  tax, and you are not reporting the pay as a business of your own."
- **Children:** roster `$f8919firm` (147/2), then per firm `f8919firm.reason` (147/3, the reason code) and
  `f8919firm.wages` (147/4).
- **Source:** f8919 p. 1, Who must file: "You believe your pay from the firm wasn't for services as an independent
  contractor ... One of the reasons listed below under Reason codes applies to you." Reason codes: "If none of the
  reason codes apply to you, but you believe you should have been treated as an employee, enter reason code G and file
  Form SS-8 on or before the date you file your tax return."
- **Who could answer Yes wrongly:** a freelancer who would rather pay half the social security tax. The designed
  guard is the reason question, whose help says to send Form SS-8. **That question is never asked:** no line or target
  in int1 reads `f8919firm.reason` (grep of `forms/2025`, `interview/2025`: only its own definition and its bank entry;
  `forms/2025/person.yaml:1026` reads only `f8919firm.wages`). Lane x2-paynow2 recorded this on 2026-11-15 ("`f8919firm.reason`
  (column (c)) is never asked: no line reads it"); it is not in BUG_INVENTORY or TASKS. Not confirmed by a walk.
  Cost: Form 8919 instead of Schedule SE, 7.65% of the pay understated, and the printed column (c), which the form
  requires, left blank. Remedy: give column (c) a reader (a display target on the printed Form 8919), so the question
  is asked.
- **Who could answer No wrongly:** a misclassified worker who does not use the word "employee"; cost: over-taxed by the
  employer's half (the filer's own choice under f8919, which turns on belief).

### D4. `scope.tips_unreported` (146/22) — new parent

- **Tick label:** "Tips not reported in full to an employer, or noncash tips". Help: "Count cash and card tips you did
  not report to the employer, and tips such as tickets or goods. Tips in box 8 of a W-2 were asked about with the W-2."
- **Children:** roster `$f4137row` (148/1) with columns (c) and (d), `person.f4137_under20` (148/4),
  `person.tips_gov` (148/5, refuses), `person.tips_noncash` (148/6).
- **Source:** i1040gi p. 24, Line 1c, "This should include any tip income you didn't report to your employer"; p531
  p. 2, "The value of noncash tips, such as tickets, passes, or other items of value, is also income".
- **Wrong No:** a server who reported some tips and thinks that is "reported"; guard: "in full" in the label. Cost:
  tips and Form 4137 tax omitted. **Wrong Yes:** harmless (reported tips in column (d) are subtracted).
- **Known ordering defect, not a guard defect:** the government-tips refusal is told only at the Schedule 2 screens,
  not at its own question (lane note, "Findings from the coverage walks"; N11). Not re-checked here.

### D5. `scope.strike_pay` (146/23) — new parent

- **Tick label:** "Strike or lockout pay". Help: "Count it from a union or a strike fund, but not true gifts. State
  unemployment pay is not this; it is asked with Form 1099-G." Child `person.strike` (147/5). Source: i1040gi p. 24,
  Line 1h, "Strike or lockout benefits (other than bona fide gifts)". Wrong Yes by a filer on state unemployment during
  a strike: guarded by the help; cost, the same pay counted twice. Adequate.

### D6. `scope.medicaid_waiver` (146/2, box on `other_pay`) — existing, now a parent

- **Tick label:** "Medicaid pay, through any agency, for care of someone living with you". Help: "Also called
  difficulty of care payments, often paid through an agency or care plan. A W-2 with code II in box 12 shows them.
  Caring for someone who does not live with you is paid work in someone's home."
- **Children:** `person.mw_box1` (149/1), `person.mw_not_box1` (149/2) → `person.mw_1099` (149/3) →
  `person.mw_business` (149/4, refuses); `person.mw_earned` (149/5, the earned-income choice).
- **Source:** p525 p. 33, "Difficulty-of-care payments. These are payments that are designated by the payer as
  compensation for providing the additional care" (the archive's Notice 2014-7 treatment is cited in `person.yaml`).
- **Wrong No:** a parent paid through a fiscal agent to care for an adult child at home; guard: "through any agency"
  (BUG-0904 fixed). Cost: excludable pay taxed (over-taxed).
- **Wrong Yes:** a carer of someone who does not live with them; guard: the help's last sentence and the child's
  "who lived with you in your home". Cost: taxable wages excluded.

| Parent | Reached | q | g | C | Pays? |
|---|---|---|---|---|---|
| `scope.household_pay` | about 0.8% reach the screen | no data | 1 | 1 amount per person | Box on a screen; yes. |
| `scope.contractor_pay` | same | no data | 1 | roster 2 + 2 per firm | Yes. |
| `scope.tips_unreported` | same | no data (tips 1.95% microdata, most reported) | 1 | roster + 2 per employer + 3 | Yes. |
| `scope.strike_pay` | same | no data | 1 | 1 per person | Yes. |
| `scope.medicaid_waiver` | all returns | no data | 1 | 2 to 5 per person | Yes. |

### D7. New questions in this area that are not parents

`retirement.dis_all_early` (170/52) refuses on No ("a No ends the interview here"), asked only after `dis_early` Yes;
wrong Yes by a filer who reached the plan's minimum age late in 2025 is guarded by "each payment of 2025". The amount
questions beneath D2 to D6 are leaves.

---

## Findings for the bug inventory

Each is this scout's judgment from the text and gates read in int1; none was confirmed in a walk.

- **F2 (medium) `scope.nol` box: a capital loss carryover reads as Yes.** Tick label "A loss still being carried into
  2025 (a 'net operating loss')"; help excludes Form 8582 losses but not capital losses; `sd.carryover` comes later
  (276 after 258). About 4.5% of returns carry a capital loss (judgment) against 0.63% with an NOL (IRS). A wrong Yes
  deducts the capital loss on line 8a without the $3,000 limit and likely again on Schedule D. Source: i1040gi p. 91,
  Line 8a. Proposed fix: label and help say "from a business, farm, rental or disaster, not from selling investments",
  or gate beneath `scope.business_before` with a disaster route.
- **F3 (medium) `scope.household_pay`: no test of household employee against self-employed.** Line 1b is for "wages
  received as a household employee" (i1040gi p. 24); p926 pp. 3 to 4 makes a self-employed cleaner or lawn-care
  business not an employee. The label, prompt and help (which names "cleaner, gardener") invite business owners to put
  business income on line 1b, omitting self-employment tax. Proposed fix: a control question beneath the box, or the
  plain word for employee in the label.
- **F6 (medium) `f8919firm.reason` is never asked.** No reader in int1 (only `f8919firm.wages` is read,
  `forms/2025/person.yaml:1026`); the Form 8919 column (c) is blank and the SS-8 requirement (f8919 p. 1, Reason codes) that
  guards a wrong Yes to `scope.contractor_pay` is never put to the filer. Recorded in lane x2-paynow2's note, not in
  BUG_INVENTORY or TASKS. Proposed fix: a display target for the printed column (c).
- **F5 (low to medium; predates x2-dep) `sa.dependent`: wrong No by a claimable student or teenager is unguarded.** The
  birth year already identifies filers of 16 to 23; nothing cross-checks it. Since x2-dep, a wrong Yes also costs
  (smaller deduction; for a young parent, the loss of dependents, head of household and EIC) where it used to refuse.
  Source: i1040gi p. 33, Line 12a. Proposed fix: for filers aged 16 to 23 at the end of 2025, a plain child or box
  ("Did a parent list you as a dependent on their 2025 return, or could they?").
- **F1 (low) `sa.spouse_extra` asked after the typical No of `sa.spouse_itemizes` (N4).** Every MFS filer whose spouse
  takes the standard deduction reads a three-part conjunction about the spouse to answer No. Lane mfs-l2 kept it
  knowingly. Proposed fix: one screen with both facts, or a box.
- **F4 (low) `scope.recovery` tick label is in tax vocabulary.** "Money back for a deduction or credit"; the property
  tax, mortgage interest (Form 1098 box 4) and insurance-repaid medical examples that make an itemizer recognize it are
  only in the help (N6, N10; technique 3.6). Proposed fix: "Money back in 2025 for something on a 2024 return, such as a
  property tax or mortgage interest refund (not a state income tax refund)", within twelve words if shortened.

Not findings, recorded for the owner: `dependent.spouse_claims` asks another person's future act (cannot be guarded
better); `f8962.mfs_exception` rests on the filer's word, as the instructions do ("Send no proof"); `ira.mfs_spouse_covered`
has no route for a filer who cannot learn the spouse's coverage.

## What was read and seen, and what is inferred

- **Read in int1:** `docs/2026-11-13_interview_construction_protocol.md` (whole); `docs/2026-11-15_coverage_expansion_protocol.md`
  8.7 to 8.10; lane notes mfs-l1 to mfs-l4, x2-dep, x2-s1o, x2-paynow2 (sections 1 to 4 and their interview parts);
  every bank entry quoted (parsed from `interview/2025/questions.yaml`); the gate expressions quoted (parsed from
  `forms/2025/*.yaml`); `interview/2025/gate_frequencies.yaml` and `reports/2025/filer_coverage.md` for shares;
  BUG_INVENTORY headings and the entries for BUG-0864, BUG-0903, the inmate-pay reversal; archived source text for
  every quote (`sources/2025/*.cols.txt`).
- **Inferred, not checked:** that each question is asked only where its gate says (no walk run); the intersections of
  shares (marked "inferred product"); every q, g and C marked judgment; the costs in dollars (illustrative arithmetic
  at the 2025 rates, not evaluated by the engine); that F6's question is never shown (grep for readers, not a walk);
  the statuses of BUG-0933 and other entries not opened.
- **Not covered:** coverage areas of the other lanes of 2026-11-15 (x1-*, other x2-* lanes); New York.
