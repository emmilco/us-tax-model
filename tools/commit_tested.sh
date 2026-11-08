#!/usr/bin/env bash
# Commits exactly the tree the last background check-all run tested
# (tools/check_all_bg.sh), leaving edits made since its snapshot uncommitted in
# the working tree. Arguments go to `git commit`, e.g. tools/commit_tested.sh -F msg.
#
# Refuses when the run was not green, when another worktree of the clone started it,
# when its tier is below the one the commit
# needs (tools/tier_paths.py: docs, fast or full), when HEAD has moved since the snapshot
# (committing the old tree would undo what came after), or when anything is
# staged (the tested tree replaces the index). The commit passes through
# tools/hooks/pre-commit as usual. Files the run regenerated (reports/,
# rendered/) are written into the working tree when the working tree still holds
# the snapshot's version of them; otherwise they are left as they are, and named.
# It reads the record of the latest finished run (check-all-bg/last), or with
# COMMIT_TESTED_TREE=<tree> that tree's latest run.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

common="$(cd "$(git rev-parse --git-common-dir)" && pwd)"
last="$common/check-all-bg/last"
die() { echo "commit-tested: $*" >&2; exit 1; }
# COMMIT_TESTED_TREE=<snapshot tree> commits that tree's latest run (a record under check-all-bg/runs/)
# instead of the latest finished one, for when another run finished after it.
if [ -n "${COMMIT_TESTED_TREE:-}" ]; then
  last="$(ls -1t "$common/check-all-bg/runs/$COMMIT_TESTED_TREE"-*/status 2>/dev/null | head -n 1 || true)"
  [ -n "$last" ] || die "no background run of snapshot tree $COMMIT_TESTED_TREE"
fi
get() { sed -n "s/^$1=//p" "$last"; }

[ -f "$last" ] || die "no finished background run (tools/check_all_bg.sh)"
[ "$(get status)" = green ] || die "the last background run is $(get status), not green; see $(get log)"
tested="$(get tested)"
snapshot="$(get snapshot)"
base="$(get base)"
tier="$(get tier)"
tier="${tier:-full}"
is_tier_green "$tier" "$tested" || die "tree $tested is not in the record of green $tier-tier runs"
run_wt="$(get worktree)"
[ -z "$run_wt" ] || [ "$run_wt" = "$(pwd)" ] || die "the last background run was started from $run_wt; commit it there"
[ "$(git rev-parse HEAD)" = "$base" ] || die "HEAD has moved since the snapshot (taken on $base); start a new run"
git diff --cached --quiet || die "the index has staged changes; unstage them first (the tested tree replaces the index)"
required_tier "$tested" "$base" || die "could not classify the tested tree's changes (tools/tier_paths.py)"
is_tier_green "$REQUIRED" "$tested" || die "the run was $tier-tier, but this commit needs the $REQUIRED tier: $REQUIRED_WHY"

carry=()
while IFS= read -r p; do
  snap_blob="$(git rev-parse -q --verify "$snapshot:$p" 2>/dev/null || true)"
  if [ -e "$p" ]; then current="$(git hash-object -- "$p")"; else current=""; fi
  if [ "$current" = "$snap_blob" ]; then
    carry+=("$p")
  else
    echo "commit-tested: $p changed in the working tree since the snapshot; left as it is" >&2
  fi
done < <(git diff-tree -r --name-only "$snapshot" "$tested")

git read-tree "$tested"
if ! git commit "$@"; then
  git read-tree HEAD
  die "commit failed; index restored to HEAD"
fi
for p in ${carry[@]+"${carry[@]}"}; do
  if git cat-file -e "$tested:$p" 2>/dev/null; then
    mkdir -p "$(dirname "$p")"
    git show "$tested:$p" > "$p"
  else
    rm -f -- "$p"
  fi
done
