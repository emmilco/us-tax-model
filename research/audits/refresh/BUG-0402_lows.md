# Refresh round (2026-11-03): low findings for one batch entry, BUG-0402

Completeness lows are ruled `real gap` with `"bug": "BUG-0402"` in `reviews/2025/completeness/rulings.json`; screen
lows are class `low` with `bugs: ["BUG-0402"]` in `reviews/2025/screens/rulings.json`. Each is wording that rarely
changes an amount. Proposed fix in brackets; none was applied (forms are not owned here).

## Completeness

| claim | source | gap [fix] |
| --- | --- | --- |
| asset#1 | p946 pp. 33-34 | An addition or improvement to personal property takes the original's class; recovery starts at the later placed-in-service date [state in `asset.class`]. Rental real estate is Schedule E, refused. |
| f4562#3 | i4562 p. 9 | A partial disposition of an asset is not named [add "or a portion of it" to `asset.screen`'s disposition item]. |
| f8606#1 | i8606 p. 9 | A repayment of a qualified reservist distribution is not added to line 1 [refuse it, e.g. in `person.ira_excess` or `retirement.special`]. |
| f8889#1 | i8889 p. 4 | Combat-zone or contingency-operation contributions after April 15, 2026 [say "or later if you served in a combat zone" in `f8889.line2`]. |
| f8889#2 | i8889 p. 3 | One rollover per 12 months, into an HSA of the same beneficiary [state in `f8889.rollover`]. |
| otjob#1 | i1040gi p. 106 | Qualified tips and weekend/holiday premiums in weeks of 40 hours or fewer are not excluded [state in `otjob.statement`]. |
| tipjob#1 | i1040gi p. 102 | Prostitution and pornographic activity are not excluded outright [add to `tipjob.qualified`]. |
| s3#1 | i1040gi p. 117 | A payment processing fee is not excluded [state in `s3.line10`]. |
| s1#4 | p504 p. 14 | Payments between spouses filing a joint return with each other are not excluded [state in `s1.alimony_received`/`_paid`]. |
| sli#1 | i1040gi pp. 98-99 | "Qualified student loan" is not defined (whose expenses, related-person lender, mixed use, employer plan) [state in `sli.interest`]. |
| s179#5 | i4562 p. 5 | `s179.line10` does not exclude carryover attributable to qualified section 179 real property [state it]. The claim's other point (line 10 hidden) is wrong: `shown_when` is display only. |
| retirement#3 | p575 p. 23 | A required minimum distribution is not an eligible rollover distribution [state in `retirement.rollover`]. |
| retirement#4 | p590b p. 28; i5329 p. 5 | BUG-0393 stated exceptions 01 to 04 only; 09 (2-year no-ownership test, spouse included), the reservist exception and 19 (eligible adoptee) still lack conditions [extend `retirement.exception`]. Caps are applied. Closest to medium of the batch. |
| sales#1 | p550 pp. 82, 86; i8949 pp. 2, 5 | Other holding-period rules: wash-sale replacement tacking, stock dividends and rights, options, nonbusiness bad debts and NAV funds (short-term), short sales [state in `sales.box` or refuse]. |
| sales#2 | p550 p. 86; i8949 pp. 6-7 | Wash-sale, short-sale dividend, compensatory option and nondividend-distribution basis adjustments [state in `sales.correct_basis`]. |
| scope#1 | p575 p. 35 | Recontribution of a home-purchase distribution canceled because of a qualified disaster (Form 8915-F) [add to `retirement.special`]. Same as screen retirement.special finding 1. |
| scope#2 | i1040gi p. 36 | Schedule J income averaging for fishing income on Schedule C is not offered (can only lower tax) [name Schedule J in `scope.other_line16`]. |
| scveh#1 | i4562 p. 14 | A leased vehicle converted to or from personal use in 2025 is not refused (`scveh.screened` gates only `scveh.cost`) [gate `scveh.lease_business` too]. |
| scveh#3 | i1040sc p. 15 | Same root as scveh#1: commuting miles of a converted leased or standard-mileage vehicle are not limited to the business period. |
| w2#2 | iw2w3 p. 17 | Box 2 of a Form W-2AS, W-2CM, W-2GU or W-2VI is territorial tax, not federal withholding [state in `w2.box2`, or refuse territorial forms]. |

## Screens

| screen, finding | source | gap [fix] |
| --- | --- | --- |
| f4952.unsupported 0, 1 | f4952 p. 3 | `f4952.line1` does not define investment interest: mixed-use loan allocation, capitalized (263A) and section 264 interest [define in `f4952.line1`]. |
| f8960.unsupported 2 | i8960 p. 13 | Gain on surrendering a life insurance contract (line 7) is not named [add to the question]. |
| f8960.unsupported 3 | i8960 p. 9 | Capital loss carryforward adjustment for earlier excluded line 5b/5c losses [name it]. |
| retirement.special 1 | p575 p. 35 | As completeness scope#1. |
| sales.special 2 | i1040sd p. 11 | "Depreciable real property" may miss a home with a past home office or former rental [say "real property for which depreciation was allowed or allowable"]. |

## From the person, household, dependent and scope adjudication

| claim | source | gap [fix] |
| --- | --- | --- |
| person (SEP worksheet) | i1040gi Schedule 1 line 16; p560 | The self-employed SEP worksheet steps carry no `shown_when` (display only) [add the worksheet's visibility]. |
| person.educator_expenses | i1040gi p. 93 | Omits the inclusion of protective equipment to stop the spread of disease [state it]. |
| ssb (SSB-L1) | i1040gi p. 32, lines 7 and 9 STOP | After the line 7 and line 9 STOPs, lines 8, 10 and 17 still show amounts (stage10.ss.none: line 10 $9,000, line 17 $17,000; line 18 and Form 1040 line 6b $0); display only, predates the round [add `shown_when` for the STOP branches]. |
| scveh column (i) | i4562 p. 13, Part V column (i) | The column prints the section 179 election as answered; for a passenger automobile whose election exceeds worksheet line 9 it shows more than the capped amount deducted (no tax amount differs) [print the capped amount]. |
| sc.line24a | i1040sc p. 8, incidental expenses | The exclusions omit "cleaning and pressing of clothing" and "telegrams" [add them]. |
