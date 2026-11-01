
## 2026-11-01 — Household gate regression preparation

- Attempt: prepare eight source-predicted cases, reading refusal metadata from Form 1040.
- Observation: preparation raised KeyError for household.hoh_community_property before writing fixtures.
- Ruled out: the old refusal is not declared directly on Form 1040.
- Inspection: forms/2025/household.yaml declares it on household.hoh_eligible; it propagates downstream.
- Next test: read both owning forms' refusal declarations, preserve expected propagation to f1040.line12e, run fixtures.

## 2026-11-01 — Household regression first run and review transports

- Fixtures: 1415/1419 passed. All four failures are new refusal expectations lacking build-enriched citation revision, snapshot and tax_year; gates, remedies and numeric controls matched predictions. Existing 1411 cases passed.
- Next test: add only manifest citation metadata to the four predicted refusal expectations, then rerun the eight cases before the full suite. No evaluator-derived tax expectations substituted.
- Review transports: sandboxed Claude exited without a response; sandboxed DeepSeek could not access its configured Keychain entry. Approved outside-sandbox retries produced all eight transcription/render reviews and the household completeness review. No raw failed replies were fabricated or reused.
- Completeness: 59 prompts changed; inspection shows new Form 1040 return-wide refusals enter HANDLED ELSEWHERE for other forms. Investigate prompt differences before selecting required refresh scope; do not silently rebaseline.

### Household review closure checkpoint — 2026-11-01

The corrected source-predicted fixtures passed the full CLI bank (1,419/1,419; `.transcription/hh2-fixtures.log`). Consumer check passed after adjudicating the three isolated model claims against the actual guarded consumers. All 51 transcription/render disagreements were adjudicated and `check_logs.py` passed. Completeness remains unresolved: 58 stale/missing reviews plus one unruled household definition claim. The read-only counterfactual recovered 55 untouched-form baseline fingerprints by removing only the two added f1040 refusal declarations. No rebaseline or receipt weakening performed; next experiments and scope choice are in the temporary backlog tracker.

### Narrow completeness baseline repair — 2026-11-01

Owner selected narrow repair. Exported f44bae4 to `/private/tmp/tax-baseline-d2ivf_kr`, rebuilt canonical output successfully, verified historical authored forms, reviewer and manifest against Git, and reproduced all 56 baseline prompt fingerprints before recording local debt subjects. Live check preserves 55 deferred entries and leaves four actual blockers. All four new regression tests and existing completeness self-tests pass. No full-suite success asserted.

### Marital-status definition correction — 2026-11-01

Primary p501 p.6 and i8889 p.4 distinguish legal year-end marriage from special filing-status rules. Adding source definitions to the shared input while retaining that distinction. Initial editing script failed to parse before any write; switched to a targeted patch. No evaluator formula or fixture answer is being derived from that failed attempt.

### Household round-three offline checks — 2026-11-01

The citation command used an incorrect script name (tools/check_citations.py), so it did not run. The suite declares tools/citations.py --strict; use that entry point. Consumer check exposes three due pairs for the changed marriage question; fresh isolated model drafts are being collected before adjudication.

### Filing-status regression metadata — 2026-11-01

All six predicted gate/deduction outcomes matched in the targeted CLI evaluation, but the two refusal objects differed in snapshot metadata: expected fixtures used the manifest layout-text hash, while canonical citations pin the reading-order layer. Corrected only the expected snapshot field from the manifest cols_sha256. Tax amounts, gates and remedies were not derived from evaluator output. Recheck exact objects next.

Correction/convergence: two metadata attempts differed because neither text-layer hash is the citation snapshot. The second attempt ruled out the reading-order hypothesis. Inspected engine/src/build.ts:74, which assigns source.sha256 (the PDF hash). Corrected the expected metadata from that manifest field; all six exact-object cases now match. No amount, remedy or gate prediction changed.

### Owner-requested usage pause — 2026-11-01

Stopped work and sent Ctrl-C to known sessions; final DeepSeek driver exited130. Process-table inspection found zero remaining matching project review processes. Claude final four-job batch completed; final completeness batch completed four forms/37 claims; the last consumer draft was not started. Latest CLI fixtures passed1,425/1,425 and strict citations passed their baselines. Final adjudication/full suite/commit are unfinished. All restart details, evidence and cautions are in handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md.

### Household closure — 2026-11-01

Applied all 114 hh4 rulings and checked the four items the previous session wrote quickly. The eic/f8889 summaries
had claimed no archive existed; the prior logs are in
`.transcription/archive/before-household-definition-review-2026-11-01/` and are identical to the committed 84fa330
versions. The f1040 DeepSeek line 19 ruling had claimed an interface label naming Form 1040 line 19; the published
interface shows only ids and types, so the ruling now rests on the printed Schedule 8812 line 14 destination. The
Claude eic scope reclassifications were confirmed against zero completed-return differences in the current triage.
f8889 lines 3 and 6 are now compound ambiguity-and-model-error rulings: the completed value differences are the
recorded readings, while the withheld `last_month` partial on an all-year filer is an availability error because
`f8889.line3_all_year` does not ask it. Offline checks passed: strict citations, instruction cites, consumers,
screens, coverage placement, operands, signs, limits, bug inventory and whitespace; completeness 92 findings (0 new,
55 baseline, 37 ruled); `check_logs.py` 0 open; second-family noise 8.7%. The full suite ran through the tested-tree
guard; the commit message records its result.

### Stale rendered subject caught by the full suite — 2026-11-01

The first full-suite run on the closed tree failed `check_logs`: the worktree's rebuild regenerated
`rendered/2025/{f1040,household}.md` and the f1040/household render logs named an earlier rendered English. The hh4
render batch had run at 10:14, before BUG-0286's gate and the widened spouse-death wording at 10:16; the source
reviews were current because their prompts come from the forms, but the render prompts come from `rendered/`. Reran
`npm run build` and `npm run render`, archived the prior render receipts under
`.transcription/archive/before-render-refresh-2026-11-01/`, and reran the four render reviews. Twelve disagreements
were ruled (scope 8, ambiguity 3, model error 1) and all logs report 0 open. This is a failed pre-commit hypothesis:
the rendered tree was assumed current after the hh4 batch; the snapshot rebuild proved otherwise.

### T-102: dependent filers enter the coverage estimate — 2026-11-01

Archived SOI Table 1.7 as `soi-23in17dp` (7,525,664 dependent returns; 160,602,107 total returns, 4.7%). Added
`dependent_filer` gated by `sa.dependent` and switched the existing README table item from an unmeasured gate to the
measured category. The independence-assumed estimate moves from 82.2% (range 81.6–85.7%) to **78.4%** (range
76.9–85.7%); the greedy ladder now runs Schedule E 84.1%, other Schedule 1 89.9%, dependent filers 94.3%, MFS 96.8%.
The old figure had counted dependent returns as covered even though `sa.dependent` refuses them at the standard
deduction. Consequence: the first 80% goal is open again; Schedule E is the first expansion step that crosses it.

### P1 verification-integrity batch — 2026-11-01

Reproduced audit 1.1 on `stage16.ira.i1`: 64 alias keys in the eval values. Fixed TS and Lean to memoize a
resolved cross-document reference only under the target key; the comparison falls from 4,558,885 to 4,471,784
values and still agrees on 2,025 cases. Added an integration assertion that no value key contains a
top-level document id after an instance bracket. Fixed the class C differential reader's unfiltered scan
(one shared filter), extended the pre-push hook to every commit in the pushed range, locked the green-list
update, and forwarded `--year` to the 16 year-aware steps that dropped it. Renderer marker (1.2) and mutation
operand coverage (1.4) are scheduled as T-155 and T-156: the first reopens five forms' render reviews, the
second needs the new mutants' survivors classified. Hook and green-list self-tests run in check-all.
