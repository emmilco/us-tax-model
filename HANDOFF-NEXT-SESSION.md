# Handoff — updated 2026-10-29, evening (Claude Opus 5.5)

## State after Stage 21: the 80% goal is reached

Stage 21, Form 5329 Parts I and VII (with Form 1099-R entries moved under each person, D1), is built, reviewed in three
rounds and committed: `handoffs/HANDOFF-STAGE-21.md`. The estimate is **82.2%** (from 79.6%), past the route's 80% goal
(`docs/2026-10-26_plan_revision.md` section E is complete). Findings BUG-0200 to BUG-0205; open review-tool and display
points T-079, T-081. Next, per the owner's standing goal: hardening (verification, loose ends, improvements to existing
code), starting from the open entries of TASKS.md and BUG_INVENTORY.md.

# Handoff — updated 2026-10-29, later (Claude Opus 5.5)

## State after Stage 19

Stage 19, the education credits (Form 8863), is built and reviewed: `handoffs/HANDOFF-STAGE-19.md`. The estimate is
79.6% (from 75.6%), short of 80%; the route's last stage, Stage 21 (Form 5329), is next: its decision batch first,
from `research/premises/stage21-form-5329.md` and its verification, then the owner's answers. Findings BUG-0194 to
BUG-0199 (BUG-0192 and 0193 closed); review-tool points T-081.

# Handoff — updated 2026-10-29 (Claude Opus 5.5)

## State after Stage 18

Stage 18, the premium tax credit (Forms 1095-A and 8962), is built, reviewed in four rounds and committed:
`handoffs/HANDOFF-STAGE-18.md`. The estimate is 75.6% (from 71.0%). Adjudication found BUG-0188 to BUG-0191 (fixed)
and BUG-0192, 0193 (open, deferred to the next change of their forms); review-tool defects are T-079; PolicyEngine-US as
a Form 8962 engine is T-078. Next: Stage 19, the education credits. Its decision batch is drafted at
`research/premises/stage19-education-credits.decisions.md` and waits for the owner's answers before authoring. Its
estimate after the stage is 79.6%, so the 80% goal also needs Stage 21 (Form 5329).

# Handoff — updated 2026-10-27, later (Claude Opus 5.5)

## State after Stage 20

Coverage work resumed on the owner's route to 80% (`docs/2026-10-26_plan_revision.md` section E: Stages 20, 18, 19,
21). Stage 20, the capital loss carryover, is built, reviewed and committed: `handoffs/HANDOFF-STAGE-20.md`. The
estimate is 71.0% (from 68.6%). Next: Stage 18, the premium tax credit; start with its decision batch from
`research/premises/stage18-premium-tax-credit.md` and its verification, checked against the current tree, and stop
for the owner's answers before authoring. Open from Stage 20: BUG-0184 (wording), T-074, T-076.

# Handoff — updated 2026-10-27 (Claude Opus 5.5)

## State on 2026-10-27

Plan revision items A, B and C (except C2) are done, each committed behind a green check-all:
citations verifiable with `--strict` (63c0d98); TY2026 rehearsal (713a566) and its seven tool
defects fixed (BUG-0177 to 0179); OpenTaxSolver modelled exactly (f7d89e3); UsTaxes as the fourth engine
(a782c87; scoreboard 243/1,532, 15.9%); mutation-equivalence second reading, prose-only 0, and the
mutation step can fail check-all (7ef41bc); the transcription hold lifted per form (73b1ebe). The
next batch fixed BUG-0165 (line 25c omitted Additional Medicare Tax withheld; all four engines now agree),
BUG-0161, 0163 (car loan column (ii) prorated), 0169, T-071, and recorded BUG-0162 as a design limit
(entries BUG-0172 to 0176), with a fourth review round adjudicated.

**Coverage gate (plan revision D):** A, B, the rehearsal and UsTaxes are done, and every confirmed
amount-affecting defect is fixed. Open entries are display-level (BUG-0180) or tasks (T-067, T-068,
T-069(2), T-070, T-072, T-073). The rehearsal cannot build 2026 data until the final i1040gi posts
(expected early 2027). Remaining plan items run alongside coverage: C2 blind whole returns, 1.5/T-066,
2.2, 2.3, 2.5, and the 21 older Claude transcription logs, migrated when their forms change.

# Handoff — updated 2026-10-26 (evening session, Claude Opus 5.5)

**Read `docs/2026-10-26_plan_revision.md` first: it controls the execution order and the gate for
resuming coverage (TY2026 target).** The earlier handoff below remains the record of the state this
session started from.

## What this session did (plan revision item A, source adjudication)

- Built executable triage (`tools/transcription/triage.py`, `triage.mjs`; policy v2 compares what the
  values sheet shows): each disagreement's project line and validated model candidate are evaluated on
  every fixture, 500 generated returns and partial records, with witnesses and whole-return state.
- Adjudicated every open Claude transcription, render and class M ruling, and the DeepSeek logs of the
  same forms, in three rounds (method: `reviews/2025/transcription/adjudication/README.md`; one summary per
  form there). Seventeen legacy DeepSeek-only logs that predate the current comparison stay pending.
- Found and fixed BUG-0147 to BUG-0160 with regressions (tax-affecting: 0147 Schedule 1-A business tips,
  0148 section 179 over the limit, 0153/0158 head of household part-year rules, 0157 Form 2441 death-year
  rule, 0159 line 25b box). Owner's decisions: skipped lines are hidden with `shown_when`; a worksheet after
  a STOP counts as skipped; part-year questions for head of household; separated-spouses box recorded as
  `amb.2025.separated_spouses_box`; round 3 is the last before commit.
- Open from round 3, to fix next: BUG-0161 (Form 2441 non-dependent screen), BUG-0162 (line 28 ACTC
  box). Tasks T-067 (helper lines `shown_when` cannot hide), T-068, T-069 (review page gaps), T-070
  (review-tool defects).
- New check-all step `refusal_reach`: every refusal fixture's return must be refused under the full interview.
- Archives (git-ignored, hash manifests): `.transcription/archive/before-adjudication-fixes-2026-10-26/`,
  `before-round3-2026-10-26/`; round proposals under `.transcription/proposed/`.

## Next, per the plan revision

B: lift T-062's hold after the commit's audit. C: UsTaxes adapter (scout note: skip self-employed returns
pending the owner's answer), blind whole returns, TY2026 rehearsal, citation locators (with T-069),
mutation second reader, the OpenTaxSolver tolerance. Then fix BUG-0161/0162 and T-070 in the next batch.

---

# Handoff — paused 2026-10-26

**Superseded in its execution order by `docs/2026-10-26_plan_revision.md` (owner amendment, 2026-10-26).** The state recorded below remains the starting point.

The owner asked to stop at a clean point and continue in a fresh session. The in-flight review batches have finished. Work is paused; do not launch more work unless the owner resumes it.

The continuing objective is to clear the integrity roadmap through the point where coverage extension can resume. **That objective is not complete.** Remaining human packets and ruling samples are optional and do not block engineering. Preserve the owner's original verdicts and existing ambiguity decisions. Use **deepseek-flash**, never Pro. Fixed-prompt paid source/calculation reviews are authorized by `CLAUDE.md`. Do not spawn sub-agents under the current developer instruction.

Read this file first, then `CLAUDE.md`, `docs/2026-10-24_validation_policy.md` and the relevant portions of `HANDOFF-INTEGRITY.md`. The controlling roadmap is `docs/2026-10-22_integrity_plan.md`, amended by that validation policy.

## Repository and validation state

- Repository: `/Users/elliotmilco/Documents/GitHub/tax-formalization`, branch `main`.
- Last commit: **9bb8205 — Fix HSA partial inputs and validate native worked examples**. It passed the entire suite: 1,083 CLI fixtures; 1,700 engine cases and 320,581 comparisons with zero unexplained differences; 2,279 mutants with 128 equivalent survivors and zero unexplained survivors; 1,683 TypeScript/Lean cases with zero differences.
- There is a substantial **uncommitted source-review/tooling batch**. Preserve it, including untracked files. Do not reset, clean, or restore older logs over it.
- Current targeted checks pass: **130 review-tool tests, 11 input-context tests, 40 adapter cases, append-only bug inventory through BUG-0146, and `git diff --check`**.
- This new batch has **not passed check-all and is not ready to commit**. `check_logs.py` fails because required Claude source rulings remain open. This is an acknowledged review backlog, not a transport or receipt-corruption failure. Do not bypass the commit hook or weaken review checks to commit it.
- The most recent numeric scoreboard remains **209 / 1,515 computed lines (13.8%)** with outside-family assertions: H=0, B=0, second-family M=57, engine=163, with overlap. The new source audits/engineering checks earn no new numeric evidence.

The filesystem sandbox permits project edits but requires escalated execution for `.git` writes. `npm run check-all` writes a tested-tree marker; after a green run, do not edit tracked/nonignored files before staging and committing. Use a body file for the commit. No full suite needs to be run merely to rediscover the known open-ruling failure.

## What the uncommitted batch does

1. **Required-interface context**, `tools/transcription/input_context.py`: every own input plus direct foreign boundaries used by either the authored form or the returned candidate, including helpers, bindings, collection fields and refusal gates. The fingerprint binds ids, printed markers, types and complete input questions. Omitting a dependency cannot shrink the context; unrelated foreign wording does not stale it. Foreign authored arithmetic is not supplied or imported as context. The old global question diagnostic remains separate.
2. **Live verification** in `compare_families.py`: current context records are checked against the actual bound request/reply, current type checks and live fingerprint. Passing headers alone are insufficient. Both logs must cover the current source-target inventory. **The global BUG-0129/T-062 qualification hold remains.**
3. **BUG-0144**: the expanded refusal checker had retained its old policy identifier. Historical policies are preserved. Current checking is `project-expression-types-v3`; context policy is `required-review-interfaces-v2`.
4. **BUG-0145**: published input records imported authored computed refusal gates, falsely requiring hidden helpers such as `asset.screened` and `person.plan_screened` from independent replies. Candidate stubs now retain input identity/type/question metadata only. Gates explicitly returned by the model on an input are preserved and checked as model IR. No authored gate placement is borrowed. Tests cover both the false rejection and explicitly malformed model gates.
5. **Explicit verified replays**, `audit_transcription.py` and `transcribe.py --from-response`: verify log/request/reply/meta identity and an exact current request/model/system match, archive the parent, and label the derived comparison with its parent hash and original policies. Parent archives and chains are hash-checked, with a depth bound. Raw replies are never repaired. Direct `--from-response` never calls a model; `rerun_all.py --resume` **can fall back to a fresh call**, so use it deliberately.
6. **T-064 election adapter**, `adapter_contracts/2025/f4952.json`: `f4952.election` is the full supplied line4g amount after its scope/limit gates, not just its capital-gain portion. Nineteen host-only cases check it and `sd.investment_election`. Four explicit foreign Schedule B/D subtotals are isolated engineering boundaries; this does not independently validate those tax calculations. The runner forbids replacing the reviewed form's arithmetic or collection entries. Dividend adapter cases remain 21. Neither adapter earns source/numeric credit; printed tax results remain blind targets.
7. **Generic protocol clarification**: own collection catalogs list input fields only, rather than implying authored computed helpers are supplied facts. Foreign catalogs remain public interfaces. Prompts emphasize defining local computed references, correctly binding collection gates and preserving the exact published result types. No source arithmetic or expected answers were added.
8. **BUG-0146**: exported targets ignored helpers read only by foreign refusal declarations. Twelve targets across five forms were missed, including `household.hoh_fails`, which gates Form1040. Discovery now includes direct refusal/visibility references; both logs are checked against the live inventory even if the authored-form subject did not change. Some IRA targets are project scope bridges and need explicit semantic classification; do not automatically exempt them. The head-of-household predicate is a real source-review gap.

No authored tax form, numeric fixture, interview question or return engine has changed since 9bb8205 in this uncommitted batch.

## Actual requests, receipts and current results

**50 actual fixed-prompt requests finished with no transport failures**, under Claude Opus 5.5 and deepseek-flash:

- Thirty replacements: both families on `asset,carloan,eic,f8995a,household,ltc,person,qdcg,s179,s1a,s8812,sa,sales,sd,sdtw`. This replaces all fifteen unverifiable Claude receipts.
- Two Form4952 requests after adapter separation.
- Eight replacements after generic protocol clarification: Flash `carloan,eic,person,qdcg,s179,s8812,f4952`; Claude `s8812`.
- Ten expanded-target requests: both families on `household,ira,s1,s179,s3`.

Thirty-two additional host replays made **no model calls**. Some were superseded by later actual requests; their parent records remain archived. Do not rerun `.transcription/replay_current_source.py` blindly: it describes an earlier exact-prompt state, and current prompts/targets have since changed.

Final read-only snapshot: **`.transcription/handoff-audit-2026-10-26.json`**.

| Diagnostic | Count |
| --- | ---: |
| Verified saved replies | 110 |
| Unverifiable receipt/subject records | 0 |
| Pass current v3 type/refusal checks | 67 |
| Pass required-interface context | 68 |
| Bound metadata + current types + current context | 59 |
| Legacy-limited receipts | 21 |
| Earlier agreements changed by current replay | 160 |

These are diagnostic counts, **not qualification or tax-bug counts**. Historical logs may record an earlier checker version even when the read-only audit now passes them. Current Flash `f4952` and `s8812` remain type-invalid; current `carloan,eic,person,qdcg,s179,household,ira,s1,s3` pass types under both families. Other older invalid records remain too.

The final comparison report has 113 form-kind pairs, 24 eligible and 89 pending. Source T is held globally; eligible R/M pairs are separate. Model-error noise is 46/2232 (2.1%) across judged second-family rows, provisional for pending reviews; individual per-form limits still apply.

**Open source rulings: Claude 207, Flash 415**, listed in `.transcription/handoff-open-rulings-2026-10-26.json`. This is the immediate commit blocker. Sixty-six unusable-IR rows were explicitly adjudicated earlier and seventeen primary-source rows were ruled; later requests superseded some of those contexts. Do not carry rulings forward automatically or treat the historical totals as current resolved-row counts. All active rulings must match their sidecar/context.

## Useful investigation leads

A host-only diagnostic ran validated candidates on existing frozen fixtures, using the normal parameter-relative input resolver. It is **not independent worked evidence** and cannot qualify a source review. Files: `.transcription/model_fixture_diagnostics.py`, `.transcription/model-fixture-diagnostics-2026-10-26.json`.

- Claude Schedule D matched 32 selected existing cases; Claude Form8995-A matched eight. This can guide source adjudication but does not prove all branches or partial-input behavior.
- Claude Schedule1-A differed on four cases, mainly fields in inactive parts and one added Medicare refusal. Establish whether final deductions differ before treating inactive intermediate amounts as tax errors. Avoid the benchmark overconstraint previously fixed in HSA BUG-0140.
- Claude Schedule A requires an unanswered gambling-loss amount when known winnings are zero, leaving line17 unknown in three cases. The authored conditional avoids that question. This is a candidate availability gap; do not call the two formulas equivalent for all partial records just because complete-record arithmetic matches. A source-based partial-input bank may be appropriate.
- Household diagnostics originally exposed omitted head-of-household interfaces. The ten expanded-target requests now include the formerly missing targets; adjudication is still needed.
- Preserve `amb.2025.s179_carryover_no_property` and its owner-adopted research (T-043). The models' Worksheet1 cost cap is the recorded alternative, not automatically model noise. Their omission of wages from line11 is a separate source error (i4562 p.5).
- Preserve `amb.2025.carloan_ratio_places`; distinguish ratio precision from the separate ScheduleC/column(ii) availability issue. Do not hide all differences behind that ambiguity label.
- Form4952 line4d includes positive short-term gains; line4e is the separate net-capital-gain quantity (f4952 p.3). A positive declared line4g election needs the form even when the interest-deduction filing exception otherwise applies (p.4).
- Sales digital boxes G–L **are in the input enum**, but are refused at transaction aggregation by `sales.one`. Earlier scope rulings on G/J distinguish that refused regime; they do not certify ungated intermediate values there.

## Archives and commands

All current-session archives were hash-verified at handoff: **233 batch artifacts plus 32 replay-parent archives** under `.transcription/archive/`:

- `before-unverified-source-replacements-2026-10-26/` — 136 artifacts.
- `before-election-adapter-2026-10-26/` — 10.
- `before-source-protocol-clarification-2026-10-26/` — 40.
- `before-foreign-gate-targets-2026-10-26/` — 47.
- `verified-replays/<stem>/<parent-log-sha>/` — exact parent log, sidecar if present, prompt, response and metadata, with manifests.

The raw receipts and these archives are git-ignored, available in this workspace. Preserve them. No original human verdict was edited. Earlier HSA and human-policy archives remain documented in `HANDOFF-INTEGRITY.md`.

Targeted checks:

```sh
python3 tools/transcription/test_review_tools.py
python3 tools/transcription/test_input_context.py
python3 tools/transcription/adapter_contracts.py
python3 tools/check_bug_inventory.py
git diff --check
```

Read-only audit and reports:

```sh
python3 tools/transcription/audit_transcription.py --report .transcription/next-audit.json
python3 tools/transcription/compare_families.py
python3 tools/transcription/check_logs.py
```

The last command currently fails on open required Claude rulings. Final logs are `/private/tmp/tax-handoff-{review-tests,context-tests,adapter-tests,bug-check,audit,families,check-logs}.log`. Request summaries are `.transcription/{source-replacements,election-adapter,source-protocol,foreign-gate}-{claude,flash}-2026-10-26.json`.

## When the owner resumes

First review the diff and current audit; finish source adjudication, replacing truly invalid IR with actual fresh source requests where needed. New calls must retain the selected models and fixed-prompt isolation; archive before overwriting. Do not repair returned IR, fabricate human readings, suppress inconvenient disputes, or release T-062's hold prematurely. Complete required checks before committing the resulting tree.

The broader roadmap still includes source migration/qualification, remaining native M migration and blind whole-return calculations, UsTaxes integration as the fourth engine, mutation-equivalence mechanization, Direct File predicate comparison, **301 citation locators**, and the year-adoption rehearsal. Do not resume coverage extension merely because this source-review batch is done. No further mandatory owner review packets are needed.
