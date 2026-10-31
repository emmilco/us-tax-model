# Screen adjudication, group 5 (2026-10-30)

Brief: `BRIEF.md`. Screens: 1 (`refund.box8`, re-reviewed after BUG-0251); findings: 2. Classes: accepted WIDE 2.
No PENDING defect. Prompt hash of the current entry: `2713d1b018178dca2dfbcd489b5d613dac00b23732438614a8cf05695b968b23`.
Evaluation: `node engine/dist/main.js eval` on the inputs of `stage16.mut.refund_single_unasked` (`fixtures/2025/stage16.json`)
with `refund.box8` yes and no; scratch in `/tmp/adj-screens-g5/`.

## `refund.box8`

Question: "Is any of these refunds a refund of a state or local income tax that applies only to income from a trade or
business (for example, box 8 is checked on the Form 1099-G that reports it), including such a refund for which you
received no Form 1099-G?" Gates `refund.taxable` (and through it Schedule 1 line 1, Form 1040 lines 8, 11a, 24).

The BUG-0251 rewording closes the NARROW gap ruled in group 3 (PENDING-3-3): a refund with no Form 1099-G is now covered.
Neither new finding is NARROW.

| # | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | UNCLEAR | accepted WIDE | f1099g p. 5, Box 8: "an income tax that applies exclusively to income from a trade or business and is not a tax of general application" | The misreading (a general income tax that in the filer's case reached only business income) gives YES and a refusal of a refund the tool computes; eval: yes refuses `refund.taxable`, `s1.line1`, `f1040.line11a` and `f1040.line24` on `refund.box8`, no gives Schedule 1 line 1 $1,400.00. A business-only tax answered NO is not invited by the wording. Safe. Optional sharpening: add "(not a tax of general application)". |
| 1 | WIDE | accepted WIDE | f1099g p. 5, Box 8: "If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate" | A nontaxable refund of a business-only tax (never deducted) is refused though zero is right. Safe; as group 3 finding 1. |

Note: the refusal's `form` text still reads "Form 1099-G box 8 (a refund of a tax on trade or business income, Schedule C
or F)"; its remedy matches the reworded question. Presentation only.
