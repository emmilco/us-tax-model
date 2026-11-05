#!/usr/bin/env bash
# Makes a release: a full check-all run on the clean tip of main and, when it is green,
# the annotated tag r<YYYY>.<MM>.<DD>.<n> on a commit whose tree that run tested.
#
#   tools/release.sh [--push] [-F <file>]
#
# HEAD must be the branch main, in the main worktree, with nothing to commit (the tree
# `git add -A` would commit is HEAD's tree). The run is tools/check_all_bg.sh --wait
# --tier full. A full run rewrites reports the fast tier leaves as they were (mutation,
# evaluator agreement, the engine differential, and evidence without its fast-run
# note); when the tested tree differs from HEAD's, tools/commit_tested.sh commits it,
# with the message in <file> or a generated one, and the tag goes on that commit.
# <n> is one more than the highest <n> among the day's existing local tags. A run that
# is not green tags nothing; the failing step's log names what broke.
# --push pushes the tag to origin, through tools/hooks/pre-push; without it nothing is
# pushed.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
. tools/green.sh
die() { echo "release: $*" >&2; exit 1; }

push=0
msg=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --push) push=1; shift ;;
    -F) [ "$#" -ge 2 ] || die "-F needs a file"; msg="$2"; shift 2 ;;
    *) die "unknown argument '$1' (usage: tools/release.sh [--push] [-F <file>])" ;;
  esac
done
[ -z "$msg" ] || [ -f "$msg" ] || die "no message file $msg"
[ "$(git symbolic-ref -q HEAD || true)" = refs/heads/main ] || die "HEAD is not the branch main"
[ "$(worktree_tree)" = "$(git rev-parse 'HEAD^{tree}')" ] || die "the working tree differs from HEAD; a release tests the tip as committed"
tip="$(git rev-parse HEAD)"

common="$(cd "$(git rev-parse --git-common-dir)" && pwd)"
last="$common/check-all-bg/last"
get() { sed -n "s/^$1=//p" "$last"; }
if ! tools/check_all_bg.sh --wait --tier full; then
  die "the full run did not pass; nothing tagged (log: $common/check-all-bg/log)"
fi
[ "$(get status)" = green ] && [ "$(get tier)" = full ] || die "the full run is $(get status), not green; nothing tagged"
[ "$(get base)" = "$tip" ] || die "the finished run was not on $tip; nothing tagged"
[ "$(git rev-parse HEAD)" = "$tip" ] || die "HEAD moved during the run; nothing tagged"
tested="$(get tested)"
is_green "$tested" || die "tree $tested is not in the full-green record; nothing tagged"

if [ "$tested" != "$(git rev-parse 'HEAD^{tree}')" ]; then
  if [ -z "$msg" ]; then
    msg="$(mktemp)"
    trap 'rm -f "$msg"' EXIT
    printf 'Release reports: full check-all run on %s\n\nThe reports a full run rewrites and the fast tier does not: mutation, evaluator\nagreement, the engine differential, and evidence.\n' \
      "$(git rev-parse --short "$tip")" > "$msg"
  fi
  tools/commit_tested.sh -F "$msg"
fi
commit="$(git rev-parse HEAD)"
[ "$(git rev-parse "$commit^{tree}")" = "$tested" ] || die "HEAD's tree is not the tested tree; nothing tagged"

day="$(date +%Y.%m.%d)"
n=0
for t in $(git tag -l "r$day.*"); do
  k="${t##*.}"
  if [[ "$k" =~ ^[0-9]+$ ]] && [ "$k" -gt "$n" ]; then n="$k"; fi
done
name="r$day.$((n + 1))"
git tag -a "$name" -m "Release $name: full check-all green on tree $tested" "$commit"
echo "release: tagged $name on $(git rev-parse --short "$commit") (tree $tested)"
if [ "$push" -eq 1 ]; then
  git push origin "refs/tags/$name"
else
  echo "release: not pushed (git push origin $name pushes it)"
fi
