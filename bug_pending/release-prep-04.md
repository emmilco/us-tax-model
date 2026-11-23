## BUG-NEW-release-prep-04 — core.hooksPath points every worktree at the main checkout's hooks

- **Date:** 2026-11-23
- **Caught by:** queue item 19 of .claude/wave-2026-11-22/after-int-queue.md; filed in release preparation.
- **Symptom:** The repository's local config (.git/config, shared by every worktree) sets core.hooksPath to the absolute path of the main checkout's tools/hooks, so a commit in any linked worktree runs the hooks of the main checkout's tree, which is on main and older than next until a release moves main. Commits on next and lane branches therefore have to be made with git -c core.hooksPath=tools/hooks commit to run their own tree's hooks.
- **Where:** the repository's core.hooksPath setting (shared by every worktree of the clone); tools/hooks.
- **Proposed fix:** set core.hooksPath to the relative path tools/hooks (resolved in each worktree), or have the worktree tools set it per worktree (extensions.worktreeConfig), with a check in tools/worktree_gc.py or preflight that the hooks a commit runs are its own tree's.
- **Severity:** low
- **Tags:** tool, hooks, worktrees; open
