# Completeness review, round 10 (xrr, release rerun after the xint integration): adjudication of the rinc family

Family `rinc` (forms `s1`, `sa`, `oi8z`, `w2`, `tipjob`, `otjob`, `f4137`, `f4137row`, `f8919`, `f8919firm`, `scope`, `f1040`,
`refund`, `s2`, `rec`, `g28`, `tcw`, `s1a`, `ltc`, `mq`, `sdtw`). Fifteen claims were unruled at the B1 plus expansion tree
(`.claude/worktrees/xint`): nine of `f1040` (subject `ef57f669`) and six of `s2` (subject `16512365`); every other claim of the
family already carried an accepted ruling. The rulings are in `/tmp/xrr/frag/rinc.completeness.json`, keys
`unruled:<form>#1.<n>`, each with the record's current `subject_sha`; the lead merges them. `xrr.py merge` (no `--write`)
refuses none of them. No new bug is filed for completeness: the two real gaps cite open numbered entries.

The xrel rulings of the same units were leads only. Each claim was checked against the current lines (`forms/2025/*.yaml`),
the interview wording (`interview/2025/questions.yaml`) and the quoted source (`sources/2025/`), and where a refusal was
the answer it was executed with `node engine/dist/main.js --year 2025 eval` on copies of fixtures under `/tmp/xrr/rinc/`.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f1040 | 9 | 2 | 0 | 7 | 0 | 0 |
| s2 | 6 | 0 | 0 | 6 | 0 | 0 |
| **total** | 15 | 2 | 0 | 13 | 0 | 0 |

## f1040

| Claim | Item | Class | Where |
|---|---|---|---|
| f1040#1.1 | status: nonresident alien spouse, the resident choices, divorce to remarry | real gap (BUG-0828) | A spouse nonresident for any part of 2025 is refused by `scope.nonresident` through `scope.other_income` (executed: line 12e, 24 and `scope.ready` refused); divorce to remarry is in the help of `household.married_dec31`. Residual: a spouse treated as a resident under a section 6013(g) choice can answer No (the help speaks only of a green card), and the return is prepared with no prompt for the first-year statement. Same cause and fix as BUG-0828 (the NIIT side); cited, not filed again. Low. |
| f1040#1.2 | line 12e: dual-status alien, line 12c | out of scope (`scope.other_income`) | A dual-status alien was nonresident for part of 2025 and answers Yes to `scope.nonresident`; executed: line 12e and 24 refused. |
| f1040#1.3 | line 1a: inmate wages, nonqualified plan pensions, chapter 11 | out of scope (`s1.line8_other`) | Inmate pay now refuses at `s1.line8_other` (T-336): executed, line 8 and 24 refused, so BUG-0893's double count no longer reaches a completed return. `s1.nqdc_pension` refuses at the same gate (executed). Chapter 11 by `scope.chapter11`. |
| f1040#1.4 | line 1h: excess deferrals, corrective distributions | out of scope (`scope.other_income`) | `scope.excess_deferral` (executed: line 24 refused); codes 8, P and E are "other" and refused by `retirement.bad_code`. |
| f1040#1.5 | line 4b: QCD and HSA funding distribution | out of scope (`retirement.special`) | `retirement.charity_hsa`; executed on `stage10.smw.first_year` as a traditional IRA: line 4b and 24 refused. |
| f1040#1.6 | line 5b: retired public safety officer exclusion | out of scope (`retirement.special`) | `retirement.pso_exclusion`; executed: line 5b and 24 refused. |
| f1040#1.7 | line 6a: disability benefits from a terrorist attack | out of scope (`ssb.terror_disability`) | The claim missed the question; executed on `stage10.ss.top`: line 6b and 24 refused. |
| f1040#1.8 | line 26: joint estimated payments on separate returns | real gap (BUG-0894) | Unchanged since xrel: the question and help address only a joint return. |
| f1040#1.9 | line 29: Form 8862 and the bans for the American opportunity credit | out of scope (`f8863.ban_refused`) | The claim missed `f8863.ban`; executed on `stage19.example.jack_kay`: line 29 $1,000, and with `f8863.ban` true line 29 and 24 refused. |

## s2

| Claim | Item | Class | Where |
|---|---|---|---|
| s2#1.1 | private activity bond dividends, box 13 of Form 1099-DIV | out of scope (`div.amt`) | Box 13 is asked through `div.other_boxes` and `div.box13`; executed: line 16 and 24 refused at `div.amt`. |
| s2#1.2 | line 2h (section 1202) and the section 170(e) adjustment | out of scope (`sales.special`) | Section 1202 sales refused by `sales.special`, box 2c by `div.section1202`. The xrel ruling's `sd.small_business_stock` is now the section 1244/1242 question and was not relied on. The AMT basis of property the tool holds is never below its regular basis, so the 170(e) adjustment can only lower AMTI and the line 4 bound holds. |
| s2#1.3 | Schedule C AMT adjustments | out of scope (`sc.screened`) | Depletion, Form 8990, the research-cost election and other amortization by `sc.special`; long-term contracts by `sc.method_other`; currently deducted research costs need no adjustment with material participation, and no material participation refuses (`sc.passive`). |
| s2#1.4 | Who Must File statements 2 and 3; Form 8801 | out of scope (`s3.business_credit_any`) | The credits are refused (`s3.business_credit_any`, `s3.ev_equipment`, `s3.other_credit`, `s3.prior_amt_if_forms`, `s3.prior_forms_if_forms`). |
| s2#1.5 | Form 2555 and Part III | out of scope (`sa.excluded_income`) | Executed: line 16 and 24 refused at `sa.excluded_income`. |
| s2#1.6 | line 4: SE tax exemptions and special cases | out of scope (`person.se_screened`) | `person.se_screen` (Form 4029, totalization, foreign government work); notary fees by the Schedule C screen; Form 2555 by `sa.excluded_income`; chapter 11 by `scope.chapter11`. |

## Defects

None filed. The real gaps cite BUG-0828 (open, low; the f1040 status statement is a sibling of its NIIT symptom, and its first
proposed fix covers both) and BUG-0894 (open, low).

## Notes for the lead

- BUG-0893 (inmate wages counted twice) no longer reaches a completed return: inmate pay refuses at `s1.line8_other` until
  T-336 computes it.
- The xrel ruling `s2#1.1` cited `sd.small_business_stock` for section 1202; that line is now the section 1244/1242 ordinary
  loss question. This round cites `sales.special` and `div.section1202`.
