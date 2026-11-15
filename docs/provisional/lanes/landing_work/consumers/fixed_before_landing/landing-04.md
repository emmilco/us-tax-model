## landing-04 (fixed before landing; never assigned an id) — Reservist distribution repayment question omits the spouse

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 95, Line 20.
- **Symptom:** scope.reservist_repaid asks "did you put back" while its parent includes the spouse. Pair consumer:scope.reservist_repaid@i1040gi:p95.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.reservist_repaid asks about the filer or spouse. Pair ruled same.
- **Fix lines:** `scope.reservist_repaid`
