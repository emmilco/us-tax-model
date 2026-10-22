# Render comparison — carloan

The rendered English of every printed line of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` (`rendered/2025/carloan.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | eaf5a136668e077ec084b6fb6fb359fb478217c6120ee593c1285bcc6cd01117 |
| subject sha256 | e3ad60c7b6114981b47aa0a5d8ed5e62b56d05cba3b15e43adcebc34ddec9216 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### 22(ii) — Interest on this loan deducted on Schedule C
Status: **MISMATCH**

Restated: Input — The part of this loan's 2025 interest you deduct on Schedule C (the business use of the vehicle; zero if none)

Model: The instructions say to enter "the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)". The restatement takes only interest deducted on Schedule C, so it leaves out Schedule E and Schedule F amounts and has no refusal for them. It also asks for any part of the loan's interest rather than only the QPVLI part.

Ruling: refusal located elsewhere; restatement accepted. Schedules E and F are outside the tool (scope.schedule1 refuses Form 1040 lines 8 and 10 whenever either applies), so the only place on the return QPVLI can be deducted is Schedule C; the question asks for the part of this loan's interest deducted there, which is QPVLI deducted elsewhere when the loan qualifies.

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **MISMATCH**

Restated: Subtract helper "Interest deducted on Schedule C (zero without a Schedule C)" from helper "Interest for this loan, Schedule 1-A". If zero or less, enter -0-.

Model: Column (iii) is "the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)". The QPVLI side matches, but the amount subtracted is only Schedule C interest, and it is zero when there is no Schedule C. QPVLI deducted on Schedule E or F is therefore not subtracted, and the same interest could be deducted twice.

Ruling: fixed (BUG-0058), then refusal located elsewhere; restatement accepted. The interest input now asks for the total interest, including any part deducted on Schedule C, so the subtraction of column (ii) removes it once. Schedules E and F are refused through scope.schedule1, so no other amount is deducted elsewhere.

## Raw response

```yaml
```yaml
lines:
  - key: "22(ii)"
    status: MISMATCH
    reason: "The instructions say to enter \"the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)\". The restatement takes only interest deducted on Schedule C, so it leaves out Schedule E and Schedule F amounts and has no refusal for them. It also asks for any part of the loan's interest rather than only the QPVLI part."
  - key: "22(iii)"
    status: MISMATCH
    reason: "Column (iii) is \"the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)\". The QPVLI side matches, but the amount subtracted is only Schedule C interest, and it is zero when there is no Schedule C. QPVLI deducted on Schedule E or F is therefore not subtracted, and the same interest could be deducted twice."
```
```
