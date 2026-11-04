# Proposed bug entries (income package: T-124 to T-126, T-128 to T-131, T-141)

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1 — Alimony screen omits the part of payments that must continue after the recipient's death

- **Caught by:** T-124 (T-092 split; screens group4 PENDING-4-8).
- **Source:** p504 p. 15, Liability for payments after death of recipient spouse, "If any part of payments you make must
  continue to be made for any period after your spouse’s death, that part of your payments isn’t alimony" and "If you
  must make any payments in cash or property after your spouse’s death as a substitute for continuing otherwise
  qualifying payments before the death, the otherwise qualifying payments aren’t alimony".
- **Symptom:** `s1.alimony_unsupported` listed child support and payments for a home as non-alimony parts, but not a
  part that must continue after the recipient's death (or that a post-death payment substitutes for). A filer with such
  a part answered No and entered the whole payment, so Schedule 1 line 2a (or 19a) included an amount that isn't
  alimony. Source and question inspection; not reproduced on a return.
- **Fix:** the screen adds payments of which any part must continue, in cash or property, after the recipient spouse's
  death (even if the instrument does not say so, for example under state law), and payments for which a payment due
  after the death is a substitute. Wording of an existing screen whose Yes already refuses at `s1.alimony_refused` and
  `s1.paid_refused`; the refusal texts are unchanged.
- **Fix lines:** `s1.alimony_unsupported`
- **Siblings checked:** `s1.alimony_refused`, `s1.paid_refused`, `s1.alimony_received`, `s1.alimony_paid`,
  `s1.line2a`, `s1.line19a`, `s1.line19b_notice`.
- **Regression predictions:** no evaluated value changes; no fixture added (the new item is a new item of a screen whose
  Yes already refuses; stage16 alimony refusal fixtures cover the refusal).
- **Validation:** source inspection; fixtures 1,442 of 1,447 (the 5 failures are the T-131 class M cases, PENDING-5).
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed

## PENDING-2 — Unemployment screen's "employer-paid tax" carve-out could exclude a self-employed filer's own payments

- **Caught by:** T-125 (T-092 split; screens group4 PENDING-4-9, introduced by the BUG-0245 rewording).
- **Source:** i1040gi p. 89, Line 7, "If you made contributions to a governmental unemployment compensation program and
  you aren't itemizing deductions, reduce the amount you report on line 7 by those contributions."
- **Symptom:** `s1.uc_unsupported` said "not counting employer-paid tax"; a self-employed filer who paid for elective
  state coverage could read their own payment as employer-paid and answer No, so line 7 was computed unreduced instead
  of refused. Question inspection; not reproduced.
- **Fix:** the question counts "payments you made yourself, such as for coverage you elected as a self-employed person"
  and excludes only "tax an employer paid on your wages". Wording only; the refusal is unchanged.
- **Fix lines:** `s1.uc_unsupported`
- **Siblings checked:** `s1.line7_figured`, `s1.has_uc`, `s1.uc_paid`, `s1.uc_repaid`.
- **Regression predictions:** none (wording only).
- **Validation:** source inspection.
- **Tags:** wording; existing-form-pass; fixed

## PENDING-3 — Alimony questions name only one form of a post-2018 change that applies the new rules

- **Caught by:** T-126 (T-092 split; fixr3 s1 Low).
- **Source:** p504 p. 16, Certain Rules for Instruments Executed or Modified After 2018, "if the modification expressly
  states that the alimony isn’t deductible to the payer or includible in the income of the recipient", and Example 2, "the
  modification expressly provided that the post-2018 alimony rules apply"; i1040gi p. 89, Line 2a.
- **Symptom:** `s1.alimony`, `s1.alimony_received` and `s1.alimony_paid` described a change "that expressly provides that
  alimony received isn't included in income"; a change that only adopts the post-2018 rules, or only denies the payer's
  deduction, could be answered as not changed, and its later payments counted as income or deducted. Question inspection.
- **Fix:** the three questions name a change after 2018 that expressly applies the post-2018 rules: one stating that the
  post-2018 alimony rules apply, or that alimony isn't deductible by the payer or isn't included in the recipient's
  income. Locators add the p504 p. 16 quotations. Wording only.
- **Fix lines:** `s1.alimony`, `s1.alimony_received`, `s1.alimony_paid`
- **Siblings checked:** `s1.alimony_unsupported`, `s1.line2a`, `s1.line19a`, `amb.2025.alimony_screen` (its "chosen"
  text says "a change that expressly excludes them"; proposed wording follow-up for the register's owner, not edited).
- **Regression predictions:** none (wording only).
- **Validation:** source inspection; `citations.py --strict` 0 findings.
- **Tags:** wording; existing-form-pass; fixed

## PENDING-4 — Retirement screen over-refused survivors of retirees and full in-kind rollovers of property

- **Caught by:** T-128 and T-129 (T-092 split; fixr2 retirement F1 and F2).
- **Source:** i1040gi p. 30, Age (or Combined Ages) at Annuity Starting Date, "If you are the survivor of a retiree, use
  the retiree’s age on their annuity starting date" and "If you are the beneficiary of an employee who died, see Pub.
  575"; p. 30, Rollovers, "special rules that apply to ... partial rollovers of property"; p575 p. 34, Survivors of
  retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax
  free is the same as the tax-free amount figured by the retiree at the annuity starting date", and "If you receive
  guaranteed payments as the decedent’s beneficiary under a life annuity contract"; p575 p. 23, Rollovers of property, "you
  must either roll over the actual property distributed or sell it and roll over the proceeds" and "If you roll over only
  part of the proceeds, you are taxed on the part you keep"; p575 p. 12, Exclusion limited to cost.
- **Symptom:** `retirement.special` refused "an annuity you receive as the beneficiary of an employee who died", which a
  survivor under a retiree's joint and survivor annuity answers Yes, though i1040gi computes it on the worksheet with
  the retiree's age; and "a rollover of property other than cash", which refuses a rollover of all of the same property,
  computed by the ordinary line 5a/5b subtraction. Over-refusals; no wrong amount.
- **Fix:** `retirement.special` now refuses the beneficiary of an employee who died before retiring, guaranteed payments
  as a retiree's beneficiary under a life annuity contract, and an annuity shared among more than one beneficiary, and
  says a survivor annuity under a retiree's joint and survivor annuity is not one of these; and refuses a property
  rollover only when the property was sold and the proceeds rolled over, or only part of the property was rolled over.
  The worksheet questions tell a survivor of a retiree to answer for the retiree's annuity: `retirement.annuity`
  (starting date and the retiree's age), `retirement.cost` (the retiree's cost), `retirement.used_last_year` and
  `retirement.last_line4` (the retiree's worksheet), `retirement.joint_life` and `retirement.combined_age` (the retiree's
  and the survivor's lives and ages), `retirement.recovered` (including the retiree's recovery). No expression changed.
  Pub. 575 (2025) is archived as `sources/2025/p575` for these citations.
- **Fix lines:** `retirement.special`, `retirement.annuity`, `retirement.cost`, `retirement.used_last_year`,
  `retirement.last_line4`, `retirement.joint_life`, `retirement.combined_age`, `retirement.recovered`
- **Siblings checked:** `retirement.rolled`, `retirement.taxable`, `retirement.amount_a`, `retirement.age` (already
  stated the survivor's age rule), `retirement.annuity_rollover` (still refuses any rollover of a Simplified Method
  annuity), `retirement.rollover`, `retirement.smw4` to `smw11`, `retirement.plan_taxable`, `retirement.show_a`.
- **Regression predictions:** written from the sources before the evaluator ran; both matched.
  `stage10.smw.survivor_of_retiree`: retiree's annuity from January 1, 2018, joint lives at 65 and 65, cost $31,000, last
  year's line 4 $100, $8,400 recovered by the retiree; survivor receives $600 a month for 12 months (code 4). Lines 4
  $100, 5 $1,200, 10 $9,600, 11 $21,400; Form 1040 line 5a $7,200, line 5b $6,000.
  `stage10.plan.property_rollover_full`: $20,000 of nonemployer stock, code 7, all of it rolled over in kind. Line 5a
  $20,000, line 5b $0, line 5c box 1 checked, line 4c unchecked. An independent GPT-6 Astra reading of both predictions
  agreed (`research/audits/income/receipts/astra_t128_t129.*`).
- **Validation:** fixtures (both new cases pass); `citations.py --strict` 0 findings; consumer and limit verdicts proposed
  (`consumers_proposed.json`).
- **Tags:** over-refusal; wording; existing-form-pass; fixed

## PENDING-5 — `sales.wash_loss` accepted a code W amount larger than the loss

- **Caught by:** T-131 (T-092 split; fixr2 sales O1; class M classm.s3.2, where $449 was added to a gain). Owner's
  decision 2026-11-01: refuse as an entry error.
- **Source:** i8949 p. 10, code W, "You have a nondeductible loss from a wash sale" and "enter the amount of the
  nondeductible loss as a positive number in column (g)"; p550 p. 86, Wash Sales, "A wash sale occurs when you sell or
  trade stock or securities at a loss".
- **Symptom:** with code W, column (g) took the entered wash-sale loss whatever the loss on the sale, so an amount larger
  than the loss (or any amount on a gain) raised column (h) above zero, adding a gain. Not re-run on the old tree: by
  the arithmetic of `sales.h`, proceeds $1,000, basis $1,200 and wash $449 give column (h) +$249; the class M case
  classm.s3.2 recorded the gain form of it (a $449 wash amount on a sale at a gain).
- **Fix:** new helper `sales.wash_over` (columns (d) less (e), plus the code B correction, plus the entered wash-sale
  loss) and gate `sales.wash_bad` (code W, wash-sale loss above zero and `sales.wash_over` above zero), refusing at
  `sales.w` as an entry error; `sales.wash_loss` states the limit. The gate is placed in `tools/coverage/tree.json`
  (sales, entry). `engine/src/generate.ts` keeps a valid generated sale's wash-sale loss within the loss (invalid entries
  keep the raw amount, so the gate is exercised); this consumes no extra randomness.
- **Fix lines:** `sales.wash_loss`, `sales.wash_over`, `sales.wash_bad`, `sales.w`
- **Siblings checked:** `sales.has_w`, `sales.b`, `sales.e`, `sales.g`, `sales.h`, `sales.bad_code` (box C/F code B),
  `sales.bad_aggregate` (aggregate route has no codes), `tools/engines/generate_cases.py` (already draws wash within the
  loss), `engine/src/generate.ts`.
- **Regression predictions:** written before the evaluator ran; all three matched. `sales.refuse.wash_over_loss`
  (proceeds $1,000, basis $1,200, wash $449) refuses at `sales[a].w` and Form 1040 line 7a with gate
  `sales[a].wash_bad`; `sales.adjust.A.W.equal_loss` (wash $200 equal to the loss) gives column (g) $200, column (h) $0,
  line 7a $0; `sales.adjust.D.BW.wash_within_corrected_loss` (box D, BW, proceeds $6,000, reported basis $7,000, correct
  basis $8,000, wash $1,500) gives column (g) $500, column (h) -$500, line 7a -$500 (the B correction counts toward the
  loss).
- **Regressions introduced (open until the class M reruns):** five recorded class M cases carry generated wash-sale
  amounts larger than the loss and now refuse: `classm.s3.2`, `classm.s3.2.deepseek`, `classm.qdcg.3`, `classm.tcw.14`,
  `classm.sa.2`. They need class M reruns of s3 (Claude and DeepSeek), qdcg, tcw and sa, which rebuild jobs from the
  corrected generator; sales class M is stale anyway.
- **Validation:** fixtures 1,442/1,447 (the five above); refusal reach 0 exceptions; coverage tree 196 gates placed;
  integration 806 passed.
- **Tags:** amount-affecting; entry-error gate; existing-form-pass; fixed (class M reruns pending)

## PENDING-6 — `sales.special` did not name collectibles held through an entity

- **Caught by:** T-130 (T-092 split; screens group4 PENDING-4-10).
- **Source:** i1040sd p. 11, line 18, "Include on the worksheet any gain (but not loss) from the sale or exchange of an
  interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation
  of collectibles"; p. 12, line 19, "You reported a long-term capital gain from the sale or exchange of an interest in a
  partnership that owned section 1250 property".
- **Symptom:** "an interest in a partnership, S corporation or trust holding such property" could be read as section
  1250 property only, so stock of an S corporation holding appreciated collectibles was answered No and its 28% gain
  taxed at 15 or 20%. Question inspection.
- **Fix:** the question names "an interest in a partnership, S corporation or trust (including S corporation stock) that
  holds collectibles or section 1250 property, such as stock of an S corporation that owns art or gold worth more than its
  cost"; the locator adds the p. 12 quotation. Wording only.
- **Fix lines:** `sales.special`
- **Siblings checked:** `sales.one` (refuses on Yes), `sales.aggregate_eligible` ("no collectibles"), `g28` lines 1 and 4,
  `sd.other_forms` (K-1 capital gains already refused).
- **Regression predictions:** none (wording; `sales.refuse.special` covers the refusal).
- **Validation:** source inspection. The refusal remedy still says "Direct sales of collectibles, section 1202 stock and
  section 1250 property are unsupported"; left unchanged because stage3 fixtures quote it 35 times (low, for the next sales
  change).
- **Tags:** wording; existing-form-pass; fixed

## PENDING-7 — `sd.filed` cited doc f1040sd for an i1040gi quotation

- **Caught by:** T-141 (TASKS verification, from T-076 (4)).
- **Source:** i1040gi p. 31, Line 7a.
- **Symptom:** the citation named doc f1040sd with an "i1040gi p. 31" locator; the cited document was wrong.
- **Fix:** doc i1040gi, locator "p. 31, Line 7a, ..." with the same three quotations (checked on p. 31).
- **Fix lines:** `sd.filed`
- **Siblings checked:** none needed (citation only).
- **Regression predictions:** none.
- **Validation:** `citations.py --strict` 0 findings.
- **Tags:** citation; fixed
