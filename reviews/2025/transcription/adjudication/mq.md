# Adjudication — mq

Method: `README.md` in this directory. Earlier rulings for mq are only in the log sidecars; this summary starts with the
backlog round.

## Backlog round

Subject after the p4-docs package, which links `amb.2025.mq_joint` from `mq.applies`. No expression changed. Fresh transcription
reviews of 2026-11-03 (Claude, deepseek-flash and gpt-6-astra). Before this round both prior logs agreed on mq.applies. The render
logs have no open section. Triage `../triage/mq[.deepseek|.gpt].json` (executable-triage-v2, 1,995 comparisons) finds no
difference for any family. Rulings are in `.transcription/proposed/bklg/transcription.mq[.deepseek|.gpt].json`.

Counts:
- transcription mq: representation 1
- transcription mq.deepseek: model error 1
- transcription mq.gpt: representation 1

| family | kind | lines | class |
| --- | --- | --- | --- |
| claude | transcription | mq.applies | representation |
| deepseek | transcription | mq.applies | model error |
| gpt | transcription | mq.applies | representation |

Findings: none. The deepseek ruling rests on a constructed rounding counterexample, not on the sample.
