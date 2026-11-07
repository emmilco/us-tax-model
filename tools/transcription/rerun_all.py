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

A model family's first usage-limit failure (USAGE_LIMIT) opens its breaker: no further job of that
family calls the model in this run (a --resume reuse of a matching saved response still runs, since it
makes no call). Calls already in flight finish. The jobs not run are listed at the end with the command
that reruns them, and recorded in the summary file with "skipped": "usage limit".
"""
import argparse, json, os, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y, YEAR_ARGS  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York documents; passed on to each tool)
import families  # noqa: E402
TOOLS = {"transcription": ("transcribe.py", "--form"), "render": ("render_compare.py", "--form"), "classm": ("classm.py", "--doc")}
# A transport's report that the account's usage allowance or balance is spent (codex: "You've hit your usage
# limit"; claude -p: "Claude AI usage limit reached", "5-hour limit reached", "You've hit your limit";
# DeepSeek: HTTP 402 "Insufficient Balance"). A rate limit, a timeout or an oversized request is not one.
USAGE_LIMIT = re.compile(r"usage limit|hit your (?:\w+ )?limit|(?:hour|weekly|session) limit reached|"
                         r"insufficient balance|exceeded your (?:current )?quota|deepseek HTTP 402", re.I)


class Breaker:
    """Per model family: the job whose usage-limit failure opened it, or nothing while closed."""

    def __init__(self):
        self.lock, self.opened = threading.Lock(), {}

    def open_for(self, family):
        with self.lock:
            return self.opened.get(family)

    def trip(self, family, job):
        with self.lock:
            self.opened.setdefault(family, job)


def forms_for(kind):
    """The forms with a log of the kind; in New York mode also the New York documents whose first review
    is pending (pending.py), so the first run reviews them."""
    d = os.path.join(str(jurisdiction.ypath("reviews", Y)), kind)
    logged = {families.split_stem(f[:-3])[0] for f in os.listdir(d) if f.endswith(".md")} if os.path.isdir(d) else set()
    if jurisdiction.NY:
        import pending
        logged |= pending.listed(kind)
    return sorted(logged)


def run(kind, form, model, resume=False, reasoning_effort=None, max_output_tokens=None, case_jobs=1, carry=True, lines=None,
        breaker=None):
    script, flag = TOOLS[kind]
    family = families.family_of(model) if model else families.DEFAULT
    cmd = [sys.executable, os.path.join(HERE, script), flag, form, *YEAR_ARGS, *jurisdiction.J_ARGS] + (["--model", model] if model else [])
    if reasoning_effort:
        cmd += ["--reasoning-effort", reasoning_effort]
    if max_output_tokens is not None:
        cmd += ["--max-output-tokens", str(max_output_tokens)]
    if lines and kind in ('transcription', 'render'):
        cmd += ['--lines', lines]  # T-219: review only the lines whose subject changed, merged into the log
    if kind == 'classm' and case_jobs != 1:
        cmd += ['--case-jobs', str(case_jobs)]
    t0 = time.time()
    reused = False
    if resume:
        r = subprocess.run([*cmd, "--from-response"], capture_output=True, text=True, cwd=ROOT)
        reused = r.returncode in (0, 3)
    if not reused:
        tripped = breaker.open_for(family) if breaker else None
        if tripped:
            return {"kind": kind, "form": form, "exit": None, "seconds": round(time.time() - t0), "reused": False,
                    "last": f"not run: the {family} family hit its usage limit ({tripped})", "stderr": "",
                    "skipped": "usage limit", "family": family}
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        if r.returncode not in (0, 3) and USAGE_LIMIT.search(r.stderr + "\n" + r.stdout) and breaker:
            breaker.trip(family, f"{kind} {form}")
    last = (r.stdout.strip().splitlines() or [""])[-1]
    if r.returncode == 3 and carry:
        # T-218: carry earlier rulings over to repeat disagreements (same line, same content, line unchanged)
        fam = families.family_of(model) if model else families.DEFAULT
        ccmd = [sys.executable, os.path.join(HERE, "carry.py"), "--kind", kind, "--form", form, *jurisdiction.J_ARGS]
        if fam != families.DEFAULT:
            ccmd += ["--family", fam]
        c = subprocess.run(ccmd, capture_output=True, text=True, cwd=ROOT)
        cl = (c.stdout.strip().splitlines() or [""])[-1]
        last = f"{last} | carry: {cl}"
    out = {"kind": kind, "form": form, "exit": r.returncode, "seconds": round(time.time() - t0), "reused": reused,
           "last": last, "stderr": r.stderr[-400:] if r.returncode not in (0, 3) else ""}
    if r.returncode not in (0, 3) and USAGE_LIMIT.search(r.stderr + "\n" + r.stdout):
        out["usage_limit"], out["family"] = True, family
    return out


def eligible(kind, form, family):
    """A second family's log of this form would qualify for second-family credit once current
    (compare_families.eligible_when_current): staleness alone does not disqualify it, so a stale log that would
    earn credit is rerun, as check_logs requires."""
    import compare_families
    try:
        return compare_families.eligible_when_current(compare_families.compare(kind, form, family)["quality"])[0]
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kinds", default="transcription,render,classm")
    ap.add_argument("--forms", help="restrict to these forms (comma-separated)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--model")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int)
    ap.add_argument("--case-jobs", type=int, default=1)
    ap.add_argument("--resume", action="store_true", help="reuse only responses whose recorded request exactly matches the current prompt/model/system/policy")
    ap.add_argument("--lines", help="line-scoped transcription and render reviews (e.g. auto: the lines whose subject changed)")
    ap.add_argument("--no-carry", action="store_true", help="do not carry earlier rulings over to repeat disagreements (carry.py)")
    ap.add_argument("--summary", default=os.path.join(ROOT, ".transcription", "rerun_summary.json"))
    a = ap.parse_args()
    if a.jobs < 1:
        ap.error("--jobs must be positive")
    if set(a.kinds.split(",")) - set(TOOLS):
        ap.error("unknown review kind")
    jobs = []
    fam = families.family_of(a.model) if a.model else families.DEFAULT
    skipped = []
    for kind in a.kinds.split(","):
        for form in forms_for(kind):
            if a.forms and form not in a.forms.split(","):
                continue
            if kind == "transcription" and fam == "deepseek" and not a.forms and not eligible(kind, form, fam):
                skipped.append(form)  # owner decision 2026-11-04: DeepSeek transcription only where it can earn credit
                continue
            jobs.append((kind, form))
    if skipped:
        print(f"skipped {len(skipped)} DeepSeek transcription form(s) not eligible for second-family credit "
              f"(name them with --forms to run anyway): {', '.join(skipped)}", flush=True)
    # classm.py rebuilds its own document's jobs under a lock. A redundant
    # all-document corpus here can exhaust the heap before any review starts.
    print(f"{len(jobs)} runs, {a.jobs} at a time", flush=True)
    results = []
    os.makedirs(os.path.dirname(a.summary), exist_ok=True)
    breaker = Breaker()
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        pending = [ex.submit(run, kind, form, a.model, a.resume, a.reasoning_effort, a.max_output_tokens, a.case_jobs, not a.no_carry, a.lines,
                             breaker) for kind, form in jobs]
        for future in as_completed(pending):
            res = future.result()
            results.append(res)
            tag = ("ok" if res["exit"] == 0 else "rule" if res["exit"] == 3 else "skip" if res.get("skipped")
                   else "LIMIT" if res.get("usage_limit") else f"EXIT {res['exit']}")
            print(f"[{tag:6s}] {res['kind']:13s} {res['form']:16s} {res['seconds']:4d}s  {res['last'][:110]}", flush=True)
            if res["stderr"]:
                print("         " + res["stderr"].replace("\n", "\n         "), flush=True)
            with open(a.summary + ".tmp", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=1)
            os.replace(a.summary + ".tmp", a.summary)
    skipped_jobs = [r for r in results if r.get("skipped")]
    bad = [r for r in results if r["exit"] not in (0, 3) and not r.get("skipped")]
    open_rulings = [r for r in results if r["exit"] == 3]
    print(f"\ndone: {len(results)} runs; {len(open_rulings)} with disagreements to rule on; {len(bad)} failed"
          + (f"; {len(skipped_jobs)} not run after a usage limit" if skipped_jobs else ""))
    print(skipped_report(results, a), end="")
    sys.exit(1 if bad or skipped_jobs else 0)


def skipped_report(results, a):
    """The jobs a usage limit stopped (the failed call and those never run), per family and kind, each
    group with the command that reruns it; '' when none."""
    groups = {}
    for r in results:
        if r.get("skipped") or r.get("usage_limit"):
            groups.setdefault((r["family"], r["kind"]), []).append(r["form"])
    if not groups:
        return ""
    out = ["", "Usage limit: these jobs did not complete; rerun them when the allowance resets:"]
    for (family, kind), forms in sorted(groups.items()):
        cmd = ["python3", "tools/transcription/rerun_all.py", "--kinds", kind, "--forms", ",".join(sorted(forms)),
               *YEAR_ARGS, *jurisdiction.J_ARGS, *(["--model", a.model] if a.model else []),
               *(["--lines", a.lines] if a.lines and kind in ("transcription", "render") else []),
               *(["--reasoning-effort", a.reasoning_effort] if a.reasoning_effort else []),
               *(["--max-output-tokens", str(a.max_output_tokens)] if a.max_output_tokens is not None else []),
               *(["--case-jobs", str(a.case_jobs)] if kind == "classm" and a.case_jobs != 1 else [])]
        out += [f"  {family} {kind} ({len(forms)}): {', '.join(sorted(forms))}", "    " + " ".join(cmd)]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    main()
