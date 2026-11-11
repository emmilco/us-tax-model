#!/usr/bin/env python3
"""Lines a check-all step's output must have: the self-tests a step runs inside itself.

    step_output.py --logs DIR STEP...     (tools/check_all_steps.sh, for the steps of a wave that passed)
    step_output.py --self-test

A self-test with a row in tools/self_tests.py is run and named by that file. A self-test that a step runs
inside itself (the comparison's planted differences, the mutation check's self-tests of its equivalence
reasoning) is only a call in the step's code: with the call removed the step would print one line less and
still pass. REQUIRED therefore lists, per step, the line each such self-test prints when it ran and found no
problem, and check-all fails a step that exits 0 without one of them.

--logs DIR STEP...: for each STEP, DIR/STEP.log is its output. Every line REQUIRED lists for the step must be
in it, whole. For each step that lacks one, what is missing is appended to its log and the step's name is
printed, one per line; the exit status is 0 whether or not a step is named, so that any other status means the
check itself did not run (the caller fails the run on it).

A row of REQUIRED is (what the line shows, a pattern the whole line must match, an example of the line). A
pattern asks for a count of one or more where the self-test reports how much it tested and that count cannot
be zero in a run that tested something.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEPS = ROOT / "tools" / "check_all_steps.sh"

# engine/src/compare.ts, compareEvaluators.
COMPARE = [
    ("the comparison's self-test on Bool and enum choose lines (typedChooseAgreement)",
     r"compare self-test: [1-9][0-9]* cases of Bool and enum choose, 0 problem\(s\)",
     "compare self-test: 11 cases of Bool and enum choose, 0 problem(s)"),
    ("the comparison's self-test of planted differences (plantedDifferences)",
     r"compare self-test: [1-9][0-9]* differences planted on generated returns, 0 problem\(s\)",
     "compare self-test: 16 differences planted on generated returns, 0 problem(s)"),
]
# engine/src/mutate.ts, runMutation. The retargeting self-test may have no pinned argument to retarget among a
# run's mutants; it fails by itself when it should have had one.
MUTATE = [
    ("the retargeting self-test of the pinned arguments (retargetSelfTest)",
     r"mutation: retargeting self-test: [0-9]+ pinned arguments retargeted and rejected, 0 problems",
     "mutation: retargeting self-test: 12 pinned arguments retargeted and rejected, 0 problems"),
    ("the whole-dollar parameter self-test (wholeParamSelfTest)",
     r"mutation: whole-dollar parameter self-test: 0 problems",
     "mutation: whole-dollar parameter self-test: 0 problems"),
    ("the unknown-guard side-condition self-test (unknownGuardSelfTest)",
     r"mutation: unknown-guard side-condition self-test: 0 problems",
     "mutation: unknown-guard side-condition self-test: 0 problems"),
    ("the guarded-figure dominance self-test (guardedFigureSelfTest)",
     r"mutation: guarded-figure dominance self-test: 0 problems",
     "mutation: guarded-figure dominance self-test: 0 problems"),
    ("the premise-digest self-test (premiseDigestSelfTest)",
     r"mutation: premise-digest self-test: [1-9][0-9]* edits checked, 0 problems",
     "mutation: premise-digest self-test: 40 edits checked, 0 problems"),
    ("the self-test of the reasoning through a Bool or enum choose (scalarChooseSelfTest)",
     r"mutation: Bool and enum choose reasoning self-test: 0 problems",
     "mutation: Bool and enum choose reasoning self-test: 0 problems"),
]
REQUIRED = {
    # engine/src/check-selftest.ts, runCheckSelfTest.
    "check_self_test": [
        ("the self-test of the fixtures' test-data defaults (defaultsSelfTest)",
         r"defaults self-test: [1-9][0-9]* cases passed \(conditional withholding, condition and rule validation, "
         r"consistency violations\)",
         "defaults self-test: 47 cases passed (conditional withholding, condition and rule validation, consistency "
         "violations)"),
    ],
    "compare": COMPARE,
    "ny_compare": COMPARE,
    "mutate": MUTATE,
    "ny_mutate": MUTATE,
    # tools/engines/run.sh runs the UsTaxes adapter's self-test; the step and the self-test each skip, saying
    # so, when the engines they need are not installed.
    "engine_differential": [
        ("the UsTaxes line cache self-test (tools/engines/ustaxes_adapter.py --self-test, run by tools/engines/run.sh), "
         "or the line that says it or the whole step was skipped",
         r"UsTaxes line cache self-test: [1-9][0-9]* returns, [1-9][0-9]* values identical with and without the cache"
         r"|UsTaxes self-test: SKIPPED - .+|engine differential: SKIPPED - .+",
         "UsTaxes line cache self-test: 20 returns, 3000 values identical with and without the cache"),
    ],
    # tools/hooks/test_green.sh (the self-test green_self_test) ends by running the path rule's own self-test.
    "bookkeeping_self_tests": [
        ("the tier path rule's self-test (tools/tier_paths.py --self-test, run by tools/hooks/test_green.sh)",
         r"tier paths self-test: ok \(.+\)",
         "tier paths self-test: ok (9 docs-tier patterns, 7 full-tier patterns, 208 code files scanned, "
         "45 references and 18 enumerations accounted for)"),
    ],
}


def missing(step, text):
    """The rows of REQUIRED[step] no whole line of `text` matches."""
    lines = text.splitlines()
    return [row for row in REQUIRED.get(step, []) if not any(re.fullmatch(row[1], line) for line in lines)]


def check_logs(logs, steps):
    """Append what each step's log lacks to that log; the steps that lack a line."""
    lacking = []
    for step in steps:
        path = Path(logs) / f"{step}.log"
        rows = missing(step, path.read_text(encoding="utf-8", errors="replace"))
        if not rows:
            continue
        lacking.append(step)
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"check-all: step {step} exited 0 without a line its output must have (tools/step_output.py); "
                    "a self-test inside the step did not run or did not pass:\n")
            for what, pattern, _ in rows:
                f.write(f"  {what}\n    no line matches: {pattern}\n")
    return lacking


def declared_steps(script):
    """The step names tools/check_all_steps.sh declares: `step NAME` and, for `jstep NAME`, NAME and ny_NAME."""
    names = set()
    for kind, name in re.findall(r"^\s*(?:if .*; then |else )?(step|jstep) ([a-z0-9_]+)\b", script, re.M):
        names.add(name)
        if kind == "jstep":
            names.add(f"ny_{name}")
    return names


def self_test():
    import tempfile
    bad = []
    for step, rows in REQUIRED.items():
        for what, pattern, example in rows:
            if not re.fullmatch(pattern, example):
                bad.append(f"{step}: the example of {what} does not match its pattern")
        full = "".join(f"{example}\n" for _, _, example in rows)
        if missing(step, "other output\n" + full + "more output\n"):
            bad.append(f"{step}: a log with every required line is reported as lacking one")
        for i, row in enumerate(rows):
            without = "".join(f"{example}\n" for j, (_, _, example) in enumerate(rows) if j != i)
            if missing(step, without) != [row]:
                bad.append(f"{step}: a log without {row[0]} is not reported as lacking exactly that line")
    # A line that reports problems, a count of zero, or the line inside a longer one is not the required line.
    for text in ("compare self-test: 16 differences planted on generated returns, 1 problem(s)\n",
                 "compare self-test: 0 differences planted on generated returns, 0 problem(s)\n",
                 "note: compare self-test: 16 differences planted on generated returns, 0 problem(s)\n"):
        if COMPARE[1] not in missing("compare", text):
            bad.append(f"accepted as the planted-differences line: {text.strip()!r}")
    if missing("check_logs", ""):
        bad.append("a step with no required line is reported as lacking one")
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "compare.log").write_text(COMPARE[0][2] + "\n", encoding="utf-8")
        (Path(d) / "ny_compare.log").write_text(COMPARE[0][2] + "\n" + COMPARE[1][2] + "\n", encoding="utf-8")
        (Path(d) / "citations.log").write_text("", encoding="utf-8")
        if check_logs(d, ["compare", "ny_compare", "citations"]) != ["compare"]:
            bad.append("--logs does not name exactly the step whose log lacks a line")
        said = (Path(d) / "compare.log").read_text(encoding="utf-8")
        if "check-all: step compare exited 0 without a line" not in said or COMPARE[1][1] not in said:
            bad.append("--logs does not write what is missing to the step's log")
        if (Path(d) / "ny_compare.log").read_text(encoding="utf-8").count("\n") != 2:
            bad.append("--logs wrote to the log of a step that lacks nothing")
    # The table and the steps script agree: every step with required lines is declared, and each wave is checked.
    script = STEPS.read_text(encoding="utf-8")
    declared = declared_steps(script)
    for step in REQUIRED:
        if step not in declared:
            bad.append(f"{step} has required lines but tools/check_all_steps.sh declares no such step")
    if len(declared) < 40:
        bad.append(f"only {len(declared)} steps read from tools/check_all_steps.sh; its declarations are not being parsed")
    wave = re.search(r"^wave\(\) \{\n(.*?)^\}", script, re.M | re.S)
    if not wave or 'python3 tools/step_output.py --logs "$logs"' not in wave.group(1):
        bad.append("wave() in tools/check_all_steps.sh does not run tools/step_output.py --logs on its steps")
    if bad:
        print("step output self-test FAILED:\n  " + "\n  ".join(bad))
        return 1
    print(f"step output self-test: ok ({sum(len(r) for r in REQUIRED.values())} required lines over {len(REQUIRED)} steps)")
    return 0


def main(argv):
    if argv == ["--self-test"]:
        return self_test()
    if len(argv) < 2 or argv[0] != "--logs":
        sys.exit(f"step_output: unknown arguments {argv!r}\n{__doc__}")
    for step in check_logs(argv[1], argv[2:]):
        print(step)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
