# Handoff: the integrity plan, Phase 0 done, Phase 1 in progress

## Current expression-validation repair after bdb2e12 — 2026-10-25

bdb2e12 committed the literal-unit repair after a full green suite. The follow-up now validates
returned expressions against the project schema and the build's reference/type checker, without
executing them. It replaces only the reviewed document, preserves published input types, rejects
new inputs and changed result types, and does not borrow omitted authored computed helpers.
This is expression/reference/type validation, not citation, guard-exhaustiveness or tax correctness
certification. All 55 authored definitions pass the same adapter; 84 offline review-tool tests pass.

New logs use checked-expression-types-v2 and project-expression-types-v1. Invalid dependencies
prevent line agreement; any invalid helper prevents a form type pass and a successful tool exit.
BUG-0132 repairs missing count/proration/table-key/collection-field dependency traversal.
Both families need passing current type and complete-input-context checks before qualification,
even after the global hold is eventually removed. Request completeness checks the actual prompt;
it does not relabel the original prompt policy or upgrade an incomplete request receipt.

BUG-0131 removes 160/220-character cuts that omitted late enum meanings and scope exceptions.
Four fresh source-only requests (dcprov/dependent, Claude/Flash) include the full questions. Both
provider replies agree on two results and pass types. Claude's dependent reply passes types but
still has source/interface omissions; Flash's fails on bare Bool tests and collection binding.
The 24 disputed sample rows are adjudicated, retaining explicit limitations and pending status.
No model output was repaired into an agreement. Originals (18 files) are hashed under
.transcription/archive/before-expression-validation-2026-10-25/; raw fresh requests stay intact.

The current read-only audit verifies/recompares 82 replies: 26 pass expression validation and
211 former AGREE rows become disagreements under the stricter checker. Twenty-three receipts
remain legacy-limited. The other 28 Claude records remain unverified/not re-comparable (27 prompt
hash mismatches, one conflicting definition id). See reports/2025/transcription_audit.md and
.transcription/expression-type-audit-current.json. The older nine-loss and 202-loss audit snapshots
are historical intermediate diagnostics. No bulk review migration has happened.

T-062 remains open: verify/replay qualifying original requests, issue fresh requests for incomplete
or unverified records, obtain valid replacements for rejected IR and adjudicate remaining source
issues. Keep the global transcription hold; do not promote Flash. No authored tax rule, numeric
fixture or human verdict changes in this batch; the numeric scoreboard stays separate. Full-suite
validation is recorded by the next commit/check marker, not inferred from these targeted checks.

## Current literal-unit repair after commit 2fdec33 — 2026-10-24

2fdec33 commits the age-at-care correction, deduction presentation changes and transcription hold
after a full green suite: all 1068 CLI fixtures, 1700 engine cases with zero unexplained differences,
and the unchanged 2278-mutant report (94.4% raw, 100% adjusted).

The next repair preserves literal Count annotations and zero/one parameter units, propagates parameter
types into foreign helpers/shared definitions, and stops treating numeric zero/one as Boolean values.
New transcription logs record comparison policy typed-literals-v1, included in ruling context hashes.
BUG-0130 repairs the missing Count-literal syntax in the generic prompt grammar. Old prompts/replies
are not relabeled as having seen that syntax. All 69 offline review-tool tests pass.

`audit_transcription.py` is a read-only comparison audit. It checks current subjects, saved prompt
hashes, metadata and the reply embedded in the original log, then writes a diagnostic report only.
It verified/recompared 82 replies (all 55 Flash and 27 Claude), including 23 explicitly legacy-limited
receipts; nine former agreements now disagree (Claude f1040:2, s1:1; Flash person:5, sa:1). Of the other
28 Claude records, 27 saved prompts fail their recorded hashes and one reply has conflicting definition
ids. They are reported as unverified/not re-comparable rather than silently repaired or reused.
Details: `.transcription/typed-literal-audit.json`; no existing log, ruling, fixture or raw reply changed.

This repairs unit preservation, not all returned-model IR typing. T-062 still requires type validation,
verified migration/fresh requests and adjudication. Keep the global transcription qualification hold
until those close. The numeric scoreboard and render/model-worked evidence remain separate.

## Current follow-up after commit 735e644 — 2026-10-24

735e644 commits the accumulated integrity work and optional-human/secondary-evidence policy.
Its full check-all passed: 1065 CLI fixtures, 1700 external-engine cases / 320581 line comparisons
with zero unexplained differences, and 2278 mutants with all survivors accounted for as equivalent
(94.4% raw, 100% adjusted). That result applies to the committed baseline.

The held BUG-0111 patch is now integrated: the new timing question is needed at the disabled child's
age 13 boundary; six targeted checks pass without changing the existing monetary results. Both
families' T/R reviews and the required Claude M run were refreshed and adjudicated. The six M cases
include both sides of the new timing question, with 388 agreements and two fragment-interpretation
values dropped. BUG-0128/T-059 clarifies the four standard-deduction presentation findings; all 16
isolated human-path tests pass and item2 regenerates. The owner's original logs remain unchanged;
new tool/bank receipts earn no H without a new reading, which is optional.

The review audit found BUG-0129: transcription normalization erases literal units. Missing Count
annotations in both new model replies can compare equal to typed project constants while evaluating
to unknown. This is a model/comparer defect, not a newly established project tax-value error. All
transcription qualification is now held until type preservation and a prior-agreement audit are done
(T-062). The report now has 23 eligible and 89 pending comparisons; the numeric scoreboard is separate.
58 offline review-tool tests pass, including the hold regression. Do not remove the hold merely to
restore the former eligible count. Repair it before additional transcription qualification/promotion.
Full-suite validation of this follow-up is recorded by its subsequent commit and check marker;
targeted checks above are not themselves a new full-suite claim.

## Controlling owner revision — 2026-10-24

The owner finished item2: fourteen saved/current answers, ten MATCH, three MISMATCH, one UNCLEAR.
He then approved removing the remaining mandatory packets and the ten-ruling sample. Human readings
are optional; stale/incomplete/negative readings earn no H and do not block unrelated validation or
reporting. Malformed records and incorrect identity/authorship still fail. The former freeze while
he read and automatic doubling of the reading list are superseded. Do not assign another sitting.
Preserve his verdicts and never migrate old receipts into current H credit without a new reading.

Read `docs/2026-10-24_validation_policy.md` and the amended plan before the historical continuation
below. The new priority is independent source and whole-return checks, four engines, defect corrections
with broader independent regression coverage, then citations/proofs and the year rehearsal. Coverage
expansion stays paused until those gates close, not until a human packet list is exhausted.
Online tax commentary is now allowed as separately recorded soft corroboration in `research/secondary/`.
It cannot override explicit archived instructions, enter blind source-only prompts or earn scoreboard
credit. The first example addresses standard-deduction increments. Engineering responses to the four
saved presentation concerns are in `reviews/2025/human_findings.md`; they remain presentation tasks.

BUG-0127 implements the optional-review gate. `check_logs.py` and the evidence generator now run
successfully while preserving every original owner log byte. The regenerated scoreboard is 198/1515
(13.1%): H0, B0, second-family M44, E163, with overlapping sub-counts. These are line assertions,
not a claim that f2441's missing STOP outputs or form-level qualification are resolved. No new
full-suite green marker is claimed. Historical stale-scoreboard notes below are superseded.

## Historical execution record — superseded where noted above

The following sections preserve earlier work, waiting conditions, source-review requirements and
scoreboard snapshots. They are not current instructions to require owner packets, freeze the active
definitions or keep the report blocked. For current execution use the controlling revision above,
the amended v7 integrity plan and `docs/2026-10-24_validation_policy.md`. `HANDOFF.md` is historical
Stage0 background. Coverage expansion still awaits the independent-validation and year-rehearsal gates.

## Continuation: standard-deduction review path

The human-reading milestone now has distinct H (source reading) and B (worked values) evidence.
`logs.py` validates the same receipts for the log checker and evidence report. Receipts cover the
printed reading and expanded helpers across forms; older browser submissions are rejected. H is
credited only after a MATCH with a reason is committed with the named reader as author. Blank and
partial saves preserve earlier completed entries. MISMATCH/UNCLEAR are saved but block the check.
The owner has begun saving real reviews; they remain his work and are not a completion signal.
Invented test verdicts stay in temporary repositories.

After the owner found the single-verdict packet overwhelming, item 2 now presents fourteen short
questions, one at a time, each beside its own source excerpt. A saved verdict credits only that
computation; references to other amounts are named and checked separately. The owner can stop after
any saved check. Full pages remain available. BUG-0104 records the usability finding. BUG-0105 adds visible validation beside Save & next,
focuses missing required fields, and preserves draft notes across a packet update. The browser test
now uses actual pointer clicks and exercises incomplete forms and rejected saves. The other packets should be
regenerated after the owner judges this one. `test_review.py` checks the full path in an isolated
repository in check-all; `test_browser.mjs` checks the browser and a separate temporary server.
The evidence report runs after the engine differential so it uses the current run's summary.
BUG-0101 to BUG-0103 record these findings. The owner is reading item 2 while independent work
continues at his request; no human source reading or worked-value assertion has been supplied by an agent.

## Continuation: independent validation, 2026-10-23

**Owner correction, 2026-10-23:** use `deepseek-flash` for second-family work. The Pro selection
in earlier handoffs was a mistake. Remaining Pro jobs were interrupted, then the owner resumed
work with Flash. Pro artifacts remain accurately labeled and are preserved with hashes under
`.transcription/archive/pro-before-flash-2026-10-23/`. The 110-job Flash run completed with no
transport/parser failures; summary is `.transcription/deepseek-flash-full-summary.json`.
`families.json` pins Flash and the transport and eligibility gate enforce it (BUG-0115).
All 57 offline review-tool tests pass; BUG-0118
accelerates local prompt preparation with identical parsed data and prompt bytes.

As of 2026-10-24, BUG-0117/0119/0120 source corrections are applied and both families' affected
render reruns accept them. BUG-0121 binds reused rulings to their actual review context. All
fourteen item-2 receipts are unchanged. BUG-0122 strengthens worked-value sampling after its
random corpus lost active Form 2441 cases. Fresh Claude/Flash value reviews completed six active
cases: 138/151 numeric agreements respectively; skipped replies are excluded. BUG-0123 removed
220 historical false M assertions that came from blanks; the raw/derived originals are archived.
The current skip audit is clear. Flash M remains pending three
skipped required line-29 results. The Flash f2441 transcription remains
ineligible (five model-error lines out of 37, plus four open rulings); do not lower the noise floor.
The evidence report could not refresh because the human validation gate correctly fails on the
owner's unresolved findings. Its older snapshot is explicitly marked stale. Do not claim a new
scoreboard, family promotion, human completion or a current full-suite green marker.

Read `docs/2026-10-23_independent_validation.md` for the current work. The review tools now enforce
the agreed model-error noise rule, omit computed labels from independent transcriptions, bind
cached transcription/render/class M responses to their actual request, and normalize exact definition
interface aliases (BUG-0106–0110). BUG-0112 also rejects malformed or duplicate raw judgments
before they can disappear in lookup maps. BUG-0113 repairs direct connection-reset retries;
BUG-0114 binds per-run output allowances and rejects truncated output. Thirty-four offline
regression tests cover these changes.
The earlier Pro batch and retries below are historical. Current transcription and render logs
all request/report Flash. Affected-fix summaries are `.transcription/*-wording-fixes-summary.json`
and `.transcription/*-line14-summary.json`; class M progress logs are under `/private/tmp/tax-classm-f2441-*-review.log`.
Disagreements require cited
rulings before qualification; DeepSeek remains optional and coverage remains paused.

BUG-0111 has a tested staged fix in `docs/patches/BUG-0111.patch`: rebased after the new boundary
fixtures, its isolated build, all 1066 CLI fixtures and six age/timing checks pass. It is not applied.
Item 2's form dependencies exclude dependent,
but registering the new interview question changes the bank hashed into every human receipt.
Hold the patch while the owner reads, then refresh receipts deliberately when applying it.
Current parsed Form 2441 class M counts and qualification blockers are saved in
`.classm/f2441-current-summary.json`; use them and the derived review logs rather than older
pre-blank-parser run summaries.
Keep forms frozen during those batches so their subject hashes describe what was actually read.
Do not change the human packet or its dependent forms while the owner is reading. His partial
MISMATCH about the per-box deduction amounts is saved and unresolved; investigate presentation
with him after he reports completion. It intentionally prevents a green log check. The earlier
full-suite green marker predates these changes; no current full-suite pass is claimed.

### Source adjudication continuation, 2026-10-24

BUG-0124 adds the missing i1040gi p.117 citation for Schedule 3 excess withholding. Flash's
refreshed maximum-reasoning transcription now agrees on line11; its four remaining differences
are documented representation/application guards, with no open ruling. Initial wrong-worksheet
answers remain archived with their original incomplete context. BUG-0125 repairs transitive render
glossary definitions and includes the sources of exposed helpers. BUG-0126 supplies i1116 p.25's
regular-tax definition. Both families' refreshed s3/ftc/f2441 render objections are adjudicated with
explicit scope/input limits. Every required Claude transcription/render/class M log is current and
has no open ruling. Flash W-2 and Additional Medicare render reviews match every line.

Flash W-2 hand-work adds 39 matching numeric results across three W-2 entries in one return.
Its focused transcription retry fixes the omitted EE deferral; a separate 1152-case comparison
checks the remaining expression on supported complete inputs. The current second-family report
has 112 form-kind pairs: 37 eligible, 73 pending, two with no judged lines. f4952 transcription
still exceeds the noise ceiling; retirement transcription still has four open differences.
The human gate remains unresolved and coverage expansion remains paused.

The three Form2441 line29 gaps are a STOP presentation issue: Flash worked the differences
(-2000, -500, -1300 dollars) but left the numeric outputs blank. They are not unworked arithmetic,
nor are they numeric zero assertions. No owner decision on this convention is inferred. See
`.classm/f2441-current-summary.json`. The fourteen active packet receipts remain unchanged.
Default citation validation has zero findings; 301 strict locator segments remain to rewrite.
Fixture verification covers all 1065 cases: the full run passed 1060 and found five refusal-citation
metadata differences from BUG-0126. Only their expected locators were updated, and all five pass a
targeted CLI rerun. No numeric expectations, inputs, gates or remedies changed in that update.
The review server returns HTTP 200 on item 2.

## Where the plan stands (prior batch)

- **Phase 0 (honest reporting): done**, commit a946fae. Evidence report with M and E columns and the scoreboard;
  citation check on computed lines (305 locators to rewrite, `--strict` not yet in check-all); LICENSE,
  LICENSE-DATA, README, `handoffs/`; spec 6.5 and 3.11 qualified; BUG-0089 to BUG-0093.
- **Phase 1, first batch: done**, commit ac69196. 1.0 packet tool; 1.0b DeepSeek transport; 1.3 per-family review
  logs, `families.json`, `compare_families.py`; 1.4(a) per-form engine lines and the not-computed floor; 1.6 spec 4.7
  and `reports/2025/equivalence_review.md`; 1.7 `reviews/2025/direct-file/predicates.md`. Scoreboard 38 of 1,510.
- **Phase 1, second batch: in progress at handoff** (see "Uncommitted work" below for exact state):
  - the fixes for BUG-0094 to BUG-0097, BUG-0092, the owner's new refusals (decision 10) and the Tax Computation
    Worksheet re-keying (decision 11), each in an agent worktree with its Claude reviews rerun;
  - 1.4(b) OpenTaxSolver adapter (23.06; the owner is to download 23.07, see below);
  - the reading packets reworked for a human reader (item 2 first, for the owner's look);
  - the reading list doubled to 26 items (decision 13);
  - README rewritten as the trust pitch (owner's instruction).
- **Not started:** 1.4(b) UsTaxes adapter (scouting note `/tmp/tax-audit1/ustaxes_scout.md`, may be gone: the clone
  is at `.engines/ustaxes-src/`, commit d276c72); 1.2 DeepSeek whole-return class M; 1.3's full DeepSeek run over
  the 55 forms (do it after the fixes land so it reads the corrected encodings once); 1.5 class M on printed
  lines; 1.6 second reader and mechanization (8 stale `EQUIVALENT_IF` entries to remove; checker rules for the
  evaluator divergences D2 and D6 and a shared reason string for D5); 1.1 the owner's reading; Phase 2.

## Stop rule

Fired 2026-10-22 with three value errors on reachable returns: BUG-0094 (Schedule A medical floor at negative AGI),
BUG-0096 (EIC filer SSN definition), BUG-0097 (no Form 8862 gate). Coverage stays paused; the reading list was
doubled. Findings from 1.1 to 1.4 and 1.7 keep counting.

## Facts a fresh session needs

- **Agents run on Opus 5.5** (owner's instruction 2026-10-22): pass `model: "opus"` on every Agent launch.
- **DeepSeek**: the key is in the macOS keychain (service `deepseek-api`, account `elliotmilco`); `call_model` reads
  it at call time; never print it. Use `deepseek-flash` for reviews (owner correction 2026-10-23).
  Transport check: `python3 tools/transcription/transport_check.py`.
- **Review logs per family**: `<form>.<family>.md` beside the Claude log; `tools/transcription/families.json`
  (claude required, deepseek optional until all 55 forms have logs). Policy (decision 14): a stale optional log
  fails check-all; an open ruling in an optional log does not. `compare_families.py` writes
  `reports/2025/second_family.md`; the agreement floor is now the implemented model-error noise rate
  (decision 12), with raw agreement retained only as a diagnostic.
- **OpenTaxSolver**: 23.06 built at `.engines/opentaxsolver-src/` (from tenforty's vendored tarball; SourceForge
  blocks scripted downloads). The owner is to download the 23.07 Linux package in a browser into that directory;
  the adapter reads the version so the swap is a rebuild. 23.06 has three known defects declared as limitations.
- **Human reading**: `python3 tools/human_review/packet.py --all` then `python3 tools/human_review/serve.py`
  (127.0.0.1:8790); logs to `reviews/2025/human/<form>.md`; the reader field must equal the git author name. The
  owner found the first packets unusable (audit English, wrong pages); the rework (per-line pages from citations,
  highlighted quotes, helpers folded into printed lines, worked examples) was being judged on item 2 at handoff.
- **check-all**: about 7 minutes; the green marker counts only if no tracked file changes during the run, so make
  no edits while it runs; the pre-commit hook refuses any other tree. Commit messages go through `-F <file>`.
- **Worktrees**: agents that edit `forms/` work in `.claude/worktrees/agent-*` with `node_modules` and `.engines`
  symlinked from the main tree; merge with `git -C <wt> diff -- <paths> | git apply`, then
  `git worktree remove --force <wt>` and `git branch -D <branch>`.
- **BUG entries** are appended before or with the fix; the parent session writes them so parallel agents do not
  collide on ids. Next id at handoff: BUG-0098 (the Tax Computation Worksheet keying, first second-family yield).

## State at handoff

- **Commit 0186a66 ("Preserve current project work and name project us-tax-model")** was made by the owner at
  21:35 on 2026-10-22, outside this session and without a green check-all (the hook was bypassed). It swept the
  main tree's uncommitted second-batch work into HEAD and renamed the project in `README.md`'s title and
  `package.json` to `us-tax-model`; the directory and `PROJECT_INDEX.md`'s title still say tax-formalization.
- **The second batch is merged on top of it** (the household and credit fixes, the Schedule A fix, the worksheet
  re-keying, the OpenTaxSolver adapter, the reworked packet tool, the second dozen reading items, the README) and
  committed only after a green check-all; see the commit that follows 0186a66, or the working tree if it is not
  there.
- **Scoreboard** before the second batch: 38 of 1,510. The OpenTaxSolver adapter alone brings 169 lines under the
  rule; read the first line of `reports/2025/evidence.md` for the current figure.
- **Fixed in the second batch but recorded "open" in committed inventory entries** (the file is append-only):
  BUG-0092 (Form 8889 reads `household.married`), BUG-0094 (`sa.agi_floor`), BUG-0095 (`dependent.claimed_no_tin`),
  BUG-0096 (`person.eic_ssn`, `household.all_eic_ssn`), BUG-0097 (`household.credit_disallowed`). The closure
  convention for a committed open entry is the owner's to set (a new entry citing the old, per spec 6.6, or a
  TASKS row). BUG-0098 to BUG-0100 are recorded; 0099 and 0100 are value-neutral and still open.
- **Class M corpora** for tcw, sa, f1040, dependent, eic, f8889, person, s8812 were regenerated by `classm-jobs` in
  the agent worktrees with a fresh greedy cover (fewer cases for sa: 6 instead of 14) and merged per document into
  `fixtures/2025/classm.json` and the git-ignored `.classm/jobs.json`. If the former sa cases' evidence is wanted
  back, merge the old jobs (HANDOFF-STAGE-16, "Class M jobs").
- **Flags for the owner's judgment:**
  - The OpenTaxSolver adapter allows up to 13–17 cents of difference on some tax lines (`OTS_SUBCENT`), set from
    the count of unrounded multiplications and the observed spread. Spec 6.2 forbids tolerance by margin; the
    allowance needs a derived per-line bound like the float categories, or must go.
  - The second-transcription prompt shows the project's own labels for printed lines, including authored helper
    labels (the Schedule A agent saw "Amount from sa.agi_floor" in the prompt), so a second transcriber can follow
    the project's structure rather than the page's. A TASKS row is warranted.
  - The agreement floor as a noise rate (decision 12) is in the plan but not yet in `compare_families.py`.
  - The reworked item 2 packet (helpers folded into the nearest printed line, Form 1040 line 12e) awaits the
    owner's look; the other 25 packets are built with the old layout and need `packet.py --all` after any further
    change.
  - OpenTaxSolver 23.07 is still to be downloaded by the owner; 23.06 limitations are version-keyed.
- **Stop rule:** three value errors (BUG-0094, 0096, 0097), all now fixed; the rule's consequence (coverage paused,
  reading list doubled) stands until the owner's reading has run.

## Next steps, in order

1. Merge the three worktrees, run check-all, commit the second batch (one commit, listing items).
2. Owner judges the reworked item 2 packet; regenerate all 26 packets; owner reads items 1 to 13, then 14 to 26.
3. UsTaxes adapter (engine 4), after OpenTaxSolver lands.
4. Full DeepSeek run: `rerun_all.py --model deepseek-flash` for transcription and render over all 55 forms; rule
   every disagreement with a source quote; implement the noise-rate floor in `compare_families.py`; move deepseek to
   required in `families.json` when every form has logs.
5. 1.2: extend `classm.py` to work a fixture case as a job (every document the case reaches), run DeepSeek over the
   3 to 5 chosen returns and the ~40 blind-predicted returns; relabel them M.
6. 1.5 class M on printed lines; 1.6 cleanup (stale entries, mechanization, checker rules D2/D6, D5 reason).
7. Citation rewrites (305 segments, `reports/2025/citations.md` "Locators to rewrite"), then `--strict` into
   check-all.
8. Phase 2: TY2026 rehearsal on the posted drafts; "complete" in spec 2.4; prevalence buckets; product surface.
