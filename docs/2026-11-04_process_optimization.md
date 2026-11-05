# Development-process optimization — 2026-11-04

Opportunities to reach the same integrity at lower inference cost or with less work, from a read-only
analysis of the process. Ephemeral: delete once its items are done or declined.

**Evidence base and limits.** The paid-call ledger `.transcription/costs.jsonl` (489 calls,
2026-11-04 02:07 to 15:29 UTC, about 13 hours) and `research/costs/agent_runs.jsonl` (61 runs,
2026-11-03 and 04). Gains are extrapolations from one day of data, not measurements. Claude dollars
are the list-price equivalents `claude -p` reports; under a subscription they stand for quota.

## Same integrity, ranked by gain against effort

### 1. Disable prompt caching on one-shot review calls — about 44% of Claude review spend

Every Claude call writes a 1-hour prompt cache that is never read: over 288 Claude calls, 24.0M
cache-write tokens against 44k cache-read tokens. A fit of the reported per-call costs against their
token counts gives $4/M input, $8/M 1-hour cache write and $20/M output, with near-zero residual, so
each review pays double for its input and gets nothing back.

- How: set `DISABLE_PROMPT_CACHING=1` in the environment of `_call_claude`
  (`tools/transcription/transcribe.py`). Not yet confirmed that `claude -p` honours it; one real call
  settles that.
- Gain: about $96 of $220 Claude spend in the window; roughly $15–18 on a round like round 2 ($41)
  or round 3 ($37).
- Integrity: none changed; same prompt, same model.

### 2. Transcription subjects ignore wording — removes wording-only transcription reruns

Owner decision 2026-11-04: yes.

`transcription_line_subjects` (`tools/transcription/subjects.py`) hashes each line with only `cite`
removed, so a `label`, `help` or `note` edit stales the transcription log. Target lines' project
labels are not in the transcription prompt ("Project-written labels and expressions are deliberately
omitted"), and `compare()` decides AGREE or DISAGREE from expressions alone; the label is copied into
the result row for display only.

- How: exclude `label`, `help` and `note` from the transcription line subject, as `of_computation`
  does for class M. Keep `expr.source`, which does reach the prompt. Wording stays covered by the
  render and completeness reviews.
- Gain: the window's Claude transcription was $122 for 0 findings and 0 bugs (395 rulings, half model
  error); round 2 was $20.48 for 0 findings.
- Residue: a log's displayed label can lag the YAML until its next real rerun (display only).

### 3. Line-scoped prompts carry a scoped catalog — roughly 30–50% fewer input tokens per scoped transcription

A line-scoped review of two lines (`sales.e`, `sales.g`) sent 480k characters: 300k of catalog (62%;
149k collection entry-field descriptions, 79k lines on other forms, 33k screening inputs), 155k of
IRS pages and 23k of data model. Scoping trims the excerpt, but the catalog is built for the whole
form.

- How: build the collection, screening and other-forms catalog from what the scoped lines reach plus
  the documents on the excerpt's pages.
- Integrity: small risk that the model lacks an id it needs; the interface check flags that. A prompt
  change, so it applies at each form's next change.

### 4. One review per form per round, after all its fixes — about 30–50% of a fix-heavy round's review spend

`sales` was reviewed 8 times on 2026-11-04 (transcription, render and completeness each time, about
$2.50 a pass), four of them between 10:40 and 11:09. Fixing lows is a change, the change triggers a
review, the review finds new lows.

- How: finish every fix to a form within a round before its review; a round that finds only lows
  starts no further round, and those lows wait for the form's next substantive change.
- Integrity: same; the final tree is reviewed.

### 5. check-all reuses unchanged steps — about 20+ minutes per bookkeeping-only commit

The pre-commit hook requires a full green check-all on the exact tree, including `TASKS.md`-only
changes. Wave 2 is bounded by mutation (713 s before tier 3; tier 3 is now about 22 minutes), the
engine differential (547 s), the Lean comparison (309 s) and fixtures (257 s). 25 commits since
2026-11-01.

- How: each step declares its input paths and records their hash with its result; a step whose
  inputs match its last green run reuses the result. A full uncached run stays on `pre-push` (or
  nightly) to catch undeclared inputs. Later: cache mutation kills per form.
- Integrity: same, given complete declared inputs, backstopped by the full pre-push run.

### 6. Route mechanical agent work to Sonnet — likely 10–25% of agent tokens (unmeasured)

59 of 61 logged agent runs were Opus (15.4M tokens) despite the 2026-11-03 decision. Packages such as
`r2-help-text` and `r3-forms-c1/c2/c3` (applying T-229 lows) look mechanical. Adjudication is 34% of
agent tokens (5.3M) and stays on Opus. `cost_usd` is null in every row.

- How: record each package's model and its class (mechanical or judgment) in the brief and in
  `agent_runs.jsonl`.

### 7. Smaller adjudication input — a share of the 5.3M adjudication tokens

About 42% of window rulings were model error (DeepSeek transcription 77%; 1 bug in 1,488 rulings
all-time). T-224's mechanical model-error rulings cover part of this.

- How: auto-rule disagreements where executable triage shows identical values on every fixture and
  the generated returns; agents see only the residue. The threshold is an owner call.

### 8. Bookkeeping writes through tools — unmeasured

`BUG_INVENTORY.md` is 596 KB, `TASKS-DONE.md` 129 KB and `PROJECT_INDEX.md` 37 KB. A tool that
assigns the next id and appends would keep agents from loading them. Not verified that agents read
them whole today.

### 9. Stop a family after its first usage-limit error — small

57 of 61 GPT-6 Astra calls failed on the usage limit; `rerun_all.py` kept calling.

## Trade-offs that lower integrity (owner decision, not recommended by default)

- Cheap family first for render and class M, Claude only on disagreement. DeepSeek class M is cheap
  ($0.18 in the window) and supplies all 32 class-M-only mutation kills, while Claude class M was
  $8.36 with no findings; but Claude is the required family, so the evidence would mean something
  different.

## What was checked

Inspected: the ledger aggregated by kind and family with cache tokens; per-token prices fitted to 288
reported Claude costs; section sizes of the scoped `sales` prompt; `subjects.py`; `_call_claude`;
`compare()`; the check-all wave layout and its last step timings; `reports/2025/review_yield.md`; the
agent-run log.

Inferred (unverified): that the caching flag works; the size of the catalog-trimming saving; whether
agents read the large bookkeeping files; every extrapolated gain.

## Implementation plan (for the coordinating session)

Written by a separate analysis session for the coordinating session, which owns scheduling and
execution. Nothing here is authorized to launch yet: see "Open owner decisions".

### Packages

**A. Review tooling** (items 1, 2, 3, 9; all in `tools/transcription/`, one owner, Opus).

1. Caching off: set `DISABLE_PROMPT_CACHING=1` in `_call_claude`'s subprocess environment. Verify with
   one real call (about $1): the ledger row should show `cacheCreationInputTokens` 0 and about half
   the input cost. If the variable is not honoured, the fallback is reordering prompts so stable
   sections come first (a prompt change, smaller saving).
2. Wording-blind transcription subjects: drop `label`, `help` and `note` from
   `transcription_line_subjects` (keep `expr.source`). The hard part is migration: every log's
   recorded subjects were computed the old way, so the change alone would stale every form, which
   the owner's no-global-re-review rule forbids. Add a no-call migration (like the `--lines auto`
   path): a log whose old subject matched the YAML at its commit gets its subject recomputed the new
   way. Tests: wording edit not stale; `expr.source` edit stale; migration idempotent; a genuinely
   stale log stays stale.
3. Scoped catalog: in the line-scoped path (`transcribe.py`, after `scoped_doc`), build the
   collection, screening and other-forms catalog from the scoped lines' reach plus the documents on
   the excerpt's pages. Validate with dry-run prompt sizes on several forms (free), then an A/B on two
   or three forms with known logs, scoped against unscoped, expecting the same verdicts (about $3–5).
   A prompt-policy change: prospective, at each form's next change.
9. Circuit breaker: `rerun_all.py` stops calling a family after its first usage-limit failure.

**B. check-all step reuse** (item 5; `tools/check_all*.sh`, `tools/green.sh`; one owner, Opus;
riskiest package, about a day).

- Each step declares its input paths; a step whose input hash matches its last green run reuses its
  result. Start coarse: anything under `engine/`, `tools/`, `forms/`, `params/`, `tables/`,
  `fixtures/`, `interview/`, `schema/`, `lean/` or `sources/` is an input to every step.
- Validate: uncached and cached runs on the same tree produce identical outputs.
- Move the full uncached run to `pre-push` (about 25 minutes per push; owner decision pending).
- Steps that read bookkeeping files still run (`check_bug_inventory`, `coverage_tree`).
- Per-form mutation-kill caching is a later, separate package.

**C. Triage auto-rulings** (item 7; extends T-224; Opus, 2–4 hours). Blocked on the owner's
threshold.

**D. Bookkeeping tools** (item 8; `new_bug.py`, `task_row.py`: assign the next id and append, with
tests; Sonnet, 1–2 hours).

**Guidance only** (items 4 and 6; no code). Draft text for the project `CLAUDE.md`, to be shown to the
owner and approved before writing:
- one review per form per round, after all its fixes; a round finding only lows starts no further
  round (optional guard: `rerun_all.py` refuses a second review of a form in a round without
  `--force`);
- every agent brief and `agent_runs.jsonl` row names its model and its class (mechanical or judgment).

### Order

A first (1 and 9 first within it), before the next Claude review round. B in parallel (disjoint
files). C after the owner's threshold. D whenever. One `TASKS.md` row per package (improvements, not
defects: no bug entries). Each package commits behind a full check-all; 3–4 commits.

### Cost

Paid calls about $5–7; no reruns of existing reviews. Agent tokens roughly 1–1.5M Opus plus a small
Sonnet package.

### Open owner decisions

Settled: item 2 (yes, 2026-11-04).

Open:
1. Implement now, or only register the packages as `TASKS.md` rows to schedule?
2. Package B: is a full uncached check-all on every `pre-push` (about 25 minutes) acceptable as the
   safety net?
3. Package C: when executable triage shows identical values on every fixture and every generated
   return, may the disagreement be ruled model error with no agent, or should agents still see a
   sample?

The launch also needs the intent readback the owner's rules require for work of this size: the goal
as read is cheaper review rounds and commits with every check producing the same evidence; the
plausible misreading is that the owner wanted a backlog to schedule rather than work now.

### Working-tree note

The analysis session left two uncommitted changes: this file (new) and one clause in the `docs/` row
of `PROJECT_INDEX.md` pointing to it. `TASKS.md` was already modified before that.
