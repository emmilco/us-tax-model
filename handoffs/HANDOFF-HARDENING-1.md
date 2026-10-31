# Hardening, first pass (2026-10-29 to 2026-10-31)

After Stage 21 reached the first coverage goal (82.2%, commit a428e8b), the owner directed a hardening phase:
verification, loose ends and improvements to existing code, before Schedule E. This records what was done, what the
owner decided, what is open, and what a fresh session needs to know.

## Commits

| Commit | Content |
| --- | --- |
| a428e8b | Stage 21 (Form 5329); 80% goal; BUG-0200 to BUG-0206 (0206: the Lean gate key on an enclosing entry) |
| a4e593a | README edit by the owner on GitHub |
| 99300a8 | Owner's answers after Stage 21: `amb.2025.hsa_step4_other_limits`, exception 09's 120-day window; round 4 |
| 2ca3311 | T-067: worksheet lines hidden where the source skips them; BUG-0207 to BUG-0210; the bug root-cause analysis |
| 0fd59d3 | Source-coverage checks T-084 to T-089; the mitigation pressure test; the completeness experiment |
| 84fa330 | Screen and completeness sweep: BUG-0211 to BUG-0260; standing completeness review (T-090); evaluator fix BUG-0257 |
| a75729f | Hardening tasks T-068, T-070, T-072, T-073, T-074, T-076, T-078, T-079, T-081, T-083; BUG-0261 to BUG-0263 |

## What changed, in brief

- **Analysis.** `docs/2026-10-29_bug_root_cause_analysis.md` classifies all recorded bugs by root cause;
  `docs/2026-10-30_mitigation_strategy_pressure_test.md` tested the proposed mitigations against the bugs and ranked
  the strategy; `docs/2026-10-30_completeness_experiment/` showed that a model reading whole instruction sections
  finds rules nothing encodes (precision 62%, recall 3 of 3).
- **Checks in check-all** (after the build): `check_instruction_cites.py`, `check_operands.py`, `check_signs.py`,
  `check_consumers.py`, `check_limits.py`, `transcription/check_screens.py`, `transcription/check_completeness.py`,
  and quote verification outside computed lines in `citations.py`. All share `tools/baseline_check.py`.
- **Standing reviews.** Screens (`screen_review.py --screens`, merged into `screen_review.json`) and completeness
  (`completeness_review.py --forms`) are rerun when their prompt changes; their findings are ruled with the prompt hash
  they judge.
- **Defects fixed.** BUG-0206 to BUG-0263. The largest: qualifying surviving spouse was never tested (BUG-0219,
  $18,500 against $10,350 on the witness); an unanswered refusal gate let a count's lower bound decide a test so a
  return completed (BUG-0257, both evaluators and spec 4.7.5); about forty questions and screens missing a definition
  or a case.
- **Review tools.** Unparenthesised worksheet markers parse; the transcription comparison compares `shown_when`;
  class M of single documents skips hidden lines; triage keeps a completed-return witness sample
  (`triage.py --explain ... --completed`); the transcription prompt says other forms' fields are referenced by id.
- **Engines.** PolicyEngine compares Form 8962 lines 3, 8a, 11d, 11e and 26 (511 comparisons, all agree).

## Owner's decisions

- Baselines (all checks): existing findings are a baseline worked off over time, not cleared at once. A finding
  about one line comes due only when that line changes (line-level subjects; 2026-10-30). T-094 is the burn-down.
- Fix-and-review loop: fix medium and high findings at once and re-review those forms; batch low findings (T-092) for
  when each form next changes; stop when a round finds nothing medium or higher.
- T-066: class M moves to printed lines form by form; printed-only mode for single documents is the next step there.
- T-067: worksheet lines get printed markers (`(CLW A n)`) and may be hidden by `shown_when`.
- Form 2441 equal plan maximums: reading 1 kept (`amb.2025.dc_plan_maximum`).
- D5: left to the session; the ITIN-application deeming applies to the credit for other dependents only
  (`amb.2025.ctc_spouse_itin_application`).
- T-076 (2): visibility counts as a real disagreement in the transcription comparison.
- T-079 (3): the transcription prompt was reworded.
- T-093: closed; the documented limit of spec 4.7.5 stays.
- Order of work: the hardening backlog, then T-091 and T-092; Schedule E (Stage 17) after.

## Open

- **T-091**: three dependent-test logic changes (a spouse's relative on a joint return; temporary absence defined
  differently for head of household and the qualifying-relative test; the kidnapped screen's qualifying-relative branch).
- **T-092**: batched low findings, including a Form 8962 display question below 100% of the poverty line and the
  Form 8863 ITIN verdicts to check against Pub. 970.
- **T-094**: the baseline burn-down (152 instruction-citation findings, 24 operand gaps, 5 signs, 384 input–page pairs,
  67 limit sentences, 6 input quotes, 3 screens, 56 forms never completeness-reviewed). Each citation fix reopens the
  form's reviews; batch by form.
- Remainders: T-076 (3), (4); T-079 (2), (4); T-081 (3), (4), (5), (7); T-066 single-document printed mode; T-069
  (folds into T-094).
- Last question put to the owner, unanswered at close: take T-091 and T-092 next with T-094 as a standing burn-down
  (recommended), or work T-094 to completion first.

## Facts a fresh session needs

- **A new input ripples to five places**, all of which must answer it or check-all fails (missed three times):
  every fixture (`fixtures/2025/*.json`, inserted as text: stage4, 15 and 16 do not round-trip `json.dumps`), the
  interview bank and profiles (`interview/*.yaml`), `engine/src/generate.ts` (as `fc.constant`, so the seeded sample does
  not shift), `tools/engines/generate_cases.py`, and the partial-input banks `tools/transcription/input_contracts/`.
- **Ratchets ask to be emptied.** When a fix makes a baseline entry, a ruling or a listed exception obsolete, the
  check fails with "stale"/"no longer fails": remove the entry (e.g. `tools/refusal_reach_exceptions.json`).
- **Rulings are tied to reviews.** Screen and completeness rulings carry the `prompt_sha` of the review they judge; a
  rerun needs new rulings.
- **Review round workflow.** Archive the stale logs (`.transcription/archive/<name>/` with a MANIFEST), rerun with
  `rerun_all.py --kinds ... --forms ...` per family, run `triage.py` for both families, adjudicate with a brief
  (the current one is `.transcription/proposed/fixr2/BRIEF.md`, with sections per round), apply with `rule.py`, and
  check with `check_logs.py`. Rendered English changes on shared lines can stale a form's render log even when the
  form itself did not change.
- **Parallel agents** worked well with disjoint file ownership; only one agent may own new inputs and their ripple.
- **deepseek-flash** sometimes exhausts its output budget on render (sb): rerun with `--max-output-tokens 131072`.
- **The Stage 19 scratch generator** (`/tmp/s19/gen.py`, not in the repo) rewrites `person.yaml` from a pre-Stage-21
  copy; it is retired. Edit the YAML directly.
- A background review run failed once on transient macOS "Operation not permitted" errors (the machine locked or a
  privacy prompt); the files were readable again afterwards and the runs were simply repeated.
- `check-all` takes about 15 minutes (mutation is most of it); the pre-commit hook requires it green on the exact tree.
