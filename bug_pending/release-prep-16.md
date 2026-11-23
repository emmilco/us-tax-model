## BUG-NEW-release-prep-16 — The early-distribution exception question does not state whose education (08) or whose first home (09) counts

- **Date:** 2026-11-23
- **Caught by:** the sampled completeness review of retirement run after the BUG-1202 fix, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: claim retirement#1.2.
- **Source:** p590b p. 27: 'The education must be for you, your spouse, or the children or grandchildren of you or your spouse'; the first-home distribution must pay costs 'for the main home of a first-time homebuyer ... who is any of the following' (you, your spouse, your or your spouse's child, grandchild or ancestor), each meeting the no-ownership test.
- **Symptom:** retirement.exception lists conditions for 01, 02, 03, 04, 09, 11 and 19; for 08 it gives none, and for 09 it states the no-ownership test for 'you' and the spouse only. A filer who paid a niece's tuition can choose 08 (the additional tax is understated); one who paid for a child's first home may read 09 as not applying (overstated).
- **Where:** forms/2025/retirement.yaml retirement.exception (source).
- **Proposed fix:** Add to the list: '08, higher education costs for you, your spouse, or your or your spouse's children or grandchildren' and, in 09, 'a first home for you, your spouse, or your or your spouse's child, grandchild, parent or other ancestor, each of whom (and their spouse) had no home in the 2 years before'.
- **Proposed fix lines:** retirement.exception
- **Severity:** low
- **Tags:** retirement, Form 5329, wording, completeness review; open
