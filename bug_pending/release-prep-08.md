## BUG-NEW-release-prep-08 — The pre-push self-test runs release.sh against the tree's real sampled reviews

- **Date:** 2026-11-23
- **Caught by:** release preparation of next: full tier, pre_push_self_test ('release: the sampled reviews are not complete for a release ... pre-push self-test: release.sh refused a release-green tree').
- **Symptom:** tools/hooks/test_pre_push.sh (pre_push_self_test) expects release.sh to promote a planted release-green tree, but release.sh runs tools/release_reviews.sh on the repository's real sampled reviews even for a release-green tree (2026-11-22 amendment, item 4), so the self-test fails whenever any real sample is due or unruled, which is the state between releases.
- **Where:** tools/hooks/test_pre_push.sh; tools/release.sh (release_reviews.sh call on the release-green branch).
- **Proposed fix:** have the self-test stub tools/release_reviews.sh (or run release.sh with a test hook that replaces it), so it tests promotion and the pre-push hook only.
- **Severity:** low
- **Tags:** tool, self-tests, release; open
