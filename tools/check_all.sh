#!/usr/bin/env bash
# Runs the whole suite (npm run check-all-steps) and, when it passes, writes
# the tested tree's hash to .git/check-all-green for tools/hooks/pre-commit.
# A run is green only if nothing outside the suite's own outputs (reports/,
# rendered/) changed while it ran; an edit made mid-run gets no marker.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

rm -f "$MARKER"
before="$(worktree_tree)"
npm run check-all-steps --silent
after="$(worktree_tree)"

outside="$(git diff-tree -r --name-only "$before" "$after" | grep -vE '^(reports|rendered)/' || true)"
if [ -n "$outside" ]; then
  echo "check-all passed, but these files changed during the run; no green marker written:" >&2
  echo "$outside" | sed 's/^/  /' >&2
  exit 1
fi
echo "$after" > "$MARKER"
echo "check-all green: tree $after"
