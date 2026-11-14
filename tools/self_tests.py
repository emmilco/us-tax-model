#!/usr/bin/env python3
"""Run the tools' self-tests and test suites, side by side in a worker pool: one check-all step per group.

    self_tests.py --group bookkeeping|code [--times FILE] [--year N]
    self_tests.py --list [--group bookkeeping|code]

Every test runs from the repository root, its output captured and printed under its name in the order of
TESTS once all have finished; the run fails, naming each failing test, if any test exits non-zero. A test
marked year-aware receives the run's year arguments (--year N). The bookkeeping group holds the tests of
the tools that read the bookkeeping paths, which the docs tier runs (tools/tier_paths.py); the code group
holds the rest. --times FILE appends "<seconds> self_tests/<name>" per test, the format of
check-all's per-step times. Workers: SELF_TEST_WORKERS, or the core count less two shared among
CHECK_ALL_MAX_RUNS runs (default 2), as engine/src/pool.ts sizes its pools.
"""
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODE = ["node", "engine/dist/main.js"]

# (name, group, year-aware, command). The slowest first, so the pool's longest test starts at once.
TESTS = [
    ("review_tools", "code", False, ["python3", "tools/transcription/test_review_tools.py"]),
    ("rerun_all_tools", "code", False, ["python3", "tools/transcription/test_rerun_all.py"]),
    ("input_context", "code", False, ["python3", "tools/transcription/test_input_context.py"]),
    ("ny_review_tools", "code", False, ["python3", "tools/transcription/test_ny_review.py"]),
    ("check_bg_self_test", "code", False, ["bash", "tools/hooks/test_check_bg.sh"]),
    ("pre_push_self_test", "code", False, ["bash", "tools/hooks/test_pre_push.sh"]),
    ("interview_rules_self_test", "code", True, NODE + ["interview-rules", "--self-test"]),
    ("interview_length_self_test", "code", True, NODE + ["interview-length", "--self-test"]),
    ("interview_words_self_test", "code", True, NODE + ["interview-words", "--self-test"]),
    ("vetting_self_test", "code", True, NODE + ["vetting-report", "--self-test"]),
    ("interview_coverage_self_test", "code", True, NODE + ["interview-coverage", "--self-test"]),
    ("spouse_wording_self_test", "code", True, NODE + ["spouse-wording", "--self-test"]),
    ("compare_corpus_self_test", "code", True, NODE + ["compare", "--corpus-self-test"]),
    ("consistency_checks", "code", False, ["node", "tools/test_consistency_checks.mjs"]),
    ("defaults_guard_self_test", "code", False, ["node", "tools/defaults_guard.mjs", "--self-test"]),
    ("engine_compare_tests", "code", False, ["python3", "-I", "tools/engines/test_compare.py"]),
    ("fetch_sources_self_test", "code", False, ["python3", "tools/fetch_sources.py", "--self-test"]),
    ("archive_text_self_test", "code", False, ["python3", "tools/archive_text.py", "--self-test"]),
    ("check_extraction_self_test", "code", False, ["python3", "tools/check_extraction.py", "--self-test"]),
    ("check_macrs_tables_self_test", "code", True, ["python3", "tools/check_macrs_tables.py", "--self-test"]),
    ("check_auto_limits_self_test", "code", True, ["python3", "tools/check_auto_limits.py", "--self-test"]),
    ("check_source_titles_self_test", "code", False, ["python3", "tools/check_source_titles.py", "--self-test"]),
    ("worktree_data_self_test", "code", False, ["python3", "tools/worktree_data.py", "--self-test"]),
    ("check_slot_self_test", "code", False, ["python3", "tools/check_slot.py", "--self-test"]),
    ("check_times_self_test", "code", False, ["python3", "tools/check_times.py", "--self-test"]),
    ("step_output_self_test", "code", False, ["python3", "tools/step_output.py", "--self-test"]),
    ("year_carry_self_test", "code", False, ["python3", "tools/transcription/year_carry.py", "--self-test"]),
    ("citations_self_test", "code", True, ["python3", "tools/citations.py", "--self-test"]),
    ("year_diff_self_test", "code", True, ["python3", "tools/year_diff.py", "--self-test"]),
    ("propose_params_self_test", "code", False, ["python3", "tools/propose_params.py", "--self-test"]),
    ("fixtures_year_self_test", "code", False, ["python3", "tools/fixtures_year.py", "--self-test"]),
    ("year_ids_self_test", "code", False, ["python3", "tools/check_year_ids.py", "--self-test"]),
    ("coverage_tree_self_test", "code", True, ["python3", "tools/coverage/tree.py", "--self-test"]),
    ("instruction_cites_self_test", "code", True, ["python3", "tools/check_instruction_cites.py", "--self-test"]),
    ("operands_self_test", "code", True, ["python3", "tools/check_operands.py", "--self-test"]),
    ("signs_self_test", "code", True, ["python3", "tools/check_signs.py", "--self-test"]),
    ("consumers_self_test", "code", True, ["python3", "tools/check_consumers.py", "--self-test"]),
    ("limits_self_test", "code", True, ["python3", "tools/check_limits.py", "--self-test"]),
    ("twins_self_test", "code", True, ["python3", "tools/check_twins.py", "--self-test"]),
    ("completeness_self_test", "code", True, ["python3", "tools/transcription/check_completeness.py", "--self-test"]),
    ("ny_predict_self_test", "code", False, ["python3", "tools/ny_predict.py", "--self-test"]),
    ("review_yield_tests", "code", False, ["python3", "tools/transcription/test_review_yield.py"]),
    ("question_review_self_test", "code", False, ["python3", "tools/transcription/question_review.py", "--self-test"]),
    ("check_questions_self_test", "code", False, ["python3", "tools/transcription/check_questions.py", "--self-test"]),
    # The bookkeeping group: the bookkeeping tools' tests, and the tier classifier's (run by test_green.sh).
    ("bookkeeping_tools", "bookkeeping", False, ["python3", "-m", "unittest", "tools/test_bookkeeping_tools.py"]),
    ("green_self_test", "bookkeeping", False, ["bash", "tools/hooks/test_green.sh"]),
    ("siblings_self_test", "bookkeeping", False, ["python3", "tools/siblings.py", "--self-test"]),
    ("check_agent_runs_self_test", "bookkeeping", False, ["python3", "tools/check_agent_runs.py", "--self-test"]),
    ("claims_self_test", "bookkeeping", False, ["python3", "tools/claims.py", "--self-test"]),
    ("bug_inventory_self_test", "bookkeeping", False, ["python3", "tools/check_bug_inventory.py", "--self-test"]),
    ("docs_conventions_self_test", "bookkeeping", False, ["python3", "tools/check_docs_conventions.py", "--self-test"]),
    ("build_fresh_self_test", "code", False, ["python3", "tools/build_fresh.py", "--self-test"]),
    ("claude_hooks_self_test", "bookkeeping", False, ["bash", "-c", "python3 tools/claude_hooks/bash_guard.py --self-test && python3 tools/claude_hooks/agents.py --self-test"]),
]
GROUPS = ("bookkeeping", "code")


def workers():
    set_ = os.environ.get("SELF_TEST_WORKERS", "")
    if set_.isdigit() and int(set_) > 0:
        return int(set_)
    runs = os.environ.get("CHECK_ALL_MAX_RUNS", "")
    runs = int(runs) if runs.isdigit() and int(runs) > 0 else 2
    return max(1, ((os.cpu_count() or 2) - 2) // runs)


def run_one(test, year_args):
    name, _, year_aware, cmd = test
    t0 = time.monotonic()
    r = subprocess.run(cmd + (year_args if year_aware else []), cwd=ROOT, stdin=subprocess.DEVNULL,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return r.returncode, r.stdout.decode("utf-8", errors="replace"), time.monotonic() - t0


def parse(argv):
    group, times, listing, year_args = None, None, False, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--group" and i + 1 < len(argv):
            group = argv[i + 1]; i += 2; continue
        if a == "--times" and i + 1 < len(argv):
            times = argv[i + 1]; i += 2; continue
        if a == "--list":
            listing = True; i += 1; continue
        if a == "--year" and i + 1 < len(argv):
            year_args += argv[i:i + 2]; i += 2; continue
        if a.startswith("--year="):
            year_args.append(a); i += 1; continue
        sys.exit(f"self_tests: unknown argument {a!r}\n{__doc__}")
    if group is not None and group not in GROUPS:
        sys.exit(f"self_tests: --group must be one of {', '.join(GROUPS)}")
    if group is None and not listing:
        sys.exit(f"self_tests: --group is required\n{__doc__}")
    return group, times, listing, year_args


def main(argv):
    group, times, listing, year_args = parse(argv)
    tests = [t for t in TESTS if group is None or t[1] == group]
    if listing:
        for name, g, year_aware, cmd in tests:
            print(f"{name}\t{g}\t{' '.join(cmd)}{' [--year N]' if year_aware else ''}")
        return 0
    with ThreadPoolExecutor(max_workers=min(workers(), len(tests))) as pool:
        results = list(pool.map(lambda t: run_one(t, year_args), tests))
    failed = []
    for (name, *_), (rc, out, secs) in zip(tests, results):
        print(f"-- {name} ({secs:.0f} s){'' if rc == 0 else f': FAILED (exit {rc})'}")
        sys.stdout.write(out if out.endswith("\n") or not out else out + "\n")
        if rc != 0:
            failed.append(name)
    if times:
        with open(times, "a", encoding="utf-8") as f:
            for (name, *_), (_, _, secs) in zip(tests, results):
                f.write(f"{round(secs)} self_tests/{name}\n")
    sys.stdout.flush()
    if failed:
        print(f"self-tests failed ({group} group): {', '.join(failed)}", file=sys.stderr)
        return 1
    print(f"self-tests: {len(tests)} passed ({group} group)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
