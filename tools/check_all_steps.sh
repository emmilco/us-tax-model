#!/usr/bin/env bash
# The steps of check-all for one tax year: pass --year N to check a year other
# than the default (the newest adopted year in years.json); every year-aware step
# receives the same arguments. tools/check_all.sh runs this and guards it.
#
# Compile first: review tools and every build consumer import engine/dist. Then
# build and render, beside only the engine self-check and the Lean build: canonical/
# and rendered/ are read by the log, review and source-coverage checks. The other
# steps run in three waves; the steps of a wave run side by side, each writing its
# output to its own log, printed in the order below when the wave ends. No two steps
# of a wave write the same file, and none reads what another of its wave writes:
# wave 1 checks the sources, logs and the build's data and runs the tools' self-tests
# (tools/self_tests.py, one step per group), wave 2 runs the evaluator checks, wave 3
# writes the evidence report and review packets and runs human_review, which copies
# reports/<year>/engine_differential.json that engine_differential (wave 2) rewrites.
# Nothing checks these rules; a new step must be placed by them. A failing step fails
# the run after its wave.
#
# Wall times, in whole seconds, go to .git/check-all-times (not tracked; rewritten by each run): each step's
# as "<seconds> <step>", each self-test's as "<seconds> self_tests/<name>", each stage's (compile, build,
# wave1 to wave3) as "<seconds> stage:<label> <its steps>", and the run's as "<seconds> run:<tier>". When the
# run ends, passed or failed, tools/check_times.py prints the summary of that file: the stages, which run
# one after another, and the steps by time, each with its stage, since the steps of a stage run side by side.
#
# A check that runs for both jurisdictions is declared once, with jstep: its New York
# run is the step ny_<name>, the same command with the New York flag.
#
# --tier full|fast|docs selects the steps (default full: every step). fast skips slow_steps: the
# mutation and independent-evaluator checks a release runs, and the human-review tooling's test
# (human packets are optional; tools/full_paths.txt makes a change to that tooling need the full
# tier). evidence then marks its E column with the latest release reachable from HEAD, because the
# engine differential it reads was not rerun. docs runs docs_steps: compile, the build without
# render, and the checks that read the bookkeeping paths of tools/docs_paths.txt (tools/tier_paths.py
# lists every reader of them).
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
run_args=("$@")
slow_steps=" lean_build mutate engine_differential compare ny_compare ny_mutate human_review "
docs_steps=" compile build check_bug_inventory check_agent_runs check_docs_conventions siblings_check bookkeeping_self_tests coverage_tree "
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
run_t0=$(date +%s)
# finish: on exit, however the run ends, record the run's time and print the summary of the times.
finish() {
  echo "$(( $(date +%s) - run_t0 )) run:$tier" >> "$times"
  echo
  python3 tools/check_times.py "$times" || true
  rm -rf "$logs"
}
trap finish EXIT
names=()
pids=()
stage_t0=0

# step NAME COMMAND...: start COMMAND in the background, logging to its own file, when NAME is in the tier.
step() {
  local name="$1"; shift
  in_tier "$name" || return 0
  [ "${#pids[@]}" -gt 0 ] || stage_t0=$(date +%s)
  ( t0=$(date +%s); rc=0; "$@" > "$logs/$name.log" 2>&1 || rc=$?
    echo "$(( $(date +%s) - t0 )) $name" >> "$times"; exit "$rc" ) &
  names+=("$name"); pids+=("$!")
}

# jstep NAME NY_FLAG COMMAND...: the check NAME for both jurisdictions: step NAME runs COMMAND with the
# run's arguments, step ny_NAME runs COMMAND, then NY_FLAG (split at spaces), then the run's arguments.
jstep() {
  local name="$1" ny="$2"; shift 2
  step "$name" "$@" ${run_args[@]+"${run_args[@]}"}
  # shellcheck disable=SC2086
  step "ny_$name" "$@" $ny ${run_args[@]+"${run_args[@]}"}
}

# wave LABEL: wait for the steps started since the last wave (the stage LABEL), record the stage's wall
# time and its steps, print their logs in order, and stop the run if any failed.
wave() {
  local i failed=() label="$1" joined
  [ "${#pids[@]}" -gt 0 ] || return 0
  for i in "${!pids[@]}"; do
    wait "${pids[$i]}" || failed+=("${names[$i]}")
  done
  joined="${names[*]}"
  echo "$(( $(date +%s) - stage_t0 )) stage:$label ${joined// /,}" >> "$times"
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

lean_build() {
  cd lean && lake build taxeval
}

# The frozen Stage 2 to 5 review packets and their values sheets (reports/<year>/stage*), regenerated through
# the eval CLI so that they show the current engine's output.
review_packets() {
  "${node[@]}" review-stage2 "$@" && "${node[@]}" review-stage3 "$@" && "${node[@]}" review-stage4 "$@" &&
    "${node[@]}" review-stage5 "$@"
}

step compile npm run compile --silent
wave compile

if [ "$tier" = docs ]; then step build "${node[@]}" build "$@"; else step build build_and_render "$@"; fi
step check_self_test "${node[@]}" check-self-test
# The Lean evaluator, for compare and ny_compare.
step lean_build lean_build
wave build

# The tools' self-tests and test suites, in a worker pool; the bookkeeping group is the docs tier's.
step bookkeeping_self_tests python3 tools/self_tests.py --group bookkeeping --times "$times" "$@"
step self_tests python3 tools/self_tests.py --group code --times "$times" "$@"
# A check declared with jstep, below, also runs for New York (docs/ny/). A New York document whose first
# review is not yet run is listed in reviews/ny/<year>/pending.json and reported as pending by the log checks;
# the list only shrinks (tools/transcription/pending.py), and deleting it makes them strict.
jstep fetch_sources "--jurisdiction ny" python3 tools/fetch_sources.py
jstep check_extraction "--jurisdiction ny" python3 tools/check_extraction.py
step check_macrs_tables python3 tools/check_macrs_tables.py "$@"
step check_ptc_tables python3 tools/extract_ptc_tables.py --check "$@"
step check_auto_limits python3 tools/check_auto_limits.py "$@"
step check_source_titles python3 tools/check_source_titles.py "$@"
step check_bug_inventory python3 tools/check_bug_inventory.py
step check_agent_runs python3 tools/check_agent_runs.py
step check_docs_conventions python3 tools/check_docs_conventions.py
step siblings_check python3 tools/siblings.py --check "$@"
step adapter_contracts python3 tools/transcription/adapter_contracts.py "$@"
step classm_skipped python3 tools/transcription/audit_skipped.py "$@"
step compare_families python3 tools/transcription/compare_families.py "$@"
jstep review_store "--jurisdiction ny" python3 tools/transcription/review_store.py check
jstep check_logs "--jurisdiction ny" python3 tools/transcription/check_logs.py
step check_table_logs python3 tools/transcription/check_table_logs.py "$@"
jstep citations "--jurisdiction ny" python3 tools/citations.py --strict
# Every candidate gate situation has a share of all returns in [0, 1] and a source, and its report is current.
step gate_frequencies python3 tools/coverage/gate_frequencies.py --check "$@"
# Source-coverage checks (T-084 to T-089) read the canonical data and rendered English the build writes.
jstep instruction_cites "--jurisdiction ny" python3 tools/check_instruction_cites.py
jstep operands "--jurisdiction ny" python3 tools/check_operands.py
jstep signs "--jurisdiction ny" python3 tools/check_signs.py
jstep screen_currency "--jurisdiction ny" python3 tools/transcription/check_screens.py
jstep false_no_currency "--jurisdiction ny" python3 tools/transcription/check_false_no.py
# Lists the questions due for the question review; fails on unruled samples and orphans (no release gate yet).
jstep question_currency "--jurisdiction ny" python3 tools/transcription/check_questions.py
jstep consumers "--jurisdiction ny" python3 tools/check_consumers.py
jstep limits "--jurisdiction ny" python3 tools/check_limits.py
# Lines stated twice (Form 8863 Part III, for a person and for a dependent) agree except where reviews/<year>/twins.json says.
step twins python3 tools/check_twins.py "$@"
jstep completeness "--jurisdiction ny" python3 tools/transcription/check_completeness.py
# New York only: its tax table.
step ny_tax_table python3 tools/extract_ny_tax_table.py --check "$@"
wave wave1

step conjecture "${node[@]}" conjecture "$@"
jstep test_fixtures --ny "${node[@]}" test-fixtures
step refusal_reach "${node[0]}" tools/check_refusal_reach.mjs "$@"
# The interview rules of the formal gates design: no input set by the interview, order independence, no early completion.
step interview_rules "${node[@]}" interview-rules "$@"
step test_integration "${node[@]}" test-integration "$@"
# The web UI server (serve): synthetic returns in temporary directories, compared with the CLI and the fixtures.
step test_serve "${node[@]}" test-serve "$@"
step classm_job_seeds "${node[0]}" tools/transcription/test_classm_jobs.mjs "$@"
step coverage "${node[@]}" coverage "$@"
# Every refusal gate placed in the decision tree, and docs/COVERAGE.md and the README block current.
step coverage_tree python3 tools/coverage/tree.py --check "$@"
# The refusal properties over generated returns; the New York run evaluates every federal and New York line.
jstep properties --ny "${node[@]}" properties
step differential "${node[@]}" differential "$@"
step engine_differential tools/engines/run.sh "$@"
# New York mutants are killed only by the New York fixtures (the federal run takes federal mutants only).
jstep mutate --ny "${node[@]}" mutate
jstep compare --ny "${node[@]}" compare
wave wave2

evidence_args=()
if [ "$tier" = fast ]; then
  evidence_args=(--engine-release "$(git describe --match 'r[0-9]*' --abbrev=0 HEAD 2>/dev/null || echo none)")
fi
step evidence "${node[@]}" evidence ${evidence_args[@]+"${evidence_args[@]}"} "$@"
step review_packets review_packets "$@"
# The human-review tooling: reading, saved verdict, signed log and evidence report, in a sandbox.
step human_review python3 tools/human_review/test_review.py "$@"
wave wave3
