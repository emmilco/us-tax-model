# Handoff: Stage 8 done; next, fixtures for the new lines

Read `HANDOFF.md` first (what the project is; decisions not to reopen; hard
constraints), then `TASKS.md` (everything known and not done), then this
file. `HANDOFF-STAGE-7.md` is the previous handoff and still describes the
integrity stack in detail; `PROJECT_INDEX.md` is current; `BUG_INVENTORY.md`
has 15 entries. Everything is committed; `npm run check-all` is green at
`10e45cb`.

## Where the project stands

- Stage 7 (integrity stack) complete: engine differential, transcription
  agreement, render comparison, class M hand-work, data-level properties,
  evaluator agreement, mutation, coverage and evidence, all in `check-all`.
- Stage 8 (household architecture test) complete and committed: `dependent`
  (root collection; Steps 1–5 of Who Qualifies as Your Dependent per listed
  person; credit eligibility; head of household Tests 1 and 2), `household`
  (filer facts and the head of household gate on Form 1040 line 12e),
  `s8812` (Schedule 8812 Parts I, II-A, II-B with Credit Limit Worksheet A
  and the Earned Income Worksheet). Zero `opaque` lines; the coverage report
  publishes the share. The `round` atom was in the vocabulary but implemented
  nowhere and now exists across the stack (Lean proofs: T-017).
- Coverage: a single filer (or single parent filing head of household) with
  wages, interest, dividends, securities sales, itemized deductions, the
  additional Medicare and net investment income taxes, the foreign tax credit
  by election, excess Social Security withholding, and the three dependent
  credits. Married statuses, Schedule 1, other credits, carryovers, digital
  assets and the earned income credit are refused with citations.

## The accepted next step (T-020)

Drive the mutation score back up on the Stage 8 lines: it fell from 89% to
83% (88% adjusted) because the new lines have few fixtures. Run class M on
`s8812` again after the fixes (`node engine/dist/main.js classm-jobs --docs
s8812` then `tools/transcription/classm.py --doc s8812`; the existing log and
cases predate BUG-0011 to BUG-0015 but their inflowing values did not
change), write fixtures that assert the dependent worksheet's per-person
lines across its branches (the generator reaches them; the fixture format is
`fixtures/2025/stage*.json`), and read `reports/2025/mutation.md` for the
surviving mutants on `dependent`, `household` and `s8812`. Class M for
collections (T-015) would cover `dependent` directly and is the larger
version of the same work.

## Facts a fresh session needs

- The Stage 2 interview check enumerates every Boolean and enum input of a
  Stage 2 fixture; give that fixture no household or dependent inputs
  (T-016 bounds it properly). The other interview checks walk fixtures.
- Every interview file now has the dependent roster and the 26 new
  questions; the fixture cases that walk the sales and later interviews carry
  `$dependent`, household and Schedule 8812 answers; earlier head of
  household fixtures carry a child who is a dependent through the
  Canada/Mexico rule but earns no credit, so their values hold.
- Engines: children and head of household are mapped in both adapters. Line
  19 is compared with PolicyEngine as `min(ctc, ctc_limiting_tax_liability)`;
  Tax-Calculator's random credit take-up is disabled by policy parameter;
  its unrounded phase-out and PolicyEngine's dependency test for 17–23-year-
  old students are feature-keyed limitations. Zero unexplained at 1,000
  cases.
- Official examples in the Schedule 8812 instructions and the dependents
  section are qualitative; no class A arithmetic fixture exists for the
  credit.
- Model runs cost about $0.10–0.60 per document per construction. Rerunning
  any of them reopens the rulings whose keys change.

## Process note

The Stage 8 commit `2c3ab39` was made while `check-all` was failing on the
mutation step, because the commit was chained on a log grep instead of the
suite's exit code; `10e45cb` fixed the cause and is the first green point.
Commit only after reading the suite's exit line (T-021 proposes a guard).

## How to work with him (unchanged)

- Stop at decisions with more than one defensible answer; give an intent
  readback before multi-artifact builds; he answers in real time.
- He will not read lines or hand-work fixtures. Keep logs legible and
  provenance lines honest (inspected vs inferred).
- Commit coherent units with messages via `-F <file>`; no destructive git.

## After T-020 (same day)

- `fixtures/2025/stage8.json`: 24 cases over the dependent tests, the head of
  household tests and the Schedule 8812 chain; every asserted Boolean and the
  key amounts were predicted by hand before recording, and the evidence notes
  say which predictions the engine corrected. Raw mutation score 83.3% to
  89.3%; adjusted 88.1% to 95.0%.
- The mutation tool classifies equivalent mutants by three mechanisms, all
  recomputed every run: copy-chain identity, shared-gate identity (a sum
  whose gated operands are identical), and a register whose entries hold only
  while the structural facts they cite hold in the data (`EQUIVALENT_IF`).
  No survivor on the Stage 8 lines is unexplained.
- Class M on `s8812` was rerun ($0.52): the same four cases and the same 15
  disagreements, all the model declining to fill lines after a printed "Stop
  here". Two `s8812` branches are unreachable by a computed generated case
  (the combat pay and Puerto Rico refusals).
- BUG-0016: all three review tools lost standing rulings on rerun when a
  disagreement followed an agreement (87 of 235 rulings in the committed logs
  would have been lost). Fixed in the parsers; before this fix, a reopened
  ruling after a rerun was not evidence that the key had changed.

## Extraction made evidence (same day, after the T-020 work)

The single `pdftotext -layout` pass that every encoded line and every model
review rested on is now checked and no longer the only reading:

- `tools/extract_text.py` writes reading-order text (`<id>.cols.txt`) beside the
  layout text of every archived PDF, from poppler's word boxes: gutters are
  found per page from word coverage (two or three columns), lines poppler ran
  across a gutter are split, bands are read column by column, hyphenated line
  breaks are rejoined only where geometry says the next line continues the
  word, and icon labels (TIP, CAUTION) stand alone. `<id>.pages.json` classifies
  each page as prose, table, mixed or single; `fetch_sources.py --derive`
  (re)builds both and records their hashes, and the plain run verifies them.
- The review tools give the model the reading-order text for pages classified
  as prose and the layout text for the rest, and their logs record both hashes;
  `check_logs.py` verifies both. Every review log predates this and must be
  rerun (the accepted plan: rerun all 74).
- `tools/check_extraction.py` runs in `check-all`: layout and reading-order text
  must agree character for character; PDFKit (an independent reader of the text
  layer) must find no word poppler lacks; every word of an instruction booklet's
  pages must occur in the IRS's HTML publication of it. Accepted per-page
  differences carry reasons in `tools/extraction/exceptions.json` (the QBI flow
  charts and loss worksheet, the sample check: images in the HTML). Report:
  `reports/2025/extraction.md`. Building the checks found and fixed four
  extractor defects (negative page coordinates, table-header and index
  rejoins, merged column lines), none in the archived layout text.
- Rulings live in `<form>.rulings.json` beside each log (T-024).
- All 74 reviews were rerun on the new text (`tools/transcription/rerun_all.py`);
  the rerun found BUG-0017 to BUG-0024 on the dependents worksheet and the
  credit refusals, all fixed and re-reviewed. `tools/extraction/page_review.py`
  builds a local page-by-page view (image beside the text the model reads) for
  a person to judge a reading against the page.
