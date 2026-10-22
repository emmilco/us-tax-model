# Handoff: Stage 16 (the remaining Schedule 1 items), built and reviewed; owner questions open

Read `HANDOFF.md` first, then `TASKS.md` (T-053), then this file. The owner's decisions are D1 to D14 in
`research/premises/stage16-schedule1-misc.decisions.md`, with the premise map and its verification beside it.

## Scope

- **Taxable state or local refund:** Schedule 1 line 1, from the Form 1040 instructions' State and Local Income Tax
  Refund Worksheet (`forms/2025/refund.yaml`). A refund is not taxable when the filer did not itemize in 2024 or
  deducted sales tax. The nine Pub. 525 exceptions, refunds of other taxes and other recoveries are refused.
- **Other income:**
  - Schedule 1 lines 8b (gambling, with losses on Schedule A line 16 capped at the winnings), 8c (fully taxable
    canceled nonbusiness debt), 8f (taxable HSA distributions, Form 8889 Part II, with the 20% tax on Schedule 2
    line 17c), 8g, 8h (with line 24a when given to the employer), 8i, 8j and 8r.
  - Line 8z as a collection of entries keyed by kind (`forms/2025/oi8z.yaml`). RTAA payments and kickbacks are
    computed; every other kind is refused.
- **The IRA deduction** (Schedule 1 line 20; `forms/2025/ira.yaml` with per-person columns in `person.yaml`), with
  Form 8606 Part I for nondeductible contributions when there is no distribution (`forms/2025/f8606.yaml`).
  - Form 8880 now counts traditional contributions, with one excess-contribution screen for traditional and Roth.
  - The social security worksheet has its own copy of the deduction's terms, which breaks the line cycle (D7).
- **Adjustments:** the early withdrawal penalty (line 18, per interest payer) and alimony under pre-2019 agreements
  (lines 2a and 19a).
- **Still refused:** Form 4797, the net operating loss deduction and the foreign earned income exclusion.
  - `scope.schedule1` now asks only about Schedule 1 items "other than the ones this tool asks about separately".
  - The question still covers rental of personal property and line 8s, which the EIC and Schedule 8812 riders read.

## How the stage was built

- **Authoring:** four agents, each in its own worktree from 4026daf: refund, other income and gambling, the IRA
  deduction, and the small items. Each used placeholders for the other areas' lines. This session then:
  - merged the four, resolving the shared sums (lines 9, 10 and 26) by hand;
  - repointed the placeholders;
  - narrowed `scope.schedule1` once for all four areas;
  - backfilled the existing fixtures with the answers that leave them unchanged.
- **Approved fixes merged with the stage:**
  - BUG-0079 (owner-approved): a refusal now outranks an unknown in atom and comparison operands. The new
    property `refusal_outranks_unknown` checks it.
  - T-052: the generator zeroes amounts behind a screen answered No. The new property `screens_respected` checks
    it.
  - The Stage 15 follow-ups the owner accepted (the Form 2441 employer-provided care screen, the Form 8880 labels,
    the premium tax credit in `scope.credits`, `amb.2025.dc_born_died_half_year`).
- **Fixtures (`fixtures/2025/stage16.json`):** blind predictions, as in Stage 15. The scenarios were written as
  facts; two agents per area, without seeing the encoding, worked each return from the archived text. Where the two
  differed, this session settled it by reading the text. Lines after a printed STOP are not asserted. One
  regression case was added for BUG-0084.
- **Reviews:**
  - Transcription, render and class M for the new documents (`refund`, `ira`, `f8606`, `oi8z`).
  - Reruns for every form whose subject changed.
  - Every disagreement ruled with its source quote. Agents drafted the rulings per group; this session checked them
    before applying.
  - The generator now sometimes draws a line 8z entry (about one return in twelve), so `oi8z` has class M jobs.

## Findings

- **BUG-0084 (fixed):** the standard deduction counted the age box of a person who died in 2025 before reaching 65.
  On a joint return whose spouse had no SSN valid for employment, nothing refused the return, and line 12e was
  $1,600 too high.
- **BUG-0085 (fixed):** the HSA medical expense question (Form 8889 line 15) left out people who would be
  dependents, and the divorced-parents rule.
- **BUG-0086 (fixed):** the IRA basis question omitted the Form 8606 line 2 adjustments. A new screen
  (`person.ira_basis_adjusted`) refuses line 2 in those cases.
- **BUG-0087 (fixed):** the HSA screen did not refuse an HSA whose owner died in 2025 with the estate as
  beneficiary. That value is excepted from the 20% tax, so such a return could be charged it.
- **Register:** `amb.2025.hsa_last_month_all_year`, proposed: whether a filer eligible all twelve months can use the
  last-month rule's coverage treatment (question 22 below).
- **Tasks:**
  - T-054: a person whose only HSA item is a qualified HSA funding distribution is never asked the Form 8889
    screen.
  - T-055: the render review does not read the English of the per-person IRA helpers.

## Coverage

`tools/coverage/estimate.py` gives 68.6% of returns, up from 64.7%.
- Retired (`refused: false`): `state_refund`, `ira_deduction`, `gambling`, `early_withdrawal`, `alimony_paid`,
  `alimony_received`, `hsa_distribution` and `cancellation_of_debt`.
- `other_income` stays refused (D11), because the estimate cannot tell which part of it is now computed. The figure
  therefore understates coverage.
- Spec 2.4's remaining list is reordered from the estimator. Schedule E comes next (74%), then the rest of Schedule
  1 (79%), then the premium tax credit (84%, the first goal). Married filing separately is still the step that
  reaches the 95% target.

## Evidence

Measured on the tree committed with this file:
- **Review logs:** current, with no open ruling. Transcription and render cover 55 forms, class M 48; 987 rulings.
- **Fixtures:** 1,027/1,027 pass. `stage16.json` has 82 cases:
  - 40 blind-predicted returns, one per scenario of the four areas;
  - 30 refusal regressions (`stage16.refuse.*`), one for each refusal no fixture had reached;
  - 11 blind-predicted mutation scenarios (`stage16.mut.*`), where two agents agreed with each other and with the
    evaluator on every asserted value;
  - the BUG-0084 regression.
- **Other checks:** integration 770 invocations; properties 8 over 400 returns, 0 failing, 1,937 of 2,185 branches
  reached; Lean compare 1,627 cases, 0 differing; engine differential 1,700 cases, 0 unexplained; citations 2,396 segments, 0 findings.
- **Mutation:** 2,267 mutants; adjusted score 98.1% (Stage 15 closed at 97.9%).
  - The first run left 49 new Stage 16 survivors: 33 refusal mutants (every Stage 16 fixture answered the gate
    questions No) and 16 operand, parameter, boundary and filter mutants.
  - The refusal regressions and the mutation scenarios kill all 49; none was equivalent. One older survivor is now
    killed too, leaving 40 unexplained, all from earlier stages.
  - The two refund mutation scenarios (`refund_single_unasked`, `refund_line3_stop`) leave out the answers the
    interview does not ask on their path. Answering every question would hide three refund mutants
    (`boundary.refund.refund.line3_more`, `operand.refund.refund.line6.amt_spouse_blind`,
    `operand.refund.refund.line9_figured.line8`). Those mutants differ only by needing an answer the interview never
    asks.

## Open for the owner

Each item gives a recommendation first and the alternative after it. Items 1 to 4 are about other income, 5 to 9 the
refund, 10 to 14 the small items, 15 to 19 the IRA deduction, and 20 to 25 cut across areas.

**Other income**

1. **Insurance policy dividends on line 8z** (the part above the net premiums paid). *Recommended:* keep the refusal.
   - Such dividends may also be net investment income on Form 8960 line 7, which cannot be tested from an 8z entry.
   - *Alternative:* compute them as an 8z kind and accept the Form 8960 gap.
2. **Jury duty pay given to the employer (line 24a) larger than the pay on line 8h.** *Recommended:* refuse it as an
   entry error (`amb.2025.jury_24a_cap`). *Alternative:* cap line 24a at line 8h silently.
3. **The professional-gambler question.** It is asked only of a filer with gambling winnings. *Recommended:* accept.
   - A professional with no 2025 winnings has nothing on line 8b or Schedule A line 16.
   - Their business would come in through the Schedule C questions.
   - *Alternative:* ask every filer.
4. **Manufacturer incentive payments to a salesperson** (Pub. 525 p. 34). Today they fall under "other", which is
   refused. *Recommended:* leave them refused; the case is small, and a kind can be added later without changing
   structure. *Alternative:* add them as a computed 8z kind now.

**Taxable refund**

5. **The "other recoveries" question (`refund.other`)** is asked of every return. *Recommended:* fold it into the
   narrowed Schedule 1 screen, which saves every filer a question. *Alternative:* keep it as its own question.
6. **When the Pub. 525 exceptions are asked.**
   - Exceptions 1 and 5, and Form 1099-G box 8, are asked for every refund.
   - Exceptions 3, 4 and 6 to 9, and nonresident status, are asked only on the worksheet path.
   - *Recommended:* accept, because off the worksheet path they cannot change the result. *Alternative:* ask all
     of them up front.
7. **The 2024 spouse boxes** are asked only when 2024 was married filing jointly or separately. Blindness is asked
   as of the end of 2024. *Recommended:* accept (`amb.2025.refund_boxes_2024`). *Alternative:* also ask for a
   qualifying surviving spouse.
8. **Worksheet line 6 is a sum of amounts per box rather than a count times an amount.** The values are equal.
   *Recommended:* accept. *Alternative:* restructure it as a count.
9. **A check that the 2024 Schedule A line 5e is not above line 5d.** *Recommended:* add one, refusing such an
   entry as an error, like `w2.g_bad`. *Alternative:* no check.

**Small items**

10. **Canceled student loans.** They are refused along with the other canceled-debt exceptions; the map proposed
    computing them as not income. *Recommended:* keep the refusal for now, since the exclusion has conditions of its
    own. *Alternative:* compute them as excluded.
11. **HSA withdrawals of excess contributions, and mistaken distributions that were repaid.** Both are refused,
    though D2 did not name them. *Recommended:* keep both refusals. *Alternative:* compute them (Form 8889 line
    14b, and the mistaken-distribution rules).
12. **Alimony that is partly child support.** It is refused, including Pub. 504's underpayment example.
    *Recommended:* keep the refusal. *Alternative:* ask for the alimony part after the rule that child support is
    paid first.
13. **Interview length.** Every filer answers an alimony yes/no question and a canceled-debt amount. Each interest
    payer adds a penalty question, and each Form 8889 adds a distributions question. *Recommended:* give canceled
    debt its own yes/no gate, so most filers answer one yes/no instead of an amount. *Alternative:* keep it as built.
14. **The Form 8889 Part III testing-period failure** was added to the HSA roster question. *Recommended:* keep it.
    *Alternative:* ask it on its own.

**IRA deduction**

15. **Pub. 590-A Example 1** prints $6,825 (and Form 8606 line 1 $175) without the worksheet's "increase to the
    next multiple of $10". The encoding gives $6,830 and $170, following the printed rule in i1040gi p. 98 line 7
    and Pub. 590-A Worksheet 1-2. *Recommended:* the fixtures use the rule ($6,830). *Alternative:* follow the
    example.
16. **Self-employment compensation (worksheet line 9)** is the Schedule C net profit, assuming the income comes
    from personal services. *Recommended:* add a screen, asked of a Schedule C filer who makes traditional
    contributions, that refuses income mainly from capital. *Alternative:* keep the assumption and say it in the
    help text.
17. **Two refusals not in the decisions:** contributions above the age limit (`ira.over_limit`) and contributions
    above compensation (`ira.over_comp`). Both are excess contributions, which go to Form 5329 (refused).
    *Recommended:* keep both. *Alternative:* compute the deduction on the allowed part.
18. **The exclusions refused on the IRA path.** Form 2555, Form 4563 and Puerto Rico income, together with plan
    coverage, are refused. i1040gi p. 96 names Forms 2555 and 8815 and adoption benefits. *Recommended:* keep the
    broader refusal. *Alternative:* narrow it to the printed list.
19. **The social security copy of line 20** can show a value different from line 20 on a worksheet that is not used
    (no benefits). It is display only. *Recommended:* accept. *Alternative:* show it only when benefits are present.

**Shared**

20. **BUG-0083: a line's own list of refusal gates stops at the first unknown gate.** Applying the
    refusal-outranks-unknown rule there makes the interview ask one or two more questions before refusing.
    *Recommended:* leave it as is, since no return comes out wrong and the refusal arrives later. *Alternative:*
    apply the rule.
21. **T-052 extended by the same rule.** Besides the Stage 15 screens, the generator also zeroes the amounts behind a
    retirement annuity and a leased vehicle answered No. *Recommended:* accept. *Alternative:* restrict it to the
    Stage 15 screens.
22. **`amb.2025.hsa_last_month_all_year`.** Can a filer eligible all twelve months use the last-month rule's coverage
    treatment for the line 6 spouse rules and line 7? The readings differ only for a joint return with a change of
    coverage type and a Yes to the last-month question.
    - On Pub. 969 Example 2's facts, line 6 is $4,275.00 under the first reading and $4,295.83 under the second.
    - *Recommended:* reading 1 (the project), since i8889's rule 2 is unqualified and Pub. 969 Example 2 treats this
      filer as using the rule. *Alternative:* reading 2, which follows Pub. 969 p. 5's "if you didn't otherwise
      have coverage".
23. **BUG-0087: the HSA of a person who died with the estate as beneficiary.** *Recommended:* the refusal now in
    `f8889.unsupported`. *Alternative:* add death to the line 17a exception question and compute it.
24. **BUG-0086: the IRA basis adjustments.** *Recommended:* the new screen that refuses Form 8606 line 2, already
    built. *Alternative:* no screen, and a reworded question asking for the line 2 amount with the chart and the
    three adjustments named, since the filer brings the number.

25. **The December 1 coverage answer is not checked against the month counts (T-056).** "None" means not eligible
    on December 1. Four answer sets are therefore contradictory:
    - self-only on December 1 with every eligible month a family month;
    - family on December 1 with no family month;
    - any coverage on December 1 with no eligible month;
    - none on December 1 with 12 eligible months.
    Under the last-month rule, such a set gives a wrong line 3. *Recommended:* refuse them as entry errors, like
    `f8889.bad_months`, at the start of the next stage. *Alternative:* leave them as the filer's responsibility.

## Facts a fresh session needs

- **Line order:**
  - The IRA worksheet reads Form 1040 line 9. The social security worksheet reads its own copy of the IRA terms
    (`person.ira_ssb_*`), not Schedule 1 line 20.
  - Line 25 (jury duty pay given to the employer) enters IRA worksheet line 4, the student loan interest worksheet
    line 3 and the social security worksheet line 6.
- **Generator inputs held at their defaults:**
  - The `NOT_DRAWN` and `UNDRAWN` sets in `engine/src/generate.ts` hold Stage 16's root inputs at no or zero, which
    keeps earlier generated returns unchanged.
  - Line 8z entries are drawn at the end of the spec record.
- **Class M jobs:** `.classm/jobs.json` holds every document's jobs. `classm-jobs --docs X` rewrites the file with
  only X's jobs, and `rule.py` reads the file when it drops a line. Merge new jobs into it rather than replacing it.
