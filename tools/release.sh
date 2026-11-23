#!/usr/bin/env bash
# Makes a release: promotes a commit of `next` to `main`. For the commit, it ensures a green full check-all run in
# release mode of its exact tree (reusing the recorded one, or running it), fast-forwards main to it, and puts the
# annotated tag r<YYYY>.<MM>.<DD>.<n> on it.
#
#   tools/release.sh [--push] [--allow-open-bugs] [-F <file>] [<commit>]
#
# <commit> defaults to the tip of next. HEAD must be that commit, in a worktree whose working tree is HEAD's tree
# (`git add -A` would commit nothing): on next itself, or detached at an earlier commit of next. main must be an
# ancestor of the commit (main moves only forward, by fast-forward), and the commit must be on next.
#
# First step (recommended): tools/release_prep.sh on the candidate tree, as soon as its content is final; it runs the
# checks that fail in minutes.
#
# When the commit's tree is already in the release list (tools/green.sh: a green full run in release mode,
# CHECK_ALL_RELEASE=1 with ENGINE_CACHE=verify, in tools/check_all_bg.sh's snapshot worktree), the run is not
# repeated; tools/release_reviews.sh still runs, so that open bugs a release allows are named in its tag. Otherwise tools/release_reviews.sh runs first (on a fresh build; a form due
# or short of samples, or an unruled finding, promotes nothing), then the release-mode full run
# (tools/check_all_bg.sh --wait --tier full; ENGINE_CACHE=verify reruns every outside engine and compares its stored
# record). A run that is not green promotes nothing; the failing step's log names what broke. Either way a linked
# worktree that tools/worktree_gc.py check lists as removable or stale promotes nothing.
#
# A release-mode run rewrites reports the light tier leaves as they were (mutation, evaluator agreement, the engine
# differential, evidence, the interview length report, figures). When the tested tree differs from HEAD's,
# tools/commit_tested.sh commits it on HEAD, with the message in <file> or a generated one, and that commit is the
# one promoted. (On next, next advances to it; detached, the commit is on no branch until next merges main.)
#
# main is fast-forwarded to the promoted commit: in the worktree that has main checked out, by `git merge --ff-only`
# (which refuses to overwrite local changes there), or, when none has, by moving the ref. <n> is one more than the
# highest <n> among the day's local tags. The promoted tree is recorded under <git common dir>/release-ready/, which
# tools/hooks/pre-push requires of a pushed release tag. --push pushes main and the tag to origin, through
# tools/hooks/pre-push; without it nothing is pushed.
#
# A sampled-review ruling that confirms an open bug of medium or high severity promotes nothing, unless --allow-open-bugs
# is given: tools/release_reviews.sh and the release checks of the full run (CHECK_ALL_ALLOW_OPEN_BUGS=1) then pass
# it on, and the tag message lists each such ruling and bug ("allowed open bug:" lines of tools/release_reviews.sh).
#
# A release does not fold agent-run rows (AGENT_RUNS_FOLD=0): the tree it tests is HEAD's as committed, and the
# hooks write only the untracked pending file, so agents may run meanwhile.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh
die() { echo "release: $*" >&2; exit 1; }

push=0
allow=()
msg=""
target=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --push) push=1; shift ;;
    --allow-open-bugs) allow=(--allow-open-bugs); shift ;;
    -F) [ "$#" -ge 2 ] || die "-F needs a file"; msg="$2"; shift 2 ;;
    -*) die "unknown argument '$1' (usage: tools/release.sh [--push] [--allow-open-bugs] [-F <file>] [<commit>])" ;;
    *) [ -z "$target" ] || die "one commit at most"; target="$1"; shift ;;
  esac
done
[ -z "$msg" ] || [ -f "$msg" ] || die "no message file $msg"
git rev-parse -q --verify refs/heads/next >/dev/null || die "there is no branch next"
tip="$(git rev-parse --verify "${target:-next}^{commit}" 2>/dev/null)" || die "no commit ${target:-next}"
[ "$(git rev-parse HEAD)" = "$tip" ] || die "HEAD is not $tip (${target:-the tip of next}); release from a worktree whose HEAD is that commit"
case "$(git symbolic-ref -q HEAD || true)" in
  ""|refs/heads/next) ;;
  *) die "HEAD is the branch $(git symbolic-ref --short HEAD); release from next, or detached at a commit of next" ;;
esac
git merge-base --is-ancestor "$tip" next || die "$tip is not on next"
git merge-base --is-ancestor main "$tip" || die "main is not an ancestor of $tip; main moves only by fast-forward (merge main into next first)"
[ "$(worktree_tree)" = "$(git rev-parse 'HEAD^{tree}')" ] || die "the working tree differs from HEAD; a release tests the commit as committed"

python3 tools/worktree_gc.py check --fail || die "linked worktrees need removal, archiving or a keep lock (above); nothing promoted"
common="$(cd "$(git rev-parse --git-common-dir)" && pwd)"
last="$common/check-all-bg/last"
get() { sed -n "s/^$1=//p" "$last"; }
reviews_out="$(mktemp)"
trap 'rm -f "$reviews_out"' EXIT
allowed=""
head_tree="$(git rev-parse 'HEAD^{tree}')"
if is_release_green "$head_tree" && is_green "$head_tree"; then
  echo "release: tree $head_tree already passed a full run in release mode; not running it again"
  # The sampled reviews are checked again (minutes): the run cannot say whether it allowed open bugs, and the tag
  # must list the ones a release allows (--allow-open-bugs).
  if ! tools/release_reviews.sh ${allow[@]+"${allow[@]}"} 2>&1 | tee "$reviews_out"; then
    die "the sampled reviews are not complete for a release (above); nothing promoted"
  fi
  allowed="$(sed -n 's/^ *allowed open bug: //p' "$reviews_out")"
  tested="$head_tree"
else
  if ! tools/release_reviews.sh ${allow[@]+"${allow[@]}"} 2>&1 | tee "$reviews_out"; then
    die "the sampled reviews are not complete for a release (above); nothing promoted"
  fi
  allowed="$(sed -n 's/^ *allowed open bug: //p' "$reviews_out")"
  [ "$(worktree_tree)" = "$(git rev-parse 'HEAD^{tree}')" ] || die "the review check changed the working tree; nothing promoted"
  if ! AGENT_RUNS_FOLD=0 CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify CHECK_ALL_ALLOW_OPEN_BUGS="${allow:+1}" tools/check_all_bg.sh --wait --tier full; then
    die "the full run did not pass; nothing promoted (log: $common/check-all-bg/log)"
  fi
  [ "$(get status)" = green ] && [ "$(get tier)" = full ] || die "the full run is $(get status), not green; nothing promoted"
  [ "$(get base)" = "$tip" ] || die "the finished run was not on $tip; nothing promoted"
  [ "$(git rev-parse HEAD)" = "$tip" ] || die "HEAD moved during the run; nothing promoted"
  tested="$(get tested)"
  is_green "$tested" || die "tree $tested is not in the full-green record; nothing promoted"
  is_release_green "$tested" || die "tree $tested is not in the release record (a run in release mode); nothing promoted"
fi

if [ "$tested" != "$(git rev-parse 'HEAD^{tree}')" ]; then
  if [ -z "$msg" ]; then
    msg="$(mktemp)"
    trap 'rm -f "$msg" "$reviews_out"' EXIT
    printf 'Release reports: full check-all run in release mode on %s\n\nThe files a release-mode run rewrites and the light tier does not: mutation, evaluator\nagreement, the engine differential, evidence, the interview length report, figures.\n' \
      "$(git rev-parse --short "$tip")" > "$msg"
  fi
  tools/commit_tested.sh -F "$msg"
fi
commit="$(git rev-parse HEAD)"
[ "$(git rev-parse "$commit^{tree}")" = "$tested" ] || die "HEAD's tree is not the tested tree; nothing promoted"

# Fast-forward main to the commit: in the worktree holding main, or by moving the ref.
old_main="$(git rev-parse main)"
git merge-base --is-ancestor "$old_main" "$commit" || die "main moved and is no longer an ancestor of $commit; nothing promoted"
main_wt="$(git worktree list --porcelain | awk '/^worktree /{w=substr($0,10)} /^branch refs\/heads\/main$/{print w}')"
if [ -n "$main_wt" ]; then
  git -C "$main_wt" merge --ff-only -q "$commit" || die "main could not be fast-forwarded in $main_wt (local changes there?); nothing tagged"
else
  git update-ref -m "release: fast-forward to $commit" refs/heads/main "$commit" "$old_main"
fi
[ "$(git rev-parse main)" = "$commit" ] || die "main is not at $commit after the fast-forward; nothing tagged"

day="$(date +%Y.%m.%d)"
n=0
for t in $(git tag -l "r$day.*"); do
  k="${t##*.}"
  if [[ "$k" =~ ^[0-9]+$ ]] && [ "$k" -gt "$n" ]; then n="$k"; fi
done
name="r$day.$((n + 1))"
tag_msg="Release $name: full check-all green in release mode on tree $tested"
if [ -n "$allowed" ]; then
  tag_msg="$tag_msg

Released with open bugs of medium or high severity that sampled-review rulings confirm (--allow-open-bugs):
$(printf '%s\n' "$allowed" | sed 's/^/- /')"
fi
git tag -a "$name" -m "$tag_msg" "$commit"
mkdir -p "$common/release-ready" && : > "$common/release-ready/$tested"
echo "release: main fast-forwarded from $(git rev-parse --short "$old_main") to $(git rev-parse --short "$commit"); tagged $name (tree $tested)"
if [ -z "$(git symbolic-ref -q HEAD || true)" ] && ! git merge-base --is-ancestor "$commit" next; then
  echo "release: $(git rev-parse --short "$commit") is on main and not on next; merge main into next before the next release"
fi
if [ "$push" -eq 1 ]; then
  git push origin refs/heads/main "refs/tags/$name"
else
  echo "release: not pushed (git push origin main $name pushes both)"
fi
