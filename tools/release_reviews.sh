#!/usr/bin/env bash
# The release gate of the sampled reviews (tools/transcription/samples.py): on a fresh build of the working tree,
# no form may be due, short of the milestone's samples, or hold an unruled finding. Called by tools/release.sh and
# tools/release_prep.sh.
# It leaves the working tree's tracked files as they are (the --release checks write no report).
# Every check runs, each under its own "== <check> (<seconds> s)" line, so one run lists every due item; the
# script then fails naming the checks that failed (exit 1). A failed compile, build or render stops it before the
# checks (exit 2).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
t0=$(date +%s)
if ! { npm run -s compile >/dev/null && node engine/dist/main.js build >/dev/null &&
       node engine/dist/main.js render >/dev/null && node engine/dist/main.js render --ny >/dev/null; }; then
  echo "release reviews: the compile, build or render failed; no review checked" >&2
  exit 2
fi
echo "== build ($(( $(date +%s) - t0 )) s)"
failed=()
for check in "check_completeness.py --release" "check_completeness.py --release --jurisdiction ny" \
             "check_screens.py --release" "check_screens.py --release --jurisdiction ny" \
             "check_false_no.py --release" "check_false_no.py --release --jurisdiction ny"; do
  t0=$(date +%s)
  rc=0
  # shellcheck disable=SC2086
  python3 tools/transcription/$check || rc=$?
  echo "== $check ($(( $(date +%s) - t0 )) s)$([ "$rc" = 0 ] || echo ": FAILED (exit $rc)")"
  [ "$rc" = 0 ] || failed+=("$check")
done
if [ "${#failed[@]}" -gt 0 ]; then
  printf 'release reviews: not complete; failed:\n' >&2
  printf '  %s\n' "${failed[@]}" >&2
  exit 1
fi
echo "release reviews: complete"
