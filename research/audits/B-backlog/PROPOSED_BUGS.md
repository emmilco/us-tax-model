# Proposed bug entries (T-169, Schedule A)

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1 — BUG-0302 is partly fixed: the Schedule A medical and tax questions carry the definition rules

- **Caught by:** BUG-0302, recorded open; this entry closes its line 1, 5a and 5b parts because the inventory is append-only. The line 12 and blindness parts stay open (PENDING-2, PENDING-3).
- **Source:** i1040sca p. 1, "If you received a distribution from a health savings account or a medical savings account in 2025, see Pub. 969 to figure your deduction", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation", "If you are a retired public safety officer, you can't include any premiums you paid to the extent they were paid for with a tax-free distribution from your retirement plan", "If you paid someone to do both nursing and housework, you can deduct only the cost of the nursing help", "Lodging expenses (but not meals) while away from home to receive medical care", "Certain medical expenses paid out of a deceased taxpayer's estate can be claimed on the deceased taxpayer's final return"; p. 2, the long-term care premium limit chart and "Don't deduct more than $50 a night for each person"; p969 pp. 9 and 13, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your HSA" (Archer MSA); i1040sca p. 3, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c. However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025".
- **Symptom:** as recorded in BUG-0302 for `sa.line1`, `sa.line5a` and `sa.line5b`. The completeness claim named only line 5a for territory taxes; the source sentence on p. 3 names lines 5a, 5b and 5c.
- **Fix:** wording only. `sa.line1` lists the exclusions (amounts equal to tax-free HSA or Archer MSA distributions, pretax premiums, a retired public safety officer's premiums paid with a tax-free plan distribution, the housework part of mixed pay, meals away from home other than hospital care, lodging over $50 a night per person), the long-term care premium limit by age with the chart amounts, and the estate-paid expenses on a final return by reference to Pub. 502. `sa.line5a`, `sa.line5b` and `sa.line5c` include U.S. territory taxes except those allocable to excluded income; `sa.line5a` also excepts territory income taxes taken as a credit; `sa.line5b` states the paid-in-2025-and-assessed-before-2026 rule. Each input now cites i1040sca (and p969 for line 1) instead of the generic Schedule A locator. No expression, gate or refusal changed.
- **Fix lines:** `sa.line1`, `sa.line5a`, `sa.line5b`, `sa.line5c`
- **Siblings checked:** `sa.line4`, `sa.line5d`, `sa.line5e`, `sa.excluded_income` (refuses excluded income, so the excluded-income exception needs no gate), `sa.unsupported` (foreign tax deduction), `ftc.taxes`, `ltc.limit` (Form 7206 uses the same age chart; not reused because Schedule A asks for one amount for all persons).
- **Regression predictions:** no evaluated value changes; every fixture result is unchanged and no fixture is added because no behavior changed. The interview text and the rendered sa page change.
- **Validation:** source inspection; the integrator reruns the sa transcription, render and completeness reviews.
- **Tags:** source-definition-debt; wording; schedule-a; fixed

## PENDING-2 — Line 12 noncash gifts: the good-used-condition rule under $500 and the $250 acknowledgment are not asked (open; the question is in `gift`)

- **Caught by:** the T-169 premise check of BUG-0302, line 12 part.
- **Source:** i1040sca p. 11, "A deduction for these contributions will be allowed only if the items are in good used condition or better. However, this rule doesn't apply to a contribution of any single item for which a deduction of more than $500 is claimed and for which you include a qualified appraisal and Form 8283 with your tax return"; "If the gift of property is $250 or more, you must also have a contemporaneous written acknowledgment from the charity."
- **Symptom:** `sa.line12` has no question of its own; it sums `gift.allowed`, which copies `gift.deduction`. `gift.special` already refuses "a clothing or household item over $500 not in good used condition", so the appraisal exception that BUG-0302 names is refused, not missed. What remains: a clothing or household item of $500 or less not in good used condition is not deductible, and `gift.deduction` does not say so; nothing asks for the contemporaneous written acknowledgment for a gift of property of $250 or more.
- **Disposition:** needs a change to `gift.deduction` (form `gift`), outside this pass's FORMS. Owner question in REPORT.md.
- **Validation:** source and implementation inspection.
- **Tags:** source-definition-debt; schedule-a; charity; explicitly-deferred

## PENDING-3 — The blindness question does not state the partial-blindness definition or the certified statement (open; the question is in `person`)

- **Caught by:** the T-169 premise check of BUG-0302, blindness part.
- **Source:** i1040gi p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that: • You can't see better than 20/200 in your better eye with glasses or contact lenses, or • Your field of vision is 20 degrees or less."
- **Symptom:** `sa.boxes_blind` counts `person.blind`, whose question is "Are you blind under the standard-deduction instructions?" in `person.yaml`, with the generic Schedule A locator. A partially blind filer may answer no.
- **Disposition:** needs a change to `person.blind` (form `person`), outside this pass's FORMS. Owner question in REPORT.md.
- **Validation:** source and implementation inspection.
- **Tags:** source-definition-debt; standard-deduction; explicitly-deferred

## PENDING-4 — Line 1 does not reduce premiums by the self-employed health insurance deduction or follow Form 8962 (open; outside T-169)

- **Caught by:** the T-169 rewording of `sa.line1`, reading the Line 1 section.
- **Source:** i1040sca p. 2, Line 1, "If advance payments of the premium tax credit were made or you think you may be eligible to claim a premium tax credit, fill out Form 8962 before filling out Schedule A, line 1"; "if you claimed the self-employed health insurance deduction on Schedule 1 (Form 1040), line 17, reduce the premiums by the amount on line 17"; p. 1, "Reduce the insurance premiums by any self-employed health insurance deduction you claimed on Schedule 1 (Form 1040), line 17."
- **Symptom:** the project computes `s1.line17` and Form 8962, but `sa.line1` asks for one supplied amount and does not tell the filer to subtract the premiums deducted on Schedule 1 line 17 or the premiums covered by the premium tax credit. A self-employed filer who itemizes can count the same premiums twice. Not reproduced by evaluation.
- **Disposition:** not in T-169's row; record as a new row. A wording fix (state both reductions in the question) or a computed split (premiums as a separate input less `s1.line17`) is a scope choice for the owner.
- **Validation:** source inspection only.
- **Tags:** source-definition-debt; schedule-a; cross-form; explicitly-deferred
