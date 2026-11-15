#!/usr/bin/env bash
# Self-test of check-all's New York skip (tools/check_all_steps.sh): the real steps script, taxyear.py and
# jurisdiction.py run in a temporary repository in which every other tool, node and npm are stubs that log
# their arguments. For a year New York has adopted every ny_* step runs and the New York render runs; for a
# year it has not adopted, no ny_* step runs, each is listed in its wave as skipped with the reason, the run
# counts them at its start and end, and the New York render runs only when forms/ny/<year>/ exists.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
repo="$tmp/repo"
mkdir -p "$repo/tools" "$repo/forms/2025" "$repo/forms/2026" "$repo/forms/ny/2025" "$tmp/bin"
cp "$here/tools/check_all_steps.sh" "$here/tools/taxyear.py" "$here/tools/jurisdiction.py" "$repo/tools/"
calls="$tmp/calls"
export CALLS="$calls"
# Every other tools/ path the steps script names becomes a stub that logs its arguments.
for path in $(grep -oE 'tools/[A-Za-z0-9_/.-]+\.(py|mjs|sh)' "$here/tools/check_all_steps.sh" | sort -u); do
  case "$path" in tools/check_all_steps.sh|tools/taxyear.py|tools/jurisdiction.py) continue ;; esac
  mkdir -p "$repo/$(dirname "$path")"
  case "$path" in
    *.py) printf 'import os, sys\nopen(os.environ["CALLS"], "a").write("%s " + " ".join(sys.argv[1:]) + "\\n")\n' "$path" > "$repo/$path" ;;
    *) printf '#!/usr/bin/env bash\necho "%s $*" >> "$CALLS"\n' "$path" > "$repo/$path"; chmod +x "$repo/$path" ;;
  esac
done
for cmd in node npm; do
  printf '#!/usr/bin/env bash\necho "%s $*" >> "$CALLS"\n' "$cmd" > "$tmp/bin/$cmd"; chmod +x "$tmp/bin/$cmd"
done
git -C "$repo" init -q

failures=0
fail() { echo "check-all New York skip self-test: $1" >&2; failures=$((failures + 1)); }
run() {  # run NY_ADOPTED ARGS...: the fast tier with years.json's ny_adopted set; output in $tmp/out
  printf '{"adopted": [2025, 2026], "ny_adopted": %s}\n' "$1" > "$repo/years.json"; shift
  : > "$calls"
  (cd "$repo" && PATH="$tmp/bin:$PATH" bash tools/check_all_steps.sh --tier fast "$@") > "$tmp/out" 2>&1 || {
    fail "the run failed:"; sed 's/^/  /' "$tmp/out" >&2; return 0; }
}
has() { grep -qF -- "$2" "$1" || fail "expected in $1: $2"; }
lacks() { if grep -qF -- "$2" "$1"; then fail "not expected in $1: $2"; fi; }

# New York adopted: every New York step runs, nothing is skipped.
run "[2025]" --year 2025
has "$calls" "tools/citations.py --strict --jurisdiction ny --year 2025"
has "$calls" "tools/extract_ny_tax_table.py --check --year 2025"
has "$calls" "node engine/dist/main.js test-fixtures --ny --year 2025"
has "$calls" "node engine/dist/main.js render --ny --year 2025"
lacks "$tmp/out" "New York steps skipped"; lacks "$tmp/out" "skipped: New York"
adopted_steps="$(grep -c '^== ny_' "$tmp/out" || true)"

# Not adopted, no New York definitions: no New York step runs, each is listed as skipped, with the counts.
run "[2025]" --year 2026
lacks "$calls" "jurisdiction ny"
lacks "$calls" "--ny"
lacks "$calls" "extract_ny_"
has "$tmp/out" "render --ny skipped: no forms/ny/2026/"
has "$tmp/out" "check-all: New York steps skipped for 2026: New York has not adopted 2026 (years.json ny_adopted: 2025)"
has "$tmp/out" "skipped: New York has not adopted 2026 (years.json ny_adopted: 2025)"
skipped_steps="$(grep -c '^== ny_' "$tmp/out" || true)"
[ "$skipped_steps" = "$adopted_steps" ] && [ "$skipped_steps" -gt 0 ] ||
  fail "listed $skipped_steps New York steps as skipped, but $adopted_steps run when adopted"
has "$tmp/out" "check-all: $adopted_steps New York steps skipped for 2026 ("
has "$calls" "tools/citations.py --strict --year 2026"

# Not adopted, but its definitions exist: still skipped, the render runs, and the reason says to adopt it.
mkdir -p "$repo/forms/ny/2026"
run "[2025]" --year 2026
lacks "$calls" "jurisdiction ny"
has "$calls" "node engine/dist/main.js render --ny --year 2026"
has "$tmp/out" "add 2026 to ny_adopted to check it"

# Adopted with its definitions: unchanged from 2025's run.
run "[2025, 2026]" --year 2026
has "$calls" "tools/citations.py --strict --jurisdiction ny --year 2026"
lacks "$tmp/out" "New York steps skipped"; lacks "$tmp/out" "skipped: New York"

# Listed without definitions: the run refuses before any step.
rmdir "$repo/forms/ny/2026"
printf '{"adopted": [2025, 2026], "ny_adopted": [2025, 2026]}\n' > "$repo/years.json"
: > "$calls"
if (cd "$repo" && PATH="$tmp/bin:$PATH" bash tools/check_all_steps.sh --tier fast --year 2026) > "$tmp/out" 2>&1; then
  fail "a year listed under ny_adopted without forms/ny/<year>/ was run"
fi
has "$tmp/out" "forms/ny/2026/ does not exist"
[ ! -s "$calls" ] || fail "steps ran although the New York list was refused"

if [ "$failures" -gt 0 ]; then
  echo "check-all New York skip self-test FAILED: $failures problem(s)" >&2
  exit 1
fi
echo "check-all New York skip self-test OK: $adopted_steps New York steps run when adopted and listed as skipped when not; render, adoption hint and bad list checked"
