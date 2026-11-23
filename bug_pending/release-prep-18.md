## BUG-NEW-release-prep-18 — Closure: BUG-NEW-release-prep-08 is fixed

- **Closes:** BUG-NEW-release-prep-08
- **Closure:** fixed
- **Caught by:** release preparation 2 (release-prep-2, claude-opus-5-5, judgment), 2026-11-23.
- **Tool change:** The self-test runs release.sh in a temporary repository against a stub release_reviews.sh, as before; what failed was its expectation for a release-green tree, written before the 2026-11-22 amendment made release.sh check the sampled reviews again for such a tree (so the tag can list allowed open bugs). tools/hooks/test_pre_push.sh now expects, for a release-green tree: no second full run, one run of the reviews check, nothing promoted or tagged while the reviews are incomplete, and promotion once they are complete. The entry's premise that the test read the repository's real sampled reviews did not hold: the stub decides.
- **Evidence:** bash tools/hooks/test_pre_push.sh: 'release.sh refused a release-green tree' before the change; 'pre-push self-test: ok' after.
- **Tags:** tool, self-tests, release, fixed
