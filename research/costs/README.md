# Run cost records

- `agent_runs.jsonl`: one line per Claude Code subagent run (package and adjudication agents), appended by the
  parent session when the agent finishes, from the harness's completion notice: total subagent tokens, tool uses
  and wall time. Fields: `date`, `package`, `description`, `model`, `class` (`mechanical` or `judgment`), `year`
  (integer tax year the work is for), `jurisdiction` (`us` or `ny`), `subagent_tokens`, `tool_uses`,
  `duration_ms`, `cost_usd`, `source`. `tools/check_agent_runs.py` (a check-all step) requires `model`, `class`,
  `year` and `jurisdiction` on every row dated 2026-11-10 or later; earlier rows are exempt and carry no `year`
  or `jurisdiction`. The notice gives no dollar figure, so `cost_usd` is null; the runs are billed under the
  subscription plan. Rows carry no session link or session identifier (the repository is public).
- Paid review-model calls (transcription, render, class M, completeness, screen) are logged separately, one line
  per call, in `.transcription/costs.jsonl` by `tools/transcription/transcribe.py`'s `call_model`, each row with
  the run's `year` and `jurisdiction`; summarize with `python3 tools/transcription/costs.py` (by year and
  jurisdiction by default).
