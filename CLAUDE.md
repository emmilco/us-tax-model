# Working guidance for this project

Current execution: read the top entry of `HANDOFF-NEXT-SESSION.md` first; it names the current handoff
(in `handoffs/`). `handoffs/HANDOFF-HARDENING-1.md` holds the owner's standing decisions and operational
facts. Older handoffs (`HANDOFF.md`, `HANDOFF-INTEGRITY.md`, `HANDOFF-STAGE-16.md` and the stage handoffs
in `handoffs/`) are historical. `docs/2026-10-24_validation_policy.md` remains the controlling validation
amendment: human packets and ruling samples are optional; proceed without waiting for them and preserve
original verdicts. Source reviews run under both families, Claude (`claude-opus-5-5`) and deepseek-flash.

- **Inference cost.** Paid model calls (the `claude -p` transcription, render and class M
  reviews in `tools/transcription/`, and any like them) are part of the work. Do not weigh
  their cost, ask before running them, or hold work back to save it, unless the owner says
  otherwise.
