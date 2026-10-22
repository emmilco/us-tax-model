# Handoff: Stage 12 (the Schedule 1-A deductions) done

Read `HANDOFF.md` first, then `TASKS.md`, then this file. `handoffs/HANDOFF-STAGE-11.md`
describes the stage before. `PROJECT_INDEX.md` is current; `BUG_INVENTORY.md`
has 43 entries.

## The roadmap changed this session

- Spec 2.4 now states the goal as coverage of **all** individual returns, measured
  over whole returns: 80% as the baseline, then 90 to 95% short of the genuinely
  exotic (owner). Stages go in the order of the coverage each gains.
- `tools/coverage/estimate.py` measures it: IRS Statistics of Income counts for tax
  year 2023 (six tables archived under `sources/2025/soi-*`), overlaps from
  PolicyEngine-US microdata (`.engines/data/`, `tools/coverage/fetch_microdata.sh`)
  raked to those counts. Report: `reports/2025/filer_coverage.md`. Estimated coverage
  after Stage 12: 33.9% (range 20.9% to 41.9%; 55 refusal gates unmeasured, T-034).
- `reports/roadmap.html` (from `tools/coverage/roadmap.py`) shows the ladder. Next
  rungs: married filers (to about 49%), self-employment (60%), other credits (67%),
  other Schedule 1 items (75%), Schedule E (82%).
- `tools/fetch_sources.py` archives spreadsheets (`xls`, raw file and hash) and
  Federal Register documents from www.govinfo.gov (owner approved the Federal
  Register; federalregister.gov blocks scripts, GovInfo is the GPO edition).

## Stage 12 scope (owner-confirmed)

All four parts of Schedule 1-A for unmarried filers (married is the next rung):

- **Tips** (employees): methods 1-3 of the instructions (Form W-2 box 7, Forms 4070
  total, box 14); one entry per employer (`forms/2025/tipjob.yaml`); an employer whose
  tips are not all qualified is refused; Form 4137 and trade-or-business tips refused.
- **Overtime** (employees): the employer-reported amount and methods 1-4, double time
  only for methods 3-4 (`forms/2025/otjob.yaml`); method 5, adjustments, other rates
  and special FLSA rules refused; overtime not in box 1 accepted.
- **Car loan interest**: one entry per loan (`forms/2025/carloan.yaml`), including
  refinanced loans, loans taken over at a death, more than two VINs and loans that
  also financed nonqualifying amounts, allocated pro rata under proposed
  § 1.163-16 (ratio six places, `amb.2025.carloan_ratio_places`); a refinancing of a
  partly qualifying loan is refused.
- **Seniors**: reuses `sa.age65` and `household.taxpayer_work_ssn`; the decedent who
  died in 2025 before 65 is refused.
- Each printed line of Parts II to V is $0 unless the part applies (owner, after
  class M). Married filing separately gets no tips, overtime or senior deduction.
- `scope.schedule1a` is retired; Form 1040 line 13b copies Schedule 1-A line 38.

## Evidence

- `fixtures/2025/stage12.json`: 51 cases predicted by hand, including the instructions'
  and the regulation's examples, every phase-out boundary, the joint amounts and the
  refusals.
- Engine differential: line 13b against PolicyEngine-US and Tax-Calculator; 0
  unexplained. Tax-Calculator now runs in exact mode and agrees with the printed
  $1,000 steps (and Schedule 8812's, so its `ctc_phaseout` exclusion is gone).
  Stated limitation: PolicyEngine-US's continuous phase-out.
- Reviews: transcription, render and class M of `s1a`, `tipjob`, `otjob`, `carloan`
  (and transcription/render of `f1040`, `scope`), all ruled; class M agrees on every
  value (s1a 344, worksheets 57).
- Mutation: no unexplained Schedule 1-A survivor (adjusted 96.7%; equivalences `s1aStepSkip`, `s1aOneEmployer`, `s1aPartGate` in `engine/src/mutate.ts`). Lean and TypeScript agree on 1,185 cases.

## Facts a fresh session needs

- Builders are in /tmp (`/tmp/s12/gen_s1a.py` writes `forms/2025/s1a.yaml`;
  `/tmp/s12/build_stage12.py` writes `fixtures/2025/stage12.json`). If /tmp is gone,
  edit the YAML and JSON directly.
- `classm-jobs` for Schedule 1-A needs a larger corpus:
  `node --max-old-space-size=24000 engine/dist/main.js classm-jobs --docs s1a --corpus 8000`.
- Locators citing documents other than IRS PDFs must name pages (`pp. N`) or the
  reviewers get no text (BUG-0041).
- `eval --batch` output for 1,000 generated returns is about 940 MB.
