#!/usr/bin/env bash
# Shared by tools/check_all.sh, tools/check_all_bg.sh, tools/commit_tested.sh, tools/release.sh
# and the hooks. worktree_tree prints the hash of the tree a full `git add -A` would commit
# (tracked and untracked files, ignored files excluded), without touching the real index.
#
# Each tier of check-all (full, fast, docs; tools/check_all_steps.sh) has its own record: a marker
# holding the tree of the last green run of that tier in this worktree, and a list of the trees of
# the last 50 green runs of that tier in any worktree of the clone, most recent last. The full
# record is MARKER and GREEN_TREES. A tier's steps include the next tier's, so is_tier_green
# accepts a tree green in that tier or a higher one: full-green is also fast- and docs-green.
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

marker_of() {
  case "$1" in
    full) echo "$MARKER" ;;
    fast|docs) echo "$MARKER-$1" ;;
    *) echo "green.sh: unknown tier '$1'" >&2; return 1 ;;
  esac
}

trees_of() {
  case "$1" in
    full) echo "$GREEN_TREES" ;;
    fast|docs) echo "${GREEN_TREES%-trees}-$1-trees" ;;
    *) echo "green.sh: unknown tier '$1'" >&2; return 1 ;;
  esac
}

# record_green TREE [TIER]: add TREE to the tier's list (default full).
record_green() (
  # Serialize the read-modify-write: a foreground and a background run can finish together,
  # and an unlocked tail/mv would lose one of the entries.
  local list lock tmp n=0
  list="$(trees_of "${2:-full}")" || exit 1
  lock="$list.lock"
  until mkdir "$lock" 2>/dev/null; do
    n=$((n + 1))
    if [ "$n" -gt 600 ]; then echo "green.sh: timed out waiting for $lock" >&2; exit 1; fi
    sleep 0.1
  done
  trap 'rmdir "$lock" 2>/dev/null || true' EXIT
  tmp="$(mktemp "$list.XXXXXX")"
  { [ -f "$list" ] && tail -n 49 "$list"; echo "$1"; } > "$tmp"
  mv "$tmp" "$list"
)

# in_record TIER TREE: TREE is the tier's marker or in the tier's list (that tier only).
in_record() {
  local marker list
  marker="$(marker_of "$1")" && list="$(trees_of "$1")" || return 1
  { [ -s "$marker" ] && [ "$(cat "$marker")" = "$2" ]; } && return 0
  [ -f "$list" ] && grep -qx "$2" "$list"
}

is_green() { in_record full "$1"; }

is_tier_green() {
  case "$1" in
    full) in_record full "$2" ;;
    fast) in_record full "$2" || in_record fast "$2" ;;
    docs) in_record full "$2" || in_record fast "$2" || in_record docs "$2" ;;
    *) echo "green.sh: unknown tier '$1'" >&2; return 1 ;;
  esac
}

# any_record: some tier has a marker or a list.
any_record() {
  local t
  for t in full fast docs; do
    [ -s "$(marker_of "$t")" ] || [ -s "$(trees_of "$t")" ] && return 0
  done
  return 1
}

# required_tier TREE [PARENT...]: sets REQUIRED (docs, fast or full) and REQUIRED_WHY for a commit of
# TREE on those parents (tools/tier_paths.py, which reads each parent's tools/docs_paths.txt and
# tools/full_paths.txt).
required_tier() {
  local out
  out="$(python3 -I "$(git rev-parse --show-toplevel)/tools/tier_paths.py" required "$@")" || return 1
  REQUIRED="${out%%$'\t'*}"
  REQUIRED_WHY="${out#*$'\t'}"
}

# tree_accepted TREE [PARENT...]: TREE is green in the tier a commit of it on those parents needs.
tree_accepted() {
  required_tier "$@" || return 1
  is_tier_green "$REQUIRED" "$1"
}
