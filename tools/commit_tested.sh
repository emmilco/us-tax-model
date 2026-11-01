#!/usr/bin/env bash
# Commits exactly the tree the last background check-all run tested
# (tools/check_all_bg.sh), leaving edits made since its snapshot uncommitted in
# the working tree. Arguments go to `git commit`, e.g. tools/commit_tested.sh -F msg.
#
# Refuses when the run was not green, when HEAD has moved since the snapshot
# (committing the old tree would undo what came after), or when anything is
# staged (the tested tree replaces the index). The commit passes through
# tools/hooks/pre-commit as usual. Files the run regenerated (reports/,
# rendered/) are written into the working tree when the working tree still holds
# the snapshot's version of them; otherwise they are left as they are, and named.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

common="$(cd "$(git rev-parse --git-common-dir)" && pwd)"
last="$common/check-all-bg/last"
die() { echo "commit-tested: $*" >&2; exit 1; }
get() { sed -n "s/^$1=//p" "$last"; }

[ -f "$last" ] || die "no finished background run (tools/check_all_bg.sh)"
[ "$(get status)" = green ] || die "the last background run is $(get status), not green; see $(get log)"
tested="$(get tested)"
snapshot="$(get snapshot)"
base="$(get base)"
is_green "$tested" || die "tree $tested is not in the record of green runs"
[ "$(git rev-parse HEAD)" = "$base" ] || die "HEAD has moved since the snapshot (taken on $base); start a new run"
git diff --cached --quiet || die "the index has staged changes; unstage them first (the tested tree replaces the index)"

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
