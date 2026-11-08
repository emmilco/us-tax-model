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

Guards, applied before any paid call:

- Once per form per round: a job whose log already answers the current subject (subjects.log_state is
  None: nothing it judged has changed) is not run. --force-rerun REASON runs it; the reason is recorded
  in the summary row and, through REVIEW_RERUN_REASON, in each paid call's cost-ledger row.
- Line-scoped by default: transcription and render run with --lines auto. A job runs whole when the
  tool reports that line scoping is impossible (no log or no line subjects to merge into, a change
  outside every compared line, a form with partial-input cases), when --whole is given, or for a
  forced rerun of a current log (no stale line to scope to); --lines names the lines explicitly.
- Cost estimate: each job is first run with the tool's --dry-run, which builds the request it would
  send (and refuses line scoping where the tool would); the prompt size is priced at the recent cost per
  prompt character of the same tool and model family in the cost ledger (.transcription/costs.jsonl).
  The estimate is printed per job and in total. A job whose saved response --resume would reuse is
  still counted.
- Owner gate: a run whose estimate exceeds COST_GATE_USD, or that includes calls the ledger cannot
  price, is refused unless --approve-cost DOLLARS is at least the estimate.

--dry-run plans and prints the estimate and calls no model.
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
COST_GATE_USD = 3.00     # an estimated run above this needs --approve-cost
PRICE_SAMPLE = 30        # recent ledger calls per (tool, family) that set the price per prompt character
REASON_ENV = "REVIEW_RERUN_REASON"   # transcribe.record_cost writes it into the ledger row
LINE_SCOPED = ("transcription", "render")
PROMPT = re.compile(r"prompt ([\d,]+) chars")
# A tool's refusal of a line-scoped review: the review must run whole.
WHOLE_NEEDED = re.compile(r"run the whole review|is reviewed whole|records no line subjects")


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


def tool_cmd(kind, form, model):
    script, flag = TOOLS[kind]
    return [sys.executable, os.path.join(HERE, script), flag, form, *YEAR_ARGS, *jurisdiction.J_ARGS] + (["--model", model] if model else [])


def run(kind, form, model, resume=False, reasoning_effort=None, max_output_tokens=None, case_jobs=1, carry=True, lines=None,
        breaker=None, reason=None):
    family = families.family_of(model) if model else families.DEFAULT
    cmd = tool_cmd(kind, form, model)
    env = {**os.environ, REASON_ENV: reason} if reason else None
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
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, env=env)
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
    if lines and kind in LINE_SCOPED:
        out["lines"] = lines
    if reason:
        out["forced"] = reason
    return out


# ---------------------------------------------------------------- guards

def answered(kind, form, family):
    """The log's reason to rerun (subjects.log_state), None when it already answers the current subject,
    or "no log" when there is none."""
    import rulings
    import subjects
    path = rulings.log_path(kind, form, family)
    if not os.path.exists(path):
        return "no log"
    try:
        return subjects.log_state(kind, form, Y, open(path, encoding="utf-8").read())
    except Exception as ex:  # a log or document the subject code cannot read is treated as stale
        return f"state unreadable ({type(ex).__name__}: {ex})"


def prices(ledger=None):
    """{(tool, family): estimated USD per prompt character} over the most recent PRICE_SAMPLE priced,
    successful calls of each tool and family in the cost ledger."""
    import costs
    import transcribe
    rows, _ = costs.read(ledger or os.path.join(transcribe.RAW, transcribe.LEDGER_NAME))
    groups = {}
    for r in rows:
        if r.get("outcome") == "ok" and r.get("estimated_cost_usd") is not None and (r.get("prompt_chars") or 0) > 0:
            groups.setdefault((r.get("tool"), families.family_of(r.get("model_requested") or "-")), []).append(r)
    out = {}
    for key, rs in groups.items():
        rs = sorted(rs, key=lambda r: r.get("timestamp", ""))[-PRICE_SAMPLE:]
        out[key] = sum(r["estimated_cost_usd"] for r in rs) / sum(r["prompt_chars"] for r in rs)
    return out


def dry_run(kind, form, model, lines):
    """(prompt characters the tool would send, or None when it refuses, its last output line)."""
    cmd = tool_cmd(kind, form, model) + ["--dry-run"] + (["--lines", lines] if lines else [])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    text = r.stdout + "\n" + r.stderr
    last = (text.strip().splitlines() or [""])[-1]
    if r.returncode != 0:
        return None, last
    return sum(int(n.replace(",", "")) for n in PROMPT.findall(r.stdout)), last


def plan_job(kind, form, model, lines=None, whole=False, force=None, price=None):
    """What a job would do, from the guards: {kind, form, family, state, run, lines, chars, usd, note}.
    `run` is False for a job refused by the once-per-round guard or one whose request cannot be built."""
    family = families.family_of(model) if model else families.DEFAULT
    state = answered(kind, form, family)
    job = {"kind": kind, "form": form, "family": family, "state": state or "current", "run": True,
           "lines": None, "chars": 0, "usd": 0.0, "note": "", "answered": False}
    if state is None and not force:
        job.update(run=False, answered=True, note="its log already answers the current subject; --force-rerun REASON to run it")
        return job
    # A forced rerun of a log that answers its subject has no stale line to scope to: it runs whole
    # unless lines are named.
    if kind in LINE_SCOPED and not whole and state != "no log" and (state is not None or lines):
        asked = lines or "auto"
        chars, last = dry_run(kind, form, model, asked)
        if chars is not None:
            job.update(lines=asked, chars=chars, note=last if not chars else "line-scoped")
        elif lines or not WHOLE_NEEDED.search(last):
            job.update(run=False, note=f"line-scoped request not built: {last}")
            return job
        else:
            job["note"] = f"whole: {last}"
    if job["lines"] is None:
        chars, last = dry_run(kind, form, model, None)
        if chars is None:
            job.update(run=False, note=f"request not built: {last}")
            return job
        job["chars"] = chars
        job["note"] = job["note"] or ("whole (asked)" if whole and kind in LINE_SCOPED else "whole")
    rate = (price or {}).get((os.path.basename(TOOLS[kind][0]), family))
    job["usd"] = None if job["chars"] and rate is None else job["chars"] * (rate or 0)
    return job


def gate(planned, approve):
    """None when the run may proceed, else the refusal: an estimate above COST_GATE_USD, or calls the
    ledger cannot price, need --approve-cost of at least the estimate."""
    total = sum(j["usd"] or 0 for j in planned if j["run"])
    unpriced = [j for j in planned if j["run"] and j["usd"] is None]
    if unpriced and approve is None:
        return (f"{len(unpriced)} job(s) have no ledger price for their tool and family "
                f"({', '.join(j['kind'] + ' ' + j['form'] for j in unpriced)}); pass --approve-cost DOLLARS to run them")
    if total > COST_GATE_USD and (approve is None or approve < total):
        return (f"estimated ${total:.2f} exceeds the ${COST_GATE_USD:.2f} gate; pass --approve-cost {total:.2f} "
                "(or more) to run it")
    return None


def estimate_report(planned):
    out = ["Cost estimate (dry-run request size x recent ledger cost per prompt character):"]
    for j in sorted(planned, key=lambda j: (j["kind"], j["form"])):
        usd = "unpriced" if j["usd"] is None else f"${j['usd']:.2f}"
        what = "not run" if not j["run"] else f"--lines {j['lines']}" if j["lines"] else "whole"
        out.append(f"  {j['kind']:13s} {j['form']:16s} {j['family']:9s} {what:20s} {j['chars']:>10,} chars  {usd:>9s}  {j['note'][:90]}")
    total = sum(j["usd"] or 0 for j in planned if j["run"])
    out.append(f"  total ${total:.2f} for {sum(j['run'] for j in planned)} job(s); gate ${COST_GATE_USD:.2f}")
    return "\n".join(out) + "\n"


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
    ap.add_argument("--lines", help="the lines of line-scoped transcription and render reviews (default auto: the lines whose "
                                    "subject changed)")
    ap.add_argument("--whole", action="store_true", help="review transcription and render whole, not line-scoped")
    ap.add_argument("--force-rerun", metavar="REASON", help="also run jobs whose log already answers the current subject; "
                    "the reason is recorded in the summary and the cost ledger")
    ap.add_argument("--approve-cost", metavar="DOLLARS", type=float, help="run although the estimate exceeds the "
                    f"${COST_GATE_USD:.2f} gate or includes unpriced calls; must be at least the estimate")
    ap.add_argument("--dry-run", action="store_true", help="plan and print the cost estimate; call no model")
    ap.add_argument("--ledger", help="cost ledger that prices the estimate (default .transcription/costs.jsonl)")
    ap.add_argument("--no-carry", action="store_true", help="do not carry earlier rulings over to repeat disagreements (carry.py)")
    ap.add_argument("--summary", default=os.path.join(ROOT, ".transcription", "rerun_summary.json"))
    a = ap.parse_args()
    if a.jobs < 1:
        ap.error("--jobs must be positive")
    if a.force_rerun is not None and not a.force_rerun.strip():
        ap.error("--force-rerun needs a reason")
    if a.whole and a.lines:
        ap.error("--whole and --lines exclude each other")
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
    price = prices(a.ledger)
    print(f"planning {len(jobs)} job(s): dry runs build each request, {a.jobs} at a time", flush=True)
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        planned = list(ex.map(lambda j: plan_job(*j, a.model, a.lines, a.whole, a.force_rerun, price), jobs))
    print(estimate_report(planned), end="", flush=True)
    current = [j for j in planned if j["answered"]]
    unbuilt = [j for j in planned if not j["run"] and not j["answered"]]
    if current:
        print(f"not run, once per form per round: {len(current)} job(s) whose log already answers the current subject "
              f"({', '.join(j['kind'] + ' ' + j['form'] for j in current)}); --force-rerun REASON runs them", flush=True)
    if unbuilt:
        print(f"not run: {len(unbuilt)} job(s) whose request could not be built: "
              + "; ".join(f"{j['kind']} {j['form']}: {j['note']}" for j in unbuilt), flush=True)
    if a.dry_run:
        print("dry run: no model called")
        sys.exit(0)
    refusal = gate(planned, a.approve_cost)
    if refusal:
        print("refused: " + refusal, flush=True)
        sys.exit(2)
    todo = [j for j in planned if j["run"]]
    print(f"{len(todo)} runs, {a.jobs} at a time", flush=True)
    results = []
    os.makedirs(os.path.dirname(a.summary), exist_ok=True)
    breaker = Breaker()
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        pending = [ex.submit(run, j["kind"], j["form"], a.model, a.resume, a.reasoning_effort, a.max_output_tokens, a.case_jobs,
                             not a.no_carry, j["lines"], breaker, a.force_rerun if j["state"] == "current" else None)
                   for j in todo]
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
    sys.exit(1 if bad or skipped_jobs or unbuilt else 0)


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
