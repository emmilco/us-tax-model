# Handoff: Stage 14 (self-employment), complete

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
- **Earlier vehicles with a special allowance (owner):** a vehicle placed in service
  2019 to 2024 that took a special depreciation allowance in its first year is refused;
  Pub. 946's automobile worksheet (later years, line 16 "Enter -0-") and its general rule
  (unadjusted basis "reduced by ... Any special depreciation allowance taken") conflict
  (ambiguity register).
- **Mid-quarter test on a joint return (owner):** both spouses' property placed in
  service in 2025 is compared together, as one return (ambiguity register).
- **Business-use percentage (owner):** business miles over total miles to six decimal
  places, half-up (the `prorate` atom; ambiguity register).
- **Settled by the text and earlier rulings:** line 16 covers SEP (Pub. 560, Deduction
  Worksheet for Self-Employed) and SIMPLE (Pub. 560 chapter 3); qualified plans with
  elective deferrals are refused. A vehicle switched from the standard mileage rate to
  actual expenses is refused. Form 461 is refused when it applies.
- **Build order (owner):** straight through, as in Stage 13: the whole premise check,
  Form 4562 included, then the build, then the reviews.

## Premise check against the archived text

Each item was read in the archived 2025 text named, before the build.

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

## What changed

- **Forms** (`forms/2025/`): `sc` (Schedule C, one entry per business under each person:
  Parts I to III, the simplified home office, Form 7206, the business's Form 4562 totals and its
  QBI), `scveh` (vehicles: standard mileage, actual expenses, leases, the Pub. 946 automobile
  worksheet and a 2019 vehicle's first year after recovery), `asset` (other property: class
  from Pub. 946 Appendix B, section 179, the special allowance, MACRS by the tables, earlier
  property and listed property), `ltc` (Form 7206 line 2), `s179` (Form 4562 Part I once per
  return), `mq` (the mid-quarter test), `f4562` (per business; see T-030), and the `se`
  definition (Schedule SE, bound per person). `person` gains Schedule SE, SEP and SIMPLE (Pub.
  560), Form 7206 per person and EIC Worksheet B; Schedule 1 lines 3, 15, 16, 17; Schedule 2
  line 4; Form 8959 Part II; Form 8995 business income and the loss carryforward; EIC Worksheet B
  and Schedule 8812's earned income readers.
- **Atom and engine:** `keyed_lookup` (owner), enclosing-entry references, enum parameters,
  definitions bound per instance; Lean evaluates them alike.
- **Tables:** `tables/2025/` MACRS rates, recovery years, passenger automobile limits, class
  lives, quarter conventions, SIMPLE catch-up and long-term care limits, each with its own check.
- **Review tools:** the transcription comparison qualifies a printed number several worksheets
  of one form share (BUG-0054); the return generator draws businesses and class M works
  collection entries with rates and definitions bound to several lines (BUG-0061).

## Fixed by this stage's reviews

BUG-0053 (Schedule 8812 line 21, one-half of the Additional Medicare Tax on self-employment
income), BUG-0055 (line 18a below zero at the Earned Income Worksheet stop), BUG-0056 (citations
without pages, so the reviews saw no Pub. 560, i8995, i1040gi Schedule 1 lines 15 to 17 or i7206
text), BUG-0057 (line 27c at the Worksheet B line 5 STOP), BUG-0058 (car loan interest on Schedule
C subtracted twice), BUG-0059 (worksheet line 19 unknown for a 2019 vehicle), BUG-0060 (the home
office deduction above line 29 with a section 179 carryover), BUG-0062 (section 179 on a separate
return, refused, owner), BUG-0063 (the long-term care limit across businesses, screened, owner),
BUG-0064 (the material participation question left out line G's oil and gas exception), BUG-0065
(sixty i4562 citations and four i1040sc citations named the wrong page; the transcription and
render reviews of the four affected forms were rerun). Review tooling: BUG-0054 (the transcription
comparison paired lines that share a printed number) and BUG-0061 (class M could not choose a case
for the Stage 14 documents).

## Evidence

- `fixtures/2025/stage14.json`: 130 cases, each predicted by hand from the archived text
  before recording (the derivation is in its evidence note), all matching; 770 fixtures in all,
  with 668 command-line integration runs.
- Engine differential: 1,700 generated returns (from 1,400; the generator now draws
  businesses), 62,900 line comparisons, 0 unexplained, 4 explained.
- Lean and TypeScript agree on all 1,370 compare cases (1,416,654 line values), business
  returns included.
- Properties: 6 of 6 hold over 400 generated returns, businesses included.
- Mutation: 1,664 mutants, adjusted 98.0% (raw 91.5%); no new unexplained survivor, and three
  earlier Form 8959 survivors are now killed. Of the three this stage's lines first left, two
  are killed by fixtures (`stage14.s8812.eiw_zero_with_se_tax`, Earned Income Worksheet line 3
  exactly zero with self-employment tax; Schedule 8812 lines 22 and 23 added to
  `stage14.f8959.se_above_threshold`) and one is a reasoned equivalence
  (`boundary.eic.eic.wsb_4b_positive` in `engine/src/mutate.ts`: at Worksheet B line 4b = 0,
  Step 5 question 3 holds because every EIC limit is positive).
- Reviews (paid `claude -p`, fixed prompt): transcription and render of the 22 new and
  changed forms, class M of `asset`, `ltc`, `s179`, `sc`, `scveh` and `se` (`f4562` exempt
  until T-030, printed by `check_logs.py`); 750 rulings in the logs, every one in a sidecar.
  Cost about $70 (the session's running tally, including the BUG-0056 and BUG-0065 reruns).
- Coverage estimate: 58.0% of returns (range 50.8% to 71.9%), from 47.8%.

## Open for the owner

- **T-046:** the agent reading `amb.2025.vehicle_s179_claimed`.
- **T-045, next (owner): year-readiness**, so that adopting TY2026 and later years is a reviewed
  worklist of what changed (TASKS.md). The roadmap pauses until it is done.
- **T-044:** a citation-page check in `check-all`, and review logs that notice a changed form.
- T-040: reading-order text of Pub. 946 pp. 98, 109 and 110.

## After the close (owner decisions on T-041 to T-043)

- **T-041:** the owner accepted six Stage 14 readings; the seventh became T-043.
- **T-043, the section 179 carryover (owner adopted):** researched from the archived statute,
  regulations and P.L. 119-21 (`ambiguities/research/amb.2025.s179_carryover_no_property.md`).
  Form 4562 line 1 is the $2,500,000 the line 1 instruction states, not the optional Worksheet
  1's smaller of that and the cost of 2025 property. A carryover is then deducted up to the
  unused dollar limitation and the business income limit, as 26 U.S.C. 179(b)(3)(B) provides.
  On a separate return line 5 is 50% of the limitation.
- **T-042, fully deductible meals (owner: the most rigorous and accurate option):** a third meals
  input on each Schedule C, deducted in full on line 24b. It covers the two cases the instruction
  names and the other exceptions Pub. 463 lists (`amb.2025.meals_full_exceptions`).
- **BUG-0066:** i4562 and i1040sc citations one page early, for headings BUG-0065's check did not
  match; all corrected after a page-by-page check against the PDFs.
- New sources: `usc-26-179`, `cfr-26-1-179-2`, `cfr-26-1-179-3`, `plaw-119-21`, `i4562-2024`
  and `p15` (the 2025 edition).
- **Found by the `sc` and `s179` review reruns, fixed:**
  - BUG-0067: the line 1 question asked for every Form 1099-MISC amount.
  - BUG-0068: class M jobs did not give a business its person's Schedule SE line 13.
  - BUG-0069 (owner: refused): the 300 square feet of the simplified method applied per business,
    not per person.
  - BUG-0070 (owner: refused through the Schedule C screen): the filer's own dependent care
    assistance contributions, deductible after Form 2441.
- **T-030, entry lines on the values sheet (owner's choices):** each collection entry has its own
  section, nested under its parent; the Lean evaluator evaluates every entry line and the compare
  harness compares all of them; `display` is allowed on collection lines again, and Simplified
  Method Worksheet lines 10 and 11 are back. Each Schedule C has one implicit Form 4562 (spec 4.4),
  printed after it even with no property; an asset shows only the lines Form 4562 reports it on:
  6(c), 14, 19(c) and 19(g) for 2025 property that is not listed, 17 for earlier property, 25, 26(h)
  and 26(i) for listed property (`shown_when`, spec 4.3). `eval --json` still carries every
  computed value. Six document titles that no longer described their documents were corrected.
- **Found by the T-030 review reruns, fixed:** BUG-0071 (the renderer printed an Enum parameter as
  money, which the Stage 14 `asset` and `scveh` render reviews saw) and BUG-0072 (owner: a vehicle
  converted from personal use during 2025 is refused). Class M jobs now leave out an entry's lines
  that `shown_when` hides, and a document without branches is worked on a case with nonzero
  amounts; Form 4562 has its first class M log. T-046: an agent reading for the owner.
- Run `node engine/dist/main.js classm-jobs --docs <doc>` before `classm.py` after any data
  change; the jobs file is not checked for age (T-044).

## Facts a fresh session needs

- Entries: `person[p].sc[k]`, `person[p].sc[k].scveh[v]`, `...sc[k].asset[a]`, `...sc[k].ltc[l]`;
  rosters `$sc@person[p]`, `$scveh@person[p].sc[k]` and so on. Section 179 Part I is the root
  form `s179`; a business reads it and the return reads the businesses.
- Every line of every collection entry is evaluated by both evaluators and printed in the entry's
  own section of the values sheet; a Form 4562 is an implicit entry of each Schedule C, and an
  asset's printed lines are shown only where Form 4562 reports that asset (`shown_when`).
- `choose` selects money only; a sign test on a signed line goes through a Bool helper (interval
  guards must start at a finite bound).
- A printed number shared by two worksheets of one form is compared as `"<number> (<line id>)"`
  in the transcription and render logs.
- The fixture builders used this stage live in `/tmp/s14/fx` (`lib.py`, `groupA.py` ...); if
  /tmp is gone, edit `fixtures/2025/stage14.json` directly.
