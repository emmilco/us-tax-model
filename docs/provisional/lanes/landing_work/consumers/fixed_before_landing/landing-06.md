## landing-06 (fixed before landing; never assigned an id) — PFIC question defines a PFIC as a fund only

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi pp. 34 and 114 (Form 8621).
- **Symptom:** scope.pfic describes a passive foreign investment company as a foreign investment fund such as a mutual fund or ETF; foreign holding or cash-rich companies meeting the income or asset test are left out. Pairs consumer:scope.pfic@i1040gi:p34 and p114.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.pfic now asks about "a fund, or a company whose income or assets are mostly investments". Pair ruled same.
- **Fix lines:** `scope.pfic`
