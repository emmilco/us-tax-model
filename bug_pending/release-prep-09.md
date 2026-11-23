## BUG-NEW-release-prep-09 — A related-party like-kind exchange of 2023 or 2024 followed by a 2025 disposition is neither asked nor refused

- **Date:** 2026-11-23
- **Caught by:** the sampled reviews of the release run, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: false-no review of gate:sd.sold_other, finding 7.
- **Source:** i8824 p. 1, 'Also file Form 8824 for the 2 years following the year of a related party exchange'; Line 7, a disposition by either party within 2 years makes the deferred gain reportable 'on your tax return for the year of disposition'.
- **Symptom:** sd.sold_other asks only about real estate or business property sold or traded in 2025 (and later payments on an earlier sale). A filer who made a like-kind exchange with a related party in 2023 or 2024, where either party disposed of the property in 2025, answers No; the deferred gain is neither computed nor refused and Form 8824 is not filed.
- **Where:** forms/2025/sd.yaml sd.sold_other (and sd.like_kind_if_sold); interview/2025/questions.yaml sd.sold_other help.
- **Proposed fix:** Name the case in the sd.sold_other help ('or you traded property with a relative or a related company in 2023 or 2024'), so a Yes reaches sd.like_kind and its refusal; or ask it as its own refusing question under the rare-sales group.
- **Proposed fix lines:** sd.sold_other, sd.like_kind
- **Severity:** low
- **Tags:** sd, Form 8824, missed refusal, sampled false-no review; open
