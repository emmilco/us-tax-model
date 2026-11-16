# New York screen and false-no adjudication, lane xrel, fork ny (2026-11-15)

These are the sampled release reviews of the New York units, adjudicated by claude-opus-5-5 (judgment) for tax year
2025, jurisdiction ny. The rulings are in `/tmp/xrel/frag/ny.screens.json` (25 samples) and `/tmp/xrel/frag/ny.false_no.json`
(20 samples), for the lead to merge; no `rulings.json` was edited. `python3 /tmp/xrel/xrel.py merge --jurisdiction ny`
(validation only) accepts all 45 with no REFUSED line. Two screen units, `ny_it201.ask.dependent_care` and `ny_it201.ask.mctmt`,
were already ruled and were not reruled.

Quotes were checked against `sources/ny/2025/ny_it201i.txt`, `ny_it201i-html.txt` and `ny_it214i.txt`. The encoding was
checked against `forms/ny/2025/ny_it201.yaml` and the federal lines it reads. The wording a filer reads was checked against
`interview/ny/2025/questions.yaml` and `interview/2025/questions.yaml`: the bank prompt, not the line's label. Two facts
settle many findings:
- The tool prepares IT-201 only for a full-year New York City resident. A No to the City question always refuses
  (`ny_it201.gate.part_year_city`), so a wrong No there is a refusal, not a silent amount.
- Every Schedule K-1 is still refused federally by `scope.k1` in `scope.schedule1`; the k1p collection is encoded but
  not wired.

One earlier ruling no longer holds. Disability pensions paid before the minimum retirement age are now computed federally
on Form 1040 line 1h, not refused. One case was evaluated (`/tmp/xrel/ny/dis_inputs.json`): a full-year City resident with
an $18,000 disability pension. It gave `f1040.line1h` $18,000, `ny_it201.line9` and `line10` $0, `has_pension_income` false and
`line26` $0, with no refusal.

## Counts

| Tool | Samples | Findings | Defect | Open residual | Covered | Out of scope | Accepted WIDE | Presentation | Model error |
|---|---|---|---|---|---|---|---|---|---|
| screens | 25 | 72 | 18 | 0 | 17 | 15 | 13 | 3 | 6 |
| false-no | 20 | 101 | 38 | 1 | 35 | 16 | 0 | 6 | 5 |

Samples with a defect: 10 of 25 screens and 13 of 20 false-no samples. The defects are 11 new pending bugs, most of them
low-severity wording.

## Screens

| Unit | Verdict | Findings (n: class) | Bug |
|---|---|---|---|
| `ny_it201.ask.414h` | UNCLEAR | 0: covered | |
| `ny_it201.ask.529_nonqualified` | WIDE | 0: accepted WIDE | |
| `ny_it201.ask.529_owner` | WIDE | 0: accepted WIDE | |
| `ny_it201.ask.abode_part_year` | UNCLEAR | 0: presentation | |
| `ny_it201.ask.city_credits` | UNCLEAR | 0: out of scope | |
| `ny_it201.ask.out_of_state_bond_interest` | NARROW | 0: out of scope (K-1) | |
| `ny_it201.ask.real_property_credit` | WIDE | 0: accepted WIDE; 1: model error | |
| `ny_it201.ask.special_accrual` | WIDE | 0: accepted WIDE; 1: defect | BUG-0855 |
| `ny_it201.ask.us_obligation_interest` | WIDE | 0, 2: accepted WIDE; 1: out of scope (K-1) | |
| `gate:ny_it201.ask.city_resident` | NARROW | 0 to 3: covered (a City No refuses) | |
| `gate:ny_it201.ask.est_any` | NARROW | 0, 1: defect | BUG-0853 |
| `gate:ny_it201.ask.owes_use_tax` | NARROW | 0: defect; 1, 2: model error (the filer is a City resident) | BUG-0854 |
| `gate:ny_it201.estimated_payments_positive` | NARROW | 0: covered (`est_penalty_balance`); 1: accepted WIDE | |
| `gate:ny_it201.federal_care` | UNCLEAR | 0, 1: covered; 2: accepted WIDE | |
| `gate:ny_it201.has_edu_account` | NARROW | 0: out of scope (`person.x_other`); 1: covered; 2: defect; 3: accepted WIDE | BUG-0851 |
| `gate:ny_it201.has_other_income` | NARROW | 0 to 2: defect | BUG-0859 |
| `gate:ny_it201.has_pension_income` | NARROW | 0, 1: defect; 2: covered; 3: accepted WIDE | BUG-0850 |
| `gate:ny_it201.has_tax_exempt` | NARROW | 0 to 2: defect; 3: out of scope (K-1); 4: accepted WIDE | BUG-0857 |
| `gate:ny_it201.low_income` | NARROW | 0, 1, 3: defect; 2: presentation; 4: accepted WIDE | BUG-0856 |
| `gate:ny_it201.mctmt_possible` | NARROW | 0, 1: out of scope; 2: accepted WIDE | |
| `gate:ny_it201.moved` | NARROW | 0 to 2: out of scope; 3: defect | BUG-0855 |
| `gate:ny_it201.ny_529_if_account` | NARROW | 0: out of scope; 1, 3: covered; 2: defect | BUG-0851 |
| `gate:ny_it201.pension_59_known` | NARROW | 0, 1, 3: covered; 2: model error | |
| `gate:ny_it201.public_job_if_w2` | UNCLEAR | 0, 1: covered; 2: model error | |
| `gate:s1.has_sc` | NARROW | 0 to 3: out of scope; 4: presentation; 5: model error | |

## False-no

| Unit | Findings (n: class) | Bug |
|---|---|---|
| `gate:ny_it201.ask.city_resident` | 0 to 6: covered (a City No refuses) | |
| `gate:ny_it201.ask.est_any` | 0 to 2: defect; 3, 4: covered | BUG-0853 |
| `gate:ny_it201.ask.owes_use_tax` | 0, 3, 4: defect; 1, 2: covered | BUG-0854 |
| `gate:ny_it201.estimated_payments_positive` | 0, 1: covered; 2, 3: defect; 4: presentation | BUG-0853 |
| `gate:ny_it201.federal_care` | 0 to 4: covered (the current f2441 prompts and help) | |
| `gate:ny_it201.gov_said_no` | 0: defect; 1: presentation; 2 to 5: covered | BUG-0850 |
| `gate:ny_it201.has_edu_account` | 0: out of scope; 1, 3: defect; 2: covered | BUG-0851 |
| `gate:ny_it201.has_line28_income` | 0, 1: defect; 2: out of scope; 3: model error | BUG-0858 |
| `gate:ny_it201.has_other_income` | 0 to 3: defect | BUG-0859 |
| `gate:ny_it201.has_pension_income` | 0: defect; 1, 2, 4: covered; 3: presentation | BUG-0850 |
| `gate:ny_it201.has_tax_exempt` | 0, 1, 4: defect (BUG-0857); 3: defect (BUG-0858); 2: out of scope; 5: model error | BUG-0857, BUG-0858 |
| `gate:ny_it201.low_income` | 0 to 5: defect | BUG-0856 |
| `gate:ny_it201.mctmt_possible` | 0 to 2: out of scope; 3: presentation | |
| `gate:ny_it201.moved` | 0, 1, 5: out of scope; 2: covered; 3, 4: defect | BUG-0855 |
| `gate:ny_it201.ny_529_if_account` | 0, 4, 5: defect; 1, 6: out of scope; 2, 3: covered; 7: presentation | BUG-0851 |
| `gate:ny_it201.pension_59_known` | 0, 1: covered; 2, 3: model error | |
| `gate:ny_it201.public_job_if_w2` | 0 to 3: covered | |
| `gate:s1.has_sc` | 0 to 2: out of scope; 3: presentation; 4: model error | |
| `gate:scope.armed_forces` | 0, 2: defect (BUG-0852); 1: out of scope; 3: open residual (BUG-0902) | BUG-0852 |
| `gate:scope.has_w2` | 0 to 2: defect; 3: out of scope | BUG-0860 |

## Pending bugs (xrelny-NN; numbered at integration in order: 01 is BUG-0850 and 11 is BUG-0860)

| Id | Severity | Defect | Proposed fix |
|---|---|---|---|
| 01 | medium | `ny_it201.has_pension_income` reads only lines 9 and 10, so a government disability pension on line 1h never reaches line 26. Evaluated. | Also make it true when `person.dis_wages` > 0; name a territory and D.C. in the gov_pension prompt. |
| 02 | medium | `ny_it201.ask.ny_529` is in the present tense: an account closed or moved to another state's plan in 2025 skips the line 22 recapture. The Advisor-Guided plan and the July 4, 2025 credentialing date are not mentioned. | Ask "At any time in 2025 ...", naming both plans and a closed or moved account. Add the credentialing date and the eligible-institution rule to 529_nonqualified. |
| 03 | low | SCRA elections: a civilian spouse on a separate return, and PHS and NOAA officers, are not asked. | Add a New York active-duty question asked on every return (spouse included), refusing with codes M4 to M9. |
| 04 | low | est_any omits estate or trust allocations and City, Yonkers and MCTMT payments. est_late can exclude a skipped installment or the spouse's payments. | Reword both questions. |
| 05 | low | owes_use_tax's shown prompt omits the spouse, services and reservation purchases. | Reword the prompt. |
| 06 | low | special_accrual's "earned in one year but paid in the other" misses income fixed before 2025 and reported in 2025, and installment gains. | Reword in terms of income fixed in one year and reported in another. |
| 07 | low | real_property_credit omits furnishings, the subsidized share, the spouse and co-ops, and asks about property owned now. | Reword the prompt. |
| 08 | low | has_tax_exempt reads line 2a, which is net of premium. Accrued interest at sale and the out-of-state share of a New York fund are also missed. | Gate on any interest or dividends, or on a premium yes/no. Extend the help. |
| 09 | low | us_obligation_interest lists only Treasuries and savings bonds. The ny_interest heading omits the spouse. | Name other federal obligations, and the spouse in the heading. |
| 10 | low | has_other_income reads Schedule 1 line 9 only. A check entered as a state refund (line 1), a spouse's check, and netting are missed. | Gate on line 1 or any line 8 item. Reword the prompt. |
| 11 | low | public_job asks about work in 2025 "in New York", missing arrears W-2s, remote work and public benefit corporations. | Ask about a 2025 W-2 from a New York public employer. |

No form data, fixture, question or tool was changed. No paid call was made, and nothing was committed.
