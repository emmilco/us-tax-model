#!/usr/bin/env bash
# Self-test for tools/green.sh: concurrent record_green calls must not lose entries.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/green-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

cd "$TMP"
git init -q
mkdir -p tools
cp "$ROOT/tools/green.sh" tools/
. tools/green.sh
for i in $(seq 1 20); do record_green "tree$i" & done
wait
for i in $(seq 1 20); do
  if ! grep -qx "tree$i" "$GREEN_TREES"; then
    echo "green self-test: lost entry tree$i" >&2
    exit 1
  fi
done
echo "green self-test: ok"
