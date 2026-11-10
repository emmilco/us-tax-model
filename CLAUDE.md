# Working guidance for this project

Current execution: read the top entry of `HANDOFF-NEXT-SESSION.md` first; it names the current handoff
(in `handoffs/`). `handoffs/HANDOFF-HARDENING-1.md` holds the owner's standing decisions and operational
facts. Older handoffs (all of `handoffs/` except HARDENING-1, including `HANDOFF.md`, `HANDOFF-INTEGRITY.md`
and `HANDOFF-STAGE-16.md`) are historical. `docs/2026-10-24_validation_policy.md` remains the controlling validation
amendment: human packets and ruling samples are optional; proceed without waiting for them and preserve
original verdicts. Reviews are Claude-only (`claude-opus-5-5`): the second review family (DeepSeek, GPT) is
inactive (owner, 2026-11-09; `docs/consolidation_charter.md`). Its machinery is kept dormant and no
second-family runs are made unless the owner reactivates a family. Existing second-family logs are historical. The consolidation charter governs the execution order and the
verification system.

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
    with `year` and `jurisdiction`, and every agent run in `research/costs/agent_runs.jsonl`.
- **Worktrees (owner decision 2026-11-07).** Agents in worktrees clone review data with
  `tools/worktree_data.py clone` and their results are carried back with `carry-back`; never copy
  `.transcription/` by hand; missing files are added with `fill`, never copied by hand;
  a file changed on both sides is taken from the worktree only with `carry-back --prefer-worktree`, after
  checking which copy the committed logs were written from.
- **Background waits (owner decision 2026-11-07; `pgrep -f` refused by tools/claude_hooks/bash_guard.py).** Never wait with `pgrep -f "<pattern>"` (it matches
  the waiting shell itself, so the wait never ends) or for a marker in the log of a run that may be
  killed. Wait on a pid or poll `tools/check_all_bg.sh --status`, always with a timeout, one wait per task.
