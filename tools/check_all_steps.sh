#!/usr/bin/env bash
# The steps of check-all for one tax year: pass --year N to check a year other
# than the default (the newest adopted year in years.json); every year-aware step
# receives the same arguments. tools/check_all.sh runs this and guards it.
#
# Compile first: review tools and every build consumer import engine/dist. Then
# build and render alone: canonical/ and rendered/ are read by the log, review and
# source-coverage checks. The other steps run in three waves; the steps of a wave
# run side by side, each writing its output to its own log, printed in the order
# below when the wave ends. No two steps of a wave write the same file, and none
# reads what another of its wave writes: wave 1 checks the sources, logs and the
# build's data, wave 2 runs the evaluator checks, wave 3 writes the evidence report
# and review packets. A failing step fails the run after its wave. Each step's wall time, in seconds,
# goes to .git/check-all-times (not tracked).
#
# --tier full|fast|docs selects the steps (default full: every step). fast skips slow_steps, the
# mutation and independent-evaluator checks a release runs; evidence then marks its E column with the
# latest release reachable from HEAD, because the engine differential it reads was not rerun. docs
# runs docs_steps: compile, the build without render, and the checks that read the bookkeeping paths
# of tools/docs_paths.txt (tools/tier_paths.py lists every reader of them).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
tier=full
args=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --tier) tier="${2:-}"; shift; [ "$#" -gt 0 ] && shift ;;
    --tier=*) tier="${1#--tier=}"; shift ;;
    *) args+=("$1"); shift ;;
  esac
done
set -- ${args[@]+"${args[@]}"}
slow_steps=" mutate engine_differential compare ny_compare ny_mutate "
docs_steps=" compile build check_bug_inventory siblings_check siblings_self_test bookkeeping_tools coverage_tree green_self_test "
case "$tier" in
  full|fast|docs) ;;
  *) echo "check-all: unknown tier '$tier' (full, fast or docs)" >&2; exit 2 ;;
esac
in_tier() {
  case "$tier" in
    full) return 0 ;;
    fast) [[ "$slow_steps" != *" $1 "* ]] ;;
    docs) [[ "$docs_steps" == *" $1 "* ]] ;;
  esac
}
node=(node engine/dist/main.js)
times="$(git rev-parse --git-path check-all-times)"
: > "$times"
logs="$(mktemp -d)"
trap 'rm -rf "$logs"' EXIT
names=()
pids=()

# step NAME COMMAND...: start COMMAND in the background, logging to its own file, when NAME is in the tier.
step() {
  local name="$1"; shift
  in_tier "$name" || return 0
  ( t0=$(date +%s); rc=0; "$@" > "$logs/$name.log" 2>&1 || rc=$?
    echo "$(( $(date +%s) - t0 )) $name" >> "$times"; exit "$rc" ) &
  names+=("$name"); pids+=("$!")
}

# wave: wait for the steps started since the last wave, print their logs in order,
# and stop the run if any failed.
wave() {
  local i failed=()
  [ "${#pids[@]}" -gt 0 ] || return 0
  for i in "${!pids[@]}"; do
    wait "${pids[$i]}" || failed+=("${names[$i]}")
  done
  for i in "${!names[@]}"; do
    echo "== ${names[$i]}"
    cat "$logs/${names[$i]}.log"
  done
  names=(); pids=()
  if [ "${#failed[@]}" -gt 0 ]; then
    echo "check-all: failed: ${failed[*]}" >&2
    exit 1
  fi
}

# Chained with && because set -e does not apply inside a command whose status is tested. The build
# writes both jurisdictions' canonical data; the New York documents render to rendered/ny/<year>/.
build_and_render() {
  "${node[@]}" build "$@" && "${node[@]}" render "$@" && "${node[@]}" render --ny "$@"
}

lean_compare() {
  (cd lean && lake build taxeval >/dev/null 2>&1) && "${node[@]}" compare "$@"
}

step compile npm run compile --silent
wave

if [ "$tier" = docs ]; then step build "${node[@]}" build "$@"; else step build build_and_render "$@"; fi
step check_self_test "${node[@]}" check-self-test
wave

step fetch_sources python3 tools/fetch_sources.py "$@"
step fetch_sources_self_test python3 tools/fetch_sources.py --self-test
step archive_text_self_test python3 tools/archive_text.py --self-test
step check_extraction python3 tools/check_extraction.py "$@"
step check_extraction_self_test python3 tools/check_extraction.py --self-test
step check_macrs_tables python3 tools/check_macrs_tables.py "$@"
step check_macrs_tables_self_test python3 tools/check_macrs_tables.py --self-test "$@"
step check_ptc_tables python3 tools/extract_ptc_tables.py --check "$@"
step check_auto_limits python3 tools/check_auto_limits.py "$@"
step check_auto_limits_self_test python3 tools/check_auto_limits.py --self-test "$@"
step check_bug_inventory python3 tools/check_bug_inventory.py
step review_tools python3 tools/transcription/test_review_tools.py
step input_context python3 tools/transcription/test_input_context.py
step rerun_all_tools python3 tools/transcription/test_rerun_all.py
step bookkeeping_tools python3 -m unittest tools/test_bookkeeping_tools.py
step pre_push_self_test bash tools/hooks/test_pre_push.sh
step green_self_test bash tools/hooks/test_green.sh
step consistency_checks node tools/test_consistency_checks.mjs
step siblings_self_test python3 tools/siblings.py --self-test
step siblings_check python3 tools/siblings.py --check "$@"
step adapter_contracts python3 tools/transcription/adapter_contracts.py "$@"
step classm_skipped python3 tools/transcription/audit_skipped.py "$@"
step compare_families python3 tools/transcription/compare_families.py "$@"
step check_logs python3 tools/transcription/check_logs.py "$@"
step check_table_logs python3 tools/transcription/check_table_logs.py "$@"
step citations python3 tools/citations.py --strict "$@"
step citations_self_test python3 tools/citations.py --self-test "$@"
step year_diff_self_test python3 tools/year_diff.py --self-test "$@"
step fixtures_year_self_test python3 tools/fixtures_year.py --self-test
step engine_compare_tests python3 -I tools/engines/test_compare.py
step coverage_tree_self_test python3 tools/coverage/tree.py --self-test "$@"
# Source-coverage checks (T-084 to T-089) read the canonical data and rendered English the build writes.
step instruction_cites python3 tools/check_instruction_cites.py "$@"
step instruction_cites_self_test python3 tools/check_instruction_cites.py --self-test "$@"
step operands python3 tools/check_operands.py "$@"
step operands_self_test python3 tools/check_operands.py --self-test "$@"
step signs python3 tools/check_signs.py "$@"
step signs_self_test python3 tools/check_signs.py --self-test "$@"
step screen_currency python3 tools/transcription/check_screens.py "$@"
step consumers python3 tools/check_consumers.py "$@"
step consumers_self_test python3 tools/check_consumers.py --self-test "$@"
step limits python3 tools/check_limits.py "$@"
step limits_self_test python3 tools/check_limits.py --self-test "$@"
step completeness python3 tools/transcription/check_completeness.py "$@"
step completeness_self_test python3 tools/transcription/check_completeness.py --self-test "$@"
# New York (docs/ny/): its sources, citations and source-coverage checks, its tax table and predictor, and
# its review logs. A New York document whose first review is not yet run is listed in
# reviews/ny/<year>/pending.json and reported as pending by the log checks; the list only shrinks
# (tools/transcription/pending.py), and deleting it makes them strict.
step ny_fetch_sources python3 tools/fetch_sources.py --jurisdiction ny "$@"
step ny_check_extraction python3 tools/check_extraction.py --jurisdiction ny "$@"
step ny_citations python3 tools/citations.py --strict --jurisdiction ny "$@"
step ny_instruction_cites python3 tools/check_instruction_cites.py --jurisdiction ny "$@"
step ny_operands python3 tools/check_operands.py --jurisdiction ny "$@"
step ny_signs python3 tools/check_signs.py --jurisdiction ny "$@"
step ny_consumers python3 tools/check_consumers.py --jurisdiction ny "$@"
step ny_limits python3 tools/check_limits.py --jurisdiction ny "$@"
step ny_tax_table python3 tools/extract_ny_tax_table.py --check "$@"
step ny_predict_self_test python3 tools/ny_predict.py --self-test
step ny_review_tools python3 tools/transcription/test_ny_review.py
step ny_check_logs python3 tools/transcription/check_logs.py --jurisdiction ny "$@"
step ny_completeness python3 tools/transcription/check_completeness.py --jurisdiction ny "$@"
step ny_screen_currency python3 tools/transcription/check_screens.py --jurisdiction ny "$@"
wave

step conjecture "${node[@]}" conjecture "$@"
step test_fixtures "${node[@]}" test-fixtures "$@"
step refusal_reach "${node[0]}" tools/check_refusal_reach.mjs "$@"
step test_integration "${node[@]}" test-integration "$@"
# The web UI server (serve): synthetic returns in temporary directories, compared with the CLI and the fixtures.
step test_serve "${node[@]}" test-serve "$@"
step human_review python3 tools/human_review/test_review.py "$@"
step classm_job_seeds "${node[0]}" tools/transcription/test_classm_jobs.mjs "$@"
step coverage "${node[@]}" coverage "$@"
# Every refusal gate placed in the decision tree, and docs/COVERAGE.md and the README block current.
step coverage_tree python3 tools/coverage/tree.py --check "$@"
step properties "${node[@]}" properties "$@"
step differential "${node[@]}" differential "$@"
step engine_differential tools/engines/run.sh "$@"
step mutate "${node[@]}" mutate "$@"
step compare lean_compare "$@"
step ny_test_fixtures "${node[@]}" test-fixtures --ny "$@"
# The refusal properties over generated returns with New York answers, every federal and New York line evaluated.
step ny_properties "${node[@]}" properties --ny "$@"
wave

evidence_args=()
if [ "$tier" = fast ]; then
  evidence_args=(--engine-release "$(git describe --match 'r[0-9]*' --abbrev=0 HEAD 2>/dev/null || echo none)")
fi
step evidence "${node[@]}" evidence ${evidence_args[@]+"${evidence_args[@]}"} "$@"
step review_stage2 "${node[@]}" review-stage2 "$@"
step review_stage3 "${node[@]}" review-stage3 "$@"
step review_stage4 "${node[@]}" review-stage4 "$@"
step review_stage5 "${node[@]}" review-stage5 "$@"
# After the compare wave, which builds the Lean evaluator.
step ny_compare "${node[@]}" compare --ny "$@"
# New York mutants, killed only by the New York fixtures (the federal run takes federal mutants only).
step ny_mutate "${node[@]}" mutate --ny "$@"
wave
