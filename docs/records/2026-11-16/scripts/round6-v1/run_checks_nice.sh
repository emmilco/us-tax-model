#!/bin/bash
# Lane V1: build, then the post-build checks, one engine process at a time, in the v1 worktree.
# Usage: run_checks.sh <outdir>
cd /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/v1 || exit 1
O="$1"; mkdir -p "$O"; : > "$O/exits.txt"
N="nice -n 15 node engine/dist/main.js"
nice -n 15 npm run build > "$O/build.txt" 2>&1; echo "build exit=$?" >> "$O/exits.txt"
$N test-fixtures > "$O/test_fixtures.txt" 2>&1; echo "test_fixtures exit=$?" >> "$O/exits.txt"
$N test-fixtures --ny > "$O/test_fixtures_ny.txt" 2>&1; echo "test_fixtures_ny exit=$?" >> "$O/exits.txt"
$N interview-coverage > "$O/interview_coverage.txt" 2>&1; echo "interview_coverage exit=$?" >> "$O/exits.txt"
$N interview-coverage --ny > "$O/interview_coverage_ny.txt" 2>&1; echo "interview_coverage_ny exit=$?" >> "$O/exits.txt"
$N interview-rules > "$O/interview_rules.txt" 2>&1; echo "interview_rules exit=$?" >> "$O/exits.txt"
$N tick-groups > "$O/tick_groups.txt" 2>&1; echo "tick_groups exit=$?" >> "$O/exits.txt"
$N draft-walk --summary --out "$O/walk" > "$O/walk.txt" 2>&1; echo "walk exit=$?" >> "$O/exits.txt"
$N draft-walk --summary --ny --out "$O/walk-ny" > "$O/walk_ny.txt" 2>&1; echo "walk_ny exit=$?" >> "$O/exits.txt"
echo ALLDONE >> "$O/exits.txt"
