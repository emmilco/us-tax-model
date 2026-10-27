# Render comparison — carloan

The rendered English of every printed line of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` (`rendered/2025/carloan.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9ae2d40babbec3ab571283fe79f05882015cf9bd7b1336ff3bef954abcadfebc |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 73e7d3c3b3e29a0d2ca71e5fd73193a615d328802d4ef4e7116a1213e923ae3b |
| lines judged | 2 |
| match / mismatch / unclear / missing | 1 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 23, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 23, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22, 23 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22, 23 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040sc | 2025 | 3, 6, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 3, 6, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i4562 | 2025 | 4 | pages named by another document's citation | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | - | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |

## Lines

### 22(ii) — QPVLI deducted elsewhere on your return (the qualifying part of the interest deducted on S
Status: **MISMATCH**

Restated: Choose — [helper "The loan and the vehicle qualify" = false → helper "Year parameter sales.zero"] [helper "The loan and the vehicle qualify" = true → helper "The QPVLI part of the Schedule C interest, by how you came to owe the loan"]

Model: The instructions say to enter 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)'. The restatement counts only interest deducted on Schedule C. It omits QPVLI deducted on Schedule E or Schedule F, and no refusal names that exclusion.

Ruling: scope; i1040gi p. 110, Schedule 1-A, Line 22: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)." The objection (Schedules E and F left out, no refusal named) is answered by a cited scope screen: scope.schedule1 asks about "rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F)" and refuses Form 1040 lines 8 and 10 when true (forms/2025/scope.yaml; f1040.line8, f1040.line10), so on every completed return Schedule C is the only place the interest can be deducted elsewhere; the form note says "Schedules E and F are refused". Same ruling as the archived rounds; the rendering is new (column (ii) is now the QPVLI part of the Schedule C interest, BUG-0175) and states that correctly ("The QPVLI part of the Schedule C interest, by how you came to owe the loan", fr-2025-24154 p. 23, proposed § 1.163-16(g)(1): "Independently deductible interest is limited to interest that is QPVLI ... and that is otherwise deductible by the taxpayer as a different type of interest"; (g)(2): the QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI"). Not a model error (the source does name E and F).

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **MATCH**

Model: The instructions say to enter 'the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)'. The restatement subtracts 22(ii) from QPVLI, which is gated on eligibility and allocated pro rata. That allocation follows Prop. Reg. 1.163-16(d)(2)(iii) and (d)(4), and the nested-refinance refusal names the excluded case. The value is still affected by the 22(ii) omission noted above.

## Raw response

```yaml
```yaml
lines:
  - key: "22(ii)"
    status: MISMATCH
    reason: "The instructions say to enter 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)'. The restatement counts only interest deducted on Schedule C. It omits QPVLI deducted on Schedule E or Schedule F, and no refusal names that exclusion."
  - key: "22(iii)"
    status: MATCH
    reason: "The instructions say to enter 'the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)'. The restatement subtracts 22(ii) from QPVLI, which is gated on eligibility and allocated pro rata. That allocation follows Prop. Reg. 1.163-16(d)(2)(iii) and (d)(4), and the nested-refinance refusal names the excluded case. The value is still affected by the 22(ii) omission noted above."
```
```
