# Render comparison — carloan

The rendered English of every printed line of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` (`rendered/2025/carloan.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 79b104da5c00f6aeef81ad630495db72307a321528bdc4b62351f11fdd4f6efa |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 70c149067b18fb4d619b448b4c58c6da4c65e15bc1b1fa5b426a1ff22eb7b2d0 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040sc | 2025 | 3, 6, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 3, 6, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i4562 | 2025 | 4 | pages named by another document's citation | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | - | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |

## Lines

### 22(ii) — Interest on this loan deducted on Schedule C
Status: **MISMATCH**

Restated: Input — The part of this loan's 2025 interest you deduct on Schedule C (the business use of the vehicle; zero if none)

Model: The IRS text says to enter 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F),' but the restatement limits the input to interest deducted on Schedule C only.

Ruling: scope; i1040gi p. 110, Schedule 1-A, Line 22: "On line 22, column (ii), enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)." The objection (Schedule E and F left out, no refusal) is answered by a cited scope screen: scope.schedule1 asks about "rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F)" and refuses Form 1040 lines 8 and 10 when true (forms/2025/f1040.yaml f1040.line8, f1040.line10; f1040 Form 1040 (2025), lines 8, 10), so on every completed return Schedule C is the only place the interest can be deducted elsewhere; the form note says "Schedules E and F are refused". Prior rulings (archived 2026-10-27) reached the same result; checked against the current rendering, which is unchanged on this point. Not a model error (the source does name E and F). Separate issue not raised by the model: the question asks for the whole Schedule C part of the loan's interest, not its QPVLI part; on a partly qualifying loan this over-subtracts (see findings.md F1, fr-2025-24154 p. 23, proposed 1.163-16(g)(1)-(2)).

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **MISMATCH**

Restated: Subtract helper "Interest deducted on Schedule C (zero without a Schedule C)" from helper "Interest for this loan, Schedule 1-A". If zero or less, enter -0-.

Model: The IRS text says to enter 'the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii),' but the restatement subtracts only a Schedule C helper that is zero without a Schedule C, omitting deductions elsewhere such as Schedule E or Schedule F.

Ruling: scope; i1040gi p. 110, Schedule 1-A, Line 22: "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)", with p. 110: "if you deducted some or all of the interest ... on Schedule C, Schedule E, or Schedule F, then you can't deduct that same interest as QPVLI". Schedules E and F are refused by scope.schedule1 at Form 1040 lines 8 and 10 (the screen names Schedule E/K-1, rental of personal property and Schedule F), so no QPVLI is deducted on E or F on a completed return and the double deduction the model describes cannot occur; the Schedule C part is subtracted once (carloan.interest asks for the total including the Schedule C part, the BUG-0058 fix). Separately (not the model's point): subtracting the whole Schedule C interest rather than its QPVLI share misstates column (iii) on a partly qualifying loan; see findings.md F1 (fr-2025-24154 p. 23, proposed 1.163-16(g)(2): QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI", and (g)(1) limits independently deductible interest to interest "that is QPVLI").

## Raw response

```yaml
lines:
  - key: "22(ii)"
    status: MISMATCH
    reason: "The IRS text says to enter 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F),' but the restatement limits the input to interest deducted on Schedule C only."
  - key: "22(iii)"
    status: MISMATCH
    reason: "The IRS text says to enter 'the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii),' but the restatement subtracts only a Schedule C helper that is zero without a Schedule C, omitting deductions elsewhere such as Schedule E or Schedule F."
```
