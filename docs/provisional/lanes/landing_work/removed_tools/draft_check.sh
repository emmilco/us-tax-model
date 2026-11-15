#!/bin/bash
# The deterministic bar of the provisional interview redraft (docs/provisional/NORMS.md, section 5): the build and the
# checks that make no paid call and read no review data. Run from the root of a worktree of the provisional clone.
# Usage: tools/draft_check.sh [--quick]   (--quick: build, fixtures, interview-rules, coverage rows and the tick-box groups only)
set -u
cd "$(dirname "$0")/.." || exit 2
out="${TMPDIR:-/tmp}/draft-check-$(basename "$PWD")-$$"
mkdir -p "$out"
fail=0
run() {
  local name="$1"; shift
  local t0; t0=$(date +%s)
  if "$@" > "$out/$name.log" 2>&1; then
    echo "ok    $name ($(( $(date +%s) - t0 ))s): $(tail -1 "$out/$name.log" | cut -c1-140)"
  else
    echo "FAIL  $name ($(( $(date +%s) - t0 ))s): see $out/$name.log"; tail -15 "$out/$name.log" | cut -c1-300
    fail=1
  fi
}
run build npm run build --silent
[ "$fail" = 0 ] || { echo "draft-check: build failed"; exit 1; }
node=(node engine/dist/main.js)
run test_fixtures "${node[@]}" test-fixtures
run interview_rules "${node[@]}" interview-rules
"${node[@]}" interview-coverage --write > "$out/coverage_write.log" 2>&1
run interview_coverage "${node[@]}" interview-coverage
run tick_groups "${node[@]}" tick-groups
if [ "${1:-}" != "--quick" ]; then
  "${node[@]}" spouse-wording --report > "$out/person_wording_write.log" 2>&1
  run person_wording "${node[@]}" spouse-wording --report --check
  run spouse_self_test "${node[@]}" spouse-wording --self-test
  run check_self_test "${node[@]}" check-self-test
  run test_integration "${node[@]}" test-integration
  run properties "${node[@]}" properties
  run test_serve "${node[@]}" test-serve
  run draft_walk_self_test "${node[@]}" draft-walk --self-test
  run order_self_test "${node[@]}" interview-order --self-test
  run tick_groups_self_test "${node[@]}" tick-groups --self-test
  run twins python3 tools/check_twins.py
  run render_check "${node[@]}" render --check
fi
if [ "$fail" = 0 ]; then echo "draft-check: green ($(git rev-parse --short HEAD), tree $(git write-tree 2>/dev/null | cut -c1-12))"; else echo "draft-check: RED"; fi
exit "$fail"
