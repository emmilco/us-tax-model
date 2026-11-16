# Lane mfs-l2: married filing separately, deductions and adjustments (2025, us)

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree: `.claude/worktrees/mfs-l2`, detached at `refs/scratch/x1-base` = `825024d8`. Brief `mfs-brief.md`; design
`scout-mfs.md` §3.3 and row L2 of §7. No paid reviews, no model calls; nothing committed; `check_all.sh` and `mutate`
not run (brief).

Forms: `sa.yaml`, `s1.yaml`, `sli.yaml`, `ira.yaml`, `person.yaml`.

## 1. What the merge must know

- **Reads L1's ids.** `household.mfs`, `household.mfs_apart_all_year` (lines) and `ira.line2_apart` (param), as declared
  in `/tmp/mfs-declared-ids.md`. My tree carried build stubs of them in `forms/2025/household.yaml` and
  `params/2025.yaml`; **these were reverted before hand-over**, so this lane's diff does not build alone: merge L1
  first. The default `household.mfs_living: together_late` is L1's; the stub default was removed too.
- **`fixtures/2025/defaults.json`**: the snapshot was replaced by `nx-b1`'s copy to build (brief, base caution). My own
  additions are the script `/tmp/mfs-l2/defaults_patch.py <tree>` (two defaults: `sa.mortgage_over_limit_mfs` false,
  `ira.mfs_spouse_covered` false), inserted by id order. Re-run it on the integration tree; do not take my file.
- **Tool-managed cases (inputs only, no expected value touched)**: `sa.mortgage_over_limit_mfs: false` stated in the 33
  married-filing-separately cases that pay mortgage interest (they take no defaults and would otherwise be unknown):
  `classm.json` 8, `classm.deepseek.json` 4, `classm.gpt.json` 1, `mutation.json` 20. Script:
  `/tmp/mfs-l2/ripple_mortgage.py <tree>` (idempotent); list in `/tmp/mfs-l2/l5_list.txt`. Those cases still state
  `sa.mortgage_over_limit: false`, which a separate return no longer reaches (harmless to the evaluator; L5 may drop it).
- **`reviews/2025/consumers.json`**: two stale rulings removed (`consumer:sli.any@p4681:p5`,
  `consumer:sli.any@i1040gi:p99`): `sli.any` is now read only by its gate.
- **Bank** (`interview/2025/questions.yaml`): new `sa.mortgage_over_limit_mfs` (200/33) and `ira.mfs_spouse_covered`
  (180/21); reworded `sa.spouse_itemizes` (help), `sa.spouse_extra` (prompt, help). Slot collisions with the scout's
  proposal: 200/22 is `sa.mortgage_over_limit`, 200/29 is the 2026 `sa.mortgage_insurance` (year_changes check), 180/14
  is `person.ira_work_plan`.
- **s1.yaml**: one new line, `s1.line20_box`, inserted before `s1.line21`; no edit to lines 5, 8v or 9 (X1 lanes).
- New coverage file `interview/2025/coverage/mfs_deductions.yaml` (7 rows; uses `household.community_property` and
  `household.mfs_living`, so it passes only on a tree with L1's opening).
- `docs/provisional/DECISIONS.md`: section "MFS lane L2" appended.
- Ambiguities (own prefixes): `amb.2025.sa_mfs_spouse_itemizes`, `amb.2025.sa_mfs_mortgage_limit`,
  `amb.2025.ira_mfs_spouse_covered`, `amb.2025.s1_line20_box` (L1's `amb.2025.mfs_lived_apart_boxes` gives the same
  reading for line 6d; the integrator may fold them).

## 2. What changed

Computed now on a separate return (once L1 removes the return-wide `s3.mfs` refusal):

| Rule | Lines | Source |
|---|---|---|
| Spouse itemizes: line 12b, standard deduction zero, Schedule A used | `sa.spouse_itemizes` (reworded to the fact), `sa.mfs_spouse_itemizes`, `sa.standard`, `sa.itemizes` (unchanged arithmetic) | i1040gi p. 33 Line 12b, p. 34 Exception 2; p504 p. 4 |
| Spouse boxes question asked only when the spouse is not itemizing (refusal kept, D4) | `sa.mfs_spouse_not_itemizing` (new), `sa.mfs_spouse_extra` (guard changed) | i1040gi pp. 33–34 |
| Mortgage limits $375,000 / $500,000 on a separate return (over: refused, as before for $750,000) | `sa.mortgage_over_limit_mfs` (new input), `sa.mortgage_over_limit_mfs_if_mfs` (gate), `sa.mortgage_interest_mfs`, `sa.mortgage_interest_not_mfs` (helpers), `sa.mortgage_over_limit_if_joint_limits` (new gate of the existing input), `sa.mortgage_over_limit_if_interest` (kept id, now the derived "either" line read by `sa.unsupported`) | i1040sca p. 8 |
| Student loan interest not asked on a separate return (deduction stays 0) | `sli.any_if_not_mfs` (a plain `choose` helper, not a `gated_by` gate: see section 3); `sli.interest_if_any`, `sli.unqualified_any_if_any`, `sli.assisted_any_if_any` read it, so `sli.any` is unreachable on a separate return | i1040gi p. 98 |
| IRA: considered covered through the spouse unless lived apart all year | `ira.mfs_spouse_covered` (new input), `ira.mfs_spouse_covered_if_asked` (gate), `ira.mfs_cov_matters`, `ira.mfs_cov_matters_trad` (helpers); `ira.anyone_covered` and `ira.line1a` read the gate | i1040gi p. 96; p590a p. 13 |
| IRA line 2: $89,000 when lived apart all year, $10,000 otherwise | `person.ira_line2_status` (now a choose), `person.ira_line2_table` (the old param line, renamed), `person.ira_line2_apart` (new param line) | i1040gi p. 97 |
| Schedule 1 line 20 box | `s1.line20_box` (new, display) | f1040s1 line 20; i1040gi p. 96 |

Questions (bank):
- `sa.spouse_itemizes` (form text): "Is your husband or wife itemizing deductions on their own 2025 return, instead of taking
  the standard deduction?" Help: "If they itemize, your standard deduction is zero and your own deductions are listed
  instead. Ask them if you do not know."
- `sa.spouse_extra` (prompt): "Did your husband or wife have no income in 2025, and are they filing no 2025 return, and were
  they born before January 2, 1961, or blind at the end of 2025?" Help: "Only then can your husband or wife's age or
  blindness raise your standard deduction. A Yes ends the interview here."
- `sa.mortgage_over_limit_mfs` (new, 200/33): "Did the loans on your home add up to more than $375,000 at any time in 2025,
  or to more than the home is worth?" Help: "Count the loans on a second home too, and the whole of a loan you owe with your
  husband or wife. If all of it was borrowed on or before December 15, 2017, the limit is $500,000. A Yes ends the
  interview here."
- `ira.mfs_spouse_covered` (new, 180/21): "Was your husband or wife covered by a retirement plan at work in 2025?" Help: "A
  pension, a 401(k) or 403(b), or a SEP or SIMPLE IRA counts, even if they put nothing in. If they were, the "Retirement
  plan" box in box 13 of their Form W-2 should be ticked."

Who could answer No wrongly: `ira.mfs_spouse_covered`, a filer who does not know the spouse's plan (help names W-2 box
13; asked only of the few it can affect). `sa.mortgage_over_limit_mfs`, a filer who counts only a half share (help says
count the whole loan). `sa.spouse_itemizes`, a filer who has not asked the spouse (help says ask). Cost: every new
question is asked only on a separate return and beneath an existing fact (a mortgage, a traditional contribution while
not covered and living together); a separate filer with nothing in these topics meets only `sa.spouse_itemizes` and,
when that is No, `sa.spouse_extra` — the same two questions as before.

## 3. Decisions (each with the alternative rejected)

Recorded in `docs/provisional/DECISIONS.md` (section "MFS lane L2"). Beyond the scout:
- The old gate id `sa.mortgage_over_limit_if_interest` is kept as a derived "either" line (protocol technique 3.1), so
  `sa.unsupported` and the 2026 operation that quotes its `expr.any` stay untouched. Rejected: add a second gate to
  `sa.unsupported` and mend `changes/2026/sa.yaml`.
- `ira.anyone_covered` takes the spouse's coverage directly; rejected the scout's per-person `person.ira_cov_effective`
  (more lines, same values on a one-person return).
- The guard of `sli.any_if_not_mfs` reads `household.mfs` (L1); the build accepts only Bool-pair guards. `sli.any` does
  **not** carry `gated_by`: the minimal (background) return of `interview-rules` / `interview-coverage` treats every
  `gated_by` input as behind a closed gate and refuses to answer it, but this gate is open on every non-separate return,
  so the background walk failed ("Unanswered: sli.any", seen in the simulated merge). Unreachability on a separate return
  comes from every reader sitting under the `choose`, as the gates design allows for unmarked inputs. Rejected: keeping
  the marker and changing the tools.
- `sa.spouse_itemizes` keeps its bank place (200/86) rather than moving first in the topic: it changes no question asked.
- `s1.line20_box` is printed only with a traditional contribution (`amb.2025.s1_line20_box`), so no separate filer is
  asked about living arrangements for a box alone.

## 4. Gates replaced and residual refusals

None of L2's forms held the `s3.mfs` refusal. Residual refusals kept on separate returns: `sa.mfs_spouse_extra` (now
narrower: not asked when the spouse itemizes), `sa.unsupported` (mortgage over the separate-return limit, as for every
status), `ira.cov_gate` (social security benefits + traditional contribution + covered, now also when considered covered
through the spouse; i1040gi p. 31 "you or your spouse were covered"). Note for L1: the screen `ssb.ira_covered` asks
about the filer's own coverage; a separate filer covered only through the spouse answers No and is refused later, at
`ira.cov_gate` (person.yaml, `person.ira_line12`), not at the screen.

## 5. Next year (protocol 7.1)

No operation file written. The lane's lines carry to 2026 as written; `year_changes.py --check`: all 1254 operations
apply. Documents: i1040gi 2026 and i1040sca 2026 are not posted (awaited); p590a and i8606 2026 editions are present in `sources/2026/` (listing seen; pages not read).
Parameter for the next `propose_params.py --from 2025 --to 2026` run: `ira.line2_apart` 8,900,000 → 9,100,000 (i8606 2026
draft p. 2, "$91,000 if single, head of household, or married filing separately and you didn’t live with your spouse at
any time in 2026", change map C-PEOP-08 note; quote read from the change map, not re-read in the 2026 archive). The
separate-return mortgage limits for 2026 were not checked (no 2026 i1040sca archived; the change map has no entry for
them): awaited. The lane's 2025 cites have no 2026 equivalent yet (awaited i1040gi).

## 6. Defects

None recorded.

## 7. For other lanes and requests

- L1: params used `ira.line2_apart` (declared); lines `household.mfs`, `household.mfs_apart_all_year`. The note on
  `ssb.ira_covered` above.
- L5: none of the line-level restatements; the 33 input-only ripples are done here (section 1).
- Integrator: a profile target for `s1.line20_box` was not added (`full.yaml` is not mine); the box is always settled on a
  return that reaches the IRA worksheet, because `household.mfs_living` is asked there anyway.

## 8. Verification (run and seen; base `825024d8` is broken, brief "Base caution")

| Command | Tree | Result |
|---|---|---|
| `node engine/dist/main.js build` | lane tree with L1-id stubs | OK (after two fixes: Bool-pair guards only; seq collisions) |
| `test-fixtures` (whole run, before the coordinator's narrowing) | lane tree | my 10 new cases: 9 ok; `mfs.sa.spouse_itemizes_return` fails only on `f1040.line37`, which is the return-wide `s3.mfs` refusal L1 removes (lines 12e, 16 = 7,460 and 24 = 7,460 match; line 33 refused for the same reason). 619 base failures (`eval exited 1`: stale `s2.amt_owed`, missing `sd.qof`); none names a line or input of this lane |
| eval of `classm.tcw.9` without the stale input | lane tree | showed `sa.mortgage_over_limit_mfs` unknown, hence the 33-case input ripple |
| `citations.py --strict` | lane tree (final) | 0 findings |
| `year_changes.py --check` | lane tree (final) | all 1254 operations apply |
| `check_consumers.py` | lane tree | my lines: two findings fixed (cites of `sa.spouse_extra`, `sa.spouse_itemizes` now include p. 34), two stale `sli.any` rulings removed; the rest are base findings on other forms |
| `transcription/check_questions.py`, `check_screens.py`, `check_false_no.py` | lane tree, after render | exit 0; sampled reviews now due (section 9) |
| `siblings.py --check`, `check_bug_inventory.py` | lane tree | fail on base entries only (BUG-0752, g1-t3-01; ty26 citations) |
| **Simulated merge**: L1's working diff (snapshot ~15:10, forms, params, interview, ambiguities, changes, fixtures incl. NY) applied over this lane, built | scratch state, reverted afterwards | build OK |
| `interview-coverage --rows coverage/mfs_deductions.yaml` | simulated merge | **7/7 rows pass** |
| `interview-coverage` home, saving, education_energy, credits, opening | simulated merge | all pass but two L1 rows in `opening.yaml` (`opening.separate` must now answer `sa.spouse_itemizes`; `opening.widowed_this_year_alone` refuses on a background answer). L1's `mfs.yaml` rows need `sa.spouse_itemizes` answered too (and one names the removed question `ssb.lived_apart`) |
| `tick-groups` | simulated merge | passed |

Not run: `interview-rules`, `test-fixtures --ny`, `mutate`, `check_all.sh` (coordinator: no full runs on the broken base);
`test-fixtures` after the `sli` change and on the simulated merge.

## 9. Review debt (round 2; no dry-run estimate made)

- Transcription (line-scoped) and class M: `sa`, `sli`, `ira`, `person` (IRA lines), `s1` (`s1.line20_box`).
- Render: `sa`, `ira`, `s1`, `sli` (new and reworded labels).
- Question review: `sa.spouse_itemizes`, `sa.spouse_extra`, `sa.mortgage_over_limit_mfs`, `ira.mfs_spouse_covered`.
- Screen and false-no samples (listed as due by the checks): `sa.spouse_extra`, `gate:ira.mfs_cov_matters`,
  `gate:sa.mfs`, `gate:household.mfs`, and the mortgage gates (`sa.mortgage_interest_mfs` / `_not_mfs`).

## 10. Walks

Not recorded (no persona of this lane; L1 owns `14_mfs_separate_finances`). The coverage rows above stand in for the
three filers: the filer with nothing in these topics meets `sa.spouse_itemizes` and `sa.spouse_extra` only.

## 11. Left open, in rank order

1. `mfs.sa.spouse_itemizes_return` line 37 (1,460 owed) to be confirmed on the merged tree (inferred from lines 24 and
   withholding).
2. The separate-return mortgage question is asked at 200/33, after `s3.mcc`, `s2.mortgage_subsidy` and the property
   tax questions (its scout slot 200/22 is taken): the refusal arrives later in the topic than the joint one (N11). A
   renumbering of order 200 would fix it; not mine to do.
3. Screen `ssb.ira_covered` (L1) does not mention coverage through the spouse; the refusal arrives later at `ira.cov_gate`.
4. 2026: `ira.line2_apart` 9,100,000 for propose_params; separate-return mortgage limits to confirm on the 2026 i1040sca.
5. Estimated coverage gain: none of its own; this lane removes no refusal gate, it makes the separate returns L1 opens
   correct on lines 12b/12e, Schedule A mortgage limits, line 21 and line 20.
