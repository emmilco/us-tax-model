#!/usr/bin/env python3
"""Fold finished agent-run rows from the pending file into the tracked ledger.

    agent_runs_fold.py [--dry-run] [--if-main]
    agent_runs_fold.py --self-test

The Claude Code hook (tools/claude_hooks/agents.py) writes each agent run's row to the untracked pending file
<git common dir>/agent-runs/pending.jsonl and totals it when the agent stops. This tool moves the finished rows (those
with `tool_uses`) to the end of research/costs/agent_runs.jsonl, in the same format, and removes them from the pending
file; a row whose `agent_id` the ledger already holds is removed without being appended again. Unfinished rows stay
pending. It runs under the hook's lock on the pending file.

It refuses (exit 1) unless the branch checked out is next (in any worktree: a branch is checked out in one at most) or
main (in the clone's main worktree): a lane branch never gains ledger rows, which would conflict when it merges.
--if-main makes that case a silent no-op (exit 0), for
tools/check_all.sh and tools/check_all_bg.sh, which fold before taking the tree they test. --dry-run reports what
would move and changes nothing.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_hooks"))
import agents  # noqa: E402


def main_worktree_on_main(root):
    """None when root is on the branch next, or in the clone's main worktree on the branch main, else the reason it
    is neither."""
    git_dir, common = agents.git(root, "rev-parse", "--absolute-git-dir"), agents.git(root, "rev-parse", "--git-common-dir")
    if git_dir is None or common is None:
        return f"{root} is not in a git repository"
    branch = agents.git(root, "symbolic-ref", "-q", "HEAD")
    if branch == "refs/heads/next":
        return None
    if os.path.realpath(git_dir) != os.path.realpath(os.path.join(root, common)):
        return "this is a linked worktree not on the branch next"
    if branch != "refs/heads/main":
        return f"HEAD is {branch or 'detached'}, not the branch main or next"
    return None


def split(pending_rows, ledger_ids):
    """(rows to append, rows to keep pending, finished rows already in the ledger)."""
    move, keep, dup = [], [], []
    seen = set(ledger_ids)
    for r in pending_rows:
        if not agents.is_finished(r):
            keep.append(r)
        elif r.get("agent_id") in seen:
            dup.append(r)
        else:
            move.append(r)
            seen.add(r.get("agent_id"))
    return move, keep, dup


def fold(root, dry_run=False):
    """Fold root's pending rows into its ledger; returns (moved, kept, duplicates) counts."""
    pending, ledger = agents.pending(root), agents.tracked_ledger(root)
    if os.path.realpath(pending) == os.path.realpath(ledger):
        raise SystemExit("agent runs fold: no git common dir; nothing to fold")
    result = {}

    def apply(rows):
        ids = {r.get("agent_id") for r in agents.read_rows(ledger) if r.get("agent_id")}
        move, keep, dup = split(rows, ids)
        result["counts"] = len(move), len(keep), len(dup)
        if dry_run or not (move or dup):
            return False
        if move:
            with open(ledger, "a", encoding="utf-8") as f:
                f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in move)
        rows[:] = keep
        return None

    if not os.path.exists(pending):
        return 0, 0, 0
    agents.locked_rows(apply, pending)
    return result["counts"]


def self_test():
    bad = []
    row = lambda aid, done: {"date": "2026-11-20", "package": aid, "description": aid, "model": "claude-opus-5-5",
                             "class": "judgment", "year": 2025, "jurisdiction": "us", "agent_id": aid,
                             "source": "agent hook", **({"usage": {"output_tokens": 1}, "tool_uses": 3,
                                                         "duration_ms": 10} if done else {})}
    env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    d = os.path.realpath(tempfile.mkdtemp())
    try:
        repo = os.path.join(d, "repo")
        os.makedirs(os.path.join(repo, "research", "costs"))
        ledger = agents.tracked_ledger(repo)
        agents.write_rows(ledger, [row("old", True)])
        run = lambda *a: subprocess.run(["git", "-C", repo, *a], check=True, capture_output=True,
                                        env={**{k: v for k, v in os.environ.items() if not k.startswith("GIT_")}, **env})
        run("init", "-q", "-b", "main")
        run("add", "-A")
        run("commit", "-q", "-m", "init")
        pending = agents.pending(repo)
        if pending != os.path.join(repo, ".git", "agent-runs", "pending.jsonl"):
            bad.append(("pending path", pending))
        os.makedirs(os.path.dirname(pending), exist_ok=True)
        agents.write_rows(pending, [row("a", True), row("b", False), row("old", True), row("c", True)])
        before = open(ledger).read(), open(pending).read()
        if fold(repo, dry_run=True) != (2, 1, 1) or (open(ledger).read(), open(pending).read()) != before:
            bad.append(("dry run", open(ledger).read()))
        if fold(repo) != (2, 1, 1):
            bad.append("counts")
        ids = [r["agent_id"] for r in agents.read_rows(ledger)]
        if ids != ["old", "a", "c"] or agents.read_rows(ledger)[1] != row("a", True):
            bad.append(("ledger after fold", ids))
        if [r["agent_id"] for r in agents.read_rows(pending)] != ["b"]:
            bad.append(("pending after fold", agents.read_rows(pending)))
        agents.locked_rows(lambda rows: rows.__setitem__(0, row("b", True)), pending)
        agents.locked_rows(lambda rows: rows.append(row("a", True)), pending)
        fold(repo)
        if [r["agent_id"] for r in agents.read_rows(ledger)] != ["old", "a", "c", "b"] or agents.read_rows(pending):
            bad.append(("second fold", agents.read_rows(ledger), agents.read_rows(pending)))
        if main_worktree_on_main(repo) is not None:
            bad.append(("main worktree on main refused", main_worktree_on_main(repo)))
        run("worktree", "add", "-q", "-b", "main-lane", os.path.join(d, "lane"))
        why = main_worktree_on_main(os.path.join(d, "lane"))
        if not why or "linked worktree" not in why:
            bad.append(("linked worktree", why))
        if main([os.path.join(d, "lane"), "--if-main"]) != 0 or main([os.path.join(d, "lane")]) != 1:
            bad.append("exit codes in a linked worktree")
        run("checkout", "-q", "-b", "lane")
        why = main_worktree_on_main(repo)
        if not why or "not the branch main" not in why:
            bad.append(("branch", why))
        agents.write_rows(pending, [row("z", True)])
        if main([repo]) != 1 or agents.read_rows(pending) != [row("z", True)]:
            bad.append("a fold off main moved rows")
        run("-C", os.path.join(d, "lane"), "checkout", "-q", "-b", "next")
        if main_worktree_on_main(os.path.join(d, "lane")) is not None or main([os.path.join(d, "lane")]) != 0 \
                or agents.read_rows(pending):
            bad.append(("a linked worktree on next did not fold", main_worktree_on_main(os.path.join(d, "lane"))))
    finally:
        shutil.rmtree(d, ignore_errors=True)
    print("agent runs fold self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", nargs="?", help=argparse.SUPPRESS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--if-main", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    root = a.root or agents.git(os.getcwd(), "rev-parse", "--show-toplevel") or os.getcwd()
    why = main_worktree_on_main(root)
    if why:
        if a.if_main:
            return 0
        print(f"agent runs fold: refused: {why} (rows are folded only on next, or in the main worktree on main)", file=sys.stderr)
        return 1
    moved, kept, dup = fold(root, a.dry_run)
    verb = "would fold" if a.dry_run else "folded"
    print(f"agent runs fold: {verb} {moved} finished row(s) into research/costs/agent_runs.jsonl"
          + (f", {'would drop' if a.dry_run else 'dropped'} {dup} already there" if dup else "")
          + f"; {kept} unfinished row(s) pending in {agents.pending(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
