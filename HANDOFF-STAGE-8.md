# Handoff: Stage 8 done; extraction made evidence; next, the commit guard

Read `HANDOFF.md` first (what the project is; decisions not to reopen; hard
constraints), then `TASKS.md` (everything known and not done), then this
file. `HANDOFF-STAGE-7.md` describes the integrity stack in detail;
`PROJECT_INDEX.md` is current; `BUG_INVENTORY.md` has 24 entries. Everything
is committed; `npm run check-all` is green at `0c8872a`.

## Where the project stands

- Stages 7 (integrity stack) and 8 (dependents, head of household, Schedule
  8812, the `round` atom) are complete. Coverage: a single filer, or a single
  parent filing head of household, with wages, interest, dividends, securities
  sales, itemized deductions, the additional Medicare and net investment
  income taxes, the foreign tax credit by election, excess Social Security
  withholding and the three dependent credits. Married statuses, Schedule 1,
  other credits, carryovers, digital assets and the earned income credit are
  refused with citations.
- Mutation score 89.3% raw, 95.0% adjusted; no unexplained survivor on the
  Stage 8 lines. Fixtures 344 through the command-line program; evaluator
  agreement and engine differential clean.

## What this session did (2026-10-17, after the Stage 8 commit)

1. **Stage 8 fixtures** (`fixtures/2025/stage8.json`, 24 cases): the dependent
   tests, head of household tests and the Schedule 8812 chain across their
   branches and refusals; every asserted Boolean and key amount was predicted
   by hand before recording, and the notes say where the engine corrected the
   prediction.
2. **Mutation tool**: equivalent mutants are classified by rules recomputed
   every run (copy-chain identity, shared-gate identity, and a register whose
   entries hold only while the structural facts they cite hold). A negative
   test confirmed an entry lapses when its facts change.
3. **Rulings as data** (`<form>.rulings.json` beside each review log,
   `tools/transcription/rulings.py`): the three review tools read kept
   rulings from the sidecar; `rule.py` writes both; `check_logs.py` verifies
   agreement; `--prune` drops entries whose disagreement no longer occurs.
   This replaced regex parsing of the markdown logs, which lost rulings on
   rerun (BUG-0016).
4. **Extraction as evidence.** The archived text was one unchecked
   `pdftotext -layout` pass whose two-column pages were spliced line by line.
   Now:
   - `tools/extract_text.py` writes reading-order text (`<id>.cols.txt`) from
     word boxes with a per-page classification (`<id>.pages.json`: prose,
     table, mixed, single); `fetch_sources.py --derive` rebuilds both and the
     plain run verifies every hash.
   - The review tools give the model reading-order text for prose pages and
     layout text otherwise, recording both hashes; `check_logs.py` checks both.
   - `tools/check_extraction.py` runs in `check-all`: layout and reading-order
     text agree character for character; PDFKit (an independent reader, via
     `tools/extraction/pdfkit_text.swift`) finds no word poppler lacks; every
     word of an instruction booklet's pages occurs in the IRS's HTML
     publication. Accepted differences carry reasons in
     `tools/extraction/exceptions.json`; report `reports/2025/extraction.md`.
   - `tools/ocr_audit.py` read every page with Tesseract once; the residue is
     OCR behaviour, adjudicated in `reviews/2025/extraction/ocr_audit.md`.
   - `tools/extraction/page_review.py` builds a local page-by-page view (page
     image beside the text the model reads) in the git-ignored
     `.extraction-review/`; the owner uses it as the court of last appeal.
5. **All 74 reviews rerun** on the new text (`tools/transcription/rerun_all.py`,
   about $20 by the CLI's estimate, 6 at a time, 15 minutes). Class M agreed on
   every computed line. The rerun exposed eight defects (BUG-0017 to BUG-0024)
   in the dependents worksheet and the credit refusals, all fixed and
   re-reviewed. "Younger than you" is now a question; `household.taxpayer_age`
   no longer exists.
6. `research/07_text_extraction_prior_art.md` records what was taken from the
   other extraction pipeline (principles only; it is not a dependency).

## Facts a fresh session needs

- Rerun a review with `tools/transcription/rerun_all.py --kinds ... --forms ...`;
  a tool exit of 3 means disagreements to rule, not a failure. Rule with
  `rule.py` (writes log and sidecar); a disagreement identical to one already
  ruled keeps its ruling automatically. After reruns, `rulings.py --prune`.
- Any change to an archived text or to `extract_text.py` (bump
  `TOOL_VERSION`, run `fetch_sources.py --derive`) changes hashes that every
  review log pins, so every review must be rerun.
- The model occasionally returns malformed YAML (one render run failed on a
  stray parenthesis); rerun the tool once before investigating.
- Review calls go through `claude -p` with no tools (fixed-prompt,
  curated input, no action surface); Tesseract and poppler are Homebrew
  installs.
- The stale sidecar pruning is deliberate: git history holds the old rulings.
- `.extraction-review/` is 233 MB and regenerable; do not commit it.

## Open items (see TASKS.md)

- T-021 commit guard: every commit this session was made by reading the
  suite's exit line by hand.
- T-015 class M for collections and shared definitions.
- T-018 earned income credit (Stage 9), T-011 the 2026 refetch (rerun every
  review and the OCR audit then).
- Per-band gutters for mixed pages (Paperwork Reduction Act notice, index):
  the reading-order text of those few pages still interleaves inside a block;
  the reviews use the layout text for them.

## How to work with him (unchanged)

- Stop at decisions with more than one defensible answer; give an intent
  readback before multi-artifact builds; he answers in real time, and when
  away he will adjudicate readings against the page through the page review.
- He will not read lines or hand-work fixtures. Keep logs legible and
  provenance lines honest (inspected vs inferred).
- Commit coherent units with messages via `-F <file>`; no destructive git.
