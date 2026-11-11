#!/usr/bin/env python3
"""Where a check-all run spent its time: a summary of the times tools/check_all_steps.sh records.

    check_times.py [FILE] [--top N]     FILE: .git/check-all-times of this worktree by default
    check_times.py --self-test

FILE holds one line per timed thing, wall time in whole seconds first, in the order each finished:

    <seconds> <step>                       a step
    <seconds> self_tests/<name>            a self-test, run inside the step self_tests or bookkeeping_self_tests
    <seconds> stage:<label> <step>,...     a stage and the steps it ran, in the order they were declared
    <seconds> run:<tier>                   the whole run of the steps script

Stages run one after another (compile, build, then the waves). The steps of a stage run side by side, so a stage
lasts as long as its slowest step and the times of its steps do not add up to wall time. The summary therefore
gives, per stage, its wall time, its slowest step and the next slowest (shortening the slowest step saves at most
the difference between the two), and then every step by wall time with its stage beside it. A step with no stage
line belongs to a stage that did not finish (a run that was interrupted). --top N lists the N slowest steps and
self-tests (default: all).
"""
import subprocess
import sys


def parse(text):
    """{"steps": {name: s}, "tests": {name: s}, "stages": [(label, s, [step])], "run": (tier, s) or None}."""
    out = {"steps": {}, "tests": {}, "stages": [], "run": None}
    for n, line in enumerate(text.splitlines(), 1):
        parts = line.split()
        if not parts:
            continue
        if len(parts) < 2 or not parts[0].isdigit():
            raise ValueError(f"line {n}: expected '<seconds> <name>', got {line!r}")
        secs, name = int(parts[0]), parts[1]
        if name.startswith("stage:"):
            out["stages"].append((name[6:], secs, parts[2].split(",") if len(parts) > 2 else []))
        elif name.startswith("run:"):
            out["run"] = (name[4:], secs)
        elif name.startswith("self_tests/"):
            out["tests"][name[11:]] = secs
        else:
            out["steps"][name] = secs
    return out


def _ranked(names, steps):
    """The timed steps among `names`, slowest first; equal times in the order given."""
    return sorted((n for n in names if n in steps), key=lambda n: -steps[n])


def summary(data, top=None):
    steps, stages = data["steps"], list(data["stages"])
    staged = {s for _, _, names in stages for s in names}
    loose = [s for s in steps if s not in staged]
    stage_of = {s: label for label, _, names in stages for s in names}
    in_stages = sum(secs for _, secs, _ in stages)
    out = []
    if data["run"]:
        tier, total = data["run"]
        out.append(f"check-all times ({tier} tier): {total} s for the steps, {in_stages} s of it in the stages below")
    else:
        total = in_stages
        out.append(f"check-all times (run not finished): {in_stages} s in the finished stages")
    out += ["Stages run one after another. The steps of a stage run side by side: a stage lasts as long as its slowest",
            "step, and step times within a stage do not add up to wall time.", "",
            f"{'stage':10s} {'wall s':>6s} {'share':>6s} {'steps':>5s} {'sum s':>6s}  slowest step, then the next slowest"]
    for label, secs, names in stages:
        ranked = _ranked(names, steps)
        lead = ", then ".join(f"{n} {steps[n]}" for n in ranked[:2]) or "-"
        share = f"{100 * secs / total:.0f}%" if total else "-"
        out.append(f"{label:10s} {secs:6d} {share:>6s} {len(names):5d} {sum(steps.get(n, 0) for n in names):6d}  {lead}")
    if loose:
        out.append(f"{'(no stage)':10s} {'-':>6s} {'-':>6s} {len(loose):5d} {sum(steps[s] for s in loose):6d}  "
                   "steps of a stage that did not finish")
    out += ["", "Steps by wall time" + (f" (the {top} slowest of {len(steps)})" if top and top < len(steps) else "") + ":",
            f"{'s':>6s}  {'stage':10s} step"]
    # The slowest step of a stage sets its wall time; the note says how far shortening it alone can help.
    limit = {}
    for label, _, names in stages:
        ranked = _ranked(names, steps)
        if len(ranked) > 1:
            limit[ranked[0]] = f"sets the stage's time; alone it can save at most {steps[ranked[0]] - steps[ranked[1]]} s (next: {ranked[1]})"
        elif ranked:
            limit[ranked[0]] = "the stage's only step"
    for name in _ranked(steps, steps)[:top]:
        note = f"   {limit[name]}" if name in limit else ""
        out.append(f"{steps[name]:6d}  {stage_of.get(name, '(no stage)'):10s} {name}{note}")
    if data["tests"]:
        tests = data["tests"]
        out += ["", "Self-tests, run in a worker pool inside the steps self_tests and bookkeeping_self_tests"
                + (f" (the {top} slowest of {len(tests)})" if top and top < len(tests) else "") + ":"]
        out += [f"{tests[n]:6d}  {n}" for n in _ranked(tests, tests)[:top]]
    return "\n".join(out) + "\n"


def self_test():
    text = "\n".join(["20 compile", "20 stage:compile compile", "9 check_self_test", "70 build", "30 lean_build",
                      "70 stage:build build,check_self_test,lean_build", "4 self_tests/quick", "40 self_tests/slow",
                      "41 self_tests", "100 mutate", "60 compare", "100 stage:wave2 self_tests,mutate,compare",
                      "195 run:full", ""])
    data = parse(text)
    got = summary(data)
    bad = []
    for want in ("check-all times (full tier): 195 s for the steps, 190 s of it in the stages below",
                 "build          70    36%     3    109  build 70, then lean_build 30",
                 "wave2         100    51%     3    201  mutate 100, then compare 60",
                 "   100  wave2      mutate   sets the stage's time; alone it can save at most 40 s (next: compare)",
                 "    20  compile    compile   the stage's only step",
                 "    30  build      lean_build\n",
                 "    40  slow\n     4  quick\n"):
        if want not in got:
            bad.append(f"missing {want!r}")
    order = [l.split()[2] for l in got.split("Steps by wall time:\n")[1].split("\n\n")[0].splitlines()[1:]]
    if order != ["mutate", "build", "compare", "self_tests", "lean_build", "compile", "check_self_test"]:
        bad.append(f"steps not sorted by time: {order}")
    # An interrupted run: a step finished but its stage and the run did not.
    cut = summary(parse("20 compile\n20 stage:compile compile\n7 fetch_sources\n"))
    for want in ("check-all times (run not finished): 20 s in the finished stages",
                 "(no stage)      -      -     1      7  steps of a stage that did not finish",
                 "     7  (no stage) fetch_sources"):
        if want not in cut:
            bad.append(f"interrupted run: missing {want!r}")
    if "the 2 slowest of 7" not in summary(data, top=2) or "  compare\n" in summary(data, top=2):
        bad.append("--top does not cut the list")
    try:
        parse("fast compile\n")
        bad.append("a malformed line was accepted")
    except ValueError:
        pass
    if bad:
        print("check_times self-test FAILED:\n  " + "\n  ".join(bad) + "\n" + got)
        return 1
    print("check_times self-test: ok")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    top, paths, i = None, [], 0
    while i < len(argv):
        if argv[i] == "--top" and i + 1 < len(argv) and argv[i + 1].isdigit():
            top = int(argv[i + 1]); i += 2
        elif argv[i].startswith("-"):
            sys.exit(f"check_times: unknown argument {argv[i]!r}\n{__doc__}")
        else:
            paths.append(argv[i]); i += 1
    if len(paths) > 1:
        sys.exit(f"check_times: one file at most\n{__doc__}")
    path = paths[0] if paths else subprocess.run(["git", "rev-parse", "--git-path", "check-all-times"], capture_output=True,
                                                 text=True, check=True).stdout.strip()
    try:
        with open(path, encoding="utf-8") as f:
            data = parse(f.read())
    except (OSError, ValueError) as ex:
        sys.exit(f"check_times: {path}: {ex}")
    sys.stdout.write(summary(data, top))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
