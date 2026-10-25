# Render comparison — carloan

The rendered English of every printed line of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` (`rendered/2025/carloan.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 95be33d73a560c02917de907e8ec2a73fd8ec91d949bf0bbbba7356ab4b01113 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: IRS column (ii) says 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)', but the restatement limits it to Schedule C.

Ruling: scope; i1040gi (2025) p. 110 line 22 column (ii) includes QPVLI deducted elsewhere, naming Schedule C, E and F. Schedule E/K-1, farm and other unmodeled Schedule 1 income are explicitly refused by scope.schedule1 at f1040.line8/line10. Within a supported completed return Schedule C is the only modeled competing interest deduction, so the input is narrowed to that amount. The objection correctly describes the wider IRS form; no claim is made that this standalone input handles a return needing E or F, and it is not model error.

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **MISMATCH**

Restated: Subtract helper "Interest deducted on Schedule C (zero without a Schedule C)" from helper "Interest for this loan, Schedule 1-A". If zero or less, enter -0-.

Model: IRS line 22(iii) says to subtract 'the amount on line 22, column (ii)', which can include Schedule E or Schedule F deductions; the restatement subtracts only a Schedule C helper (zero without a Schedule C), so it does not compute the IRS line.

Ruling: scope; i1040gi (2025) p. 110 line 22 column (iii) subtracts column (ii) from QPVLI. The preceding column (ii) scope ruling applies: Schedule E/F and partnership income are refused through scope.schedule1 at Form 1040 lines 8/10, leaving Schedule C as the supported competing deduction. The subtraction matches within that completed-return slice. Do not count the objection as model noise or claim standalone support for the excluded cases.

## Raw response

```yaml
lines:
  - key: "22(ii)"
    status: MISMATCH
    reason: "IRS column (ii) says 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)', but the restatement limits it to Schedule C."
  - key: "22(iii)"
    status: MISMATCH
    reason: "IRS line 22(iii) says to subtract 'the amount on line 22, column (ii)', which can include Schedule E or Schedule F deductions; the restatement subtracts only a Schedule C helper (zero without a Schedule C), so it does not compute the IRS line."
```
