# Completeness review, round 9 (xrel, sampled release reviews): adjudication of the inc family

Family `inc` (forms `s1`, `sa`, `oi8z`, `w2`, `tipjob`, `otjob`, `f4137`, `f4137row`, `f8919`, `f8919firm`). Twenty-two
claims were unruled at the B1 plus expansion tree (`.claude/worktrees/xint`); `s1` and `otjob` had none. The rulings
are in the fragment `/tmp/xrel/frag/inc.completeness.json`, keys `unruled:<form>#1.<n>`, each with the record's
current `subject_sha`; the lead merges them into `rulings.json`. `xrel.py merge` (no `--write`) refuses none of them.
The four real gaps carry pending ids (`BUG-0801` to `-04`), which fail the gate until the numbered-bug pass.

Earlier rulings were leads only. Each claim was checked against the current lines (`forms/2025/*.yaml`), the
rendered English (`rendered/2025/*.md`) and the interview wording (`interview/2025/questions.yaml`), and its quote
against `sources/2025/*.cols.txt`. No claim turned on an amount the tool computes, so no evaluation was run.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f4137 | 4 | 0 | 3 | 1 | 0 | 0 |
| f4137row | 3 | 0 | 1 | 1 | 1 | 0 |
| f8919 | 2 | 0 | 1 | 0 | 0 | 1 |
| f8919firm | 2 | 0 | 1 | 0 | 1 | 0 |
| oi8z | 2 | 1 | 0 | 1 | 0 | 0 |
| sa | 5 | 3 | 0 | 2 | 0 | 0 |
| tipjob | 1 | 0 | 1 | 0 | 0 | 0 |
| w2 | 3 | 0 | 0 | 3 | 0 | 0 |
| **total** | 22 | 4 | 7 | 8 | 2 | 1 |

## f4137 and f4137row

| Claim | Item | Class | Where |
|---|---|---|---|
| f4137#1.1 | line 2: allocated tips (W-2 box 8); timing of reported tips (f4137 p. 2) | out of scope (gate `s2.other`) | `s2.w2_marks` asks about any box 8 amount ("A Yes ends the interview here") and refuses through `s2.other`. Timing as f4137#1.2. |
| f4137#1.2 | line 3: timely or late reporting decides the year | covered (`f4137row.col_d`) | col_c help moves December 2025 tips reported in January 2026 to 2026; col_d help counts late-reported 2025 tips. December 2024 tips reported in January 2025 drop out of columns (c) and (d) together, so line 4 and the tax do not change. |
| f4137#1.3 | line 5: the $20 rule per employer | covered (`person.f4137_under20`) | "because the tips at one job came to less than $20 in a calendar month". |
| f4137#1.4 | files: a misclassified worker's Form 1099 pay is not for Form 4137 | covered (`scope.contractor_pay`) | Form 4137 takes only tips per employer; contractor pay is asked by `scope.contractor_pay` and goes to Form 8919. |
| f4137row#1.1 | col_c: allocated tips; RRTA | out of scope (gate `s2.other`) | Box 8 as f4137#1.1; RRTA refused on `f4137.line8` (`person.rrta`). |
| f4137row#1.2 | col_d: the timing rule and the 10th-day rule | covered (`f4137row.col_d`) | As f4137#1.2. |
| f4137row#1.3 | columns (a), (b); more than five employers | presentation | Names and EINs change no amount; the rows have no limit of five and lines 2 and 3 total them. |

## f8919 and f8919firm

| Claim | Item | Class | Where |
|---|---|---|---|
| f8919#1.1 | files: who must file, reason codes, Form SS-8 | covered (`scope.contractor_pay`) | `scope.contractor_pay` asks the three conditions together; `f8919firm.reason` asks the code, and its help gives both SS-8 rules (code G: send it by the filing date; code H: do not send it). |
| f8919#1.2 | line 6 to Form 8959 line 3; per-firm columns | wrong | `f8959.line3` sums `person.f8919_wages`, so line 6 reaches the Additional Medicare Tax. The columns change no amount. |
| f8919firm#1.1 | reason: columns (a), (b), (d), (e); SS-8 with code H | presentation | Columns change no amount (collection note). The code-H SS-8 point is false: the help says "With the last one, do not send Form SS-8." |
| f8919firm#1.2 | wages: a separate Form 8919 for each spouse | covered (`f8919firm.wages`) | Firms are listed within each person, and Form 8919 is one per person, with that person's own wage base. |

## oi8z

| Claim | Item | Class | Where |
|---|---|---|---|
| oi8z#1.1 | injury: medical care for non-physical emotional distress; awards before September 13, 1995; attorney fees (p525 p. 32) | **real gap**, low, BUG-0804 | `oi8z.injury` asks only about a physical injury; `oi8z.amount` gives no rule for these three points. |
| oi8z#1.2 | amount: credit card insurance, a free tour, sale of an expected inheritance (p525 pp. 32-34) | out of scope (gate `oi8z.figured`) | Each is kind "Something else", which `oi8z.figured` refuses. |

## sa

| Claim | Item | Class | Where |
|---|---|---|---|
| sa#1.1 | line 1: a person who would be a dependent but for the filer being claimable (i1040sca p. 2) | **real gap**, low, BUG-0801 | The `sa.line1` list leaves out this category; no refusal covers it. |
| sa#1.2 | line 6: generation-skipping tax on income distributions (i1040sca p. 7) | **real gap**, low, BUG-0802 | Line 6 is zero; `sa.unsupported` refuses only the foreign tax deduction; no question names GST. |
| sa#1.3 | line 8a: reduce by Form 8396 line 3 (i1040sca p. 8) | out of scope (gate `s3.mcc_if_interest`) | `s3.mcc` is asked when line 8a is above zero, and a Yes refuses on `s3.line7` (Form 8396). |
| sa#1.4 | line 11: gifts to foreign organizations (i1040sca p. 10) | **real gap**, medium, BUG-0803 | No leave-out for a gift made directly to a foreign charity. |
| sa#1.5 | line 16: repayment of more than $3,000 under a claim of right (i1040sca p. 12) | out of scope (gate `s3.repaid_income`) | Asked in the rare-credits group; a Yes refuses on `s3.line14`. The reviewer did not see this question because it is on Schedule 3. |

## tipjob and w2

| Claim | Item | Class | Where |
|---|---|---|---|
| tipjob#1.1 | tips: the Form 4070 total as column 1(b) (i1040gi p. 103) | covered (`tipjob.tips`) | The help offers the Form 4070 total, with the $176,100 note. |
| w2#1.1 | box 5: Form 499R-2/W-2PR box 22 (i8959 p. 1) | out of scope (gate `f8959.unsupported`) | `f8959.territory_w2` (a Yes ends the interview) refuses Form 8959. Same as the earlier w2 rulings, rechecked. |
| w2#1.2 | box 6: Form 499R-2/W-2PR box 23 | out of scope (gate `f8959.unsupported`) | As w2#1.1. |
| w2#1.3 | dc_benefits: the combat pay election on Form 2441 (i2441 p. 5) | out of scope (gate `s8812.combat_pay`) | Asked of every filer; a Yes refuses the Form 2441 combat pay election (lines 4, 5, 18 and 19). |

## Bugs filed (pending)

- BUG-0801 (low): add the fourth category of whose medical costs count to `sa.line1`.
- BUG-0802 (low): ask about and refuse generation-skipping tax on Schedule A line 6.
- BUG-0803 (medium): leave out gifts made directly to foreign charities on line 11 and in `gift.deduction`.
- BUG-0804 (low): rules for taxable damages. Also reached by the screen `oi8z.injury` and the false-no review
  `gate:oi8z.damages` (see `reviews/2025/screens/adjudication/xrel-inc.md`). Those reviews propose a second fix:
  widen `oi8z.injury` so that a Yes refuses these damages too.
