# Engineering responses to optional human review — 2026-10-24

The original verdicts in `human/*.md` are the owner's records. This file is an agent's investigation,
not a revised verdict, human approval or H/B evidence. All fourteen answers were saved before the
owner retired the remaining mandatory packets. No new owner sitting is required.

| Finding | Engineering assessment | Status / next action |
| --- | --- | --- |
| sa.extra: the dollar increments do not appear explicitly on the shown page | Correct presentation criticism. i1040gi p.35 gives total deductions; the increments follow by comparing its rows with the base amounts. | Updated: both base and chart excerpts are provided, with instructions to compare successive rows or subtract the base. The amount is labeled dollars per box. |
| sa.extra_age65: wording appears to multiply age and blindness counts | The expression multiplies sa.extra (money per box) by sa.boxes_age65 (count), not by the blindness count. | Updated: reference and question explicitly distinguish dollars per box, age count and resulting dollars. |
| sa.extra_blind: wording appears to multiply the two counts | The expression independently multiplies the same money increment by the blindness count. | Updated: the separate dollar addition and its count are named explicitly. |
| sa.standardraw: explanation confusing relative to the page | The expression adds base + age addition + blindness addition, algebraically base + increment × (age boxes + blindness boxes). | Updated: the question explains the equivalence to the IRS's combined box count. |

No tax-value error is established by these four observations. The source-backed reasoning and first
secondary corroboration are in `research/secondary/2025-standard-deduction.md`. BUG-0128 records
the implemented presentation changes. All 16 isolated review-path tests pass and item2 regenerates.
This is an engineering correction, not a new owner MATCH or H credit. Confirmed arithmetic defects,
if found during investigation, still require an inventory entry, correction and independent checks.
