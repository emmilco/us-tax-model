#!/usr/bin/env python3
"""The run settings a self-test does not inherit, and the check that every variable the tools read is classified.

    hermetic_env.py --unset        print a shell command that unsets every run setting (STRIP)
    hermetic_env.py --unclassified print each variable the tools read that no list classifies, with a file reading it
    hermetic_env.py --self-test

A check-all run sets variables for its own steps: the run's mode (CHECK_ALL_RELEASE, ENGINE_CACHE, BUILD_CACHE),
what it has already done (CHECK_ALL_PREFLIGHT) or skips (AGENT_RUNS_FOLD), what a step checks (tools/green.sh,
SIZING_ENV), and the places a tool is pointed at instead of its own (CHECK_ALL_SLOT_DIR, BUILD_CACHE_DIR). A
self-test sets up the cases it tests and expects the tools' defaults otherwise, so it must behave inside a run, release
mode and the preflight included, as when run alone. Every self-test runner therefore drops STRIP from the environment
it gives its tests: tools/self_tests.py through hermetic(), and each shell self-test (tools/hooks/test_*.sh,
tools/test_*.sh) on its first line through `eval "$(python3 -I tools/hermetic_env.py --unset)"`.

PASS is passed on: the worker counts and CHECK_ALL_MAX_RUNS (the run's share of the machine) set only how fast a test
runs, and CHECK_ALL_SLOT says the process already holds a check-all slot, so that an engine command that takes one
(engine/src/slot.ts) does not wait for a second slot while its own run holds the first. EXTERNAL lists the
variables of the system and of other programs that the tools read.

--self-test: every variable the tools read from the environment (read_names(): os.environ and os.getenv in Python,
process.env in TypeScript and JavaScript, $NAME in a shell script that does not assign NAME itself) is in STRIP, PASS
or EXTERNAL, so that a new run setting cannot leak into the self-tests unclassified; every shell self-test unsets
STRIP; then hermetic() and --unset on a planted environment.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The run settings: dropped from every self-test's environment. PREFLIGHT_FAIL, FAIL and NO_TIER_LINE are what the shell
# self-tests set for their stubs in some calls only.
STRIP = frozenset("""
    CHECK_ALL_RELEASE CHECK_ALL_PREFLIGHT CHECK_ALL_ALLOW_OPEN_BUGS CHECK_ALL_SLOT_DIR CHECK_ALL_SLOT_MEASURE
    AGENT_RUNS_FOLD RUN_DIR COMMIT_TESTED_TREE PREFLIGHT_FAIL
    ENGINE_CACHE ENGINE_CACHE_WORKTREE ENGINE_TRACE_DIR ENGINE_TRACE_ID ENGINE_SEED ENGINE_CASES ENGINE_SE_CASES
    ENGINE_JOINT_CASES BUILD_CACHE BUILD_CACHE_DIR BUILD_CACHE_SELF_TEST_VAR
    PROPERTY_RUNS INTERVIEW_RULES_RUNS INTERVIEW_RULES_COMPLETE INTERVIEW_RULES_POOL INTERVIEW_RULES_RANDOM_EVERY
    INTERVIEW_RULES_SEEDS MUTATE_TIER MUTATE_SAMPLE MUTATE_SAMPLE_TIMES SIBLINGS_BUGS NY_REVIEWS_ROOT REVIEW_PENDING_FILE
    FAIL NO_TIER_LINE
""".split())
# Passed on: how fast a test runs, and whether its process already holds a check-all slot.
PASS = frozenset("""
    CHECK_ALL_MAX_RUNS CHECK_ALL_SLOT BUILD_WORKERS TEST_WORKERS INTERVIEW_WORKERS MUTATE_WORKERS SELF_TEST_WORKERS
""".split())
# The system's and other programs' variables, and bash's own.
EXTERNAL = frozenset("""
    TMPDIR HOME PATH NODE_OPTIONS PYENV_VERSION CLAUDE_PROJECT_DIR DEEPSEEK_KEYCHAIN_ACCOUNT
    RANDOM PIPESTATUS BASH_SOURCE LINENO SECONDS
""".split())
# Variables a shell script reads that tools/green.sh, which it sources, sets.
SOURCED = frozenset("MARKER GREEN_TREES SIZING_ENV REQUIRED REQUIRED_WHY".split())

PY_READS = [r'os\.environ\.get\(\s*["\']([A-Z_][A-Z0-9_]*)', r'os\.environ\[\s*["\']([A-Z_][A-Z0-9_]*)',
            r'os\.getenv\(\s*["\']([A-Z_][A-Z0-9_]*)', r'["\']([A-Z_][A-Z0-9_]*)["\']\s+(?:not\s+)?in\s+os\.environ']
TS_READS = [r'process\.env\.([A-Z_][A-Z0-9_]*)', r'process\.env\[\s*["\']([A-Z_][A-Z0-9_]*)']
SH_READ = r'\$\{?!?([A-Z_][A-Z0-9_]*)'


def scanned_files(root):
    for base in ("tools", "engine/src", "ui/src"):
        for p in sorted((root / base).rglob("*")):
            if p.is_file() and not ({"node_modules", "ustaxes", "__pycache__"} & set(p.parts)):
                yield p


def kind(p, text):
    if p.suffix == ".py":
        return "py"
    if p.suffix in (".ts", ".mjs", ".js"):
        return "ts"
    first = text.split("\n", 1)[0]
    if p.suffix == ".sh" or (first.startswith("#!") and ("bash" in first or first.endswith("/sh"))):
        return "sh"
    return None


def shell_reads(text):
    """The upper-case variables a shell script reads and does not assign itself (comments dropped)."""
    code = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    names = set(re.findall(SH_READ, code))
    assigned = set(re.findall(r'(?:^|[\s;(&|])(?:export\s+|local\s+|readonly\s+)?([A-Z_][A-Z0-9_]*)\+?=', code))
    assigned |= set(re.findall(r'\bfor\s+([A-Z_][A-Z0-9_]*)\s+in\b', code))
    for decl in re.findall(r'\b(?:read|local|export|unset)\s+((?:-\w+\s+)*[A-Z_][A-Z0-9_ ]*)', code):
        assigned |= set(re.findall(r'\b[A-Z_][A-Z0-9_]*\b', decl))
    return names - assigned


def read_names(root=ROOT):
    """{variable: first file reading it} over tools/, engine/src/ and ui/src/."""
    found = {}
    for p in scanned_files(root):
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        k = kind(p, text)
        if k == "py":
            names = {n for pat in PY_READS for n in re.findall(pat, text)}
        elif k == "ts":
            names = {n for pat in TS_READS for n in re.findall(pat, text)}
        elif k == "sh":
            names = shell_reads(text)
        else:
            continue
        for n in sorted(names):
            found.setdefault(n, str(p.relative_to(root)))
    return found


def unclassified(root=ROOT):
    return {n: f for n, f in read_names(root).items() if n not in STRIP | PASS | EXTERNAL | SOURCED}


def hermetic(env=None):
    """The environment without the run settings."""
    return {k: v for k, v in (os.environ if env is None else env).items() if k not in STRIP}


def unset_command():
    return "unset " + " ".join(sorted(STRIP))


def self_test():
    problems = []
    for n, f in sorted(unclassified().items()):
        problems.append(f"{n} (read in {f}) is in none of STRIP, PASS and EXTERNAL: a run setting goes in STRIP")
    for n in sorted(STRIP & (PASS | EXTERNAL)) + sorted(PASS & EXTERNAL):
        problems.append(f"{n} is in two lists")
    known = read_names()
    for must in ("CHECK_ALL_RELEASE", "CHECK_ALL_PREFLIGHT", "ENGINE_CACHE", "AGENT_RUNS_FOLD", "CHECK_ALL_SLOT"):
        if must not in known:
            problems.append(f"the scan of the tools' reads lost {must}")
    for p in sorted(list((ROOT / "tools").glob("test_*.sh")) + list((ROOT / "tools" / "hooks").glob("test_*.sh"))):
        if "tools/hermetic_env.py\" --unset)\"" not in p.read_text(encoding="utf-8"):
            problems.append(f"{p.relative_to(ROOT)} does not unset the run settings (eval \"$(python3 -I "
                            "\"$ROOT/tools/hermetic_env.py\" --unset)\")")
    planted = {"PATH": "/bin", "CHECK_ALL_PREFLIGHT": "done", "ENGINE_CACHE": "verify", "CHECK_ALL_SLOT": "/s",
               "CHECK_ALL_MAX_RUNS": "2", "PROPERTY_RUNS": "9"}
    if hermetic(planted) != {"PATH": "/bin", "CHECK_ALL_SLOT": "/s", "CHECK_ALL_MAX_RUNS": "2"}:
        problems.append(f"hermetic() kept or dropped the wrong variables: {hermetic(planted)}")
    env = dict(os.environ, CHECK_ALL_PREFLIGHT="done", CHECK_ALL_RELEASE="1", CHECK_ALL_SLOT="/s")
    out = subprocess.run(["bash", "-c", f'eval "$({sys.executable} -I {__file__} --unset)"; '
                          'echo "${CHECK_ALL_PREFLIGHT-unset} ${CHECK_ALL_RELEASE-unset} ${CHECK_ALL_SLOT-unset}"'],
                         env=env, capture_output=True, text=True).stdout.strip()
    if out != "unset unset /s":
        problems.append(f"--unset in a shell left: {out!r}")
    sample = 'X="$CHECK_ALL_RELEASE"\nY=1\necho "$Y ${Z:-}"\n# $COMMENTED\nfor W in a; do :; done; echo "$W"\n'
    if shell_reads(sample) != {"CHECK_ALL_RELEASE", "Z"}:
        problems.append(f"shell_reads on a sample: {sorted(shell_reads(sample))}")
    for p in problems:
        print(f"hermetic-env self-test: {p}", file=sys.stderr)
    if problems:
        return 1
    print(f"hermetic-env self-test: {len(known)} variables the tools read, all classified; 0 problems")
    return 0


def main(argv):
    if argv == ["--unset"]:
        print(unset_command())
        return 0
    if argv == ["--unclassified"]:
        for n, f in sorted(unclassified().items()):
            print(f"{n}\t{f}")
        return 0
    if argv == ["--self-test"]:
        return self_test()
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
