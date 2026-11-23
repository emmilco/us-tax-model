## BUG-NEW-release-prep-12 — The main home sale screen states the joint exclusion without the both-spouses use test or the two-year rule, and does not name a spouse's home

- **Date:** 2026-11-23
- **Caught by:** the sampled reviews of the release run, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: screen review of sd.home_sale, findings 0 to 2.
- **Source:** i1040sd p. 2: 'If both you and your spouse meet these tests and you file a joint return, you can exclude up to $500,000'; Test 2, 'You haven't excluded gain on the sale or exchange of another main home during the 2-year period'.
- **Symptom:** sd.home_sale's help says 'Gain of up to $250,000 ($500,000 on a joint return) is usually excluded if you owned the home and lived in it for 2 of the 5 years'. A joint filer with only one spouse meeting the use test and a gain between the two limits, or a filer who excluded gain on another home within 2 years, can answer No without a Form 1099-S; the prompt 'Was any of it your main home' does not name a spouse's own home. The reportable gain is then neither computed nor refused.
- **Where:** interview/2025/questions.yaml sd.home_sale (prompt and help); forms/2025/sd.yaml sd.home_sale.
- **Proposed fix:** Prompt: 'Was any of it your (or, on a joint return, your spouse's) main home, ...'; help: '$500,000 on a joint return only if both of you lived in it for 2 of the 5 years; no exclusion if either of you excluded gain on another home sold in the 2 years before.'
- **Proposed fix lines:** sd.home_sale
- **Severity:** low
- **Tags:** sd, interview, wording, sampled screen review; open
