# Temporary backlog plan — 2026-11-01

**Status: active. Owner-approved sequence, recorded 2026-11-01. Delete this document when the retirement checklist below is satisfied.**

## Authority and purpose

Clear the existing hardening backlog systematically, in bounded packages grouped by their shared review footprint. Coverage expansion is the lowest priority. This plan supersedes earlier execution orders in handoffs, the 2026-10-26 plan revision, and the spec; it does not supersede validation requirements, source-evidence rules, existing ambiguity decisions, or owner verdicts.

`../TASKS.md` remains the authoritative task register; `../TASKS-DONE.md` holds completed and explicitly closed items. This document owns package order, dependencies, and program progress. It is temporary coordination material, not a second permanent backlog. Never mark a task done solely because a package row says done.

Backlog closure means each item is fixed, explicitly accepted with a reason, or assigned a concrete external trigger. It does not require implementing every proposed refactor. Waiting on another package is an internal dependency, not an external trigger that permits retirement.

## Start here

- **P0 — household closure is closed** (2026-11-01, household closure commit; evidence in the closure section below). T-114–117 are done and BUG-0272–0286 are recorded.
- **P1 and P2 are largely done** (2026-11-01): T-102 corrected coverage to **78.4%** (`dependent_filer`, 4.7%); the P1 verification repairs (BUG-0287–0289), T-155 renderer marker, T-156 mutation operands, T-096 guard domains, T-150/T-143 review tooling and T-160 DeepSeek adjudication are committed. Remaining P2 work is T-159 and the T-139–140/T-142/T-144/T-146–148 rows.
- **P3 coordinated form passes are the active package.** The next form pass is **f8962 (T-134 + T-162)**; then the shared **asset/Schedule C** pass (T-157/BUG-0290, T-158/BUG-0291); then **Form 5329/person** (T-161/BUG-0292); then F1 dependent/education.
- The code tree is `cbd7302` (parent of this documentation commit), working tree clean, full suite green on tree `ea29fdda`. The current handoff, including the f8962 pass procedure and the queue order, is the top entry of `../HANDOFF-NEXT-SESSION.md`. Older reported test results are historical evidence, not a green result for the current tree.

## Package tracker

Update status, next action, and closure evidence as work proceeds. Use ready, active, blocked (name the dependency), done (cite commit/evidence), or accepted (cite decision). Each package may contain several small, independently validated commits.

| Package | Status / dependency | Scope | Exit condition / closure evidence |
| --- | --- | --- | --- |
| P0 Household closure | Done 2026-11-01 (household closure commit) | T-114–117; bug entries for the introduced corrections and new gates; source-predicted regression fixtures; gate placement; round-two reviews | Required reviews adjudicated (114 current rulings, 0 open); all introduced defects and medium/high findings resolved; exact tested tree committed. Evidence: closure section below. |
| P1 Verification integrity | Done in part 2026-11-01 | Reproduce and resolve the differential reader, memo aliases, green-history update race, push-guard scope, renderer markers, mutation operand omissions; T-096 | Memo aliases, differential reader, push-guard scope, green-list race and `--year` forwarding fixed (BUG-0287–0289); renderer marker fixed (T-155, 20 lines in five forms, ten render reviews rerun; BUG-0290/0291 recorded). Mutation coverage is T-156 (done in part; guard/table-key remainder is T-159); T-096 is fixed. Evidence: P1 checkpoint below. |
| P2 Review preparation | Triage sample investigated 2026-11-01 (309 completed returns, not 95; 95 counted disagreements). T-150, T-143, T-160 done 2026-11-01. Next T-159 (needs EIC table-key fixtures), then T-139–140, T-142, T-144, T-146–148 | T-150; T-143; T-160; T-159; T-139–140, T-142, T-144, T-146–148 | Review inputs usable; mutation-critical regressions survive regeneration; interfaces explicit; printed-only mode ready before single-document Class M reruns. Evidence: `tools/siblings.py` and its check-all steps. |
| P3 Existing behavior and form debt | Active 2026-11-01; next f8962 (T-134 + T-162), then asset/sc (T-157/T-158), then f5329/person (T-161), then F1. Batches below | T-104–113, T-118–121, T-123–134, T-136–137, T-141, T-145; applicable T-094, T-057, T-095, T-101 | Each form batch meets the closure procedure; every remaining form scheduled for a pass. Evidence: pending. |
| P4 Evidence and reporting | Small reporting corrections can run early; final closure after P3 | Remaining T-094/T-057; T-006/T-095; T-098–100; T-099 and documentation portion of T-012; reconcile older integrity obligations | Claims supported or narrowed; required review gaps resolved; remaining exceptions explicitly dispositioned. Evidence: pending. |
| P5 Bounded maintenance | After higher-priority work; pull forward only a demonstrated dependency | Selected audit improvements to helpers/parsers, generators, Lean batching, fixture formatting, extraction, and year handling | Concrete maintenance failure or measured benefit addressed; remaining design proposals explicitly accepted or given real external triggers. Evidence: pending. |
| P6 Coverage expansion | Deferred until this finite hardening program retires | T-151 Schedule E; T-002/003/005; remaining scope additions in T-012 | Outside this temporary program. Resume from the permanent task register after retirement. |

### Priority exceptions and limits

- **T-102 is early reporting work**, alongside closing P0/P1: correct the dependent-filer coverage estimate. Reporting accuracy is not coverage expansion.
- Known amount-affecting defects do not wait behind a long tooling project. T-118 and T-134 deserve early attention under the existing medium/high rule. Tooling precedes such fixes only where required to validate them.
- Fix medium/high findings promptly and re-review; fix every regression introduced by uncommitted work, regardless of severity. Batch older lows with their owning forms.
- P2 is bounded. T-150 addresses recorded sibling/input-ripple failures; it is not a general dependency-platform rewrite. T-143 needs a concrete failing candidate and explicit treatment of invalid dependencies before partial execution is trusted.
- Preserve the review-tool freeze's requirement for a concrete failure before changing policy/checker versions. Do not trigger a global receipt refresh merely for architectural tidiness.
- T-101 corrections within already supported situations are maintenance, even if measured coverage rises.
- Final-year adoption is maintenance of the intended filing year, not expansion. Prepare year handling before its external trigger arrives.

## P3 form-batch tracker

Before editing a batch, identify its full review footprint, relevant baseline entries, consumers, ambiguity links, and existing lows. Coordinate shared person/dependent changes so the same interfaces are not repeatedly reopened. The rows describe coordination groups, not a requirement for one giant commit.

| Batch | Status | Tasks / footprint | Closure evidence |
| --- | --- | --- | --- |
| F1 Dependent and education eligibility | Pending | T-104–113; include the person-side T-113 change and related education/household consumers | Pending |
| F2 Person, retirement, dependent care | Pending; coordinate with F1 | T-118–121, T-123, T-127–129; person, retirement, Form 2441, affected scope questions | Pending |
| F3 Premium tax credit and energy credits | Pending; T-134 is the f8962 form pass (a screen-only attempt reverted 2026-11-01) | T-134 and T-162 (f8962); T-132 and T-145 together; relevant generator and partial-input cases | Pending |
| F4 Income, investments, deductions | Pending | T-124–126, T-130–131, T-133, T-136–137, T-141 | Pending |
| F5 Remaining forms | Pending inventory | Remaining T-094 baselines and review migrations, ordered by risk and shared dependencies | Pending |

Apply T-101 gate by gate within its owning batch. Carry T-057's ten legacy render reviews and T-095's ambiguity links with the affected forms; use P4 for any residue.

**Approved change to the former opportunistic burn-down:** schedule every remaining form for a pass. Keep the existing line-level invalidation rules, but do not leave T-094 indefinitely waiting for a form to change accidentally. At batch closure, no baseline entry in its agreed scope remains unexamined. A disposition may be defect, justified exception, duplicate, obsolete entry, or explicit follow-up task; it is not automatically a bug.

## Intake and T-152 disposition work

- [ ] Reconcile `TASKS.md`, completed tasks, older integrity plans, the current handoff, and audit claims into one task inventory. Check blind whole-return work, product-surface work, completeness definitions, and prevalence work against artifacts before declaring them open or done.
- [ ] For each actionable task, record package, priority, dependencies, exit condition, and disposition in the register or its linked detail. Keep existing IDs. Split a bundle only when its pieces have different dependencies or exit conditions.
- [ ] Give every audit subclaim a disposition and a task ID where action remains. Do not mechanically create 37 implementation tasks: the audit's grouping is inconsistent.
- [ ] Map every remaining form into F1–F5, with its baseline/review inventory. Initialize the progress measures below from current artifacts.
- [ ] Record accepted design tradeoffs with their reason. A speculative redesign requires a bounded investigation, concrete benefit, and migration cost; preserve independent evaluators.

### Audit investigation carry-forward

Three Luna agents inspected the audit's sections on 2026-11-01; the parent reviewed their findings. This was source inspection and read-only counting/JSON probing, not runtime reproduction or a full check run. The table preserves investigation leads and corrections, not new bug certifications. Recheck against current code when creating tasks; record detailed evidence in the permanent task/bug records before retiring this document.

| Audit sections | Carry-forward assessment | Destination |
| --- | --- | --- |
| 1.1 | Memo aliases supported by TS/Lean source and export paths; tax-value/performance impact not established | P1 |
| 1.2; 2.1 | Missing `(screen)` renderer marker; 20 saved prose lines contain `column (screen)`, not the headings claimed. Different helper consumers may have different semantics | P1 focused correction; P5 any broader consolidation |
| 1.3 | 56 step calls, 23 without argument forwarding in the inspected script; only some are year-aware. Reproduce named year-sensitive cases | P1 if needed for current checks; otherwise year preparation/P5 |
| 1.4; 2.2 | Operand traversal omissions supported; mutation-score effect unmeasured. Other AST walkers have differing responsibilities | P1 mutation coverage; P5 shared visitor proposal |
| 1.5 | `differentialClassC` assumes `.values` on existing investigation-array JSON; fixture coverage calls it. Failure path inspected, not run | P1 |
| 1.6 | Tip-only push check differs from its comment; unlocked green-history update has a separate lost-update risk. BUG-0268's build/read race does not resolve it. Snapshot Git objects alone are not a correctness defect | P1; dispose of housekeeping separately |
| 1.7; 4.3–4.4 | Direct PTC text reads bypass archive-reader regex enforcement; hardcoded year/page assumptions and fragile parsing patterns exist, but resulting corruption not demonstrated | Extraction/year package; prioritize demonstrated failures |
| 2.3–2.5 | Repeated key regexes and import-time year state exist; duplicate atom sets exist, but unsupported vocabulary need not be obsolete | P5; accept intentional constraints where justified |
| 2.6–2.8 | Generator coupling, form-specific mutation equivalence logic, and early-stage workflows exist; their existence alone does not establish incorrect behavior | P2 specific generator defects; P5 remaining proposals |
| 3.1–3.3 | Raw JSON evaluation and inline arithmetic exist. Weak evaluator theorem scope is already documented; no wrong valid-data calculation established. Missing monotonicity lemmas overlap T-100 | P4 T-100/claim accuracy; P5 robustness/design |
| 3.4 | Audit's operand examples are materially inaccurate: several cited inline operands already work in Lean. Per-case subprocess spawning is real; inspected fixture/generator counts imply 2,011 cases, not saved 1,994 | Correct T-152 disposition; P5 measured batching benefit |
| 4.1–4.2 | Multiple specialized renderers, models, parsers, loaders exist; they are not all interchangeable duplicates. `UnroundedModel` is specialized comparison tooling | P5 only with demonstrated overlap/benefit |
| 4.5 | Blanket zero-self-tests claim false: UsTaxes has a scoped self-test. Listed LOC subtotals wrong; inspected eleven files total 5,051 lines. Integration evidence differs from unit coverage | P2/P5 targeted testing gaps; correct audit disposition |
| 5.1–5.3 | Large forms, parallel education blocks, schema constraints, monthly repetition and generic interview help exist. Whole-file lengths are not a count of monthly boilerplate | Owning form pass for wording; P5 bounded architecture proposals |
| 5.4 | Input ripple is not universal. Fixture JSON round-trips semantically, though formatting changes. Unasked contradictory answers do not by themselves prove an invalid evaluated return | P2 fixture/generator cases; P5 formatting |
| 6.1 | Conflicting entrypoints/spec claims; 91 ambiguity entries with 12 unlinked were recounted | P4; update entrypoints immediately when needed |
| 6.2 | Recounted 736 baseline entries, 11 citation exceptions, 27 PDF exceptions. Not 736 certified defects. Screen table's 70 is `covered` findings, not all rulings. 78/149 pending is a saved report figure, not recomputed eligibility | P3/P4; initialize current metrics before relying on totals |
| 7 | 37/12/25 split not a reliable atomic issue count; T-152 is umbrella tracking and several task mappings need correction | Intake; close T-152 only after dispositions and task mapping |

## Conditional work

Waiting items stay in the permanent register with explicit triggers and do not keep this temporary tracker alive indefinitely.

| Work | Trigger / handling |
| --- | --- |
| T-011 final TY2026 adoption | Required final documents available; prepare year forwarding and year-specific tooling beforehand. Check availability when this work is scheduled; no availability claim is made here |
| T-034 refreshed prevalence estimates | Suitable new data available; distinguish data waiting from methodological work that can be done now |
| T-097 platform requirements and distribution/legal questions in T-012 | Before outside reproduction/distribution; explicitly document the supported platform if portability is not implemented |
| T-040 and related extraction findings | Scheduled extraction-maintenance package in P5, or earlier if needed for a current source check. This is internal work, not an indefinite external wait |

Broad proposals such as a typed Lean AST, a month-indexed schema, a Date type, person-form decomposition, or wholesale year-context redesign need bounded investigations. At program close they must be implemented, explicitly accepted as tradeoffs, or genuinely externally waiting; simply moving them to another unprioritized list is not closure.

## Closure procedure for each package

1. Inspect current artifacts; confirm the issue and identify sibling lines, consumers, fixtures and review footprint.
2. State expected behavior and predict regression results from the governing source before recording evaluator output.
3. Implement the bounded batch, including applicable known lows and baseline work.
4. Run targeted checks first; resolve mechanical failures before expensive reviews.
5. Review the final candidate: preserve/archive prior receipts, rerun affected required reviews, triage and adjudicate. Preserve original owner verdicts and ambiguity choices.
6. Resolve all introduced defects and medium/high findings under the standing rules. Run the required full suite on the candidate, commit the exact tested tree through the guard, and update task/package dispositions with evidence. A later edit invalidates any claim that the earlier green result covers it.

## Work in progress and progress measures

One active integration package at a time. Parallel read-only investigations or isolated changes may proceed where they do not share inputs, generators, or review receipts. Only one owner controls a shared input change and its ripple. Finish and commit a package before opening another shared-schema/evaluator change.

Update these measures at package closure; label snapshots with date/tree and do not substitute historic reports for current results:

| Measure | Current baseline | Latest / evidence |
| --- | --- | --- |
| Confirmed correctness defects by severity | Not yet reconciled | Pending intake |
| Packages ready / active / blocked / closed | P1 active, T-102 alongside; P0 closed | Closure snapshot, 2026-11-01 |
| Baseline entries dispositioned / newly added | Historical inspection counted 736 entries; current scoped inventory pending | Pending intake |
| Forms with current, adjudicated required reviews | Not freshly measured | Pending inventory |
| Completed / partial / refused scenarios exercised in triage | Reduced completed sample reported by household handoff; cause unverified | P2 investigation |
| Accepted tradeoffs / external waits | Decisions not yet consolidated | Pending intake |

Fixture counts, model-call counts, and deleted task rows alone do not establish progress.

## Retirement: dispose of this document

- [ ] P0–P5 and early T-102 are closed with evidence or explicit accepted dispositions; no internally blocked work remains hidden here.
- [ ] T-152's subclaims and older-plan obligations have permanent task/closure records; all remaining forms received their scheduled disposition.
- [ ] External waits retain their exact triggers in `TASKS.md`; coverage expansion remains there in its agreed order.
- [ ] Move durable decisions and still-needed evidence into the relevant spec, tool docs, task records, or bug inventory. Do not preserve this entire tracker as another historical handoff.
- [ ] Replace its links in `TASKS.md`, `HANDOFF-NEXT-SESSION.md`, `PROJECT_INDEX.md`, and the 2026-10-26 plan revision with the next current entrypoint; search for other backlinks.
- [ ] Delete this file in the closing change, recording program closure and relevant evidence in the commit/task records. Git history retains the temporary plan.

The program ends before P6 begins; this document need not survive until every future coverage stage or external trigger finishes.

## P0 execution checkpoint — 2026-11-01

Still active; no commit and no full-suite success claimed.

- Added BUG-0276–0278, eight source-predicted `stage21.household.*` fixtures, and the two new refusal gates to the coverage tree. Build and render succeeded. Full CLI fixture run: **1,419/1,419 passed**, recorded in `.transcription/hh2-fixtures.log`.
- Refreshed household and f1040 transcription/render reviews under both families, archived the prior receipts with hashes, and adjudicated all 51 disagreements. Summaries: `reviews/2025/transcription/adjudication/{household,f1040}.md`, section “Household pass, round 2”. `check_logs.py` passed; this does not qualify the type-invalid DeepSeek f1040 reply or other pending second-family evidence.
- Consumer checks: three new pairs adjudicated after isolated Claude responses and inspection of the actual conjunctions; 437 findings, 54 ruled, 383 baseline, zero new/stale. Instruction citations, operands, signs, limits, screens, strict citations and coverage placement passed their targeted checks. Existing baseline debt remains.
- Household completeness: six fresh claims. Five ruled against the current prompt; claim #1 (marital-status definitions) remains open. `household.married` is also used by EIC and HSA, so a filing-status-only definition must not be copied blindly into that shared input. Inspect each consumer before fixing or disposing of this claim. No new bug has yet been certified for it.
- Completeness check currently fails with 59 new findings: 58 stale/missing reviews and the one unruled household claim. Of 56 existing baseline entries, **55 recover their original baseline fingerprint when only the two new f1040 refusal declarations are removed in a read-only counterfactual**; f1040 itself remains changed. Evidence: `.transcription/proposed/hhpass2/completeness-impact.json`. `elsewhere()` adds every f1040 refusal to all foreign prompts, and the checker uses that full prompt hash as the baseline subject. Thus the additions pull untouched forms out of the agreed form-by-form backlog.
- A scope choice was presented to the owner: investigate a narrow baseline-policy repair (recommended), or refresh/adjudicate all affected forms. No answer recorded at this checkpoint. No baseline entries or receipt fingerprints have been relaxed. Investigation is not authorization to accept stale reviews.

Proposed bounds for a baseline repair, if selected: preserve full prompt hashing for every actual review and claim ruling; give never-reviewed legacy debt a separate fingerprint tied to its own canonical form, source sections and review policy; migrate only entries whose historical provenance can be reconstructed and verified. Keep changed own forms due now. Prove with tests that foreign refusal additions cannot silently qualify an old review, own form/source/policy changes still invalidate debt, and malformed/mismatched migration records fail closed. Do not simply run `--baseline`. Previously reviewed dependent/f2441 and changed f1040 still need current review/disposition under the selected policy.

Next: resolve the open household claim and the completeness scope choice; rerun only reviews/checks invalidated by resulting changes; run the full snapshot suite and use the tested-tree commit guard. T-114–117 stay in progress until package closure.

### Narrow completeness repair — owner selected, 2026-11-01

Implemented BUG-0279 after the owner selected the narrow baseline approach. All 56 historical baseline prompt fingerprints were reconstructed from an independently exported/built f44bae4 checkout before migration. The original baseline map is unchanged; 55 untouched forms are deferred by matching local subjects. f1040 remains due. Existing dependent/f2441 receipts remain stale and cannot use the exemption. Four regression tests are included in the normal completeness self-test; all pass. The live check reports 55 baseline, five ruled and four new: dependent, f1040, f2441 and household claim1. Full-suite validation and P0 commit remain pending. This supersedes the unanswered scope choice recorded above.

## Usage pause checkpoint — 2026-11-01

Owner stopped work for usage. Full restart state: [household closure handoff](../handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md). P0 remains active/uncommitted. BUG-0280/0286 add marriage definitions and filing-status entry consistency; BUG-0281 fixes consumer prompt generation. BUG-0282–0285 explicitly preserve older definition debt with T-107/T-109/T-111/T-113 and new T-153/T-154. Latest build/render, strict citations and 1,425/1,425 fixtures passed; no full-suite result. Final source/render/completeness rulings are pending; DeepSeek batch interrupted, all matching jobs stopped. Do not rerun the old ordinal-based completeness adjudication script.

## P0 closure — 2026-11-01

P0 is closed in the household closure commit (parent f44bae4). The exact tree passed the full suite through
`tools/commit_tested.sh`.

- Authored: BUG-0272–0286; T-114–117 done. `household.married` definitions (BUG-0280), the filing-status
  consistency gate (BUG-0286), the death-year and community-property gates (BUG-0277/0278), the consumer prompt
  fix (BUG-0281) and the narrow completeness debt repair (BUG-0279). The older definition debt remains open in
  BUG-0282–0285 with T-107/T-109/T-111/T-113/T-153/T-154.
- Fixtures: 1,425/1,425 CLI fixtures passed (`.transcription/hh4-fixtures.log`); six source-predicted status cases
  matched; the coverage tree has 188 gates.
- Reviews: household and f1040 transcription and render under both families; eic and f8889 transcription refreshed
  for the changed shared input. The full suite caught that the hh4 render batch had reviewed a stale `rendered/`
  tree (it predated BUG-0286); the rendered English was regenerated, the prior receipts archived under
  `.transcription/archive/before-render-refresh-2026-11-01/`, and the four render reviews rerun. 114 hh4 rulings
  plus 12 render-refresh rulings applied; `check_logs.py` reports 0 open.
- Completeness: 92 findings, 0 new, 55 deferred baseline forms, 37 ruled. Consumers: 438 findings, 0 new, 380
  baseline, 58 ruled. Second-family model-error noise 8.7% (409/4,675), provisional for pending reviews.
- Offline checks: strict citations, instruction cites, consumers, screens, coverage placement, operands, signs,
  limits, bug inventory and `git diff --check` all passed.
- Corrections made while checking the hhpass4 work before commit: the eic/f8889 archive pointer (the prior logs
  are under `.transcription/archive/before-household-definition-review-2026-11-01/`), the f1040 DeepSeek line 19
  justification (the printed Schedule 8812 line 14 destination, not an interface label), and the f8889 line 3 and
  line 6 splits into ambiguity plus model error for the withheld `last_month` partial.

## P1 checkpoint — 2026-11-01

Reproduced the audit findings on the current tree and fixed the evidence-integrity items in one batch:

- **1.1 memo aliases (BUG-0287).** A cross-document reference from a collection entry cached its result
  under a key such as `person[spouse].f8606[form].person.ira_files_8606`; one return carried 64 aliases
  into `eval --json`, values-sheet derivations and the TS/Lean comparison. Both evaluators now memoize
  under the target key only. The comparison loses 87,101 alias values and still agrees on 2,025 cases;
  `test-integration` asserts no alias keys. Fifty-nine stage1 fixtures had recorded the aliases as
  duplicate expectations; the canonical keys remain and the CLI fixtures pass 1,425/1,425.
- **1.5 differential reader (BUG-0288).** `differentialClassC` read the investigation-log array as a
  calculator record; both readers now use one `calculatorRecords()` filter.
- **1.6 commit guard (BUG-0289).** `pre-push` checks every commit in the pushed range, not only the tip;
  `record_green` takes a lock. `test_pre_push.sh` and `test_green.sh` run in check-all.
- **1.3 `--year` forwarding.** The 16 year-aware steps that dropped the arguments now receive them; the
  script's comment no longer claims every step does.
- **Follow-ups.** 1.2 (renderer marker) was T-155 and is fixed: the 20 `(screen)` lines now render as
  helpers, the ten render logs were rerun and ruled, and the exercise exposed BUG-0290 (Schedule C at-risk
  wording) and BUG-0291 (asset 40%/50% allowance), scheduled as T-157/T-158. 1.4 (mutation operands) is
  T-156: the string `rate`, `prorate.whole`, `percent_floor.whole` and definition-bind operands are added (2,778 mutants, 95.6% raw / 100% adjusted); table keys, choose branches and test operands are T-159 because the full extension produced 518 unexplained survivors (256 without guards, 7 table keys with guards and branches off). T-096 stays open. The one 1.6 subclaim not fixed (dangling snapshot commits) is
  git housekeeping, not a guard defect.

## Triage sample check — 2026-11-01

The household handoff read f1040's ~95 completed-return differences as a collapsed sample. It is not: the
completed sample is 309 returns (1,425 fixtures + 500 generated), plus completed partial records; 95 was the
number of disagreements *on* completed returns, which fell from 520 because the refreshed candidate computes
more of them. The fixture and generated states are unchanged from f44bae4 (194/193 completed fixtures,
116/116 generated). `triage.py` now records `bank.return_states` and says that `kinds_by_return` counts
differences, not sample size.

## T-150 — fix-sibling tool, 2026-11-01

`tools/siblings.py` lists, for changed lines, the lines that read the same rule leaves (the input and
gate lines the changed line directly reads), predicates testing the same constants, and lines and
questions anchored on the same (document, page, heading); `--input` lists a new input's ripple across
forms, questions, fixtures, the generators, input contracts and Class M jobs. Check-all runs its
self-test and `--check`. Bug entries from BUG-0290 onward with a Fix field must name `Fix lines` and
`Siblings checked`; the check generates the sibling set and fails when it is omitted, and when a
sibling form has no review log changed since the entry's base (the commit that added it, or HEAD for
an uncommitted entry). The first closure followed computed values and was too broad (283 lines for
`sa.dependent`); the rule-leaf version yields 5 there and 1 for `sc.at_risk`. A synthetic entry naming
only `sa.standard` for a fix on `sa.dependent` still fails, as intended.

## Known-defect queue checkpoint — 2026-11-01

Queue 1 of the hardening pass, first batch: T-118 (the IRA excess questions now say the excess must have
remained in the IRA at the end of 2025). The person transcription and render logs were rerun and ruled; the
stage16 remedy fixture and `docs/COVERAGE.md` were regenerated. The screen review for `person.x_other` was
rerun and ruled; it found a new gap, BUG-0292/T-161 (an earlier-year HSA excess alongside a 2025 Form 8889 is
not asked). The new person DeepSeek transcription reply is type-invalid with 70 open sections, recorded as T-160.

BUG-0290/T-157 was reverted from this batch and returned to the Schedule C pass: changing `sc.at_risk` makes
the sc form due for completeness review, and that review produced 18 claims — the Schedule C form pass, not a
wording fix. The sc evidence is restored to HEAD.

Still to do in this queue: T-157 (Schedule C at-risk), T-134 (Form 8962 other coverage) and BUG-0291/T-158
(asset special allowance: refuse the 50% reuse/recycling class and the pre-September-27-2017 boundary).
