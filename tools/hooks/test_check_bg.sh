#!/usr/bin/env bash
# Self-test for the per-run records of tools/check_all_bg.sh, in a temporary repository with a stub
# check-all: each run keeps its own record and log (runs/<tree>-<timestamp>/), `last` and `log` follow
# the newest, --status [TREE] reads them, only the newest 50 run directories are kept, a background
# run waits for a check-all slot while another holds it, and tools/commit_tested.sh can name the
# tree it commits. (The slot lock itself: tools/check_slot.py --self-test.)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/check-bg-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
fail() { echo "check-bg self-test: $*" >&2; exit 1; }

cd "$TMP"
git init -q
git config user.email test@example.com
git config user.name test
mkdir -p tools
cp "$ROOT/tools/green.sh" "$ROOT/tools/check_all_bg.sh" "$ROOT/tools/check_slot.py" tools/
cat > tools/worktree_data.py <<'PY'
import sys
sys.exit(0)
PY
cat > tools/check_all.sh <<'SH'
#!/usr/bin/env bash
set -euo pipefail
. tools/green.sh
tree="$(worktree_tree)"
echo "$tree" > "$(marker_of full)"
record_green "$tree" full
echo "stub check-all ok"
SH
chmod +x tools/*.sh tools/check_slot.py
echo one > f.txt
git add -A
git commit -qm base
unset CHECK_ALL_SLOT  # set when this test runs inside a check-all run, which would skip the slot wait
export CHECK_ALL_SLOT_DIR="$TMP/slots" CHECK_ALL_MAX_RUNS=2
state="$(cd "$(git rev-parse --git-common-dir)" && pwd)/check-all-bg"
get() { sed -n "s/^$2=//p" "$1"; }

tools/check_all_bg.sh --help | grep -q "check_all_bg.sh \[--wait\]" || fail "--help did not print the usage"
! tools/check_all_bg.sh --bogus 2>/dev/null || fail "an unknown argument was accepted"
[ ! -d "$state/runs" ] || fail "--help or an unknown argument started a run"
tools/check_all_bg.sh --wait > out1.txt 2>&1 || { cat out1.txt; fail "first run failed"; }
echo two > f.txt
sleep 1
tools/check_all_bg.sh --wait > out2.txt 2>&1 || { cat out2.txt; fail "second run failed"; }
[ "$(ls -1d "$state"/runs/*/ | wc -l)" -eq 2 ] || fail "expected two run directories"
t1="$(get "$(ls -1d "$state"/runs/*/ | head -n 1)status" snapshot)"
for d in "$state"/runs/*/; do
  [ -s "${d}status" ] && [ -s "${d}log" ] || fail "run directory ${d} lacks its status or log"
  grep -q 'stub check-all ok' "${d}log" || fail "the log of ${d} lacks the run's output"
done
newest="$(ls -1dt "$state"/runs/*/ | head -n 1)"
cmp -s "$state/last" "${newest}status" || fail "last is not the newest run's record"
dir_of() { basename "$(dirname "$1")"; }  # the run directory's name (the temp path may be spelled /var or /private/var)
[ "$(dir_of "$(readlink "$state/log")")" = "$(basename "$newest")" ] || fail "log does not point to the newest run's log"
[ "$(get "$state/last" status)" = green ] || fail "the stub run was not recorded green"
[ "$(dir_of "$(get "$state/last" log)")" = "$(basename "$newest")" ] || fail "the record names another log"

# Both records survive, each findable by tree; the older one is not the latest.
trees="$(for d in "$state"/runs/*/; do get "${d}status" snapshot; done | sort -u | wc -l)"
[ "$trees" -eq 2 ] || fail "the two runs did not record two snapshot trees"
old="$(tools/check_all_bg.sh --status "$(get "$state/last" snapshot)" | sed -n 's/^snapshot=//p')"
[ "$old" = "$(get "$state/last" snapshot)" ] || fail "--status TREE did not show that tree's record"
other="$(for d in "$state"/runs/*/; do get "${d}status" snapshot; done | grep -vx "$(get "$state/last" snapshot)")"
[ "$(tools/check_all_bg.sh --status "$other" | sed -n 's/^status=//p')" = green ] || fail "--status TREE lost the earlier run's record"
! tools/check_all_bg.sh --status 0000 > /dev/null 2>&1 || fail "--status of an unknown tree succeeded"
out="$(tools/check_all_bg.sh --status 2>&1)" || fail "--status failed: $out"
case "$out" in *'latest finished'*) ;; *) fail "--status lacks the latest finished run: $out" ;; esac

# A background run waits while the limit's slots are held, shows as running, and finishes when one frees.
CHECK_ALL_MAX_RUNS=1 python3 tools/check_slot.py -- sleep 60 &
holder=$!
for _ in $(seq 1 100); do case "$(python3 tools/check_slot.py --status 2>&1)" in 1*) break ;; esac; sleep 0.1; done
echo three > f.txt
CHECK_ALL_MAX_RUNS=1 tools/check_all_bg.sh > out3.txt 2>&1
sleep 1.5
running() { tools/check_all_bg.sh --status 2>&1 | sed -n 's/^running: pid /&/p'; }  # sed reads to the end: no broken pipe
[ -n "$(running)" ] || fail "--status does not show the waiting background run as running: $(tools/check_all_bg.sh --status 2>&1; ls -R "$state/runs" | head -20)"
grep -q 'waiting for a slot' "$(readlink "$state/log")" || fail "the waiting run did not say it was waiting"
kill "$holder"; wait "$holder" 2>/dev/null || true
for _ in $(seq 1 100); do [ -n "$(running)" ] || break; sleep 0.2; done
[ -z "$(running)" ] || fail "the background run did not finish after the slot freed"
[ "$(ls -1d "$state"/runs/*/ | wc -l)" -eq 3 ] || fail "expected three run directories"
[ "$(get "$state/last" status)" = green ] || fail "the waiting run did not finish green"

# Pruning keeps the newest 50.
for i in $(seq 1 60); do
  mkdir "$state/runs/fake$i-20000101-000000"
  echo status=green > "$state/runs/fake$i-20000101-000000/status"
  touch -t 200001010000 "$state/runs/fake$i-20000101-000000"
done
echo four > f.txt
tools/check_all_bg.sh --wait > out4.txt 2>&1 || fail "run before pruning failed"
[ "$(ls -1d "$state"/runs/*/ | wc -l)" -eq 50 ] || fail "pruning left $(ls -1d "$state"/runs/*/ | wc -l) run directories, not 50"
[ -s "$(ls -1dt "$state"/runs/*/ | head -n 1)status" ] || fail "pruning removed the newest run"
echo "check-bg self-test: ok"
