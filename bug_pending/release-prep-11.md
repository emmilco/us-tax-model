## BUG-NEW-release-prep-11 — New York alimony under an agreement made after 2018 is not asked when other 2025 alimony is under an older agreement or a recapture

- **Date:** 2026-11-23
- **Caught by:** the sampled reviews of the release run, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: false-no and screen reviews of gate:s1.alimony_if_any (New York), findings 0, 1 and 3.
- **Source:** ny_it225i p. 10, A-119, and p. 18, S-136: applicable alimony is a payment under an instrument 'executed after December 31, 2018'; i1040gi p. 89 provides for alimony 'from more than one divorce or separation agreement'.
- **Symptom:** ny_it201.ask.alimony_later is asked only when s1.alimony_if_any is false. A filer (or, on a joint return, the other spouse) with any 2025 alimony under a pre-2019 agreement, or a recapture, makes the gate true, so post-2018 alimony under a second agreement gets no New York addition (A-119) or subtraction (S-136) and no refusal.
- **Where:** forms/ny/2025/ny_it201.yaml ny_it201.alimony_later_if_not_old; interview/ny/2025/questions.yaml ny_it201.ask.alimony_later.
- **Proposed fix:** Ask ny_it201.ask.alimony_later whenever alimony was paid or received since 2023 (the federal alimony_any answer), worded 'under an agreement made after 2018, or an older one changed to adopt the new rules', and refuse a Yes; fold BUG-1215 (1) into the same wording.
- **Proposed fix lines:** ny_it201.alimony_later_if_not_old, ny_it201.ask.alimony_later
- **Severity:** low
- **Tags:** ny, alimony, missed refusal, sampled false-no review; open
