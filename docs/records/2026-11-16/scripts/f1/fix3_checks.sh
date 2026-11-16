#!/bin/bash
# Lane F1b: the post-build checks, run one at a time in the f1 worktree.
cd /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/f1 || exit 1
O=/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/nightplan-2026-11-16/f1/fix3
N="node engine/dist/main.js"
$N test-fixtures > $O/test_fixtures.txt 2>&1; echo "test_fixtures exit=$?" >> $O/exits.txt
$N test-fixtures --ny > $O/test_fixtures___ny.txt 2>&1; echo "test_fixtures_ny exit=$?" >> $O/exits.txt
$N interview-coverage > $O/interview_coverage.txt 2>&1; echo "interview_coverage exit=$?" >> $O/exits.txt
$N interview-coverage --ny > $O/interview_coverage_ny.txt 2>&1; echo "interview_coverage_ny exit=$?" >> $O/exits.txt
$N interview-rules > $O/interview_rules.txt 2>&1; echo "interview_rules exit=$?" >> $O/exits.txt
$N tick-groups > $O/tick_groups.txt 2>&1; echo "tick_groups exit=$?" >> $O/exits.txt
$N draft-walk --summary --out $O/walk > $O/walk.txt 2>&1; echo "walk exit=$?" >> $O/exits.txt
$N draft-walk --summary --ny --out $O/walk-ny > $O/walk_ny.txt 2>&1; echo "walk_ny exit=$?" >> $O/exits.txt
echo ALLDONE >> $O/exits.txt
