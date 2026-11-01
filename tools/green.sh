#!/usr/bin/env bash
# Shared by tools/check_all.sh, tools/check_all_bg.sh, tools/commit_tested.sh and the hooks.
# worktree_tree prints the hash of the tree a full `git add -A` would commit
# (tracked and untracked files, ignored files excluded), without touching the
# real index. The marker holds that hash after a green check-all run in this
# worktree. GREEN_TREES lists the trees of the last 50 green runs in any
# worktree of the clone, most recent last; is_green accepts a tree in either.
MARKER="$(git rev-parse --git-path check-all-green)"
GREEN_TREES="$(cd "$(git rev-parse --git-common-dir)" && pwd)/check-all-green-trees"

worktree_tree() {
  local tmp
  tmp="$(mktemp -d)"
  cp "$(git rev-parse --git-path index)" "$tmp/index" 2>/dev/null || true
  GIT_INDEX_FILE="$tmp/index" git add -A
  GIT_INDEX_FILE="$tmp/index" git write-tree
  rm -rf "$tmp"
}

record_green() (
  # Serialize the read-modify-write: a foreground and a background run can finish together,
  # and an unlocked tail/mv would lose one of the entries.
  local lock="$GREEN_TREES.lock" tmp n=0
  until mkdir "$lock" 2>/dev/null; do
    n=$((n + 1))
    if [ "$n" -gt 600 ]; then echo "green.sh: timed out waiting for $lock" >&2; exit 1; fi
    sleep 0.1
  done
  trap 'rmdir "$lock" 2>/dev/null || true' EXIT
  tmp="$(mktemp "$GREEN_TREES.XXXXXX")"
  { [ -f "$GREEN_TREES" ] && tail -n 49 "$GREEN_TREES"; echo "$1"; } > "$tmp"
  mv "$tmp" "$GREEN_TREES"
)

is_green() {
  { [ -s "$MARKER" ] && [ "$(cat "$MARKER")" = "$1" ]; } && return 0
  [ -f "$GREEN_TREES" ] && grep -qx "$1" "$GREEN_TREES"
}
