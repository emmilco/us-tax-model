# Screen adjudication, group 11 (round 3, 2026-11-04): retirement.special after the round-3 fixes

The rerun after `retirement.special` named nonperiodic payments on or after the annuity starting date (a single sum at
the start, a full discharge, a payment that reduced later payments) and a recontribution of a wrongfully levied
distribution (BUG-0414's lows retirement#1 and retirement#3): verdict NARROW, five findings. Finding 0 is covered by
`retirement.bad_code`; findings 1 and 2 are model errors (box 5, the cost the payer reports as recovered tax free this
year, is subtracted for any plan distribution, which includes the pro-rata and pre-1987 rules for a distribution before
the annuity starting date); findings 3 (plan loan offset) and 4 (nondeductible IRA basis) can only refuse. Findings 0, 1
and 4 repeat groups 9 and 10 (`group9.md`, `group10.md`). The round-3 additions drew no finding. No defect.
