## landing-03 (fixed before landing; never assigned an id) — Form 8978 question omits the spouse

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 34, Line 16 (Form 8978).
- **Symptom:** scope.f8978 asks about "a partnership you were in"; a Form 8986 sent to the spouse is missed. Pair consumer:scope.f8978@i1040gi:p34.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.f8978 asks about the filer or spouse. Pair ruled same.
- **Fix lines:** `scope.f8978`
