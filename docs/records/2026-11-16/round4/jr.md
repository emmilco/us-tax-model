# Lane A1-jr: v3 patches for the six REAL findings of jr-verify.md

claude-opus-5-5, judgment, year 2025, jurisdiction us. Written 2026-11-16, round 4. Paths are relative to the xint
worktree unless they start with P (= `.claude/nightplan-2026-11-16/nightplan`). **[C path:line]** = checked against
that file this session. **[I]** = inference or judgment, not checked. Nothing in xint was written. No build, engine,
walk, fixture run or model call was made. Patches were checked only by `patch -p1` on scratch copies, YAML/JSON
parsing, the project's own citation logic (`tools/citations.py` `segments`/`on_pages`/`anchor_on`, imported read-only
by `P/scratch/round4-jr/tools/checkloc.py`) and word counts by the tick-group rule (tokens with a letter or digit).

## Summary

**Files written.**
- `P/patches/v3/jr.patch` (14 files). **Base: the stack int-n10-ticks (v2), inc-m12 (v2), inc-m34 (v2),
  inc-m12-lows (v3), inc-m34-lows (v3).** Use this one.
- `P/patches/v3/jr.xint.patch`: the same changes made straight on xint. Use it only if that stack is not adopted.
- `P/patches/v3/jr-digital.patch` (optional, one hunk): a follow-on to the v2 inc-m12 BUG-0896 text. It applies
  after jr.patch.
- Scratch: `P/scratch/round4-jr/` (a/ and b/ xint copies, base/ = the stack, try/ = stack + jr, the checker scripts).

**The coordinator's overlap warning: what I did.**
- **scope.recovery.** v3 `inc-m34-lows.patch` (not m12-lows) changes the **help** for BUG-0908 (44 words)
  [C P/patches/v3/inc-m34-lows.patch:130-135]. Its tick stays "Paid back a deduction or credit that lowered tax (not
  state/local refund)", so it does not cover this finding, which is about the tick. **I dropped my help change and
  kept only the tick.** jr.patch therefore applies **after inc-m34-lows**.
- **f1040.digital_assets.** v2 inc-m12 (BUG-0896) already carries the jr-verify fix verbatim: prompt "get crypto … as
  pay or a reward, or sell, trade, spend or give any away?" and help "No: … getting it as a gift …" [C
  P/patches/v2/inc-m12.patch:1824-1835]. **jr.patch does not touch the entry.** The finding closes with that hunk. Two
  residual gaps are in the optional `jr-digital.patch` (section 4).
- **sche.qbi_business.** v2 int-n10-ticks adds a full prompt and moves the example to help [C
  P/patches/v2/int-n10-ticks.patch:~105-112]. jr.patch is based on that. It replaces the help and changes that prompt
  (section 5).

**Sequential apply tests** (patch -p1 on fresh xint copies; no fuzz, no offset message, no reject):
- int-n10-ticks, inc-m12, inc-m34, inc-m12-lows, inc-m34-lows, **jr**, **jr-digital**: clean. Every YAML file parses,
  and defaults.json parses.
- The coordinator's shorter sequence (int-n10-ticks, inc-m12, inc-m12-lows, jr) **fails one hunk** (scope.recovery):
  that hunk's context is inc-m34-lows's help. Include v2 inc-m34 and v3 inc-m34-lows, or use jr.xint.patch's hunk.
- The wide stack: sche-a, int-amt, int-p18, int-personas, int-n10, int-n10-ticks, inc-m12, inc-m34, older-ny,
  older-credits, older-scha, then the v3 lows (inc-m12, inc-m34, int, older-credits, older-scha, sche-a, older-ny),
  k1int-1..3, then jr and jr-digital.
  - jr and jr-digital apply clean.
  - The stack has failures that are **not jr's**: inc-m12 and inc-m34 each reject one hunk after `int-n10` (the
    known int-n10 versus n10-ticks choice), and sche-a-lows ignores a hunk.

**What the six changes are:**

| # | Finding | Change | Model change? |
|---|---|---|---|
| 1 (medium) | community property is decided by domicile | Wider prompt; a new question on the spouse's state; three readers rewired; the cp_married wording; the refusal remedies; two ambiguity entries | **yes** (5 new lines in household) |
| 2 | scope.recovery tick reads as the filer paying | tick only | no |
| 3 | sa.dependent Yes has no guard | help drafted; a child sketched (not in the patch) | no |
| 4 | f1040.digital_assets gift = Yes | none in jr.patch (landed by v2 inc-m12); optional follow-on | no |
| 5 | sche.qbi_business misses safe-harbor landlords | tick, help, n10-ticks prompt | no |
| 6 | mfs_living with spouses under one roof | help, form source, ambiguity reading | no |

**Owner decisions.** Each is put as a question in section 9.
1. Ask the spouse question on the ended-marriage path. It costs about 14% of returns [I] one step, to catch a very
   rare case. The patch asks it, as the brief said; the alternative is a one-line change.
2. The sa.dependent help is 56 words, against N10's "about 40". The protocol answer is the child question, sketched
   in section 3.
3. jr-digital: a 32-word prompt (N10's aim is 25), in exchange for catching a fork or airdrop filer.

**Corrections to earlier lane files** (checked):
- Military pay is on p555 **p. 6**, not p. 5 [C citations check; p555.cols.txt:138 is the page 5 footer].
- **Rev. Proc. 2019-38 is archived** (`sources/2025/rp-2019-38.*`, in manifest.json) [C]. jr-verify said it is not.
- **Pub. 915 is archived** [C manifest], but amb.2025.mfs_lived_apart still says it is not. Fixed in the patch.
- Pub. 555 itself says "When this publication refers to where you live, it means your domicile." (p. 3) [C]. That is
  the strongest support for finding 1.
- The current recovery tick's "(not state/local refund)" also invites a **property-tax** refund recipient to skip the
  box: a county property-tax refund is a local refund. The new tick says "income tax".

---

## 1. household.community_property: domicile (MEDIUM)

### What the patch does (forms/2025/household.yaml, questions.yaml, f1040.yaml, ambiguities, generator, defaults)

**Wording.**
- `household.community_property`:
  - Prompt (26 words): "At any time in 2025, did you live in, or have your permanent home in, Arizona, California, Idaho,
    Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?"
  - Help (37): "Your permanent home is the state you mean to return to when away, for example while on military orders.
    If you were married in 2025 and are not filing jointly, a Yes can end the interview here."
  - The form label and source are widened to match ("permanent home (domicile)"). Two p555 segments are added to the
    cite.

**New input `household.spouse_cp_domicile`** (order 103, seq 2, right after the parent).
- Prompt (33): "At any time in 2025 while you were married, did your husband or wife live in, or have their permanent
  home in, Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?"
- Help (41): "Count a marriage that ended in 2025, for the time before it ended. Their permanent home is the state they
  mean to return to when away. Answer No if you were not married in 2025. A Yes ends the interview here."
- `rdp` moves to seq 3 and `cp_married` to seq 4.

**New lines.**

| line | expression | read by |
|---|---|---|
| `spouse_cp_domicile_if_asked` (gate line) | choose: marriage_possible and status ≠ qss → the input; else household.no | cp_any, cp_spouse_ended |
| `cp_any` | choose on community_property: true → community_property; false → the gate line | mfs_community_property (mfs), hoh_cp_married (married) |
| `cp_spouse_ended` | choose on household.married: true → no; false → the gate line | cp_not_joint (its community_property = false branch, which was household.no) |

Because of these reads, the spouse question is asked only after a No to the parent, and only of:
- MFS filers (the mfs_community_property path);
- a married head of household (the hoh_cp_married path);
- ever-married filers not married at year end, filing single, HOH or MFS (the cp_marriage_ended path).

It is never asked of joint filers, QSS filers or anyone never married.

**Other wording.**
- `household.cp_married`, prompt and source: "while you lived in, or had your permanent home in, one of those states
  (…)".
- Three remedies are reworded: f1040 line 1a mfs_community_property and cp_marriage_ended, and the household
  hoh_community_property refusal. Each now reads "where either spouse lived in or had a permanent home in…". Without
  this, a filer refused for the spouse's state would read "who lived in a community property state".

**Ambiguities.**
- `amb.2025.mfs_community_property`:
  - text_at_issue drops "Pub. 555 and Form 8958 are not archived" and quotes p555 pp. 2–3.
  - reading 2 and chosen name the spouse question.
  - reason keeps D1 (the "lived in" over-refusal) and adds the other side.
  - cite is now p555, with p504 kept as a segment.
- `amb.2025.hoh_community_property`, a sibling: it had the same stale sentence. I replaced it with the p555 p. 2 quote,
  and reading 2 now names cp_any.

**Plumbing.**
- `engine/src/generate.ts`: the new input is added to FIXED (on its own line after line 195, which keeps it clear of
  inc-m12's hunk) and is set false beside cp_married. Without this, generated returns would draw it at random.
- `fixtures/2025/defaults.json`: `household.spouse_cp_domicile` = false, "Closed…", in alphabetical place.

### Red team, sentence by sentence (who answers wrongly; the source)

**Parent prompt, "live in, or have your permanent home in".**
- **Wrong No, now caught:**
  - A Texas-domiciled servicemember stationed in Virginia, or that servicemember's spouse.
  - A Californian on a long posting abroad.
  - Source: "where you are domiciled will determine if you have community property" (p555 p. 2) [C]; "When this
    publication refers to where you live, it means your domicile." (p. 3) [C]; "Active military pay earned while
    married and domiciled in a community property state is also community income" (p. 6) [C].
- **Wrong No, residual:**
  - A filer who moved away for good in 2024 but still "feels" a CP state is home: a Yes, which over-refuses only.
  - A servicemember who does not know their legal state of residence: the help example aims at them. [I]
- **Wrong Yes:** a student or servicemember living in a CP state while domiciled elsewhere. This is the accepted
  over-refusal (D1) and is unchanged.

**Parent help.**
- "Your permanent home is the state you mean to return to when away" paraphrases "a permanent legal home that you
  intend to use for an indefinite or unlimited period, and to which, when absent, you intend to return" (p555 pp. 2–3)
  [C].
- "a Yes can end the interview here" is accurate:
  - MFS and married HOH refuse at once.
  - An ended marriage refuses only after cp_married.
  - A never-married filer: nothing happens.

**Spouse prompt, "while you were married".**
- A filer divorced years ago answers No at once.
- A filer divorced in 2025 whose former husband moved to California only after the divorce answers No. That is right:
  "Any income received after the community ends is separate income" (p555 p. 10) [C].
- **Wrong No, residual:** an MFS filer who does not know the spouse's legal domicile, for example a military spouse
  whose "home of record" differs. The help gloss is the only guard. [I]
- **Wrong Yes:** the spouse works temporarily in a CP state but is domiciled elsewhere. The cost is an over-refusal,
  in the D1 direction.

**Spouse help.**
- "Count a marriage that ended in 2025, for the time before it ended": "taxed on half the community income for the
  part of the year before the community ends" (p555 p. 10) [C].
- "A Yes ends the interview here": the gate is "check the laws of each" (p555 p. 2) [C], which is outside the tool.

**cp_married "or had your permanent home in".** Same ground as the parent.

**Why the spouse-only case refuses rather than computes.** Spouses living apart all year still split community income
from property ("their share of the interest income from community property", p555 p. 9 example) [C
p555.cols.txt:227]. Other separated spouses "must treat your income according to the laws of your state" [C :228].

### Ended-marriage cost (owner decision 1)
- **Cost** [I]: the spouse question reaches every ever-married filer who is single, an unmarried HOH or MFS-not-married
  and answers No to the parent. That is roughly 14% of returns, from SOI single + HOH shares and a guess at ever-married.
  The answer costs 1 for almost all of them ("not married in 2025").
- **Gain:** divorced-in-2025 filers whose former spouse alone was domiciled in a CP state, perhaps 0.01 to 0.02% of
  returns [I].
- **To drop it:** in `household.cp_not_joint`, set the `community_property = false` branch back to `household.no` and
  delete `household.cp_spouse_ended`. MFS and married HOH keep the question, at about 2 to 3% of returns. Remove the
  rows household.divorced_2025_spouse_cp_domicile, household.single_divorced, household.hoh_divorced and
  hsa.former_spouse_* answers of the new input. Record the residual in amb.2025.mfs_community_property.

### Coverage rows and sets (predicted ends; none of the existing expected ends changed)

**The new answer `household.spouse_cp_domicile: false`, where a walk now passes the question:**
- Sets:
  - mfs.yaml `separate`
  - mfs_credits.yaml `separate`
  - mfs_deductions.yaml `mfs_filer`
  - dependents.yaml `mfs_one_listed`
- Rows:
  - mfs.spouse_died_2025
  - opening.separate
  - household.single_divorced
  - household.hoh_divorced
  - household.hoh_married_not_considered_unmarried
  - hsa.former_spouse_family
  - hsa.former_spouse_no_family
- Persona `15_mfs_separate_finances` (Ohio).
- **Why these** [C `P/scratch/round4-jr/tools/scan_rows.py`]: status single/hoh with ever_married true, or mfs, and the
  parent No. The background return is single and never married, so it never meets the question [C
  reports/2025/interview_coverage.md:1544-1553].
- **Rows not touched**, because their walk stops before order 103 [C report paths]: mfs.not_married,
  opening.married_picks_single, opening.widowed_this_year_alone, opening.living_apart_parent.
- **[I] One row may be stale.** household.hoh_married_not_considered_unmarried asks the parent before hoh_fails [C
  report:475], so I predict it also reaches the new question. If the walk does not ask it, drop the answer: the row
  will fail as stale.

**New rows:**

| id | answers (beyond status/marriage) | predicted end |
|---|---|---|
| mfs.spouse_cp_domicile | mfs, married_dec31 true, cp false, spouse true | refused household.mfs_community_property (the gate reads cp_any; told at the spouse answer, as mfs.community_property is at the parent's [I]) |
| mfs.spouse_cp_domicile_asked | mfs, married, cp false | asks household.spouse_cp_domicile |
| household.divorced_2025_spouse_cp_domicile | single, ever_married true, married_dec31 false, spouse_died false, cp false, spouse true | refused household.cp_marriage_ended (cp_not_joint → cp_spouse_ended → the gate) [I on when it is told: f1040 line 1a lists mfs_community_property, roster_bad, then cp_marriage_ended; the first two are settled] |
| household.hoh_married_asks_spouse_state | hoh, married, considered_unmarried true, cp false | asks household.spouse_cp_domicile (I chose `asks` because hoh_eligible lists hoh_absence before hoh_community_property, so the refusal may wait on dependent answers) |
| household.never_married_not_asked_spouse_state | single, ever_married false | proceeds, f1040.status single; not_asked the new input |

**Fixtures.** No fixture JSON is changed. For every existing case the default `false` makes `cp_any` equal to
`community_property` and `cp_spouse_ended` false, so every value and refusal is unchanged [I, by the expressions].
classm.*.json cases state community_property false and take the new default.

**Not checked [I]:**
- That the gate-line rule (formal gates design: "whose guards do not read it, and whose other alternatives are a
  parameter") accepts an `all`/`any` guard. Guards elsewhere are simple `eq` tests. If the build refuses, nest a second
  choose: status ≠ qss → marriage_possible.
- Mutation: the new choose operands may add surviving mutants. One example is the qss guard, which is equivalent on
  every return that reaches it. Watch the mutation baseline.
- tools/engines/generate_cases.py makes only single/hoh never-married and mfj cases [C :217, :639, :804], so it needs
  no change.

### Pending bug entry (candidate 1)
```
## BUG-NEW-JR-01 — household.community_property asks where the filer lived, but community income turns on each spouse's domicile; a separate or head-of-household return is computed without the split

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 1), ruled in lane jr-verify and drafted in lane A1-jr (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p555 p. 2, Domicile, "The law of the state, or the law of the foreign country, where you are domiciled will determine if you have community property, community income, or both. If you and your spouse (or your RDP) have different domiciles, check the laws of each"; p555 p. 3, "When this publication refers to where you live, it means your domicile."; p555 p. 6, Military retirement pay, "Active military pay earned while married and domiciled in a community property state is also community income."
- **Symptom:** household.community_property asks "At any time in 2025, did you live in Arizona, ... or Wisconsin?" and no question asks about the husband or wife. A married filer domiciled in one of the states who lived elsewhere all of 2025 (a servicemember on orders, or that servicemember's spouse), and a filer whose husband or wife alone was domiciled in one, answer No; household.mfs_community_property, household.hoh_community_property and household.cp_marriage_ended are then false and the return is computed with no community-income split (Form 8958). amb.2025.mfs_community_property and amb.2025.hoh_community_property still say Pub. 555 and Form 8958 are not archived; both are (sources/2025/p555.*, f8958.*). Pub. 555 confirms rather than removes the over-refusal kept in BUG-0732 item (4), which is not reopened. Not executed; read from the questions and the source.
- **Where:** forms/2025/household.yaml household.community_property, household.cp_married, household.hoh_cp_married, household.cp_not_joint, household.mfs_community_property, the hoh_community_property refusal; forms/2025/f1040.yaml line 1a refusal remedies; interview/2025/questions.yaml household.community_property, household.cp_married; ambiguities/2025.yaml amb.2025.mfs_community_property, amb.2025.hoh_community_property.
- **Proposed fix:** P/patches/v3/jr.patch: the prompt and form source ask "live in, or have your permanent home in"; a new input household.spouse_cp_domicile (gate household.spouse_cp_domicile_if_asked: marriage possible, not qualifying surviving spouse), asked after a No, which the three refusals read through household.cp_any (separate, married head of household) and household.cp_spouse_ended (marriage ended in 2025); cp_married and the three remedies say "lived in or had a permanent home in"; both ambiguity entries quote p555. Coverage rows mfs.spouse_cp_domicile, mfs.spouse_cp_domicile_asked, household.divorced_2025_spouse_cp_domicile, household.hoh_married_asks_spouse_state, household.never_married_not_asked_spouse_state.
- **Proposed fix lines:** household.community_property, household.spouse_cp_domicile, household.spouse_cp_domicile_if_asked, household.cp_any, household.cp_spouse_ended, household.hoh_cp_married, household.cp_not_joint, household.cp_married, household.mfs_community_property, household.hoh_eligible, f1040.line1a
- **Severity:** medium
- **Tags:** screen; false-no; community-property; married-filing-separately; household
```
(`hoh_eligible` and `f1040.line1a` are the lines that hold the reworded remedies [C household.yaml:1146; f1040.yaml:93-111].)

---

## 2. scope.recovery tick (low)

**Change.** The tick only (12 words): "Money back for a deduction or credit (not state/local income tax refund)". The help is
whatever the stack carries; on the base that is inc-m34-lows's BUG-0908 help.

**Red team** (source: "A recovery is a return of an amount you deducted or took a credit for in an earlier year";
"recoveries of items for which you previously claimed a tax credit", p525 p. 24 [C]):
- "Money back": incoming. A filer who repaid income (s3.repaid_income) no longer reads it as theirs.
- "for a deduction or credit": covers property tax, 1098 box 4, medical reimbursement, a repaid bad debt and credit
  rebates. **Residual:**
  - a filer who reads "deduction" as a payroll deduction, for example an excess 401(k) deferral returned. That is a
    wrong Yes, costing a few steps and probably a rec_kinds dead end [I];
  - a same-year refund, which leads to a few wasted steps [I]. The deductibility test, which turns on the year of the
    deduction, sits in the inc-m34-lows help.
- "(not state/local income tax refund)": a state income-tax refund stays out of the box, so there is no double count
  through rec_kinds "Something else you itemized". "income tax" also stops the property-tax refund recipient from
  excluding themselves, which the old "(not state/local refund)" invited [I].
- **Siblings.** The rec_rare and rec_kinds headings ("About the money paid back in 2025…") are seen only after the
  tick, and there "paid back" refers to the money just ticked. They are left unchanged, and that is judgment [I].

**Coverage and fixtures.** No path changes, so no rows. The existing s1o rows (rec_not_2024, rec_nonitemized,
rec_sales_tax) pass through unchanged [I].

```
## BUG-NEW-JR-02 — scope.recovery: the tick "Paid back a deduction or credit" reads as the filer paying, the opposite of a recovery

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 2), ruled in lane jr-verify, drafted in lane A1-jr (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p525 p. 24, Recoveries, "A recovery is a return of an amount you deducted or took a credit for in an earlier year".
- **Symptom:** Under the heading "Did any of these happen to you (or, on a joint return, your spouse)?" the tick reads "Paid back a deduction or credit that lowered tax (not state/local refund)", which reads as something the filer paid; s3.repaid_income uses "Paid back" for the filer's own repayment. A filer with a property tax or mortgage interest refund can leave it unticked (the recovery is left out of Schedule 1 line 8z), and "(not state/local refund)" also reads as excluding a county property tax refund. Not executed; read from the bank.
- **Where:** interview/2025/questions.yaml input scope.recovery (tick).
- **Proposed fix:** P/patches/v3/jr.patch: tick "Money back for a deduction or credit (not state/local income tax refund)" (12 words). The help is BUG-0908's (v3 inc-m34-lows).
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-no; wording; tick; recovery
```

---

## 3. sa.dependent (low): help drafted, child sketched

**Help in the patch** (56 words; N10 says about 40): "It is whether they can, not whether they do. At 24 or older, or
19 or older and not a full-time student, they can only if your income was under $5,200, unless you were disabled.
Answer No if that person need not file a return and files none, or files only to get back tax withheld."

**Red team, sentence by sentence:**
- "At 24 or older, or 19 or older and not a full-time student": the age test is "(a) under age 19 at the end of the
  year …; (b) under age 24 at the end of the year, a student …; or (c) any age if permanently and totally disabled"
  (p501 p. 12) [C]. Outside (a) to (c) only the qualifying-relative path remains.
- "they can only if your income was under $5,200": "the person's gross income for the year must be less than $5,200"
  (p501 p. 19) [C]; "If your gross income was $5,200 or more, you usually can't be claimed as a dependent unless you
  are a qualifying child" (p. 4) [C].
  - **Who still errs:**
    - A self-employed filer who reads "income" as profit (gross income uses gross receipts) [I].
    - A student aged 19 to 23 who paid over half their own support. The help states only a necessary condition, and
      the support test is left out for length. A wrong Yes there limits the deduction.
- "unless you were disabled": test (c). A disabled adult child earning $5,200 or more would otherwise answer No wrongly,
  overstating the deduction.
- The last sentence is unchanged. It is p501's "isn't required to file … files only to get a refund" [C
  p501.cols.txt:726].
- Joint filers: the help speaks to "you" only. On a joint return the joint return test applies, which is rare. [I]

**Child sketch** (not in the patch; this is the protocol's answer under N10, "a rule … goes into a child question").
- Ask under a Yes, only when `person.birth_year` gives age 19 or over at the end of 2025. birth_year is asked just
  before sa.dependent [C background #5, #6].
- `sa.dependent_young`: "Were you a full-time student during some part of 5 months of 2025, or permanently and totally
  disabled?" Ask it only for ages 19 to 23; from 24 only the disabled part matters.
  - A Yes passes.
  - A No opens `sa.dependent_income`: "Was your gross income in 2025, from all sources before any costs, under
    $5,200?" A No there sets dependent false, recorded with a note. Alternatively it refuses as a conflict, which is
    the safer first version.
- **A cheaper variant with no question:** a computed check (kind C gate). sa.dependent Yes, age 19 or over, not a
  student, and total income line 9 at $5,200 or more gives the conflict refusal `sa.dependent_conflict`. Line 9 is
  not gross income (business receipts), so this misses some filers but never over-claims.
- **N3** [I]: the child reaches about 1 to 2% of returns (Yes at 4.7% gf, times ages 19+). Its cost is 2 to 5.

**Coverage and fixtures.** Help only: none. The existing rows dep.* answer sa.dependent directly [C report:244-246].

```
## BUG-NEW-JR-03 — sa.dependent: a Yes now limits the standard deduction and denies credits, and the help gives none of the tests that decide whether someone can claim the filer

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 3), ruled in lane jr-verify, drafted in lane A1-jr (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p501 p. 4, "If your gross income was $5,200 or more, you usually can't be claimed as a dependent unless you are a qualifying child"; p501 p. 12, age test, "(a) under age 19 at the end of the year ...; (b) under age 24 at the end of the year, a student ...; or (c) any age if permanently and totally disabled"; p501 p. 19, Gross Income Test, "a person's gross income for the year must be less than $5,200".
- **Symptom:** sa.dependent asks "Can a parent or anyone else claim you (or, on a joint return, your spouse) as a dependent on their 2025 return?" with help only on "can, not do" and on a person who need not file. A Yes no longer refuses: it computes the dependent standard deduction worksheet (sa.dep_*), makes eic.step4 false, enters the saver's credit student test and refuses Form 8962. A filer aged 19 or over who is not a student or disabled, with gross income of $5,200 or more, cannot be anyone's dependent but can answer Yes. Not executed; read from the question and the source.
- **Where:** interview/2025/questions.yaml input sa.dependent (help).
- **Proposed fix:** P/patches/v3/jr.patch help (56 words, over N10's about 40; owner). Alternative per N10: a child beneath Yes for ages 19 and over (student or disabled; else gross income under $5,200), sketched in P/round4/jr.md section 3.
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-yes; wording; dependent-filer
```

---

## 4. f1040.digital_assets (low): merged with BUG-0896 in v2 inc-m12

**How they merge.** v2 inc-m12's BUG-0896 hunk is the fix for this finding as well:
- The prompt narrows receipt to "as pay or a reward". That is i1040gi's "(a) received (as a reward, award, or payment
  for property or services)" (p. 15) [C i1040gi-html.txt:1275].
- The help says "No: … getting it as a gift".

The new entry closes with BUG-0896, on the same commit. jr.patch has no hunk here.

**Optional `jr-digital.patch`** (applies after jr.patch; hunk at questions.yaml f1040.digital_assets):
- **Prompt "as pay, a reward or new coins"** (32 words, against 30 in v2).
  - Who errs on the v2 text: a holder whose only 2025 event was coins from a hard fork, or an airdrop. They do not
    read "pay or a reward" as theirs, answer No, and s1.digital_income is never asked, so the line 8v income is
    dropped.
  - i1040gi lists "Received digital assets as a result of a hard fork" and "mining, staking, and similar activities"
    as Yes [C i1040gi-html.txt:1277-1280]. Rev. Rul. 2019-24 covers the airdrop [C rr-2019-24.cols.txt:32-35].
  - Whether "new coins" invites someone who bought new coins with dollars: the help's "buying it with dollars" is No
    [I].
- **Help "getting it as a gift or an inheritance".** An heir is not "paid" or "rewarded", so the risk was small; the
  change costs 2 words.
- Gift or inheritance as No is [I], read from the (a) definition, as v2 inc.md also says.

```
## BUG-NEW-JR-04 — f1040.digital_assets: the prompt counts crypto received as a gift or inheritance as a Yes, so the printed Digital Assets box is checked Yes wrongly

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 4), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i1040gi p. 15, Digital Assets, "Check the 'Yes' box ... if at any time during 2025, you (a) received (as a reward, award, or payment for property or services); or (b) sold, exchanged, or otherwise disposed of a digital asset".
- **Symptom:** The prompt asks "In 2025, did you (or, on a joint return, your spouse) receive, sell, trade, spend or give away crypto or another digital asset?", dropping the form label's "(as a reward, award, or payment for property or services)". A filer whose only 2025 event was receiving crypto as a gift or an inheritance answers Yes: Form 1040 page 1 prints Yes where the instructions call for No, and s1.digital_income is asked without need. No tax amount changes. Not executed; read from the question and the source.
- **Where:** interview/2025/questions.yaml input f1040.digital_assets (prompt, help).
- **Proposed fix:** landed by the BUG-0896 hunk of P/patches/v2/inc-m12.patch (prompt "get crypto ... as pay or a reward, or sell, trade, spend or give any away?"; help "No: ... getting it as a gift"); close both entries on that commit. Optional follow-on P/patches/v3/jr-digital.patch ("as pay, a reward or new coins"; "a gift or an inheritance").
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-yes; wording; digital-assets; printed-answer
```
The page is p. 15 [C, the citation checker passes the quote and the anchor on p. 15 and fails them on p. 14].
jr-verify's "p. 16" is wrong.

---

## 5. sche.qbi_business (low): tick, help and the n10-ticks prompt

**Changes:**
- Tick (11 words): "A rental claimed for the qualified business income deduction (Form 8995)".
- Help (39): "Answer Yes if your 2024 Form 8995 or 8995-A listed a rental, or if you use the rental safe harbor (usually
  250 hours or more a year of rental services, with separate books). A Yes ends the interview here."
- Prompt: n10-ticks's "Do you treat a rental as a business for the qualified business income deduction?" becomes
  "Do you claim the qualified business income deduction for a rental (Form 8995 or 8995-A)?" (15).
- The form source is left alone. It still carries its own example and is the CLI text off the bank.

**Red team:**
- "claimed … (Form 8995)": a landlord whose software claimed the deduction now recognizes the form. Under N6 a plain
  description comes first, with the form in parentheses.
  - A filer whose Form 8995 listed only a Schedule C business: the tick says "A rental", so they answer No, correctly.
  - A landlord who qualifies but has never claimed: No, as before. That residual cannot be closed by wording. [I]
- "2024 Form 8995 … listed a rental" is a proxy: "The determination to use this safe harbor must be made annually" [C
  rp-2019-38 p. 5]. A prior claim gives a Yes, which only refuses.
- "usually 250 hours … with separate books": "Separate books and records are maintained" and "250 or more hours of
  rental services are performed" [C rp-2019-38 p. 5]. "usually" covers the 3-of-5-year rule for enterprises of 4 years
  or more [C rp-2019-38.cols.txt:105-109].
- i8995: "provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business"
  [C i8995 p. 1].

```
## BUG-NEW-JR-05 — sche.qbi_business: the tick drops its source's example, so a landlord who claimed rental QBI can answer No

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 5), ruled in lane jr-verify, drafted in lane A1-jr (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i8995 p. 1, Trade or business, "provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business for purposes of the QBI deduction"; rp-2019-38 p. 5, "Separate books and records are maintained", "250 or more hours of rental services are performed" and "The determination to use this safe harbor must be made annually".
- **Symptom:** The tick reads "A rental treated as a business for the qualified business income deduction" with help "A Yes ends the interview here."; a landlord whose earlier return listed the rental on Form 8995 or 8995-A (often by software) may not know it was "treated as a business" and answers No; the return is computed with no QBI deduction for the rental (an overpayment) where a Yes would refuse. Not executed; read from the bank and the sources.
- **Where:** interview/2025/questions.yaml input sche.qbi_business (tick, help, prompt).
- **Proposed fix:** P/patches/v3/jr.patch (based on v2 int-n10-ticks): tick "A rental claimed for the qualified business income deduction (Form 8995)"; help naming the 2024 Form 8995 or 8995-A and the safe harbor; prompt "Do you claim the qualified business income deduction for a rental (Form 8995 or 8995-A)?".
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-no; wording; schedule-e; qbi
```

---

## 6. household.mfs_living: spouses under one roof (low)

**Changes:**
- Help (32): adds "So does time you shared a home, even if you were separated."
- Form source: adds "and so does time you shared a home while separated", with a p501 p. 8 segment in the cite.
- `amb.2025.mfs_lived_apart`:
  - text_at_issue now says Pub. 915 only repeats the line 6d words (p. 1) [C]. The stale "not archived" is gone.
  - It quotes p501 p. 8: "Your spouse didn't live in your home during the last 6 months of the tax year" [C].
  - A fourth reading is added (separated spouses under one roof lived apart) and rejected.
  - chosen: the first reading, with a shared home counting as living together.
  - The reason gives the home-based wording of the 6-month tests and N8.
  - The status line drops "Pub. 915 to archive".

**Red team:**
- Who answered wrongly before: estranged spouses in one house choosing "Not at any time" or "Only before July". The
  help now names them.
- Who might now answer wrongly: owners of a duplex where each lives in their own unit. "Shared a home" is not their
  case, and the right answer is apart [I].
- The all-year reading has no archived definition (p915 [C], i1040gi [C]), so it stays an ambiguity reading. It is not
  a sourced rule.

**Coverage and fixtures.** None. The rows mfs.ssb_* and mfs_ded.ira_apart answer the choice directly. The values are
unchanged.

```
## BUG-NEW-JR-06 — household.mfs_living: an estranged husband or wife sharing the home can be answered as not living with the filer

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 7), ruled in lane jr-verify, drafted in lane A1-jr (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i1040gi p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025. Temporary absences for special circumstances ... count as time lived in the home"; p501 p. 8, Considered Unmarried, "Your spouse didn't live in your home during the last 6 months of the tax year."
- **Symptom:** household.mfs_living asks "In 2025, when did your husband or wife live with you?" with help on temporary absences only. A separated filer whose husband or wife still lived in the same home can answer "Not at any time in 2025" or "Only before July", though the sources measure living apart by the home; the answer then checks the line 6d box, lowers the social security base and passes the 6-month tests. amb.2025.mfs_lived_apart still says Pub. 915 is not archived; it is, and it gives no definition. Not executed; read from the question and the sources.
- **Where:** interview/2025/questions.yaml input household.mfs_living (help); forms/2025/household.yaml household.mfs_living (source, cite); ambiguities/2025.yaml amb.2025.mfs_lived_apart.
- **Proposed fix:** P/patches/v3/jr.patch: help "So does time you shared a home, even if you were separated."; the ambiguity entry adds and rejects the one-roof reading and corrects the Pub. 915 statement.
- **Proposed fix lines:** household.mfs_living
- **Severity:** low
- **Tags:** screen; wording; married-filing-separately; household
```

---

## 7. Reviews made due (review what changed; line-scoped where the tool allows)

- **household** (form content changed):
  - transcription and render, line-scoped: community_property, spouse_cp_domicile, spouse_cp_domicile_if_asked,
    cp_any, cp_spouse_ended, hoh_cp_married, cp_not_joint, cp_married, mfs_living, mfs_community_property, the
    hoh_eligible remedy;
  - class M for the three new computed lines and the three rewired ones;
  - completeness is sampled per release.
- **f1040:** transcription line-scoped on line 1a (two remedies only).
- **Screen and false-no**, sampled per release; these are the subjects the change makes due:
  - gate:household.community_property and the new gate:household.spouse_cp_domicile;
  - gate:scope.recovery, shown the **tick**: the last screen saw only the source [C
    .transcription/screens/gate_scope.recovery.prompt.txt:15, per jr-verify];
  - gate:sa.dependent;
  - gate:f1040.digital_assets, shared with BUG-0896;
  - sche.qbi_business.
- **Question reviews:** household.community_property, household.spouse_cp_domicile, household.cp_married,
  household.mfs_living, sa.dependent.
- **Tick-group renders:** money_b (scope.recovery) and rental_return (sche.qbi_business).
- **Ambiguity entries:** owner reading of the three changed entries.
- **Generated reports to rewrite:**
  - interview-coverage --write (the reports quote the wording);
  - the persona walks (persona 15 gains a step);
  - interview-order and tick-groups;
  - citations.md. Every new and changed locator passes the project's quote and anchor rules [C checkloc on xint
    sources].

**To run when the CPU is free** (not run here): build; test-fixtures (expect no value change); interview-coverage (all
rows, especially the five new rows and the [I] row above); tick-groups; draft-walk for personas 15 and 16;
interview-rules, including the order-independence baseline; citations; the gates check (gated_by rule); mutation.

## 8. What was checked and what was inferred

- **Checked:**
  - every quote cited in the patch, by the project's citation code;
  - p555 page numbers 2, 3, 6, 9 and 10, from the footers;
  - the readers of community_property [C grep];
  - the refusal-list order for line 1a and hoh_eligible;
  - the coverage rows that reach the new input [C scan + report paths];
  - the background answers [C report:1544];
  - the tick and heading limits (12 and 25) [C engine/src/tick-groups.ts:17-18];
  - no 2026 change operation touches a changed field (the only hit is the f1040.digital_assets cite.locator, which is
    not edited) [C grep changes/2026];
  - the sequential applies, as above.
- **Inferred [I]:**
  - when each new refusal is told;
  - that `all`/`any` guards pass the gate-line rule;
  - the cost and share figures;
  - every reader's misreading named above;
  - whether the hoh_married_not_considered_unmarried row reaches the new question.

## 9. Questions for the owner (each stands alone)

1. **Ask the spouse question after a marriage ended in 2025?** The patch asks every ever-married filer who is not
   filing jointly and not married at year end (about 14% of returns [I], one step each) whether a husband or wife
   during 2025 had a community-property-state home. This catches the rare case where only the former spouse was
   domiciled there, which Pub. 555 would settle by "the laws of each". Keep it, or limit the question to separate
   filers and married heads of household (about 2 to 3% [I]) and record the rest as a known gap? The one-line
   reversion is in section 1.
2. **sa.dependent: a 56-word help, or a child question?** N10 caps help at about 40 words and says a rule belongs in a
   child. The patch has the help. The alternative is a short question beneath a Yes, for ages 19 and over (student or
   disabled? if not, gross income under $5,200?), or a computed conflict check on total income. Which do you want?
3. **Apply jr-digital.patch?** It makes the digital-asset prompt "as pay, a reward or new coins" (32 words, over the
   25-word aim). A holder whose only crypto event was coins from a fork or airdrop would then answer Yes, so their
   line 8v income is not dropped. The cost is two more words for every filer.
