#!/usr/bin/env bash
# Runs the preflight (tools/preflight.sh: regenerates the derived files the steps compare, then the fast bookkeeping
# checks; a failure stops the run before it starts; CHECK_ALL_PREFLIGHT=done skips it), then the suite
# (tools/check_all_steps.sh, passing on its arguments, e.g. --tier full or --year N) and, when it passes, writes the
# tested tree's hash to the tier's marker and list of green trees (tools/green.sh) for
# tools/hooks/pre-commit and pre-push. The tier is light unless --tier says otherwise.
# It refuses to start while a variable that changes what a step checks (tools/green.sh,
# SIZING_ENV: PROPERTY_RUNS and the like) is set.
# A run is green only if nothing outside the suite's own outputs (reports/,
# rendered/, and the figure blocks its last wave writes: tools/doc_figures.py --blocks-changed) changed while it
# ran; an edit made mid-run gets no marker. A run
# for a year other than the default (--year N) is checked but never marked
# green: a commit must have passed on the default year. It refuses to run when a
# git-ignored raw review file the review logs reference is missing
# (tools/worktree_data.py check; a linked worktree has none until cloned in). At most
# CHECK_ALL_MAX_RUNS runs, in any worktree and either script, execute at once (unset: two, and more
# while the machine's measured load and memory leave room for one); the others wait their turn
# (tools/check_slot.py). A green full run made in release mode
# (CHECK_ALL_RELEASE=1 with ENGINE_CACHE=verify) in the snapshot worktree of tools/check_all_bg.sh, where
# nothing else writes during the run, also adds its tree to the release list, which lets tools/release.sh tag
# that tree without running the suite again. Start such a run with
# `CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify tools/check_all_bg.sh --wait --tier full`.
# On the branch next, or in the main worktree on the branch main, it first folds the finished agent-run rows into
# research/costs/agent_runs.jsonl (tools/agent_runs_fold.py), so they are part of the tree it tests and
# the commit that follows; AGENT_RUNS_FOLD=0 skips the fold (tools/release.sh sets it).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

orig=("$@")
tier=light
rest=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --tier) tier="${2:-}"; shift; [ "$#" -gt 0 ] && shift ;;
    --tier=*) tier="${1#--tier=}"; shift ;;
    *) rest+=("$1"); shift ;;
  esac
done
set -- ${rest[@]+"${rest[@]}"}
marker="$(marker_of "$tier")" || exit 2
refuse_sizing_env || exit 2

if [ -z "${CHECK_ALL_SLOT:-}" ] && [ "${CHECK_ALL_PREFLIGHT:-}" != done ]; then
  tools/preflight.sh --tier "$tier" "$@" || exit 1
  export CHECK_ALL_PREFLIGHT=done
fi

# At most CHECK_ALL_MAX_RUNS runs execute at once on the machine (tools/check_slot.py): wait for a
# slot, then run again from the top holding it. A run started by check_all_bg.sh already holds one.
if [ -z "${CHECK_ALL_SLOT:-}" ]; then
  exec python3 tools/check_slot.py --tier "$tier" -- "$0" ${orig[@]+"${orig[@]}"}
fi

rm -f "$marker"
python3 tools/worktree_data.py check || exit 1
timeout 300 python3 tools/worktree_gc.py check || true  # listed, not failed: a release fails on it (release.sh)
year_of() { python3 -I -c 'import sys; sys.path.insert(0, "tools"); import taxyear; print(taxyear.Y)' "$@"; }
year="$(year_of "$@")"
default_year="$(year_of)"
if [ "${AGENT_RUNS_FOLD:-1}" != 0 ]; then python3 tools/agent_runs_fold.py --if-main || exit 1; fi
before="$(worktree_tree)"
tools/check_all_steps.sh --tier "$tier" "$@"
after="$(worktree_tree)"

outside="$(git diff-tree -r --name-only "$before" "$after" | grep -vE '^(reports|rendered)/' || true)"
if [ -n "$outside" ]; then
  # The figure blocks the last wave writes (tools/doc_figures.py) are the run's own output when only they changed.
  own="$(python3 tools/doc_figures.py --blocks-changed "$before")"
  outside="$(echo "$outside" | grep -vxF -f <(echo "$own"; echo /dev/null) || true)"
fi
if [ -n "$outside" ]; then
  echo "check-all passed, but these files changed during the run; no green marker written:" >&2
  echo "$outside" | sed 's/^/  /' >&2
  exit 1
fi
if [ "$year" != "$default_year" ]; then
  echo "check-all passed for $year; no green marker written (only a run on the default year, $default_year, is marked green)"
  exit 0
fi
echo "$after" > "$marker"
record_green "$after" "$tier"
echo "check-all green ($tier tier): tree $after"
bg_worktree="$(cd "$(git rev-parse --git-common-dir)" && pwd)/check-all-worktree"
if [ "$tier" = full ] && release_mode && [ "$(pwd -P)" = "$(cd "$bg_worktree" 2>/dev/null && pwd -P)" ]; then
  record_green "$after" release
  echo "check-all green in release mode: tree $after (tools/release.sh tags it without another run)"
fi
