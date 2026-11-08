# Working guidance for this project

Current execution: read the top entry of `HANDOFF-NEXT-SESSION.md` first; it names the current handoff
(in `handoffs/`). `handoffs/HANDOFF-HARDENING-1.md` holds the owner's standing decisions and operational
facts. Older handoffs (all of `handoffs/` except HARDENING-1, including `HANDOFF.md`, `HANDOFF-INTEGRITY.md`
and `HANDOFF-STAGE-16.md`) are historical. `docs/2026-10-24_validation_policy.md` remains the controlling validation
amendment: human packets and ruling samples are optional; proceed without waiting for them and preserve
original verdicts. The required review family is Claude (`claude-opus-5-5`); `deepseek-flash` and
`gpt-6-astra` are optional peer families (owner's model-authority ranking is in the validation policy:
`claude-fable-5-1` above all; `gpt-6-astra`, `claude-opus-5-5`, `gemini-4-argon`, `deepseek-v4.1-flash`
and `gpt-6.1-sol` interchangeable; Gemini 3, GPT-6 Luna/Terra, Claude Sonnet/Haiku mechanical or
advisory only).

- **Inference cost (owner decision 2026-11-03).** Use inference only where it adds evidence.
  Paid review calls (transcription, render, class M, completeness, screen) and agents are
  weighed against what they can find; screen and completeness reviews have the best yield.
  - Review what changed: rerun a form's reviews when its content changes, and adjudicate only
    forms whose content changed. A review-prompt or tool change applies prospectively, at each
    form's next real change; there is no global re-review unless a measured defect calls for it.
  - Rule repeat disagreements mechanically where the carry-over tool allows (T-218), and scope
    reviews to changed lines and their readers once that exists (T-219).
  - DeepSeek transcription runs only on forms where its log is eligible for second-family credit
    (`compare_families.py`) or for a change the owner flags; DeepSeek render and class M run as before
    (owner decision 2026-11-04).
  - Mechanical agent work (applying rulings, bug-entry formatting, input ripple, bookkeeping)
    runs on Sonnet; judgment (adjudication, source reading, design) on Opus.
  - One review per form per round, run after all of that form's fixes in the round
    have landed; a round whose reviews find only lows starts no further round (the
    lows wait for the form's next substantive change).
  - Every agent brief states the agent's model and its class (mechanical or
    judgment), and every `agent_runs.jsonl` row records both, as `model` and
    `class` fields.
  - Every paid review call is logged in `.transcription/costs.jsonl` (`tools/transcription/costs.py`)
    and every agent run in `research/costs/agent_runs.jsonl`.
- **Worktrees (owner decision 2026-11-07).** Agents in worktrees clone review data with
  `tools/worktree_data.py clone` and their results are carried back with `carry-back`; never copy
  `.transcription/` by hand.
- **Background waits (owner decision 2026-11-07).** Never wait with `pgrep -f "<pattern>"` (it matches
  the waiting shell itself, so the wait never ends) or for a marker in the log of a run that may be
  killed. Wait on a pid or poll `tools/check_all_bg.sh --status`, always with a timeout, one wait per task.
