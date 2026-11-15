## landing-10 (fixed before landing; never assigned an id) — Schedule 1 line 8e: Archer and Medicare Advantage MSA distributions not asked

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 91, Line 8e (Form 8853 lines 8, 12 and 26).
- **Symptom:** s1.ltc_payout asks only about long-term care payments and accelerated death benefits; taxable Archer MSA and Medicare Advantage MSA distributions (Form 8853 lines 8 and 12) are not asked and not refused. Pair consumer:s1.ltc_payout@i1040gi:p91.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.archer_msa asks about money put into or taken out of an Archer or Medicare Advantage MSA, refusing at the Schedule 1 refusal. Pair ruled same.
- **Fix lines:** `scope.archer_msa`
