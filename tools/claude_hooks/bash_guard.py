#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Claude Code PreToolUse hook on Bash: refuses commands that break the project's process rules (project CLAUDE.md).

- `pgrep -f` matches the waiting shell's own command line, so a wait on it never ends. Wait on a pid, or poll
  `tools/check_all_bg.sh --status`, with a timeout.
- Review data (`.transcription/`, `.classm/`) is written only by its tools: a `cp`, `rsync`, `ditto` or `mv` whose
  target lies in it is refused (`tools/worktree_data.py` clone, fill and carry-back move it between worktrees).
  Copying out of it is allowed.

Text a command only writes or prints (heredoc bodies; quoted strings for the `pgrep` rule) is not judged. Reads the
hook payload on stdin; prints a deny decision, or nothing to let the call proceed.
"""
import json
import re
import shlex
import sys

PGREP_F = re.compile(r"\bpgrep\b(?:\s+-[A-Za-z]*\b)*?\s+-[A-Za-z]*f")
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?^\s*\2\s*$", re.S | re.M)
QUOTED = re.compile(r"'[^']*'|\"(?:\\.|[^\"\\])*\"")
SEGMENT = re.compile(r"&&|\|\||[;|\n&]")
COPIERS = {"cp", "rsync", "ditto", "mv"}
REVIEW_DATA = re.compile(r"(^|/)\.(transcription|classm)(/|$)")


def code(command):
    """The command without heredoc bodies and quoted strings: text a command only writes or prints is not run."""
    return QUOTED.sub("''", HEREDOC.sub("", command or ""))


def copy_targets(command):
    """The target path of each cp/rsync/ditto/mv in the command (heredoc bodies removed)."""
    out = []
    for seg in SEGMENT.split(HEREDOC.sub("", command or "")):
        try:
            argv = shlex.split(seg)
        except ValueError:
            continue
        while argv and ("=" in argv[0] and not argv[0].startswith("-") or argv[0] in ("sudo", "command", "nohup")):
            argv = argv[1:]
        if argv and argv[0] in COPIERS:
            paths = [a for a in argv[1:] if not a.startswith("-")]
            if len(paths) >= 2:
                out.append(paths[-1])
    return out


def decide(command):
    """The reason to refuse a command, or None."""
    if PGREP_F.search(code(command)):
        return ("`pgrep -f` matches the waiting shell's own command line, so the wait never ends. Wait on a pid "
                "(`ps -ax -o pid,command | grep ...` to find it once), or poll `tools/check_all_bg.sh --status`, "
                "always with a timeout (project CLAUDE.md, background waits).")
    into = [t for t in copy_targets(command) if REVIEW_DATA.search(t)]
    if into:
        return (f"review data is not copied by hand (target {into[0]}); use tools/worktree_data.py clone, fill or "
                "carry-back (project CLAUDE.md, worktrees).")
    return None


def main():
    payload = json.load(sys.stdin)
    why = decide((payload.get("tool_input") or {}).get("command", ""))
    if why:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                 "permissionDecisionReason": why}}))
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        cases = {"pgrep -f check_all": True, "while pgrep -lf foo; do sleep 5; done": True, "pgrep -x node": False,
                 "pgrep node": False, "ps -ax | grep pgrep": False, "echo 'pgrep -f is banned'": False,
                 "python3 - <<'EOF'\ns = 'never pgrep -f'\nEOF\n": False,
                 "cat > x <<EOF\npgrep -f y\nEOF\npgrep -f z": True,
                 "bash -c \"pgrep -f x\"": False,
                 "cp -R ../wt/.transcription/logs .transcription/": True,
                 "cd x && rsync -a a/ \"/repo/.classm/\"": True,
                 "cp .transcription/costs.jsonl /tmp/costs.jsonl": False,
                 "mv /tmp/x.json .transcription/completeness/x.json": True,
                 "cp a b && echo .transcription": False,
                 "python3 tools/worktree_data.py carry-back wt": False,
                 "cat > n.md <<'EOF'\ncp a .transcription/\nEOF\n": False}
        bad = [c for c, want in cases.items() if bool(decide(c)) != want]
        print("bash_guard self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
        sys.exit(1 if bad else 0)
    sys.exit(main())
