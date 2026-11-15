## landing-11 (fixed before landing; never assigned an id) — Digital asset income question omits forks

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 92, Line 8v.
- **Symptom:** The prompt of s1.digital_income names pay, rewards, mining and staking but not forks, which line 8v lists. Pair consumer:s1.digital_income@i1040gi:p92.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): the s1.digital_income prompt, tick and help name forks. Pair ruled same.
- **Fix lines:** `s1.digital_income`
