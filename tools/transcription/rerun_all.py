#!/usr/bin/env python3
"""Rerun every model review (transcription agreement, render comparison, class M
hand-work) against the current archived text, a few at a time, and report.

Each tool call uses the selected model's fixed-prompt transport with no tools
(curated input, no action surface). Exit status 3 from a tool means disagreements to
rule on, not a failure of the run. Logs and fixtures are written by the tools
themselves; this driver only schedules and summarises.

    rerun_all.py [--kinds transcription,render,classm] [--forms a,b] [--jobs 4] [--model M]

The forms of a kind are those with a log of any model family; each tool writes the log of
the family `--model` names (families.py), so a second family's run leaves the Claude logs as
they are.
"""
import argparse, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y, YEAR_ARGS  # noqa: E402
import families  # noqa: E402
TOOLS = {"transcription": ("transcribe.py", "--form"), "render": ("render_compare.py", "--form"), "classm": ("classm.py", "--doc")}


def forms_for(kind):
    d = os.path.join(ROOT, "reviews", Y, kind)
    return sorted({families.split_stem(f[:-3])[0] for f in os.listdir(d) if f.endswith(".md")})


def run(kind, form, model, resume=False, reasoning_effort=None, max_output_tokens=None):
    script, flag = TOOLS[kind]
    cmd = [sys.executable, os.path.join(HERE, script), flag, form, *YEAR_ARGS] + (["--model", model] if model else [])
    if reasoning_effort:
        cmd += ["--reasoning-effort", reasoning_effort]
    if max_output_tokens is not None:
        cmd += ["--max-output-tokens", str(max_output_tokens)]
    t0 = time.time()
    reused = False
    if resume:
        r = subprocess.run([*cmd, "--from-response"], capture_output=True, text=True, cwd=ROOT)
        reused = r.returncode in (0, 3)
    if not reused:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    last = (r.stdout.strip().splitlines() or [""])[-1]
    return {"kind": kind, "form": form, "exit": r.returncode, "seconds": round(time.time() - t0), "reused": reused,
            "last": last, "stderr": r.stderr[-400:] if r.returncode not in (0, 3) else ""}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kinds", default="transcription,render,classm")
    ap.add_argument("--forms", help="restrict to these forms (comma-separated)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--model")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int)
    ap.add_argument("--resume", action="store_true", help="reuse only responses whose recorded request exactly matches the current prompt/model/system/policy")
    ap.add_argument("--summary", default=os.path.join(ROOT, ".transcription", "rerun_summary.json"))
    a = ap.parse_args()
    if a.jobs < 1:
        ap.error("--jobs must be positive")
    if set(a.kinds.split(",")) - set(TOOLS):
        ap.error("unknown review kind")
    jobs = []
    for kind in a.kinds.split(","):
        for form in forms_for(kind):
            if a.forms and form not in a.forms.split(","):
                continue
            jobs.append((kind, form))
    # classm.py rebuilds its own document's jobs under a lock. A redundant
    # all-document corpus here can exhaust the heap before any review starts.
    print(f"{len(jobs)} runs, {a.jobs} at a time", flush=True)
    results = []
    os.makedirs(os.path.dirname(a.summary), exist_ok=True)
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        pending = [ex.submit(run, kind, form, a.model, a.resume, a.reasoning_effort, a.max_output_tokens) for kind, form in jobs]
        for future in as_completed(pending):
            res = future.result()
            results.append(res)
            tag = "ok" if res["exit"] == 0 else "rule" if res["exit"] == 3 else f"EXIT {res['exit']}"
            print(f"[{tag:6s}] {res['kind']:13s} {res['form']:16s} {res['seconds']:4d}s  {res['last'][:110]}", flush=True)
            if res["stderr"]:
                print("         " + res["stderr"].replace("\n", "\n         "), flush=True)
            with open(a.summary + ".tmp", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=1)
            os.replace(a.summary + ".tmp", a.summary)
    bad = [r for r in results if r["exit"] not in (0, 3)]
    open_rulings = [r for r in results if r["exit"] == 3]
    print(f"\ndone: {len(results)} runs; {len(open_rulings)} with disagreements to rule on; {len(bad)} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
