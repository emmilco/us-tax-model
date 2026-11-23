#!/usr/bin/env bash
# The preflight of a check-all run: regenerate, in the working tree, every derived file a check-all step compares with
# what it would write, then run the bookkeeping checks that fail in seconds. tools/check_all.sh and
# tools/check_all_bg.sh run it first, in the worktree being tested (check_all_bg.sh before it takes its snapshot), and
# stop when it fails; CHECK_ALL_PREFLIGHT=done skips it (check_all_bg.sh sets it for the run in its snapshot).
#
#   tools/preflight.sh [--tier light|full|docs] [--year N]
#
# 1. The build, when it is stale (tools/build_fresh.py): npm run compile and the build. The person wording report and
#    the coverage tree are generated from it.
# 2. Regenerate, each with the command whose --check the step runs: reports/bug_status.md (tools/bug_status.py --write),
#    docs/COVERAGE.md and the README's coverage table (tools/coverage/tree.py), reports/<year>/gate_frequencies.md
#    (tools/coverage/gate_frequencies.py), reports/<year>/person_wording.md (spouse-wording --report), and, when the run
#    will compare it (the full tier, or a light run whose change is unscoped: tools/change_scope.py prints all),
#    reports/<year>/interview_coverage.md (interview-coverage --write). Last, the figure blocks of the handoff,
#    README.md and docs/TRUST.md (tools/doc_figures.py), from the reports as they now are.
# 3. The checks: check_bug_inventory, check_agent_runs, check_docs_conventions, bug_status --check and
#    doc_figures --check. A failure stops the preflight at once (exit 1) and names the step.
#
# Files the run itself regenerates (reports/, rendered/, and the figure blocks its last wave writes) are consistent by
# construction; the preflight covers the derived files outside them and makes the run's comparisons start from
# current files. Each item prints "preflight: <item> (<seconds> s)"; the last line is "preflight: ok (<seconds> s)".
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
tier=light
args=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --tier) tier="${2:-}"; shift; [ "$#" -gt 0 ] && shift ;;
    --tier=*) tier="${1#--tier=}"; shift ;;
    --year) args+=("$1" "${2:-}"); shift; [ "$#" -gt 0 ] && shift ;;
    --year=*) args+=("$1"); shift ;;
    *) echo "preflight: unknown argument '$1' (usage: tools/preflight.sh [--tier light|full|docs] [--year N])" >&2; exit 2 ;;
  esac
done
case "$tier" in light|full|docs) ;; *) echo "preflight: unknown tier '$tier'" >&2; exit 2 ;; esac
set -- ${args[@]+"${args[@]}"}
node=(node engine/dist/main.js)
t_start=$(date +%s)

# item NAME COMMAND...: run COMMAND, its output kept unless it fails; stop the preflight when it fails.
item() {
  local name="$1" t0 out rc=0
  shift
  t0=$(date +%s)
  out="$("$@" 2>&1)" || rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "$out" >&2
    echo "preflight: FAILED at $name (exit $rc, $(( $(date +%s) - t0 )) s); check-all not started" >&2
    exit 1
  fi
  echo "preflight: $name ($(( $(date +%s) - t0 )) s)"
}

build() { npm run -s compile && "${node[@]}" build "$@" > /dev/null; }
if python3 tools/build_fresh.py "$@" > /dev/null 2>&1; then
  echo "preflight: build current"
else
  item build build "$@"
fi
item "regenerate reports/bug_status.md" python3 tools/bug_status.py --write
item "regenerate the coverage tree" python3 tools/coverage/tree.py "$@"
item "regenerate the gate frequencies report" python3 tools/coverage/gate_frequencies.py "$@"
item "regenerate the person wording report" "${node[@]}" spouse-wording --report "$@"
compare_coverage=0
if [ "$tier" = full ]; then
  compare_coverage=1
elif [ "$tier" = light ] && [ "$(python3 tools/change_scope.py "$@")" = all ]; then
  compare_coverage=1
fi
if [ "$compare_coverage" = 1 ]; then
  item "regenerate the interview coverage report" "${node[@]}" interview-coverage --write "$@"
fi
item "regenerate the figure blocks" python3 tools/doc_figures.py
item check_bug_inventory python3 tools/check_bug_inventory.py
item check_agent_runs python3 tools/check_agent_runs.py
item check_docs_conventions python3 tools/check_docs_conventions.py
item "bug_status --check" python3 tools/bug_status.py --check
item "doc_figures --check" python3 tools/doc_figures.py --check
echo "preflight: ok ($(( $(date +%s) - t_start )) s)"
