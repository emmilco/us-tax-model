#!/usr/bin/env bash
# The checks a candidate tree runs before its release-mode full check (tools/release.sh): the ones that fail in
# minutes, where the full check fails only when the wave holding the defect ends.
#
#   tools/release_prep.sh [--fail-fast] [--allow-open-bugs]
#
# 1. tools/release_reviews.sh (given --allow-open-bugs when this run is): it compiles, builds and renders the working tree, then runs every release check of
#    the sampled reviews, each separately, so one run lists every due item. A failed compile, build or render
#    stops the run here, since the steps below read the build.
# 2. The check-all steps named in PREP_STEPS, one after another, cheapest first, each with the command that
#    `tools/check_all_steps.sh --print-steps --tier full` declares for it (the default year): no command is
#    written here, so the two cannot drift. A name the steps script does not declare stops the run (exit 2).
#    A New York step the year skips is listed as SKIP. As in check-all, a step that exits 0 without a line
#    tools/step_output.py requires of it fails.
# 3. tools/worktree_gc.py check --fail (step `worktrees`): a removable or stale linked worktree fails the release, as
#    in tools/release.sh; remove it, archive it, or lock it with a reason starting "keep".
#
# Every step runs, unless --fail-fast stops at the first failure. Each step's output goes to
# <git dir>/release-prep/<step>.log (rewritten by each run); a failing step's log is printed. The run ends with one
# line per step (PASS, FAIL or SKIP, and its seconds) and one summary line, "release-prep: PASS" (exit 0) or
# "release-prep: FAIL: <steps>" (exit 1).
#
# It regenerates no report of its own. The steps write only what they write in check-all (coverage rewrites
# reports/<year>/coverage.md); reports that only later waves or a release rewrite (interview_length.md, evidence,
# mutation, the engine differential) are left as they are, so doc_figures checks the figures against the
# committed reports. A pass therefore says the fast-failing steps pass, not that the full check will.
# Like check-all, it waits for one of the machine's CHECK_ALL_MAX_RUNS slots (tools/check_slot.py).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# Cheapest first, from the recorded check-all times; the release reviews run before all of them.
PREP_STEPS="check_bug_inventory bug_status check_agent_runs doc_figures limits ny_limits consumers ny_consumers
  renamed_ids ny_renamed_ids year_changes ny_year_changes citations ny_citations check_extraction ny_check_extraction
  check_logs ny_check_logs bookkeeping_self_tests ny_test_fixtures test_fixtures coverage interview_rules self_tests"

fail_fast=0
allow=()
orig=("$@")
while [ "$#" -gt 0 ]; do
  case "$1" in
    --fail-fast) fail_fast=1; shift ;;
    --allow-open-bugs) allow=(--allow-open-bugs); shift ;;
    *) echo "release-prep: unknown argument '$1' (usage: tools/release_prep.sh [--fail-fast] [--allow-open-bugs])" >&2; exit 2 ;;
  esac
done
if [ -z "${CHECK_ALL_SLOT:-}" ]; then
  exec python3 tools/check_slot.py --tier release-prep -- "$0" ${orig[@]+"${orig[@]}"}
fi

listing="$(tools/check_all_steps.sh --print-steps --tier full)" || {
  echo "release-prep: tools/check_all_steps.sh --print-steps failed; nothing run" >&2; exit 2; }
known=(); cmds=()
while IFS=$'\t' read -r name cmd reason; do
  [ -n "$name" ] || continue
  known+=("$name")
  if [ "$cmd" = skip ]; then cmds+=("skip:$reason"); else cmds+=("$cmd"); fi
done <<< "$listing"
command_of() {  # command_of NAME: the declared command (or "skip:<reason>"); status 1 if NAME is not declared
  local i
  for i in "${!known[@]}"; do
    if [ "${known[$i]}" = "$1" ]; then printf '%s' "${cmds[$i]}"; return 0; fi
  done
  return 1
}
missing=()
for name in $PREP_STEPS; do
  command_of "$name" > /dev/null || missing+=("$name")
done
if [ "${#missing[@]}" -gt 0 ]; then
  echo "release-prep: tools/check_all_steps.sh declares no step ${missing[*]} (full tier); PREP_STEPS is out of date" >&2
  exit 2
fi

logs="$(git rev-parse --git-path release-prep)"
rm -rf "$logs"
mkdir -p "$logs"
results=()
failed=()
record() {  # record NAME STATUS SECONDS
  results+=("$(printf '%-5s %5s s  %s' "$2" "$3" "$1")")
  if [ "$2" = FAIL ]; then
    failed+=("$1")
    echo "== $1: FAILED ($3 s); its output ($logs/$1.log):"
    cat "$logs/$1.log"
  else
    echo "== $1: $2 ($3 s)"
  fi
}
finish() {
  echo
  echo "release-prep: steps"
  printf '  %s\n' "${results[@]}"
  if [ "${#failed[@]}" -gt 0 ]; then
    echo "release-prep: FAIL: ${failed[*]}"
    exit 1
  fi
  echo "release-prep: PASS"
  exit 0
}

t0=$(date +%s)
rc=0
tools/release_reviews.sh ${allow[@]+"${allow[@]}"} > "$logs/release_reviews.log" 2>&1 || rc=$?
if [ "$rc" = 0 ]; then
  record release_reviews PASS $(( $(date +%s) - t0 ))
else
  record release_reviews FAIL $(( $(date +%s) - t0 ))
  if [ "$rc" = 2 ] || [ "$fail_fast" = 1 ]; then
    [ "$rc" != 2 ] || echo "release-prep: no build to check; the other steps were not run"
    finish
  fi
fi

t0=$(date +%s)
if python3 tools/worktree_gc.py check --fail > "$logs/worktrees.log" 2>&1; then
  record worktrees PASS $(( $(date +%s) - t0 ))
else
  record worktrees FAIL $(( $(date +%s) - t0 ))
  [ "$fail_fast" = 0 ] || finish
fi

for name in $PREP_STEPS; do
  cmd="$(command_of "$name")"
  if [[ "$cmd" == skip:* ]]; then
    echo "${cmd#skip:}" > "$logs/$name.log"
    record "$name" SKIP 0
    continue
  fi
  t0=$(date +%s)
  rc=0
  ( eval "$cmd" ) > "$logs/$name.log" 2>&1 < /dev/null || rc=$?
  secs=$(( $(date +%s) - t0 ))
  if [ "$rc" = 0 ]; then
    if ! lacking="$(python3 tools/step_output.py --logs "$logs" "$name")"; then
      echo "release-prep: tools/step_output.py did not run; the step's required lines are unchecked" >> "$logs/$name.log"
      rc=1
    elif [ -n "$lacking" ]; then
      rc=1
    fi
  fi
  if [ "$rc" = 0 ]; then record "$name" PASS "$secs"; else record "$name" FAIL "$secs"; fi
  if [ "$rc" != 0 ] && [ "$fail_fast" = 1 ]; then
    finish
  fi
done
finish
