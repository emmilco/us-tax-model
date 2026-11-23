# Working guidance for this project

**Start here.** `HANDOFF-NEXT-SESSION.md` is the current state: what is on `main` (released) and `next` (integrated,
unreleased), what is in flight, and what governs each kind of work. Then the top of `TASKS.md` (the order of work; the register is authoritative for each
task's status).

**Normative documents.** Read the one that applies before the first change of that kind:
- any work: `docs/consolidation_charter.md` (architecture, verification system, order of work, documentation
  conventions);
- validation, rulings and human review: `docs/2026-10-24_validation_policy.md` (human packets and ruling samples
  are optional; proceed without waiting for them and preserve original verdicts);
- adding or changing an interview question, topic or form: `docs/2026-11-13_interview_construction_protocol.md`
  (owner decision 2026-11-13; the standard, norms N1 to N12, the phases, how agents are briefed, the checklist for
  extending coverage);
- extending coverage to a new area (a form, schedule, worksheet or situation now refused):
  `docs/2026-11-15_coverage_expansion_protocol.md` (owner decision 2026-11-15; intake and the stop rule, lanes and
  merges, reviews, tax-year rules, the definition of done);
- releases and check tiers: `docs/2026-11-05_release_gating_design.md` and `tools/README.md`;
- tax year 2026: `docs/ty2026/ADOPTION.md` and `docs/2026-11-14_year_change_operations.md`;
- New York: `docs/ny/INTEGRATION.md` and `docs/ny/2026-11-14_ny_year_handling.md`.

**Standing decisions** are the bullets below, `handoffs/HANDOFF-HARDENING-1.md` (the hardening phase) and
`docs/provisional/DECISIONS.md` (the interview redraft, under the owner's delegation of 2026-11-14).

**Records are not guidance.** `docs/provisional/` (above all `lanes/`, one note per past agent lane, and every
`*_work/` folder), `docs/records/`, `handoffs/` other than HARDENING-1, the handoff archive and dated documents in `docs/` not named
above record what was done or proposed on a date. Cite them as evidence; check a claim in them against the tree
before relying on it; never follow them as instructions (`docs/provisional/README.md`).

- **Review families (owner, 2026-11-17).** `tools/transcription/families.json` lists the qualified models, any one of which is
  sufficient as a reviewer, and the advisory models, which may review only beside a qualified one (the owner's
  words). A family's `callable` flag says only whether the tools may call it. New review calls run on Claude
  (`claude-opus-5-5`; owner, 2026-11-21): Claude is callable and qualified; DeepSeek is qualified and not callable,
  and its current logs still satisfy the forms they cover; GPT is advisory and not callable. Reviews run under
  whichever qualified family can be called.
- **Inference cost (owner decision 2026-11-03).** Use inference only where it adds evidence.
  Paid review calls (transcription, render, class M, completeness, screen) and agents are
  weighed against what they can find; screen and completeness reviews have the best yield.
  - Review what changed: rerun a form's reviews when its content changes, and adjudicate only
    forms whose content changed. A review-prompt or tool change applies prospectively, at each
    form's next real change; there is no global re-review unless a measured defect calls for it.
  - Rule repeat disagreements mechanically where the carry-over tool allows (T-218), and scope
    reviews to changed lines and their readers (T-219). Enforced in `rerun_all.py`: carry runs after
    each review, and transcription and render are line-scoped unless the tool refuses or `--whole`.
  - Mechanical agent work (applying rulings, bug-entry formatting, input ripple, bookkeeping)
    runs on Sonnet; judgment (adjudication, source reading, design) on Opus.
    Fable (`claude-fable-5-2`) may run either class, and the launch hook allows it (owner decision
    2026-11-10). Use it for agents and for review calls (`--model claude-fable-5-2`) only when the
    owner says so for the session; the defaults above hold otherwise.
    Adjudication of review findings may run on Sonnet (owner, 2026-11-21, on cost), subject to a calibration
    against Opus rulings on the same packets; its briefs carry the line `Work: adjudication`, which the launch
    hook accepts on Sonnet, and every defect it claims is checked against the source before filing.
  - One review per form per round, run after all of that form's fixes in the round
    have landed; a round whose reviews find only lows starts no further round (the
    lows wait for the form's next substantive change). Enforced in `rerun_all.py` for transcription,
    render and class M: a log that already answers its subject is not rerun without
    `--force-rerun REASON`, and a run estimated above $3.00 needs `--approve-cost`
    (tools/README.md, "Review rerun guards"). Completeness, screen and false-no reviews are sampled per
    release (tools/README.md, "Sampled completeness, screen and false-no reviews"): `completeness_review.py`,
    `screen_review.py` and `false_no_review.py` refuse samples beyond the milestone without
    `--force-rerun REASON`, and runs above $3.00 without `--approve-cost`.
  - Every agent brief states the agent's model and its class (mechanical or
    judgment), and every `agent_runs.jsonl` row records both, as `model` and
    `class` fields, with the tax `year` and `jurisdiction` (`us` or `ny`) the work is for
    (`tools/check_agent_runs.py` requires all four on rows from 2026-11-10).
  - Every paid review call is logged in `.transcription/costs.jsonl` (`tools/transcription/costs.py`),
    with `year` and `jurisdiction`, and every agent run in `research/costs/agent_runs.jsonl`: the agent hook writes
    the row to the untracked `<git common dir>/agent-runs/pending.jsonl`, and `tools/agent_runs_fold.py`, which
    check-all runs first in the main worktree on `main`, moves finished rows into the ledger (tools/README.md, "Commit guard").
- **Worktrees (owner decision 2026-11-07).** Agents in worktrees clone review data with
  `tools/worktree_data.py clone` and their results are carried back with `carry-back`; never copy
  `.transcription/` by hand; missing files are added with `fill`, never copied by hand;
  a file changed on both sides is taken from the worktree only with `carry-back --prefer-worktree`, after
  checking which copy the committed logs were written from.
- **Commit guard and releases (owner decision 2026-11-22; `docs/2026-11-05_release_gating_design.md`, amendment).**
  Work is committed on `next` or a lane branch, never on `main`: `pre-commit` refuses a commit on `main`, and `main`
  moves only when `tools/release.sh` fast-forwards it to a commit of `next` whose exact tree passed a release-mode full
  run (`pre-push` refuses `main` at any other commit). A commit needs a green run of the light tier on its exact tree
  (`tools/check_all.sh`, light by default; the docs tier for bookkeeping-only changes): compile, build, the
  fixtures, the bookkeeping and generated-report checks, and the interview checks scoped to the forms the change
  touches. Mutation, the evaluator comparisons, the unscoped interview rules, properties, the web UI tests, refusal
  reach and the sampled-review release checks run only in the release's full run. Every run starts with
  `tools/preflight.sh`, which regenerates the derived files the steps compare; never run a full-tier check outside a
  release.
- **No ceremonial reruns (owner rule 2026-11-15; advisory, no tool enforces it).** Rerun a check only where the tree
  changed in what that check verifies. The commit guard still requires a green light-tier record of the exact tree;
  where a rerun would be purely ceremonial, the owner decides (on 2026-11-15, three commits with `--no-verify`). A
  release whose tree is already release-green reruns nothing (`tools/release.sh`).
- **Background waits (owner decision 2026-11-07; `pgrep -f` refused by tools/claude_hooks/bash_guard.py).** Never wait with `pgrep -f "<pattern>"` (it matches
  the waiting shell itself, so the wait never ends) or for a marker in the log of a run that may be
  killed. Wait on a pid or poll `tools/check_all_bg.sh --status`, always with a timeout, one wait per task.
- **Usage is no longer scarce (owner, 2026-11-22).** The owner is back on Ultra and asked for heavy parallel work with
  agent autonomy. The linear one-unit-at-a-time rule of 2026-11-16 has ended; the parallel-work bullet below governs
  again. The cost rules of the inference-cost bullet (review only what changed, rerun guards, `--approve-cost`) still
  hold: they are about evidence per dollar, not about the subscription.
- **DeepSeek through opencode (owner, 2026-11-16).** Claude sessions may run DeepSeek via opencode, with the
  owner's approval. It runs in the owner's main account (the owner suspended the AISP sandbox rule for these
  sessions). Reviews run under the qualified families of `tools/transcription/families.json`; see the review-family bullet.
- **Parallel work (owner decision 2026-11-10).** When work splits into independent pieces (separate forms, separate
  tools), run them as parallel agent lanes in worktrees rather than in sequence. Lanes claim their forms
  (`tools/claims.py`), and each lane's agent brief follows the cost rules above. Lanes branch from `next` and are
  merged into `next`. `tools/check_all_bg.sh` runs one at a time per clone; a lane verifies with the light tier of
  `tools/check_all.sh` in its own worktree, which only waits for one of the machine-wide slots
  (`CHECK_ALL_MAX_RUNS`, default 2). A lane's worktree is removed or archived
  (`tools/worktree_gc.py`) in the unit that integrates it, after `worktree_data.py carry-back`; one kept for later
  work is locked with `git worktree lock --reason "keep: <why>"` (owner, 2026-11-21). A release fails while any
  worktree is removable or stale.
