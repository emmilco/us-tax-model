# Fix plan: open MEDIUM entries in older areas (lane plan-med-older)

Lane: plan-med-older. Model claude-opus-5-5, judgment. Year 2025, us and ny. Read only; nothing in the repository
was changed. Every "checked" claim names the file read in the xint worktree
(`.claude/worktrees/xint`), the main tree as of `acde74b5` (read with `git show acde74b5:<path>`), or the archived
source under `sources/`. "Inferred" means no direct check.

## Summary

- **All 12 named entries are open** (`tools/bug_status.py`: each "open [only a proposal]"), and **all 12 are
  confirmed** against xint's forms, interview and the archived source.
- **Origin.** 11 of 12 predate tonight: the interview prompt/help and form source of each are byte-identical on
  `acde74b5` (checked: the question entries compared field by field; `forms/ny/2025/ny_it201.yaml`,
  `interview/ny/2025/questions.yaml`, `forms/2025/f5695.yaml`, `forms/2025/asset.yaml` have 0 changed lines against
  main). **BUG-0850 is new tonight**: the New York file is unchanged, but `retirement.dis_wages` / `person.dis_wages`
  (federal line 1h disability pensions) do not exist on main (`git grep dis_wages acde74b5 -- forms` finds
  nothing). Supporting them federally is what made the NY pension gate wrong.
- **One more uncovered open medium:** BUG-0790 (`asset.listed`, xrelbiz-16, Form 4562). The K-1/Schedule E lane does
  not cover it, and neither does the income-gates lane. It predates tonight. Every other open medium is in one of the two other lanes (map below).
- **Open HIGH:** only BUG-0629, parts (1) and (2), and T-295 (done 2026-11-14) appears to have fixed it. The entry
  only lacks a closure record. See the last section.
- **Stale-open (not medium, noted in passing):** BUG-0092 (Form 8889 tests filing status) looks fixed in xint:
  `f8889.married_family` and `f8889.age55_unmarried` read `household.married`
  (`forms/2025/f8889.yaml:1034,1040,1120`). Inferred that it needs only a closure record. It becomes more reachable
  with tonight's married-filing-separately expansion, so it is worth closing properly.
- **Most fixes change wording only** (interview prompt or help, sometimes the form `source`). Two change structure:
  BUG-0817 (ask the carryover of every filer) and BUG-0850 (widen a NY gate). A third, BUG-0861, does too if the
  owner wants Chart B computed.
- **Owner decisions needed: 7** (listed at the end). The biggest are BUG-0817 (change the structure or reword) and
  BUG-0861 (reword or compute).
- **An open point in BUG-0861 is already settled.** Its question whether self-employment of $400 or more counts was
  decided by owner decision D7(b) and registered as `amb.2025.ptc_dependent_filing`: Chart B only, Chart C does not
  count (checked: `ambiguities/2025.yaml:1592-1608`). The fix should cite it, not reopen it.
- **Source gaps:** Pub. 936 is not archived, so a gloss of "substantially improve" (BUG-0805) cannot be checked. No
  archived source names New York's "Advisor-Guided Plan" (BUG-0851). And i8862 says nothing about a spouse's
  earlier denial on a joint return (BUG-0797).

## Map of open mediums to lanes (checked: severity field, `/tmp/xint/assign.out`)

| Lane | Entries |
|---|---|
| this lane (older areas) | 0803, 0805, 0815, 0817 (Sch A); 0793, 0796, 0797 (credits); 0861, 0862, 0870 (people/retirement); 0850, 0851 (NY); **0790 (asset.listed, uncovered)** |
| K-1 / Sch E / rental / royalty | 0775, 0789 (xrelbiz-01, -15), 0836-0838, 0841-0843 (xrelk1p), 0882, 0885, 0886, 0890 (xrelsche), 0911 (xrev-01) |
| income gates | 0806, 0808, 0810, 0822 (xrelinc-06/08/10/22), 0830, 0833 (xrelinv), 0873 (xrelret-01), 0896-0907 (xrelwide) |

Entries before BUG-0605 have no Severity field. I skimmed the symptom of each one that has no "low" tag, and none
reads as medium beyond BUG-0092 (stale, above) and BUG-0647/0734 (2026 year-change, out of scope).

---

## Detail per entry

Word counts are from a script (whitespace split). Where a proposal is over the N10 aim (25 words for a parent, 40
for a child, about 40 for help), the current text is over it too, and the proposal is no longer than the current
one unless noted.

### BUG-0803 (xrelinc-03): Schedule A line 11 does not leave out gifts to foreign organizations

1. **Confirmed.** The `sa.line11` help in `interview/2025/questions.yaml` (about line 1594) leaves out "tuition, club dues, gifts
   to people, money paid back to you, and a gift's part that earned a state tax credit". The prompt leaves out
   "political gifts and raffle tickets". The `sa.gifts` help (line 848) lists kinds of charity and has no U.S.
   requirement. The source, `sources/2025/i1040sca.txt:770`, reads: "Gifts to foreign organizations. However, you
   may be able to deduct gifts to certain U.S. organizations that transfer funds to foreign charities and certain
   Canadian, Israeli, and Mexican charities".
2. **Origin:** before tonight. The text is identical on acde74b5.
3. **Failure mode:** line 11 is overstated for a filer who gave directly to a charity abroad. The value is wrong,
   and nothing refuses.
4. **Fix** (wording only):
   - `sa.line11` prompt: change "give to charity" to "give to U.S. charities". 48 words; the current one has 47.
   - `sa.line11` help, add: "A gift straight to a charity abroad is left out; a gift through a U.S. charity that
     sends money abroad counts." (21 words, which brings the help to about 66.) To stay under N10, drop "Count only
     gifts you have a bank record or receipt for" from the help and make it a clause of the prompt. That move is
     optional.
   - Add the same clause to the help of the `$gift` property list.
   - Source check: "U.S. organizations that transfer funds to foreign charities" supports the second half. The
     Canadian, Israeli and Mexican treaty cases are left out by this wording, which understates the deduction for
     those filers. Owner decision 1 is whether to leave them out or refuse them.
5. **Fixtures:** none change, because no input changes meaning. Reviews made due: the question reviews of `sa.line11`
   and `sa.gifts`, and the false-no sample of gate `sa.gifts` if its help changes. A screen's subject leaves out
   help (tools/README.md:520-533), so the screen review is not due. Rewrite the coverage report (`--write`) if a
   row meets the question.
6. **Effort:** 20 minutes.

### BUG-0805 (xrelinc-05): `sa.mortgage_other_use` says "improving", not "substantially improve"

1. **Confirmed.** The prompt in `interview/2025/questions.yaml` (about line 1364) reads "...other than buying,
   building or improving it, such as paying off other debts?". The source (`i1040sca.txt:573,594,598,603`) reads
   "buy, build, or substantially improve".
2. **Origin:** before tonight. Identical on main.
3. **Failure mode:** an equity loan spent on repairs or furniture is answered No. The limited-interest refusal is
   missed, and line 8a is overstated.
4. **Fix:**
   - Prompt: "Was any of the money borrowed against your home used for something other than buying, building or
     substantially improving it, such as paying off other debts?" (26 words). This is backed by the source's own
     word.
   - Help, add: "Repairs, upkeep and furniture are other uses." This needs Pub. 936, which defines the term, and Pub. 936 is
     not archived (checked: no `p936*` under `sources/2025`). Owner decision 3: archive Pub. 936 (a free fetch)
     before adding the gloss, or ship the prompt alone.
5. **Fixtures:** none. Reviews due: the question review of `sa.mortgage_other_use`, and the screen and false-no
   samples of gate `sa.has_mortgage_interest` (the screen's prompt changes).
6. **Effort:** 15 minutes, plus 10 to archive Pub. 936.

### BUG-0815 (xrelinc-15): the other-state-tax gate omits a refund applied to 2025 and other withholding

1. **Confirmed.** `sa.state_tax_other_any` is a tick in group `paid_2025` (about line 1545). Its help names a pension,
   unemployment and winnings, but not 1099-NEC, 1099-MISC or IRA withholding, and not an applied refund. Its prompt
   says "estimated payments". The source is `i1040sca.txt:230`: "including any part of a prior year refund that you
   chose to have credited to your 2025 state or local income taxes".
2. **Origin:** before tonight.
3. **Failure mode:** a false No makes line 5a too small, so the deduction is understated (taxpayer-unfavourable).
4. **Fix:**
   - Help: "Count state tax taken out of anything but wages (a pension or IRA, unemployment, winnings, a 1099-NEC or
     1099-MISC); an earlier year's refund you applied to 2025; disability or family leave fund from pay (W-2 box 14
     or 19); territory tax; a charity tax credit applied." (46 words; the current one has about 50.)
   - Prompt: "...such as estimated payments (including an earlier year's refund applied to 2025) or a payment with a
     state return...".
   - Source check: the withholding list comes from i1040sca p. 3 ("Forms W-2G, 1099-G, 1099-R, 1099-MISC, and
     1099-NEC may also show state and local income taxes withheld"), quoted in the entry. I did not re-grep that
     sentence (inferred from the entry).
5. **Fixtures:** none. Reviews due: the question review, and the false-no sample of gate `sa.state_tax_other_any`. The
   tick label does not change, so the screen review is not due.
6. **Effort:** 15 minutes.

### BUG-0817 (xrelinc-17): a filer with 2025 gifts and an earlier carryover is led to answer No

1. **Confirmed.** `sa.gift_carryover` is reached only through `sa.gift_carryover_if_no_gifts`, which is guarded by
   `sa.gifts = false` (`forms/2025/sa.yaml:155-170`). A filer who gave in 2025 meets the carryover only inside
   `sa.charity_limited` (`interview/2025/questions.yaml` about line 1267). Its parenthesis, "(A limit can apply only
   when the year's gifts are more than 20% of your income.)", invites a No from a carryover-only filer. Line 13
   refuses on both gates (`sa.yaml:1574-1597`). The source is `i1040sca.txt:831` ("5 years to use contributions").
2. **Origin:** before tonight, from the provisional redraft, lane 7a. Coverage rows `home.gift_carryover_only` and
   `home.gifts_of_money` (`interview/2025/coverage/home.yaml:150-170`) encode the current design.
3. **Failure mode:** a carryover is dropped from line 13 without a refusal. The deduction is understated, and the
   return is reported as complete when it should be refused.
4. **Fix** (owner decision 2):
   - **(a) Recommended (N1, one subject):** ask `sa.gift_carryover` of every filer. It is already a tick in group
     `paid_more`, so the added cost is one box. Make `sa.gift_carryover_if_no_gifts` a plain copy of
     `sa.gift_carryover` and keep its id, so line 13's refusal entry is unchanged (technique 3.1). Relabel it. Remove
     the carryover clause from `sa.charity_limited`. Prompt: "Were your 2025 gifts to charity so large that the law
     limits what you can deduct? (This can happen only when they are more than 20% of your income.)" (29 words).
     Help: drop "or carried-over".
     - Coverage: `home.gifts_of_money` loses `not_asked: [sa.gift_carryover]` and answers it false.
       `home.gifts_limited` keeps its end, and a new row `home.gifts_and_carryover` (gifts Yes, limited No,
       carryover Yes) must end refused on `sa.gift_carryover_if_no_gifts`.
     - Fixtures: `sa.gift_carryover` has a default (`fixtures/2025/defaults.json:4571`), so hand fixtures need
       nothing. Class M and mutation take no defaults, so check whether class M cases with `sa.gifts = true` now leave
       `sa.gift_carryover` unanswered (8 files reference it).
   - **(b) Wording only:** "Were your 2025 gifts to charity so large that the law limits what you can deduct (only
     possible above 20% of your income)? Or is a gift from an earlier year that was too large to deduct then still
     carried over?" This still asks two things in one question.
5. **Reviews due:**
   - (a): transcription review, line-scoped, of `sa.gift_carryover_if_no_gifts` and `sa.charity_limited` (label and
     source change); screen and false-no samples of both gates; question reviews; and the coverage report.
   - (b): question review and false-no of `sa.charity_limited` only.
6. **Effort:** (a) about 1 hour with the rows. (b) 15 minutes.

### BUG-0793 (xrelcred-01): the EIC lived-with-relative screen omits step and foster older relatives

1. **Confirmed.**
   - Form source (`forms/2025/eic.yaml:14-28`): "...your parent, grandparent, brother, sister, aunt or uncle, or a
     foster parent? Count time you were temporarily away, for example at school."
   - Interview help: "Stepparents, half brothers and sisters, great-grandparents, great-aunts and great-uncles count
     too. If you are not sure, answer Yes."
   - The form's own note states the correct rule: "parent, stepparent, foster parent, brother or sister (step or half
     included) or an ancestor of one of them".
   - Source: `i1040gi.txt:923` / `:2674` ("stepbrother, stepsister ... or a descendant of any of them"), and
     `:763-788`, "Temporary absences by you or the other person".
2. **Origin:** before tonight. The source and help are identical on main.
3. **Failure mode:** a false No skips Step 3 question 6 and Step 4 question 5, and the EIC can be allowed to someone
   who is another person's qualifying child. That is an overstated credit.
4. **Fix:** over-inclusion is safe here, because a Yes only asks the next question.
   - Source/prompt: "In 2025, did you live for more than half the year in the same home as a parent, grandparent,
     brother, sister, aunt or uncle, counting step, half and foster relatives?" (30 words; the current one has 31).
   - Help: "Great-grandparents, great-aunts and great-uncles count. Time either of you was away for a while, such as at
     school, counts as time together. If you are not sure, answer Yes." (29 words.)
   - The entry also asks to add the birth or death exception. That exception (i1040gi p. 41 TIP) is about the child.
     For this question, a relative who died in 2025 after living with the filer is still covered by "If you are not
     sure, answer Yes". I suggest leaving the birth/death clause out, to stay within N10 (judgment).
5. **Fixtures:** none (8 files reference the input; its meaning only widens). Reviews due: line-scoped transcription
   of `eic.lived_with_relative` (the source changes); the question review; the screen and false-no samples of gate
   `eic.lived_with_relative`.
6. **Effort:** 20 minutes.

### BUG-0796 (xrelcred-04): Form 5695 opening question drops construction timing, condo share, consecutive-year panel, and 21a tense

1. **Confirmed.**
   - The `f5695.any` help (about line 5913): "It counts for 2025 if the installation was finished in 2025, whenever it
     was paid for." The tick group heading is "And in 2025, did you (or, on a joint return, your spouse) do any of
     these?".
   - `f5695.condo` (about line 6351) and `f5695.construction_later` (about line 6000) are reached only after a Yes.
   - The panel tick reads "A new or upgraded electrical panel, circuits or wiring", in the 2025 frame.
   - The `f5695.line21a` prompt says "that you live in?". The consecutive-year choice appears only in the `line25a`
     help and form source (`forms/2025/f5695.yaml:3713-3733`).
2. **Origin:** before tonight (the redraft on main; identical on acde74b5). The entry tags it as a regression of the
   BUG-0552 and BUG-0553 fixes.
3. **Failure mode:** false Nos, so the credit is lost. That understates the credit (taxpayer-unfavourable), and
   nothing refuses.
4. **Fix:**
   - `f5695.any` help: "Count work finished in 2025, and work in a home built or rebuilt that you first lived in
     during 2025. Count your share of work a condo association or housing co-op paid for. A panel, wiring or energy
     audit counts. If in doubt, answer Yes." (45 words; the current one has about 33. Slightly over the aim; the
     furnace/boiler sentence is dropped because the tick already says "heating equipment".)
   - Source check, against i5695 p. 1 and p. 2 as quoted in the entry: construction applies to Part I only,
     reconstruction to both parts. The help is wider than the rule for Part II construction. That is harmless at a
     gate, because `f5695.b_new_home` exists below it (checked: interview line 6173).
   - Panel tick: "An electrical panel, circuits or wiring, put in in 2024 or 2025" (12 words). A 2024 panel with no
     2025 item gets No at `line25a` and no credit (checked: `line25a` source, `f5695.yaml:3722-3727`).
   - The reverse case (a 2025 panel enabling a 2024 item) stays unasked. It is rare; note it on the entry.
   - `f5695.line21a`: "...at a home in the United States that you lived in during 2025?" (22 words). Source: i5695 p. 3,
     "a home that you used during 2025 located in the United States". Change the form `source` to match.
5. **Fixtures:** none change values (12 files reference `f5695.any`). Reviews due: the question reviews of
   `f5695.any`, `panel` and `line21a`; the screen and false-no samples of gates `f5695.any`, `panel_if_any` and
   `line21a`; line-scoped transcription of `f5695.line21a`. The entry asks to re-check the kind-gate samples; only
   the kind gates whose tick or help text changed are due (the cost rule).
6. **Effort:** 30 minutes.

### BUG-0797 (xrelcred-05): Form 8863 ban help tells a filer whose ban has run out to answer No

1. **Confirmed.**
   - The `f8863.ban` help (`interview/2025/questions.yaml`, order 242): "Answer No if, after that, you filed Form
     8862 with a later year's return and the credit was then allowed, or if a bar has run out...".
   - `sources/2025/i8862.txt` (exceptions, lines about 76-92): Form 8862 is not needed only when "(a) you filed Form
     8862 (or other documents) and your credit was then allowed, and (b) your credit has not been reduced or
     disallowed again". The end of a ban is not an exception.
   - Also `i8863.txt:48-54`.
2. **Origin:** before tonight (identical on main).
3. **Failure mode:** the American opportunity credit is claimed without Form 8862, so the return is wrong and should
   have been refused.
4. **Fix:**
   - Help: "Answer No only if, after the denial, you filed Form 8862 for this credit with a later year's return and
     the credit was allowed. A ban that has ended does not make the answer No. A Yes ends the interview here." (41
     words.)
   - Spouse: i8862 says nothing about a spouse's earlier denial on a joint return (checked: its "joint" mentions are
     about SSNs and qualifying children only). Owner decision 5: keep "you", or widen to "(or, on a joint
     return, your spouse)" and register it as an ambiguity.
5. **Fixtures:** none. Reviews due: the question review, and the false-no sample of gate `f8863.aoc_claimed`.
6. **Effort:** 15 minutes.

### BUG-0861 (xrelpeople-01): `dependent.ptc_files` states only the single, under-65, not-blind tests

1. **Confirmed.**
   - Source, `forms/2025/dependent.yaml:2242-2258`: "...for a single dependent under 65 and not blind". The interview
     help repeats it.
   - Chart B (`sources/2025/i1040gi.txt`, "Chart B—For Children and Other Dependents"): earned income includes
     "taxable scholarship and fellowship grants". For a dependent 65 or older or blind the limits are "$3,350
     ($5,350 if 65 or older and blind)" and "$17,750 ($19,750...)". Married dependents have their own rows and the $5
     spouse-itemizes rule.
   - i8962 p. 8 (`i8962.txt:205-215`): "required to file an income tax return because their income meets the income
     tax return filing threshold".
2. **Origin:** before tonight.
3. **Failure mode:** both directions. Scholarship-only income is answered No, so the PTC is overstated. A dependent
   65 or older or blind with income between the limits is answered Yes, so the PTC is understated.
4. **Fix:** owner decision 4.
   - **Wording:**
     - Prompt: "Did this dependent have enough income of their own in 2025 to have to file a tax return: more than
       $1,350 not from work, or more than $15,750 of pay (a taxable scholarship counts as pay)? A return filed only
       to get a refund does not count." (47 words; the current one has about 45.)
     - Help: "With both kinds, they must file when the total is more than the larger of $1,350 and their pay (up to
       $15,300) plus $450. A dependent 65 or older or blind has higher limits: $3,350 not from work, $17,750 of
       pay." (41 words.)
     - The form source drops "for a single dependent under 65 and not blind" and says "by Chart B".
     - Married dependents' different limits are left to the source wording (rare).
   - **Computed:** ask whether the dependent is blind (age comes from `dependent.age`, an input,
     `dependent.yaml:39`), married from `dependent.married`, and the two amounts. Compute Chart B. This takes 2 to 3
     hours, plus class M cases.
   - The self-employment point is already decided (D7(b), `amb.2025.ptc_dependent_filing`). Cite it on the closure.
5. **Fixtures:** one file references the input, so no change for wording. Reviews due: line-scoped transcription of
   `dependent.ptc_files`; the question review; the screen and false-no samples of gate `dependent.ptc_files`.
6. **Effort:** wording 30 minutes; computed 2 to 3 hours.

### BUG-0862 (xrelpeople-02): `household.credit_disallowed` omits the ACTC and credits taken back after an audit

1. **Confirmed.** The interview prompt names "a child tax credit, a credit for other dependents or an earned income
   credit". The help has no audit or repayment clause. The form source already names the additional child tax credit
   (`forms/2025/household.yaml:748-752`), so only the interview wording is narrow. Sources: i8862's table (CTC,
   RCTC, ACTC, ODC; `i8862.txt:30-60`) and `i1040gi.txt:4225`.
2. **Origin:** before tonight.
3. **Failure mode:** a credit is claimed without Form 8862 instead of refusing.
4. **Fix:**
   - Prompt: "Has the IRS ever reduced or refused a child tax credit (including the additional child tax credit), a
     credit for other dependents or an earned income credit that you (or, on a joint return, your spouse) claimed,
     other than to fix a math or clerical error?" (46 words; the current one has 39).
   - Help: "Count any earlier return, including a joint return with someone else, and a credit taken back after an IRS
     letter asking for proof or an audit, even one you agreed to. If you are not sure, answer Yes. A Yes ends the
     interview here." (44 words.)
   - Leave out the entry's "only an arithmetic or missing-SSN notice is a math error". No archived source defines
     math or clerical error (checked: `grep` of i1040gi and i8862 finds only the phrase). That the audit clause is not
     a math error is inferred from the phrase.
   - Also drop the year detail from the help (1997 for EIC, 2016 for the others): about 10 words. A filer cannot have
     an earlier denial outside those years that would change the answer in practice (judgment). Or keep it and
     accept about 55 words.
5. **Fixtures:** none (11 files reference the input). Reviews due: the question review, and the false-no sample of
   gate `household.claims_8862_credit`.
6. **Effort:** 15 minutes.

### BUG-0870 (xrelpeople-10): the missed-RMD question names only a yearly minimum

1. **Confirmed.**
   - `person.rmd_missed` prompt (order 180, seq 25): "Did you take less than the required yearly minimum out of a
     retirement account by its deadline". The help says "usually must take a minimum amount out each year".
   - The form source is neutral: "a required minimum distribution ... by its deadline" (`forms/2025/person.yaml:7389-7392`).
   - Source, `i5329.txt:640`: "due for the tax year that includes the last day by which the minimum required
     distribution must be taken".
2. **Origin:** before tonight (the interview text is identical on main).
3. **Failure mode:** the excise tax is missed and the return computed without a refusal (5-year or 10-year deadline;
   first distribution due April 1, 2025).
4. **Fix:**
   - Prompt: "For this person (you, or your spouse on a joint return) — Was any amount you had to take out of a
     retirement account by a 2025 deadline not taken out in full by then, even if you made it up later?" (42 words,
     including the fixed 9-word frame; the current one has 36.) "A 2025 deadline" is exactly the i5329 rule: a first
     distribution due April 1, 2026 is correctly outside it.
   - Help: "This includes a yearly minimum, a first required amount due April 1, 2025, and emptying an inherited
     account by its 5-year or 10-year deadline. A Yes ends the interview here." (30 words.)
   - The QDRO alternate payee (entry item 3) is rare. Widening the `person.inherited_account` tick help to "or a
     share of someone's account you received under a divorce order" is optional (inferred: the source of the
     alternate-payee RMD rule is not archived; p590b would need checking).
5. **Fixtures:** none. Reviews due: the question review, and the false-no sample of gate `person.rmd_possible`.
6. **Effort:** 15 minutes, plus 15 for the p590b check if the QDRO clause is added.

### BUG-0850 (xrelny-01): the NY pension gate misses line 1h disability pensions (NEW tonight)

1. **Confirmed.**
   - `ny_it201.has_pension_income` is `line9 > 0 or line10 > 0` (`forms/ny/2025/ny_it201.yaml:783-793`). Its note
     still says federal screens refuse a disability pension paid as wages, which is no longer true.
   - `retirement.dis_wages` and `person.dis_wages` (`forms/2025/retirement.yaml:649`,
     `forms/2025/person.yaml:1941-1958`) put such pensions on `f1040.line1h`.
   - Line 26 refuses on `gate.line26` (`ny_it201.yaml:831-841`), so the effect of the gap is a missed refusal.
2. **Origin:** new tonight, from the interaction of the federal line 1h support (not on acde74b5) with an unchanged NY file.
3. **Failure mode:** NY tax is overstated with no refusal for a government disability pension.
4. **Fix** (expression sketch):

   ```yaml
   - id: ny_it201.dis_pension_wages
     printed: '(helper)'
     type: NonNegDollars
     label: 'Disability pensions paid before the minimum retirement age, in federal wages (Form 1040 line 1h)'
     expr: { op: sum_over, collection: person, field: person.dis_wages }
   - id: ny_it201.gov_pension_candidate
     printed: '(gate)'
     type: Bool
     label: 'Pension, annuity or IRA income on line 9 or 10, or a disability pension in wages'
     expr: { op: test, any: [ { op: test, eq: ["ny_it201.has_pension_income", {const: true}] },
                              { op: test, gt: ["ny_it201.dis_pension_wages", {const: 0}] } ] }
   ```

   - Use `gov_pension_candidate` in place of `has_pension_income` in `ny_it201.gov_pension_if_income` and
     `ny_it201.gov_said_no` only.
   - Leave the line 29 chain (`ny_it201.yaml:917`) on lines 9 and 10. Whether a pre-retirement disability pension is
     "pension and annuity income" for line 29 is a separate source question. Do not widen it silently; note it on the
     entry.
   - Fix the note.
   - The existing prompt ("pension or retirement money from the federal government, the military, or a New York State
     or local government job") reads correctly for a disability pension (judgment).
5. **Fixtures:** add a NY case with a full-year resident, a disability Form 1099-R wholly before the minimum
   retirement age, and `gov_pension` Yes, expecting a refusal at `ny_it201.line26`. The entry's witness is
   `/tmp/xrel/ny/dis_inputs.json`. Add one with `gov_pension` No, expecting `line26` $0 and no refusal. Reviews due:
   line-scoped transcription of the changed NY lines; the screen and false-no samples of gates
   `has_pension_income`/`gov_pension_if_income` and `gov_said_no` (their subject changes); the NY coverage report if
   rows meet them.
6. **Effort:** 1 hour.

### BUG-0851 (xrelny-02): the NY 529 ownership question is in the present tense

1. **Confirmed.**
   - Source (`forms/ny/2025/ny_it201.yaml:694-700`): "Is any 529 account you (or, on a joint return, your spouse)
     own part of New York's own 529 college savings program?".
   - `gate.line22` and `gate.line30` both hang on it (`:707`, `:930`).
   - Source text, `sources/ny/2025/ny_it201i.txt:472-505`: "the transfer to another state's program" is
     nonqualified, and "qualified postsecondary credentialing expenses ... at an eligible educational institution on
     or after July 4, 2025".
   - The federal gate `person.x_edu_account` ("money put into or taken out of", `person.yaml` about line 7104) does
     reach the NY question for a rollover.
2. **Origin:** before tonight (NY files unchanged).
3. **Failure mode:** the line 22 recapture is left out silently, so NY tax is understated.
4. **Fix:**
   - Source/prompt: "At any time in 2025, did you (or, on a joint return, your spouse) own an account in New York's
     529 college savings program?" (24 words.)
   - Help: "Count an account you closed or moved to another state's plan during 2025. A 529 plan of another state, or
     an account someone else owns for you, counts as No." (30 words.)
   - Do not name the "Advisor-Guided Plan": it is not in any archived source (checked: `grep` finds only "Direct
     Plan", in the refund-allocation section). This is owner decision 7, if the name is wanted.
   - `ask.529_nonqualified` prompt: "In 2025, did you take money out of that New York 529 account for anything but
     college, student loans, or career training at a college or other eligible school from July 4 on? A move to
     another state's plan counts." Move "school tuition before college" to the help. Mirror the form label's list
     (`ny_it201.yaml:175-182`).
5. **Fixtures:** none change (3 files, 7 references). Reviews due: line-scoped transcription of `ask.ny_529` and
   `ask.529_nonqualified`; the screen and false-no samples of gates `has_edu_account` and `ny_529_if_account`; the
   question reviews.
6. **Effort:** 30 minutes.

### BUG-0790 (xrelbiz-16, uncovered by the other lanes): `asset.listed` narrows listed property to "equipment"

1. **Confirmed.**
   - Interview prompt: "equipment of a kind used for entertainment or recreation (such as a camera, or sound or video
     recording equipment)".
   - Form source (`forms/2025/asset.yaml:1065-1075`) and i4562 (`i4562.txt:180`): "photographic, phonographic,
     communication, and video recording equipment".
   - A boat: p946 classes boats as "Other property used for transportation" (`p946.txt:3635`), not as entertainment
     property. The tool screens neither: `asset.kind_excluded` ("a building, land, a vehicle, an aircraft, a film or
     a recording", `asset.yaml:135-142`) does not name boats.
2. **Origin:** before tonight (identical on main).
3. **Failure mode:** listed property used 50% or less in business is depreciated by GDS instead of being refused
   (entry witness: $4,000 on Schedule C line 13).
4. **Fix:**
   - Prompt: restore the source terms: "...property of a kind used for entertainment or recreation (such as
     photographic, sound, communication or video recording equipment)...". Keep the computer sentence.
   - Boat (owner decision 6): the source-faithful home is `asset.kind_excluded`, with tick "A building, land, a
     vehicle or boat, an aircraft, a film or a recording" (12 words). That refuses every boat, including boats used
     more than 50% in business (an over-refusal, but safe). The alternative, the entry's "or a boat" in
     `asset.listed`, mixes p946's two categories.
5. **Fixtures:** none. Reviews due: the question review of `asset.listed` (the entry asks for it); the screen and
   false-no samples of gate `asset.listed`; if the kind tick changes, those of `asset.kind_excluded`.
6. **Effort:** 15 minutes.

---

## Lane split and order

All lanes are mechanical once the owner decisions are made. The source checks are done above. Sonnet can apply the
wording, but Opus is advised for BUG-0817(a), BUG-0850 and BUG-0861 (computed), which are structural.

| Order | Lane | Entries | Files claimed | Model / class | Effort |
|---|---|---|---|---|---|
| 1 | NY | 0850, 0851 | `forms/ny/2025/ny_it201.yaml`, `interview/ny/2025/questions.yaml`, NY fixtures | Opus / judgment (0850 structural) | 1.5 h |
| 2 | Credits and people | 0797, 0862, 0870, 0793, 0861 (wording), 0796 | `interview/2025/questions.yaml` (their entries), `forms/2025/{eic,dependent,f5695}.yaml` source fields | Sonnet / mechanical, with this plan's text | 2 h |
| 3 | Schedule A | 0817, 0803, 0805, 0815 | `forms/2025/sa.yaml`, `interview/2025/questions.yaml` (`sa.*`), `interview/2025/coverage/home.yaml` | Opus / judgment if 0817(a); else Sonnet | 1.5 h |
| 4 | Biz | 0790 | `interview/2025/questions.yaml` (`asset.*`), maybe `forms/2025/asset.yaml` | Sonnet / mechanical | 0.3 h |

**Why this order:**
- NY first: BUG-0850 is the only new-tonight defect, and the only one in this lane that misses a refusal for a value
  the tool computes. BUG-0851 is in the same file.
- Then 0797 and 0862, which both let a credit through without Form 8862, then 0870 (excise tax missed), then 0793 (an
  EIC overstatement).
- The Schedule A and Form 5695 changes are mostly taxpayer-unfavourable understatements, except BUG-0803.

**Conflicts:** lanes 2, 3 and 4 all edit `interview/2025/questions.yaml`, but in disjoint entries. Claim by form
(`tools/claims.py`) and merge in sequence.

**Reviews:** run them after each lane's fixes land, one review per form per round. Most changes touch help or prompt
only, so the due work is question reviews plus false-no samples, line-scoped. Estimate each batch with `--dry-run`
against the $3.00 gate.

## Owner decisions

1. **BUG-0803:** gifts to the Canadian, Israeli and Mexican charities the treaties allow. Leave them out of line 11
   (understates; simplest), or refuse them?
2. **BUG-0817:** (a) ask the earlier-year carryover of every filer as a tick in the existing screen. This changes
   coverage row `home.gifts_of_money` and the redraft's lane-7a design. Or (b) reword `sa.charity_limited`, which
   keeps two subjects in one question?
3. **BUG-0805:** archive Pub. 936 so the help can say that repairs and furniture are not "substantially improving",
   or change only the prompt word?
4. **BUG-0861:** wording, which states the 65-or-older and blind limits in help (married dependents stay approximate),
   or compute Chart B (ask blind and the two amounts)?
5. **BUG-0797:** does a spouse's earlier American opportunity credit denial need Form 8862 on a joint return?
   i8862 says nothing. Keep "you", or widen and register an ambiguity?
6. **BUG-0790:** put boats in `asset.kind_excluded` (refuses every boat; p946 calls boats transportation property),
   or in `asset.listed` as the entry proposes?
7. **BUG-0851:** name the New York plans (the Direct Plan and the Advisor-Guided Plan) in help? The second is not in
   the archived instructions.

## Open HIGH entries

- **BUG-0629, parts (1) and (2)** (federal 2026 cannot be adopted without New York; a carried vehicle's
  placed-in-service year stops fixtures_year and properties). The plan is to write the closure record: `Closes=BUG-0629`,
  `Closure=fixed`, `Evidence=T-295` (`TASKS-DONE.md:271`, done 2026-11-14: `years.json ny_adopted`,
  `dropNyConflicts`, `extend_year_enums`, and so on). Record that the end-to-end proof is T-317 (the real-adoption
  rehearsal). It is still listed open only because no closure exists (checked: `bug_status.py BUG-0629` says "Status:
  open ... done tasks T-295"). The `line79_over` conflict check is still in
  `interview/2025/conflict_checks.yaml:95`, which is expected, since the fix drops it at build. That T-295's
  self-tests cover part (1) is inferred from the TASKS-DONE row and was not run here (no builds tonight).
- No other open entry has a high severity (checked: `grep "Severity:** high"` in `BUG_INVENTORY.md` gives only line
  8003, which is BUG-0629).
