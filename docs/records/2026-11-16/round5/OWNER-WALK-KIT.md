# Owner walk kit (T-332): the seven new areas

**Status.** This kit is for the release candidate at http://localhost:8791/. It was written by lane D6-personas
(claude-opus-5-5, judgment, 2025, us) on 2026-11-16.

**How the kit was made, and what it rests on.**
- Each story is one of the new personas, 23 to 31 (`round5/personas.md`). The figures in the stories are the figures
  to type.
- The "watch for" items are findings still open after the fix round. They are gathered from `med-*.md`,
  `round4/*.md`, `MORNING-REPORT.md` and `decisions.md`.
- **Word counts:** a fork counted prompt and help words against the base bank tonight. The other items are relayed
  from those files, not re-checked.
- **Trims:** the N10 trims (`round4/trimA.json`, `trimB.json`) are not applied, so every long text listed is still
  long in the browser.

**Rating.** For each question listed, give two numbers from the scale of the protocol (1.1):
- the effort of the answer this filer gives;
- the effort of the other answer.

Note any question you would answer wrongly, and any refusal that comes later than the question that names it.

---

## 1. Schedule 1 other income: long-term care paid at a daily rate (Form 8853)

**Story to play (persona 23).** You are single, 56, with one job: W-2 box 1 $52,000, box 2 $5,200. Your mother's
long-term care policy, which you own, paid you $450 a day for 200 days ($90,000; "Per diem" and "Qualified contract"
checked). Her nursing home cost $76,000 for those days, and Medicare paid $8,000 of it.

**The end to expect.**
- Taxable payments $14,000 (Schedule 1 line 8e).
- If you leave Medicare out of the "reimbursed" question, it is $6,000. Which one is right is your open decision 8.

**Watch for.**
- **Where the topic starts.** It opens from one tick box on the "Did any of these happen" screen, which reads "A
  long-term care insurance payout, or life insurance paid early". Is that a plain place to find it?
- **Long prompts.** As shown with the "For this person …" frame:
  - "Were any of the payments a set amount" (39 words);
  - "was anyone besides you … paid" (49 words);
  - "How much of those care costs was … reimbursed" (42 words).
- **The reimbursement question.** It does not say whether Medicare or VA paying the home directly counts. You will
  have to decide.
- **Four refusals on the path:** the rate changed during the year; someone else was paid for the same person; a
  policy that is not "qualified"; a policy from before August 1996. Each should be told at its own question.
  - A rate rise during the year may be common. If so, that refusal will bite real filers (inferred).

**Rate:** `s1.ltc_payout` (the tick box), `f8853c.periodic`, `f8853c.others_paid`, `f8853c.rate_changed`,
`f8853c.days`, `f8853c.line22`, `f8853c.line24`.

---

## 2. Pay not on a W-2 (household pay)

**Story to play (persona 24).** You are single, 31, with one job (W-2 $52,000, box 2 $5,200). You also babysat for
two families, who paid you $2,300 and $2,600 with no W-2.

**The end to expect.** $4,900 added to wages on line 1b. No self-employment tax.

**Watch for.**
- **The first screen.** You reach the topic through the box "Wages, tips, or strike or lockout pay not on a W-2".
  Then a second screen, "Which of these were you paid", asks which kind.
- **The worst wrong answer.**
  - The household-pay box says "home, garden or driving work", and its prompt is 29 words.
  - A freelance tutor, or someone who runs a cleaning business, could tick it. Their pay would then be taxed as
    wages, with no self-employment tax.
  - Ask yourself whether a self-employed reader would stop.
- **The amount question.** "Add up the pay from every household …": check its length. A 47-word form text shows behind
  it.
- **The Medicaid-pay box** on the first screen (help 42 words). An agency aide who cares for clients in the clients'
  own homes might tick it.
- **"Religious work" box (53 words).** A one-time wedding officiant who ticks it is refused, which is more than
  necessary.

**Rate:** `scope.pay_no_w2`, `scope.household_pay`, `scope.contractor_pay`, `scope.wages_no_form`,
`person.household_wages`, `scope.medicaid_waiver`.

---

## 3. Married filing separately

**Story A, refused (persona 25).** You live in New York, married, filing apart from your husband. You never lived in a
community property state, but his permanent home is California. Expect the walk to stop at the question about his
state.

**Story B, completed (persona 26).** You live in Pennsylvania with your wife and file apart, because she itemizes her
medical bills. You have one W-2: $70,000, box 2 $7,000. You paid $2,849 of state and local income tax, gave $1,200 in
cash to charity, and rent your home.
- The end to expect: no standard deduction (it is $0 when she itemizes); itemized deductions of $4,049; tax $9,429.

**Watch for.**
- **The two state questions.** "Did you live in, or have your permanent home in …" (26 words) is followed by the same
  question about your husband or wife (33 words, help 41).
  - Would you know your spouse's legal home? For example a military spouse's home of record.
  - The spouse question's help still says "Count a marriage that ended in 2025 … Answer No if you were not married".
    That wording is stale after the fix round.
- **"Were you married on December 31?" (help 72 words).** It says "If your husband or wife died in 2025, answer No",
  which is wrong for a widow or widower who remarried in 2025.
- **Where "your spouse itemizes" comes (B).** It is asked late, after the deduction screens, so you enter Schedule A
  amounts before you learn that you must itemize. Is that order right?
- **Long texts:** the child-care question for a separate filer about the spouse's earnings (40 words, help 42); the
  mortgage-limit help for separate filers (43 words).
- **Joint estimated payments split on separate returns.** The help is 43 words, and the rule was drafted by a lane,
  not taken from a source. Your decision 9 is pending.

**Rate:** `f1040.status` (the "married, filing apart" line), `household.married_dec31`,
`household.community_property`, `household.spouse_cp_domicile`, `sa.spouse_itemizes`.

---

## 4. Dependent filers with income that is not pay

**Story A, completed (persona 27).** You are 19, and your parents claim you. You had a summer job (W-2 $6,000, box 2
$120) and $2,100 of interest on a CD your grandparents opened.
- The end to expect: standard deduction $6,450; tax $166; you owe $46.

**Story B, refused (persona 28).** You are 20, a full-time student, and your parents support you. You have $4,000 of
dividends from shares your grandparents gave you. Expect the walk to stop at the question about a parent and your
support (Form 8615 is not prepared).

**Watch for.**
- **"Can someone claim you as a dependent?" (help 56 words).** The people who answer it wrongly are:
  - a self-employed person who reads "income" as profit;
  - a student, 19 to 23, who paid their own support.
  - A wrong Yes cuts the standard deduction and removes credits. Your open question: keep the long help, or add a
    child question?
- **"More than $2,700 of income that was not pay" (help 24 words).** It counts scholarships, unemployment and trust
  income. A student may count a scholarship as pay and answer No.
- **The refusal (B).** It comes at the question on the parent and support (`scope.f8615`). Does it name your situation
  plainly?
- **Urgent, unrelated to the walk (owner action O9).** Commit `e812db31` (the `qdcg_amount` definition Form 8615 needs)
  is held by no branch. Pin it before a `git gc` or a worktree cleanup removes it.

**Rate:** `sa.dependent`, `scope.unearned_2700`, `scope.f8615`, `$interest`, `interest.amount`.

---

## 5. Foreign tax (Form 1116)

**Story to play (persona 29).**
- You are single, 52, with one job: W-2 $90,000, box 2 $11,000.
- An international index fund's Form 1099-DIV shows $6,000 of dividends (box 1a), $5,000 of them qualified (box 1b),
  and $360 of foreign tax (box 7). Its year-end statement says $4,000 of the income was foreign.
- Your 2024 Form 1116 carried $100 of unused foreign tax from 2024 into 2025.

**The end to expect.** Foreign tax credit $460: this year's $360 and the carried $100, all used. Tax $12,225; owed
$765.

**Watch for.**
- **The opening question (31 words, help 41).** "Have you ever paid income tax to another country …?" The help says to count a
  fund's foreign tax only if you once filed Form 1116. A first-year fund holder answers No. The foreign-tax amount
  is still asked later, as persona 04's walk shows, so the credit is reached (inferred). Is that confusing?
- **"How much foreign tax did you pay" (43 words).** It names three boxes on three forms.
- **The four-box screen** (gain from abroad, refund of foreign tax, reductions, loss accounts). The "reductions"
  label is the catch-all kind, with a help of 34 words.
- **The carryover questions:** "Which earlier years …" and its year list, which runs to the column numerals of the
  2024 Schedule B. Can you pick the year from your 2024 paper?
- **No Form 1116 under $300.** For small foreign tax, the credit is taken without the form automatically (your decision
  D3, recommended "confirm"). Foreign tax above your U.S. tax is then simply lost, with no carryover offered.
- **Unchecked lead.** Form 1116 line 3e may leave out rental and K-1 income from the division of deductions. Not
  confirmed by anyone.

**Rate:** `s3.foreign_any`, `ftc.carryover`, `ftc.taxes`, `ftc.all_passive`, `ftc.statements`, `ftc.eligible`,
`$f1116col`, `f1116col.div_income`, `$f1116sbyr`, `f1116sbyr.year`.

---

## 6. Digital assets: staking and an airdrop

**Story to play (persona 30).**
- You are single, 31, with one job (W-2 $52,000).
- You received $300 of coins from staking, and an airdrop of tokens worth $500 when they arrived.
- You later sold all the airdropped tokens for $800. The exchange sent Form 1099-DA with no basis (box H); your basis
  is the $500.

**The end to expect.** Other income $800; short-term gain $300; tax $4,247.

**Watch for.**
- **Every filer now meets the crypto question** (32 words; a parent's limit is 25; help 45). It costs one step for the
  filer with nothing. Your decision 10 recommends accepting it.
- **"As pay, a reward or new coins."** A credit-card holder whose card pays crypto rewards on purchases may answer
  Yes, although those are usually rebates (inferred).
- **The staking and airdrop question** (33 words, help 37). Is it plain that the amount is the value on the day the
  coins arrived?
- **Airdrops have no source of their own.** An airdrop not tied to a fork is counted only as a "similar activity"; no
  archived source says so.
- **Each sale costs about five screens.** Persona 17 (three sales) took 18 more steps.

**Rate:** `f1040.digital_assets`, `s1.digital_income`, `s1.digital_amount`, `sales.box`, `sales.correct_basis`.

---

## 7. Rental with personal use (Schedule E)

**Story to play (persona 31).**
- You are single, 31, with one job (W-2 $52,000).
- You own a lake cabin bought in July 2021; the building cost $200,000 without the land. You rented it by the month
  for 180 days in 2025, for $19,500, and stayed there yourself for 14 days.
- You paid mortgage interest $6,000, property tax $3,000, insurance $1,200 and utilities $1,800. You make the rental
  decisions yourself.

**The end to expect.**
- Costs are divided by 180/194 of the days.
- Rental income $1,618.76; tax $4,307.

**Watch for.**
- **"How many days was it used that way" (48 words).** It carries a 12-month main-home rule and an "or less if you
  then sold it" clause. It has not been moved to a child question yet.
- **"Rented at a fair price" (35 words) and the personal-use help (45 words).**
- **Average stays.** The question asks "30 days or less", then "7 days or less". A Yes to the second ends the
  interview. Exactly 30 days counts as Yes to the first.
- **The rare-items screen.** It can stop you too early:
  - "Part of a building you lived in or used yourself" might catch an owner who only keeps tools in the basement.
  - "Services for renters" might catch an owner whose manager only collects rent.
- **The building's cost question (43 words)** carries a "smaller of" rule for a former home.
- **Not asked at all.** The interview never asks about a like-kind exchange, or about a loss carried from a year
  when the place was also your home. Such returns are figured without those rules.
- **Scale.** The rental topic costs about 25 steps for a typical landlord (persona 19). Is that acceptable?

**Rate:** `scope.rental`, `rental.kind`, `rental.days_fair`, `rental.personal_any`, `rental.days_personal`,
`rental.short_stays`, `rental.stay7`, the `rental_rare` screen, `rprop.basis`.
