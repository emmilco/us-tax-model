# Process rules sweep (phase 2, step 0)

Charter section 5: every process rule is either enforced by a tool or marked advisory; no new prose-only rules.
This sweep lists the process rules stated in prose in the controlling documents and says, for each, what enforces
it today and what could. It is the input to the phase 2 plan; the charter's section 5 table is updated only after
the owner has reviewed it.

**Documents read:** `CLAUDE.md` (project), `handoffs/HANDOFF-HARDENING-1.md`, `HANDOFF-NEXT-SESSION.md` (both
entries, including the process lessons of 2026-11-09/10), `docs/consolidation_charter.md`,
`docs/2026-10-24_validation_policy.md`, `tools/README.md`, `tools/transcription/README.md` (searched for normative
wording, not read in full). Historical handoffs were not read: a rule from them counts only if it was carried
forward.

**Status codes:**
- **E**: enforced by a tool (checked in the code named).
- **P**: partly enforced; the gap is stated.
- **H**: not enforced; mechanically detectable, so a hook or check could enforce it.
- **A**: not enforced and judgment-bound; proposed to be marked advisory.

"Checked" means I read the enforcing code or ran a search for it this session. "Unverified" means it is relayed
from the documents.

## 1. The charter's open rows (already in the phase 2 plan)

| # | Rule | Source | Status | Proposal |
|---|---|---|---|---|
| 1.1 | Completeness and screen reruns: once per round, cost estimate, $3 gate | charter 5; CLAUDE.md | H (checked: neither tool has `--approve-cost` or `--force-rerun`) | Guards in the tools themselves, sharing `prices()`/`gate()` with `rerun_all.py`. See conflict 4.1 |
| 1.2 | Background waits: never `pgrep -f`; wait on a pid or `check_all_bg.sh --status`; always with a timeout; one wait per task | CLAUDE.md; charter 5 | H for `pgrep -f`; A for "timeout" and "one wait per task" | Claude hook on Bash (`tools/claude_hooks/`) refusing `pgrep -f`. A timeout check is possible only for simple forms (`until`/`while` loops without `timeout`); proposed advisory |
| 1.3 | Agent brief states model and class; mechanical work on Sonnet; `agent_runs.jsonl` row with model, class, year, jurisdiction | CLAUDE.md; charter 5 | P (checked: `check_agent_runs.py` validates rows that exist; nothing makes a row exist or checks the launch) | Claude hooks on the Agent tool: PreToolUse requires `model` and `Class:`/`Year:`/`Jurisdiction:` lines, Sonnet for mechanical; PostToolUse appends the row |
| 1.4 | Two lanes never edit the same form at once | charter 5 | H | Form-claim registry in the git common dir, checked by `pre-commit`; a merge releases the merged branch's claims (owner, 2026-11-10: option a) |

## 2. Rules found by the sweep

| # | Rule | Source | Status | Proposal |
|---|---|---|---|---|
| 2.1 | Rebuild (`npm run compile`, `build`, `render`, `render --ny`) on main after every merge before review checks or triage | handoff 11-09/10 lessons | H (checked: no freshness check in `triage.py`, `check_completeness.py`, `check_screens.py`) | A build stamp: `build` records the source tree hash it built from in `canonical/`; triage and the review checks refuse when it differs from the current sources. Two false failures came from this |
| 2.2 | Renumber BUG ids in a branch commit before merging, not in the merge commit | handoff 11-09/10 lessons | P (checked: `check_bug_inventory.py` fails on repeated or gapped ids, so a collision is caught; nothing stops the renumber being done inside the merge commit) | `pre-commit` on a merge: refuse when the merge result renames a `## BUG-NNNN` heading that either parent introduced |
| 2.3 | A merge commit equals the tested tree | handoff 11-09/10 lessons | E (`tools/hooks/pre-commit`, MERGE_HEAD handled) | None; the lesson is how to satisfy the hook. Move it to `tools/README.md` |
| 2.4 | Only one check-all run per clone | handoff 11-09/10 lessons | E (unverified: the handoff reports refused starts) | None |
| 2.5 | Don't run `tools/check_all_bg.sh --help` (it starts a run) | handoff "what not to redo" | H (checked: no `--help` case at line 171) | Fix the tool: `--help`/`-h` print usage and exit. A bug, not a rule |
| 2.6 | Wait on the detached runner, not the launcher pid | handoff "what not to redo" | H | Have `check_all_bg.sh` print the runner pid (or write it to the status record) so the right pid is the one shown. Unverified whether it already prints it |
| 2.7 | Verify agents' claims of check-all status by reading the status and log yourself | handoff "what not to redo" | A | Advisory. Partly covered by 1.3 (a ledger row per run) and by `commit_tested.sh` refusing non-green trees |
| 2.8 | Review data is never copied by hand (`.transcription/`, `.classm/`) | CLAUDE.md worktrees | P (checked: the tool exists; a hand `cp` is not blocked) | Claude hook on Bash refusing `cp`/`rsync`/`ditto` whose source or target names `.transcription` or `.classm` |
| 2.9 | A file changed on both sides is taken from the worktree only with `--prefer-worktree`, after checking which copy the logs were written from | CLAUDE.md worktrees | P (the flag is required by the tool; "after checking" is judgment) | Advisory for the check; the flag is enforced |
| 2.10 | One review per form per round, run after all of that form's fixes landed | CLAUDE.md cost rules | P (once-per-subject enforced by `rerun_all.py`; "after all fixes landed" is judgment) | Advisory for the timing |
| 2.11 | A round whose reviews find only lows starts no further round | CLAUDE.md; HARDENING-1 | A | Advisory. A check would need a notion of "round"; not worth building |
| 2.12 | Adjudicate only forms whose content changed; review-prompt changes apply prospectively, no global re-review | CLAUDE.md cost rules | P for the review kinds `rerun_all.py` guards; see conflict 4.2 for completeness | Settle 4.2 |
| 2.13 | Every paid review call logged with year and jurisdiction | CLAUDE.md | E (checked: `transcribe.py` appends every call to `costs.jsonl`; year/jurisdiction fields unverified) | Confirm the fields are required by a check; if not, extend `check_agent_runs.py`'s pattern to `costs.jsonl` |
| 2.14 | A defect introduced by the change being prepared is fixed before that change is committed | HARDENING-1 (owner, 10-31) | A | Advisory: deciding what the change introduced is judgment |
| 2.15 | Only one agent owns new inputs and their ripple | HARDENING-1 | H | Fold into 1.4: the registry also takes claims on "inputs" (one global claim) |
| 2.16 | Human verdicts are preserved; never rewritten or signed on the owner's behalf | validation policy | P (unverified: the archive holds hashes; no check found by name search) | A check that the archived originals still match their recorded hashes, if one does not exist. Low priority: nothing has touched them |
| 2.17 | `HANDOFF-NEXT-SESSION.md` keeps the latest two entries; older ones go to the monthly archive | charter 6 | H (currently satisfied: 2 entries) | A docs-tier check counting top-level entries |
| 2.18 | Docs are dated `YYYY-MM-DD_` unless they are listed living documents | charter 6 | H | A docs-tier check against a list of living documents |
| 2.19 | Push and release tags only from green trees | `tools/README.md` | E (`tools/hooks/pre-push`) | None |
| 2.20 | Baselines and held-leak templates only shrink; obsolete exceptions are removed | HARDENING-1; charter 3 | E | None |
| 2.21 | A new input ripples to fixtures, interview, `generate.ts`, `generate_cases.py`, input contracts | HARDENING-1 | E (check-all fails when one is missed, per the handoff; unverified per place) | None |

## 3. Rules that are not process rules

Architecture invariants (charter 2: the interview never sets an input, order never changes a value, all tax logic in
the formal model) are enforced by `interview-rules`, the Lean comparison and the fixture checks; they belong to the
model, not to this table. Owner decisions recorded in the handoffs (accepted trade-offs, rulings) are decisions, not
rules.

## 4. Conflicts between documents and tools

**4.1 Completeness cadence.** The charter (section 4) says completeness, screen and false-no reviews run "a fixed
sample per form per milestone, its union ruled once" in maintenance, because rerunning on every edit only pulls in old
low findings. `check_completeness.py` makes a form stale whenever its prompt hash changes, and the prompt includes
the form's whole encoding, so any edit to a form brings its completeness review due. The guard in 1.1 enforces
whatever cadence is chosen; the two documents need to agree first. (Checked: `check_completeness.py` lines 40-115
hash the prompt built by `completeness_review.sections` with `SYSTEM`.)

**4.2 Prompt changes.** CLAUDE.md says a review-prompt change applies prospectively, with no global re-review.
Because `SYSTEM` is part of the completeness hash, a change to the completeness system prompt makes every
completed form stale at once (legacy never-reviewed debt is exempt through `completeness_debt`). Unverified whether
the screen check behaves the same way.

## 5. Summary

- Already enforced: 2.3, 2.4, 2.13 (in part), 2.19, 2.20, 2.21.
- Buildable (hooks or checks): 1.1 to 1.4, 2.1, 2.2, 2.5, 2.6, 2.8, 2.15, 2.17, 2.18, and 2.16 if needed.
- Advisory: 1.2 (timeouts), 2.7, 2.9 (the check), 2.10 (timing), 2.11, 2.14.
- Needs an owner decision first: 4.1 and 4.2.
