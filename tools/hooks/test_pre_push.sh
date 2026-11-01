#!/usr/bin/env bash
# Self-test for tools/hooks/pre-push: it must check every commit in the pushed
# range, not only the tip, and must handle a new ref against a remote-tracking base.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/pre-push-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

cd "$TMP"
git init -q
git config user.email test@example.com
git config user.name test
mkdir -p tools/hooks
cp "$ROOT/tools/green.sh" tools/
cp "$ROOT/tools/hooks/pre-push" tools/hooks/
chmod +x tools/hooks/pre-push
git config core.hooksPath tools/hooks

commit() { echo "$1" >> f; git add f; git commit -qm "$1"; git rev-parse HEAD; }
A="$(commit a)"; B="$(commit b)"; C="$(commit c)"
green() { git rev-parse "$1^{tree}"; }
hook() { printf 'refs/heads/%s %s refs/heads/%s %s\n' "$1" "$2" "$1" "$3" | tools/hooks/pre-push; }

# An untested intermediate commit is refused even when the tip's tree is green.
echo "$(green "$C")" > .git/check-all-green-trees
if hook main "$C" "$A" 2>/dev/null; then
  echo "pre-push self-test: accepted an untested intermediate commit" >&2
  exit 1
fi

# Every commit in the range green: accepted.
printf '%s\n%s\n' "$(green "$B")" "$(green "$C")" > .git/check-all-green-trees
hook main "$C" "$A"

# A new ref is measured against the remote-tracking base, not the whole history.
git update-ref refs/remotes/origin/main "$A"
hook new "$C" 0000000000000000000000000000000000000000

# A new ref with an untested commit is refused.
echo "$(green "$C")" > .git/check-all-green-trees
if hook new "$C" 0000000000000000000000000000000000000000 2>/dev/null; then
  echo "pre-push self-test: accepted an untested commit on a new ref" >&2
  exit 1
fi

echo "pre-push self-test: ok"
