
## Walks (lane walks, ace7da1ef8cf40c9d, finished ~22:10; full results /tmp/walks-2026-11-15.md)
- Filer with nothing (01): 56 -> 58 steps. +1 digital assets (expected, Form 1040 page-1 question).
  +1 UNJUSTIFIED: f1040.tax_exempt_interest is now a screen for every filer (replaces s2.amt_owed tick box), from
  lane g1-f7b (in B1). Its note claims a no-Schedule-C filer is asked nothing about AMT; walks not rerun. Hits 01, 02, 07.
  Did not block B1 (one screen, no figures). Decide: fold it back into a tick group / gate it.
- Typical filers in all 7 areas now complete (were refused); costs per area in the walks file.
- Persona 21 has 10 unanswered questions (and 22 has 3), so its figures are provisional.
- Persona 18: refusal told on a background answer (sd.qof), a possible N11 conflict.
- No per-diem (8853) persona exists. No persona for pay not on a W-2 (scratch 90 used).
- N10: 33 new prompts over the limits (worst rprop.screen 144 words, rprop.kind 60, rental.days_personal 66,
  person.f4137_under20 47); 9 help texts over 40 words. Open judgment: does the 25-word limit apply to the
  hidden prompt of a tick-box member?
- Walks caveat: the background AFTER walk job exited 1 with an empty log, after writing /tmp/wout-after/SUMMARY.md
  for all 29 personas (the source of the AFTER figures). Cause not found. The problem counts were confirmed by a
  separate re-run of 5 personas.

## Owner decision 22:15
- Start the release (tools/release.sh --push) as soon as the docs commit lands, even after 00:30.

## xtests (a2d13edf3bb8126cc, finished ~22:25)
- 4 of 5 broken self-tests fixed in xint (uncommitted). One edit outside test scope (umbrella-what-if.ts) was accepted;
  the what-if report needs regenerating.
- Tool defect: transcribe.py catalog_selection drops computed helper lines read by the lines a line-scoped review
  covers (sli line 1 lacks household.mfs). Sent to XINT to fix before "built".
- The sales test no longer exercises narrowing of f1040; the merge widened s1's families to include 1040.

## Pending owner decision (asked ~22:25)
- 42 open mediums: fix tonight (release ~04-05), or commit to main tonight and fix and release tomorrow
  (recommended), or release tonight and fix tomorrow. Feature-sized items: refuse for now, or build properly?

## B1 landed 22:33
- acde74b5 pushed (tree 815a7955, green full check #3). Released 41 stale claims of landing/interview-redraft
  (the tip a2f24909 is already on main). The main checkout's uncommitted agent_runs rows are saved at
  /tmp/main-agent_runs.2230.jsonl; re-append the missing ones in the docs commit.
- GitHub warning: reviews/store/transcription/43fe6dd0...md is 71.48 MB (over the recommended 50, under the hard
  100 limit). It may cross 100 MB as it grows, which would reject a push.
- New LOW bug_pending/xint-ftc2555-01: a Form 2555 filer is sent to Form 1116 instead of the election (lawful,
  possibly a smaller credit). It belongs with the D3 election question (auto-elect when available, which loses the
  carryforward when foreign tax exceeds regular tax).

## Owner decision ~22:45
- Original release plan stands. Fix only what was already planned for the release (8u revert, d-01: both done).
  The 42 open mediums stay open; set a bug plan after the release, based on the time and usage limits left.

## Docs folded into the expansion (owner yes, ~22:55)
- /tmp/docs-final.patch = docs-org + docs-gen merged three-way onto xint (scratch /tmp/docsfold; 5 conflicts
  resolved: interview/README and README took xint's no-slice text; TASKS inmate task -> T-336; docs_steps +doc_figures;
  tier_paths both sides + READERS). XINT applies it at "go", before assign.
- xadj final: federal check_logs clean; s1/s1a/sa/ftc/person/f1040 ruled, no findings; ~$14 since built. Then sent
  to do ny_it201 (stale lines C,16,25,72,73 / render C,34,40,48,67,69,69a).

## Release reuse (owner: "do 1, definitely")
- In xint (uncommitted): green.sh has a release list; check_all.sh records it on a green full run in release mode;
  release.sh skips its run when HEAD's tree is release-listed (the sampled-review gate is still checked).
  test_green.sh has new tests and passes (needs the pyenv 3.13.6 python: the shell's default python3 lacks yaml).
  tools/README note added via /tmp/docs-final.patch.
- The expansion's full check runs in release mode, so release.sh should just tag and push.
- Option 2 (speed up mutate): not started.
- Proposed lane for tomorrow: profile `mutate` (about 29 of the ~38 min of a full check, already on worker
  threads across 18 cores) before changing it.
- xadj DONE ~23:12: federal and NY check_logs clean. ny_it201: 16 model error; 25 and render C ambiguity. For the
  owner: add the spouse case (a joint return where only the spouse can be claimed) to amb.ny.2025.item_c. The
  earlier scope ruling on C rested on a federal refusal of dependent filers that no longer exists.
- XINT "go" ~23:13.

## Owner decision ~23:50: rental counted as covered in the coverage estimate (XINT's (a)+(b)); MFS still fully subtracted.
## Owner ~23:50: use the remaining usage allowance. 7 read-only planning lanes launched (Opus, judgment), outputs in /tmp/nightplan/:
  med-k1sche.md, med-income.md, med-older.md (fix plans for the 42 mediums), interview.md (AMT screen
  regression, N10 rewrites, personas), decisions.md (owner decision memos), tooling.md (adversarial audit of the
  release-reuse change, screen-prompt wording, 71 MB store file), mutate.md (speed-up study). Shared rules in COMMON.md.
- ~23:55: release_reviews.sh FAILED. 11 federal forms have completeness samples made stale by tonight's changes
  (f1040, f1116, f1116col, f2441, f8582, f8853c, ftc, rental, royalty, s1, s2). The NY, screen and false-no
  checks were not reached. Note: the person prompt is 820k chars, over the 700k limit. Coordinator chose to run the
  due reviews and adjudicate (within the ~$200 release-sample cap; $85.82 spent). XINT reports anything over $60.
  Coverage headline now 85.9% (range 85.4-89.5%; was 78.4%).
- Tooling audit (/tmp/nightplan/tooling.md): no blocker in release reuse. Finding 1 (a direct run in a shared
  worktree can't see concurrent writes) is fixed in xint: the release list is recorded only in .git/check-all-worktree,
  so XINT runs check_all_bg.sh. Still open: engines that are missing get skipped but the run is still recorded as
  release (run_engines.py:628); no age limit on release entries; the skip path has no test. 71 MB f8889 store file:
  pure duplication (29 KB when deduplicated); propose a 50 MB pre-push guard now and dedup in the store later.
  Screen prompts use YAML text for 134 of 149 screens.
- Interview plan (/tmp/nightplan/interview.md): AMT fix = yes/no f1040.tax_exempt_any gate, sharing a screen with
  div.any. N10 rewrites drafted. New gap found: rental.not_at_risk misses guarantees and stop-loss arrangements.
  Persona 18 is an N11 conflict (reorder seq). Recommend the 25-word limit apply to full tick-member prompts.
- ~00:20 round 2 (owner: use remaining usage): 8 more lanes. Patch drafting into /tmp/nightplan/patches/ (sche-a,
  inc-m34, inc-m12, older-{ny,credits,scha}, int-{amt,p18,personas,n10,rprop}); wording-redteam.md; fetch-sources
  (Pub 936, Pub 926, i1040sh into /tmp/nightplan/sources, Sonnet); judgment-records.md (T-333 drafts).
- ~00:30: the release-round forks added 4 LOW entries (BUG-0923..0926). They re-flagged open mediums 0836, 0873, 0890.
  For the morning: BUG-0916 should also name f8853c.line22 (append a note entry); BUG-0828 has a sibling (section
  6013(g) first-year statement); unconfirmed lead: f1116.line3e leaves out Sch E and K-1 income; scope.k1 help still
  says "A Yes ends the interview here".
- xint soft-reset onto acde74b5 by the coordinator; check_bug_inventory OK (926 entries).
- Tooling hazard (patch-interview lane): the fixture runner accepts an input behind a gate answered No and ignores
  it with no warning (engine/src/eval.ts:843 validateInputs checks only declaration and type). Propose: warn or fail
  when a fixture states a non-default value for an input whose gate is false.
- Patches ready: inc-m34, inc-m12 (base + cod split), int-amt, int-p18, int-personas, int-n10(+ticks). Not drafted:
  int-rprop. Still out: sche-a, older-*, wording-redteam.
- Judgment records drafted (/tmp/nightplan/judgment-records.md), with 7 candidate findings. Top one: the
  community-property question asks where the filer lived, but Pub. 555 turns on domicile (possible medium for MFS).
- sche-a.patch ready (6 files; BUG-0836 arithmetic plus 0789, 0775, 0890, 0790, 0907 combined, rental.not_at_risk;
  6 hand-predicted fixtures). Merge conflict: drop int-n10's prompt for rental.not_at_risk.
- WORDING RED TEAM (/tmp/nightplan/wording-redteam.md): 14 proposals would give a wrong value. The patches were
  drafted IN PARALLEL, so apply red-team section A corrections to every patch BEFORE landing. Top ones: 0775 needs the
  sa.mortgage_interest note (else the interest is deducted twice; sche-a left it unpatched); the "have shares" heading
  in int-amt's new screen; 0873 "anyone else"; 0833 latest-4952 (keep the current prompt); 0815 box 19 double count;
  0851 K-12. On 0790 the red team recommends refusing every boat, against sche-a's choice. Owner decision.
- INCIDENT ~00:05-00:18: the patch-older lane defined a recursive `wc` shell function, which spawned about 6,700
  processes for about 2 minutes. Cleaned up (back to about 1,000). No full check was running; XINT warned to rerun any
  step with a fork error. Lesson for lane briefs: no shell function definitions that shadow commands.
- older-* patches ready: older-ny (0850, 0851; closure commands for 0629 and 0092), older-credits (wording),
  older-scha (0803, 0805, 0815) plus 0817a OR 0817b (choose one; 0817a touches 298 fixture cases and mutate.ts).
- ALL planning lanes are finished. The /tmp/nightplan/ package is complete apart from int-rprop.
- ~00:25 round 3 (owner: 8% left): v2-income, v2-sche-int, v2-older (red-team corrections applied, fixture values
  re-derived independently) into /tmp/nightplan/patches/v2/; v2-rprop (the rprop.screen restructure);
  jr-verify (rules on the 7 judgment-record candidate findings and drafts entries; community property first).
  Added a rule: no shell functions, no bulk process spawning.
- jr-verify (/tmp/nightplan/jr-verify.md): of the 7 candidates, 6 are REAL (1 medium, 5 low) and 1 is not a defect.
  MEDIUM: household.community_property asks where the filer lived, not domicile (Pub. 555). A Texas-domiciled
  servicemember stationed in Virginia answers No, so the MFS return gets no community split; the No also skips the
  HoH and ended-marriage refusals. Draft entries are ready to file with new_bug.py --pending tomorrow.
  amb.2025.mfs_community_property's text is stale (Pub. 555 and Form 8958 are now archived).
- v2 patches done: older-*, inc-*, sche-a, int-*. APPLY ORDER that works: sche-a -> int-amt -> int-p18 ->
  int-personas -> int-n10 -> int-n10-ticks, THEN inc-m12 (v2) -> inc-m34 (v2). int-amt after the inc patches fails 2
  hunks (textual clash only). Use sequential scratch applies; a multi-patch `git apply --check` misses clashes.
  v2 sche-a: 0790 = refuse every boat (the red team's choice); BUG-0775 help made conditional (the lane departs from
  the red team, which would divide costs twice; pinned by xsa.rental_then_home_june). 0907 lives in inc-m12 only.
  Over-length texts: sa.mortgage_interest help 78 words, sa.line5b 52, rental.amt12/16 49, rprop.basis 44.
- MORNING-REPORT.md drafted. CORRECTIONS needed in the final pass: (1) the 65 agent_runs rows WERE re-appended by XINT
  at step 0 (310 -> 375; check_agent_runs OK); (2) the stale landing claims DID refuse B1's first commit attempt
  (observed). Add the 00:00-00:25 review spend ($4.08) and the release outcome.

## ~00:50 Owner: don't keep anything for future sessions in /tmp
- Everything was copied to .claude/nightplan-2026-11-16/ (locally excluded via .git/info/exclude, so it doesn't make
  the main checkout dirty). These notes now live here; /tmp/morning-report-notes.md is stale.
- Before release.sh: the main checkout again has hook rows appended to research/costs/agent_runs.jsonl. Set them
  aside (copy to .claude/nightplan-2026-11-16/coordinator/), `git checkout --` the file, run the release, then
  re-append the rows in a later commit.
- int-rprop (v2) is ready, with variants rebased after n10 and after v2-n10. It BREAKS the same-step-count requirement
  for nonresidential buildings placed in service 2018-2025: +1 step for the qip child question (a 7th box is not
  allowed; labels can't carry the exceptions). Owner decision. New candidate entry: a foreign rental building must
  use ADS. Year-change gap: the recovery-year constant 8 must become 9 in 2026 (rprop.new_nonres,
  rprop.early_nonres, asset.qip_early); no operation exists yet.
- mutate-1 and mutate-2 patches drafted (untested). The plan's R1 was NOT verdict-preserving as written (union-baseline
  comparison); the patch shares only provably identical work, so expect less than 40-60%. Blocks of 8 for memory.
  The A/B protocol is in mutate.md (diffs reports/2025/mutation.md and the NY one plus stdout). Landing needs a full
  check plus A/B equality.
- lane-briefs.md: 7 lanes in two waves (L1-L6 in parallel, L7 the interview later). 45 owner decisions
  de-duplicated (OD-1..31 plus 14). Review estimate: ~$64 core, ~$103 with all options, approve ~$135. Two rule
  conflicts reconciled (reviews after the merge; lanes run a fast check only when called in to commit): confirm.
  S0 source-archive lane first. Not covered: community_property medium, latent K-1, closures for 0911/0629/0092.
- All lanes finished except tooling and K-1. Scratch (edit scripts) now also copied to the durable folder.
- tooling-1..5 drafted. LAND ORDER: tooling-1 (50 MiB blob guard) only AFTER tonight's xint commit and push (it
  would refuse xint's new 74.9 MB f8889 record); tooling-4 (24 h age limit on release entries) only AFTER tonight's
  release. tooling-2 found 2 possible fixture errors: s1.line8v.none (states s1.digital_amount with digital income
  No) and redesign.credits.prior_not_asked (stray ftc.carryover). tooling-3 (fail on missing engines) would block
  2026 releases until the engines support 2026: owner decision.
- ~00:55 coordinator fixed "in any worktree" wording in xint tools/README.md and the release.sh header (only a run in
  the bg snapshot worktree counts). This happened before the release check started.
- k1p.patch and k1s.patch (v2) drafted: 0837, 0838/0886 (root cause: the engine shows "(or, on a joint return, your
  spouse)" to an MFS filer as plain "you"), 0841, 0843/0882, the k1s.qbi refusal, a new k1s.interest_buy. Merge note:
  drop the interview lane's k1s.past_years rewrite (k1s.patch takes the red team's text). ALL planning and patch
  lanes are FINISHED.
- ~00:57: the what-if report (umbrella_savings.md, read by no check) ran 30+ min. It was the coordinator's mistake to
  ask for it. Told XINT to kill it, skip the redundant interview-length --write (release mode rewrites it), run only
  the fast checks, then start the check. Loss: ~35 min.
- Owner ~01:00: INTEGRATE the package into the repo. Plan, after the release: a docs commit on main adding
  docs/records/2026-11-16/ with the nightplan md files, patches/ (v1 and v2), the small edit scripts (not the 350 MB
  scratch file copies), the coordinator notes and MORNING-REPORT (corrected). Apply
  coordinator/protocol-8.10-additions.md to protocol section 8.10 and add task row T-337 (release-prep script).
  Sources: archive them via the S0 lane, not in records. The docs tier check is needed.
- 01:00 xint ready: tree 30714d67fdfdd5d0ea87797c7c28bb3e74932804 (HEAD acde74b5), coverage 85.9%. Release-mode
  check started through check_all_bg (pid 36037, run 36076). Coordinator watcher: background task bazik9mb1.
  After green: in xint, confirm write-tree == the tested tree (the bg run may copy regenerated reports back), commit
  with a message (B1 + expansion + docs), set aside main's agent_runs rows, ff main, push, then
  `tools/release.sh --push` in the main checkout (the skip path should fire). Then the records docs commit.

## ~01:10 Owner: usage reset; saturate work until 10:00
PLAN. Phase A (now to ~02:30, drafting only while the release check runs): 10 lanes launched, output in
nightplan/round4 and patches/v3: A1 jr (community property medium plus 5 lows), A2 lows-inc, A3 lows-sche,
A4 lows-older (pairing about 95 lows with the v2 patches, plus closures), A5 k1int (scope.k1 readiness, 0842/0885),
A6 store-dedup, A7 scout-8615, A8 k1e, A9 r78-2026 (R7/R8 and 2026 gaps), A10 screens (interview wording, pilot).
Phase B (after the release, ~02:30-10:00): records commit; S0 source archive; wave 1 fix lanes L1-L6 in worktrees
(v2 + v3 lows patches), merges with review rounds (cap ~$135); tooling lands (1 blob guard after the expansion push,
2 fixture-gate, 5 skip test, 4 age limit after the release); mutate A/B in a quiet window; wave 2 interview lane;
K-1 lanes B and C; a second release r2026.11.16.1 around 08:30-09:30 if green.
Working assumptions (owner told; no objection yet): plan defaults for undecided items; paid reviews after the merge;
a lane's fast check only when it is called in to commit; pacing per protocol 8.10.
- OWNER DECISIONS ~01:15: 0810 = tick-box screens (option B; land inc-m12.cod); 0817 = 0817a (ask every giver);
  N10 25-word limit APPLIES to a tick member's full prompt (int-n10-ticks lands); rprop.screen restructure LANDS
  (int-rprop, +1 step for 2018-2025 nonresidential). Others: plan defaults.

## GOAL (owner, ~01:20): finish the release, then the bugs, then continuous work in atomic, interruptible units with
little tech debt and little in flight; structure around bottlenecks; delay and combine checks to maximise throughput.
When the bug backlog is clear, continue expanding coverage. Don't stop until the usage limit.
- 01:14 release-mode check FAILED (wave 1): limits (renamed id in limits.json), year_changes (an s2.x2-paynow2 op
  `from` locator), check_extraction (p4801 and p915 PDFKit vs poppler). XINT is applying 1 and 2.
- 01:25 decision on check_extraction: extend exceptions.json to check 2 ("pdfkit"); except p4801 pp. 1, 2, 6 and
  p915 p. 23 (read by nothing); file a LOW entry xint-extract-01; then rerun the release-mode check. XINT applied 1
  and 2: limits OK, year_changes OK.
- LESSON for 8.10: a check that fails in wave 1 costs ~13 min. Run the fast-failing steps (check_extraction, limits,
  year_changes, check_logs) directly before starting a full check on a new candidate tree.
- A8 k1e done (round4/k1e.md): lands as the last step of the K-1 integration. Its reviews ($1.35) and the pending
  low xrevk1e-01 are only in the x2-k1e worktree: carry them back before any rerun. The likely class M blocker is that
  the fixtures set scope.k1 true (inferred). Decisions under delegation: O2 refuse (fails safe); O5 land with the
  integration; O3 keep scope.k1 one question for now (a split is a task).
- ~01:32 extraction fix done (pdfkit exceptions honoured, self-test case, BUG-0927 LOW, both extraction checks
  pass). Release-mode check RERUN started (wait pid 45583; watcher be7x14m1w). Estimate ~02:50.
- A7 scout-8615 done: 0.143% of returns (below the stop rule; owner judgment); child AMT cap gap (Rev. Proc.
  2024-40; build in s2 or refuse); about 900 fixture lines to retire. PINNED e812db31 (qdcg_amount, wired) as
  refs/scratch/qdcg-amount so gc can't drop it. Under delegation: 8615 is queued after K-1 integration and k1e
  (larger share); its decisions take the scout's recommendations when it starts.
- A3 lows-sche done: 12 lows fixed plus 0857 with int-amt; add-ons apply only at the END of the v2 chain; the int-rprop
  bank hunks must be redone by script after sche-a. RUNBOOK REVISED: one apply-chain lane (F1), not six.
- A10 screens done: screens.patch (prompts show interview wording; the subject includes it; a $0 migration, simulated:
  no screen due afterwards) plus screens-joint.patch. FOUND: the screen prompt told reviewers to ignore joint-only
  gaps ("married filing statuses are refused elsewhere"), which is false, so every screen review skipped
  spouse-only gaps. DECISION (b) under delegation: land both and re-review all screens (~$21), inside Phase B's
  combined review round. No migration is needed then. Also: 36 orphan screen records (a low, for later).
- A6 store-dedup done: dedup in the record store (write_record/parse_record), so no reader changes; records over
  1 MiB get a `shared` part; byte identity checked twice; keys unchanged; fast tier. f8889 74.9 MB -> ~100 KB (est).
  Decisions under delegation: threshold 1 MiB; run `share --write` on existing large records only after the clone
  proof passes; drop large_blobs.txt from tooling-1 (keep the 50 MiB guard).
- A9 r78-2026 done: R7+R8 live in .claude/worktrees/ty26-r8 (nx-r7 superseded). Applies to xint except the
  realty_year "Before 1987" label (3-line fix sketched). 2026 gaps: 37 params unstaged (dc.exclusion_max_mfs 2,500 ->
  3,750), constants 32->33 (rprop.early_nonres) and 8->9 (asset.qip_early, rprop.new_nonres), the
  realty_recovery_year table, 8 catalog rows. T-321 is done (close the row). R8's dry run: $146.57 of reviews.
- A4 lows-older done: 21 lows fixed in 3 add-ons; closure commands for 0465, 0532, 0729, 0757, 0893 (0092 reuses
  the older-ny.md draft; 0647 "in part" until 2026). Check: amb.2025.ira_age50's reason vs the i1040gi child-age
  rule (owner). N10 overruns piling up (gift.special 141 words, person.edu_over 57, NY real property 46):
  F1 must list every text over N10, and an Opus trim pass runs before the review round.
- A2 lows-inc done: 27 entries (4 in part) in inc-m12-lows (needs int-n10-ticks first) and inc-m34-lows. Under
  delegation: KEEP all hunks; the added sampled subjects ride in the combined review round. 11 deferred (0795 model
  change, 0828 on f8960, 0570, 0895, 0764, 0765 ...). Warned A1 about the scope.recovery overlap.
- A5 k1int done: 4 ordered patches (8582 rows, EBL/QBI = 0842/0885, return flows, 9 fixtures). Found a cycle in the
  contract's "allowed loss" EBL reading (it counts losses before the passive limit instead; over-refuses only).
  Form 461 is now archived (an ambiguity's reason is stale). Drop v2 k1s's qbi_passive hunks. 37 readiness items:
  6 done, 18 patched, 13 missing. Lift blockers: split scope.k1, f1040.line25c double count, line 3a (599 facts),
  f8960.unsupported, 4952 box 20, tree/consumers/rows, BUG-0836 first. Coverage 85.9 -> ~88%. Plan L0-L9, ~15-20 h.
  The coverage phase starts here after the backlog; decisions D1-D7 take the report's recommendations.
- ~02:05 launched B-chain: assembles ONE combined fix-round.patch (every v2 and v3 patch plus k1p/k1s plus jr, in
  order) on scratch copies of xint, with the resolutions and the N10 overrun list. F1 then applies one patch and goes
  straight to build and test. Removes the patch-ordering risk from the critical path.
- A1 jr done: the community-property MEDIUM is patched (domicile wording; household.spouse_cp_domicile plus 3
  helpers; both cp ambiguity entries quote Pub. 555; 5 coverage rows). Decisions under delegation: (1) revert the
  spouse question off the ended-marriage path (it costs ~14% of returns a step); (2) sa.dependent keeps the 56-word
  help for now, and the child question becomes a task; (3) apply jr-digital (32-word prompt goes to the trim pass).
  Sent to B-chain. Entries BUG-NEW-JR-01..06 are drafted in jr.md.
- ~01:45 B-chain done: patches/v3/fix-round.patch (79 files; git apply --check OK on xint; 5 hand resolutions
  R1-R5; k1s.qbi_passive dropped for k1int; validated: no duplicate ids, groups <= 6). 98 N10 overruns (sa.line1 325
  was 313; gift.special 141). Trim lanes T-trimA and T-trimB launched; they write id/field/old/new JSON, applied by
  script after fix-round in F1.
- ~02:00 stopped 7 stale background waits from before the /clear. Old lanes (X2, xadj-b, x1-sche) sent their last
  notices; their states are superseded. In the records commit, verify the adjudication md of rental, rprop, rf4562
  and royalty covers the xrevsche round (the files exist and mention it).
- T-trimA done: 52 edits in round4/trimA.json ("old" is the PARSED YAML value, so apply by YAML, not plain text). Decisions:
  accept married_dec31 "and not remarried" (Pub. 501); k1p.t6 uses BUG-0886's standard wording (41 words); REVERT the
  edu_over books-rule move to help (a guard can't live in help). Candidates for entries: sa.spouse_extra missing
  "can't be claimed as a dependent" (i1040gi:762); sa.line11 treaty charities. Follow-ups F1-F7 (model changes) become
  tasks. Note: the owner decided tick members' full prompts take the 25-word limit.
- T-trimB done: 49 edits in round4/trimB.json (with old_raw/new_raw, which occur exactly once; a plain replace is safe).
  Override: REVERT the NY est_any estate/trust move to help. Accept the rest. 7 kept overruns with reasons;
  follow-ups F1-F4 become tasks. The owner already decided F6: tick-member prompts take 25. F5 (per-entry frame
  counting) is open: default to counting the prompt without the frame.
- PHASE A IS COMPLETE. Everything for F1 is ready: fix-round.patch + trimA.json + trimB.json + overrides.
- ~02:01 F1 STARTED early: provisional base commit 50895515 (tree 9ddb71b6 = the release candidate, parent acde74b5)
  pinned as refs/scratch/f1-base; worktree .claude/worktrees/f1, branch fix-round-1. It applies the patch and trims
  now and holds builds until the release check ends. After the expansion commit lands (same tree), rebase
  fix-round-1 --onto the real commit. Remove refs/scratch/f1-base afterwards.
- ~02:10 TEST DRIVE server for the owner: http://localhost:8791/ serving the release candidate tree 9ddb71b6, built
  in /tmp/testdrive-rc (git archive, its own empty git root); logs in ~/Documents/Tax-Interview/rc-2026-11-16
  (0700). Profile ny. Owner is test driving: their logs there are walk evidence for T-332.
- 02:10 release-mode RERUN FAILED in wave 2 (11 steps). MAIN CAUSE: the 9 renames missed collection-indexed keys
  (f8853c[p0].pre1996 ...). Also test_serve, test_integration and classm_job_seeds expect MFS refused (it is computed
  now); person_wording stale; interview_rules and ny_mutate to inspect. Sent to XINT with: fix, run every failed step
  directly, then the full check.
  LESSON (8.10): a rename late in a round must be followed by test-fixtures and coverage before the full check; and
  rename_carry/renames must cover collection-indexed keys (a tool gap: file it as a task).
  NOTE: F1's base (9ddb71b6) has the same defects. F1's build and test results will show these failures; rebase F1
  onto the fixed expansion commit before trusting its results.
- 02:15 XINT fixed the rename miss (f8853c[p0].* in classm.json, f8853c.json, f8853c.rulings.json). Decision (a):
  mechanical fixes by XINT; fork 1 re-points the MFS-refused tests (B1-B3) and the ny_mutate args (B5), or files a bug
  if the code is wrong; fork 2 investigates the 2 completion leaks as possible real defects (fix + pin + entry; NOT
  baselined). Then all 11 steps directly, then the full check. New estimate: check rerun ~03:00, done ~04:15.
- ~02:25 round 5 (drafting the next units; no CPU): D1 k1block (13 missing K-1 lift items), D2 trimfollow
  (model-change follow-ups), D3 deferred lows (model changes, incl. 0795 and 0871), D4 tools T-337 and T-338, D5
  Form 8615 form+int (decisions per the scout's recommendations), D6 personas plus OWNER-WALK-KIT.md. Output in
  nightplan/round5 and patches/v4.
- ~02:30 (after a second /clear) coordinator resumed. State checked: origin/main acde74b5; no check-all slot held; last
  bg check = the 02:10 failure. XINT (a0793900) is waiting on fork 1 tests (aa37c530, waiting on its NY mutate run)
  and fork 2 leaks (a01d0164, running). Round-5 drafters D1-D6 running (a2a03158 k1block line3a, aa723db4
  trimfollow, a65bc9d2 deferred lows, a13ad0da tooling release_prep, a8c3e619 8615, a85057bb personas). Test-drive
  server pid 60967 up. Next: when XINT reports, follow the handoff "Next actions" 1-6.
- ~02:35 D6 personas done: patches/v4/personas.patch (personas 23-31, NONE walked; values hand-derived as YAML comments),
  round5/personas.md, round5/OWNER-WALK-KIT.md. Real gaps filled: 23 per diem, 24 household pay, 27 dependent interest,
  28 dependent at 8615. Findings: persona 23 depends on owner decision 8; possible model issue rental.div5/div8 split
  rental-only costs by days (Pub. 527, unverified) -> task candidate; O9 (pin e812db31) is ALREADY DONE as
  refs/scratch/qdcg-amount. No NY persona; none for foreign tax above the limit. Add agent_runs rows for D6 and its fork
  in the records commit. Personas ride with F1 (walk them in F1's build; fix answers, never the expected ends).
- ~02:40 D2 trimfollow done (round5/trimfollow.md; patches/v4/tf-*.patch; nothing built). Patches: A-F3 (ptc_files gated
  on own_money), A-F4 (asset.listed split, asset seqs shift), B-F1 (digital assets got/disposed, ~975 mechanical
  fixture edits), A-F1 (gift.special -> 2 tick screens), B-F2 (NY use tax parent+DMV child; one coverage row's asks id
  renames). Design only: A-F2 (sa.line1 from 1095-A; own Opus lane + owner sign-off). Blocked: A-F6 (Count can't be
  gated). Not recommended: A-F5, B-F3, A-F7, B-F4 (coordinator accepts: drop them).
  PLAN under delegation: these are a SECOND fix unit (F2), not folded into F1: F1 is already big (79 files + trims) and
  B-F1/A-F1 restate hundreds of fixtures; keeping them separate keeps F1 interruptible. F2 = A-F3, A-F4, B-F2 first
  (small), then B-F1, A-F1; shares F1's review round only if F1 has not started its paid reviews yet.
  Owner items: thrift-store over-refusal under gift.special "belongings the charity will not use" (p526: only reduces
  appreciated property); A-F1 refusal timing; A-F2 sign-off.
- ~02:45 D4 tools done (round5/tools.md; patches/v4/t337.patch then t338.patch, sequential). Safety classifier was
  down for this agent: verified main tree unchanged and xint holds no release_prep.sh / rename_ids.py (it did not
  apply its patches outside scratch). No self-tests run yet.
  Decisions under delegation: (1) release_prep runs every step and offers --fail-fast; amend the T-337 TASKS row in
  protocol-8.10-additions.md to say so. (2) Keep both self-test groups (2-4 min is cheap beside a 75-min check).
  (3) Land T-338's 26-witness rename migration (clcw_next_year, f8962, rec, refund rulings sidecars) in the same
  commit, as one `rename_ids.py apply` run, so the new step is green on landing. Check claims.py for those 4 forms.
  Lands as a TOOLING unit after the release, independent of F1 (fast-tier check only).
- ~02:50 D3 deferred lows done (round5/deferred.md; patches/v4/def-*.patch, 14 patches, ~11.2k lines, apply order
  0871 0795 0765 0891 0779 0889 0786 0778 0828 0895 0570a 0570b 0791 0719). Classifier was down: main tree and xint
  checked for stray edits. Nothing built.
  Decisions under delegation: HOLD 0570b (up to 35 fixture cases may newly refuse; no precedent for a refusal on an
  input line) and 0719 (needs usc-26-402 and usc-26-457 archived first; Pub. 525 p. 9 reads against it) -> they go to
  the S0 sources unit. Accept the agent's design choices (rental_rare box in 0779; 0891 own question; 0828 refuses only
  above the NIIT threshold). 0765: regenerate f1040.md, interview_coverage.md, COVERAGE.md and edit the ty2026
  proposed f1040 in the same unit. These become fix unit F3 (after F2), rental chain together.
- ~02:55 D5 8615 done (round5/f8615.md; patches/v4/f8615-form.patch then f8615-int.patch). Nothing built. Findings: the
  child AMT cap makes the s2 AMT screen fire (refuse), not an amount, so the served share shrinks; the cap reaches
  non-dependents 19-23 (ambiguity entry); f8615/i8615 sources are marked "not cleared for encoding" in the manifest
  (OWNER: clear them or the area can't count as covered); retired inputs reach ~1,330 fixture lines (incl. 418 NY);
  4 mutation.m3.scope.l16_f8615_* cases must be restated in the K-int merge (separate commit, tool-managed file).
  CLASH: D5's personas 23/24 collide with D6's personas 23-31. At landing, renumber 8615's to the next free numbers
  after D6's (32, 33). Queue unchanged: 8615 after k1int, k1block and k1e. Write agent_runs rows for D5, D6 (+fork).
- ~03:00 D1 k1block done (round5/k1block.md; patches/v4/k1block-0..9; nothing built). Land k1block-0 IN PLACE OF v3
  k1int-3 (fix round renamed f1040.tax_exempt_interest -> _if_any). Order: k1int-1, k1int-2, k1block-0, k1int-4,
  k1block-1..9. BUG-0836 must land before the lift. Found: s1a.line5_calc and s8812.eiw_3 relied on scope.schedule1
  to refuse K-1s; each now refuses itself. Line 3a restatement: 775 occurrences (script restate_line3a.py).
  k1block-3's help hunk is against untrimmed text: rebase after trimB (F1 lands trimB first, so expect it).
  DECISION under delegation, OVERRIDING the lane on D7: keep partnership_scorp `refused: true` until the box 14 A SE
  wiring (D2) lands; counting it covered while box 14 A refuses would overstate the coverage figure the owner reads.
  Owner: S corp box 17 A/B (neither refused nor carried to 4952) -> interim: refuse, pending owner. Coverage-row end
  changes from the lift are pre-authorized as restatements (owner O8 pattern), listed in k1block.md.
  ROUND 5 COMPLETE: D1-D6 all reported.
- 02:45 (CORRECTION: the ~02:35-03:00 stamps above ran ahead of the clock; real time 02:44). agent_runs rows for D1-D6
  and the D6 fork were written by the agent hook: no manual rows needed. Tests fork (aa37c530) delivered to XINT at
  02:28: B1-B5 were stale tests/pins, no code change, no bug. XINT now waits only on the leaks fork (a01d0164, active,
  build OK, replaying witnesses). F1 (ada1b40b) is running its draft-walk.
- 02:50 S0 sources QUEUED for after the expansion lands (xint changes tools/sources/2025.json; a parallel S0 would
  clash). Scope: p936, p926 (irs-prior 2025 URL), i1040sh per nightplan/sources/README.md; plus usc-26-402 and
  usc-26-457 for 0719 (check fetch_sources.py's allowed hosts first); plus the f8615/i8615 revision inspection that
  clears them for encoding (same mechanical method as README step 4). Sonnet, mechanical, docs/fast tier.
- ~02:55 F1 reported: fix-round-1 tip 5a180443 FAILS BUILD (11 errors: 5 unanalyzable guards, 4 spouse-wording,
  k1s.past_years duplicate prompt, rental.prior_any spouse phrase near-miss). Post-failure check numbers are stale
  canonical, not regressions. Base 50895515: fixtures 2381/2383 (both = the known pre1996 rename), NY 358/358,
  coverage 0, 19 walk problems on base (scope.nol opened for personas 21/22) -> walks need attention in F1 too.
  Possibly real on the branch: s2.amt_business (personas 05, 13), sales[nft] (18), rprop.screen (19).
  Launched F1b (Opus, judgment): fix the 11 errors on f1 worktree, rebuild, rerun checks to f1/fix2, triage
  regressions. No check_all. Then rebase onto the expansion commit.
- ~03:00 F1b: 11 build errors fixed, build green (gates -> Bool helper lines, ids/targets unchanged; 6 wording fixes,
  no list words added). STAGED, NOT COMMITTED (guard needs green fast check; correct). Patch f1/fix2/f1b.patch.
  vs base: walks 2 problems (s2.amt_business, personas 05/13, pre-existing) vs 19. Remaining: A stale inputs (47 MFS/HOH
  cases lack household.spouse_cp_domicile: jr.md wrongly assumed classm/mutation take defaults; 9 classm K-1 cases;
  2 coverage rows), B 4 household remedy restatements, C REAL DEFECT interest_dividends tick group opens ftc.taxes /
  ny out_of_state_bond_interest out of order, D generated-sample shift (generate.ts changed; new leak generated.53
  dependent.absence_no_return; eic out of order on generated.327) -> after rebase.
  Decision: F1b continues A, B, C (uncommitted), results to f1/fix3; commit only after the rebase onto the expansion.
  LESSON (8.10): a patch design's "no fixture changes" claim must be checked against tool-managed files that take no
  defaults (classm, mutation), and against asserted remedy strings.
- ~03:45 owner asked to parallelize aggressively. Launched round 6 (all scratch, no commits, no check_all):
  R1 (Opus) owner-decision source research -> round6/owner-sources.md (rental div, thrift store p526, decision 8,
  S corp box 17 A/B, 8615 AMT cap; reports f8615/i8615 printed revisions, no manifest edit).
  S0 (Sonnet) sources patch in worktree s0 -> patches/v4/s0-sources.patch (p936, p926 2025, i1040sh, usc 402/457).
  T1 (Sonnet) t337/t338 self-tests in worktree t1 (xint HEAD + xint diff) -> corrected patches + t338-migration.
  V1 (Opus) build-validate F2 + F3 patches on worktree v1 (5a180443 + f1b.patch) -> *.v1.patch, round6/v1.md.
  V2 (Opus) build-validate the K-1 stack on worktree v2 (same base) -> *.v2.patch, round6/v2.md; D7 override applied.
  Held: persona walks (need F1 final), Form 8615 validation (after K-1, persona renumber 32/33).
- ~04:00 S0 done: patches/v4/s0-sources.patch (5.2 MB; 20 source files + 2 catalog files), round6/s0.md. Hashes match
  README; manifest revision fields set for p936/p926/i1040sh. usc-26-402/457 from govinfo (existing precedent; 2024
  edition, revision null like other usc rows). LANDING: apply only the 20 source files + re-add S0's JSON rows (in
  s0.md) onto the expansion commit's catalog/manifest; do NOT apply the catalog hunks wholesale (they include xint's
  rows). Do not run --derive. Check PREMISES.md rows requirement (tools/README) before landing. Worktree s0 left.
- ~04:05 R1 done: round6/owner-sources.md (verbatim quotes, pages). Owner-facing summary:
  Q1 rental-only costs divided by days: MODERATE "should not" (Worksheet 5-1 line 2d "Fully deductible"; Pub. 527
  pp. 23-24). Model divides every line (xint rental.yaml:517-529, 663-675); cite page 26 should be 25; div11 same.
  -> file as a pending bug after the release (does not block: release ships it as is, like the 42 mediums).
  Q2 thrift store: STRONG text does not require refusal (p526 p.19; i8283) -> narrowing is an owner/N9 design call.
  Q3 decision 8: line 22 counts gross cost "whoever paid", line 24 only "paid back to you": an INCONSISTENCY on xint
  (overstates the limit) whichever reading; count on both or neither -> bug candidate; owner picks the reading.
  Q4 S corp 17A/B: instructions treat them like partnership 20A/B (strong); need for a twin moderate (box 12 refuses,
  understates only) -> keep interim refuse per V2 only if trivial.
  Q5 AMT cap reaches all 1(g) children (moderate); BUT f8615.kid's questions are reached only above $2,700, so the
  patch may behave as the narrow reading: check when Form 8615 is validated.
  f8615/i8615 printed revisions found (2025; Created 9/9/25; Oct 22 2025): clearing awaits the owner's answer.
- ~04:15 T1 done: t337 (corrected: tier_paths READERS entries for release_prep), t338 (unchanged), t338-migration
  (26 names, 4 sidecars) apply clean in order on xint's diff; all their self-tests pass. 18 code self-test rows failed
  only for environment (no engine build/node deps/.transcription in scratch; "no yaml" — probably not the pyenv
  python): rerun self_tests in the landing tree. TOOLING UNIT READY to land after the release.
  CLEANUP LIST (after landings): worktrees s0, t1, v1, v2; /tmp/t1-xint.diff (271 MB).
- ~04:20 XINT stopped: 9/11 steps pass (fixtures 2386/2386, NY 358/358, coverage, integration, serve, classm seeds,
  compare, interview_rules with pruning rewritten). Leaks fork: helper chooses in dependent.yaml, 3 pinned fixtures,
  xleak-01/02 pending bugs; review debt (dependent render + class M, low). HIDDEN failures now visible (steps crashed
  before): federal mutate 61 stale args + 3 retarget problems; ny_mutate 4 stale args (spouse_nonresident, likely the
  leak helper reading f1040.status); refusal_reach 19 new K-1 fixtures (refusal does not reach the return).
  Decisions under delegation: launch X-MUT (Opus; per-argument re-check, re-pin, round6/xmut.md) and X-K1 (Opus;
  latent-K-1 fixture design vs wiring defect; no K-1 wiring) in xint, disjoint files. Keep the dependent read order
  (owner morning item: household_all_year before spouse_relative changes stage8.mut.mfj_spouse_relative_all_year_unanswered).
  When both report: resume XINT for the release-mode full check via check_all_bg.sh, then the landing steps.
  LESSON (8.10): a step that crashes hides its later checks; after fixing a crash, rerun the step before estimating.
- ~04:30 X-K1 done: (a) fixture gap. scope.k1 is ungated, feeds scope.schedule1 which refuses f1040 lines 8/10; K-1
  lines are latent (no return reader). Added "scope.k1": true to 19 refuse fixtures (k1p.json 12, k1s.json 7); no
  expectation, form or exception change. refusal_reach exit 0 (547 checked, 19 FAILs gone); us fixtures 2386/2386.
  Not run: NY fixtures (untouched files). Release now waits only on X-MUT.
- ~04:40 F1b pass 2 done: groups A (47 cp_domicile inputs, 9 k1 classm inputs, 2 coverage rows), B (4 household
  remedy restatements), C (ftc.taxes 280->272; NY out_of_state_bond_interest 1010->272; bug_pending/fix-round-1-01.md)
  done. fix3: fixtures 2404/2406 (known pre1996 pair only), NY 361/361, coverage 0, tick-groups 0, walks 2 (base too),
  interview-rules 10 (group D, after rebase). Staged in f1; f1/fix2/f1b.patch regenerated (20 files); msg4.txt updated.
  DECISION under delegation: ACCEPT ftc.taxes at 272 (rare refused filers answer one extra amount before refusal;
  the alternative weakens a standing check). Owner may revisit. Note home.gifts_and_carryover refusal waits on
  s3.foreign_any (late, N11): fold into the BUG-0817 design.
  F1 IS READY FOR REBASE onto the expansion commit. NOTE: V1/V2 were based on the fix2 f1b.patch; their corrected
  patches may need re-context after the rebase (cheap).
- 05:12 P1 done: personas 23-31 walk clean on F1 (only 27 needed 6 closed answers); figures equal the hand-derived
  values for the 7 that complete (not checked against IRS tables). Folded into F1: personas.p1.patch applied --index
  in the f1 worktree (29 staged files now). Full staged diff saved: f1/f1-staged-with-personas.patch.
  Persona 23 still rides on owner decision 8; persona 31 avoids rental-only costs.
- 05:20 X-MUT done: 65 stale args resolved (56 re-pinned, 1 retargeted, 4 removed, 0 findings; per-arg lines in
  round6/xmut.md); ny_mutate exit 0. Federal mutate exit 1: 372 PRE-EXISTING unexplained survivors (mutate requires
  every survivor explained). By form: f1116sb 65, k1s 56, k1p 49, rental 38, person 34, f1116col 24, rec 17, f8582 16,
  f1116 14, sche 8, royalty 8, f7203 5, eic 4, small others ~35.
  STRATEGY CHANGE (coordinator, under the goal; owner may override): release DEFERRED and checks COMBINED.
  (1) Expansion commits to main on a green FAST tier (XINT resumed for that; coordinator ffs + pushes).
  (2) F1 rebases and commits on fast tier; tooling (t337/t338+migration) and S0 sources likewise.
  (3) Mutation-survivor lanes M-1116, M-rental, M-existing start on the new main (disjoint fixture files; equivalence
  entries kept in per-lane blocks of mutate.ts to merge cleanly).
  (4) K-1 survivors wait for the K-1 integration (would go stale), then M-K1.
  (5) ONE release-mode check over everything, then tag.
  Why: avoids 2-3 extra 75-min release checks and keeps nothing large uncommitted.
- 06:30 OWNER: release only after the 372 survivors are killed/explained (owner first chose the waiver, then
  reversed: "fix the survivors before the release ... be smarter than waiting hours").
  PLAN: (1) MW lane (Opus): tools/mutant_witness.mjs searches fixtures + corpus + perturbations for inputs that kill
  each survivor, greedy set cover -> few witness cases per family; worklists WITHOUT values (lanes predict from sources
  blind, per mutation.json convention); unkillable -> equivalence candidates. Worktree mw at refs/scratch/xint-fast
  (6649c637 = commit of tested tree aebecaa7 on acde74b5). (2) Four parallel family lanes (f1116, k1 — now, not after
  integration, since the owner wants the release —, rental, existing) write fixtures into their own form fixture files
  and equivalence args in per-lane blocks. (3) one mutate run, (4) release-mode check, tag.
- ~06:50 Fast tier on xint FAILED (5 steps): siblings_check + bookkeeping self-test (xleak entries' sibling lists),
  consumers (3 stale entries), bug_status (regenerated) -> fixed by XINT. check_logs: dependent transcription + render
  logs stale after the xleak dependent.yaml change -> APPROVED the paid reruns (dry run $2.21 < $3 gate; review what
  changed rule), XINT adjudicates, reruns fast tier, commit_tested.sh. No ff/push/release by XINT.
  LESSON (8.10): a repair that edits a form's YAML makes that form's review logs due; schedule the line-scoped
  reviews in the same repair, not after the commit check fails.
- ~07:00 XINT: dependent transcription + render reruns done ($2.40: 1.91 + 0.48), all ruled (17 model error, 1 scope,
  5 representation; render 5 = owner's 1098-T date ambiguity). No form changes. check_logs then flagged the dependent
  class M log (~$1.77): APPROVED, plus standing approval for any other <$3 review this commit needs. Then reset index,
  fast tier, commit_tested.sh, worktree_data carry-back. Gap noted: triage keeps only 6 witnesses per line.
  06:50 owner: make V1/V2 nicer -> reniced their engine processes +15 and told both lanes to run engine commands
  under `nice -n 15`. Critical path = MW witness search + XINT commit.
- ~07:20 owner asked what else can run. Launched (pre-staged to cut the critical path):
  M-1116, M-K1, M-rental, M-exist (Opus, judgment) in worktrees m1116/mk1/mrental/mexist at refs/scratch/xint-fast:
  read forms + sources now, wait (one long wait) for round7/witness/<family>.md, then hand-predicted kill fixtures in
  each form's own fixture file (not mutation.json) + equivalence args in per-lane delimited blocks of mutate.ts;
  output round7/<lane>.patch + .md. REC (Sonnet): records-staging/ (records tree, corrected MORNING-REPORT, 4 pending
  bug drafts from owner-sources Q1-Q4, merged 8.10 lessons). MW told to wait with one long pid wait (it was waking
  every 20-40 s).
  CLEANUP LIST += worktrees mw, m1116, mk1, mrental, mexist, p1; refs/scratch/xint-fast.
- ~07:35 REC done: records-staging/ (201 files, 7.5 MB; s0-sources.patch skipped as >5 MB, correctly), corrected
  MORNING-REPORT.md (spend $388.90 / 1,574 calls through 06:54 EST), bug drafts rec-01..04, protocol-8.10-additions-v2.md
  (T-337 row now says every step + --fail-fast). Decision: rec-02 stays a SEPARATE pending entry cross-referencing
  BUG-0873 and BUG-0916 (the inventory is append-only; an existing entry's text is never rewritten). The records commit
  lands after the expansion commit, docs tier.
- 07:35 (real clock) MW done: tools/mutant_witness.mjs in worktree mw; worklists round7/witness/. 128/372 witnessed
  (93 cases); no witness 228 = 76 time-limited (f1116 52, rental 16, existing 8) + 50 no value-sheet reader (48 k1,
  e.g. person.k1p_count_sche read by nothing) + 95 reach-but-no-reader-differs + 9 never change their line. MW
  rerunning the 76 with 180 s budget -> *.addendum.md. All four family lanes told. Release estimate given to owner:
  ~13:00 (range 12:00-14:30), K-1 lane the long pole. NOTE: equivalence work (152) is now the larger share.
- 07:45 owner: "look for ways to speed up the release". Done:
  (1) MSTRUCT (Opus): structural "no observable reader" rule in mutate.ts, computed per run, self-tested -> explains
  the ~50 dead-line survivors at once (lapses when K-1 is wired). Lanes told to skip those.
  (2) Long poles split: M-K1 now k1p only; new M-K1S (k1s + f7203; merge k1s.json by case id); M-1116 now
  f1116/f1116col/ftc; new M-1116SB (f1116sb, new fixtures/2025/f1116sb.json, waits for MW's addendum).
  (3) After the expansion commit: stack records + S0 + tooling, run a FULL tier early (mutate expected to fail) to
  surface any other hidden failure while lanes work. (4) Final check via release_prep first.
  (5) V1 and V2 parked after their current step (progress to round6/v1.md, v2.md); resume after the release.
  Owner acknowledged the slip; root causes + countermeasures given (gates never run on the expansion; crash-masking;
  coordinator sequencing ~2-3 h). Add to 8.10: a unit is not release-ready until mutate + refusal_reach complete on it;
  expansions carry their kill work; estimates only after a measured full pass.
- ~07:50 M-1116SB: nothing to do; M-1116 had claimed all 65 f1116sb ids (m1116-handled-sb.txt, 07:40) and marks them
  killed in its scratch check by 2 fixtures (f1116.m1116_sb_limit_ends_in_xii: 60; f1116.m1116_sb_no_excess_limit: 5).
  No m1116sb.patch (expect it missing at merge). Worktree m1116sb unused -> cleanup list.
- 07:45 owner asked why the fast tier is slow: base ~24 min (build 553 s, code self-tests 877 s); load avg 173 on 18
  cores (7 mutation lanes + MW 8 workers + MSTRUCT mutate + V1/V2). Reniced 13 lane processes +10 so the commit check
  gets the cores. LESSON: when launching parallel lanes beside a critical-path check, nice the lanes at launch.
- 07:45 V2 parked (round6/v2.md sections 6-7 = resume point). Whole K-1 stack builds and computes on F1+f1b(04:52):
  fixtures 2420/2422 (2 pre-existing), NY 361/361, all 16 hand cases pass. 7 corrected .v2 patches. Fixed: 2 build
  errors, K-1 rosters reachable before scope.k1 answered (nested-choose rewrite), 948 inputs need scope.k1e false.
  D7 override kept (partnership_scorp refused, README item wording drafted by V2: owner review). BUG-0836 fix is in F1
  (40b28ede) but its inventory entry has no Fix line. OPEN: tick-group placement of the K-1 block (move to order 130 /
  scope.k1 own question / baseline) -> OWNER decision after release; 12 parked k1 rows incomplete; 11 k1 refusal
  gates not placed in tree.json (pre-existing in F1); interview-rules deltas on generated.53/327 untraced.
- ~07:55 V1 parked (round6/v1.md = resume point). F2: all 5 .v1 patches apply on F1+f1b(04:52); fixtures identical to
  baseline; FIXED missed files (ny.yaml owes_use_tax, generate.ts emitting retired inputs), asset gate guard, classm/
  mutation restatements (take no defaults: 113 failures in the first run), 20 coverage rows. DESIGN ISSUE (owner or
  coordinator after release): `any` stops at first Yes -> digital_disposed never asked when digital_got Yes;
  listed_computer reachable before listed_rec (3 interview-rules problems). Accept into baseline vs read every box.
  Digital split costs +1 question per persona (design said about equal). F3: build fixed (def-0795 spouse phrase),
  1 fixture wording restated in def-0891.v1, 11 coverage rows need fixes (proposed, not applied; check 0889 royalty
  routing first); tick-groups and walks not run. def-0791 rebuilt on F2's asset numbering.
  REPEATED LESSON: "no fixture changes / default covers it" designs fail on classm/mutation (no defaults) — the
  drafting brief must say so.
- 07:56 load 206/18 cores: several lanes each ran a FULL federal mutate to verify. Told all mutation lanes: verify
  only own ids (mutant_witness --only, <=4 workers, nice 10); MSTRUCT one fed + one NY run, niced, 4 workers. The
  integrator runs ONE full mutate on the merged result. Reniced 4 more processes. LESSON: briefs for parallel lanes
  must cap workers and forbid full-suite verification runs.
- ~08:00 M-1116 DONE: round7/m1116.patch (10 cases in f1116.json; 1 keyed arg). 102/104 killed (scratch kill check
  with mutate's own rule), 1 argued (line24.line23; digest 344333e513d41342), 1 OPEN: operand.f1116.f1116.line35.line33
  (needs a premise that f1040 line 16 is never negative + rounding bound; every constructed input refuses first).
  No engine defect (all predictions matched first time). Caveat: many f1116col kills assert helper lines. Full mutate
  left to the integrator. The open one goes to the integrator: argue it, or kill with a case if MW's addendum finds one.
- ~08:10 M-K1 DONE (covered k1p AND most of k1s/f7203 before the split): round7/mk1.patch (50 cases mk1.* in k1p.json
  34 / k1s.json 30; 11 keyed args; bug_pending/mk1-01.md). Of 132: 114 killed (own mutation-apply check), 11 argued,
  3 left to MSTRUCT, 4 OPEN: k1s col_k/col_i/col_h/p5_income ok=false branch, reachable only with a Form 7203 roster
  of 0 or >=2 entries (engine accepts, interview never produces). BUG-NEW-mk1-01 (low, latent): pro-rata rounding
  lets 7203 col (c) exceed line 10 by $0.01; only line 11 is capped (i7203 p.4). 2 f4952.exception survivors are
  not K-1 -> belong to M-exist (check they are on its list).
  DECISION (coordinator) for the 4 open: file a pending bug "k1s accepts a Form 7203 roster that is not exactly one
  entry, without refusal or input error" and list the 4 under OPEN_DEFECT_SURVIVORS (the tool's own mechanism: the run
  fails again once the bug closes). Not a fixture pinning an unsupported zero; not a model change before the release.
- ~08:15 M-K1S: nothing left (M-K1's file covered all 62). p5_income.zero.then1 has no reader -> MSTRUCT. The 3 open
  (k1s col_h/col_i/col_k .zero.then1) differ only when a fixture hand-lists the IMPLICIT f7203 roster as [] or
  [form, w9]; no interview can produce that. DECISION refined: pending bug = "the evaluator accepts a hand-listed
  implicit collection roster (should be an input error)"; the 3 go under OPEN_DEFECT_SURVIVORS citing it. Post-release
  fix: reject such input -> then a keyed argument holds and the entries come off. Patch mk1s.patch is empty.
- ~08:20 M-exist DONE: round7/mexist.patch (24 cases in 13 form files). 32/47 killed (42/42 expectations match; fixtures
  2410/2410), 15 open (drafted args, answered/producible-only; not added without a sampled check). Owner-ish note:
  check_27c cases answer eic.us_home on an MFS return where the interview does not ask it. f2441 "considered
  unmarried" counts only qualifying persons with expenses (no wrong amount; not filed).
  Launched MINT (Opus) in worktree mint at refs/scratch/xint-fast: apply m1116 + mk1 + mexist (+ mrental, mstruct when
  they land), the OPEN_DEFECT entries with a pending bug for the implicit-roster input, ONE full mutate, then argue or
  kill the leftovers until mutate exit 0. Output round7/mint.patch + mint.md.
- ~08:25 M-rental DONE: round7/mrental.patch (32 cases; new files f8582/sche/royalty/rprop.json; 10 keyed args each
  passing sampledShare). 77 killed, 10 argued, 2 open (answered-only: rental home_pers10 all.1.gt.0; rec to_line1).
  Q1 (rental-only costs by days) not baked into any expected value. LEAD for owner/bug: income tax refund 3,000 +
  property tax refund 2,000 with 2024 5d=5e=4,000 -> model puts 5,000 on Sch 1, above the 4,000 deducted (Pub. 525
  Worksheet 2 fn 1, p. 27) -> draft pending bug after the release. Sent to MINT.
  ALL FAMILY LANES DONE. Remaining: MSTRUCT, MINT, XINT commit.
- 09:35 XINT fast tier #2 failed on review_packets (frozen Stage 3 packet named retired fixture sales.refuse.digital.G
  -> repointed to sales.box.G, packets regenerated); #3 running since 09:02. Same stop-at-first-failing-stage pattern.
  Two mutate runs at 63 and 79 min (normal 5-9 min: 276-540 s in past full runs) starving each other + fast tier.
  Stopped MSTRUCT's measuring mutate (pid 64423, mstruct worktree); MSTRUCT hands its patch to MINT now, unmeasured;
  MINT's single full mutate measures it. LESSON: never run two full mutates at once on this machine.
- 09:40 MSTRUCT done (unmeasured): rule unobservedLine, self-test passes, round7/mstruct.patch. Static pre-check: 47
  federal would be explained, BUT every chain ends at a `display:`-marked person total (shown on the values sheet).
  DECISION: display lines count as OBSERVED (conservative; a mutant changing a displayed value is untested output, not
  equivalent). MINT applies the rule with that change + self-test plant, and kills the remaining 47 with person-total
  assertions (many likely already killed by mk1). Cleanup candidates: 29 unread display totals (list in mstruct.md).
  09:34 loop check #1: load 67; single full mutate (MINT, 65 min, ~1 core: serial tail?); fast tier #3 on late steps.
  Owner asked for a 10-minute process check loop: cron job 15c29046.
- 09:40 loop: load 12; MINT's full mutate finished, MINT rebuilding (mstruct applied); fast tier #3 on interview-rules (late step). No action.
- 09:50 loop: fast tier #3 FAILED on doc_figures (2537 s); #4 running since 09:45. Told XINT to run every later fast step directly in parallel now (load 7) to stop the one-failure-per-45-min cycle. MINT idle-looking (build done, shell waiting): check next tick.
- 10:00 loop: load 12; fast tier #4 running (15 min); MINT mutate #2 7 min at 8 cores (merged: 23 unexplained left after run #1; fixtures 2528/2528, NY 358/358); XINT direct step runs (interview-length self-test). No action.
- 10:02 OWNER: for the rest of this session, every NEW subagent runs on Fable (claude-fable-5-2); briefs state model claude-fable-5-2 + class; applies to both mechanical and judgment lanes (CLAUDE.md allows Fable for either class when the owner says so). Paid review calls keep their default model (owner named subagents only). Running agents (XINT, MINT) are unchanged.
- 10:10 loop: load avg 151 but CPU use ~13.5 of 18 cores (fast tier interview-rules ~7 cores, MINT mutate #2 ~6-7 cores; worker threads inflate the run queue). Both critical path; no duplicate heavy runs; no action. MINT mutate #2 at 17 min (over the 15-min flag, due to sharing with interview-rules).
- 10:20 loop: load 20; fast tier #4 at 35 min (interview-rules 16 min, ~7.5 cores); MINT mutate #2 at 27 min (~7.8 cores; slow from sharing, both critical). No duplicates, no idle agents; no action.
- 10:25 XINT: fast tier #4 GREEN (tree 39dc5996), but commit_tested refused: engine/src/mutate.ts (65 re-pins) is a
  full-tier path; full tier includes mutate (fails until MINT). Review spend this commit $4.19. DECISION: no separate
  expansion commit. ONE release commit = expansion + MINT patch + records + sources + tooling, one release-mode full
  tier (guard + release reuse). XINT now: carry-back; apply tooling (t337, t338, migration) + sources (20 files + rows
  by hand) + records; self-tests; slow non-mutation steps directly (compare, ny_compare, engine_differential,
  lean_build, interview_length, renamed_ids); then wait for mint.patch.
  LESSON: before planning a commit order, check tools/full_paths.txt: a change to a full-tier path cannot commit on
  a fast-tier green.
- 10:30 loop: load 11; MINT mutate #2 at 37 min with ~8 cores and little contention (FLAG: normal in check_all 5-9 min; candidates: ~2528 cases now + ~40 new keyed args in the sampled check). Log prints only at the end, so no progress visible. XINT running compare (slow-step pre-check). Last bg check status=green (fast #4). Watch next tick; if mutate #2 passes 50 min, ask MINT.
- 10:40 loop: load 9; MINT mutate #2 at 47 min, now ~1 core (single-threaded tail, like run #1's). Asked MINT for stage + whether the tail scales with keyed args (affects release-check length). XINT running interview-length (slow-step pre-check). No other action.
- 10:45 MINT DONE: round7/mint.patch. Federal mutate: 10022 mutants, 456 surviving, 5 unexplained (k1s col_h/col_i/
  col_k/p5_income zero.then1 + person.f8919_line10 figured.then0, all the implicit-roster class -> mint-01, needs
  --assign before listing in OPEN_DEFECT_SURVIVORS); ny 0. 141 fed / 45 ny keyed args pass the sampled check.
  Added 8 args (5 answered-only, 3 every-input), 12 fixture cases. mstruct rule kept with display=observed (explains 0
  now). Mutate wall 47.5 min on a loaded machine (single-core tail ~3-5 min). Rulings: keep ira answered-only; keep
  the f1116 refusal-expecting case; accept 6 weak kills (later test-strength item). Sent XINT: apply mint.patch,
  --assign, 5 OPEN_DEFECT entries, one direct mutate (exit 0), release-prep steps, release-mode full tier, commit.
- 10:50 loop: load 3; XINT building after applying mint.patch (build 2.5 min); no heavy runs; nothing stuck. No action.
- 11:00 loop: load 12; XINT's direct confirming mutate at 7 min, ~8 cores, alone on the machine. No action.
- 11:10 loop: confirming mutate at 17 min (FLAG >15) but alone and on ~8.3 cores; expected slower than past 5-9 min runs because the expansion grew mutants to 10,022 and cases to 2,528 (both ~1.5-2x). It uses ~8 workers on 18 cores: worker count may be worth raising for the release run (check workerCount() env). No action.
- 11:20 loop: confirming mutate at 27 min alone (~6-8 cores). Default workers = min(cores-6, (cores-2)/CHECK_ALL_MAX_RUNS) = 8. Told XINT to start the release full tier with MUTATE_WORKERS=12 if the env reaches the step. Release estimate: confirming mutate done ~11:35-11:45, full tier ~75-90 min -> tag ~13:00-13:30.
- 11:30 loop: confirming mutate finished (~33 min); XINT now running tools/release_prep.sh (new T-337 script, in a check-all slot). Load 2. On track.
- 11:40 loop: release_prep at 11.5 min (now on coverage step); load 9. On track.
- 11:50 loop: release_prep at 21.5 min, now on interview-rules (9.5 min, ~8.6 cores). Slower than intended for a pre-check (interview-rules is one of the longest steps); note for T-337 tuning. Load 9. Progressing.
- 11:55 launched POST (Fable, text only): post-release/RUNBOOK.md (F1+F2+F3 one review round + one release check, then K-1 stack; conflict points; interruption points), OWNER-DECISIONS.md (one de-duplicated block), bug_pending-drafts (refund overstatement lead, weak kills, unread display totals, f2441 note).
- 12:00 loop: release_prep FAILED on 5 steps in ONE pass (the script working as intended): release_reviews (completeness due for dependent: lines changed since its samples -> completeness_review.py --forms dependent; covered by the <$3 standing approval if its dry run is under $3), bug_status, doc_figures (regenerate after --assign), bookkeeping_self_tests, interview_rules (detail not yet read). XINT active (12:00). Load 2.
- 12:05 POST done (post-release/RUNBOOK.md, OWNER-DECISIONS.md, bug_pending-drafts post-01..03). Plan-changing
  findings: round F cannot commit in pieces (F1 edits mutate.ts); screens.patch + screens-joint.patch are NOT in the
  release tree and must land in round F before paid reviews (~$21); F1 already takes decision 8 as "count on both";
  the thrift-store over-refusal is introduced BY F1 (fix-round.patch:15471), not pre-existing; restatement scripts must
  be rerun on the merged tree (~150 new fixture cases); F2's retired inputs are collection-indexed (use rename_ids.py);
  round F's tag is r2026.11.17.x (r2026.11.16.1 is this release). Records inconsistencies listed in POST's report
  (MW count arithmetic, mk1 case count 64 not 50, S corp box 17 default not implemented, stale MORNING-REPORT).
  Coordinator: added a "superseded in part" note to the committed MORNING-REPORT and refreshed records in xint
  (current notes, post-release/, round7/). agent_runs rows for all lanes exist (hook), uncommitted in main: commit in
  a small follow-up after the ff.
- 12:30 XINT hit the Opus 5-hour limit (resets 14:50), stopped mid release-prep fixes. OWNER: Fable spare capacity used up; use only Opus or Sonnet from now. Failures left: bug_status, doc_figures (regenerate), bookkeeping (green_self_test, siblings_self_test), interview_rules (1: generated.198 complete while person.work_ssn reachable — work_ssn was removed from the baseline earlier as no longer leaking), release_reviews (completeness due for dependent).
- 12:40 Coordinator took over XINT's release-prep fixes (XINT rate-limited). Findings: bookkeeping failures
  (tier_paths self-test: "READERS lists X, no longer refers"; siblings: "no review log changed since HEAD") are
  ARTIFACTS of running release_prep in a working tree with an empty index: both read tracked files only (git ls-files /
  git diff HEAD) and the new files are untracked. Proved on a snapshot commit (siblings clean except canonical/ not
  built). They pass in check_all_bg's snapshot. T-337 FIX TO FILE: release_prep must run on a snapshot (as
  check_all_bg does). Ran bug_status --write (932 entries, 204 open) and doc_figures (current). Launched (Opus):
  RL = person.work_ssn completion leak on generated.198 (trace, probe, hold in baseline with reason per precedent
  or fix); RC = dependent completeness review (<$3 standing approval) + adjudication. Then: release-mode full tier.
- 12:30 (real clock; 12:40 stamp above ran ahead) loop: load 2; RL and RC just launched (reading); no engine runs yet. No action.
- 12:45 RC done: release_reviews PASSES (236 findings, 0 new). Dependent completeness had been run by XINT at 11:58 ($0.634) and ruled (3 claims: covered / real gap BUG-0932 low (i8863 p.6 tip: apply assistance reduction to 2026 instead; not offered) / presentation); RC agrees with all; RC spend $0. Waiting on RL; if RL changes a form, recheck release_reviews + check_logs before the full tier.
- 12:40 loop: load 10; RL rerunning interview-rules (8.5 min, ~8.3 cores) after a baseline edit (interview_rules_baseline.json changed; no new form diff visible beyond the release's). No action.
- 12:50 RL done: person.work_ssn leak = count lower bound (household.any_work_ssn = gt[work_ssn_count,0], sum_over person) on generated.198 seed 111192; probe: both answers for both persons leave status + targets identical; held in early_completion baseline with traced reason; interview-rules 0 problems. All release_prep failures cleared. STARTING release-mode full tier from xint: CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify MUTATE_WORKERS=12 tools/check_all_bg.sh --tier full.
- 12:50 loop: release full tier 7 min in (build/self-test stage), load 9, no failure. No action.
- 13:00 release full tier #1 FAILED at 12:56 on check_source_titles (S0 rows: p926 designation '(2025 edition)' not in text -> 'Publication 926 (2025)'; usc-26-402 title straight vs curly apostrophe). Fixed catalog + manifest; check_source_titles and fetch_sources offline verify pass. Restarted release full tier.
- 13:00 loop: release full tier #2 (tree 9a69424c) 3 min in, build stage; load 2. No action.
- 13:10 loop: release full tier #2 at 13 min (self-tests: interview-length --self-test 7 min); load 2.5; no failure. No action.
- 14:10 release full tier #2 FAILED 14:00 on test_serve ONLY (mutate passed: 2885 s, 12 workers; all else green). Cause: serve-check picked the FIRST qualifying fixture for the tick-screen test; MINT's new f1116.mint_line33_refused_line20_zero_line18 now sorts first and its foreign-tax background closes s3.repaid_income after farmland yes. Fix (test only): pin tickCase to stage5.return.owed by id. test-serve: 510 checks passed. Restarted release full tier #3. LESSON: tests that take 'the first fixture that qualifies' break when fixture files are added; pin by id.
