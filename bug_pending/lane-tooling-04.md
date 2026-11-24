## BUG-NEW-lane-tooling-04 — Closure: BUG-NEW-release-prep-04 is fixed: core.hooksPath is relative, so each worktree runs its own tree's hooks

- **Closes:** BUG-NEW-release-prep-04
- **Closure:** fixed
- **Caught by:** BUG-NEW-release-prep-04, recorded open; lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Reproduced:** git config --show-origin core.hooksPath gave the absolute path of the main checkout's tools/hooks, set in the clone's shared .git/config. No tool sets it: every instruction (tools/README.md, README.md, docs/TRUST.md, the hooks' own headers) says git config core.hooksPath tools/hooks, so the absolute value was set by hand.
- **Change:** the clone's config set to core.hooksPath tools/hooks (git config, once, in the shared .git/config; not a tracked file). tools/worktree_gc.py: check needs action (and so fails a release) while core.hooksPath is absolute (hooks_path_problem), with a self-test; tools/README.md says why the path is relative.
- **Evidence:** git resolves a relative hooksPath against the root of the worktree a command runs in: in a scratch clone with a linked worktree, a sentinel pre-commit hook ran from each tree's own tools/hooks, for a commit in the main checkout, in the worktree, in a subdirectory of it and with git -C. With the real hooks, git -c core.hooksPath=tools/hooks hook run pre-merge-commit ran this lane's hook in its worktree and the main checkout's in the main checkout (which, on main, refused as it should). Every hook cds to git rev-parse --show-toplevel first; tools/release.sh fast-forwards main with git -C <main worktree> merge --ff-only (runs no hook) and pushes with git push (pre-push from the tree it runs in, the release commit's), so none depends on an absolute path. The wave's git -c core.hooksPath=tools/hooks commit is now equivalent to a plain git commit.
- **Fix lines:** none (repository configuration; tool change: tools/worktree_gc.py)
- **Tags:** tool, hooks, worktrees, fixed
