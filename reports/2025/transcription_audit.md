# Transcription expression audit — 2026-10-25

T-062 / BUG-0129 remains open. This audit diagnoses saved model replies; it does not qualify reviews, migrate receipts or change numeric evidence.

| Family | Verified/recompared replies | Passing expression checks | Former AGREE rows now DISAGREE | Legacy-limited receipts |
| --- | ---: | ---: | ---: | ---: |
| claude | 27 | 6 | 92 | 23 |
| deepseek | 55 | 20 | 119 | 0 |

Of the 82 verified replies, 4 contain the complete current filer-input questions. A passing type check alone cannot repair truncated input meanings or incomplete provenance.

The other 28 Claude records could not be verified/recompared: 27 saved prompts differ from their recorded hashes, and se has conflicting ids after definition-namespace normalization. These remain gaps; no original request or response was silently corrected.

The adapter checks the project expression schema and the build’s existing reference/type rules. It replaces only the reviewed document, preserves published inputs, rejects added inputs and changed result types, and does not borrow missing computed helpers from that document. Candidate expressions are never executed. Passing these checks does not certify guard exhaustiveness, citations, source interpretation or tax correctness.

Four fresh, full-context source-only sample requests used Claude Opus 5.5 and deepseek-flash, once per model for dcprov and dependent. Both dcprov replies pass and agree on two results. Claude’s dependent reply passes expression checks but retains source/interface omissions. Flash’s dependent reply fails on bare Boolean ids used as tests and an invalid collection binding. Each dependent reply has 12 disputes; all are adjudicated with explicit limits, and both remain pending.

Original sample artifacts (18 files) are preserved with SHA-256 hashes under `.transcription/archive/before-expression-validation-2026-10-25/`. Fresh request policies and metadata retain the values actually used. The read-only audit JSON is `.transcription/expression-type-audit-current.json`; the earlier literal-only audit and intermediate expression audit remain separate historical snapshots. Audit exit 1 reports the 28 unresolved records.

Next: verify/replay usable original requests, replace incomplete/unverified requests, obtain valid replacements for rejected expressions, and adjudicate the remaining source differences. Both families must have current passing expression checks and verified complete input context before qualification; the global hold remains until migration/adjudication is complete. No further human packet is required.
