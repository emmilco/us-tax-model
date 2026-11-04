# Run cost records

- `agent_runs.jsonl`: one line per Claude Code subagent run (package and adjudication agents), appended by the
  parent session when the agent finishes, from the harness's completion notice: total subagent tokens, tool uses
  and wall time. The notice gives no dollar figure, so `cost_usd` is null; the runs are billed under the
  subscription plan.
- Paid review-model calls (transcription, render, class M, completeness, screen) are logged separately, one line
  per call, in `.transcription/costs.jsonl` by `tools/transcription/transcribe.py`'s `call_model`; summarize with
  `python3 tools/transcription/costs.py`.
