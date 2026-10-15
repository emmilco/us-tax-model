# Stage 4 review packet

Stage 4 implements additional form slices and their CLI interview. AGI and taxable income remain supplied subtotals; Stage 5 must connect a complete Form 1040. These sample values sheets are synthetic worksheet exercises, not complete returns.

## Review against archived sources

Compare rendered/2025/sa.md with f1040sa and i1040sca p. 7 (SALT); f4952.md with f4952; gift.md with i8283 pp. 1–3. Check standard deduction amounts and exceptions against i1040gi pp. 34–35. Compare sb.md with f1040sb and i1040sb.

Compare sdtw.md with i1040sd pp. 15–16, g28.md and u1250.md with pp. 11–14. The special-rates fixture asserts all 47 worksheet lines; independently hand-work those expectations, including the printed skip instructions.

Compare f8959.md and f8960.md with their forms and instructions (NIIT deductions pp. 17–18 and MAGI p. 22). Compare qbi.md, f8995.md and f8995a.md with their forms, i8995-correction and i8995a. Compare ftc.md with i1116 pp. 1–2 and s2.md with f1040s2.

## Concrete checks

The combined-deductions case gives $2,500 medical + $9,000 taxes + $11,000 interest + $5,200 charity = $27,700 itemized deductions. The additional-taxes case gives $450 Additional Medicare Tax + $646 NIIT = $1,096 Schedule 2 line 21; additional withholding is separately $450. Check each amount and its source assumptions.

- [stage4.sdtw.special_rates](stage4.sdtw.special_rates.txt)
- [stage4.deductions.combined](stage4.deductions.combined.txt)
- [stage4.additional_taxes.combined](stage4.additional_taxes.combined.txt)
- [stage4.refuse.div.section1202](stage4.refuse.div.section1202.txt)
- [stage4.refuse.ftc.limit](stage4.refuse.ftc.limit.txt)

## Limits and evidence

1099-DIV box 2c remains a cited refusal because its inclusion conflicts with the code Q/Form 6251 exclusions. See amb.2025.box2c_scope; no owner decision to expand scope is recorded. Boxes 2b/2d feed the special-gain worksheets. Direct special-property sales remain refused.

Eligibility screens rely on explicit answers. Charity valuation, basis reductions and income-limit checks, mortgage eligibility, NIIT allocation, REIT-dividend eligibility and simple FTC eligibility are supplied determinations. Form 8283 support groups amounts and routes Section A/B; dates, descriptions and donee records are not prepared. Per-spouse interviews remain refused. Exact-cent calculations continue; return-wide whole-dollar rounding is deferred.

Official evidence added: i8959 p. 2 example 5 supplies $75,000 wages subject to additional tax; its married inputs are arithmetic scaffolding, not support for a married interview. Other i8959 examples require self-employment/RRTA, which are screened out. i8283 p. 2 supplies the $5,400 grouped-books Section B example. The i8960 rental allocation example is outside scope and is not claimed computed. Synthetic expectations remain regressions, not independently human-verified class B.

All spec 2.2 refusal categories have cited screens and fixtures: FTC (ftc), other QBI (qbi), carryover/digital/unsupported adjustments/direct special-property sales (sd/sales), AMT (s2/div), Schedule 1/1-A and other credits (scope), excluded itemized deductions (sa/gift/f4952), special interest treatment and foreign reporting (sb), married per-spouse treatment (s3/scope). Screening is a target of the Stage 4 interview; individual form evaluations are not a whole-return acceptance decision.

See coverage.md, mutation.md and evaluator_agreement.md for current counts and remaining gaps. Mutation survivors are published, including unresolved ones; coverage does not certify tax correctness. Interview fixture-path checks are representative, not exhaustive. Record source-review and hand-work observations in reviews/2025/stage4.md.
