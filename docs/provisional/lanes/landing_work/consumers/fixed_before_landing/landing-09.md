## landing-09 (fixed before landing; never assigned an id) — AMT question asks only whether AMT is owed, not whether Form 6251 must be filed

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i6251 p. 1, Who Must File (four statements).
- **Symptom:** The prompt of s2.amt_owed asks whether the filer owes AMT (statement 1); a filer required to file by statement 4 (negative adjustments) answers No and the required Form 6251 is not flagged. Pair consumer:s2.amt_owed@i6251:p1.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): the s2.amt_owed prompt also asks whether Form 6251 must be filed, as the form line's text does. Pair ruled same.
- **Fix lines:** `s2.amt_owed`
