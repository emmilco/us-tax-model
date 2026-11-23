#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Claude Code hooks on agent launches: the brief states model and class, mechanical work runs on Sonnet and judgment
on Opus (Fable may run either class; Sonnet may run adjudication), and every run gets its row in the pending file
<git common dir>/agent-runs/pending.jsonl, untracked, from which tools/agent_runs_fold.py moves finished rows into the
tracked ledger research/costs/agent_runs.jsonl (checked by tools/check_agent_runs.py).

- PreToolUse on Agent: refuses a launch without an explicit `model`, or whose prompt lacks the lines
  `Class: mechanical|judgment`, `Year: <tax year>` and `Jurisdiction: us|ny`; refuses mechanical work on a model other
  than Sonnet and judgment work on a model other than Opus; Fable is allowed for both classes. A judgment brief with the
  line `Work: adjudication` (ruling review findings against the sources) may also run on Sonnet (owner, 2026-11-21).
- PostToolUse on Agent: appends the run's row (date, description, model, class, year, jurisdiction, agent_id) to the
  pending file.
- SubagentStop: totals the token usage, tool uses and duration in the agent's transcript into its pending row; a row
  with `tool_uses` is finished, and only finished rows are folded.

Reads the hook payload on stdin. The pending file is found from $CLAUDE_PROJECT_DIR (or the working directory) with
`git rev-parse --git-common-dir`, so every worktree of the clone shares it and no hook writes a tracked file; when git
cannot resolve a common dir, rows go to the tracked ledger instead.
"""
import datetime
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

FIELDS = {"class": re.compile(r"\bClass:\**\s*(mechanical|judgment)\b", re.I),
          "year": re.compile(r"\bYear:\**\s*(\d{4})\b", re.I),
          "jurisdiction": re.compile(r"\bJurisdiction:\**\s*(us|ny)\b", re.I)}
FAMILY = {"mechanical": "sonnet", "judgment": "opus"}
ANY_CLASS = ("fable",)  # models allowed for either class
ADJUDICATION = re.compile(r"\bWork:\**\s*adjudication\b", re.I)  # judgment work Sonnet may also run


def project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def tracked_ledger(root=None):
    """The tracked ledger of a checkout."""
    return os.path.join(root or project_dir(), "research", "costs", "agent_runs.jsonl")


def git(root, *args):
    """`git -C root args` (stdout stripped), or None when git is missing or fails. Git's location variables are
    dropped so that `root` alone decides the repository."""
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE")}
    try:
        out = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=30, env=env)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def pending(root=None):
    """The pending file: <git common dir of root>/agent-runs/pending.jsonl, or the tracked ledger when git cannot
    resolve a common dir."""
    root = root or project_dir()
    common = git(root, "rev-parse", "--git-common-dir")
    if not common:
        return tracked_ledger(root)
    return os.path.join(os.path.realpath(os.path.join(root, common)), "agent-runs", "pending.jsonl")


def ledger():
    """Where the hook writes rows."""
    return pending()


def read_rows(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()] if os.path.exists(path) else []


def write_rows(path, rows):
    with open(path + ".tmp", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    os.replace(path + ".tmp", path)


def is_finished(row):
    """Whether SubagentStop has totalled the row."""
    return "tool_uses" in row


def brief(prompt):
    """{class, year, jurisdiction} found in a prompt (missing ones absent)."""
    out = {}
    for k, rx in FIELDS.items():
        m = rx.search(prompt or "")
        if m:
            out[k] = int(m.group(1)) if k == "year" else m.group(1).lower()
    return out


def refusal(tool_input):
    """The reason to refuse a launch, or None."""
    model = (tool_input.get("model") or "").lower()
    got = brief(tool_input.get("prompt"))
    missing = [k for k in FIELDS if k not in got]
    problems = []
    if not model:
        problems.append("no explicit `model` (sonnet for mechanical work, opus for judgment)")
    if missing:
        problems.append("the brief lacks the line(s) " + ", ".join(f"`{k.capitalize()}:`" for k in missing)
                        + " (Class: mechanical|judgment, Year: <tax year>, Jurisdiction: us|ny)")
    adjudication = got.get("class") == "judgment" and "sonnet" in model and ADJUDICATION.search(tool_input.get("prompt") or "")
    if (model and "class" in got and FAMILY[got["class"]] not in model and not any(m in model for m in ANY_CLASS)
            and not adjudication):
        problems.append(f"{got['class']} work runs on {FAMILY[got['class']]}, not {model}")
    if not problems:
        return None
    return "Agent launch refused (project CLAUDE.md, cost rules): " + "; ".join(problems) + "."


def locked_rows(fn, path=None):
    """Apply fn to the rows (a list of dicts) of path (the hook's file by default) under a lock and write them back,
    unless fn returns False."""
    path = os.path.realpath(path or ledger())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # The lock lives outside the working tree, so it is never committed: one per file path.
    lock_path = os.path.join(tempfile.gettempdir(), "agent_runs-" + hashlib.sha256(path.encode()).hexdigest()[:16] + ".lock")
    with open(lock_path, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        rows = read_rows(path)
        if fn(rows) is False:
            return
        write_rows(path, rows)


def launched(payload):
    """The ledger row of a launch (PostToolUse on Agent)."""
    ti, tr = payload.get("tool_input") or {}, payload.get("tool_response") or {}
    tr = tr if isinstance(tr, dict) else {}
    got = brief(ti.get("prompt"))
    row = {"date": datetime.date.today().isoformat(), "package": re.sub(r"[^a-z0-9]+", "-", (ti.get("description") or "agent").lower()).strip("-"),
           "description": ti.get("description") or "", "model": tr.get("resolvedModel") or ti.get("model"),
           "class": got.get("class"), "year": got.get("year"), "jurisdiction": got.get("jurisdiction"),
           "agent_id": tr.get("agentId") or tr.get("agent_id"), "source": "agent hook"}
    usage = tr.get("usage")
    if isinstance(usage, dict):
        row["usage"] = usage
    return row


def transcript_totals(path):
    """(usage totals, tool uses, duration in ms) over an agent transcript (JSONL of messages)."""
    usage, tools, stamps = {}, 0, []
    for line in open(path, encoding="utf-8"):
        try:
            m = json.loads(line)
        except json.JSONDecodeError:
            continue
        if m.get("timestamp"):
            stamps.append(m["timestamp"])
        msg = m.get("message") or {}
        if m.get("type") == "assistant" and isinstance(msg, dict):
            for k, v in (msg.get("usage") or {}).items():
                if isinstance(v, int):
                    usage[k] = usage.get(k, 0) + v
            tools += sum(1 for c in msg.get("content") or [] if isinstance(c, dict) and c.get("type") == "tool_use")
    ms = None
    if len(stamps) >= 2:
        t = sorted(datetime.datetime.fromisoformat(s.replace("Z", "+00:00")) for s in stamps)
        ms = int((t[-1] - t[0]).total_seconds() * 1000)
    return usage, tools, ms


def finished(payload, rows):
    """Fill the finished agent's row (SubagentStop) with its transcript's totals; False when no row is its."""
    aid, path = payload.get("agent_id"), payload.get("agent_transcript_path")
    row = next((r for r in reversed(rows) if aid and r.get("agent_id") == aid), None)
    if row is None or not path or not os.path.exists(path):
        return False
    row["usage"], row["tool_uses"], row["duration_ms"] = transcript_totals(path)
    return None


def main():
    payload = json.load(sys.stdin)
    event = payload.get("hook_event_name")
    if event == "PreToolUse":
        why = refusal(payload.get("tool_input") or {})
        if why:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                     "permissionDecisionReason": why}}))
    elif event == "PostToolUse":
        row = launched(payload)
        locked_rows(lambda rows: rows.append(row))
    elif event == "SubagentStop":
        locked_rows(lambda rows: finished(payload, rows))
    return 0


def self_test():
    import tempfile
    from unittest import mock
    bad = []
    ok = "do it\nClass: mechanical\nYear: 2025\nJurisdiction: us\n"
    cases = [({"model": "sonnet", "prompt": ok}, None), ({"prompt": ok}, "no explicit"),
             ({"model": "opus", "prompt": ok}, "mechanical work runs on sonnet"),
             ({"model": "opus", "prompt": "Model: x. Class: judgment. Year: 2025. Jurisdiction: us."}, None),
             ({"model": "opus", "prompt": "Class: judgment. Jurisdiction: us."}, "`Year:`"),
             ({"model": "opus", "prompt": "**Class:** judgment\n**Year:** 2025\n**Jurisdiction:** ny"}, None),
             ({"model": "sonnet", "prompt": "Class: judgment\nYear: 2025\nJurisdiction: us"}, "judgment work runs on opus"),
             ({"model": "fable", "prompt": "Class: judgment\nYear: 2025\nJurisdiction: us"}, None),
             ({"model": "sonnet", "prompt": "Class: judgment\nWork: adjudication\nYear: 2025\nJurisdiction: us"}, None),
             ({"model": "sonnet", "prompt": "Class: mechanical\nWork: adjudication\nYear: 2025\nJurisdiction: us"}, None),
             ({"model": "haiku", "prompt": "Class: judgment\nWork: adjudication\nYear: 2025\nJurisdiction: us"},
              "judgment work runs on opus"),
             ({"model": "fable", "prompt": ok}, None),
             ({"model": "fable", "prompt": "Class: judgment. Jurisdiction: us."}, "`Year:`")]
    for ti, want in cases:
        got = refusal(ti)
        if (want is None) != (got is None) or (want and want not in got):
            bad.append((ti, got))
    launch = {"tool_input": {"description": "Rule claims", "model": "opus",
                             "prompt": "Class: judgment\nYear: 2025\nJurisdiction: us"},
              "tool_response": {"status": "async_launched", "agentId": "a1", "resolvedModel": "claude-opus-5-5"}}
    want = {"model": "claude-opus-5-5", "class": "judgment", "year": 2025, "jurisdiction": "us", "agent_id": "a1",
            "usage": {"input_tokens": 20, "output_tokens": 10}, "tool_uses": 2, "duration_ms": 30000}
    for repo in (True, False):
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(os.environ, {"CLAUDE_PROJECT_DIR": d}):
            d = os.path.realpath(d)
            if repo and git(d, "init", "-q") is None:
                bad.append(("git init", d))
                continue
            expect = os.path.join(d, ".git", "agent-runs", "pending.jsonl") if repo else tracked_ledger(d)
            if os.path.realpath(ledger()) != expect:
                bad.append(("path", repo, ledger(), expect))
                continue
            locked_rows(lambda rows: rows.append(launched(launch)))
            rows = read_rows(expect)
            if len(rows) != 1 or is_finished(rows[0]):
                bad.append(("launch row", repo, rows))
            tp = os.path.join(d, "t.jsonl")
            with open(tp, "w") as f:
                for ts in ("2026-11-10T10:00:00Z", "2026-11-10T10:00:30Z"):
                    f.write(json.dumps({"type": "assistant", "timestamp": ts, "message": {
                        "usage": {"input_tokens": 10, "output_tokens": 5}, "content": [{"type": "tool_use"}]}}) + "\n")
            locked_rows(lambda rows: finished({"agent_id": "a1", "agent_transcript_path": tp}, rows))
            rows = read_rows(expect)
            if len(rows) != 1 or not is_finished(rows[0]) or any(rows[0].get(k) != v for k, v in want.items()):
                bad.append(("stopped row", repo, rows))
            if repo and os.path.exists(tracked_ledger(d)):
                bad.append(("the hook wrote the tracked ledger in a repository", d))
    print("agents hook self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())
