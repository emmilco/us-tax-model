## landing-12 (fixed before landing; never assigned an id) — Medicaid waiver question asks only about care in the filer's home

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): the pair was drafted as "differs" by an Opus reading agent of the landing lane (claude-opus-5-5, judgment), 2026-11-14, and left unruled; not yet checked by a second reader.
- **Source:** i1040gi p. 24, Line 1d.
- **Symptom:** scope.medicaid_waiver asks about care of someone who lives in your home; taxable Medicaid waiver payments (line 1d) are generally those not excludable, which the question leaves out (the agent's reading of Notice 2014-7, not checked on the page). Pair consumer:scope.medicaid_waiver@i1040gi:p24.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): help of scope.medicaid_waiver points to scope.pay_no_w2 (same screen, same refusal), which catches taxable pay for care in another's home with no W-2; the question itself is not widened, since that would refuse W-2 caregivers who get a correct return. Pair ruled same.
- **Fix lines:** `scope.medicaid_waiver`
