# Interview questions asked and never read, or reachable out of turn: catalog of every affected template

Tax year 2025, federal (the New York profile's generated returns all end refused and showed nothing). Scratch work on main at `2e13fd84`; written 2026-11-11. Nothing in the repository was changed. Files named here are under `/tmp/f1095a/`.

## 1. Summary

**What is wrong.** A line written as `all(A, B)` or `any(A, B)` reads B while A is still unknown (spec 4.7.2: an unknown conjunct is passed over and a later one may decide the test). So B's question is reachable before the answer that could make it moot. This is the pattern BUG-0466 named and BUG-0471 and BUG-0492 rewrote for 69 lines; the baseline has read as empty since. It is not empty: `interview-rules` classes only 3 generated returns, and over 5,000 generated returns (1,147 complete) the tool's own rules flag **70 input templates on 811 of the complete returns**, plus one more found by other means. They trace to **46 lines in 21 families** of that same pattern (45 of them in the combined patch), and to one other cause (a count's lower bound, class L1).

**Three kinds of finding, by what a filer meets.**

| Class | Templates | What it costs |
|---|---|---|
| Left reachable at completion (the serious class) | 15 (on 134 returns) | For the same answers, no status or value ever differed by order (no order error in five random orders of each of the 1,147 complete returns, nor in an earlier 1,000-return sweep that also ran its 799 refused returns). But in some orders the interview says "complete" with a question still open, and for **6 of the 15** an answer to that open question **refuses the return** (`dependent.multiple_support` and `dependent.kidnapped` at every such state; `dependent.citizen`, `dependent.canada_mexico`, `dependent.disabled`, `dependent.gross_income` at some). All 6 are refusal gates of the dependent test, left unanswered when `dependent.odc_person` (D1) is decided by a later operand. No answer changes a value while the return stays complete. The other 9 only inflate the pending list; 3 of those are the lower-bound class, which is by design. |
| Asked in bank order and unread | 42 (24 of them the monthly Form 1095-A columns) | Questions the filer answers for nothing: 921 over the 1,147 complete returns, on 354 of them. `dependent.citizen` alone is 226. |
| Reached only out of bank order | 36 (24 of them seen in the bank-order walk itself, the rest only in a random order) | The interface asks the first open question in bank order, so a filer does not see these as questions; they enlarge the pending count and make the check fail. |

**The rewrites.** Each line becomes a nested `choose` on its operands in their original order (the BUG-0471 convention). Each family was applied alone to main's tip, built and tested; then all together (`patches/ALL_combined.patch`: 45 lines rewritten, 78 helper lines added, 15 form files).

- **Safety, all rewrites together:** federal fixtures 1,767 of 1,768 and New York 338 of 338 pass. The one that changes is `stage8.mut.hoh_child_months_unanswered_absence`, where `dependent[child].hoh_test2` goes from false to unknown with `dependent[child].months` unanswered: the trade-off the owner accepted in BUG-0471, and it comes from one line (D5). Status and every target value are identical to main on 3,000 generated returns (712 complete) and on every fixture's inputs. Over 2,000 swept returns the status never differs and no order error appears.
- **Effect:** on the 449 complete returns of that sweep, 373 fewer questions (141 returns shorter, none longer); asked-and-unread questions 373 to 0; returns with any finding 315 to 12; templates 69 to 4, all four the lower-bound class. At the 243 states where main reports complete with a question open, 71 of the 321 open questions have an answer that refuses the return; with every rewrite 46 such states remain and none of their open questions does; with D1 alone 72 remain, and none does. `interview-rules` at its defaults then reports only that the three BUG-0487 holds can be removed. On the `interview-length` set (162 complete returns) the complete returns go from 10,738 to 10,725 questions: 11 of them were asked more than the inputs their return reads, and none is afterwards (143 of that set's 162 complete returns are slice-profile fixtures, so it understates the effect).
- **Costs:** 18 of the 52 pinned mutation arguments are un-pinned (many only because a premise line gained a reader); 15 rendered form pages and the index change; the transcription, render and class M subjects of 15 forms change. No review, `mutate`, `compare` or `check-all` was run.

**Ranking (section 5).** D1 first: it removes the refusal-capable open questions and the most unread questions (253), with one line and three helpers. Then P2 (269 unread; closes BUG-0487), D2 (138), P1 (183; up to 24 amounts per Form 1095-A), D4 (40), D3, A1 (21). The remaining fourteen families save few or no questions and clean the check; D5 is the only one that changes a fixture.

**The check (section 6).** Selecting 60 complete generated returns instead of 12 unselected ones costs about 20 s on a 106 s run and finds 24 problems on main's forms; nine minimal returns with one entry per collection add 19 s of one thread and are independent of the generator. With no rewrite made, the baseline would have to hold 7 early-completion, 24 out-of-order and 21 asked-unread templates on day one. Sampling does not exhaust the defect: the 70th template appeared at return 4,762, and a static count finds 231 lines of the shape.

**Three cautions for whoever lands these.** (1) Fixing one conjunction can expose the next one upstream: three more lines turned up only after their neighbours were rewritten (`person.edu_llc_tin_refused`, `f8889.split`, and the lower-bound counts). (2) D5's three lines must land together: `dependent.hoh_test2_lived` alone makes the interview ask `dependent.absence_no_return` on 3 of 15 returns where main does not. (3) Main has moved to `2be2a2cf` since (`dependent.yaml` and `person.yaml` changed for Form 8863 Part III); every patch still applies there (`git apply --check`), but the tests were run on `2e13fd84`.

## 2. What was run, and on what

Everything here was run in scratch copies under `/tmp/f1095a/`; nothing in the repository was edited, no paid review was run, no sub-agent was launched.

- **Base:** `/tmp/f1095a/base`, a `git archive` of main at `2e13fd84` (the tip when this work began), built there. Each rewrite was applied to a fresh copy of it, built, and tested alone; then all of them together (`/tmp/f1095a/all2`).
- **The check's own machinery, called from scratch scripts.** The tool has a count option (`INTERVIEW_RULES_RUNS`) and a fixed seed (`SEED = 11`), so other seeds were reached by calling its exported pieces (`sampleReturns`, `runTask`, `walk`, `bankOrder`, `minimalAnswers`, `readInputs`) from `/tmp/f1095a/scripts/seeds.mjs`. For seed 11 and 12 returns the script reproduces the tool's own count (1,645 states, 0 problems).
- **Sweep:** 100 seeds of 50 generated federal returns (5,000 returns, 1,147 of them complete). Every return was walked in bank order; each complete return was also answered in 5 random orders and tested on random subsets of its answers, as the tool does. The 3,853 returns that end refused were walked in bank order only: the tool classes reach and early completion on complete returns only, and an earlier sweep of 1,000 returns that ran the random orders on its 799 refused returns found nothing on them.
- **Where new templates stopped: they did not.** 35 of the 70 templates had appeared by return 1,000 and 45 by return 1,620; the 24 monthly Form 1095-A templates first appeared at return 1,727, and the 70th template (`f5695.qmid_ac`) at return 4,762 of 5,000, after 3,000 returns with none. Two further templates (`person.sav_student`, and `person.tin` through `person.edu_llc_tin_refused`) were found by other means (section 7). Sampling does not exhaust this defect: a static count of the lines that have the shape is in section 7.
- **Cause of each finding:** `/tmp/f1095a/scripts/trace.mjs` replays the return to a state at which the template's input is reachable and unanswered and prints the lines one of whose operands waits on that input while the line itself is decided or waits on another input. The expression of each such line was then read. One witness return per template and class.
- **For each input left reachable at completion,** every answer to it was tried at every such state the sweep reached (243 states on 134 returns; `/tmp/f1095a/scripts/probe_all.mjs`), recording whether the status or any target value changes.
- **Each rewrite** was made by `/tmp/f1095a/scripts/nest.py` (two by hand), which turns `all(t1, ..., tn)` into nested `choose` lines on the operands in their original order, as BUG-0471 and BUG-0492 did: the first operand's own Bool line as the guard where the operand is `<line> = true` or `= false`, a helper test line otherwise; the false alternative is the document's `<doc>.no` line (the parameter `household.no`), added where the document had none; `any` takes the guard line itself when true and the rest when false; helper lines go at the end of the document with the rewritten line's citation. Helper ids (`<line>_from2`, `<line>_test1`) and labels are mechanical and would be renamed by the lane that lands them.
- **Tests per family** (`/tmp/f1095a/scripts/fam.sh`): the build; `test-fixtures` and `test-fixtures --ny`; the sweep returns that showed the family, walked again in bank order and 5 random orders; status and target values of 1,500 generated returns (3,000 for the combined run) and of every fixture's inputs compared with main; the pinned mutation arguments of `engine/src/mutate.ts` whose premise digest moves (`premiseDigest` evaluated on main's and the patched data for each of the 52 pinned premise lists); `render` and the rendered files it changes. The `interview-length` tool takes about 10 minutes, so it was run once on main and once with every rewrite; per family the static count it reports was recomputed for the full profile's part of its set (11 whole-return fixtures, the 12 generated returns, 5 minimal returns: 28 walks, complete and refused).
- **Not run:** `mutate`, `compare` (Lean), the engine differential, `check-all`, any review. Review state (`.transcription/`) is not in a `git archive`, so which review logs go stale was read from `tools/transcription/subjects.py` (a form's transcription, render and class M subjects are its definition, its rendered text and its lines' expressions), not measured.
- **Load:** the machine was busy with other work throughout (load average 40 to 100), so wall times are inflated and are given with a same-conditions comparison where it matters.

## 3. Table of all templates

One row per template and class. "Returns" counts complete generated returns of the 5,000-return sweep on main. The cause line is the line whose expression reads the template's input while another operand is unknown (found by replaying one witness return per row, then read; a template with several rows has a cause per class). Families are described in section 4. The last two columns are test results: the witness returns re-walked with one family's rewrite applied alone, and the 2,000-return sweep (seeds 1 to 40) with every rewrite applied. For a finding seen only in random orders, "gone" under a family that does not own its cause line can be a different random order in that build rather than a fix; the last column is the firmer evidence.

Sweep: 5000 generated federal returns (100 seeds of 50), 1147 complete; 70 templates; 811 complete returns show at least one.

| Template | Class | Returns (of 1147 complete) | Cause line: the operand read past | Family | Gone on the witness returns with one family's rewrite alone | With every rewrite (2,000 returns) |
|---|---|---|---|---|---|---|
| `asset.not179` | asked and unread | 20 (21 questions) | `asset.s179_bad` := `all(asset.s179 > asset.zero, any(asset.s179 > asset.basis, asset.over_half = false, asset.not179 = true))` | A1 | asset | gone |
| `carloan.vehicle` | reached only out of bank order | 1 (1 seen in the bank-order walk itself, the rest only in a random order) | `carloan.eligible` := `all(carloan.requirements = true, carloan.vehicle = true)` | C1 | carloan | gone |
| `dependent.absence_no_return` | reached only out of bank order | 22 (0 seen in the bank-order walk itself, the rest only in a random order) | `dependent.hoh_test2` := `all(dependent.hoh_test2_lived = true, dependent.absence_no_return = false)` | D5 | dep_hoh, dep_hoh2 | gone |
| `dependent.absence_no_return` | asked and unread | 6 (6 questions) | `dependent.hoh_test2` := `all(dependent.hoh_test2_lived = true, dependent.absence_no_return = false)` | D5 | dep_hoh, dep_hoh2 | gone |
| `dependent.age` | left reachable at completion. At 6 such states no answer changes the status or a value | 5 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | - | gone |
| `dependent.canada_mexico` | left reachable at completion. **At 2 of 23 such states an answer refuses the return** (gate `dependent.claimed_no_tin`) | 22 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `dependent.citizen` | left reachable at completion. **At 1 of 1 such states an answer refuses the return** (gate `dependent.claimed_no_tin`) | 1 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | - | not in these 2,000 on main either |
| `dependent.citizen` | asked and unread | 208 (226 questions) | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `dependent.disabled` | left reachable at completion. **At 1 of 40 such states an answer refuses the return** (gate `dependent.income_exception`) | 32 | `dependent.income_exception` := `all(dependent.disabled = true, dependent.qr_income = false)` | D3 | dep_hoh, dep_hoh1, dep_hoh2, dep_hoh2lived, dep_odc | gone |
| `dependent.edu_tin_issued` | reached only out of bank order | 96 (79 seen in the bank-order walk itself, the rest only in a random order) | `dependent.edu_llc_tin_refused` := `all(dependent.edu_llc = true, dependent.edu_tin_issued = false)` | D6 | dep_edutin | gone |
| `dependent.gross_income` | left reachable at completion. **At 2 of 45 such states an answer refuses the return** (gate `dependent.income_exception`) | 39 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | - | gone |
| `dependent.gross_income` | reached only out of bank order | 31 (31 seen in the bank-order walk itself, the rest only in a random order) | `dependent.income_exception` := `all(dependent.disabled = true, dependent.qr_income = false)` | D3 | dep_incx | gone |
| `dependent.gross_income` | asked and unread | 64 (70 questions) | `dependent.income_exception` := `all(dependent.disabled = true, dependent.qr_income = false)` | D3 | dep_qr | gone |
| `dependent.kidnapped` | left reachable at completion. **At 21 of 21 such states an answer refuses the return** (gate `dependent.qr_kidnapped`) | 17 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `dependent.lawful` | left reachable at completion. At 9 such states no answer changes the status or a value | 8 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_qrrel | gone |
| `dependent.lawful` | asked and unread | 37 (40 questions) | `dependent.qr_other_relation` := `any(all(f1040.status = "mfj", dependent.spouse_relative = true), all(dependent.qr_all_year = true, dependent.lawful = true))` | D4 | dep_qrrel | gone |
| `dependent.months` | reached only out of bank order | 22 (0 seen in the bank-order walk itself, the rest only in a random order) | `dependent.hoh_test2_lived` := `any(all(dependent.claimed = true, dependent.relationship != "household_member", dependent.relationship != "sibling_descendant", dependent.relationship != "other", dependent.hoh_lived_half = true), all(dependent.qualifying_child = …` | D5 | dep_hoh, dep_hoh2lived | gone |
| `dependent.multiple_support` | left reachable at completion. **At 44 of 44 such states an answer refuses the return** (gate `dependent.multiple_support`) | 30 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `dependent.parent_home_paid` | reached only out of bank order | 73 (0 seen in the bank-order walk itself, the rest only in a random order) | `dependent.hoh_test1` := `all(dependent.relationship = "parent", dependent.claimed = true, dependent.parent_home_paid = true)` | D5 | dep_hoh, dep_hoh1 | gone |
| `dependent.qr_all_year` | left reachable at completion. At 25 such states no answer changes the status or a value | 18 | `dependent.qualifying_relative` := `all(dependent.qr_relationship = true, dependent.qualifying_child = false, dependent.qr_income = true, dependent.supported = true)` | D2 | dep_incx, dep_odc | gone |
| `dependent.spouse_relative` | left reachable at completion. At 7 such states no answer changes the status or a value | 7 | `dependent.qr_other_relation` := `any(all(f1040.status = "mfj", dependent.spouse_relative = true), all(dependent.qr_all_year = true, dependent.lawful = true))` | D4 | dep_incx, dep_odc, dep_qr, dep_qrrel | gone |
| `dependent.spouse_relative` | reached only out of bank order | 7 (0 seen in the bank-order walk itself, the rest only in a random order) | `dependent.qr_other_relation` := `any(all(f1040.status = "mfj", dependent.spouse_relative = true), all(dependent.qr_all_year = true, dependent.lawful = true))` | D4 | dep_incx, dep_qr, dep_qrrel | gone |
| `dependent.supported` | left reachable at completion. At 13 such states no answer changes the status or a value | 8 | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `dependent.supported` | reached only out of bank order | 85 (85 seen in the bank-order walk itself, the rest only in a random order) | `dependent.qualifying_relative` := `all(dependent.qr_relationship = true, dependent.qualifying_child = false, dependent.qr_income = true, dependent.supported = true)` | D2 | dep_qr | gone |
| `dependent.supported` | asked and unread | 63 (68 questions) | `dependent.qualifying_relative` := `all(dependent.qr_relationship = true, dependent.qualifying_child = false, dependent.qr_income = true, dependent.supported = true)` | D2 | dep_qr | gone |
| `eic.legally_separated` | reached only out of bank order | 1 (0 seen in the bank-order walk itself, the rest only in a random order) | `eic.step3_married` := `any(eic.married_rules = false, eic.same_home = false, eic.legally_separated = true)` | X2 | eic_step3 | gone |
| `eic.legally_separated` | asked and unread | 1 (1 questions) | `eic.step3_married` := `any(eic.married_rules = false, eic.same_home = false, eic.legally_separated = true)` | X2 | - | not in these 2,000 on main either |
| `eic.same_home` | reached only out of bank order | 1 (0 seen in the bank-order walk itself, the rest only in a random order) | `eic.step3_married` := `any(eic.married_rules = false, eic.same_home = false, eic.legally_separated = true)` | X2 | eic_step3 | gone |
| `f1095a.b_counted` | asked and unread | 6 (12 questions) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |
| `f1095a.c_total` | asked and unread | 5 (5 questions) | `f8962.applicable` := `any(f8962.line5 >= 100, all(f8962.aptc = true, f8962.estimate_100 = true))` | P2 | f8962_applicable | gone |
| `f1095a.mo_a` | asked and unread | 11 (13 questions) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |
| `f1095a.mo_b` | asked and unread | 11 (11 questions) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |
| `f2441.nondependent` | reached only out of bank order | 2 (2 seen in the bank-order walk itself, the rest only in a random order) | `f2441.nondependent_gate` := `all(f2441.care = true, f2441.nondependent = true)` | X3 | f2441 | gone |
| `f5695.b_new_home` | asked and unread | 1 (1 questions) | `f5695.sec_b_new_home` := `all(f5695.sec_b_claimed = true, f5695.b_new_home = true)` | E1 | f5695 | gone |
| `f5695.line17b` | reached only out of bank order | 2 (2 seen in the bank-order walk itself, the rest only in a random order) | `f5695.sec_a_claimed` := `all(f5695.line17a = true, f5695.line17b = true, f5695.line17c = true)` | E1 | f5695 | gone |
| `f5695.line17c` | reached only out of bank order | 2 (2 seen in the bank-order walk itself, the rest only in a random order) | `f5695.sec_a_claimed` := `all(f5695.line17a = true, f5695.line17b = true, f5695.line17c = true)` | E1 | f5695 | gone |
| `f5695.line17e` | reached only out of bank order | 2 (2 seen in the bank-order walk itself, the rest only in a random order) | `f5695.sec_a_new_home` := `all(f5695.sec_a_claimed = true, f5695.line17e = true)` | E1 | f5695 | gone |
| `f5695.line25a` | reached only out of bank order | 1 (1 seen in the bank-order walk itself, the rest only in a random order) | `f5695.enabling_claimed` := `all(f5695.sec_b_claimed = true, f5695.line25a = true)` | E1 | f5695 | gone |
| `f5695.qmid_ac` | reached only out of bank order | 1 (1 seen in the bank-order walk itself, the rest only in a random order) | `f5695.ac_no_qmid` := `all(f5695.line22c > param sales.zero, f5695.qmid_ac = false)` | E1 | f5695 | not in these 2,000 on main either |
| `f5695.separate_homes` | reached only out of bank order | 2 (0 seen in the bank-order walk itself, the rest only in a random order) | `f5695.separate_homes_joint` := `all(f1040.status = "mfj", f5695.separate_homes = true)` | E1 | f5695 | gone |
| `f8889.employer_in_box1` | reached only out of bank order | 163 (163 seen in the bank-order walk itself, the rest only in a random order) | `f8889.excess` := `all(f8889.line11 > f8889.line8, f8889.employer_in_box1 = false)` | H1 | f8889 | gone |
| `f8889.last_month` | reached only out of bank order | 33 (16 seen in the bank-order walk itself, the rest only in a random order) | `f8889.married_family` := `all(household.married = true, f8889.family_any_time = true)` | H1 | f8889 | gone |
| `f8962.alien_below` | asked and unread | 132 (132 questions) | `f8962.alien_branch` := `all(f8962.any = true, f8962.line5 < 100, f8962.alien_below = true)` | P2 | f8962_applicable | gone |
| `f8962.estimate_100` | asked and unread | 132 (132 questions) | `f8962.applicable` := `any(f8962.line5 >= 100, all(f8962.aptc = true, f8962.estimate_100 = true))` | P2 | f8962_applicable | gone |
| `household.married` | left reachable at completion. At 3 such states no answer changes the status or a value | 3 | `f8889.married_family` := `all(household.married = true, f8889.family_any_time = true)` | H1 | f8889 | gone |
| `person.blind` | asked and unread | 5 (6 questions) | `sa.itemizes` := `any(sa.elect_itemize = true, sa.mfs_spouse_itemizes = true, sa.line17 > sa.standard)` | X4 | sa | gone |
| `person.born_after_1960` | left reachable at completion. At 34 such states no answer changes the status or a value | 9 | `eic.age_range` := `eic.age_range_count > 0` | L1 | eic_age | left on 2 return(s) |
| `person.born_after_1960` | reached only out of bank order | 6 (0 seen in the bank-order walk itself, the rest only in a random order) | `eic.age_range_count` := `sum_over(person, person.one, where all(person.born_before_2001 = true, person.born_after_1960 = true))` | X5, L1 | eic_age | gone |
| `person.born_after_1960` | asked and unread | 3 (3 questions) | `eic.age_range_count` := `sum_over(person, person.one, where all(person.born_before_2001 = true, person.born_after_1960 = true))` | X5, L1 | - | gone |
| `person.born_before_2001` | left reachable at completion. At 32 such states no answer changes the status or a value | 8 | `eic.age_range_count` := `sum_over(person, person.one, where all(person.born_before_2001 = true, person.born_after_1960 = true))`; `eic.age_range` := `eic.age_range_count > 0` | X5, L1 | - | left on 5 return(s) |
| `person.born_before_2001` | reached only out of bank order | 6 (0 seen in the bank-order walk itself, the rest only in a random order) | `eic.age_range_count` := `sum_over(person, person.one, where all(person.born_before_2001 = true, person.born_after_1960 = true))` | X5, L1 | - | left on 3 return(s) |
| `person.died_before_65` | reached only out of bank order | 20 (0 seen in the bank-order walk itself, the rest only in a random order) | `s1a.spouse_died_before_65_count` := `sum_over(person, person.one, where all(person.role = "spouse", person.died_before_65 = true))` | X1 | s1a_died | gone |
| `person.itin_applied` | reached only out of bank order | 1 (1 seen in the bank-order walk itself, the rest only in a random order) | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | - | not in these 2,000 on main either |
| `person.itin_applied` | asked and unread | 4 (4 questions) | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `person.tin` | reached only out of bank order | 76 (76 seen in the bank-order walk itself, the rest only in a random order) | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_odc | gone |
| `person.tin` | asked and unread | 21 (23 questions) | `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)` | D1 | dep_edutin, dep_odc | gone |
| `person.work_ssn` | left reachable at completion. At 18 such states no answer changes the status or a value | 13 | `household.any_work_ssn` := `household.work_ssn_count > 0` | L1 | - | left on 2 return(s) |
| `retirement.exception` | reached only out of bank order | 306 (0 seen in the bank-order walk itself, the rest only in a random order) | `retirement.has_exception` := `all(retirement.early = true, retirement.exception != "none")`; `retirement.is_e05` := `all(retirement.has_exception = true, retirement.exception = "e05")` | R1 | retirement | gone |
| `scveh.owned` | reached only out of bank order | 100 (100 seen in the bank-order walk itself, the rest only in a random order) | `scveh.is_actual_owned` := `all(scveh.method = "actual", scveh.owned = true)`; `scveh.is_actual_leased` := `all(scveh.method = "actual", scveh.owned = false)` | V1 | scveh | gone |
| `ssb.lived_apart` | reached only out of bank order | 227 (0 seen in the bank-order walk itself, the rest only in a random order) | `ssb.mfs_together` := `all(f1040.status = "mfs", ssb.lived_apart = false)` | S1 | ssb | gone |
| `f1095a.in_a_<month> (12 templates)` | asked and unread | 5 (96 questions) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |
| `f1095a.in_b_<month> (12 templates)` | reached only out of bank order | 1 (1 seen in the bank-order walk itself, the rest only in a random order) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |
| `f1095a.in_b_<month> (12 templates)` | asked and unread | 5 (51 questions) | `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > …` | P1 | f8962_bzero | gone |

Two findings are outside this table because no generated return of the sweep showed them on main:

- `person.sav_student`, reached only out of bank order: `person.sav_ineligible` := `any(person.sav_born = false, person.sav_student = true, all(sa.dependent = true, person.sav_claimed = true))` reads the student answer while the birth-date answer is unknown (family X6). Found by the one-entry-per-collection minimal returns (section 6) and by a hand-built return with a Form 1095-A and tax owed.
- `dependent.absence_no_return`, left reachable at completion (class L1, below): seen on 4 of 449 complete returns once the rewrites are in, and on none of 5,000 on main.

**Class L1, the lower bound of a count (not the BUG-0466 pattern; no rewrite proposed).** `household.any_work_ssn` := `household.work_ssn_count > 0` and `eic.age_range` := `eic.age_range_count > 0` are decided true as soon as one person's entry counts, while another person's `person.work_ssn` or birth-date answers are still unknown; `household.any_test2_person` := `household.test2_persons > 0` does the same for a second dependent's `dependent.absence_no_return`. This is the rule of spec 4.7.5 (a partial count keeps the known entries as a lower bound, and a comparison may be decided from it), which the spec restricts to counts with no pending refusal gate. At every such open question probed (84 on main, 45 with the rewrites) no answer changes the status or a value. `person.born_before_2001` is also reached out of bank order by the same route on 3 returns. These four templates are what a widened check would still hold after every rewrite: either listed in the baseline with that reason, or exempted by a rule in the check (an input reachable only under a count whose lower bound has already decided every reader). That is a decision for the owner; nothing was built.

## 4. Families: cause, rewrite and test

Each family is one or more lines of the same shape on one form, rewritten and tested together. Expressions are quoted as on main, in a compact notation (`all(...)`, `any(...)`, `choose{guard -> line; ...}`, `sum_over(collection, field, where ...)`). "Gone" and "New" compare the family's witness returns on main and with this family's patch alone; a finding listed as left belongs to another family. A finding that is "new" on a witness return is named and explained where it occurs; random orders differ between two builds, so a template of another family can show on a return where the sample missed it before.

Conventions followed (BUG-0471, BUG-0492, `docs/2026-11-06_formal_gates_design.md`, "Leaking conjunctions are rewritten as nested `choose`"): operands keep their original order, so an `all` and its chain stop at the same first false or refused operand and a complete return's value cannot change; the evaluator is untouched; the false alternative is the document's `<doc>.no` helper on the parameter `household.no`; helper lines go at the end of the document. The accepted trade-off applies to every family: on a record with an answer withheld, a value that the three-valued `all`/`any` decided from a later operand is unknown until the first guard is answered. One asserted fixture holds such a state (D5).

### D1. Credit for other dependents test reads citizenship and the filer's TIN past an undecided dependent test

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.odc_person` := `all(dependent.claimed = true, dependent.tin = true, dependent.citizen = true, dependent.ctc_child = false, household.all_tin = true)`
- **Pattern:** BUG-0466 conjunction. `all` goes on past the unknown first operand `dependent.claimed`; a later operand that is false decides it.
- **What a filer meets:** Serious class. With `dependent.tin`, `dependent.citizen` or `household.all_tin` answered No first, the line is false while `dependent.claimed` is still unknown, every target is known, and the interview reports complete with the dependent-test questions open. Two of them refuse the return when answered Yes (`dependent.multiple_support`, `dependent.kidnapped` through `dependent.qr_kidnapped`), and `dependent.citizen` or `dependent.canada_mexico` Yes refuses through `dependent.claimed_no_tin`. In bank order the same line asks `dependent.citizen`, `person.tin` and `person.itin_applied` before the dependent test is decided, and the complete return then does not read them.
- **Rewrite:** Nested `choose` in the operands' order: `dependent.claimed`, then `dependent.tin`, `dependent.citizen`, `dependent.ctc_child` = false, `household.all_tin` (3 helper lines). Patch: `/tmp/f1095a/patches/dep_odc.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 29 sweep returns that showed the family: questions asked in bank order 4808 to 4788 (20 saved on 18 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `dependent.citizen`, `person.itin_applied`, `person.tin`; left reachable at completion: `dependent.canada_mexico`, `dependent.disabled`, `dependent.kidnapped`, `dependent.multiple_support`, `dependent.qr_all_year`, `dependent.spouse_relative`, `dependent.supported`; out of bank order: `person.tin`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2935 questions.
- **Touched:** 1 line(s) rewritten, 3 helper line(s) added, in `dependent.yaml` (+78/-20 lines); 5 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`; review subjects (transcription, render, class M) of `dependent`.
- **Note:** Probed alone on the 134 returns that show an early completion on main: 72 states still report complete with a question open (107 open questions, against 243 and 321 on main), and no answer to any of them refuses the return or changes a value. So this one line removes every refusal-capable finding.

### D2. Qualifying relative test reads gross income and support past an undecided relationship

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.qualifying_relative` := `all(dependent.qr_relationship = true, dependent.qualifying_child = false, dependent.qr_income = true, dependent.supported = true)`; refusal gates: dependent.multiple_support, dependent.income_exception, dependent.married, dependent.qr_kidnapped
- **Pattern:** BUG-0466 conjunction (`all` of four).
- **What a filer meets:** `dependent.supported` is reachable while `dependent.gross_income` is unanswered and hidden once the income is at or above the limit; `dependent.gross_income` and `dependent.supported` are asked while `dependent.qr_relationship` waits on `dependent.qr_all_year`, and unread when it turns out false. Also leaves `dependent.qr_all_year` reachable at completion when the income test is false first.
- **Rewrite:** Nested `choose` in order: `dependent.qr_relationship`, `dependent.qualifying_child` = false, `dependent.qr_income`, `dependent.supported` (2 helper lines). The line's four refusal gates are unchanged. Patch: `/tmp/f1095a/patches/dep_qr.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 29 sweep returns that showed the family: questions asked in bank order 4808 to 4799 (9 saved on 8 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `dependent.gross_income`, `dependent.supported`; left reachable at completion: `dependent.spouse_relative`; out of bank order: `dependent.spouse_relative`, `dependent.supported`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2937 questions.
- **Touched:** 1 line(s) rewritten, 2 helper line(s) added, in `dependent.yaml` (+56/-16 lines); 5 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`; review subjects (transcription, render, class M) of `dependent`.

### D3. Disabled-person income exception reads gross income before the disability answer

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.income_exception` := `all(dependent.disabled = true, dependent.qr_income = false)`
- **Pattern:** BUG-0466 conjunction on a refusal gate of `dependent.qualifying_relative`.
- **What a filer meets:** `dependent.gross_income` is reachable until `dependent.disabled` is answered No; with the income below the limit first, `dependent.disabled` stays reachable at completion. At 3 of 85 such states an answer (disabled Yes, or income at or above the limit) refuses the return through this gate; those states are complete only because `dependent.odc_person` (D1) was decided past the undecided dependent test, and D1's rewrite alone removes them.
- **Rewrite:** Nested `choose` on `dependent.disabled` first, then the income test (1 helper line). Patch: `/tmp/f1095a/patches/dep_incx.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 29 sweep returns that showed the family: questions asked in bank order 4808 to 4808 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: left reachable at completion: `dependent.qr_all_year`, `dependent.spouse_relative`; out of bank order: `dependent.gross_income`, `dependent.spouse_relative`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 1 helper line(s) added, in `dependent.yaml` (+24/-8 lines); 5 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`; review subjects (transcription, render, class M) of `dependent`.

### D4. Member-of-household relationship test reads the spouse-relative and lawful-relationship answers out of turn

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.qr_other_relation` := `any(all(f1040.status = "mfj", dependent.spouse_relative = true), all(dependent.qr_all_year = true, dependent.lawful = true))`
  - `dependent.qr_household_member` := `any(all(f1040.status = "mfj", dependent.spouse_relative = true), dependent.qr_all_year = true)`
- **Pattern:** BUG-0466 conjunction: `any` of two `all`s.
- **What a filer meets:** `dependent.lawful` is asked while `dependent.qr_all_year` is unanswered and unread when that is No; `dependent.spouse_relative` is reachable before the filing status is known and left reachable at completion when the all-year branch decides the `any`.
- **Rewrite:** Nested `choose`: joint return and `dependent.spouse_relative` first, then `dependent.qr_all_year`, then `dependent.lawful` (5 helper lines over the two lines). Patch: `/tmp/f1095a/patches/dep_qrrel.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 29 sweep returns that showed the family: questions asked in bank order 4808 to 4804 (4 saved on 4 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `dependent.lawful`; left reachable at completion: `dependent.lawful`, `dependent.spouse_relative`; out of bank order: `dependent.spouse_relative`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2937 questions.
- **Touched:** 5 line(s) rewritten, 5 helper line(s) added, in `dependent.yaml` (+123/-33 lines); 8 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`; review subjects (transcription, render, class M) of `dependent`.

### D5. Head of household person tests read the absence, months and parent's-home answers out of turn

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.hoh_test2` := `all(dependent.hoh_test2_lived = true, dependent.absence_no_return = false)`
  - `dependent.hoh_test1` := `all(dependent.relationship = "parent", dependent.claimed = true, dependent.parent_home_paid = true)`; refusal gates: dependent.claimed_no_tin
  - `dependent.hoh_test2_lived` := `any(all(dependent.claimed = true, dependent.relationship != "household_member", dependent.relationship != "sibling_descendant", dependent.relationship != "other", dependent.hoh_lived_half = true), all(dependent.qualifying_child = true, dependent.married = false, dependent.lived_half = true))`
- **Pattern:** BUG-0466 conjunctions (`all` of two, `all` of three, `any` of two `all`s).
- **What a filer meets:** `dependent.absence_no_return` is asked before `dependent.hoh_test2_lived` is decided (unread on 6 returns) and reachable in other orders; `dependent.months` and `dependent.parent_home_paid` are reachable while `dependent.claimed` or the relationship is undecided.
- **Rewrite:** Nested `choose` in order on each of the three lines (12 helper lines). Patch: `/tmp/f1095a/patches/dep_hoh.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1767/1768, New York 338/338. The one federal fixture that changes is `stage8.mut.hoh_child_months_unanswered_absence`: `dependent[child].hoh_test2` was false and is unknown, with `dependent[child].months` unanswered (an incomplete state; no value or refusal of a complete return changes). Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 15 sweep returns that showed the family: questions asked in bank order 2514 to 2512 (2 saved on 2 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `dependent.absence_no_return`; left reachable at completion: `dependent.disabled`; out of bank order: `dependent.absence_no_return`, `dependent.months`, `dependent.parent_home_paid`. New there: left reachable at completion: `dependent.absence_no_return`; out of bank order: `eic.legally_separated`, `eic.same_home`. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2969 questions.
- **Touched:** 5 line(s) rewritten, 12 helper line(s) added, in `dependent.yaml` (+252/-58 lines); 5 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`; review subjects (transcription, render, class M) of `dependent`.
- **Note:** The three lines must land together: with `dependent.hoh_test2_lived` alone (`patches/dep_hoh2lived.patch`) the interview newly asks `dependent.absence_no_return` on 3 of the 15 witness returns, because `dependent.hoh_test2`, still an `all`, reads it past the now longer-unknown first operand. The fixture change comes from `dependent.hoh_test2` alone (`patches/dep_hoh2.patch`). The new early completion of `dependent.absence_no_return` is class L1 (`household.any_test2_person` decided by another dependent's entry; no answer changes anything). `eic.legally_separated` and `eic.same_home` are family X2's, reached here by a random order that differs between the two builds. The 31 more questions of the standard set are on two refused generated returns (104 to 124 and 123 to 134); no complete return is longer.

### D6. Lifetime learning credit TIN refusal reads the TIN answer before the student test

- **Cause lines** (`forms/2025/`, as on main):
  - `dependent.edu_llc_tin_refused` := `all(dependent.edu_llc = true, dependent.edu_tin_issued = false)`
  - `person.edu_llc_tin_refused` := `all(person.edu_llc = true, person.tin = false)`
- **Pattern:** BUG-0466 conjunction on a refusal gate; the person-level line is the same expression and was found only after the dependent one was fixed.
- **What a filer meets:** `dependent.edu_tin_issued` is reachable until `dependent.edu` is answered No; `person.tin` is asked while `person.edu` is unanswered and unread when it is No.
- **Rewrite:** Nested `choose` on `edu_llc` first, then the TIN test, on both lines (2 helper lines). Patch: `/tmp/f1095a/patches/dep_edutin.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 16 sweep returns that showed the family: questions asked in bank order 2654 to 2653 (1 saved on 1 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `person.tin`; out of bank order: `dependent.edu_tin_issued`. New there: out of bank order: `person.tin`. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 2 line(s) rewritten, 2 helper line(s) added, in `dependent.yaml`, `person.yaml` (+54/-20 lines); 7 of 52 pinned mutation arguments un-pinned; rendered files changed: `dependent.md`, `index.md`, `person.md`; review subjects (transcription, render, class M) of `dependent`, `person`.
- **Note:** The out-of-order `person.tin` that appears on one witness return is family D1's (`dependent.odc_person` reads `household.all_tin`): on main the question was asked there and unread; once it is no longer asked, D1's reach of it is what remains. With every rewrite it is gone.

### P1. Form 8962 zero-column-(b) refusal reads Form 1095-A columns A and B before the applicable-taxpayer test

- **Cause lines** (`forms/2025/`, as on main):
  - `f8962.b_zero` := `all(f8962.show_applicable = true, any(all(f8962.line12a > 0, f8962.line12b = 0), all(f8962.line13a > 0, f8962.line13b = 0), all(f8962.line14a > 0, f8962.line14b = 0), all(f8962.line15a > 0, f8962.line15b = 0), all(f8962.line16a > 0, f8962.line16b = 0), all(f8962.line17a > 0, f8962.line17b = 0), all(f8962.line18a > 0, f8962.line18b = 0), all(f8962.line19a > 0, f8962.line19b = 0), all(f8962.line20a > 0, f8962.line20b = 0), all(f8962.line21a > 0, f8962.line21b = 0), all(f8962.line22a > 0, f8962.line22b = 0), all(f8962…`
- **Pattern:** BUG-0466 conjunction on a refusal gate of `f8962.line24` (through `f8962.two_counted`).
- **What a filer meets:** For a filer who is not an applicable taxpayer the interview asks up to 24 monthly column A and B amounts per Form 1095-A (or `f1095a.mo_a`, `f1095a.mo_b` and `f1095a.b_counted`) that the return never reads; column B of a month is reachable until that month's column A is answered zero.
- **Rewrite:** `choose` on `f8962.show_applicable` (No: false; Yes: the month tests), top level only (1 helper line holding the twelve month tests unchanged). Patch: `/tmp/f1095a/patches/f8962_bzero.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 17 sweep returns that showed the family: questions asked in bank order 3186 to 3041 (145 saved on 9 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `f1095a.in_a_<month>` (12 months), `f1095a.in_b_<month>` (12 months), `f1095a.b_counted`, `f1095a.mo_a`, `f1095a.mo_b`; out of bank order: `f1095a.in_b_<month>` (9 months). New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 1 helper line(s) added, in `f8962.yaml` (+151/-128 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `f8962.md`, `index.md`; review subjects (transcription, render, class M) of `f8962`.
- **Note:** Hand-built returns with one monthly Form 1095-A and every other answer closed (`out/min_dec_only.json`, `min_allmonths.json`, `min_halfyear.json`): 112 to 99, 121 to 97 and 115 to 97 questions, none unread after. The month lines' `shown_when` (`f8962.show_jan` to `show_dec`) read columns A and B and are unknown at completion for a filer who is not an applicable taxpayer, before and after; what the renderer does with an unknown `shown_when` was not checked.

### P2. Applicable-taxpayer test asks the Marketplace-estimate and lawfully-present-alien questions before household income (BUG-0487)

- **Cause lines** (`forms/2025/`, as on main):
  - `f8962.applicable` := `any(f8962.line5 >= 100, all(f8962.aptc = true, f8962.estimate_100 = true))`
  - `f8962.alien_branch` := `all(f8962.any = true, f8962.line5 < 100, f8962.alien_below = true)`
- **Pattern:** BUG-0466 conjunction; the three templates BUG-0487 holds in `walked_unused`.
- **What a filer meets:** `f8962.estimate_100`, `f8962.alien_below` and `f1095a.c_total` are asked on every return with a Form 1095-A before line 5 is known, and unread when line 5 is at least 100.
- **Rewrite:** Nested `choose`: `f8962.applicable` on the line 5 test first, then `f8962.aptc`, then `f8962.estimate_100`; `f8962.alien_branch` on `f8962.any`, then line 5 below 100, then `f8962.alien_below` (4 helper lines). Patch: `/tmp/f1095a/patches/f8962_applicable.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 8 sweep returns that showed the family: questions asked in bank order 1278 to 1263 (15 saved on 7 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `f1095a.c_total`, `f8962.alien_below`, `f8962.estimate_100`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2896 questions.
- **Touched:** 3 line(s) rewritten, 4 helper line(s) added, in `f8962.yaml` (+103/-29 lines); 1 of 52 pinned mutation arguments un-pinned; rendered files changed: `f8962.md`, `index.md`; review subjects (transcription, render, class M) of `f8962`.
- **Note:** Of the 42 questions fewer in the standard set, 3 are on the complete generated return 4 and 39 on the refused generated return 10. With this rewrite the three `walked_unused` holds of BUG-0487 fail as no longer seen and are removed from the baseline.

### E1. Form 5695 Part II section tests read later yes/no lines before the first

- **Cause lines** (`forms/2025/`, as on main):
  - `f5695.sec_a_claimed` := `all(f5695.line17a = true, f5695.line17b = true, f5695.line17c = true)`
  - `f5695.sec_a_new_home` := `all(f5695.sec_a_claimed = true, f5695.line17e = true)`
  - `f5695.sec_b_claimed` := `all(f5695.line21a = true, f5695.line21b = true)`
  - `f5695.sec_b_new_home` := `all(f5695.sec_b_claimed = true, f5695.b_new_home = true)`
  - `f5695.enabling_claimed` := `all(f5695.sec_b_claimed = true, f5695.line25a = true)`
  - `f5695.separate_homes_joint` := `all(f1040.status = "mfj", f5695.separate_homes = true)`
  - `f5695.ac_no_qmid` := `all(f5695.line22c > param sales.zero, f5695.qmid_ac = false)`
  - `f5695.doors_no_qmid` := `all(f5695.doors_cost > param sales.zero, f5695.qmid_doors = false)`
  - `f5695.windows_no_qmid` := `all(f5695.line20c > param sales.zero, f5695.qmid_windows = false)`
  - `f5695.enabling_no_qmid` := `all(f5695.line25c > param sales.zero, f5695.qmid_enabling = false)`
- **Pattern:** BUG-0466 conjunctions. BUG-0471 rewrote `f5695.wh_no_qmid`, `furnace_no_qmid` and `hp_no_qmid`; `ac_no_qmid` and its three siblings were left as `all`.
- **What a filer meets:** Lines 17b, 17c, 17e and 25a, `f5695.qmid_ac` and `f5695.separate_homes` are reachable before the answer that decides them; `f5695.b_new_home` is asked and unread.
- **Rewrite:** Nested `choose` in order on the ten lines (10 helper lines). `doors_no_qmid`, `windows_no_qmid` and `enabling_no_qmid` showed no finding in the sweeps and are included as siblings of the same shape. Patch: `/tmp/f1095a/patches/f5695.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 2 sweep returns that showed the family: questions asked in bank order 325 to 324 (1 saved on 1 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `f5695.b_new_home`; out of bank order: `f5695.line17b`, `f5695.line17c`, `f5695.line17e`, `f5695.line25a`, `f5695.qmid_ac`, `f5695.separate_homes`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 10 line(s) rewritten, 10 helper line(s) added, in `f5695.yaml` (+280/-104 lines); 3 of 52 pinned mutation arguments un-pinned; rendered files changed: `f5695.md`, `index.md`; review subjects (transcription, render, class M) of `f5695`.

### H1. Form 8889 excess-contribution, married-family and split tests read their second operand first

- **Cause lines** (`forms/2025/`, as on main):
  - `f8889.excess` := `all(f8889.line11 > f8889.line8, f8889.employer_in_box1 = false)`
  - `f8889.married_family` := `all(household.married = true, f8889.family_any_time = true)`
  - `f8889.split` := `all(f8889.married_family = true, household.hsa_both = true)`
- **Pattern:** BUG-0466 conjunctions.
- **What a filer meets:** `f8889.employer_in_box1` is reachable until line 9 or the months are answered; `f8889.last_month` until `household.married` is answered; `household.married` is left reachable at completion when the family test is false first.
- **Rewrite:** Nested `choose` in order on the three lines (3 helper lines). Patch: `/tmp/f1095a/patches/f8889.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 11 sweep returns that showed the family: questions asked in bank order 1337 to 1337 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: left reachable at completion: `household.married`; out of bank order: `f8889.employer_in_box1`, `f8889.last_month`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 3 line(s) rewritten, 3 helper line(s) added, in `f8889.yaml` (+76/-30 lines); 3 of 52 pinned mutation arguments un-pinned; rendered files changed: `f8889.md`, `index.md`; review subjects (transcription, render, class M) of `f8889`.
- **Note:** `f8889.split` := `all(f8889.married_family = true, household.hsa_both = true)` was added after the first test of this family: with only the first two lines nested, `household.married` was still left reachable at completion at one probed state, through this line. `patches/f8889.patch` has all three; `ALL_combined.patch` was built before and has the first two.

### V1. Vehicle ownership is reachable before the expense method

- **Cause lines** (`forms/2025/`, as on main):
  - `scveh.is_actual_owned` := `all(scveh.method = "actual", scveh.owned = true)`
  - `scveh.is_actual_leased` := `all(scveh.method = "actual", scveh.owned = false)`
- **Pattern:** BUG-0466 conjunctions.
- **What a filer meets:** `scveh.owned` is reachable until `scveh.method` is answered with the standard mileage rate.
- **Rewrite:** Nested `choose` on the method test first on both lines (4 helper lines, one of them `scveh.no`). Patch: `/tmp/f1095a/patches/scveh.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 6 sweep returns that showed the family: questions asked in bank order 1141 to 1141 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `scveh.owned`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 2 line(s) rewritten, 4 helper line(s) added, in `scveh.yaml` (+74/-20 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `index.md`, `scveh.md`; review subjects (transcription, render, class M) of `scveh`.

### R1. Early-distribution exception is reachable before the distribution code

- **Cause lines** (`forms/2025/`, as on main):
  - `retirement.has_exception` := `all(retirement.early = true, retirement.exception != "none")`
  - `retirement.is_e05` := `all(retirement.has_exception = true, retirement.exception = "e05")`
  - `retirement.is_e09` := `all(retirement.has_exception = true, retirement.exception = "e09")`
  - `retirement.is_e19` := `all(retirement.has_exception = true, retirement.exception = "e19")`
  - `retirement.is_e22` := `all(retirement.has_exception = true, retirement.exception = "e22")`
  - `retirement.is_e23` := `all(retirement.has_exception = true, retirement.exception = "e23")`
  - `retirement.wrong_kind` := `all(retirement.has_exception = true, any(all(retirement.is_ira = true, any(retirement.exception = "e01", retirement.exception = "e06")), all(retirement.is_ira = false, any(retirement.exception = "e07", retirement.exception = "e08", retirement.exception = "e09"))))`
- **Pattern:** BUG-0466 conjunctions: seven lines read `retirement.exception` past `retirement.early` or `retirement.has_exception`.
- **What a filer meets:** `retirement.exception` is reachable in other orders before `retirement.code` is answered. The bank order already asks the code first, so no question is saved.
- **Rewrite:** Nested `choose` in order on the seven lines, `retirement.wrong_kind` at its top level only. Patch: `/tmp/f1095a/patches/retirement.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 6 sweep returns that showed the family: questions asked in bank order 783 to 783 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `retirement.exception`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 7 line(s) rewritten, 8 helper line(s) added, in `retirement.yaml` (+232/-104 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `index.md`, `retirement.md`; review subjects (transcription, render, class M) of `retirement`.
- **Note:** `retirement.is_e05` to `is_e23` and `retirement.wrong_kind` read the exception past `retirement.has_exception`, so nesting `has_exception` alone would leave the question reachable; all seven go together.

### S1. Lived-apart question is reachable before the filing status

- **Cause lines** (`forms/2025/`, as on main):
  - `ssb.mfs_together` := `all(f1040.status = "mfs", ssb.lived_apart = false)`
  - `f1040.line6d` := `all(f1040.status = "mfs", ssb.lived_apart = true)`
- **Pattern:** BUG-0466 conjunctions on the filing status.
- **What a filer meets:** `ssb.lived_apart` is reachable before the filing status is known. Bank order asks the status first.
- **Rewrite:** Nested `choose` on the status test first on both lines (5 helper lines, among them `ssb.no` and `f1040.no`). Patch: `/tmp/f1095a/patches/ssb.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 6 sweep returns that showed the family: questions asked in bank order 787 to 787 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `ssb.lived_apart`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 2 line(s) rewritten, 5 helper line(s) added, in `f1040.yaml`, `ssb.yaml` (+84/-20 lines); 5 of 52 pinned mutation arguments un-pinned; rendered files changed: `f1040.md`, `index.md`, `ssb.md`; review subjects (transcription, render, class M) of `f1040`, `ssb`.

### A1. Section 179 screen asks the not-eligible question before the amount

- **Cause lines** (`forms/2025/`, as on main):
  - `asset.s179_bad` := `all(asset.s179 > asset.zero, any(asset.s179 > asset.basis, asset.over_half = false, asset.not179 = true))`
- **Pattern:** BUG-0466 conjunction on a refusal gate: `all` of an amount test and an `any` of three.
- **What a filer meets:** `asset.not179` is asked for each asset before `asset.s179` and the business-use percentage are answered, and unread when no section 179 amount is elected.
- **Rewrite:** Nested `choose`: the amount above zero first, then the three tests in order (6 helper lines). Patch: `/tmp/f1095a/patches/asset.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 5 sweep returns that showed the family: questions asked in bank order 1235 to 1230 (5 saved on 5 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `asset.not179`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 2 line(s) rewritten, 6 helper line(s) added, in `asset.yaml` (+114/-18 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `asset.md`, `index.md`; review subjects (transcription, render, class M) of `asset`.

### X1. Schedule 1-A died-before-65 counts read the answer before the person's role

- **Cause lines** (`forms/2025/`, as on main):
  - `s1a.spouse_died_before_65_count` := `sum_over(person, person.one, where all(person.role = "spouse", person.died_before_65 = true))`
  - `s1a.died_before_65_count` := `sum_over(person, person.one, where all(person.role = "taxpayer", person.died_before_65 = true))`
- **Pattern:** BUG-0466 in a `sum_over` filter: `where all(role, died_before_65)`.
- **What a filer meets:** `person.died_before_65` is reachable for a person whose role is not yet known.
- **Rewrite:** Two per-person lines that take the role first (the `person.spouse_senior_work_ssn` pattern), read by the two counts' filters. Written by hand (`patches_hand/s1a_died.sh`). Patch: `/tmp/f1095a/patches/s1a_died.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 3 sweep returns that showed the family: questions asked in bank order 637 to 637 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `person.died_before_65`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 0 line(s) rewritten, 2 helper line(s) added, in `person.yaml`, `s1a.yaml` (+50/-18 lines); 3 of 52 pinned mutation arguments un-pinned; rendered files changed: `index.md`, `person.md`, `s1a.md`; review subjects (transcription, render, class M) of `person`, `s1a`.

### C1. Car loan vehicle test is reachable before the loan requirements

- **Cause lines** (`forms/2025/`, as on main):
  - `carloan.eligible` := `all(carloan.requirements = true, carloan.vehicle = true)`
- **Pattern:** BUG-0466 conjunction.
- **What a filer meets:** `carloan.vehicle` is reachable until `carloan.requirements` is answered No.
- **Rewrite:** Nested `choose` on `carloan.requirements` first. Patch: `/tmp/f1095a/patches/carloan.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 1 sweep returns that showed the family: questions asked in bank order 199 to 199 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `carloan.vehicle`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 1 helper line(s) added, in `carloan.yaml` (+24/-10 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `carloan.md`, `index.md`; review subjects (transcription, render, class M) of `carloan`.

### X2. EIC Step 3 separation questions are reachable before the marital rules are known

- **Cause lines** (`forms/2025/`, as on main):
  - `eic.step3_married` := `any(eic.married_rules = false, eic.same_home = false, eic.legally_separated = true)`
- **Pattern:** BUG-0466 conjunction: `any` of three.
- **What a filer meets:** `eic.same_home` and `eic.legally_separated` are reachable before `eic.married_rules` is decided; `eic.legally_separated` is asked and unread on one return of 5,000.
- **Rewrite:** Nested `choose`: `eic.married_rules` = false first, then `eic.same_home` = false, then `eic.legally_separated`. Patch: `/tmp/f1095a/patches/eic_step3.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 1 sweep returns that showed the family: questions asked in bank order 150 to 150 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `eic.legally_separated`, `eic.same_home`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 3 helper line(s) added, in `eic.yaml` (+63/-14 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `eic.md`, `index.md`; review subjects (transcription, render, class M) of `eic`.

### X3. Form 2441 nondependent-care question is reachable before the care question

- **Cause lines** (`forms/2025/`, as on main):
  - `f2441.nondependent_gate` := `all(f2441.care = true, f2441.nondependent = true)`
- **Pattern:** BUG-0466 conjunction.
- **What a filer meets:** `f2441.nondependent` is reachable until `f2441.care` is answered No.
- **Rewrite:** Nested `choose` on `f2441.care` first. Patch: `/tmp/f1095a/patches/f2441.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 2 sweep returns that showed the family: questions asked in bank order 361 to 361 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: out of bank order: `f2441.nondependent`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 0 helper line(s) added, in `f2441.yaml` (+12/-8 lines); 0 of 52 pinned mutation arguments un-pinned; rendered files changed: `f2441.md`; review subjects (transcription, render, class M) of `f2441`.

### X4. Itemize test reads the standard deduction before the election to itemize

- **Cause lines** (`forms/2025/`, as on main):
  - `sa.itemizes` := `any(sa.elect_itemize = true, sa.mfs_spouse_itemizes = true, sa.line17 > sa.standard)`
- **Pattern:** BUG-0466 conjunction: `any` of three whose third operand compares line 17 with the standard deduction.
- **What a filer meets:** `person.blind` (read by the standard deduction) is asked before `sa.elect_itemize` and unread when the filer elects to itemize.
- **Rewrite:** Nested `choose`: `sa.elect_itemize` first, then `sa.mfs_spouse_itemizes`, then the comparison (2 helper lines). Patch: `/tmp/f1095a/patches/sa.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 3 sweep returns that showed the family: questions asked in bank order 534 to 531 (3 saved on 3 returns); status differs on 0, values on 0; order errors 0. Gone there: asked and unread: `person.blind`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 1 line(s) rewritten, 2 helper line(s) added, in `sa.yaml` (+52/-12 lines); 1 of 52 pinned mutation arguments un-pinned; rendered files changed: `index.md`, `sa.md`; review subjects (transcription, render, class M) of `sa`.

### X5. EIC age-range count reads both birth-date answers at once

- **Cause lines** (`forms/2025/`, as on main):
  - `eic.age_range_count` := `sum_over(person, person.one, where all(person.born_before_2001 = true, person.born_after_1960 = true))`
- **Pattern:** BUG-0466 in a `sum_over` filter: `where all(born_before_2001, born_after_1960)`. The early-completion findings on the same two inputs are the lower-bound class L1 and stay.
- **What a filer meets:** `person.born_after_1960` is asked while `person.born_before_2001` is unanswered and unread when that is No.
- **Rewrite:** A per-person line `person.eic_age_range` (born before 2001 first, then born after 1960), read by the count's filter. Written by hand (`patches_hand/eic_age.sh`). Patch: `/tmp/f1095a/patches/eic_age.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 6 sweep returns that showed the family: questions asked in bank order 1078 to 1078 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: left reachable at completion: `person.born_after_1960`; out of bank order: `person.born_after_1960`. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 0 line(s) rewritten, 1 helper line(s) added, in `eic.yaml`, `person.yaml` (+27/-9 lines); 2 of 52 pinned mutation arguments un-pinned; rendered files changed: `eic.md`, `index.md`, `person.md`; review subjects (transcription, render, class M) of `eic`, `person`.
- **Note:** `person.born_before_2001` and `person.born_after_1960` stay left reachable at completion on returns with two people (class L1: `eic.age_range` is decided by the first person's entry). One of those is in a bank-order walk.

### X6. Saver's credit ineligibility test reads the student answer before the birth-date answer

- **Cause lines** (`forms/2025/`, as on main):
  - `person.sav_ineligible` := `any(person.sav_born = false, person.sav_student = true, all(sa.dependent = true, person.sav_claimed = true))`
- **Pattern:** BUG-0466 conjunction: `any` of three. Found only by the one-entry-per-collection minimal returns, not by 5,000 generated returns.
- **What a filer meets:** `person.sav_student` is reachable until `person.sav_born` is answered No.
- **Rewrite:** Nested `choose` in order. Patch: `/tmp/f1095a/patches/sav.patch`.
- **Test (this family alone, on main's tip):** build OK; fixtures pass federal 1768/1768, New York 338/338. Target values and status of 1500 generated returns (360 complete) and of every fixture's inputs: 0 differ from main. On the 0 sweep returns that showed the family: questions asked in bank order 0 to 0 (0 saved on 0 returns); status differs on 0, values on 0; order errors 0. Gone there: none. New there: none. Standard length set (full profile, 28 walks, complete and refused): 2938 to 2938 questions.
- **Touched:** 2 line(s) rewritten, 3 helper line(s) added, in `person.yaml` (+70/-17 lines); 2 of 52 pinned mutation arguments un-pinned; rendered files changed: `index.md`, `person.md`; review subjects (transcription, render, class M) of `person`.
- **Note:** No generated return of the sweep shows it, so there is no witness set; on the hand-built return `out/min_dec_only.json` `person.sav_student` is reached out of order on main and not with the patch.

## 5. Ranking: filer benefit against cost

Benefit is questions a filer answers for nothing (the "unread" column: questions asked in bank order and not read, over the 1,147 complete returns of the sweep, attributed to the family whose rewrite removed them in its own test), weighed by who meets the case, with the refusal-capable findings first. The generated returns are not a sample of filers: the generator draws dependents, Forms 1095-A and businesses far more often than the population has them, so the share column (from `interview/2025/gate_frequencies.yaml`, the share of all returns in the situation that leads to the questions) is the better guide to how often, and the unread column to how many questions when it happens. Families that are "out of order" only save no question in the interface, which asks the first open question in bank order; their benefit is a smaller pending count and a check that can be widened without holds. Cost is lines rewritten (lines nested by the tool, including helper lines it nested in turn) plus helper lines added, fixtures changed, pinned mutation arguments whose digest moves, and the forms whose reviews fall due.

| Rank | Family | Classes seen | Complete returns showing it (of 1147) | Unread questions (5,000 returns) | Who meets it (share of all returns, `gate_frequencies.yaml`) | Lines rewritten + helpers | Fixtures changed | Pins un-pinned (of 52) | Forms to re-review | Why here |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **D1** Credit for other dependents test reads citizenship and the filer's TIN past an undecided dependent test | left reachable at completion, out of order, asked and unread | 276 | 253 | dependents: 29.4% | 1 + 3 | 0 | 5 | dependent | Removes the only findings where an unanswered question can refuse a return the interview calls complete, and the most unread questions. |
| 2 | **P2** Applicable-taxpayer test asks the Marketplace-estimate and lawfully-present-alien questions before household income (BUG-0487) | asked and unread | 132 | 269 | marketplace: 8.5% | 3 + 4 | 0 | 1 | f8962 | Two questions on nearly every return with a Form 1095-A; closes BUG-0487 and empties the baseline. |
| 3 | **D2** Qualifying relative test reads gross income and support past an undecided relationship | out of order, asked and unread | 148 | 138 | dependents: 29.4% | 1 + 2 | 0 | 5 | dependent | Second most unread questions; same form and review round as D1. |
| 4 | **P1** Form 8962 zero-column-(b) refusal reads Form 1095-A columns A and B before the applicable-taxpayer test | out of order, asked and unread | 15 | 183 | marketplace: 8.5% | 1 + 1 | 0 | 0 | f8962 | Up to 24 amounts per Form 1095-A, but only for filers who are not applicable taxpayers. |
| 5 | **D4** Member-of-household relationship test reads the spouse-relative and lawful-relationship answers out of turn | left reachable at completion, asked and unread | 43 | 40 | dependents: 29.4% | 5 + 5 | 0 | 8 | dependent | One hard question (lawful relationship) for member-of-household dependents. |
| 6 | **D3** Disabled-person income exception reads gross income before the disability answer | out of order | 31 | 0 | dependents: 29.4% | 1 + 1 | 0 | 5 | dependent | No question saved in bank order; its gate is one D1 stops leaving open (3 of 85 states refuse there on main). |
| 7 | **A1** Section 179 screen asks the not-eligible question before the amount | asked and unread | 20 | 21 | self_employment (with depreciable property): 19.0% | 2 + 6 | 0 | 0 | asset | One question per business asset for filers who elect no section 179. |
| 8 | **H1** Form 8889 excess-contribution, married-family and split tests read their second operand first | left reachable at completion, out of order | 171 | 0 | hsa: 11.0% | 3 + 3 | 0 | 3 | f8889 | Out of order only, and `household.married` left open at completion (benign there). |
| 9 | **D6** Lifetime learning credit TIN refusal reads the TIN answer before the student test | out of order | 96 | 0 | education: 9.0% | 2 + 2 | 0 | 7 | dependent, person | One unread question on 1 return of 5,000; the dependent line is out of order only. |
| 10 | **X4** Itemize test reads the standard deduction before the election to itemize | asked and unread | 5 | 6 | (filers who elect to itemize when the standard deduction is larger: no share recorded) | 1 + 2 | 0 | 1 | sa | `person.blind` asked of filers who then elect to itemize. |
| 11 | **X5** EIC age-range count reads both birth-date answers at once | left reachable at completion, out of order, asked and unread | 12 | 3 | (EIC claimants without a qualifying child: no share recorded) | 0 + 1 | 0 | 2 | eic, person | One birth-date question; the early-completion findings on these inputs stay (L1). |
| 12 | **V1** Vehicle ownership is reachable before the expense method | out of order | 100 | 0 | self_employment (a business vehicle is a part of it): 19.0% | 2 + 4 | 0 | 0 | scveh | Out of order only; no question saved. |
| 13 | **S1** Lived-apart question is reachable before the filing status | out of order | 227 | 0 | social_security: 20.0% | 2 + 5 | 0 | 5 | f1040, ssb | Out of order only; no question saved. |
| 14 | **R1** Early-distribution exception is reachable before the distribution code | out of order | 306 | 0 | retirement_distributions: 23.6% | 7 + 8 | 0 | 0 | retirement | Out of order only; seven lines for no question saved. |
| 15 | **E1** Form 5695 Part II section tests read later yes/no lines before the first | out of order, asked and unread | 2 | 1 | home_improvement_part2: 1.6% | 10 + 10 | 0 | 3 | f5695 | Out of order only bar one unread question on 1 return; ten lines. |
| 16 | **D5** Head of household person tests read the absence, months and parent's-home answers out of turn | out of order, asked and unread | 73 | 6 | dependents: 29.4% | 5 + 12 | 1 | 5 | dependent | Six unread questions in 5,000 returns; changes one asserted fixture to unknown and adds questions on refused returns. |
| 17 | **X3** Form 2441 nondependent-care question is reachable before the care question | out of order | 2 | 0 | care_expenses: 4.5% | 1 + 0 | 0 | 0 | f2441 | Out of order only. |
| 18 | **X2** EIC Step 3 separation questions are reachable before the marital rules are known | out of order, asked and unread | 2 | 1 | (EIC claimants who are married and not filing jointly: no share recorded) | 1 + 3 | 0 | 0 | eic | Out of order only bar one unread question on 1 return. |
| 19 | **C1** Car loan vehicle test is reachable before the loan requirements | out of order | 1 | 0 | (Schedule 1-A Part IV car loan interest: no share recorded under this input) | 1 + 1 | 0 | 0 | carloan | Out of order only. |
| 20 | **X1** Schedule 1-A died-before-65 counts read the answer before the person's role | out of order | 20 | 0 | spouse_died (the nearest recorded share): 0.6% | 0 + 2 | 0 | 3 | person, s1a | Out of order only. |
| 21 | **X6** Saver's credit ineligibility test reads the student answer before the birth-date answer | none in the sweep | 0 | 0 | (saver's credit candidates: no share recorded) | 2 + 3 | 0 | 2 | person | Out of order only; seen on no generated return. |


Notes on the table and on landing:

- **Review cost is not measured.** Each form's transcription and render reviews are line-scoped to the changed lines; class M has no line scope and reruns per form. For scale, the inventory records $62.45 for BUG-0471 (53 lines, 14 forms) and $39.13 for BUG-0492 (16 lines, 6 forms); those are the entries' figures, not re-derived. D1 to D6 share `dependent.yaml`, and P1 and P2 share `f8962.yaml`, so landing a form's families together pays for its reviews once.
- **Pins.** The premise digest covers each premise line's readers, so a rewrite un-pins arguments that never name the rewritten line. `f5695.separate_homes_joint` gains a helper that reads `f1040.status`, which un-pins a New York argument, a dependent one and a household one whose premises include `f1040.status`. All rewrites together un-pin 18 of 52. Each un-pinned argument has to be re-argued or its digest renewed; new helper lines also create new mutants (BUG-0492 added seven fixture cases to kill eleven survivors), which `mutate` would show and was not run.
- **Families that must not be split or need a sibling:** D5 lands as three lines or not at all (`dependent.hoh_test2_lived` alone adds a question on 3 of 15 returns). H1 needs `f8889.split` with it, or `household.married` is still left open at completion. D6 needs both the dependent and the person line. P1 and R1 are rewritten at the top level only (`f8962.b_zero!`, `retirement.wrong_kind!` in `nest.py`'s notation): nesting the twelve month tests of `f8962.b_zero` as well adds 47 helper lines, and the top-level rewrite already removes every Form 1095-A finding on its witness returns.
- **D5's fixture.** `stage8.mut.hoh_child_months_unanswered_absence` asserts `dependent[child].hoh_test2` false with `dependent[child].months` unanswered; it becomes unknown. It changes with `dependent.hoh_test2` alone (`patches/dep_hoh2.patch`: 1,767 of 1,768) and with neither of the other two lines alone. By its name it is a mutation-killing case, so its mutant would need another kill.
- **Refused returns.** With every rewrite, 640 of the 1,551 refused returns of the 2,000-return sweep are walked in fewer questions and 26 in more (the walk goes on past a refusal while a reachable question has an answer, and a chain that is unknown where the conjunction was false leaves more reachable). No complete return is longer.
- **Patches.** One patch per family in `/tmp/f1095a/patches/`, each against main's tip and each tested alone. They do not compose by `git apply` (several add helper lines at the same place in `dependent.yaml` or `person.yaml`); `ALL_combined.patch` is all of them together, and `scripts/nest.py <copy> <line ids>` regenerates any subset in one pass (the line ids are in each family's section; `patches_hand/s1a_died.sh` and `patches_hand/eic_age.sh` make the two hand rewrites). `dep_hoh1.patch`, `dep_hoh2.patch` and `dep_hoh2lived.patch` are D5's three lines singly, kept as evidence, not for landing.

## 6. The check: why it passes today, the widening recommended, its time, and the day-one baseline

### 6.1 Why `interview-rules` reports 0 problems on main

- It walks 24 generated returns (12 federal, 12 New York; `GENERATED = 12`, `SEED = 11`, a constant with no option). 9 of the 12 federal ones and all 12 New York ones end refused, and a refused return is not classed for reach or early completion. **Three generated returns carry those rules.**
- Its minimal returns open each Bool or enum existence gate alone (8 returns) and never a collection roster: no dependent, Form 1095-A, Form 1099-R, HSA, business, vehicle or asset entry is walked that way.
- The generated sample is not stable: `derivedStream` in `engine/src/generate.ts` hashes the input ids with their values, so renaming one input redraws the education, early-distribution and Form 1095-A/8962 answers of every return (verified: with `eic.died_2025` renamed, every fast-check-drawn value of the 12 returns is identical and only those derived answers differ; the same rename under two different new names gives 6 problems and 27). An added input also moves the fast-check stream itself (BUG-0487 was caught that way).
- With the same seed and more returns the tool itself reports the findings: `INTERVIEW_RULES_RUNS=200` gives 23 problems on unmodified data.

### 6.2 Recommended widening

**(a) Select complete returns.** Take the federal generated returns from a pool (2,000, same seed) and keep the first K whose stated answers evaluate to a complete return; walk only those. Implemented in a scratch copy (`/tmp/f1095a/wcheck`; 13 lines in `engine/src/interview-rules.ts`; `/tmp/f1095a/patches/CHECK_select_complete_returns.patch`, for reference, not a finished change: it leaves the New York generated returns as they are, and all 12 of those end refused).

| Run (same machine, back to back, heavily loaded) | Federal generated returns | Complete returns classed | Wall | Problems on main's forms |
|---|---|---|---|---|
| default | 12 (3 complete) | 80 | 106 s | 0 |
| K = 60 | 60 complete | 137 | 126 s | 24 |
| K = 120 | 120 complete | 197 | 151 s | 55 |
| `INTERVIEW_RULES_RUNS=200` (today's option; measured earlier under similar load) | 200 (53 complete) | 130 | 485 s | 23 |

K = 60 costs about 20 s more than the default under this load (about a fifth of the step) and finds what 200 unselected returns find in a quarter of their time. In the full tier this step was recorded at 162 s (`docs/2026-11-11_check_all_timing.md` in the working tree, another session's note, not re-measured here), so the widening is of the order of half a minute there. Standalone and less loaded, the default took 53 s earlier in this work.

**(b) Minimal returns with one entry per collection.** The existing minimal return (every answer closed), with each roster it asks given one entry, alone, and rosters nested under that entry given one entry too. Prototype: `/tmp/f1095a/patches/CHECK_one_entry_minimal_returns_prototype.mjs` (a scratch script over the tool's exported `walk`, `minimalAnswers`, `bankOrder` and `readInputs`, not a change to the tool). 9 returns (`$dependent`, `$f1095a`, `$f8889`, `$interest`, `$oi8z`, `$retirement`, `$sales`, `$sc`, `$w2`), 19 s on one thread for the bank-order walk and 3 random orders each. On main's forms these 9 returns alone show `dependent.citizen`, `person.tin`, `dependent.multiple_support` (left reachable at completion), the 24 monthly Form 1095-A columns, `f8962.estimate_100`, `retirement.exception` and `scveh.owned`. They are deterministic and do not depend on the generator, its seed or the input ids. A larger variant that also gives each Bool, enum and amount answer of the entry another value, alone, is 315 returns and 979 s on one thread under load (about 3 s a return), and found one template that 5,000 generated returns did not (`person.sav_student`); it belongs in the release tier, if anywhere, and its returns have no income, so it never reaches the branches that need an applicable taxpayer.

**(c) Seed the derived stream independently of the ids.** Not implemented. `derivedStream(inputs, salt)` should take its seed from a number drawn by fast-check (one integer in the generator's record) rather than from `JSON.stringify` of the sorted input map. Then a rename should change no generated return (under the rename tested, every fast-check-drawn value was already identical; only the derived answers moved). An added Bool or amount input still moves the fast-check stream, because the generator draws one value per declared root input in declaration order; holding the sample still under additions would need the per-input draws keyed by id, a larger change. Adopting (c) changes the sample once.

**(d) A static list, as a report rather than a gate.** `/tmp/f1095a/scripts/static_scan.py` lists every federal line whose expression, or `sum_over` filter, is an `all`/`any` of two or more operands in which a later operand reads an input no earlier operand reads: **231 lines** on main (`/tmp/f1095a/out/static_candidates.json`; by document: sd 34, f8962 21, person 20, dependent 19, ira 12, f5695 11, f8889 9, household 9, retirement 9, sc 9, asset 8, eic 7, f2441 6, f8863 6, scveh 5, sales 4, and 22 documents with 1 to 3). The rewrites in this catalog cover 39 of them, and 6 further lines the rule does not count (`person.edu_llc_tin_refused` and five `retirement.is_e..` lines, where the later operand's input is also reachable through the earlier operand, yet is read while that operand waits on a different input), so 231 is not an upper bound either; 309 federal lines have a top-level `all`/`any` of two or more operands. Not every one of the 231 is a finding (where the later operand's input is asked earlier in bank order, or is read elsewhere anyway, no question is wasted), but each is a place where a question is reachable in some order before the answer that could hide it, and it is the population the sampled check draws from. This is why new templates kept appearing.

### 6.3 What the baseline would have to hold on day one

With widening (a) at K = 60 and (b) with the nine one-entry returns, on main's forms as they are, `tools/interview_rules_baseline.json` would have to hold:

- `early_completion` (7 templates): `dependent.canada_mexico`, `dependent.disabled`, `dependent.gross_income`, `dependent.kidnapped`, `dependent.multiple_support`, `dependent.supported`, `household.married`. Five of them (`dependent.kidnapped`, `dependent.multiple_support`, `dependent.canada_mexico`, `dependent.disabled`, `dependent.gross_income`) are among the six whose open question can refuse the return, so a baseline that holds them holds a known serious finding.
- `order_dependent_reach` (24 templates): `dependent.absence_no_return`, `dependent.edu_tin_issued`, `dependent.months`, `dependent.parent_home_paid`, `dependent.supported`, `f1095a.in_b_<month> (12 templates)`, `f8889.employer_in_box1`, `f8962.estimate_100`, `person.died_before_65`, `person.tin`, `retirement.exception`, `scveh.owned`, `ssb.lived_apart`.
- `walked_unused` (21 templates, the three of BUG-0487 included): `asset.not179`, `dependent.citizen`, `dependent.gross_income`, `dependent.lawful`, `dependent.supported`, `f1095a.c_total`, `f1095a.in_a_<month> (12 templates)`, `f8962.alien_below`, `f8962.estimate_100`, `person.tin`.

At K = 120 the tool reports 10 early-completion, 12 out-of-order and 33 new asked-unread templates (55 problems), so the lists grow with the sample and would grow again with each new input or rename until (c) is in. Holds are by template with a reason, and a held template no longer seen fails until it is removed, so a baseline this size would churn with every change to the sample.

With every rewrite of this catalog applied (`patches/ALL_combined.patch`), the same widened check (K = 60, 97 s) reports 4 problems: the three BUG-0487 holds to remove, and one early completion of class L1 (`dependent.absence_no_return`); the nine one-entry returns show nothing. The day-one baseline would then be the L1 templates only: `dependent.absence_no_return`, and, as other samples draw them, `person.born_before_2001`, `person.born_after_1960` and `person.work_ssn`.

**Recommendation.** Land D1 first, on its own if need be, because the baseline should not hold a refusal-capable finding. Then widen with (a) and (b) together with whichever families the owner accepts, holding the rest by name; decide the L1 class once (hold or exempt); take (c) with the next change to the generator. Keep (d) as a report: it is the honest measure of how much of this shape remains (231 lines), and each rewrite round should be checked against it for siblings, since three of the lines in this catalog are siblings that earlier rounds or this one missed (`f5695.ac_no_qmid`, `person.edu_llc_tin_refused`, `f8889.split`).

## 7. What was surprising, and the limits of this catalog

1. **"Complete" with a refusing question still open.** The rule is in the spec (4.7.2: a deciding conjunct of `all`/`any` decides even past an unknown conjunct that is waiting on a refusal gate), but its consequence in `dependent.odc_person` was not recorded anywhere I found: answer the SSN, citizenship or all-have-TINs question No before the dependent test is finished, and the return is complete without the multiple-support or kidnapping question, either of which would have refused it. In bank order those questions come first, so the bank-order interview is not affected; an interface that let a filer answer in another order, or a correction that reopens the earlier answers, could reach it. Witness: generated return seed 20, index 47, `dependent[dep_b]`: complete with `multiple_support` open; Yes refuses at `dependent.multiple_support`; the same return with that answer Yes, walked in bank order, is refused after 144 questions.
2. **The sample never ran dry.** Template 70 appeared at return 4,762 of 5,000, after 3,000 returns with nothing new, and two more causes were found only by other routes. A static count of the shape gives 231 lines (309 by a looser rule); this catalog rewrites 46. The earlier rounds' "the baseline is empty" was true of twelve returns.
3. **Fixing a line moves the finding to its reader.** With `f8889.married_family` nested, `household.married` is still left open through `f8889.split` := `all(f8889.married_family = true, household.hsa_both = true)`. With `dependent.edu_llc_tin_refused` nested, the same expression on `person.edu_llc_tin_refused` showed for the first time. With the head-of-household lines nested, `dependent.absence_no_return` moved from "out of order" to "left reachable at completion" through a count's lower bound. A round of rewrites has to be re-swept, not just checked against the list it started from.
4. **A sibling was missed in BUG-0471.** `f5695.wh_no_qmid`, `furnace_no_qmid` and `hp_no_qmid` were rewritten then; `f5695.ac_no_qmid`, `doors_no_qmid`, `windows_no_qmid` and `enabling_no_qmid` have the same expression shape and were left as `all`.
5. **One line of a family can make things worse alone.** `dependent.hoh_test2_lived` as a chain, without `dependent.hoh_test2`, asks `dependent.absence_no_return` on three returns where main does not.
6. **Pins move without being named.** A rewrite on Form 5695 un-pins a New York mutation argument, because the digest includes each premise line's readers and a new helper reads `f1040.status`.
7. **The same rename under two names gave 6 problems and 27.** The sample depends on the spelling of the ids, not only on their set.
8. **`dependent.citizen` is asked and unread on 208 of 1,147 complete generated returns** (18%), the largest single item, and it comes from one five-operand line.
9. **The handoff says the baseline is empty (0/0/0); the file holds three `walked_unused` templates** (BUG-0487). P2 removes them.
10. **Bank order within a shared order number is alphabetical by input key.** All Form 1095-A questions have `order: 2`, so the months are asked April, August, December, February, and so on. Seen in every walk; not a finding of the check, and not pursued here.

**Limits.**

- One witness return was traced per template and class. A template can have more than one cause line; the table's test columns (which family's rewrite removed it, and what is left with all of them) are the check on the attribution, and after every rewrite only the L1 class is left in 2,000 returns.
- The sweeps are federal. New York's generated returns all end refused and are not classed; New York forms were not scanned statically.
- The rewrites are mechanical. Helper ids and labels (`dependent.odc_person_from2`, "…: conditions 2 to 5") are placeholders; each helper carries the rewritten line's citation unchanged, which a transcription review may want narrowed. No wording, question or interview-order entry changes.
- `mutate`, `compare` (Lean), the engine differential, `check-all` and every review were not run. The Lean evaluator reads the same data and the rewrites use only `choose`, `test` and `param`, which it has (the design note says so; not checked by running `compare`).
- Main moved from `2e13fd84` to `2be2a2cf` during this work (Form 8863 Part III lines in `dependent.yaml` and `person.yaml`). Every patch passes `git apply --check` on the new tip; none was rebuilt or retested there.
- Times were taken on a machine at load 40 to 100.

## 8. Verified by running, read, or inferred

**Run and observed (scratch copies of main at `2e13fd84`):**

- The 5,000-return sweep on main, its counts per template and class, and the first appearance of each template.
- A traced witness for every template and class in the table (65 traces), and the expression of each cause line as built in `canonical/2025/`.
- The probe of 243 early-complete states on main, 46 with every rewrite, 72 with D1 alone: each open question given each answer.
- For each of the 21 families alone: the build, both fixture suites, the witness returns in bank order and five random orders, values of 1,500 generated returns and all fixture inputs against main, the pin digests, the rendered files. For the three D5 lines singly, the same.
- All rewrites together: build, both fixture suites, 3,000 generated returns and all fixture inputs against main, `interview-rules` at its defaults, a 2,000-return sweep compared return by return with main, the one-entry returns, the widened check at K = 60.
- The widened check on main's forms at K = 60 and K = 120, back to back with the default; `INTERVIEW_RULES_RUNS=200`; the nine one-entry returns and their 315-return variant; the static scan.
- `interview-length` on main and with the rewrites (0 problems each; its report written in the scratch copies: over its 162 complete returns, 10,738 questions on main (the committed report, which the tool reproduces on main but for a trailing blank line) and 10,725 with the rewrites, 11 returns shorter and none longer; 11 complete returns were asked more than the inputs their return reads, none is after; of the 92 refused returns 4 are shorter and 2 longer, the generated returns 1 and 11).
- `git apply --check` of every patch on `2e13fd84` and on `2be2a2cf`.

**Read, not run:** the spec's sections 4.7.2 to 4.7.5; BUG-0466, BUG-0471, BUG-0487, BUG-0492 and the formal-gates design note for the conventions and the accepted trade-off; `tools/transcription/subjects.py` for what makes a review stale; `ui/app.ts` for the interface asking the first pending question; `interview/2025/gate_frequencies.yaml` for the shares; `engine/src/mutate.ts` for how pins are digested.

**Inferred, not checked:**

- Which reviews fall due and what they cost (review state is not in the scratch copies).
- That the pin count found by pattern in `mutate.ts` (52 distinct premise lists, all holding on main's data) is every pin; pins built in loops share a list and are counted once.
- That no mutant survives or dies differently (not run), and that the Lean evaluator agrees on the rewritten lines.
- The share of filers who meet each case: the frequency file's share is for the situation (dependents, Marketplace coverage), not for the branch inside it.
- That `dependent.absence_no_return` can be left reachable through the lower bound on main as well; it was seen only with the rewrites.
- Full-tier time of the widened step: from the 162 s recorded in another session's timing note plus the 20 s measured here.

## Appendix: files

| Path under `/tmp/f1095a/` | What |
|---|---|
| `catalog.md` | this document |
| `patches/<family>.patch` | one tested rewrite per family, against main at `2e13fd84` (also applies at `2be2a2cf`): `dep_odc` (D1), `dep_qr` (D2), `dep_incx` (D3), `dep_qrrel` (D4), `dep_hoh` (D5; `dep_hoh1`, `dep_hoh2`, `dep_hoh2lived` are its lines singly), `dep_edutin` (D6), `f8962_bzero` (P1), `f8962_applicable` (P2), `f5695` (E1), `f8889` (H1), `scveh` (V1), `retirement` (R1), `ssb` (S1), `asset` (A1), `s1a_died` (X1), `carloan` (C1), `eic_step3` (X2), `f2441` (X3), `sa` (X4), `eic_age` (X5), `sav` (X6) |
| `patches/ALL_combined.patch` | every family together (H1 without `f8889.split`), as tested in `all2/` |
| `patches/CHECK_select_complete_returns.patch`, `patches/CHECK_one_entry_minimal_returns_prototype.mjs` | the two check widenings, scratch quality |
| `patches_hand/s1a_died.sh`, `patches_hand/eic_age.sh` | the two hand rewrites as scripts |
| `scripts/nest.py` | the rewrite tool (`python3 -I nest.py <copy> <line id> ...`; `<id>!` rewrites the top level only) |
| `scripts/seeds.mjs`, `sweep2.sh`, `trace.mjs`, `probe_all.mjs`, `measure.mjs`, `differential.mjs`, `pins.mjs`, `askdiff.mjs`, `collections.mjs`, `static_scan.py`, `fam.sh`, `all2.sh` | the sweep, tracer, probe, per-family pipeline and combined run |
| `out/base_sweep/`, `out/all2_sweep/` | sweep rows, one JSON line per return |
| `out/fam_<family>/` | each family's build, fixture, measure, differential, pin and render outputs |
| `out/causes.json`, `out/famsummary.json`, `out/all2_vs_base.json`, `out/day_one.json`, `out/static_candidates.json`, `out/probe_early_base.txt`, `out/probe_early_all.txt` | the data behind the tables |
| `base/`, `all2/`, `wcheck/`, `wcheck_all/` | main built; main with every rewrite; main with the widened check; both |
| `draft_bug.md` | the two draft inventory entries from the first report (BUG-XXXX for `f8962.b_zero`, BUG-YYYY for the check) |
