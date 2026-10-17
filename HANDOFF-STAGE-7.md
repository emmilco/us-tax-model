# Handoff: Stage 7 in progress — the integrity stack

Read `HANDOFF.md` first (what the project is; decisions not to reopen; hard
constraints), then `TASKS.md` (everything known and not done). Then `spec/spec.md` sections 1, 2.4, 3 (requirement 11), 6.1,
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

- **Data-level properties** (`engine/src/properties.ts`, report
  `reports/2025/properties.md`, `node engine/dist/main.js properties`,
  `PROPERTY_RUNS` to change the 400-case default): five properties of spec
  6.3 over fast-check-generated returns in every filing status, each with
  an "applicable" count so a property cannot pass by never applying. The
  Schedule D Tax Worksheet skip rule is now machine-checked (the argument in
  `reviews/2025/transcription/sdtw.md` stands; lines 1 = 32 with 1 ≠ 16 is
  exercised only by the investor profile); tax bounds and method never above
  the ordinary computation; the deduction choice never worse; a refusal never
  becomes a number; tax monotone in wages. The generator
  (`engine/src/generate.ts`) covers every declared input and reports which
  branches the corpus reaches; the unreached ones at 400 cases are the
  structural ones the fixture coverage report also exempts, plus the narrow
  band where the worksheet tax exceeds the ordinary tax (`qdcg.line25:right`,
  `sdtw.line47:right`), which class M should target.

- **Render comparison** (`tools/transcription/render_compare.py`, logs in
  `reviews/2025/render/<form>.md`, all 26 adjudicated, about $0.10–0.40 per
  form): an isolated model judges each printed line's rendered English
  against the cited pages (MATCH / MISMATCH / UNCLEAR with a reason). Built
  on the transcription scaffold; `check_logs.py` holds both log sets to the
  same rules and `rule.py --kind render` writes rulings. The renderer now
  names helpers by label, qualifies shared printed markers by id, and words
  def references and counts readably; the excerpt builder now also gives
  pages a locator names for another document, refusal citations, and
  parameter citations. It found eight defects (BUG-0003 to BUG-0010): one
  copied helper label, six scope screens narrower than the lines they stand
  in for or not wired to the line, and one expression that dropped a refused
  line (QBI taxable income before the deduction omitted Form 1040 line 13b).
  None changed a value on any fixture or generated return. Standing rulings
  are mostly scope (digital assets, Forms 4797/2439/6252/K-1, carryovers,
  Form 2555) and representation (derived questions, cross-form wiring).

- **Class M hand-work** (`engine/src/classm.ts` chooses the cases,
  `tools/transcription/classm.py` runs them; logs in
  `reviews/2025/classm/<doc>.md`, fixtures in `fixtures/2025/classm.json`):
  for each of the 15 non-collection documents with printed computed lines, a
  greedy cover of every branch a computed case can reach, worked by hand by
  an isolated model from the document's pages and the amounts flowing into
  it. 39 cases, 889 lines worked, 882 agree; the 7 disagreements are all
  blank-versus-computed on skipped parts or lines (Form 8959 parts the
  filer skips, Schedule D line 20 after a loss, Schedule D Tax Worksheet
  lines 41–43 after the line-19 skip), ruled and dropped from the fixtures.
  Cost about $4.50 for all 15. Collections and shared definitions have no
  class M cases yet (T-015).

Stage 7's constructions are all built. Its done-when still wants class M
for the collection documents and definitions (T-015) and the evidence report
free of computed lines without an asserted fixture; check the report.

Then Stage 8: one dependent, qualifying-child tests, head of household, the
child tax credit — the test of whether the atom vocabulary expresses
household predicates without `opaque` (stop condition: more than one line in
eight).

## Defects found this stage (BUG_INVENTORY.md has the detail)

- BUG-0001: Form 1040 line 9 summed line 3a (qualified dividends) in
  addition to 3b. Caught by the engine scout. Fixed; 13 fixtures corrected.
- BUG-0002: Tax Computation Worksheet row guards strict at the upper bound
  where the text reads "not over"; value-neutral (the worksheet is
  continuous at breakpoints) but contradicted the page and its rendering.
  Caught by the second transcription. Fixed; the checker's seam rule now
  requires exactly one side of a seam to include the seam point.
- BUG-0003 to BUG-0010: found by the render comparison and by reading the
  renderings while building it. Pattern worth watching: a scope screen
  written from the lines it gates on one form, narrower than the instruction
  text of a line it also stands in for (five of the eight).

## Follow-ups

All tracked in `TASKS.md` (one row per item, with source and trigger). The
rulings still carry the sentence that raised each one.


## Facts about the environment and tools

- `npm run check-all` takes several minutes (Lean build, mutation, the
  engine differential at ~30 s); the properties step takes about a second.
- `node engine/dist/main.js eval --batch cases.json` evaluates many returns
  in one process (added this stage).
- Render logs key their rulings to (printed line, restatement, model
  reason); a renderer change that alters a restatement, or a new response,
  reopens them. A rerun costs about $3 for all 26 forms.
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
