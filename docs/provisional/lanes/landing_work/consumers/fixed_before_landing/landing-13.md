## landing-13 (fixed before landing; never assigned an id) — Education credit recapture question asks only about the filer's own refund or aid

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 34, Line 16 (recapture of education credits).
- **Symptom:** scope.education_recapture asks whether you or your spouse were refunded or given aid; the rule is aid or a refund received for the student, often a dependent. Pair consumer:scope.education_recapture@i1040gi:p34.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.education_recapture asks about a refund or tax-free aid for any student the credit was claimed for. Pair ruled same.
- **Fix lines:** `scope.education_recapture`
