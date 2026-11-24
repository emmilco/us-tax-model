#!/usr/bin/env bash
# The steps of check-all for one tax year: pass --year N to check a year other
# than the default (the newest adopted year in years.json); every year-aware step
# receives the same arguments. A last stage builds and runs the fixtures of every
# other adopted year (below). tools/check_all.sh runs this and guards it.
#
# Compile first: review tools and every build consumer import engine/dist. Then
# build and render, beside only the engine self-check and the Lean build: canonical/
# and rendered/ are read by the log, review and source-coverage checks. The other
# steps run in four waves; the steps of a wave run side by side, each writing its
# output to its own log, printed in the order below when the wave ends. No two steps
# of a wave write the same file, and none reads what another of its wave writes:
# wave 1 checks the sources, logs and the build's data and runs the tools' self-tests
# (tools/self_tests.py, one step per group), wave 2 runs the evaluator checks, wave 3
# writes the evidence report, which reads reports/<year>/engine_differential.json that
# engine_differential (wave 2) rewrites, and the stage review packets, and wave 4 checks
# the figures the entry documents quote from the reports the earlier waves write.
# Nothing checks these rules; a new step must be placed by them. A failing step fails
# the run after its wave. So does a step that exits 0 without a line tools/step_output.py
# requires of it: the line of each self-test the step runs inside itself, which would
# otherwise go unnoticed if its call were removed.
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
# New York publishes after the IRS, so a year may be adopted federally before New York has adopted it
# (years.json, ny_adopted; tools/jurisdiction.py --ny-status). For such a year every step named ny_* is
# skipped: it is listed in its wave as "== ny_<name>" with the reason, and the run says how many it skipped
# at its start and its end. The New York render runs when the year has New York definitions (forms/ny/<year>/).
#
# --tier light|full|docs selects the steps (default light, the tier a commit on `next` or a lane branch needs).
# light runs light_steps: compile, build and render, the federal and New York fixtures, the bookkeeping checks, the
# checks of generated reports, the year-label lint, four checks of seconds that otherwise fail only at a release
# (hermetic_env, twins, refusal_reach, engine_cases), the static guards (the next year's operations still apply, no
# renamed id left, the keyed mutation arguments hold on the build, every parameter read), and the interview checks of
# scoped_steps scoped to the forms the change touches
# (tools/change_scope.py: `--forms <ids>`; no step when no form is touched; when the change can reach any walk,
# interview_coverage, tick_groups and spouse_phrase run unscoped and interview_rules, whose unscoped run is the release's, not at all). full is the release's tier: every step, the interview checks unscoped, except release_steps (the interview
# length report and the release checks of the sampled reviews), which run only in release mode
# (CHECK_ALL_RELEASE=1, as tools/release.sh runs it). engine_differential reuses an outside engine's stored record
# while everything that determines it is unchanged (tools/engines/engine_cache.py; ENGINE_CACHE=verify reruns every
# engine and compares, as tools/release.sh does). docs runs docs_steps: compile, the build without render, and the
# checks that read the bookkeeping paths of tools/docs_paths.txt (tools/tier_paths.py lists every reader of them).
#
# --print-steps lists the tier's steps instead of running them, in the order declared, one per line: the step's
# name, a tab, and its command quoted for eval (printf %q; a command that is a function of this script, such as
# build_and_render, is printed by its name). For a New York step the year skips, the line is its name,
# "skip" and the reason, tab-separated. Nothing is run and no times file is written (a printed command's times
# file is /dev/null). tools/release_prep.sh runs its steps from this list, so a step's command is declared here only.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
tier=light
print_steps=0
args=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --print-steps) print_steps=1; shift ;;
    --tier) tier="${2:-}"; shift; [ "$#" -gt 0 ] && shift ;;
    --tier=*) tier="${1#--tier=}"; shift ;;
    *) args+=("$1"); shift ;;
  esac
done
set -- ${args[@]+"${args[@]}"}
run_args=("$@")
year="$(python3 -I -c 'import sys; sys.path.insert(0, "tools"); import taxyear; print(taxyear.Y)' "$@")"
# ny_skip: empty when New York has adopted the year; otherwise why its steps are skipped.
ny_skip=""
ny_rc=0
ny_status="$(python3 tools/jurisdiction.py --ny-status "$@")" || ny_rc=$?
case "$ny_rc" in
  0) ;;
  3) ny_skip="$ny_status" ;;
  *) echo "check-all: tools/jurisdiction.py --ny-status failed" >&2; exit 2 ;;
esac
light_steps=" compile build check_self_test bookkeeping_self_tests hermetic_env twins refusal_reach engine_cases check_bug_inventory bug_status check_agent_runs check_docs_conventions siblings_check gate_frequencies person_wording label_year coverage_tree doc_figures test_fixtures ny_test_fixtures interview_rules interview_coverage tick_groups spouse_phrase year_changes ny_year_changes renamed_ids ny_renamed_ids mutate_arguments ny_mutate_arguments unread_params "
docs_steps=" compile build check_bug_inventory bug_status check_agent_runs check_docs_conventions siblings_check bookkeeping_self_tests coverage_tree doc_figures "
scoped_steps=" interview_rules interview_coverage tick_groups spouse_phrase "
release_unscoped=" interview_rules "
case "$tier" in
  full|light|docs) ;;
  *) echo "check-all: unknown tier '$tier' (light, full or docs)" >&2; exit 2 ;;
esac
release_steps=" interview_length release_completeness ny_release_completeness release_screens ny_release_screens release_false_no ny_release_false_no "
in_tier() {
  if [[ "$release_steps" == *" $1 "* ]] && [ "${CHECK_ALL_RELEASE:-}" != 1 ]; then return 1; fi
  case "$tier" in
    full) return 0 ;;
    light) [[ "$light_steps" == *" $1 "* ]] || [[ "$1" == y[0-9]*_build || "$1" == y[0-9]*_test_fixtures || "$1" == y[0-9]*_ny_test_fixtures ]] ;;
    docs) [[ "$docs_steps" == *" $1 "* ]] ;;
  esac
}
# scope: in the light tier, what the change touches (tools/change_scope.py): all, none, or a list of form ids.
scope=all
if [ "$tier" = light ]; then
  scope="$(python3 tools/change_scope.py "$@")" || { echo "check-all: tools/change_scope.py failed" >&2; exit 2; }
  [ "$print_steps" = 1 ] || echo "check-all: light tier; the interview checks' scope: $scope"
fi
# scope_skip NAME: print why the light tier skips the scoped step NAME (status 0), or nothing (status 1).
scope_skip() {
  [ "$tier" = light ] && [[ "$scoped_steps" == *" $1 "* ]] || return 1
  if [ "$scope" = none ]; then echo "the change touches no form the interview reads (tools/change_scope.py)"; return 0; fi
  if [ "$scope" = all ] && [[ "$release_unscoped" == *" $1 "* ]]; then
    echo "the change can reach any walk (tools/change_scope.py: all); the unscoped run is the release's"; return 0
  fi
  return 1
}
node=(node engine/dist/main.js)
times="$(git rev-parse --git-path check-all-times)"
run_t0=$(date +%s)
# finish: on exit, however the run ends, record the run's time and print the summary of the times.
finish() {
  echo "$(( $(date +%s) - run_t0 )) run:$tier" >> "$times"
  echo
  python3 tools/check_times.py "$times" || true
  rm -rf "$logs"
}
if [ "$print_steps" = 0 ]; then
  : > "$times"
  logs="$(mktemp -d)"
  trap finish EXIT
else
  times=/dev/null  # the printed commands that take a times file (self_tests.py --times) write nowhere
fi
names=()
pids=()
skipped=()
stage_t0=0

# step NAME COMMAND...: start COMMAND in the background, logging to its own file, when NAME is in the tier.
# A New York step (ny_*) for a year New York has not adopted is not started: its log is the reason, and its
# wave lists it with an empty pid, as skipped.
step() {
  local name="$1"; shift
  in_tier "$name" || return 0
  [ "${#pids[@]}" -gt 0 ] || stage_t0=$(date +%s)
  if [ -n "$ny_skip" ] && [[ "$name" == ny_* ]]; then
    echo "skipped: $ny_skip" > "$logs/$name.log"
    names+=("$name"); pids+=(""); skipped+=("$name")
    return 0
  fi
  local why
  if why="$(scope_skip "$name")"; then
    echo "skipped: $why" > "$logs/$name.log"
    names+=("$name"); pids+=("")
    return 0
  fi
  if [[ "$scoped_steps" == *" $name "* ]] && [ "$scope" != all ]; then set -- "$@" --forms "$scope"; fi
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
# time and its steps, fail each step that passed without a line required of it (tools/step_output.py writes
# what is missing to the step's log), print the logs in order, and stop the run if any step failed.
wave() {
  local i failed=() passed=() label="$1" joined lacking
  [ "${#pids[@]}" -gt 0 ] || return 0
  for i in "${!pids[@]}"; do
    [ -n "${pids[$i]}" ] || continue
    if wait "${pids[$i]}"; then passed+=("${names[$i]}"); else failed+=("${names[$i]}"); fi
  done
  joined="${names[*]}"
  echo "$(( $(date +%s) - stage_t0 )) stage:$label ${joined// /,}" >> "$times"
  if lacking="$(python3 tools/step_output.py --logs "$logs" ${passed[@]+"${passed[@]}"})"; then
    # shellcheck disable=SC2206
    failed+=($lacking)
  else
    echo "check-all: tools/step_output.py did not run; the steps' required lines are unchecked" >&2
    failed+=(step_output)
  fi
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
  "${node[@]}" build "$@" && "${node[@]}" render "$@" || return 1
  if [ -d "forms/ny/$year" ]; then
    "${node[@]}" render --ny "$@"
  else
    echo "render --ny skipped: no forms/ny/$year/"
  fi
}

lean_build() {
  (cd lean && lake build taxeval)
}

# The frozen Stage 2 to 5 review packets and their values sheets (reports/<year>/stage*), regenerated through
# the eval CLI so that they show the current engine's output.
review_packets() {
  "${node[@]}" review-stage2 "$@" && "${node[@]}" review-stage3 "$@" && "${node[@]}" review-stage4 "$@" &&
    "${node[@]}" review-stage5 "$@"
}

if [ "$print_steps" = 1 ]; then
  # --print-steps: step() prints the line of its command instead of starting it; wave() waits for nothing.
  step() {
    local name="$1"; shift
    in_tier "$name" || return 0
    if [ -n "$ny_skip" ] && [[ "$name" == ny_* ]]; then
      printf '%s\tskip\t%s\n' "$name" "$ny_skip"
      return 0
    fi
    local why
    if why="$(scope_skip "$name")"; then
      printf '%s\tskip\t%s\n' "$name" "$why"
      return 0
    fi
    if [[ "$scoped_steps" == *" $name "* ]] && [ "$scope" != all ]; then set -- "$@" --forms "$scope"; fi
    printf '%s\t' "$name"
    printf ' %q' "$@"
    printf '\n'
  }
  wave() { :; }
elif [ -n "$ny_skip" ]; then
  echo "check-all: New York steps skipped for $year: $ny_skip"
fi
step compile npm run compile --silent
wave compile

if [ "$tier" = docs ]; then step build "${node[@]}" build "$@"; else step build build_and_render "$@"; fi
step check_self_test "${node[@]}" check-self-test "$@"
# The Lean evaluator, for compare and ny_compare.
step lean_build lean_build
wave build

# The tools' self-tests and test suites, in a worker pool; the bookkeeping group is the docs tier's.
step bookkeeping_self_tests python3 tools/self_tests.py --group bookkeeping --times "$times" "$@"
step self_tests python3 tools/self_tests.py --group code --times "$times" "$@"
# Every variable the tools read from the environment is classified, and the self-test runners drop the run settings
# (tools/hermetic_env.py), so that a self-test behaves inside a run as alone.
step hermetic_env python3 tools/hermetic_env.py --self-test
# A check declared with jstep, below, also runs for New York (docs/ny/). A New York document whose first
# review is not yet run is listed in reviews/ny/<year>/pending.json and reported as pending by the log checks;
# the list only shrinks (tools/transcription/pending.py), and deleting it makes them strict.
jstep fetch_sources "--jurisdiction ny" python3 tools/fetch_sources.py
jstep check_extraction "--jurisdiction ny" python3 tools/check_extraction.py
step check_macrs_tables python3 tools/check_macrs_tables.py "$@"
step check_ptc_tables python3 tools/extract_ptc_tables.py --check "$@"
step check_realty_tables python3 tools/extract_realty_tables.py --check "$@"
step check_auto_limits python3 tools/check_auto_limits.py "$@"
step check_printed_tables python3 tools/extract_printed_tables.py --check "$@"
step check_layouts python3 tools/layouts.py --check "$@"
step check_source_titles python3 tools/check_source_titles.py "$@"
step check_bug_inventory python3 tools/check_bug_inventory.py
# Each bug entry's status, derived from the inventory, its closure entries and the task registers; the report current.
step bug_status python3 tools/bug_status.py --check
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
# The engine differential's generator against the build: a sample of each kind of return evaluates, with a value.
step engine_cases python3 -I tools/engines/generate_cases.py --check-project "$@"
jstep completeness "--jurisdiction ny" python3 tools/transcription/check_completeness.py
# The release gate of the sampled reviews, the checks of tools/release_reviews.sh (release mode only).
# A ruling that confirms an open bug of medium or high severity fails them unless the release allows it
# (tools/release.sh --allow-open-bugs sets CHECK_ALL_ALLOW_OPEN_BUGS=1).
open_bugs=()
[ "${CHECK_ALL_ALLOW_OPEN_BUGS:-}" = 1 ] && open_bugs=(--allow-open-bugs)
jstep release_completeness "--jurisdiction ny" python3 tools/transcription/check_completeness.py --release ${open_bugs[@]+"${open_bugs[@]}"}
jstep release_screens "--jurisdiction ny" python3 tools/transcription/check_screens.py --release ${open_bugs[@]+"${open_bugs[@]}"}
jstep release_false_no "--jurisdiction ny" python3 tools/transcription/check_false_no.py --release ${open_bugs[@]+"${open_bugs[@]}"}
# No id of either jurisdiction's build carries a year, but for the ids listed in tools/year_ids.json (spec 4.3).
step year_ids python3 tools/check_year_ids.py "$@"
# No old id of tools/year_free_names.json is left in the fixtures (defaults included), coverage rows, personas or the
# triage witnesses of the rulings, in any form, the collection-indexed `doc[entry].name` included, nor, in the federal
# run, as a bare quoted name beside its document in the code (tools/rename_ids.py).
jstep renamed_ids "--jurisdiction ny" python3 tools/rename_ids.py check
# The prepared operations of the next tax year (changes/<year+1>/) still apply to this year's forms, question bank and
# profiles: no line gone or renamed, no expected text changed, no collision, reference or gate broken, evidence printed.
jstep year_changes "--jurisdiction ny" python3 tools/year_changes.py --check
# The keyed equivalence arguments of engine/src/mutate.ts on this build, without a mutation run: each one's mutant still
# generated, reading the line it names, and the argument holding; those of tools/mutation_arguments_open.json known.
jstep mutate_arguments --ny "${node[@]}" mutate-arguments
# Every parameter of both jurisdictions read by a form, interview, change file or code (tools/unread_params_allow.json:
# the names code builds).
step unread_params python3 tools/check_unread_params.py "$@"
# A label or question that prints a dollar parameter's amount which changes next year is rewritten by an operation of
# changes/<year+1>/ or held, with its reason, in tools/label_year_baseline.json.
step label_year python3 tools/check_label_year.py "$@"
# New York only: its tax tables and household credit tables, each the same as a fresh extraction.
step ny_tax_table python3 tools/extract_ny_tax_table.py --check "$@"
step ny_household_tables python3 tools/extract_ny_household_tables.py --check "$@"
wave wave1

step conjecture "${node[@]}" conjecture "$@"
jstep test_fixtures --ny "${node[@]}" test-fixtures
step refusal_reach "${node[0]}" tools/check_refusal_reach.mjs "$@"
# The interview rules of the formal gates design: no input set by the interview, order independence, no early completion.
step interview_rules "${node[@]}" interview-rules "$@"
# The tick-box groups of the question bank: each group's declaration, and what a ticked or unticked member opens in
# the built interview, as tick-groups.ts asks them.
step tick_groups "${node[@]}" tick-groups "$@"
# The questions asked of a person, as stored and as shown for each entry: the tracked report is what the built questions give.
step person_wording "${node[@]}" spouse-wording --report --check "$@"
# A question asked once per return whose prompt says "you" names the spouse, or is held, with its reason, in
# tools/spouse_phrase_baseline.json (interview/README.md, "A joint return combines both spouses' items").
step spouse_phrase "${node[@]}" spouse-phrase "$@"
# reports/<year>/interview_length.md, rewritten above its hand-written findings (full tier only); interview_rules,
# above, fails when reports/<year>/interview_pruning.md is not what it finds. interview_length and interview_coverage
# each spread their walks over INTERVIEW_WORKERS worker threads (default defaultWorkers() of engine/src/pool.ts,
# sized to CHECK_ALL_MAX_RUNS as the other pools are); the output is the same for every count, and
# INTERVIEW_WORKERS=1 runs each on one thread.
step interview_length "${node[@]}" interview-length --write "$@"
# The coverage rows (interview/<year>/coverage/): each situation walked through the built interview ends where its row
# says, and reports/<year>/interview_coverage.md is what the rows produce.
step interview_coverage "${node[@]}" interview-coverage "$@"
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
if [ "$tier" = light ]; then
  evidence_args=(--engine-release "$(git describe --match 'r[0-9]*' --abbrev=0 HEAD 2>/dev/null || echo none)")
fi
step evidence "${node[@]}" evidence ${evidence_args[@]+"${evidence_args[@]}"} "$@"
step review_packets review_packets "$@"
wave wave3
# The generated figures of the handoff, README.md and docs/TRUST.md (tools/doc_figures.py), after the waves that
# rewrite the reports they quote: written from the reports this run wrote, then checked.
step doc_figures sh -c 'python3 tools/doc_figures.py && python3 tools/doc_figures.py --check'
wave wave4

# Every other adopted tax year (years.json `adopted`, the run's year left out). The engine, the Lean evaluator and the
# tools are shared by every year, so a change to them must not break a year this run does not check: each other year
# is built with this run's engine and its fixtures evaluated, federally and, where New York has adopted that year,
# for New York; the full tier also compares each with the Lean evaluator. A change confined to one year's directories
# (forms/<year>/, params/, tables/, fixtures/, interview/, reviews/) needs only that year's run (--year); the steps
# here are the shared code's. Steps are named y<year>_<check>; each writes only canonical/<year>/ and its reports.
other_years="$(python3 -I -c 'import json, sys; print(" ".join(str(y) for y in sorted(json.load(open("years.json"))["adopted"]) if str(y) != sys.argv[1]))' "$year")"
for y in $other_years; do
  step "y${y}_build" "${node[@]}" build --year "$y"
done
wave other_years_build
for y in $other_years; do
  step "y${y}_test_fixtures" "${node[@]}" test-fixtures --year "$y"
  step "y${y}_compare" "${node[@]}" compare --year "$y"
  if python3 tools/jurisdiction.py --ny-status --year "$y" > /dev/null; then
    step "y${y}_ny_test_fixtures" "${node[@]}" test-fixtures --ny --year "$y"
    step "y${y}_ny_compare" "${node[@]}" compare --ny --year "$y"
  fi
done
wave other_years
if [ "$print_steps" = 0 ] && [ "${#skipped[@]}" -gt 0 ]; then
  echo "check-all: ${#skipped[@]} New York steps skipped for $year (${skipped[*]}): $ny_skip"
fi
