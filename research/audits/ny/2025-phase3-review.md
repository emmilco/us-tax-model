# New York Phase 3: in-session independent review (step 7)

Three fresh subagents of the Phase 3 session, each given only the archived New York sources (`sources/ny/2025/`) and
the encoding (`forms/ny/2025/`, `params/ny/2025.yaml`, `tables/ny/2025/`, `ambiguities/ny/2025.yaml`,
`interview/ny/`), not the session's reasoning, reviewed the encoding on 2026-11-04 (brief, Phase 3 step 7). No
model or API call was made; no project review tool was run. Their reports are kept verbatim beside this file:

| Review | Report | Findings |
| --- | --- | --- |
| (a) completeness: operative rules the encoding neither computes, asks nor refuses | `2025-phase3-review/a_completeness.md` | 3 high, 1 medium, 5 low |
| (b) line-by-line re-transcription of every computed line and parameter | `2025-phase3-review/b_transcription.md` | 1 high, 1 medium, 5 low; 213 parameters, 1,302 x 2 tax-table bands, 92 household-credit cells and every worksheet constant confirmed |
| (c) refusal screens (too wide, too narrow, unclear) | `2025-phase3-review/c_screens.md` | 43 screens: 30 right; 3 high, 8 medium, 8 low (with the uncaught situations) |

These do not replace the project's review tools, which run on the owner's machine at integration (Phase 4).

## Rulings: medium and higher

Each fix has a fixture in `fixtures/ny/2025/it201.json` (case id in the last column).

| # | Finding | Ruling | Fix | Fixture |
| --- | --- | --- | --- | --- |
| b-H1 | Lines 72 and 73 summed W-2 withholding in cents; IT-2 p. 2 requires whole dollars per record ("drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar") | correct | `ny_it2.state_whole`, `ny_it2.city_whole` round each record half-up; lines 72, 73 sum them | `ny.review.it2_whole_dollars` |
| b-M1 | Worksheets' line 8/9: the prorated product was rounded to the cent and then to the dollar, contrary to `amb.ny.2025.whole_dollars`; $1 too much on some returns (807 x 0.0254 = 20.4978 entered as $21) | correct | the amount is scaled by 100 so prorate's product is exact, then divided by 100 with one rounding (`ny_tcw`, `ny_tcw_first`); register entry `amb.ny.2025.fourth_decimal` updated | `ny.review.worksheet_single_rounding` |
| a-H1, c-H1, c-M10, c-M11 | The estimated-tax penalty screen fired only with a balance due and annual totals: late or short installments (even with a refund) and a missing full-year 2024 return passed | correct | `gate.estimated_penalty` also refuses with no full-year 2024 return and a balance due (`ask.prior_full_year`), and with any estimated payment made late or short (`ask.est_late`) | `ny.refuse.no_prior_full_year`, `ny.refuse.est_late` |
| a-H2 | The line 75 question named only State and City payments | correct | the question names Yonkers and MCTMT payments, a spouse's separate payments, the Department-adjusted 2024 overpayment, estate or trust allocations, and excludes the NYC unincorporated business tax | (wording; no amount changes) |
| a-H3 | Line 59: the chart amount is prorated by months of a New York abode for part of the year; not asked | correct | `ask.abode_part_year`; `gate.use_tax_abode` refuses line 59 when use tax is owed with a part-year abode | `ny.refuse.use_tax_abode` |
| a-M1 | The residency questions omitted the Group A/B domicile exceptions, active military service and undergraduate housing (p. 30) | correct | the State question names them (the City question applies the same test) | (wording) |
| c-H2 | The pension exclusion question omitted IRA distributions, which qualify (p. 9) | correct | the question names IRA distributions | (wording) |
| c-H3 | Item H must include dependents "you were entitled to claim ... but chose not to"; the count reads `dependent.claimed` | not a defect | `dependent.claimed` (forms/2025/dependent.yaml) is true for a qualifying child or qualifying relative dependent, which is the entitlement, not whether the dependent was listed; no change | — |
| c-M4 | `gate.it270` uses the highest threshold plus $5,000 rather than the threshold for the number of dependents, refusing some filers whose credit would be zero | correct, by design | owner decision B10 (refuse where the credit may apply); the bound refuses more often but never lets a credit through; kept | `ny.household.hoh.*` (refusal of line 70a) |
| c-M5 | The line 4 branch of `gate.line25` | correct, by design | owner decision B1 (`amb.ny.2025.line25`); kept | `ny.refuse.line25` |
| c-M6 | `ask.special_code` refuses codes that change no computed line | correct, by design | owner decision B11; kept | `ny.refuse.special_code` |
| c-M7 | The IT-225 question named no common modification | correct | the question names S-124, S-118, A-215 and Form 4970 | (wording) |
| c-M8 | The itemizing question asked what the filer "wants", and missed the married-filing-separately rule (p. 11) | correct | the question asks whether the New York itemized deduction is larger, or the spouse itemizes on a separate return | (wording) |
| c-M9 | "Do you qualify" for the real property tax credit cannot be answered without IT-214 | correct (partly) | the question says the credit is limited to low-income households paying property tax or rent and to read the IT-214 instructions if unsure; IT-214 is not archived, so its test is not stated | (wording) |

## Lows (listed; not fixed unless noted)

- a-L1: items B, D1, D2, F, the Standard box and the "Identify" text are not produced (presentation; the values sheet).
- a-L2: lines 37 and 38 show 0 where the instructions say to leave them blank (the encoding's reading, stated in the line's note).
- a-L3: the federal joint filer whose spouse refuses to sign a joint New York return (p. 5) is not asked about.
- a-L4: an IT-2 record for foreign income without a W-2 is not covered.
- a-L5: the IT-225 question's examples (fixed under c-M7).
- b-L1: the "over 7 people" refusal also fired for single filers. **Fixed**: the gates now require a status other than single.
- b-L2: for married filing separately the household-credit range test uses the filer's own line 19; it misses a refusal only when the spouse's AGI is negative.
- b-L3: lines 77 and 80 would both count line 81 if it were ever nonzero; it is always zero (refused otherwise).
- b-L4, b-L5: covered by a-H3 and a-H1 above.
- c (lows): the spouse non-resident remedy wording for a spouse who lived in New York State but not the City (p. 15, line 51); the government pension and 414(h) help could name MTA, LIRR, MABSTOA, CUNY/SUNY optional retirement and military pensions; the MCTMT question could say the $50,000 test is per person and per zone; and the other lows in the report.

## Open item raised by the engine differential (step 6)

PolicyEngine-US selects the recapture of the tax table benefit by New York AGI alone; the printed worksheets select by
taxable income as well ("your taxable income (line 38) is $215,400 or less" for worksheet 7). Where New York AGI is
above a worksheet's taxable-income limit but taxable income is not, the two differ by up to several hundred dollars
(`reports/ny/2025/engine_differential.md`). The encoding follows the printed instructions. Whether the statute (Tax
Law § 601(d), not archived) agrees is listed for the owner in `docs/ny/INTEGRATION.md`.
