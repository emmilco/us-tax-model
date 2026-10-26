#!/usr/bin/env bash
# The steps of check-all for one tax year: pass --year N to check a year other
# than the default (the newest adopted year in years.json); every step receives
# the same arguments. tools/check_all.sh runs this and guards it.
#
# Compile first: review tools and every build consumer import engine/dist.
# Other steps run in three waves; the steps of a wave run side by side, each writing
# its output to its own log, printed in the order below when the wave ends. No
# two steps of a wave write the same file, and none reads what another of its
# wave writes: wave 1 checks the sources and logs while it builds and renders,
# wave 2 runs the checks that read the build, wave 3 writes the evidence report and review packets. A
# failing step fails the run after its wave. Each step's wall time, in seconds,
# goes to .git/check-all-times (not tracked).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
node=(node engine/dist/main.js)
times="$(git rev-parse --git-path check-all-times)"
: > "$times"
logs="$(mktemp -d)"
trap 'rm -rf "$logs"' EXIT
names=()
pids=()

# step NAME COMMAND...: start COMMAND in the background, logging to its own file.
step() {
  local name="$1"; shift
  ( t0=$(date +%s); rc=0; "$@" > "$logs/$name.log" 2>&1 || rc=$?
    echo "$(( $(date +%s) - t0 )) $name" >> "$times"; exit "$rc" ) &
  names+=("$name"); pids+=("$!")
}

# wave: wait for the steps started since the last wave, print their logs in order,
# and stop the run if any failed.
wave() {
  local i failed=()
  for i in "${!pids[@]}"; do
    wait "${pids[$i]}" || failed+=("${names[$i]}")
  done
  for i in "${!names[@]}"; do
    echo "== ${names[$i]}"
    cat "$logs/${names[$i]}.log"
  done
  names=(); pids=()
  if [ "${#failed[@]}" -gt 0 ]; then
    echo "check-all: failed: ${failed[*]}" >&2
    exit 1
  fi
}

# Chained with && because set -e does not apply inside a command whose status is tested.
build_and_render() {
  "${node[@]}" build "$@" && "${node[@]}" render "$@"
}

lean_compare() {
  (cd lean && lake build taxeval >/dev/null 2>&1) && "${node[@]}" compare "$@"
}

step compile npm run compile --silent
wave

step fetch_sources python3 tools/fetch_sources.py "$@"
step check_extraction python3 tools/check_extraction.py "$@"
step check_macrs_tables python3 tools/check_macrs_tables.py "$@"
step check_auto_limits python3 tools/check_auto_limits.py "$@"
step check_bug_inventory python3 tools/check_bug_inventory.py
step review_tools python3 tools/transcription/test_review_tools.py
step adapter_contracts python3 tools/transcription/adapter_contracts.py "$@"
step classm_skipped python3 tools/transcription/audit_skipped.py
step compare_families python3 tools/transcription/compare_families.py "$@"
step check_logs python3 tools/transcription/check_logs.py "$@"
step check_table_logs python3 tools/transcription/check_table_logs.py "$@"
# citations runs without --strict: the computed-line locators it lists under
# "Locators to rewrite" are reported, not failed, until that list is empty;
# then --strict is added here.
step citations python3 tools/citations.py "$@"
step citations_self_test python3 tools/citations.py --self-test "$@"
step year_diff_self_test python3 tools/year_diff.py --self-test "$@"
step build build_and_render "$@"
wave

step conjecture "${node[@]}" conjecture "$@"
step test_fixtures "${node[@]}" test-fixtures "$@"
step test_integration "${node[@]}" test-integration "$@"
step human_review python3 tools/human_review/test_review.py
step classm_job_seeds "${node[0]}" tools/transcription/test_classm_jobs.mjs
step coverage "${node[@]}" coverage "$@"
step properties "${node[@]}" properties "$@"
step differential "${node[@]}" differential "$@"
step engine_differential tools/engines/run.sh "$@"
step mutate "${node[@]}" mutate "$@"
step compare lean_compare "$@"
wave

step evidence "${node[@]}" evidence "$@"
step review_stage2 "${node[@]}" review-stage2 "$@"
step review_stage3 "${node[@]}" review-stage3 "$@"
step review_stage4 "${node[@]}" review-stage4 "$@"
step review_stage5 "${node[@]}" review-stage5 "$@"
wave
