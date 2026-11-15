## landing-07 (fixed before landing; never assigned an id) — Adoption parent question misses employer-paid benefits with no qualifying expense of the filer

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 24, Line 1f.
- **Symptom:** s3.adoption_any can truthfully be No when an employer paid adoption costs directly and the filer paid nothing; the box 12 code T question beneath it is then never asked, and w2.box12_any does not list code T. Pair consumer:s3.adoption_any@i1040gi:p24.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): s3.adoption_any now asks whether the filer paid (or had an employer pay) adoption costs, so code T reaches scope.adoption_benefits, which refuses. Pair ruled same.
- **Fix lines:** `s3.adoption_any`
