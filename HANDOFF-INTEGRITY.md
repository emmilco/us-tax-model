# Handoff: the integrity plan, Phase 0 done, Phase 1 in progress

Read `HANDOFF.md` first, then `docs/2026-10-22_project_evaluation.md`, then `docs/2026-10-22_integrity_plan.md`
(v6, the plan with the owner's decisions 1 to 14), then this file. The roadmap stages (spec 2.4) are paused under
the plan's stop rule; nothing in `HANDOFF-STAGE-16.md` is to be continued until the plan says so.

## Where the plan stands

- **Phase 0 (honest reporting): done**, commit a946fae. Evidence report with M and E columns and the scoreboard;
  citation check on computed lines (305 locators to rewrite, `--strict` not yet in check-all); LICENSE,
  LICENSE-DATA, README, `handoffs/`; spec 6.5 and 3.11 qualified; BUG-0089 to BUG-0093.
- **Phase 1, first batch: done**, commit ac69196. 1.0 packet tool; 1.0b DeepSeek transport; 1.3 per-family review
  logs, `families.json`, `compare_families.py`; 1.4(a) per-form engine lines and the not-computed floor; 1.6 spec 4.7
  and `reports/2025/equivalence_review.md`; 1.7 `reviews/2025/direct-file/predicates.md`. Scoreboard 38 of 1,510.
- **Phase 1, second batch: in progress at handoff** (see "Uncommitted work" below for exact state):
  - the fixes for BUG-0094 to BUG-0097, BUG-0092, the owner's new refusals (decision 10) and the Tax Computation
    Worksheet re-keying (decision 11), each in an agent worktree with its Claude reviews rerun;
  - 1.4(b) OpenTaxSolver adapter (23.06; the owner is to download 23.07, see below);
  - the reading packets reworked for a human reader (item 2 first, for the owner's look);
  - the reading list doubled to 26 items (decision 13);
  - README rewritten as the trust pitch (owner's instruction).
- **Not started:** 1.4(b) UsTaxes adapter (scouting note `/tmp/tax-audit1/ustaxes_scout.md`, may be gone: the clone
  is at `.engines/ustaxes-src/`, commit d276c72); 1.2 DeepSeek whole-return class M; 1.3's full DeepSeek run over
  the 55 forms (do it after the fixes land so it reads the corrected encodings once); 1.5 class M on printed
  lines; 1.6 second reader and mechanization (8 stale `EQUIVALENT_IF` entries to remove; checker rules for the
  evaluator divergences D2 and D6 and a shared reason string for D5); 1.1 the owner's reading; Phase 2.

## Stop rule

Fired 2026-10-22 with three value errors on reachable returns: BUG-0094 (Schedule A medical floor at negative AGI),
BUG-0096 (EIC filer SSN definition), BUG-0097 (no Form 8862 gate). Coverage stays paused; the reading list was
doubled. Findings from 1.1 to 1.4 and 1.7 keep counting.

## Facts a fresh session needs

- **Agents run on Opus 5.5** (owner's instruction 2026-10-22): pass `model: "opus"` on every Agent launch.
- **DeepSeek**: the key is in the macOS keychain (service `deepseek-api`, account `elliotmilco`); `call_model` reads
  it at call time; never print it. Models available: `deepseek-v4-pro` (use for reviews), `deepseek-flash`.
  Transport check: `python3 tools/transcription/transport_check.py`.
- **Review logs per family**: `<form>.<family>.md` beside the Claude log; `tools/transcription/families.json`
  (claude required, deepseek optional until all 55 forms have logs). Policy (decision 14): a stale optional log
  fails check-all; an open ruling in an optional log does not. `compare_families.py` writes
  `reports/2025/second_family.md`; the agreement floor is a noise rate (decision 12), not yet implemented as such in
  `compare_families.py` (it still prints the raw 90% rule).
- **OpenTaxSolver**: 23.06 built at `.engines/opentaxsolver-src/` (from tenforty's vendored tarball; SourceForge
  blocks scripted downloads). The owner is to download the 23.07 Linux package in a browser into that directory;
  the adapter reads the version so the swap is a rebuild. 23.06 has three known defects declared as limitations.
- **Human reading**: `python3 tools/human_review/packet.py --all` then `python3 tools/human_review/serve.py`
  (127.0.0.1:8790); logs to `reviews/2025/human/<form>.md`; the reader field must equal the git author name. The
  owner found the first packets unusable (audit English, wrong pages); the rework (per-line pages from citations,
  highlighted quotes, helpers folded into printed lines, worked examples) was being judged on item 2 at handoff.
- **check-all**: about 7 minutes; the green marker counts only if no tracked file changes during the run, so make
  no edits while it runs; the pre-commit hook refuses any other tree. Commit messages go through `-F <file>`.
- **Worktrees**: agents that edit `forms/` work in `.claude/worktrees/agent-*` with `node_modules` and `.engines`
  symlinked from the main tree; merge with `git -C <wt> diff -- <paths> | git apply`, then
  `git worktree remove --force <wt>` and `git branch -D <branch>`.
- **BUG entries** are appended before or with the fix; the parent session writes them so parallel agents do not
  collide on ids. Next id at handoff: BUG-0098 (the Tax Computation Worksheet keying, first second-family yield).

## Uncommitted work at handoff

(filled in at wrap-up)

## Next steps, in order

1. Merge the three worktrees, run check-all, commit the second batch (one commit, listing items).
2. Owner judges the reworked item 2 packet; regenerate all 26 packets; owner reads items 1 to 13, then 14 to 26.
3. UsTaxes adapter (engine 4), after OpenTaxSolver lands.
4. Full DeepSeek run: `rerun_all.py --model deepseek-v4-pro` for transcription and render over all 55 forms; rule
   every disagreement with a source quote; implement the noise-rate floor in `compare_families.py`; move deepseek to
   required in `families.json` when every form has logs.
5. 1.2: extend `classm.py` to work a fixture case as a job (every document the case reaches), run DeepSeek over the
   3 to 5 chosen returns and the ~40 blind-predicted returns; relabel them M.
6. 1.5 class M on printed lines; 1.6 cleanup (stale entries, mechanization, checker rules D2/D6, D5 reason).
7. Citation rewrites (305 segments, `reports/2025/citations.md` "Locators to rewrite"), then `--strict` into
   check-all.
8. Phase 2: TY2026 rehearsal on the posted drafts; "complete" in spec 2.4; prevalence buckets; product surface.
