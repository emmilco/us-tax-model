# Stage 2 review packet

Status: owner approved proceeding after Stage 2; detailed reviewer annotations and independent hand-work were not supplied. See reviews/2025/stage2.md.

## Source transcription

Read rendered/2025/w2.md, rendered/2025/person.md, rendered/2025/s3.md and the added Form 1040 line 31 against the archived sources below. Helper labels are authored explanations, not verbatim IRS lines.

- i1040gi.pdf, printed p. 117, Schedule 3 line 11.
- iw2w3.pdf, printed p. 18, boxes 3, 4 and 7; pp. 12–13 for the railroad exclusion.
- fw2.pdf, employee and employer identity and boxes 3, 4 and 7.
- f1040s3.pdf, lines 9–15; f1040.pdf, line 31.

Record reviewer, date, snapshot hashes and corrections in reviews/2025/stage2.md (preserved, not generated). Owner response is recorded in that file.

## Candidate fixture answers — not class B

Use integer cents below. Work each case independently on the archived instructions before comparing the candidate answer. Synthetic boundary inputs can deliberately contain unusual withholding; they test the encoded instructions, not payroll plausibility.

| Case | Status | Per-employer (box 3; box 7; box 4), cents | Candidate line 11 |
| --- | --- | --- | --- |
| ss.multi | single | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 10000000; 0; 620000 | 148180 |
| ss.base.below | single | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 7609999; 0; 471820 | 0 |
| ss.base.exact | single | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 7610000; 0; 471821 | 0 |
| ss.base.above | single | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 7610001; 0; 471821 | 1 |
| ss.withheld.below | single | person[taxpayer].w2[a]: 10000000; 0; 600000 / person[taxpayer].w2[b]: 10000000; 0; 491819 | 0 |
| ss.withheld.exact | single | person[taxpayer].w2[a]: 10000000; 0; 600000 / person[taxpayer].w2[b]: 10000000; 0; 491820 | 0 |
| ss.withheld.above | single | person[taxpayer].w2[a]: 10000000; 0; 600000 / person[taxpayer].w2[b]: 10000000; 0; 491821 | 1 |
| ss.single.exact | single | person[taxpayer].w2[a]: 17610000; 0; 1091820 | 0 |
| ss.single.below | single | person[taxpayer].w2[a]: 17609999; 0; 1091819 | 0 |
| ss.single.over | single | person[taxpayer].w2[a]: 17610000; 0; 1091821 | refusal: Form 843 |
| ss.multi.over | single | person[taxpayer].w2[a]: 17610000; 0; 1091821 / person[taxpayer].w2[b]: 5000000; 0; 310000 | refusal: Form 843 |
| ss.tips | single | person[taxpayer].w2[a]: 9000000; 1000000; 620000 / person[taxpayer].w2[b]: 7610001; 0; 471821 | 1 |
| ss.none | single | none | 0 |
| ss.mfj | mfj | none | 0 |
| ss.mfs | mfs | none | refusal: Married filing separately |
| ss.rrta | single | none | refusal: Schedule 3 line 11 (RRTA path) |
| ss.hoh | hoh | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 10000000; 0; 620000 | 148180 |
| ss.qss | qss | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 10000000; 0; 620000 | 148180 |
| ss.other.components | single | person[taxpayer].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[b]: 10000000; 0; 620000 | 148180 |
| ss.person.separation | single | person[second].w2[a]: 10000000; 0; 620000 / person[taxpayer].w2[a]: 10000000; 0; 620000 | 0 |
| ss.early.refusal | single | person[taxpayer].w2[a]: unknown; 0; 1091821 / person[taxpayer].w2[b]: 5000000; 0; 0 | refusal: Form 843 |

RRTA case has the railroad answer true. Other Schedule 3 components are zero except ss.other.components: lines 9, 10, 12 and 14 are 123, 500, 7 and 20 cents; line 15 and Form 1040 line 31 should be 148830 cents.

ss.person.separation is a generic engine test with two people, one employer each. It is not an enabled interview path.

The additional qdcg.table.minimum.regression covers the previously unobserved final minimum: taxable income $50,010, qualified dividends $1, Single; both ordinary and full income use the $50,000–$50,050 Tax Table cell ($5,920). The candidate preferred calculation is $5,920.15, so the ordinary tax wins. This is also pending human review.

## Remaining limits

- This is a slice, not a complete return. Non-Social-Security Schedule 3 components are explicitly supplied subtotals; their underlying forms are not prepared.
- One person is reachable through the interview. Married filing statuses and RRTA are refused.
- Whole-dollar return-wide rounding remains deferred; the slice operates in cents.
- Build-time interview checks enumerate finite enum/Boolean answers over fixture amounts and roster sizes. They are not a proof for unbounded collections.
- Lean proves the added aggregation non-negativity and fixed-filter monotonicity. Evaluator agreement is testing, not a proof of the TypeScript evaluator or of the IRS transcription.
- Stage 1 human review remains outstanding. Stage 3 has not started.
