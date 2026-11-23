#!/usr/bin/env bash
# Self-test for tools/hooks/pre-push and tools/release.sh, in a temporary repository
# with no remote. pre-push must check every commit in the pushed range, not only the
# tip, each against its own parents in the tier it needs (tools/tier_paths.py); must
# handle a new ref against a remote-tracking base; must refuse main at a commit whose tree is not
# recorded release-green; and must refuse a release tag (refs/tags/r*) whose commit's tree is not
# full-green or not recorded release-ready. release.sh runs against stubs of tools/check_all_bg.sh and
# tools/release_reviews.sh and must promote next to main by fast-forward only, and tag, only a tree green
# in release mode whose sampled reviews are complete; it skips release_reviews.sh for a release-green tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/pre-push-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
fail() { echo "pre-push self-test: $*" >&2; exit 1; }

cd "$TMP"
git init -q
git symbolic-ref HEAD refs/heads/next
git config user.email test@example.com
git config user.name test
mkdir -p tools/hooks docs engine/src
cp "$ROOT/tools/green.sh" "$ROOT/tools/tier_paths.py" "$ROOT/tools/docs_paths.txt" "$ROOT/tools/claims.py" "$ROOT/tools/check_bug_inventory.py" \
  "$ROOT/tools/commit_tested.sh" "$ROOT/tools/release.sh" "$ROOT/tools/worktree_gc.py" "$ROOT/tools/worktree_data.py" tools/
cp "$ROOT/tools/hooks/pre-push" "$ROOT/tools/hooks/pre-commit" tools/hooks/
chmod +x tools/hooks/pre-push tools/hooks/pre-commit tools/commit_tested.sh tools/release.sh
echo a > docs/a.md; echo m > engine/src/mutate.ts
. tools/green.sh

Z=0000000000000000000000000000000000000000
commit() { for f in "${@:2}"; do echo "$1" >> "$f"; done; git add -A; git commit -qm "$1"; git rev-parse HEAD; }
tree() { git rev-parse "$1^{tree}"; }
only() { local x; for x in full light docs release; do rm -f "$(trees_of "$x")"; done; }
rec() { record_green "$(tree "$2")" "$1"; }
hook() { printf '%s %s %s %s\n' "$1" "$2" "$1" "$3" | tools/hooks/pre-push 2>/dev/null; }
branch() { hook "refs/heads/$1" "$2" "$3"; }

A="$(commit a f)"; B="$(commit b f)"; C="$(commit c f)"

# An untested intermediate commit is refused even when the tip's tree is green.
only; rec light "$C"
! branch next "$C" "$A" || fail "accepted an untested intermediate commit"

# Every commit in the range green in its tier: accepted.
only; rec light "$B"; rec light "$C"
branch next "$C" "$A" || fail "refused a light-green range"

# A new ref is measured against the remote-tracking base, not the whole history.
git update-ref refs/remotes/origin/next "$A"
branch new "$C" "$Z" || fail "refused a new ref whose commits past the remote base are green"

# A new ref with an untested commit is refused.
only; rec light "$C"
! branch new "$C" "$Z" || fail "accepted an untested commit on a new ref"

# A root commit needs the full tier.
git update-ref -d refs/remotes/origin/next
only; rec light "$A"; rec light "$B"; rec light "$C"
! branch new "$C" "$Z" || fail "accepted a root commit on a light-green tree"
rec full "$A"
branch new "$C" "$Z" || fail "refused a full-green root commit with light-green descendants"
git update-ref refs/remotes/origin/next "$C"

# An input of the release's steps (the mutation tool) needs only the light tier at commit.
D="$(commit d engine/src/mutate.ts)"
only; rec light "$D"
branch next "$D" "$C" || fail "refused a light-green change to an input of the release's steps"
git update-ref refs/remotes/origin/next "$D"

# Docs tier: a bookkeeping-only commit with a docs-green tree passes; with one stray path it does not.
E="$(commit e docs/a.md)"
only; rec docs "$E"
branch next "$E" "$D" || fail "refused a docs-only commit with a docs-green tree"
only
! branch next "$E" "$D" || fail "accepted a docs-only commit with no green tree"
F="$(commit f docs/a.md f)"
only; rec docs "$E"; rec docs "$F"
! branch next "$F" "$D" || fail "accepted a docs-tier commit with a stray path on a docs-green tree"
rec light "$F"
branch next "$F" "$D" || fail "refused a light-green commit after a docs-green one"
git update-ref refs/remotes/origin/next "$F"

# A merge needs at least the light tier, even when it changes only bookkeeping paths.
git checkout -q -b side "$E"
G="$(commit g docs/b.md)"
git checkout -q next
git merge -q --no-ff --no-verify -m merge "$G" >/dev/null
M="$(git rev-parse HEAD)"
only; rec light "$G"; rec docs "$M"
! branch next "$M" "$F" || fail "accepted a merge on a docs-green tree"
rec light "$M"
branch next "$M" "$F" || fail "refused a light-green merge"

# main: refused at a commit whose tree is only light- or full-green; accepted once a release-mode run recorded it.
only; rec light "$G"; rec light "$M"
! branch main "$M" "$F" || fail "accepted main at an unrecorded (light-green only) commit"
rec full "$M"
! branch main "$M" "$F" || fail "accepted main at a full-green commit with no release-mode record"
rec release "$M"
branch main "$M" "$F" || fail "refused main at a release-green commit"

# Release tags: refused unless the tagged commit's tree is full-green; other tags follow the branch rule.
git update-ref refs/remotes/origin/next "$M"
git tag -a r2026.01.01.1 -m t "$M"
only; rec light "$M"
! hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "accepted a release tag on a light-green tree"
rec full "$M"
! hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "accepted a release tag on a tree not recorded release-ready"
ready="$(cd "$(git rev-parse --git-common-dir)" && pwd)/release-ready"
mkdir -p "$ready" && : > "$ready/$(tree "$M")"
hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "refused a release tag on a full-green, release-ready tree"
git tag -a v1 -m t "$M"
only; rec light "$M"
hook refs/tags/v1 "$(git rev-parse v1)" "$Z" || fail "refused a non-release tag on a light-green commit"
git tag -d r2026.01.01.1 v1 >/dev/null

# release.sh, with a stub runner: STUB=same tests HEAD's tree, STUB=reports adds a regenerated report,
# STUB=red fails. The stub writes the background run's result file as tools/check_all_bg.sh does.
cat > tools/check_all_bg.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
. tools/green.sh
state="$(cd "$(git rev-parse --git-common-dir)" && pwd)/check-all-bg"
mkdir -p "$state"
snap="$(git rev-parse 'HEAD^{tree}')"
tested="$snap"
if [ "$STUB" = reports ]; then
  idx="$(mktemp)"
  GIT_INDEX_FILE="$idx" git read-tree HEAD
  blob="$(echo "report $RANDOM" | git hash-object -w --stdin)"
  GIT_INDEX_FILE="$idx" git update-index --add --cacheinfo "100644,$blob,reports/r.md"
  tested="$(GIT_INDEX_FILE="$idx" git write-tree)"
  rm -f "$idx"
fi
status=green
if [ "$STUB" = red ]; then status=failed; else record_green "$tested" full; ! release_mode || record_green "$tested" release; fi
echo "$tested" >> "$(git rev-parse --git-common-dir)/stub-runs"
printf 'status=%s\ntier=full\nbase=%s\nsnapshot=%s\nsnapshot_commit=%s\ntested=%s\nlog=%s\n' \
  "$status" "$(git rev-parse HEAD)" "$snap" "$snap" "$tested" "$state/log" > "$state/last"
[ "$status" = green ]
EOF
chmod +x tools/check_all_bg.sh
printf '#!/usr/bin/env bash\necho run >> "$(git rev-parse --git-common-dir)/reviews-runs"\n[ "${REVIEWS:-}" != incomplete ]\n' > tools/release_reviews.sh
chmod +x tools/release_reviews.sh
git add -A
git commit -qm stub --no-verify
git config core.hooksPath tools/hooks
day="$(date +%Y.%m.%d)"
common="$(git rev-parse --git-common-dir)"
# main starts at the first commit; next is ahead of it.
git branch -f main "$A"
only

# A commit on main is refused (pre-commit); main moves only by the release.
git checkout -q main
echo x >> f; git add -A
! git commit -qm "on main" 2>/dev/null || fail "pre-commit accepted a commit on main"
git reset -q; git checkout -q -- f; git checkout -q next

STUB=red tools/release.sh >/dev/null 2>&1 && fail "release.sh succeeded on a red run"
[ -z "$(git tag -l 'r*')" ] || fail "release.sh tagged after a red run"
[ "$(git rev-parse main)" = "$A" ] || fail "release.sh moved main after a red run"

REVIEWS=incomplete STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh succeeded with incomplete sampled reviews"
[ -z "$(git tag -l 'r*')" ] || fail "release.sh tagged with incomplete sampled reviews"

echo x > untracked.txt
STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh ran on a working tree that differs from HEAD"
rm untracked.txt

git checkout -q main
STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh ran with HEAD on main"
git checkout -q next

# main must be an ancestor: a main that diverged from next is never moved.
X="$(echo diverged | git commit-tree "$(tree "$A")" -p "$A")"
git branch -f main "$X"
STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh promoted a commit main is not an ancestor of"
[ "$(git rev-parse main)" = "$X" ] || fail "release.sh moved a diverged main"
git branch -f main "$A"

: > "$common/stub-runs"; : > "$common/reviews-runs"
STUB=same tools/release.sh >/dev/null
[ "$(git rev-parse "r$day.1^{commit}")" = "$(git rev-parse HEAD)" ] || fail "release.sh did not tag the tested tip as r$day.1"
[ "$(git rev-parse main)" = "$(git rev-parse next)" ] || fail "release.sh did not fast-forward main to next"
git merge-base --is-ancestor "$A" main || fail "main did not move by fast-forward"
is_release_green "$(tree "r$day.1")" || fail "the release tag's tree is not release-green"
[ "$(wc -l < "$common/stub-runs")" -eq 1 ] && [ "$(wc -l < "$common/reviews-runs")" -eq 1 ] || fail "the first release did not run the reviews and the full run once each"
hook refs/tags/r$day.1 "$(git rev-parse "r$day.1")" "$Z" || fail "pre-push refused the tag release.sh made"
# The commits of next before the release were pushed light-green; only main's tip needs the release record.
for c in $(git rev-list "$A..main"); do record_green "$(tree "$c")" light; done
branch main "$(git rev-parse main)" "$A" || fail "pre-push refused main at the release"

# A tree already release-green: neither the run nor release_reviews.sh again, even with reviews that would fail.
git tag -d "r$day.1" >/dev/null
git branch -f main "$A"
: > "$common/stub-runs"; : > "$common/reviews-runs"
REVIEWS=incomplete STUB=red tools/release.sh >/dev/null || fail "release.sh refused a release-green tree"
[ ! -s "$common/stub-runs" ] && [ ! -s "$common/reviews-runs" ] || fail "release.sh reran the run or the reviews for a release-green tree"
[ "$(git rev-parse main)" = "$(git rev-parse next)" ] || fail "release.sh did not promote the release-green tree"
git tag -d "r$day.1" >/dev/null

# A light commit on next, then a release whose run rewrites a report: the reports commit lands on next, main
# fast-forwards to it, and it is tagged.
echo more >> docs/a.md; git add -A
record_green "$(worktree_tree)" light
git commit -qm "light work on next" || fail "pre-commit refused a light-green commit on next"
before="$(git rev-parse HEAD)"
STUB=reports tools/release.sh >/dev/null
[ "$(git rev-parse HEAD^)" = "$before" ] || fail "release.sh did not commit the regenerated reports on next"
[ "$(git symbolic-ref --short HEAD)" = next ] || fail "the reports commit is not on next"
[ "$(git rev-parse main)" = "$(git rev-parse HEAD)" ] || fail "main was not fast-forwarded to the reports commit"
tag="$(git tag --points-at HEAD 'r*')"
[ -n "$tag" ] || fail "release.sh did not tag the reports commit"
[ -f reports/r.md ] || fail "release.sh did not write the regenerated report into the working tree"
hook "refs/tags/$tag" "$(git rev-parse "$tag")" "$Z" || fail "pre-push refused the tag release.sh made"
for c in $(git rev-list "$A..main"); do record_green "$(tree "$c")" light; done
branch main "$(git rev-parse main)" "$A" || fail "pre-push refused main at the promoted reports commit"

echo "pre-push self-test: ok"
