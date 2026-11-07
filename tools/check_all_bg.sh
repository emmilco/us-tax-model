#!/usr/bin/env bash
# Runs check-all on a snapshot of the working tree in a separate worktree, so the
# main tree stays free to edit while it runs.
#
#   tools/check_all_bg.sh [--wait] [--tier full|fast|docs] [--year N]
#                                     snapshot now and test it (detached unless --wait; tier full by default)
#   tools/check_all_bg.sh --status    the running run and the last finished one
#
# The snapshot is the tree a full `git add -A` would commit (tools/green.sh),
# wrapped in a commit object no ref points to. It is checked out in
# .git/check-all-worktree, a worktree this script owns and resets before each
# run (forced checkout, then `git clean -fd`). Ignored data the suite reads is
# copied in from the main tree as copy-on-write clones (cp -c): the review and
# extraction folders, node_modules and .engines/work fresh each run, the other
# .engines folders linked (read-only installs); lean/.lake is kept between runs;
# canonical/ and engine/dist are removed so the suite rebuilds them from the
# snapshot. tools/check_all.sh does the run; a green run records its tree in the
# clone's list of green trees for its tier, which both hooks read, and
# tools/commit_tested.sh commits that tree, from the worktree that started the run.
# One run at a time per clone.
#
# It runs from the main worktree or a linked one (an agent's). The snapshot and the
# review data come from the worktree it runs in, which must hold the review data
# in full (tools/worktree_data.py check; a linked worktree starts with none of it:
# tools/worktree_data.py clone <worktree> clones it in). node_modules, .engines and
# lean/.lake, which are installs, come from the main worktree when the worktree it
# runs in has none.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh

main="$(pwd)"
common="$(cd "$(git rev-parse --git-common-dir)" && pwd)"
wt="$common/check-all-worktree"
state="$common/check-all-bg"
lock="$state/lock"
cloned=(.transcription .classm .human-review .extraction-review .direct-file node_modules)
# The clone's main worktree (the first git lists): where installs come from when this worktree has none.
primary="$(git worktree list --porcelain | sed -n '1s/^worktree //p')"
# from NAME: the copy of the ignored folder NAME to use: this worktree's, or for an install
# this worktree lacks, the main worktree's.
from() {
  case "$1" in
    node_modules|.engines|lean/.lake) if [ -e "$main/$1" ]; then echo "$main/$1"; else echo "$primary/$1"; fi ;;
    *) echo "$main/$1" ;;
  esac
}

status() {
  if [ -d "$lock" ] && kill -0 "$(cat "$lock/pid" 2>/dev/null)" 2>/dev/null; then
    echo "running: pid $(cat "$lock/pid"), snapshot tree $(cat "$lock/tree"), log $state/log"
  fi
  if [ -f "$state/last" ]; then cat "$state/last"; else echo "no finished run"; fi
}

take_lock() {
  mkdir -p "$state"
  if ! mkdir "$lock" 2>/dev/null; then
    if kill -0 "$(cat "$lock/pid" 2>/dev/null)" 2>/dev/null; then
      echo "check-all-bg: a run is in progress (pid $(cat "$lock/pid")); see --status" >&2
      exit 1
    fi
    rm -rf "$lock"
    mkdir "$lock"
  fi
}

# prepare SNAP BASE: check out the snapshot's files with HEAD at BASE, the commit the snapshot was taken
# on, so that steps comparing the tree with HEAD (check_bug_inventory, siblings, human_review) see the
# snapshot's changes as uncommitted, as they would in the main worktree.
prepare() {
  local snap="$1" base="$2" e n
  if [ -e "$wt/.git" ]; then
    git -C "$wt" checkout -q --detach --force "$snap"
    git -C "$wt" clean -fdq
  else
    git worktree prune
    git worktree add -q --detach "$wt" "$snap"
  fi
  git -C "$wt" reset -q --soft "$base"
  rm -rf "$wt/canonical" "$wt/engine/dist"
  for e in "${cloned[@]}"; do
    rm -rf "${wt:?}/$e"
    if [ -e "$(from "$e")" ]; then cp -cR "$(from "$e")" "$wt/$e"; fi
  done
  rm -rf "$wt/.engines"
  if [ -d "$(from .engines)" ]; then
    mkdir "$wt/.engines"
    for e in "$(from .engines)"/* "$(from .engines)"/.[!.]*; do
      [ -e "$e" ] || continue
      n="$(basename "$e")"
      if [ "$n" = work ]; then cp -cR "$e" "$wt/.engines/work"; else ln -s "$e" "$wt/.engines/$n"; fi
    done
  fi
  if [ ! -d "$wt/lean/.lake" ] && [ -d "$(from lean/.lake)" ]; then cp -cR "$(from lean/.lake)" "$wt/lean/.lake"; fi
}

# run BASE TREE SNAP [check-all args]: test the snapshot and write $state/last.
run() {
  local base="$1" tree="$2" snap="$3" rc tested="" result tier=full a prev=""
  shift 3
  for a in "$@"; do
    case "$a" in --tier=*) tier="${a#--tier=}" ;; esac
    [ "$prev" = --tier ] && tier="$a"
    prev="$a"
  done
  trap 'rm -rf "$lock"' EXIT
  echo "check-all-bg: snapshot tree $tree (on $base), $tier tier, started $(date '+%Y-%m-%d %H:%M:%S')"
  prepare "$snap" "$base"
  set +e
  (cd "$wt" && tools/check_all.sh "$@")
  rc=$?
  set -e
  if [ "$rc" -eq 0 ]; then
    tested="$(cd "$wt" && . tools/green.sh && m="$(marker_of "$tier")" && { [ -s "$m" ] && cat "$m" || true; })"
  fi
  if [ "$rc" -ne 0 ]; then result=failed; elif [ -n "$tested" ]; then result=green; else result=passed-unmarked; fi
  {
    echo "status=$result"
    echo "tier=$tier"
    echo "base=$base"
    echo "snapshot=$tree"
    echo "snapshot_commit=$snap"
    echo "worktree=$main"
    echo "tested=$tested"
    echo "finished=$(date '+%Y-%m-%d %H:%M:%S')"
    echo "log=$state/log"
  } > "$state/last.tmp"
  mv "$state/last.tmp" "$state/last"
  echo "check-all-bg: $result"
  [ "$result" != failed ]
}

case "${1:-}" in
  --status) status; exit 0 ;;
  --run) shift; run "$@"; exit $? ;;
esac
wait=0
if [ "${1:-}" = "--wait" ]; then wait=1; shift; fi
if [ "$(cd "$main" && pwd -P)" = "$(cd "$wt" 2>/dev/null && pwd -P)" ]; then
  echo "check-all-bg: this is the background run's own worktree; run it from the worktree you edit" >&2
  exit 2
fi
python3 tools/worktree_data.py check || exit 1

take_lock
base="$(git rev-parse HEAD)"
tree="$(worktree_tree)"
snap="$(git commit-tree "$tree" -p "$base" -m "check-all snapshot")"
echo "$tree" > "$lock/tree"
if [ "$wait" -eq 1 ]; then
  echo $$ > "$lock/pid"
  run "$base" "$tree" "$snap" "$@" 2>&1 | tee "$state/log"
  exit "${PIPESTATUS[0]}"
fi
nohup "$0" --run "$base" "$tree" "$snap" "$@" > "$state/log" 2>&1 < /dev/null &
echo $! > "$lock/pid"
echo "check-all-bg: testing snapshot tree $tree in $wt (pid $!)"
echo "check-all-bg: log $state/log; tools/check_all_bg.sh --status; on green, commit it with tools/commit_tested.sh -F <file>"
