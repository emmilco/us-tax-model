# Household closure — usage pause, 2026-11-01

## Closed — 2026-11-01

P0 is closed and committed (household closure commit, parent `f44bae4`). The remaining steps in this handoff were
completed: the four pre-commit checks, the offline check set, the documentation updates, and the full suite through
the tested-tree guard. The suite also caught that the hh4 render batch had reviewed a stale `rendered/` tree; the
rendered English was regenerated, the prior render receipts archived under
`.transcription/archive/before-render-refresh-2026-11-01/`, and the four render reviews rerun and ruled. `check_logs.py` reports 0 open; completeness passes at 92 findings (0 new, 55 deferred
baseline forms, 37 ruled) and consumers at 438 (0 new, 380 baseline, 58 ruled); T-114–117 are done; BUG-0272–0286
are recorded. The review and validation state below is the pause record, not the current state; see
`HANDOFF-NEXT-SESSION.md` for what follows. Do not rerun the interrupted DeepSeek batch: the current household and
f1040 render logs pass `check_logs.py`'s current subject and snapshot bindings, and the final rulings name them.

## Resume here (historical)

The owner explicitly stopped work because usage ran out and requested this handoff. **Do not start more work until the owner resumes.** The overall backlog and P0 household package are NOT complete. No commit, push, or full-suite success occurred. HEAD remains `f44bae4`; preserve the large existing working tree, including all untracked files. Do not reset, stash, clean, or restore older review files over it.

Read this handoff, `CLAUDE.md`, `docs/2026-11-01_backlog_plan.md`, and the standing decisions in `handoffs/HANDOFF-HARDENING-1.md`. The temporary plan is the approved priority/tracking document; TASKS.md is the permanent status authority. Coverage expansion remains last. Finish P0 before T-102/P1/P2 and the remaining form passes. Do not delete the tracker yet.

Owner chose the **narrow completeness baseline repair** rather than refreshing the entire deferred backlog. That repair is implemented, with exact prompt checks retained for actual reviews. It is not permission to accept stale receipts or rebaseline unrelated debt.

## Process shutdown

- Sent Ctrl-C to all known outstanding session handles. Most were already finished.
- Final DeepSeek batch session `85933` exited 130 when interrupted. Its transcription jobs had completed; render jobs may have been interrupted or written partial outputs. Verify receipts before using them.
- A process-table check outside the sandbox found **zero remaining matching project review processes** after interruption. No review jobs should be consuming usage.
- The last consumer-review invocation was aborted before starting: `.transcription/hh4-consumer-review.log` did not exist at inspection. Its one prompt exists; no response was collected.

## Authored household work now in the tree

Earlier changes, preserved from the prior Claude session:

- Quick-clearance work T-058/BUG-0270, T-149/BUG-0271, T-135, accepted owner decisions T-046/T-122/T-138, and explicit future decisions T-113/T-131.
- Household T-114–117: considered-unmarried tests, QSS kidnapping exclusion/remedy, TANF costs, services wording (BUG-0272–0275).
- Introduced wording corrections (BUG-0276), death-year screen (BUG-0277), ended-marriage community-property screen (BUG-0278).
- Inputs `household.spouse_died_2025`, `household.cp_married`; gate wiring and broad fixture/profile/generator ripple already present.

Added during this continuation:

1. **BUG-0279, narrow completeness debt repair.**
   - New `tools/transcription/completeness_debt.py`, `migrate_completeness_debt.py`, `test_completeness_debt.py`; checker integration in `check_completeness.py`.
   - Actual completed reviews and claim rulings still require exact current full prompt hashes, including HANDLED ELSEWHERE.
   - Never-reviewed legacy debt can retain its original baseline fingerprint only while its own canonical form, source sections, system prompt and reviewer implementation remain unchanged, and its verified migration record matches.
   - Independently exported/built historical `f44bae4801bc36934cfc361bf2d9f8c52884a8bf` at `/private/tmp/tax-baseline-d2ivf_kr`; reproduced all 56 old baseline hashes before migration. `deferred_debt` records live in completeness/rulings.json. Original baseline map was initially preserved. The f1040 entry was subsequently retired because it now has an actual review; 55 untouched forms remain deferred.
   - Four regression tests are included in the normal completeness self-test. Existing stale completed reviews cannot take this exemption.
   - README documents it. Review the implementation before final commit; it has targeted validation, not full-suite validation.
2. **BUG-0280, marriage definitions.**
   - `household.married` now explains recognized common-law/foreign/tribal marriages, final versus interlocutory divorce, legal separation, annulment, and partnerships/civil unions that are not marriage.
   - Keeps legal year-end marriage distinct from the spouse-death filing-status rule, because EIC and HSA consume this input.
   - Adds a separately labelled filing-status warning for divorce solely to file unmarried followed by intended/actual remarriage next year.
   - Cite additions repeat `p501 p. 6` on each semicolon segment: the parser does not inherit a previous segment's document ID. The first attempt omitted repeated IDs, and input-quote checking caught it; fixed before hh4 build/reviews.
3. **BUG-0281, consumer prompt generation.**
   - `tools/check_consumers.py --prompts` previously skipped changed baseline questions because the pair ID existed. It now compares the baseline subject hash.
   - The self-test exercises unchanged suppression and generation after a question change. It passed.
4. **BUG-0286, filing-status consistency check.**
   - New `household.filing_status_conflict`, refused at `f1040.line12e`.
   - True for Single + year-end married Yes, or MFJ + year-end married No + spouse died in 2025 No.
   - Joint death-year returns remain supported; HOH/QSS keep their separate tests. This is an **entry** check in coverage/tree.json, not a new excluded situation.
   - Death-year input wording now also covers a joint filer who was not married at year end. No new input ID.
   - Six source-predicted `stage21.household.status_*` fixtures: valid/conflicting Single and MFJ, joint death-year, married HOH. Existing eight `stage21.household.*` widow/community cases remain.
   - Seventeen older Claude ClassM cases had MFJ + married False + no death-year fact as unused context. Corrected only that marriage input to True and annotated the host repair; all expected values and original model receipts are unchanged. Do not claim new independent evidence credit. Some current raw `.classm/` prompts have been overwritten since original receipt hashes, so do not assume every current prompt is the original one. These 17 cases do not target HSA/EIC, the consumers of this marriage input.

## Explicitly deferred existing definition debt

Fresh completeness reviews repeated older low findings. These are NOT fixed or certified as implemented/refused merely to clear review checks:

- BUG-0282: remaining dependent support-definition details, T-107/T-109 expanded to include the full residual list. Dependent form pass.
- BUG-0283: other-claimant question does not exclude non-filer/refund-only/non-taxpayer cases; existing over-refusal. New T-153, dependent pass.
- BUG-0284: explicit daily/mixed-purpose care-expense allocation and child-support wording. New T-154, dependent/f2441 passes.
- BUG-0285: issued versus merely applied-for student TIN for lifetime learning. Existing owner decision T-113 schedules dependent and person together; AOC deeming stays supported.
- T-111 still covers the dependent TANF sibling; the household half is fixed. T-106 still requests explicit newborn hospital wording, currently covered in substance by the medical-care absence rule.

These bug entries explicitly state deferred/open status and no new numerical evidence. Preserve the owner's rule: fix newly introduced defects at any severity; fix medium/high findings immediately; older lows may follow their scheduled form passes.

## Validation actually observed

On the latest authored gate/wording tree:

- `.transcription/hh4-build.log`: build OK.
- `.transcription/hh4-render.log`: rendered 68 files.
- `.transcription/hh4-fixtures.log`: **1,425/1,425 CLI fixtures passed**.
- Six new status cases exactly matched source-predicted gates/refusals/deductions in `.transcription/hh4-status-actual.json`.
- Refusal fixture metadata initially used a text hash, then incorrectly a reading-order hash. Inspected `engine/src/build.ts:74`: `snapshot` is **manifest `sha256` (PDF hash)**. Corrected expected metadata from that field; no amounts, gates or remedies were taken from evaluator results. This is recorded with the two failed hypotheses in experiment_log.md.
- `.transcription/hh4-citations.log`: strict citations and input quotes passed their existing baselines (zero new; six old input-quote findings remain).
- Coverage tree regenerated: **188 gates**; README and docs/COVERAGE.md updated.
- Consumer self-test passed; completeness self-tests including four debt tests passed; bug inventory append-only check passed through BUG-0286.
- No current full `check-all` run. Older `check_logs.py` passes predate the new definition/gate; current logs have open rulings. Do not claim current review closure.

## Reviews: exact current state

### Final hh4 household + f1040 source/render batch

Archives before overwrite:
`.transcription/archive/before-household-status-gate-review-2026-11-01/` with checked hash MANIFEST.
Earlier archives: `before-household-round2-2026-11-01`, `before-household-completeness-close-2026-11-01`, `before-household-definition-review-2026-11-01`.

Claude batch finished, all four successful:
- `.transcription/hh4-claude-run.log`, `hh4-claude-summary.json`.
- Transcription household: 8 open; f1040: 5 open.
- Render household: 1 open; f1040: 4 open.

DeepSeek batch was interrupted:
- `.transcription/hh4-flash-run.log`: household transcription finished (13 open), f1040 transcription finished (13 open).
- Driver was killed before its summary/final render completion. At shutdown render household had 6 open and f1040 0 open, **but these counts alone do not establish current receipts**; either may be an older hh3/hh2 log or partially replaced output. Validate subject/source/request/reply binding; rerun only unfinished/stale jobs.

**No hh4 rulings or triage have been applied.** Earlier hh2 household/f1040 rulings were all adjudicated and recorded in `reviews/2025/transcription/adjudication/{household,f1040}.md`, but current replies supersede them. Prior ruling proposals are under `.transcription/proposed/hhpass2/`. Use evidence on merits, not automatic carry-forward.

### EIC and HSA consumer transcription refresh (hh3)

Completed both families for `eic,f8889` because the marriage input's question changed. No authored EIC/HSA formulas changed. Current logs and triage exist, but **all fresh disagreements remain open**:

- Claude EIC 16; DeepSeek EIC 17.
- Claude f8889 9; DeepSeek f8889 16.
- `.transcription/hh3-{claude,flash}-summary.json`; triage files under `reviews/2025/transcription/triage/`.
- Claude EIC triage: 2,081 comparisons, no completed-return value/refusal/unknown differences on final credit; many **candidate-shows-skipped** differences on worksheet lines. Candidate omitted shown_when for lines after STOP/inapplicable worksheets. Source instructions require skipping those lines. Partial/refused differences also need line-by-line classification; do not claim universal equivalence.
- DeepSeek EIC candidate is **type-invalid**: collection `person.has_sc`/`person.se_screen` read without sum_over (self_employed and clergy). No executable equivalence evidence. Other declarations must still be judged individually, not all dismissed on one error. Candidate also refuses all self-employed credit instead of implementing supported Worksheet B, and over-broadly derives 27c from any ineligibility/zero credit.
- Claude f8889 triage: 1,487 comparisons. Two completed numerical witnesses (`classm.s2.2` and `.deepseek`) have line6/13 $4,987.50 candidate vs $4,279.17 project. This is the **already recorded `amb.2025.hsa_step4_other_limits`**: candidate adds line5-Step1 in full; project uses the chosen self-only-month Step4 amount. Read ambiguity p.137ff (search ID), source i8889 p.7/p969 p.6. This also propagates to excess_amt. Do not “fix” the adopted reading.
- Candidate f8889 line7 counts only family months; `amb.2025.hsa_line7_months` chooses all eligible months for the married family-year catch-up. Other relevant register entries: `hsa_last_month_change`, `hsa_last_month_all_year`, `hsa_partial_exception`.
- Claude f8889 line3/step1 reads last_month even when all_year already determines the limit; sampled completed partial case becomes candidate-unknown. Other partial/refusal differences are availability/scope and need classification. Line16 matched all 1,487 comparisons (candidate lacks explicit zero-distribution shortcut).
- DeepSeek f8889 changed published line3 type (`Dollars` to `NonNegDollars`), so whole candidate is invalid for execution. Rule this declaration as such; inspect other expressions individually. No sample equivalence claim.

### Completeness

Final `.transcription/hh4-completeness-run.log` finished: **4 forms, 37 claims, zero unparsed**. Records now in `reviews/2025/completeness/completeness.json`:
- dependent: 12 claims, prompt prefix `3c47691431`.
- f1040: 12, `7f0caef60b`.
- f2441: 7, `df5bcc830f`.
- household: 6, `f049d8a43b`.

**These final claims have not been read/adjudicated.** Existing rulings are for older hh3/hh2 prompt SHAs and are stale. Re-read current claims and match each source/evidence on merits, replacing keys and SHAs. Delete rulings whose claims no longer exist; never just change the SHA.

Scratch `.transcription/proposed/hhpass3/adjudicate_completeness.py` contains the 35 hh3 rulings and evidence for dependent/f2441/f1040. **DO NOT RUN IT AGAIN:** it hardcodes old claim ordinals and would misrule current final claims. It is reference material only. The prior current records/rulings were archived before hh4.

Remaining 55 deferred forms retain local baseline subjects. A changed foreign gate must NOT qualify actual stale reviews or bring all 55 due. After actual f1040 review, its `stale:f1040` baseline and deferred_debt record were removed intentionally. Migration script currently requires the baseline to exactly equal the historical map, so rerunning that one-time script after shrink will reject; do not restore retired baseline entries just to rerun it.

### Consumers

- Three changed marriage-input baseline pairs were reviewed by isolated Claude and adjudicated in `.transcription/proposed/hhpass3/adjudicate_consumers.py`:
  - `household.married@i1040gi:p23`: same for this still-married HOH reader; separate cp_marriage_ended and rdp gates handle the model's other cases.
  - `...@i8889:p5`: same read with p.4 rule6 and p.6's explicit year-end unmarried chart; the draft offered a competing grammatical reading of “at any time”.
  - `...@i8889:p6`: same, model also agreed.
- Their three baseline entries were removed and rulings added. Last check: 438 findings, 57 ruled, 380 baseline, **one new**.
- New pair: `consumer:household.married@i1040gi:p13`, reader filing_status_conflict.
- Its draft prompt exists: `.transcription/proposed/hhpass4/consumers/household.married@i1040gi_p13.txt`.
- Driver exists `.transcription/proposed/hhpass4/review_consumers.py`; no response collected before stop. Run deliberately once resumed, inspect against actual conjunction and the separate death-year input, then adjudicate. Existing raw model responses for other consumer pairs are saved; preserve them.

## Exact next steps after owner resumes

1. Read the diff and this handoff; verify no model processes are still running. Preserve all work.
2. Audit hh4 receipts and finish only the two DeepSeek render jobs if stale/incomplete. Archive before overwriting. Models: Claude `claude-opus-5-5`, **deepseek-flash**, never Pro.
3. Read all 37 final completeness claims, adjudicate against current source and implementation, carrying explicit older low debt to the existing tasks/BUG entries where justified. Fix any introduced or medium/high finding and rerun only invalidated reviews. Pay particular attention to whether final household/f1040 claims accept the new consistency gate and definitions; do not assume they do.
4. Complete the single new consumer review/ruling; run check_consumers and its self-test.
5. Run current household/f1040 triage for both families, then rule final source/render disagreements. Rule already-completed EIC/f8889 source refreshes using current triage and source/ambiguity evidence above. Append final summaries to adjudication briefs; eic/f8889 also need a household-input-refresh section. Never blanket-classify a type-invalid reply's unaffected lines.
6. Offline checks: check_logs, strict citations, instruction citations, consumers, screens, completeness, coverage placement, operands/signs/limits, bug inventory, diff whitespace. Recheck metadata/ruling contexts after final changes. The new source wording may expose changed-context baselines; do not silently rebaseline.
7. Update T-114–117 only at package closure; keep them in progress until committed. Close experiment-log outcomes, update tracker/handoff/index. Ensure claims about fixed bugs versus deferred ones are accurate.
8. Run `npm run check-all-bg` on the final snapshot, inspect full result, fix any actual failures. Use `tools/commit_tested.sh -F <body-file>` to commit EXACTLY the tested tree; do not bypass hooks. Git metadata writes require sandbox escalation. Prior handoff authorizes pushing after checks; preserve remote changes via merge, not reset/rebase of tested work. No commit/push occurred yet.
9. Then continue the approved plan: early T-102 reporting correction and P1 verification bugs; P2 tools before the remaining form passes. Dependent/person and T-113 are next in the form sequence. Coverage expansion stays last.

## Operational constraints

- Fixed-prompt model calls are authorized work. Claude uses naked CLI print mode with `--setting-sources ""`, replacement system prompt, no tools, no persistence, no permission prompts. Do NOT use the Anthropic API/keychain API key. DeepSeek uses existing flash transport. Read `~/.claude/AISP.md` before invoking AI in a fresh session.
- Sandbox blocks Claude credentials/network. The sandboxed completeness call failed, then the approved escalated retry succeeded. Use normal escalation, not a workaround, if needed. Do not print secrets.
- All `.transcription/` and `.classm/` receipts/archives are ignored but needed for provenance. Preserve them and verify exact request/reply hashes when qualifying evidence.
- Reviews may be type-invalid/noisy and thus pending even after human/agent adjudication. check_logs passing does not grant qualification. Do not rewrite raw replies or original verdicts.
- No agents were spawned for implementation. Earlier three Luna audit agents completed read-only audit work; their findings are already in the tracker. Do not restart them automatically.
- Append-only experiment log contains failed command/metadata hypotheses and corrections. No harness memory was written.
