#!/usr/bin/env bash
# Self-test for tools/green.sh and tools/hooks/pre-commit, in a temporary repository:
# concurrent record_green calls must not lose entries in any tier's list; a tier's
# record implies the lower tiers' and not the higher; and pre-commit accepts a staged
# tree only when it is green in the tier the commit needs (tools/tier_paths.py). Then
# the path rule's own self-test on this repository (tools/tier_paths.py --self-test).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/green-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
fail() { echo "green self-test: $*" >&2; exit 1; }

cd "$TMP"
git init -q
git config user.email test@example.com
git config user.name test
mkdir -p tools/hooks
cp "$ROOT/tools/green.sh" "$ROOT/tools/tier_paths.py" "$ROOT/tools/docs_paths.txt" "$ROOT/tools/full_paths.txt" "$ROOT/tools/claims.py" "$ROOT/tools/check_bug_inventory.py" tools/
cp "$ROOT/tools/hooks/pre-commit" tools/hooks/
chmod +x tools/hooks/pre-commit
. tools/green.sh

# Concurrent records lose nothing, in each tier's own list.
for t in full fast docs; do
  for i in $(seq 1 20); do record_green "$t$i" "$t" & done
done
wait
for t in full fast docs; do
  for i in $(seq 1 20); do
    grep -qx "$t$i" "$(trees_of "$t")" || fail "lost entry $t$i"
  done
  [ "$(wc -l < "$(trees_of "$t")")" -eq 20 ] || fail "the $t list holds another tier's entries"
done

# A full-green tree is fast- and docs-green; a fast-green tree docs-green, not full-green.
is_tier_green fast full1 && is_tier_green docs full1 || fail "a full-green tree is not fast- and docs-green"
is_tier_green docs fast1 || fail "a fast-green tree is not docs-green"
! is_tier_green full fast1 || fail "a fast-green tree passed as full-green"
! is_tier_green fast docs1 || fail "a docs-green tree passed as fast-green"
for t in full fast docs; do rm -f "$(trees_of "$t")"; done
echo marker > "$(marker_of fast)"
is_tier_green fast marker && ! is_green marker || fail "the fast marker is not read as the fast record only"
rm -f "$(marker_of fast)"

# pre-commit. The base commit carries the path lists the next commit is judged by.
mkdir -p docs engine/src src
echo a > docs/a.md; echo m > engine/src/mutate.ts; echo s > src/s.txt; echo b > BUG_INVENTORY.md
git add -A
git commit -qm base
git config core.hooksPath tools/hooks
stage() { git reset -q --hard HEAD; for f in "$@"; do echo "$RANDOM" >> "$f"; done; git add -A; git write-tree; }
accepts() { git commit -qm "$1" >/dev/null 2>&1; }
# record_only TIER TREE: TREE is the only green tree of any tier (no arguments: none is).
record_only() { local x; for x in full fast docs; do rm -f "$(trees_of "$x")"; done; [ "$#" -lt 2 ] || record_green "$2" "$1"; }

# No record at all: refused.
t="$(stage docs/a.md)"; record_only
! accepts "no record" || fail "pre-commit accepted a commit with no green record"

# Docs tier: bookkeeping paths only, with a docs-green tree.
t="$(stage docs/a.md BUG_INVENTORY.md)"; record_only docs "$t"
accepts "docs" || fail "pre-commit refused a docs-only commit with a docs-green tree"
t="$(stage docs/a.md)"; record_only fast other
! accepts "docs without record" || fail "pre-commit accepted a docs-only commit with no green tree"

# One stray path outside the allowlist: the docs record is not enough; fast is.
t="$(stage docs/a.md src/s.txt)"; record_only docs "$t"
! accepts "stray" || fail "pre-commit accepted a docs-tier commit with a stray path on a docs-green tree"
record_only fast "$t"
accepts "stray fast" || fail "pre-commit refused a fast-green commit"

# A full-green tree also passes as fast.
t="$(stage src/s.txt)"; record_only full "$t"
accepts "full as fast" || fail "pre-commit refused a full-green tree for a fast-tier commit"

# Trigger path: fast is not enough; full is.
t="$(stage engine/src/mutate.ts)"; record_only fast "$t"
! accepts "trigger fast" || fail "pre-commit accepted a full-tier path change on a fast-green tree"
record_only full "$t"
accepts "trigger full" || fail "pre-commit refused a full-tier path change on a full-green tree"

# A commit cannot widen the allowlist it is judged by: the list is read from HEAD, so a
# list that names itself and src/ still leaves this commit in the fast tier.
git reset -q --hard HEAD
printf 'tools/docs_paths.txt\nsrc/*\n' >> tools/docs_paths.txt
echo x >> src/s.txt
git add -A
t="$(git write-tree)"; record_only docs "$t"
! accepts "widen" || fail "pre-commit let a commit widen the docs-tier list it was judged by"
git reset -q --hard HEAD
echo "green self-test: ok"

cd "$ROOT"
python3 -I tools/tier_paths.py --self-test
