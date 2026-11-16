# Plan: finish consolidation and fix the meaningful known bugs (goal 1), with an outline of goal 2

Written 2026-11-15 by a planning agent (claude-opus-5-5, judgment, year 2025, jurisdiction us). Read-only: nothing in
any checkout was changed. Base tree: `.claude/worktrees/sweep-tasks` at `63a20efc` ("snapshot: ty26 batch rehearsal
intB"), which is the landing of the interview redraft plus 2026-preparation batches A and B, not yet on main.

Labels: **[V]** verified here (command or file named); **[T]** testimony from a project doc or lane note, not
re-measured; **[I]** inferred.

---

## 0. Where things stand

- Main is `83c7d1c0`. The landing tree and batches A/B are snapshots that are not merged yet. 25 `bug_pending/`
  entries are waiting for `new_bug.py --assign` [V `ls bug_pending`]. The last inventory id is BUG-0630 [V].
- The `HANDOFF-NEXT-SESSION.md` top entry in this tree is still the 11-11/12 entry [V]. The landing's handoff has not
  been written.
- Releases: the latest is `r2026.11.09.1` [V `git tag`]. A release is the milestone for the sampled reviews
  (release gating design; `tools/release_reviews.sh`) [T].
- T-299, the landing review round. Transcription, render and class M ran on the landing tree: 290 calls, $109.39 since
  11-14, in `.claude/worktrees/landing/.transcription/costs.jsonl` [V]. They were adjudicated by lanes
  land3-adj1..14 [T]. Four fix lanes followed (land3-holes, -fix, -sa, -screen), and each one's dry run needs
  `--approve-cost`:
  - scope and s2: $3.45
  - f1095a and f8962: $3.56
  - sa: $3.53
  - ira, scveh and person (transcription): $3.30

  Whether those reruns ran is not established [I]: the lanes say "no job was run" [T]. The sampled screen, false-no,
  question and completeness reviews have not started. A worktree `nx-sampled` exists at "landing tree for the sampled
  release reviews" with no new calls [V].
- `.claude/worktrees/nx-r5` and `nx-protocol` exist at `63a20efc` with no changes [V]. They look like reserved lanes
  for the R5 rehearsal and the goal-2 protocol [I].

---

## (a) What remains of the consolidation

Each charter item below was checked against the tree, not against the charter's own status text.

| # | Charter item | State | What "done" means, and how to verify it |
|---|---|---|---|
| C1 | §8.1 / §7 rollover procedure | **Built** [V]: `changes/2026/` (56 files), `tools/year_changes.py`, `propose_params.py`, `extract_printed_tables.py`, `layouts.py`, `year_carry.py` (writes rulings sidecars), `years.json` `ny_adopted`, `extends_with_year` and `moves_with_year` (14) in `params/2025.yaml`. **Open:** (1) the R5 draft-adoption rehearsal was never run: no `tools/year_rehearse.sh`, no rehearsal doc [V]. (2) BUG-NEW-ty26-o2-01 / o6-01: `write_state` drops YAML anchors; aliases exist in `f1095a` (75), `f8962` (17), `sc` (13) and `retirement` (3) [V grep]; adoption would write a form that does not parse. (3) BUG-NEW-ty26-o5-02, second half (twins' declared differences under 2026 operations) [T r2]. (4) T-300, year literals in text (charter 7.4, second half). | (1) `tools/year_rehearse.sh` runs the whole draft adoption in a scratch copy (`year_diff --adopt`, staged params and tables, `build --year 2026`, `fixtures_year`, `test-fixtures`, `year_carry` dry run, `rerun_all --dry-run`). A dated doc then lists zero unexplained failures and **re-measures the charter §7 numbers**: missed changes, mechanical parameter share, tables made by hand, fixtures re-recorded, review estimate. That re-measurement is the charter's stated yardstick. (2) A self-test plants an alias case and `--check` refuses or expands it. (3) `check_twins --year 2026` passes in the rehearsal. (4) Decision D11. |
| C2 | §8.2 content-addressed review logs | Done [T T-256]. `tools/transcription/review_store.py` exists [V]. | none |
| C3 | §8.3 second family inactive | Done [V `families.json` `active`: deepseek and gpt false] | none |
| C4 | §8.4 check-all folding; `human_review`, `review_stage2..5` | Done: no such step in `tools/check_all_steps.sh` [V grep]; `tools/self_tests.py` exists [V]. | none |
| C5 | §8.5 the 22 tech-debt rows | **Partly.** The inventory §5.1 dispositions [T] left some deferred because the gate-wave lane owned their paths; that reason has expired. **5.1a** `person.yaml` is 6,425 lines [V]. **5.1b** the Form 8863 duplication, kept in step by `check_twins` (BUG-0600) [T]. **5.2d** the SEP rate is faked: `person.cent` / `person.hundred` [V]. **5.3b** the legacy profiles `social-security`, `sales`, `stage4` are still loaded (`engine/src/interview.ts:140`) [V], and BUG-0432 says the default profile fails to start [T]. Proposals still open: **2.6** `compare.ts` has its own generator (`generatedCases`, line 75) [V]; **3.4b** Lean batch mode; **5.4c** = T-262. Partials: **1.3** (22 steps drop `"$@"`), **2.1** (`mutate.ts` compares `=== "(helper)"`), **2.3** (`properties.ts` regex), **2.5** (dead `bracket_schedule` / `opaque`) [T inventory]. | Each row has a final disposition (fixed or won't-fix with a reason) in a dated doc. The rows fixed under D10 pass check-all. Verify by re-running the inventory's greps on the merged tree. |
| C6 | §8.6 `tools/` scripts | Done [T inventory §4.1, phase 1 note] | none |
| C7 | §8.7 / §6 conventions | Done: `interview/<year>/` and `interview/ny/<year>/` [V]. The `adapter_contracts/2025` layout was ruled conforming [T inventory §6.1]. T-256's "adapter_contracts/2025 remains" is stale bookkeeping. | Correct the T-256 status text. |
| C8 | §8.8 tracked-but-ignored files | Done [V `git ls-files -ci --exclude-standard` = 0] | none |
| C9 | §9 retired docs carry a banner | Done [V: all four] | none |
| C10 | §5 advisory rules (4) | Allowed by the charter as advisory | none (D-note: leave them advisory) |
| C11 | Phase 3 close (T-299) and adoption of the redraft | **Open.** Four things remain: the post-fix reruns of eight forms; the sampled reviews (dry runs: federal screen 185, false-no 142, question 748, completeness 62; New York 32 / 23 / 52 / 4) [T T-299]; a release; and the owner's adoption, since `CLAUDE.md` still calls the redraft provisional [T land3-docs]. T-312's unsettled redraft choices also remain. | `check_logs.py` has no stale or open ruling for transcription, render or class M. `release_reviews.sh` passes (no form short of its sample, no unruled finding). `tools/release.sh` tags `r2026.11.<d>.1`. `DECISIONS.md` settles every T-312 item. The owner adopts, and `CLAUDE.md`'s provisional sentence is removed. |
| C12 | Validation policy, item 4 (the charter cites it) | **Open:** mutation-equivalence mechanization (T-280: 90 pinned prose arguments, 361 survivors; no machine backing) [T]. The year-adoption rehearsal is C1(1). Citation precision is T-094: 588 baseline entries, due line by line by rule, so it is not a blocker [T]. | `mutate` re-checks each pinned argument on a generated sample at several withheld-answer rates, with a known-killed control, inside check-all's full tier; T-250's 8 answered-only pins are killed or re-argued. |
| C13 | Engine semantics on incomplete returns (T-249, T-250, T-292; BUG-0430, BUG-0083) | Open since 11-05, deferred twice | Decision D7. If kept as is, close all three with the reason. |
| C14 | Bug-inventory status is not machine-readable (found here) | Of the 630 entries, 226 look open by their own fields. 107 remain after subtracting "BUG-x is fixed" entries [V script]. Many of those are closed only through TASKS rows (T-063/064/065/175/180/222/229/233/264) or later lanes, with no closure entry. | Decision D8: add `tools/bug_status.py` and closure entries; check-all fails on an open entry that neither a TASKS row nor `reports/bug_status.md` names. |
| C15 | Docs truthfulness (T-246, T-294, T-034) | `reports/2025/filer_coverage.md` is from 11-01 and lists gates that no longer exist; the tree has 234 gates [T land3-docs]. Figures in README and TRUST are stale [T]. | After the release: regenerate the estimate, and add a check that fails when the estimate's gate list differs from the forms. README and TRUST quote only regenerated figures. |

TY2026 work that waits for IRS finals (T-296 remainder, T-297; ty26-plan waves 3 and 4) is not consolidation. It stays
on its own track. Only C1's tool defects and the rehearsal are in goal 1.

---

## (b) Open bugs, triaged

Classes:
- **M1:** a wrong completed return (a value, a missing required form, a wrong printed box).
- **M2:** a refusal of a return the tool's declared scope should compute, reachable by a real filer.
- **M3:** question text a filer would plausibly misanswer, with M1 or M2 as the consequence.
- **MT:** a check or review tool that misses defects.

Not meaningful:
- **NC:** cosmetic (label, citation, display with no amount changed)
- **NU:** unreachable or vanishingly rare
- **NS:** superseded, fixed, or closed elsewhere (needs a closure entry only)
- **ND:** an owner decision already taken

"chk" means the current text was spot-checked here by a pattern grep over form source + bank prompt/help [V]: "open"
means the fix's wording is absent. Rows without "chk" relay the entry [T].

### b1. Meaningful: wrong value or missing form (M1)

| Bug | Form | Sev | Reason |
|---|---|---|---|
| BUG-0593 | refund | (none stated) | A joint 2025 return after separate 2024 returns runs both spouses' state refunds through one 2024 return; Schedule 1 line 1 can be wrong either way; no gate catches it. Reach: newlyweds and couples who switched from married filing separately. |
| T-304 (item 1) | household | — | A filer entitled to head of household who picks "None of these" gets single rates and is told nothing: a higher tax, silently. |
| BUG-NEW-ty26-o9-01 | sc | — | 2025: home storage space is counted without the "sole fixed location" test, so the simplified home office deduction is overstated (p587). |
| BUG-0488 | sales | — | Three rules not asked: a loss after an extraordinary dividend, constructive ownership gain, and same-day blocks netting a wash loss. Rare, but each gives a wrong gain. |
| BUG-0451 | sd, scope | low | A qualified opportunity fund deferral of a gain with no sale entry (box 2a) is neither asked nor refused. chk open. |
| BUG-0510 | scveh | low | The SUV exception drops the integral-enclosure condition, so the $31,300 cap is escaped. chk open. |
| BUG-0535 | f8889 | low | An excess employer contribution partly in box 1 cannot be entered (yes/no): income doubled or omitted. |
| BUG-0615 | s1 / HSA | low | A Medicare Advantage MSA or Archer MSA distribution with no HSA: the return completes without Form 8853. |
| BUG-0618 | f8889 | low | Divorced or widowed in 2025: the then-spouse's family coverage months are figured at the self-only limit. `household.ever_married` now exists, so the blocker is gone. |
| BUG-0548 (2) | person | low | A prior-year SEP excess carryover is asked nowhere, so the deduction omits it. |
| BUG-NEW-land3-adj8-01 | f1095a / f8962 | low | Month-varying Part III with no advance credit payments (APTC) or another doubt about column B: Form 8962 line 10 is No where it should be Yes, so the line 10 box and a few dollars are wrong. |
| BUG-0597 | f5695 | low | A spouse's own 2024 carryforward on a joint return. The instructions are silent, so this needs an ambiguity register entry and a choice. |
| BUG-0620 (11) | s3 | low | A section 965 installment payer under 10% never reaches the line 13d question. |
| T-310 (l8a) | f8962 | — | A person on someone else's Marketplace plan with no Form 1095-A is asked nothing. |
| T-310 (l7b) | s2 | — | `s2.mortgage_subsidy` is missed after a loan payoff and sale. |

### b2. Meaningful: question text misanswered (M3), value consequence

| Bug | Form | Sev | Reason |
|---|---|---|---|
| T-307 | s2 / Form 6251 | high reach | "Do you owe AMT or need Form 6251?" is asked of everyone, and a typical filer cannot answer it without the arithmetic. A wrong No leaves out the tax. Remedy: a computed screen from the first lines of Form 6251 (new arithmetic). |
| BUG-0447 | f2441 | **medium** | "so that you could work" lets a married filer whose spouse studied or was disabled answer No, losing the credit. chk open: the prompt still reads "so that you could work". |
| BUG-0433 | scope | low | The Form 8615 condition omits "capital gains, capital gain distributions". A child with fund distributions answers No, and the kiddie tax is omitted. chk open. |
| BUG-0531 | eic | low | The military sentence of the US-home question names only "you", so a joint filer with a deployed spouse can lose the EIC. chk open. |
| BUG-0459, BUG-0573 | sa | low | Lines 8a and 11 state no reductions (mortgage interest refund, points; raffle, political). The deduction is overstated. chk open. |
| BUG-0443, BUG-0453 | f8889 | low | Line 15 does not say that items not on Schedule A count; HDHP tests, cash-only, insurer contributions, excess withdrawn after the due date. chk open (0443). |
| BUG-0436 | sales | low | `sales.code` does not name nominee or personal-use loss adjustments, so a gain or loss is reported that should be zero. chk open. |
| BUG-0438 | s1 | low | `s1.line8r` misses the part of a grant paid for required services, so income is understated. chk open. |
| BUG-0517 | div | low | Amounts with no form, or paid in another's name, are left out of box 12 and box 3 (social security worksheet, MAGI). chk open. |
| BUG-0518 | sd | low | No 2024 return: the filer answers No and loses the carryover. chk open. |
| BUG-0541 | qbi | low | The 199A holding period is not stated, so Form 8995 line 6 is overstated. |
| BUG-0571 | f4952 | low | A spouse's separate 2024 carryover. chk open. |
| BUG-0456 = BUG-0490 | person | low | The SIMPLE salary-reduction deferral has no deposit or due-date condition (one defect, two entries). chk open. |
| BUG-0547, BUG-0548 (1, 3-5), BUG-0549 | person | low | IRA, SEP and SIMPLE, and person-record wording lows. Mixed: some values (basis, the excess deferral), some refuse only. |
| BUG-0503, BUG-0546, BUG-0455, BUG-0569 | person / dependent edu, f8863 | low | Education wording: attendance fees, the outside-materials gate, the scholarship inclusion limit, the Form 1098-T date against `amb.2025.edu_1098t_date`. |
| BUG-0520 | ira | low | Deferred compensation that is not in box 11 escapes the screen; compensation is overstated where it limits the deduction. |
| BUG-0534 | f2441 | low | Benefits outside box 10; the spouse's plan maximum and grace-period carryforward. |
| BUG-0529, BUG-0559 | sc, scveh | low | Schedule C expense, cost-of-goods and vehicle lows with rare value effects. |
| BUG-0537, BUG-0515 | otjob, carloan | low | Overtime period and mixed-rate totals; carloan rebates and refinance chains. |
| BUG-0539 | s1 | low | Canceled-debt timing, a child's Alaska dividend, prize points. |
| BUG-0563 | sli | low | "for that year" (the loan year). |
| BUG-0576, BUG-0594 | sb | low | The foreign account is undefined, so line 7a prints wrong; a foreign nonprofit's board member misses the Form 5471 refusal. chk open (0576, 0594). |
| BUG-0449, BUG-0491, BUG-0521, BUG-0551, BUG-0424 (T-244) | ny_it201, ny_it2 | low | New York: 529 "part" of a refund (the election is lost; chk open); DMV use tax (overstated; chk open); W-2c figures; residency carve-outs (mostly refuse more). |
| Land3-fix residual | f1095a | low | Monthly route: a filer with no APTC is not told column B may be wrong. |
| Land3-sa residual | sa | low | `sa.state_tax_other_any` omits the charitable tax-credit safe harbor. |
| T-310 (l2b, l6b, l9) | eic, dependent, scveh, sc | low | Questions asked of the wrong filers. Mostly length; check each for a value case while in the form. |

### b3. Meaningful: refused where it should compute (M2)

Each of these is fixable by wording, with no new arithmetic, unless marked.

| Bug | Form | Reason |
|---|---|---|
| BUG-0507 | otjob | **Real reach.** "Is this *employer* covered by" 7(j) hospitals, so a hospital nurse paid under the general 7(a) rule answers Yes and is refused. chk open. |
| BUG-0511 | tipjob | "not paid in cash (including by check ...)", so a casino dealer tipped in chips is refused (a common tipped occupation). [V the text at `tipjob.yaml:91`.] |
| BUG-0504 | f8962 | Married in 2025 with no APTC or no excess APTC is refused. chk open (`married_this_year`). |
| BUG-0505, BUG-0540 | ftc | The small-tax election: high-taxed passive income; the carryover phrase. chk open (0505). |
| BUG-0506 | gift | Certain other securities of Section A are refused. |
| BUG-0572 | f8863 | The Form 8862 exception names only 2024. chk open. |
| BUG-0519, BUG-0530 | household, sc | Marriage and community property; at-risk qualified nonrecourse; spouse's hours; chapter 11 as a creditor. |
| BUG-0613, BUG-0614, BUG-0616 | f8889 | A surviving spouse's inherited HSA; an untouched Archer MSA; the testing period wider than Part III. One child question each, with no new arithmetic [T entries]. |
| BUG-0620 (3) | s3 | Over-refusals: AMT from exclusion items, a stepchild adoption, an adoption not final, a bond issuer's election. Each closes with one question beneath. |
| T-311 (qc_tiebreak) | dependent | Refused where every other claimant is not a taxpayer. |
| T-291 | f8889 | Excess contributions withdrawn by the due date. The owner's own past situation. **New arithmetic** (lines 2, 13, 14a/b, earnings next year), so it is coverage expansion. Decision D1. |

### b4. Meaningful: tools that miss defects (MT)

| Bug | Tool | Reason |
|---|---|---|
| BUG-0602 (with T-276, T-290) | `engine/src/interview-rules.ts` | It classes 3 generated returns; at 200 returns it reports 23 problems on unmodified data. A pass says little. Medium. |
| T-280 | `engine/src/mutate.ts` | 90 pinned prose equivalence arguments that no machine checks (C12). |
| T-311 (`mutation.json`) | fixtures | 232 of 245 mutation cases do not state `f1040.withheld_other_any`, so lines 25b-d are unknown and cannot kill downstream mutants [T re-measured by land3-tasks]. |
| T-262, T-306, T-270 | `engine/src/generate.ts`, `classm.json` | The class M corpus has impossible people: 11 of 266 are married filing jointly yet unmarried; 60 have contradicted birth years; 16 have dependent ages. Two inputs are never generated, so every reader is unknown in Lean and properties. Evidence about values the cases do not describe. |
| BUG-NEW-land3-adj11-01 | `engine/src/classm.ts`, `classm.py` | New York class M prompts give rate-schedule results as unnamed (39)/(47a), so the Tax Table lookup cannot be worked and the reviewer copies a given. |
| T-316 | `triage`, `rule.py`, `siblings.py`, class M generator | Triage ignores the reply's `shown_when`. `siblings.py` reads "none" as empty and counts a fix's own lines. The class M generator spends cases on returns the tool refuses; W-2 box 3 is always 0 in stage-derived cases. |
| Land3-screen "not addressed" | `transcribe.py` `Expander` | References to two different screening inputs expand to the same `(screen)`, so the comparison cannot see a swapped screen. |
| BUG-0445 | `screens()` | A gated refusal screen leaves the screen review. **Verify:** BUG-0448 looks like its fix [I]. |
| BUG-0129 | `transcribe.py` `Expander.ref` | An untyped month constant can show AGREE on an invalid comparison. **Verify:** no closure found [I]. |
| BUG-NEW-ty26-o2-01 / o6-01 (one defect) | `tools/year_changes.py` | Drops YAML anchors, so adoption writes a form that does not parse (C1). |
| BUG-NEW-ty26-o5-02 (rest) | `year_diff` / twins | The twins' declared differences are not restated (C1). |

### b5. Not meaningful (with reason)

- **NC, cosmetic.** These ride with their form's next substantive change, which for most is a lane below.
  - BUG-0184 (sd labels say "/carryover")
  - BUG-0341 (ambiguity register reading stale; record evidence only)
  - BUG-0489 (a REFUSED helper on the values sheet with no home office; no outcome change, but visible, so fold into F5)
  - BUG-0570 (refund election amounts unbounded and read by nothing; builder wording)
  - BUG-0562 (column (e) is presentation only)
  - BUG-0565 (asset presentation lows)
  - BUG-NEW-land3-adj5-01 (Form 2441 Part III lines shown with no benefits; fold into F2)
  - BUG-NEW-land3-adj6-01 (vehicle worksheet lines past the stop notes; fold into F5)
  - BUG-NEW-land3-adj9-02 (s1 cites)
  - BUG-NEW-land3-adj9-03 (sd label)
  - BUG-0626 remainder (the `s1.yaml:240` wording "section 3.32") [T p1r4]
  - BUG-0439 (NY line 1 cite)
  - T-311: the `sb.unsupported_if_income` label; the `eic.clergy` refusal text; Schedule A line 13 vs line 15 (the return is refused either way)
  - T-316: the `bonus_same` default reason
  - T-316: personas numbered 13
- **NU, unreachable or vanishingly rare.**
  - BUG-0508 (several survivor annuitants)
  - BUG-0532 (covered by the same question's sentence)
  - BUG-0554 (plain in asking order)
  - BUG-0555 (refusal-only, or $150 capped)
  - BUG-0560 (refusal-only)
  - BUG-0509 (the detail route gives the same gain)
  - BUG-0575 (same gain; futures contracts)
  - BUG-0502 (1040-NR: other clcw lines name it now [V])
  - BUG-0465 (questions only)
  - BUG-NEW-ty26-o7-01 (2026; believed empty because depletion is refused)
  - T-316: `asset.screen` with an election out when `bonus_same` is false (the other property refuses the return) [T land3-adj4]
- **Questions only (no value; interview length).** Work on these is T-276, T-290, T-302 and T-308, which is
  interview quality, not bugs by the owner's definition: BUG-0466 (resolved under T-264 [T]; residuals are BUG-0602),
  BUG-0430 (mid-interview only, labelled provisional; C13), BUG-0605, BUG-0606 (test data; no asserted value wrong).
- **ND, owner decision.** BUG-0595 (11-10: follows the printed line 8), BUG-0083 / T-249 (kept open, C13),
  BUG-0620 (1, 2) (owner judgment of the slice).
- **NS, needs a closure entry only** (lane T1 verifies each, then writes `Closes:`):
  - Closed by tasks: BUG-0134 → T-063; BUG-0135 → T-064; BUG-0138 → T-065; BUG-0314 → BUG-0393 / T-175; BUG-0327 → T-180; BUG-0402 → BUG-0408; BUG-0414 → BUG-0415; BUG-0417 → BUG-0418.
  - Fixed in place or with documented limits: BUG-0166/0167/0168 (fix written in the Where field; 0167 says "open in the same tool: about 15 ...", so verify); BUG-0189, BUG-0257 (with T-093's documented limit), BUG-0279, BUG-0323, BUG-0415, BUG-0583.
  - BUG-0199 (a disposition entry).
  - BUG-0435 (chk: code S SIMPLE rule present [V]); BUG-0450 (chk: Zone 2 counties in help [V]).
  - BUG-0444 (no fix field; the spouse-wording lanes likely closed it, verify) [I].
  - BUG-0601 → BUG-0604.
  - BUG-0627 (corrected by P1 [T p1r4]).
  - BUG-0629: all nine items fixed by R1, R2, R3, R4 and R6 [T lane notes; not re-run].
  - BUG-0625 / T-283 (diagnosable; wait for the next red run).
  - Pending entries already carrying a fix: land3-adj10-01, adj5-02 (= adj9-01, a duplicate), adj7-01, adj9-04, landing-05, landing-08 (fixed by land3-holes [V their Fix fields], which makes T-310's text stale), ty26-o3a-01 (R3 follow-on), o3b-01, o5-01, o6-02, o8-01, p2-01, r2-01.

Count: about 60 meaningful items in roughly 35 forms, plus 11 tool items. Nearly all are low wording, but they are
reachable. The ones that matter most by reach and stake are T-307, BUG-0593, T-304(1), BUG-0447, BUG-0507,
BUG-0511 and BUG-0602.

---

## (c) Lane plan

Standing rules for every lane:
- Each brief states Model, `Class:`, `Year: 2025` (2026 for T6), `Jurisdiction:`.
- Work happens in a worktree (`tools/worktree_data.py clone`; `carry-back`). Each lane claims its forms
  (`python3 tools/claims.py claim <forms> --reason "goal1 <lane>"`).
- Defects go in `bug_pending/`; lanes never edit `BUG_INVENTORY.md`, `TASKS.md` or `changes/2026/README.md`.
- After an edit to a form that a 2026 operation names, run `python3 tools/year_changes.py --check` and mend the
  operation in `changes/2026/` (ty26-plan D14).
- Follow the interview protocol (11-13) for any question change: personas walked before and after, a coverage row
  per refusal, notes kept as you go.
- No expected value is edited to pass. A value change stops the lane and goes to the coordinator.
- Verify with `tools/check_all.sh --tier fast` in the lane's own worktree.
- **Lows ride along (D4):** each fix lane also fixes the low items on its own forms, since its change is the forms'
  next substantive change and the round's one review covers them.

### Wave 0, coordinator (no agent), immediately

**B0.** Land the landing and batches A and B on main (already planned), then make one bookkeeping commit:
- `new_bug.py --assign`
- statuses: landing-05/08 fixed; BUG-0629 and BUG-0627 fixed in this tree; T-298 done (P1); T-295 items done by R1, R2, R4 and R6; T-310 text; T-256's "adapter_contracts remains"
- a `HANDOFF-NEXT-SESSION.md` entry
- **hold `nx-sampled`** (D3)

One check-all, full tier, since the merge touches `mutate.ts` pins and the evaluators [T release design].

### Wave 1: fix and tool lanes (file-disjoint; run about 8 at a time; `CHECK_ALL_MAX_RUNS=2`)

| Lane | Model / class | Scope (claims) | Bugs | Deliverable and verification | Paid reviews (after B1 merge) |
|---|---|---|---|---|---|
| **F1** HSA | Opus / judgment | `f8889` (+ `s1` line 8 only if 0615 needs it, coordinated with F7a) | 0443, 0453, 0535, 0613, 0614, 0616, 0615, 0618; T-288 residuals; T-291 if D1 says yes | Questions and model; fixtures plus coverage rows; persona walks; `test-fixtures` with no expected value edited, except new cases. | transcription (ls), render (ls), class M (whole) on f8889; screen, false-no and question for new children at the sample |
| **F2** Care | Opus / judgment | `f2441`, `dcprov` | **0447**, 0534, adj5-01 (`shown_when` on f2441.benefits) | the `f2441.care` rewording also reruns the NY gate's screen and false-no (0447 says so) | render f2441, dcprov; transcription and class M f2441 (adj5-01 and the benefits lines) |
| **F3** PTC | Opus / judgment | `f1095a`, `f8962` | adj8-01, land3-fix residual, 0504, T-310 (l8a) | **Lands before** land3-fix's pending $3.56 rerun, so that one round covers both | transcription, render and class M on f1095a and f8962 (the land3-fix dry run plus deltas; about $4-6) |
| **F4** Schedule A and refunds | Opus / judgment | `sa`, `refund` | **0593** (a gate or the per-spouse worksheet; read the i1040gi worksheet first), 0459, 0573, land3-sa residual | Covers land3-sa's pending rerun ($3.53) | transcription, render, class M on sa and refund |
| **F5** Schedule C | Opus / judgment | `sc`, `scveh`, `asset`, `s179` | **ty26-o9-01 (2025)**, 0510, 0529, 0530, 0559, 0489, adj6-01; T-310 (l6b) | mend `changes/2026/sc.yaml` C-BUS-06 so 2025 and 2026 agree; covers the scveh part of land3-screen's rerun | transcription, render, class M on sc and scveh; render only on asset |
| **F6** Investments | Opus / judgment | `sales`, `sd`, `div`, `qbi`, `ftc`, `f4952`, `gift` | 0436, **0488**, 0451, 0517, 0518, 0541, 0505, 0540, 0571, 0506, adj9-03 | | render on all 7; transcription and class M on sales and sd (0488, 0451) |
| **F7a** Schedule 1 and scope | Opus / judgment | `s1`, `scope`, `sli` | 0433, 0438, 0539, 0563, adj9-02 | Covers scope's part of land3-holes' rerun | render on s1, scope, sli; transcription on scope (gates) |
| **F7b** AMT screen | Opus / judgment | `s2` (and a new `f6251` screen form if the design needs one) | **T-307**, T-310 (l7b) | Design note first: which first lines of Form 6251 decide "may owe" without the full form; archive i6251 / f6251 if not in `sources/2025`. Then build, with fixtures and coverage rows. Stop for the coordinator if a value of an existing fixture would change. | transcription, render, class M on s2 (+ f6251); question, screen and false-no at the sample |
| **F8** Person record | Opus / judgment | `person`, `retirement`, `ira`, `f5329`, `dependent` (edu only), `f8863` | 0456/0490, 0547, 0548, 0549, 0520; then edu: 0503, 0546, 0455, 0569, 0572; tech-debt 5.2d if the SEP lines are touched | **The longest lane** (shared `person.yaml`, twins with `dependent`). It must write a handoff at its midpoint (the lesson of HANDOFF 11-12). `check_twins` passes. | transcription and render on person, retirement, ira, f8863, dependent; class M on person and f8863 |
| **F9** Household, EIC, credits | Opus / judgment | `household`, `eic`, `s3`, `s8812`, `f5695` | **T-304 (1)**, 0531, 0519, 0597 (ambiguity entry), 0434, 0620 (3, 6, 11), T-311 (qc_tiebreak is in `dependent`, so hand it to F8) | | transcription and class M on household, eic, s3; render on all 5 |
| **F10** Wage add-ons | Opus / judgment | `otjob`, `tipjob`, `carloan` | **0507**, **0511**, 0537, 0515 | | render and transcription (ls) on otjob and tipjob; render on carloan |
| **F11** Schedule B | Opus / judgment | `sb` | 0576, 0594, T-268 (archive Treas. Reg. 301.7701-7 with `fetch_sources.py`; reword if it differs) | | render on sb; screen and false-no on the `sb` gates at the sample |
| **F12** New York | Opus / judgment; `Jurisdiction: ny` | `ny_it201`, `ny_it2`, `interview/ny/2025/questions.yaml` | 0449, 0491, 0521, 0551, T-244 (BUG-0424 lows), 0439 | `test-fixtures --ny` | render on both forms; New York screen and false-no at the sample |
| **T1** Inventory status | Opus / judgment | `tools/bug_status.py` (new), `bug_pending/close-*.md`, a check-all docs-tier step | D8; verify every NS row above (0129, 0444, 0445, 0167 especially) and write the closure entries | `bug_status.py --self-test`; `check_bug_inventory.py` OK; `reports/bug_status.md` lists every open entry with its TASKS row | none |
| **T5** Review-tool fixes | Opus / judgment | `engine/src/classm.ts`, `tools/transcription/{classm,triage,rule,transcribe}.py`, `tools/siblings.py` | adj11-01, T-316 tool items, the land3-screen screening-operand expansion (only if D: a prospective change; no global re-review), 0129 and 0445 if T1 finds them open | unit tests (`unittest discover -s tools/transcription`); dry-run prompt diffs for 3 forms; applies prospectively (CLAUDE.md) | none |
| **T7** Tech-debt sweep | Sonnet / mechanical | `engine/src/{interview,build,atoms,types,properties}.ts`, `schema/`, `tools/check_all_steps.sh` | C5: 5.3b (retire the legacy profiles; this closes BUG-0432; first check what `interview-check.ts` and `fixtures.ts` read), 1.3, 2.3, 2.5 | check-all **full** (build and schema) | none |

### Wave 1′: tool lanes that need the full tier (start with wave 1; merge as batch B2)

| Lane | Model / class | Scope | Work | Verify |
|---|---|---|---|---|
| **T2** Generator and interview-rules | Opus / judgment | `engine/src/{generate,interview-rules,compare}.ts`, `fixtures/2025/classm*.json` (case restatement) | T-262, T-306, T-270, the BUG-0602 widening (complete returns selected, minimal returns, a derived stream), the T-290 stability check, inventory 2.6 (`compare.ts` uses `sampleReturns`); then rerun the T-276 catalog sweep on the landed tree and report (no family rewrites: they wait for T3) | full tier; Lean compare disagreements triaged; class M reruns of the forms whose cases change, coordinated with round 2 (D6) |
| **T3** Mutation backing | Opus / judgment | `engine/src/mutate.ts`, `fixtures/2025/mutation.json` | T-280 mechanical check of the pinned arguments; T-250's 8 answered-only pins; T-311's `withheld_other_any` gap in the mutation cases | full tier; survivors 0 unexplained; a known-killed control |
| **T6** Year tools and rehearsal | Opus / judgment; `Year: 2026` | `tools/year_changes.py`, `tools/year_diff.py`, new `tools/year_rehearse.sh`, a dated rehearsal doc | C1 (1)-(3): the alias fix with a self-test, the twins rest, then the R5 rehearsal and the re-measurement of charter §7 | self-tests; the rehearsal doc; reruns after B1 because 2025 forms change |

### Wave 2: review round 2 (after B1 lands)

- **RV1.** For each fix lane, after rebasing onto B1: `rerun_all.py` with the lane's forms, line-scoped
  transcription and render, class M only where the arithmetic changed; `--approve-cost` per lane. Then Opus
  adjudication and `carry.py`. Done in the same lane (via SendMessage), so the adjudicator knows the change. Lows
  found here wait (the charter rule); a non-low starts a fix in the same lane, then one more review of that form.
- **RV2.** The sampled release reviews (`screen_review.py`, `false_no_review.py`, the question review,
  `completeness_review.py`; one sample per subject; `release_reviews.sh` as the gate). Two Opus adjudication lanes
  split by form range, plus one New York lane. Then `tools/release.sh`.

### Paid review estimate (dry runs not made here; per-call means from the main ledger [V]: transcription $0.61, render $0.34, class M $0.23, completeness $0.31, screen $0.21, false-no $0.18, question $0.07)

| Kind | Forms (round 2) | Estimate |
|---|---:|---:|
| Transcription, line-scoped | about 18 | about $15 |
| Render, line-scoped | about 34 | about $14 |
| Class M (whole form, arithmetic changed) | about 14 | about $20-30 |
| Sampled screen / false-no / question / completeness (federal and NY; the T-299 counts plus about 10% for new questions) | the release sample | about $155 |
| **Total** | | **about $200-215** |

Every lane's own dry run governs, and each lane over $3.00 needs `--approve-cost`. Part of the land3-* pending
reruns (about $14) is absorbed by F3, F4, F5 and F7a.

### Merge batches (one check-all per batch)

| Batch | Contents | Check |
|---|---|---|
| B0 | the landing, batch A, batch B; bookkeeping | full |
| B1 | F1-F12, T1, T5, T7 on one integration branch; bank and fixtures merged structurally (by entry and case id); generated files regenerated, never merged | one full run (T7 needs it) |
| B1r | RV1 rulings and their non-low fixes | fast |
| B2 | T2, T3, T6 | full |
| R | RV2 rulings, then `release.sh` (its own full run) | release |
| B3 | Docs: T-294 regenerated plus its check, T-246 sweep, README and TRUST figures, the `CLAUDE.md` provisional line (owner), the handoff (a Sonnet lane) | docs |

**Critical path:** B0 → F8 (person, the longest) and F7b (the AMT design) → B1 → RV1 for those forms → RV2 → release.
Everything else is off the path. B2 (T2, T3, T6) runs in parallel. It only has to land before the release if T2's
corpus restatement changes class M subjects (D6). If not, B2 can follow the release.

Not in goal 1, waiting:
- the T-276 remaining families (after T3)
- T-301, T-302, T-303, T-305, T-308, T-309, T-313 (interview quality, rule "at each question's next change")
- T-208, T-181 (coverage expansion)
- the TY2026 waves 3 and 4 (IRS finals)

---

## (d) Decisions the plan makes for the owner (recommendation; to confirm)

| # | Decision | Recommendation |
|---|---|---|
| D1 | T-291 (excess HSA withdrawn): goal 1 or goal 3? | Goal 3 (new arithmetic), **unless the owner intends to file TY2025 with the tool**, in which case F1 does it now. |
| D2 | T-307 AMT computed screen in goal 1 | **Yes.** It is the one question everyone is asked that a typical filer cannot answer correctly. |
| D3 | Hold the sampled release reviews (nx-sampled) until round 2 lands | **Yes.** Otherwise every reworded prompt is sampled twice (about $40-60 wasted) [I]. |
| D4 | Fix the low items on any form a fix lane touches, in the same change | **Yes.** It is the form's next substantive change, so the review is spent anyway. |
| D5 | Fix 2025 first; mend `changes/2026` operations in the same lane | Yes (ty26-plan D12, D14). |
| D6 | The class M corpus (T-262, T-306): restate now or lazily? | Fix the generator now (T2). Restate `classm.json` cases in B2, and **only** rerun class M for forms whose cases change if they are not already in round 2. Ask whether stale class M subjects are acceptable until each form's next change instead. |
| D7 | Incomplete-return semantics (T-249, T-292, BUG-0430) | Keep the provisional label and close T-249 and T-292 as won't-fix for complete returns. T-250 goes to T3. Reopen only if the UI must show exact mid-interview refusals. |
| D8 | Inventory status | Add `tools/bug_status.py` with `Closes:` closure entries and a docs-tier check (charter §5: no prose rules). |
| D9 | Legacy interview profiles | Retire `social-security`, `sales`, `stage4` (this closes BUG-0432 and tech-debt 5.3b). `full` and `ny` remain. |
| D10 | Deferred tech debt | 5.1a: won't fix (the churn reopens reviews). 5.1b: won't fix (`check_twins` suffices). 5.2d: only within F8's lines. 2.6: in T2. 3.4b: won't fix. |
| D11 | T-300 year literals in text | Accept R6's adoption listing (year-moving literals listed at adoption) as charter 7.4's enforcement and close it. Rename the 5 doubtful ids only if the owner wants to. |
| D12 | T-312 redraft choices | Settle each in the lane owning its form, under the 11-14 delegation, recorded in `DECISIONS.md`. |
| D13 | Adopting the redraft | The owner adopts at the release. Remove `CLAUDE.md`'s "provisional" sentence then (an owner edit). |
| D14 | Models | Opus for judgment and Sonnet for mechanical, unless the owner names Fable for the session. |
| D15 | BUG-0597 (the spouse's own carryforward; the instructions are silent) | Add an ambiguity register entry and choose "count both spouses' carryforwards on a joint return" (the general joint-return rule), cited as such. |

---

## (e) Outline of the coverage-expansion protocol (goal 2)

One document, `docs/<date>_coverage_expansion_protocol.md`. Its machinery must be enforced by tools where charter §5
allows. It must specify:

1. **Intake.** A candidate (form, situation, or a refusal to lift) enters from:
   - the coverage estimate, which must be current first (T-294's regenerated `filer_coverage.md` plus a check that its gate list matches the forms; `tools/coverage/estimate.py`, `roadmap.py`)
   - spec 2.4's order (Schedule E, the rest of Schedule 1, married filing separately, Form 1116)
   - over-refusals found in use (T-291, T-208, T-181)

   Each candidate is a TASKS row ranked by coverage gained per estimated cost. The owner approves a decision batch
   before authoring (the stage 16/18 pattern).
2. **Sources.** Archive everything cited before any reading: `tools/sources/<year>.json`, `fetch_sources.py`,
   `check_extraction.py`. The next year's drafts are archived too where they are posted. No claim rests on an
   unarchived page (the T-268 lesson).
3. **Premises.** A premise map plus an independent verification (`research/premises/<topic>.md` and
   `.verification.md`), owner decisions recorded, and ambiguity register entries (`ambiguities/<year>.yaml`).
4. **Encoding.** The DSL in `forms/<year>/`, following the formal gates design (A/B/C gates, `<input>_if_<cond>`,
   `gated_by`):
   - refusals as values
   - year-free ids (`check_year_ids`)
   - parameters with citations, flagged `moves_with_year` / `extends_with_year` where they move
   - tables through `extract_printed_tables.py`; layouts as data
5. **Interview.** The 11-13 protocol: norms N1-N12, §2 judgment, §7 checklist. Personas and walks before and after;
   an off-ramp question; an order range; tick groups; one coverage row per refused situation.
6. **Fixtures and predictions.**
   - Per-form fixtures with `defaults.json` (a new default needs the normal tier).
   - Predictions written before the first run, from the source, in the bug or fixture notes (the "Regression predictions" pattern).
   - Whole returns in `returns.json`.
   - Engine differential, Lean agreement, mutation kills with no new pinned argument without the T3 backing, properties, interview-rules.
7. **Reviews.** The "building" column of charter §4: whole-form transcription, render and class M; completeness,
   screen, false-no and question. All Claude-only, line-scoped after the first pass, one per form per round, the
   $3.00 gate, Opus adjudication, `carry.py`, `bug_pending/` entries.
8. **Rollover hooks** (so that a form added mid-year carries into the next year):
   - if next-year drafts exist, `changes/<next>/<form>.yaml` operations (or an explicit "no change" entry), checked by `year_changes.py --check`
   - its parameters visible to `propose_params.py`
   - catalog rows in `tools/sources/<next>.json`
   - contract banks required from their first year (R2's `required(year)`)
   - twins declared
   - a row in the next change map

   The T6 rehearsal (`year_rehearse.sh`) must include the new form before it counts as done. Across years, generalize
   `docs/ty2026/ADOPTION.md` into a year-generic runbook. The rule for which year an addition targets (D12 of the
   ty26 plan): the newest adopted year; once a new year is adopted, the old tree takes defect fixes only.
9. **Claims and lanes.**
   - `claims.py` per form; one owner per shared form per round (`person`, `dependent`, `f1040`, `scope`, `s1`, `questions.yaml` entries)
   - the brief template (protocol §5 plus model, class, year and jurisdiction lines)
   - the bank and fixtures merged structurally
   - generated files regenerated
   - mid-lane handoffs for long lanes
10. **The bar.** Protocol §6's deterministic bar, plus check-all at the full tier, plus a release. An addition is
    done when:
    - the estimate is regenerated and the README table is current
    - `COVERAGE.md` is regenerated
    - its reviews are ruled
    - the release is tagged

    Also state what the bar does not show (protocol §6).
11. **Measurement.** Each addition's cost from `research/costs/agent_runs.jsonl` and `.transcription/costs.jsonl` (both
    carry year and jurisdiction), reported per addition, with a small report tool, so the cost per point of coverage
    is known.

**Existing docs it builds on:**
- spec 2.4 and 11, and `spec/design.md` §5 (stage discipline)
- `docs/consolidation_charter.md` §§2-7
- `docs/2026-11-13_interview_construction_protocol.md`
- `docs/2026-11-06_formal_gates_design.md`
- `docs/2026-10-24_validation_policy.md`
- `docs/2026-11-05_release_gating_design.md`
- `docs/2026-11-09_review_store_design.md` (the carry across years)
- `docs/2026-11-14_year_change_operations.md` and `docs/ty2026/ADOPTION.md`
- `docs/COVERAGE.md` and `tools/coverage/*`
- `research/premises/*` (the premise and verification pattern)
- `docs/provisional/lanes/ty26-plan.md` (the lane machinery, D3 split files, D14 claims)
- `tools/README.md`

**Gaps to close first (prerequisites):**
- T-294 regenerate plus its check
- the T6 rehearsal tool
- the year-generic adoption runbook
- `bug_status.py` (D8)

These are in goal 1's lanes (T6, B3, T1), so goal 2 can start on the release.
