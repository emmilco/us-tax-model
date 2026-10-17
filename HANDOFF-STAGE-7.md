# Handoff: Stage 7 in progress — the integrity stack

Read `HANDOFF.md` first (what the project is; decisions not to reopen; hard
constraints). Then `spec/spec.md` sections 1, 2.4, 3 (requirement 11), 6.1,
6.5, 6.6 and `spec/design.md` section 5 (Stages 6–9), all amended this stage.
`PROJECT_INDEX.md` is current. `BUG_INVENTORY.md` is append-only and checked.

## Decisions made this stage (owner's, recorded in the spec)

- The product is the prepared, cited federal return the person files
  themselves; coverage grows toward most ordinary filers (spec 2.4), federal
  first, state returns only after federal. No filing or transmission, ever.
- The owner does no line-by-line reading and no hand-work. No human reading
  of the encoding against the source is claimed (spec 3, requirement 11).
  Trust rests on agreement among independent constructions (spec 6.5), each
  logged, with every disagreement recorded and ruled on.
- Every caught defect goes in `BUG_INVENTORY.md` (spec 6.6), append-only,
  enforced in `check-all`.
- Stage order: Stage 7 (integrity stack) before Stage 8 (household
  architecture test) before breadth. Stage 6 (TY2026) waits on IRS
  publication and runs alongside.

## Where Stage 7 stands

Done, in `check-all`:

- **Engine differential** (`tools/engines/`, report
  `reports/2025/engine_differential.md`): 1000 generated single-filer returns
  through PolicyEngine-US 2.49.4 and Tax-Calculator 6.8.5, 21,000 line
  comparisons, zero unexplained. Engines live in the git-ignored `.engines/`
  (`tools/engines/setup.sh`, the one network step); `check-all` skips visibly
  without them. Engine limitations are rules keyed by case features, listed
  in the report. Read `tools/engines/README.md` before changing it.
- **Transcription agreement** (`tools/transcription/`, logs in
  `reviews/2025/transcription/<form>.md`, one per form, all 26 adjudicated):
  an isolated Opus 5.5 call per form (`claude -p --setting-sources ""
  --tools "" --no-session-persistence --permission-prompts none`, verified
  tool-less) transcribes the form from its cited archived pages; the two
  transcriptions are compared per printed line and per exported helper after
  expansion and normalisation. `check_logs.py` fails `check-all` on a missing
  log, an open ruling, or a log made against a different source snapshot.
  Read `tools/transcription/README.md` before running it; a run costs about
  $0.25–0.55 per form in nominal usage and is a deliberate network step.

Not done (spec 6.5, design Stage 7):

1. **Render comparison** — an isolated model reads `rendered/2025/<form>.md`
   against the archived pages and flags lines whose English says something
   else. Same scaffold as transcription; not built.
2. **Class M hand-work** — branch-covering inputs worked on the archived
   worksheet by an isolated model, becoming class M fixtures. No input
   generator exists yet (design 2.10 promised one); `engine/src/compare.ts`
   has a random generator for the evaluator agreement that could seed it.
3. **Data-level properties** (spec 6.3, extended this stage): first concrete
   target is the Schedule D Tax Worksheet skip rule — a skipped line
   evaluates to zero under the project's reading and under unconditional
   computation (argued, not proved, in `reviews/2025/transcription/sdtw.md`).
   Others: deduction choice never worse; refusal never becomes a number; the
   chosen tax method never exceeds the ordinary computation.

Then Stage 8: one dependent, qualifying-child tests, head of household, the
child tax credit — the test of whether the atom vocabulary expresses
household predicates without `opaque` (stop condition: more than one line in
eight).

## Defects found this stage

- BUG-0001: Form 1040 line 9 summed line 3a (qualified dividends) in
  addition to 3b. Caught by the engine scout. Fixed; 13 fixtures corrected.
- BUG-0002: Tax Computation Worksheet row guards strict at the upper bound
  where the text reads "not over"; value-neutral (the worksheet is
  continuous at breakpoints) but contradicted the page and its rendering.
  Caught by the second transcription. Fixed; the checker's seam rule now
  requires exactly one side of a seam to include the seam point.

## Follow-ups recorded inside the transcription rulings (grep "records that")

- Schedule D lines 6/14 and the 28% worksheet line 5: a positive carryover
  must be subtracted (parentheses convention) when carryovers come into scope.
- Schedule D line filters must widen to boxes G–L when digital assets come
  into scope; `sd.filed` must then test the raw 1099-DIV boxes, not the
  netted worksheet results.
- Form 1040 line 1z must change when lines 1b–1h come into scope; Form 8995
  line 8 when line 7 can be nonzero.
- The transcription prompt's grammar has no `refuses` construct, so refusal
  gates always surface as disagreements; adding it would remove four
  standing rulings.

## Facts about the environment and tools

- `npm run check-all` is green at `0c80b0e`; takes several minutes (Lean
  build, mutation, the engine differential at ~30 s).
- `node engine/dist/main.js eval --batch cases.json` evaluates many returns
  in one process (added this stage).
- Transcription logs key their rulings to the exact expanded trees; a
  changed response or a changed normalisation reopens a ruling. Re-compare a
  saved response with `--from-response` (no model call) after changing the
  comparison. Rulings are written with `tools/transcription/rule.py`.
- Refetching a source changes its text hash and makes every log citing it
  stale; rerun those forms.
- Raw prompts/responses live in the git-ignored `.transcription/`; the engine
  work files in `.engines/work/`. The scratchpad virtualenv is gone; the
  real one is `.engines/venv`.
- Third-party datasets were assessed and set aside: IRS ATS scenarios give
  inputs only; TaxCalcBench's in-scope cases are all TY2024 single-filer
  wage returns; VITA answer keys are not public. See
  `research/03_source_material.md` (corrected this stage).

## How to work with him (unchanged, plus)

- Stop at decisions with more than one defensible answer; he answers in real
  time. Give an intent readback before multi-artifact builds.
- He will not read lines or hand-work fixtures; do not plan around it. He
  does want to be able to vouch for the process, so keep logs legible and
  provenance lines honest (inspected vs inferred).
- Commit coherent units with messages via `-F <file>`; no destructive git.
