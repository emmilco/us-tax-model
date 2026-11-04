# Round 2 (2026-11-04): low findings for one batch entry, BUG-0414

Completeness lows are ruled `real gap` with `"bug": "BUG-0414"` in `reviews/2025/completeness/rulings.json`. Each is
wording that rarely changes an amount. Proposed fix in brackets; none was applied (each is fixed with its form's next
pass, T-229). No screen lows this round.

| claim | source | gap [fix] |
| --- | --- | --- |
| f8889#1 | i8889 pp. 2-3 | `f8889.medical` does not say insurance premiums count only for long-term care, COBRA, coverage while receiving unemployment compensation, or Medicare at 65 or older (not Medigap), or that a beneficiary under 65 cannot count a spouse's Medicare [state these rules]. |
| f8889#2 | i8889 pp. 3-4 | `f8889.line2` does not exclude direct trustee-to-trustee transfers between the filer's own HSAs [add them to the exclusions]. |
| retirement#1 | p575 p. 21; i5329 p. 2 | `retirement.rollover` omits other distributions that cannot be rolled over (substantially equal payments, hardship, dividends on employer securities, cost of life insurance, most beneficiary distributions), that a code S distribution in its first 2 years can go only to a SIMPLE IRA, and the recontribution of a wrongfully levied amount [state them, or refuse]. |
| s1#2 | p4681 p. 5 | `sli.interest` does not exclude interest paid through tax-free student loan repayment assistance (NHSC and state health-service programs) [exclude it]. |
| s1#3 | p504 p. 13 | `s1.alimony_received` says cash payments only and omits cash paid to third parties, including premiums on life insurance the recipient owns [say these count]. |
| sales#1 | p550 p. 82; i8949 p. 6 | `sales.box` lacks the remaining holding-period rules: Treasury auction and subscription dates, automatic investment services, nontaxable-trade tacking, a 2010 decedent with a Form 8939 election, real property, trade date rather than settlement date, the 2001 deemed sale [state them, or refuse the rare ones]. |
| sales#2 | i8949 p. 6 | `sales.proceeds` does not add the premium of a written call that was exercised [state it]. |
| sales#3 | i8949 pp. 6-7 | `sales.correct_basis` does not name gift basis (donor's basis), inherited basis (value at death), the 2001 deemed sale, stock splits, OID and market discount included in income, bond premium amortization, bargain sales or the average basis method [name them]. |
| sales#4 | p550 p. 86 | `sales.wash_loss` does not define a wash sale: the 30-day window, contracts and options, IRA purchases, spouse or controlled corporation, the dealer exception [define it]. Nearest to medium. |
| scveh#2 | p463 p. 26 | `scveh.cost` does not mention destination charges, dealer preparation or the gas guzzler tax reduction; `scveh.screen` does not name substantial improvements [name these in `scveh.cost`; add substantial improvements to `scveh.screen`]. |
| scveh#3 | i4562 p. 14; p463 p. 25 | investment-use miles are not asked, so the business/investment use percentage is understated [ask for them, or refuse any investment use]. |
| retirement#3 (rerun after BUG-0413) | p575 p. 16 | `retirement.annuity` does not say that a box 1 including a nonperiodic payment received on or after the annuity starting date is not paid in periodic payments; on the Simplified Method path the periodic exclusion would reach it [say so in `retirement.annuity`, or refuse in `retirement.special`]. |

Added by the first completeness reviews of f4952, f8880 and person (T-094, 2026-11-04), after the BUG-0414 entry was
written:

| claim | source | gap [fix] |
| --- | --- | --- |
| f4952#2 | f4952 p. 4 | `f4952.line4g` takes any elected amount without saying the election must be made "on a timely filed return, including extensions"; the amended-return election, the 301.9100-2 notation and revocation are amended-return matters, out of scope [say timely filed, including extensions, in `f4952.line4g`, or refuse an election on a late-filed return, as `sc.ho_other` does for the home office election]. |
| person#2 | p560 p. 17 | `person.simple_employer` asks for employer contributions "for 2025" without the deadline, "by the due date (including extensions)", which `person.sep_contrib` states [add it to `person.simple_employer`]. |
