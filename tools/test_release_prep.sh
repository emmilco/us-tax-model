#!/usr/bin/env bash
# Self-test of tools/release_prep.sh: the real release_prep.sh, release_reviews.sh, check_all_steps.sh, step_output.py,
# taxyear.py and jurisdiction.py run in a temporary repository in which every other tool, node and npm are stubs
# that log their arguments and fail when the FAIL variable (|-separated) names part of their call. Checked: the
# release reviews and the listed steps run with the commands check_all_steps.sh declares, and no other step; every
# step runs after a failure, unless --fail-fast; a failed build stops the run; a step that exits 0 without a line
# step_output.py requires fails; a listed step the steps script does not declare stops the run; a New York step the
# year skips is listed as skipped; and check-all's times file is not written. Then tools/preflight.sh, in the same
# repository: it regenerates each derived file before it runs a check, and stops at the first failure.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
repo="$tmp/repo"
mkdir -p "$repo/tools" "$repo/forms/2025" "$repo/forms/ny/2025" "$tmp/bin"
real="tools/release_prep.sh tools/release_reviews.sh tools/check_all_steps.sh tools/step_output.py tools/taxyear.py tools/jurisdiction.py tools/preflight.sh"
for path in $real; do cp "$here/$path" "$repo/tools/"; done
export CALLS="$tmp/calls" STUB="$tmp/stub.sh"
# The one stub: logs "<name> <args>", prints the tier-path line bookkeeping_self_tests must have (unless
# NO_TIER_LINE is set), and fails when a part of FAIL is in the logged call.
cat > "$STUB" <<'EOF'
line="$*"
echo "$line" >> "$CALLS"
if [ "$1" = tools/self_tests.py ] && [[ "$line" == *bookkeeping* ]] && [ -z "${NO_TIER_LINE:-}" ]; then
  echo "tier paths self-test: ok (stub)"
fi
IFS='|'
for part in ${FAIL:-}; do
  if [ -n "$part" ] && [[ "$line" == *"$part"* ]]; then exit 1; fi
done
exit 0
EOF
for path in $(grep -ohE 'tools/[A-Za-z0-9_/.-]+\.(py|mjs|sh)' "$here/tools/check_all_steps.sh" "$here/tools/release_reviews.sh" \
              "$here/tools/release_prep.sh" "$here/tools/preflight.sh" | sort -u); do
  case " $real " in *" $path "*) continue ;; esac
  mkdir -p "$repo/$(dirname "$path")"
  case "$path" in
    *.py) printf 'import os, subprocess, sys\nsys.exit(subprocess.call(["bash", os.environ["STUB"], "%s"] + sys.argv[1:]))\n' \
            "$path" > "$repo/$path" ;;
    *) printf '#!/usr/bin/env bash\nexec bash "$STUB" %s "$@"\n' "$path" > "$repo/$path"; chmod +x "$repo/$path" ;;
  esac
done
for cmd in node npm; do
  printf '#!/usr/bin/env bash\nexec bash "$STUB" %s "$@"\n' "$cmd" > "$tmp/bin/$cmd"; chmod +x "$tmp/bin/$cmd"
done
git -C "$repo" init -q
times="$repo/.git/check-all-times"

failures=0
fail() { echo "release-prep self-test: $1" >&2; failures=$((failures + 1)); }
status=0
run() {  # run NY_ADOPTED ARGS...: release_prep.sh with years.json's ny_adopted set; output in $tmp/out, exit in $status
  printf '{"adopted": [2025], "ny_adopted": %s}\n' "$1" > "$repo/years.json"; shift
  : > "$CALLS"
  echo "sentinel" > "$times"
  status=0
  (cd "$repo" && PATH="$tmp/bin:$PATH" CHECK_ALL_SLOT=test bash tools/release_prep.sh "$@") > "$tmp/out" 2>&1 || status=$?
  [ "$(cat "$times")" = sentinel ] || fail "check-all's times file was written"
}
has() { grep -qF -- "$2" "$1" || fail "expected in $(basename "$1"): $2"; }
lacks() { if grep -qF -- "$2" "$1"; then fail "not expected in $(basename "$1"): $2"; fi; }
exits() { [ "$status" = "$1" ] || { fail "exit $status, expected $1; output:"; sed 's/^/  /' "$tmp/out" >&2; }; }

# All pass: the release reviews, then each listed step with its declared command, and nothing else.
run "[2025]"
exits 0
has "$tmp/out" "release-prep: PASS"
for call in "npm run -s compile" "node engine/dist/main.js render --ny" \
    "tools/transcription/check_completeness.py --release --jurisdiction ny" "tools/transcription/check_false_no.py --release" \
    "tools/check_bug_inventory.py" "tools/bug_status.py --check" "tools/check_agent_runs.py" "tools/doc_figures.py --check" \
    "tools/rename_ids.py check --jurisdiction ny" \
    "tools/check_limits.py --jurisdiction ny" "tools/check_consumers.py" "tools/year_changes.py --check --jurisdiction ny" \
    "tools/citations.py --strict --jurisdiction ny" "tools/check_extraction.py" "tools/transcription/check_logs.py --jurisdiction ny" \
    "tools/self_tests.py --group bookkeeping --times /dev/null" "tools/self_tests.py --group code --times /dev/null" \
    "node engine/dist/main.js test-fixtures --ny" "node engine/dist/main.js coverage" "node engine/dist/main.js interview-rules"; do
  has "$CALLS" "$call"
done
for call in "mutate" "interview-length" "evidence" "review-stage" "tools/engines/run.sh" "test-integration" "compare" \
    "properties" "tools/check_twins.py" "interview-coverage" "tools/check_slot.py"; do
  lacks "$CALLS" "$call"
done
has "$tmp/out" "== release_reviews: PASS ("
has "$tmp/out" "== test_fixtures: PASS ("
[ "$(grep -c '^  PASS ' "$tmp/out" || true)" = 26 ] || fail "expected 26 steps listed as PASS (the reviews, the worktree gate and 24 steps)"
first="$(grep -n 'tools/check_bug_inventory.py' "$CALLS" | head -1 | cut -d: -f1)"
last_review="$(grep -n 'check_false_no.py --release --jurisdiction ny' "$CALLS" | head -1 | cut -d: -f1)"
[ "${first:-0}" -gt "${last_review:-0}" ] || fail "the steps ran before the release reviews ended"

# Failures are collected: every review check and every step still runs; the summary names each failure.
FAIL="check_screens.py --release --jurisdiction ny|tools/check_limits.py --jurisdiction ny" run "[2025]"
exits 1
has "$tmp/out" "release-prep: FAIL: release_reviews ny_limits"
has "$CALLS" "tools/transcription/check_false_no.py --release --jurisdiction ny"
has "$CALLS" "tools/self_tests.py --group code"
has "$tmp/out" "release reviews: not complete; failed:"
has "$tmp/out" "  check_screens.py --release --jurisdiction ny"

# --fail-fast stops at the first failure.
FAIL="tools/check_limits.py --jurisdiction ny" run "[2025]" --fail-fast
exits 1
has "$tmp/out" "release-prep: FAIL: ny_limits"
lacks "$CALLS" "tools/check_consumers.py"

# A failed build stops the run before any review check or step.
FAIL="npm run -s compile" run "[2025]"
exits 1
has "$tmp/out" "no build to check"
lacks "$CALLS" "check_completeness.py"
lacks "$CALLS" "tools/check_bug_inventory.py"

# A step that passes without its required line (tools/step_output.py) fails.
NO_TIER_LINE=1 run "[2025]"
exits 1
has "$tmp/out" "release-prep: FAIL: bookkeeping_self_tests"
has "$tmp/out" "exited 0 without a line its output must have"

# New York not adopted: its steps are listed as skipped, not run.
run "[]"
exits 0
has "$tmp/out" "SKIP      0 s  ny_test_fixtures"
lacks "$CALLS" "node engine/dist/main.js test-fixtures --ny"

# A listed step the steps script does not declare stops the run before anything runs.
cp "$repo/tools/check_all_steps.sh" "$tmp/steps.orig"
grep -v '^jstep limits ' "$tmp/steps.orig" > "$repo/tools/check_all_steps.sh"
run "[2025]"
exits 2
has "$tmp/out" "declares no step limits ny_limits"
[ ! -s "$CALLS" ] || fail "something ran although the step list was refused"
cp "$tmp/steps.orig" "$repo/tools/check_all_steps.sh"

# The preflight: the build when stale, each regeneration, then the checks, in that order; the first failure stops it.
printf '{"adopted": [2025], "ny_adopted": [2025]}\n' > "$repo/years.json"
: > "$CALLS"
pstatus=0
(cd "$repo" && PATH="$tmp/bin:$PATH" FAIL="tools/build_fresh.py" bash tools/preflight.sh --tier full) > "$tmp/out" 2>&1 || pstatus=$?
[ "$pstatus" = 0 ] || { fail "preflight failed (exit $pstatus):"; sed 's/^/  /' "$tmp/out" >&2; }
has "$tmp/out" "preflight: ok"
for call in "npm run -s compile" "node engine/dist/main.js build" "tools/bug_status.py --write" "tools/coverage/tree.py" \
    "tools/coverage/gate_frequencies.py" "node engine/dist/main.js spouse-wording --report" \
    "node engine/dist/main.js interview-coverage --write" "tools/check_bug_inventory.py" "tools/doc_figures.py --check"; do
  has "$CALLS" "$call"
done
write_at="$(grep -n '^tools/doc_figures.py$' "$CALLS" | head -1 | cut -d: -f1)"
check_at="$(grep -n 'tools/check_bug_inventory.py' "$CALLS" | head -1 | cut -d: -f1)"
regen_at="$(grep -n 'tools/bug_status.py --write' "$CALLS" | head -1 | cut -d: -f1)"
[ -n "$write_at" ] && [ "${regen_at:-99}" -lt "$write_at" ] && [ "$write_at" -lt "${check_at:-0}" ] \
  || fail "the preflight did not regenerate (bug status, then the figures) before its checks"
# A fresh build is not rebuilt; a failing regeneration stops the preflight before any check.
: > "$CALLS"
pstatus=0
(cd "$repo" && PATH="$tmp/bin:$PATH" FAIL="tools/coverage/tree.py" bash tools/preflight.sh) > "$tmp/out" 2>&1 || pstatus=$?
[ "$pstatus" = 1 ] || fail "a failing regeneration did not fail the preflight (exit $pstatus)"
has "$tmp/out" "preflight: FAILED at regenerate the coverage tree"
lacks "$CALLS" "node engine/dist/main.js build"
lacks "$CALLS" "tools/check_bug_inventory.py"
lacks "$CALLS" "spouse-wording"

if [ "$failures" -gt 0 ]; then
  echo "release-prep self-test FAILED: $failures problem(s)" >&2
  exit 1
fi
echo "release-prep self-test OK: commands from the steps script, failures collected, --fail-fast, build stop, required lines, New York skip, drift; preflight order and fail-fast"
