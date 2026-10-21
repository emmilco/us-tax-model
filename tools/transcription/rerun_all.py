#!/usr/bin/env python3
"""Rerun every model review (transcription agreement, render comparison, class M
hand-work) against the current archived text, a few at a time, and report.

Each tool call is one fixed-prompt `claude -p` with no tools (fixed-prompt,
curated input, no action surface). Exit status 3 from a tool means disagreements to
rule on, not a failure of the run. Logs and fixtures are written by the tools
themselves; this driver only schedules and summarises.

    rerun_all.py [--kinds transcription,render,classm] [--forms a,b] [--jobs 4] [--model M]
"""
import argparse, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y, YEAR_ARGS  # noqa: E402
TOOLS = {"transcription": ("transcribe.py", "--form"), "render": ("render_compare.py", "--form"), "classm": ("classm.py", "--doc")}


def forms_for(kind):
    d = os.path.join(ROOT, "reviews", Y, kind)
    return sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md"))


def run(kind, form, model):
    script, flag = TOOLS[kind]
    cmd = [sys.executable, os.path.join(HERE, script), flag, form, *YEAR_ARGS] + (["--model", model] if model else [])
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    last = (r.stdout.strip().splitlines() or [""])[-1]
    return {"kind": kind, "form": form, "exit": r.returncode, "seconds": round(time.time() - t0), "last": last, "stderr": r.stderr[-400:] if r.returncode not in (0, 3) else ""}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kinds", default="transcription,render,classm")
    ap.add_argument("--forms", help="restrict to these forms (comma-separated)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--model")
    ap.add_argument("--summary", default=os.path.join(ROOT, ".transcription", "rerun_summary.json"))
    a = ap.parse_args()
    jobs = []
    for kind in a.kinds.split(","):
        for form in forms_for(kind):
            if a.forms and form not in a.forms.split(","):
                continue
            jobs.append((kind, form))
    if "classm" in a.kinds.split(","):
        subprocess.run(["node", os.path.join(ROOT, "engine", "dist", "main.js"), "classm-jobs", *YEAR_ARGS], check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
    print(f"{len(jobs)} runs, {a.jobs} at a time", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for res in ex.map(lambda kf: run(kf[0], kf[1], a.model), jobs):
            results.append(res)
            tag = "ok" if res["exit"] == 0 else "rule" if res["exit"] == 3 else f"EXIT {res['exit']}"
            print(f"[{tag:6s}] {res['kind']:13s} {res['form']:16s} {res['seconds']:4d}s  {res['last'][:110]}", flush=True)
            if res["stderr"]:
                print("         " + res["stderr"].replace("\n", "\n         "), flush=True)
    os.makedirs(os.path.dirname(a.summary), exist_ok=True)
    json.dump(results, open(a.summary, "w"), indent=1)
    bad = [r for r in results if r["exit"] not in (0, 3)]
    open_rulings = [r for r in results if r["exit"] == 3]
    print(f"\ndone: {len(results)} runs; {len(open_rulings)} with disagreements to rule on; {len(bad)} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
