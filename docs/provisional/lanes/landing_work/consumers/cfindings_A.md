# Consumer-check findings, group A (5 of 108 pairs not ruled)

Read for every finding: the prompt file in /tmp/landing2/cprompts/us/, the reader's definition in
forms/2025 (scope.yaml or s1.yaml), the input's own line in forms/2025, and its entry in
interview/2025/questions.yaml (prompt, tick, help). Coverage by other inputs was checked by grep of
questions.yaml and forms/2025.

## 1. consumer:s1.ltc_payout@i1040gi:p91 (differs)
- Question: "payments under a long-term care insurance contract, or accelerated death benefits under a life
  insurance contract" (prompt: "paid by a long-term care insurance policy, or paid part of a life insurance
  death benefit early?").
- Page (line 8e, the reader's cite for this input): "Enter the total of the amounts from Form 8853, lines 8, 12,
  and 26" and "You may have to pay an additional tax if you received a taxable distribution from an Archer MSA
  or Medicare Advantage MSA."
- Why: lines 8 and 12 of Form 8853 are taxable Archer MSA and Medicare Advantage MSA distributions. The
  question asks only about long-term care and accelerated death benefits (line 26), so a filer with only
  a taxable MSA distribution answers No and s1.line8_other is not set. scope.archer_msa asks only about
  money put in during 2025. f8889.archer ("have an Archer MSA in 2025?") is asked only inside the HSA
  section. No question mentions a Medicare Advantage MSA.

## 2. consumer:s1.digital_income@i1040gi:p92 (differs)
- Question source: "digital assets as ordinary income not reported elsewhere on the return". The prompt the
  filer reads: "receive crypto or another digital asset as pay, as a reward, or from mining or staking?"
- Page (line 8v): "you received ordinary income in connection with digital assets that isn’t reported
  elsewhere on your return (for example, digital assets, such as income from forks, staking, or mining"
- Why: the page names forks. The filer-facing prompt lists pay, rewards, mining and staking, but not
  forks or airdrops, so a filer whose only line 8v income is coins from a hard fork can answer No. No
  question mentions forks or airdrops (grep found none). "As pay" also catches W-2 wages paid in crypto,
  which is harmless over-refusal.

## 3. consumer:scope.medicaid_waiver@i1040gi:p24 (differs)
- Question: "did a state Medicaid program pay you (or, on a joint return, your spouse) to care for someone who
  lives in your home". Help: "These are Medicaid waiver payments, also called difficulty of care payments."
- Page (line 1d, the reader's cite): "Enter your taxable Medicaid waiver payments that were not reported on"
  Form(s) W-2, and "If you do not have a separate trade or business of providing these services, enter on
  Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC."
- Why: the payments that can be excluded are the ones for care of someone who lives in the caregiver's
  home. Taxable Medicaid waiver payments, the main subject of line 1d, are generally those for care of
  someone who lives elsewhere, and the question excludes them. A caregiver paid on a 1099-MISC for a
  parent who lives elsewhere answers No. The excludable-payment rule comes from Notice 2014-7, not from
  this page. I did not check whether another question would catch that 1099 income some other way.

## 4. consumer:scope.education_recapture@i1040gi:p34 (differs)
- Question: "were you (or, on a joint return, your spouse) refunded tuition, or given tax-free aid, for a year
  for which an education credit had already been claimed?" (tick: "Got tuition refunded ...").
- Page (line 16): "You may owe this tax if you claimed an education credit in an earlier year, and either
  tax-free educational assistance or a refund of qualified expenses was received in 2025 for the student."
- Why: the page's trigger is a refund or aid received "for the student", who is often a dependent. The
  question asks whether you or your spouse were refunded or given aid. A parent who claimed the credit
  for a child, where the child got a 2025 scholarship or refund, can read this as No. "Tuition" is also
  narrower than "qualified expenses", which also include required fees and course materials.

## 5. consumer:scope.reforestation@i1040gi:p99 (unsure; low)
- Question: "own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before"
- Page (lines 24a-24z): "Enter reforestation amortization and expenses (see the Instructions for Form 4562)."
- Why: the page states no ownership condition. Section 194 reforestation costs may also be taken on
  qualified timber property held under a lease. That rule is from Reg. 1.194-3 as I recall it, not from
  this page, and I did not verify it. A lessee who reforested would answer No under "own". This is
  narrow and rare; I listed it because I was not sure enough to rule "same". The seven-year window
  appears to cover the 84-month amortization.

## Observation outside the pair verdicts (not a pair finding)
- i1040se p. 1, cited by scope.schedule1: "Use Schedule E (Form 1040) to report income or loss from rental
  real estate, royalties, partnerships, S corporations, estates, trusts, and residual interests in REMICs".
  scope.rental and scope.k1 together cover everything on that list except residual interests in REMICs.
  No question in questions.yaml or forms/2025 mentions REMIC residual interests outside the wash-sale text
  in sales.yaml. That is a gap in the reader's coverage, not a difference in what either question means,
  so I ruled consumer:scope.k1@i1040se:p1 "same".
