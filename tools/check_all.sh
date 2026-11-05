#!/usr/bin/env bash
# Runs the suite (tools/check_all_steps.sh, passing on its arguments, e.g.
# --tier fast or --year N) and, when it passes, writes the tested tree's hash to
# the tier's marker and list of green trees (tools/green.sh) for
# tools/hooks/pre-commit and pre-push. The tier is full unless --tier says otherwise.
# A run is green only if nothing outside the suite's own outputs (reports/,
# rendered/) changed while it ran; an edit made mid-run gets no marker. A run
# for a year other than the default (--year N) is checked but never marked
# green: a commit must have passed on the default year.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

tier=full
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

rm -f "$marker"
year_of() { python3 -I -c 'import sys; sys.path.insert(0, "tools"); import taxyear; print(taxyear.Y)' "$@"; }
year="$(year_of "$@")"
default_year="$(year_of)"
before="$(worktree_tree)"
tools/check_all_steps.sh --tier "$tier" "$@"
after="$(worktree_tree)"

outside="$(git diff-tree -r --name-only "$before" "$after" | grep -vE '^(reports|rendered)/' || true)"
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
