## BUG-NEW-release-prep-06 — A release-mode check-all passes its run settings to the self-tests, which then fail

- **Date:** 2026-11-23
- **Caught by:** release preparation of next: the full tier in release mode (AGENT_RUNS_FOLD=0 CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify, as tools/release.sh runs it) failed self_tests on build_cache_self_test, step_cache_self_test and check_bg_self_test; each passes when run without those settings.
- **Symptom:** tools/self_tests.py ran every test with the run's environment. ENGINE_CACHE=verify makes the build-cache and step-cache self-tests miss every reuse they test ('same inputs: not reused'), and AGENT_RUNS_FOLD=0 stops the fold test_check_bg.sh expects ('the fold did not run before the snapshot was taken'). Every release-mode full run, and so every release, would fail self_tests.
- **Where:** tools/self_tests.py run_one.
- **Tool change:** run_one passes the environment without ENGINE_CACHE, AGENT_RUNS_FOLD, CHECK_ALL_RELEASE and CHECK_ALL_ALLOW_OPEN_BUGS (RUN_SETTINGS); a self-test sets up the cases it tests and expects the tool defaults otherwise.
- **Evidence:** node engine/dist/main.js build-cache --self-test: ok without ENGINE_CACHE, fails with ENGINE_CACHE=verify; bash tools/hooks/test_check_bg.sh: ok without AGENT_RUNS_FOLD=0, fails with it.
- **Severity:** medium
- **Tags:** tool, self-tests, release, fixed
