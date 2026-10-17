#!/usr/bin/env bash
# Shared by tools/check_all.sh and tools/hooks/pre-commit.
# worktree_tree prints the hash of the tree a full `git add -A` would commit
# (tracked and untracked files, ignored files excluded), without touching the
# real index. The marker holds that hash after a green check-all run.
MARKER="$(git rev-parse --git-path check-all-green)"

worktree_tree() {
  local tmp
  tmp="$(mktemp -d)"
  cp "$(git rev-parse --git-path index)" "$tmp/index" 2>/dev/null || true
  GIT_INDEX_FILE="$tmp/index" git add -A
  GIT_INDEX_FILE="$tmp/index" git write-tree
  rm -rf "$tmp"
}
