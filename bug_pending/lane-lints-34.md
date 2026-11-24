## BUG-NEW-lane-lints-34 — retirement.exception: exception 09 does not state the 120-day deadline or that the money must pay qualified acquisition costs

- **Date:** 2026-11-24
- **Caught by:** the question review of 2026-11-24 (claude-opus-5-5), sample #1 on the reworded question, ruled in lane lints (claude-opus-5-5, judgment)
- **Source:** p590b (2025) p. 27, First home, "It must be used to pay qualified acquisition costs (defined next) before the close of the 120th day after the day you received it."
- **Symptom:** A filer whose first-home distribution was not spent on buying, building or rebuilding costs within 120 days can still choose 09, understating the additional tax.
- **Where:** forms/2025/retirement.yaml retirement.exception (source).
- **Proposed fix:** Add to 09: "used within 120 days to pay the costs of buying, building or rebuilding the home, including closing costs".
- **Proposed fix lines:** retirement.exception
- **Severity:** low
- **Tags:** retirement, Form 5329, wording, question review; open
