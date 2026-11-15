## landing-01 (fixed before landing; never assigned an id) — Mortgage limit question does not count a second home

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): drafted as "differs" by an Opus reading agent of the landing lane, 2026-11-14, and confirmed by the landing agent against the question's prompt and help in interview/2025/questions.yaml.
- **Source:** i1040sca p. 8, Limits on home mortgage interest ("$500,000 if you are married filing separately"; $375,000 for debt after December 15, 2017).
- **Symptom:** the sa.mortgage_over_limit question says "the loans on your home", but the debt limit counts the main home and a second home together; a filer over the limit only with both homes counted can answer No. (Drafted first as missing the married-filing-separately limits; that case is refused earlier.) Pair consumer:sa.mortgage_over_limit@i1040sca:p8.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): help of sa.mortgage_over_limit now says to count a second home with the main home (the limit counts both); the married-filing-separately limits cannot arise, since s3.mfs refuses at scope.ready_credits. Pair ruled same.
- **Fix lines:** `sa.mortgage_over_limit`
