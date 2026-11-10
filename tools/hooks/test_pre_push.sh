#!/usr/bin/env bash
# Self-test for tools/hooks/pre-push and tools/release.sh, in a temporary repository
# with no remote. pre-push must check every commit in the pushed range, not only the
# tip, each against its own parents in the tier it needs (tools/tier_paths.py); must
# handle a new ref against a remote-tracking base; and must refuse a release tag
# (refs/tags/r*) whose commit's tree is not full-green or not recorded release-ready. release.sh
# runs against stubs of tools/check_all_bg.sh and tools/release_reviews.sh and must tag only a
# full-green tree whose sampled reviews are complete.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/pre-push-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
fail() { echo "pre-push self-test: $*" >&2; exit 1; }

cd "$TMP"
git init -q
git symbolic-ref HEAD refs/heads/main
git config user.email test@example.com
git config user.name test
mkdir -p tools/hooks docs engine/src
cp "$ROOT/tools/green.sh" "$ROOT/tools/tier_paths.py" "$ROOT/tools/docs_paths.txt" "$ROOT/tools/full_paths.txt" "$ROOT/tools/claims.py" "$ROOT/tools/check_bug_inventory.py" \
  "$ROOT/tools/commit_tested.sh" "$ROOT/tools/release.sh" tools/
cp "$ROOT/tools/hooks/pre-push" "$ROOT/tools/hooks/pre-commit" tools/hooks/
chmod +x tools/hooks/pre-push tools/hooks/pre-commit tools/commit_tested.sh tools/release.sh
echo a > docs/a.md; echo m > engine/src/mutate.ts
. tools/green.sh

Z=0000000000000000000000000000000000000000
commit() { for f in "${@:2}"; do echo "$1" >> "$f"; done; git add -A; git commit -qm "$1"; git rev-parse HEAD; }
tree() { git rev-parse "$1^{tree}"; }
only() { local x; for x in full fast docs; do rm -f "$(trees_of "$x")"; done; }
rec() { record_green "$(tree "$2")" "$1"; }
hook() { printf '%s %s %s %s\n' "$1" "$2" "$1" "$3" | tools/hooks/pre-push 2>/dev/null; }
branch() { hook "refs/heads/$1" "$2" "$3"; }

A="$(commit a f)"; B="$(commit b f)"; C="$(commit c f)"

# An untested intermediate commit is refused even when the tip's tree is green.
only; rec fast "$C"
! branch main "$C" "$A" || fail "accepted an untested intermediate commit"

# Every commit in the range green in its tier: accepted.
only; rec fast "$B"; rec fast "$C"
branch main "$C" "$A" || fail "refused a fast-green range"

# A new ref is measured against the remote-tracking base, not the whole history.
git update-ref refs/remotes/origin/main "$A"
branch new "$C" "$Z" || fail "refused a new ref whose commits past the remote base are green"

# A new ref with an untested commit is refused.
only; rec fast "$C"
! branch new "$C" "$Z" || fail "accepted an untested commit on a new ref"

# A root commit needs the full tier.
git update-ref -d refs/remotes/origin/main
only; rec fast "$A"; rec fast "$B"; rec fast "$C"
! branch new "$C" "$Z" || fail "accepted a root commit on a fast-green tree"
rec full "$A"
branch new "$C" "$Z" || fail "refused a full-green root commit with fast-green descendants"
git update-ref refs/remotes/origin/main "$C"

# Trigger path: a fast-green tree is refused, a full-green one accepted.
D="$(commit d engine/src/mutate.ts)"
only; rec fast "$D"
! branch main "$D" "$C" || fail "accepted a full-tier path change on a fast-green tree"
rec full "$D"
branch main "$D" "$C" || fail "refused a full-tier path change on a full-green tree"
git update-ref refs/remotes/origin/main "$D"

# Docs tier: a bookkeeping-only commit with a docs-green tree passes; with one stray path it does not.
E="$(commit e docs/a.md)"
only; rec docs "$E"
branch main "$E" "$D" || fail "refused a docs-only commit with a docs-green tree"
only
! branch main "$E" "$D" || fail "accepted a docs-only commit with no green tree"
F="$(commit f docs/a.md f)"
only; rec docs "$E"; rec docs "$F"
! branch main "$F" "$D" || fail "accepted a docs-tier commit with a stray path on a docs-green tree"
rec fast "$F"
branch main "$F" "$D" || fail "refused a fast-green commit after a docs-green one"
git update-ref refs/remotes/origin/main "$F"

# A merge needs at least the fast tier, even when it changes only bookkeeping paths.
git checkout -q -b side "$E"
G="$(commit g docs/b.md)"
git checkout -q main
git merge -q --no-ff --no-verify -m merge "$G" >/dev/null
M="$(git rev-parse HEAD)"
only; rec fast "$G"; rec docs "$M"
! branch main "$M" "$F" || fail "accepted a merge on a docs-green tree"
rec fast "$M"
branch main "$M" "$F" || fail "refused a fast-green merge"

# Release tags: refused unless the tagged commit's tree is full-green; other tags follow the branch rule.
git update-ref refs/remotes/origin/main "$M"
git tag -a r2026.01.01.1 -m t "$M"
only; rec fast "$M"
! hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "accepted a release tag on a fast-green tree"
rec full "$M"
! hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "accepted a release tag on a tree not recorded release-ready"
ready="$(cd "$(git rev-parse --git-common-dir)" && pwd)/release-ready"
mkdir -p "$ready" && : > "$ready/$(tree "$M")"
hook refs/tags/r2026.01.01.1 "$(git rev-parse r2026.01.01.1)" "$Z" || fail "refused a release tag on a full-green, release-ready tree"
git tag -a v1 -m t "$M"
only; rec fast "$M"
hook refs/tags/v1 "$(git rev-parse v1)" "$Z" || fail "refused a non-release tag on a fast-green commit"
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
if [ "$STUB" = red ]; then status=failed; else record_green "$tested" full; fi
printf 'status=%s\ntier=full\nbase=%s\nsnapshot=%s\nsnapshot_commit=%s\ntested=%s\nlog=%s\n' \
  "$status" "$(git rev-parse HEAD)" "$snap" "$snap" "$tested" "$state/log" > "$state/last"
[ "$status" = green ]
EOF
chmod +x tools/check_all_bg.sh
printf '#!/usr/bin/env bash\n[ "${REVIEWS:-}" != incomplete ]\n' > tools/release_reviews.sh
chmod +x tools/release_reviews.sh
git add -A
git commit -qm stub --no-verify
git config core.hooksPath tools/hooks
day="$(date +%Y.%m.%d)"

STUB=red tools/release.sh >/dev/null 2>&1 && fail "release.sh succeeded on a red run"
[ -z "$(git tag -l 'r*')" ] || fail "release.sh tagged after a red run"

REVIEWS=incomplete STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh succeeded with incomplete sampled reviews"
[ -z "$(git tag -l 'r*')" ] || fail "release.sh tagged with incomplete sampled reviews"

echo x > untracked.txt
STUB=same tools/release.sh >/dev/null 2>&1 && fail "release.sh ran on a working tree that differs from HEAD"
rm untracked.txt

STUB=same tools/release.sh >/dev/null
[ "$(git rev-parse "r$day.1^{commit}")" = "$(git rev-parse HEAD)" ] || fail "release.sh did not tag the tested tip as r$day.1"
is_green "$(tree "r$day.1")" || fail "the release tag's tree is not full-green"

before="$(git rev-parse HEAD)"
STUB=reports tools/release.sh >/dev/null
[ "$(git rev-parse HEAD^)" = "$before" ] || fail "release.sh did not commit the regenerated reports on the tip"
[ "$(git rev-parse "r$day.2^{commit}")" = "$(git rev-parse HEAD)" ] || fail "release.sh did not tag the reports commit as r$day.2"
[ -f reports/r.md ] || fail "release.sh did not write the regenerated report into the working tree"
hook "refs/tags/r$day.2" "$(git rev-parse "r$day.2")" "$Z" || fail "pre-push refused the tag release.sh made"

echo "pre-push self-test: ok"
