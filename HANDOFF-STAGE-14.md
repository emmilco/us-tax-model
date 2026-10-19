# Handoff: Stage 14 (self-employment), in progress

Read `HANDOFF.md` first, then `TASKS.md`, then this file. `HANDOFF-STAGE-13.md`
describes the stage before and holds the owner-confirmed Stage 14 scope (its
"Next" section; TASKS.md T-039).

## Sources archived

Added to `tools/sources-2025.json` and archived by `fetch_sources.py`, each with
its printed revision recorded in the manifest:

- Forms and instructions: `f1040sc`, `i1040sc`, `f1040sse`, `i1040sse`, `f4562`,
  `i4562`, `f7206`, `i7206` (all 2025 revisions).
- Publications for 2025 returns: `p334` (small business), `p946` (depreciation),
  `p463` (car expenses), `p587` (business use of home), `p560` (SEP/SIMPLE).
- `n-25-05`: Notice 2025-5, the 2025 standard mileage rates.
- Statistics of Income: `soi-nonfarm-sp` (the sole proprietorship statistics
  page), `soi-23sp02is` (Table 2, income statements, tax year 2023) and
  `soi-20sp04ra` (Table 4, returns with Schedule C attached, tax year 2020).

Not yet archived: Notice 2026-11 (special depreciation for property acquired after
January 19, 2025), which Pub. 463 cites; whether Form 4562 needs it is a question
for the premise check.

## Feature prevalence (measured from the SOI tables)

The published tables do not count returns per Schedule C line; Table 2 gives
amounts only. The owner accepted dollar shares as the proxy for line-level
features, with the confirmed slice unchanged.

Table 2, tax year 2023, all nonfarm sole proprietorships (31,125,909 returns;
total business deductions $1,687.3 billion):

| Item | Amount ($ billion) | Share of total deductions |
|---|---|---|
| Cost of sales and operations (Part III) | 560.0 | 33.2% |
| Car and truck expenses | 150.2 | 8.9% |
| Depreciation | 77.9 | 4.6% |
| Home office, both methods | 14.4 | 0.9% |

Table 4, tax year 2020, individual returns with Schedule C attached (28,353,367):

| Item | Returns | Share |
|---|---|---|
| Self-employment tax (and its deductible part) | 18,492,379 | 65.2% |
| Qualified business income deduction | 12,499,340 | 44.1% |
| Schedule C net loss | 7,750,203 | 27.3% |
| Self-employed health insurance deduction | 2,503,312 | 8.8% |
| Payments to a Keogh plan (SEP, SIMPLE, qualified plans) | 739,308 | 2.6% |
| Married filing separately | 566,596 | 2.0% |
| Predetermined estimated tax penalty | 3,899,939 | 13.8% |

The estimated tax penalty is out of scope by spec (the tool says the IRS will
figure it). Net losses are common enough that the loss paths (Schedule SE, the
earned-income readers) are part of the build, not an edge case. These counts are
for 2020 and 2023; the 2025 shares are assumed similar.

## Owner rulings this stage

- **Prevalence proxy:** dollar shares from Table 2 stand in for per-line counts;
  the confirmed slice is unchanged.
- **Extraction check:** a PDFKit word equal to a poppler-only number plus a
  poppler-only digit counts as the same text (footnote markers in the car
  depreciation tables of Pubs. 463 and 946; BUG-0050, `BUG_INVENTORY.md` now has
  50 entries).
- **Form 4562 depth (option 3 of 3):** Part I (section 179: the dollar limit, the
  business income limit and the carryover), Part II (the special allowance, 100%
  for property acquired after January 19, 2025 and 40% before), Part III (MACRS
  general depreciation for 2025 property with the Pub. 946 tables and the half-year
  and mid-quarter conventions), and Part V (listed property, including vehicles on
  actual expenses and the 2025 passenger automobile limits). The limits are printed
  in `i4562` ("Limits for passenger automobiles": $12,200, or $20,200 with the special
  allowance, then $19,600) and `p463` ($7,060 for later years), so no further source
  is needed for them. - **Assets placed in service before 2025 (owner):** derived per asset, not entered
  as an amount: basis, date placed in service, property class, convention and the
  part already expensed (section 179, special allowance) are asked, and the 2025
  deduction is figured from the Pub. 946 tables (Form 4562 line 17, or Schedule C
  line 13 directly when no Form 4562 is required). Assets outside the tables (ADS,
  real property, property placed in service before 1987) are refused.

- **Prior-year carryovers (owner):** the section 179 carryover (Form 4562 line 10,
  from 2024 Form 4562 line 13) and a qualified business loss carryforward (Form 8995
  line 3) are taken as the amounts printed on last year's return, cited to that line,
  as the capital loss carryover already is.
- **Form 7206 (owner):** built, for more than one source of self-employment income
  and for qualified long-term care premiums with their age limits; Form 2555 and a
  Marketplace plan with the premium tax credit (Pub. 974) are refused.
- **Recovery class (owner):** Pub. 946's Table of Class Lives and Recovery Periods
  (Appendix B) is encoded, so an asset is classified from its asset class.
- **Second source for Pub. 946 Appendix B (owner):** a second independent
  transcription by a fixed-prompt `claude -p` run (the `tools/transcription`
  isolation), compared row by row with the project's parse of pp. 99 to 110, every
  difference settled against the PDF. The HTML twin carries Tables B-1 and B-2 as
  images, and their IRS text descriptions (`/media/168781`, `/media/168786`) return
  404, so no IRS rendering is available as a second source.
- **HTML twins (owner):** `p946-html` and `p463-html` are archived; pages the HTML
  cannot reproduce are listed in `tools/extraction/exceptions.json`. The HTML check
  ignores numbers, so the numeric tables get their second check elsewhere: MACRS
  rates against rates derived from the method and convention, the car limits
  between `i4562` and `p463`, Appendix B by the second transcription.
- **Vehicle depreciation reach (owner):** passenger automobiles (including trucks
  and vans) on actual expenses placed in service 2019 to 2025: the recovery-period
  years and a 2019 vehicle's first year after its recovery period, all derived from
  the vehicle's own facts. Vehicles placed in service in 2018 or earlier are refused
  (their deduction needs each earlier post-recovery year's business use, or `i4562`
  Tables 1, 3 and 4).
- **Form 4562 per business (owner):** `f4562` is a one-per-business entry under
  `sc` and reads its business's totals through the new enclosing-entry reference
  (spec 4.4); vehicles (`scveh`) and other property (`asset`) are entries under `sc`.
  Section 179 Part I is figured once per return; when the allowed deduction differs
  from the amounts elected for 2025, it goes to the only Schedule C on the return,
  and more than one Schedule C is refused in that case.
- **Settled by the text and earlier rulings:** line 16 covers SEP (Pub. 560, Deduction
  Worksheet for Self-Employed) and SIMPLE (Pub. 560 chapter 3); qualified plans with
  elective deferrals are refused. A vehicle switched from the standard mileage rate to
  actual expenses is refused. Form 461 is refused when it applies.
- **Build order (owner):** straight through, as in Stage 13: the whole premise check,
  Form 4562 included, then the build, then the reviews.

## Premise check against the archived text (in progress)

Each item was read in the archived 2025 text named; nothing is encoded yet.

**Confirmed amounts.** Schedule SE: 92.35%, the $400 filing floor, the $176,100
wage base (f1040sse lines 4a, 4c, 7). Standard mileage rate 70 cents (n-25-05 sec. 3;
i1040sc What's New and line 9). Simplified home office $5 per square foot, at most
300 (i1040sc Simplified Method Worksheet). Form 8995 thresholds $197,300 / $394,600
(f8995). Schedule 1 line 17 has its own worksheet in i1040gi, with Form 7206 only
under the exceptions of that line.

**Schedule C (i1040sc) items that need a screen or a refusal:**
- Line G "No" (passive activity, Form 8582) and line 32b (amounts not at risk,
  Form 6198).
- A loss on line 31 and Form 461 (excess business loss) above its threshold.
- Statutory employee (W-2 box 13): its own Schedule C, kept off Schedule SE line 2.
- Notary public fees (kept off Schedule SE).
- Accounting method other than cash; inventory kept under a method other than
  cost; a section 481(a) adjustment; capitalization under section 263A.
- Business interest subject to Form 8990 (not a small business taxpayer); line 12
  depletion; line 27a (Form 7205); Form 8941, 5884, 8844, 8932, 8994 credit
  reductions of lines 14 and 26.
- Line 6 recapture when listed property drops to 50% business use or less
  (Form 4797 Part IV).
- Line 9: actual expenses are required with five or more vehicles at once; the
  standard rate only if used in the vehicle's first year (owned) or for the whole
  lease; leased-vehicle inclusion amounts (line 20a, Pub. 463).
- Line 24b: 50% generally, 80% under DOT hours-of-service limits; standard meal
  allowance rates by locality (GSA) are not in the archive.
- Line 30, simplified method: gross income limitation (worksheet line 1 with the
  A to E computation when Form 8949 or 4797 gains or losses relate to the business),
  daycare reduction (line 3b worksheet), part-year or changed area (monthly
  average, under 15 days counts zero), shared use, more than one home (Form 8829
  for the others), actual expenses (Form 8829) refused.
- Qualified joint venture and community-property business (both spouses on a
  joint return; each files a Schedule C and SE for their share).
- Chapter 11 debtors, Form 1040-SS, extraterritorial income (Form 8873), installment
  sales of timeshares and lots (section 453(l)).

**Schedule SE (i1040sse) items that need a screen or a refusal:** church employee
income ($108.28 floor, lines 5a and 5b), ministers and Forms 4361/4029, partnership
earnings (box 14 code A), Conservation Reserve Program payments (line 1b),
farm income, the optional methods (Part II), community income on separate returns,
foreign social security agreements and exempt income abroad. On a joint return each
spouse with self-employment income files their own Schedule SE; the combined tax
goes on Schedule 2 line 4. Line 8 coordinates with each person's W-2 social
security wages (and tips) toward the wage base; the 0.9% Additional Medicare Tax
on self-employment income is figured on Form 8959 Part II.

## Findings during the build

- **MACRS percentage tables** (`tables/2025/macrs_gds.yaml`, 410 rates, extracted by
  `tools/extract_macrs_tables.py`): every column totals 100%; 388 rates equal the rate
  derived from the method and convention (each year on 1 less the printed earlier
  rates, half-up to the printed precision); two official columns depart from that rule,
  7-year mid-quarter Q2 (truncated, not rounded) and 20-year mid-quarter Q1 (year 2
  printed 7.000 where 7.008 is derived); the 66 half-year rates also printed in `i4562`
  Tables A and B agree (`tools/check_macrs_tables.py`, `reports/2025/macrs_tables.md`).
  The two departing columns are to be included in the second transcription.
- **Passenger automobile limits** (`tables/2025/auto_limit.yaml`,
  `auto_limit_first_nobonus.yaml`): every cell agrees with Pub. 946 (PDF and HTML) and
  Pub. 463 (`tools/check_auto_limits.py`). The two publications disagree on the
  first-year limit without the special allowance for a vehicle placed in service in
  2020 (Pub. 946 footnote 5, $10,200; Pub. 463 groups 2019-2020 under footnote 6,
  $10,100). No 2025 computation reaches that limit (only 2025 vehicles' first year
  and a 2019 vehicle's unrecovered basis use a first-year limit, and both publications
  agree on those), so the table holds only those two rows.
