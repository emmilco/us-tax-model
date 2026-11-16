# Decision memos for the owner: six open questions (tax year 2025, us and ny)

Lane plan-decisions, claude-opus-5-5, judgment, 2026-11-15. Read only; base: the xint worktree
(`.claude/worktrees/xint`, uncommitted coverage-expansion candidate). Paths below are relative to that worktree.
Labels: **[V]** checked against the file named (path:line); **[I]** inferred or hand-figured, not run;
**[T]** relayed from a project note (testimony), not re-checked. No dollar figure below was produced by the engine:
all worked examples are hand arithmetic [I].

## Summary (one line per question)

| # | Question | Project now | Recommendation | Reversal cost |
|---|---|---|---|---|
| 1 | D3: always take the "no Form 1116" election when available | Elects automatically (`forms/2025/ftc.yaml:157-181`); only a claimed carryover blocks it (D7) | **Confirm**, and fix BUG-0774 with it. The only filers it can hurt (foreign tax above regular tax, at most $300/$600) mostly land on a Form 1116 path the tool refuses anyway (high-taxed income) | Low: re-add one question, 470 fixture facts |
| 1b | BUG-0774: Form 2555 filer denied the election | Low bug, open | **Fix** as the entry proposes (narrower 4563/Puerto Rico input) | Low |
| 2 | NY item C on a joint return where only the spouse is claimable | Item C = Yes (federal "you or your spouse" Yes carries over) (`forms/ny/2025/ny_it201.yaml:437-443`) | **Refuse narrowly** where the two readings change the return (joint, federal Yes, NYC resident or FAGI ≤ $18,000), as with line 25 (B1); or ask the owner's NY knowledge first | Low: one gate |
| 3 | Farm depreciation parent model (Schedule F) | Not built; `asset`/`scveh` have one parent, `sc` | **Defer** until Schedule F is scheduled (the scout itself ranks it after Schedule E and Form 4797); when it is, take option (i) multi-parent collections, or (iv) duplicate-plus-twin-check if the owner wants to repeat the T-274 choice | Decision is free now; costly once a farm form exists |
| 4 | K-1 decisions D-K1..D-K16 | Settled by the coordinator as the scout recommends (D-K1 by the owner) | **Confirm all**, with one watch item: D-K2 (basis asked, not computed) can overstate a loss on a wrong "No" | Each is one group of lines in `k1p.yaml`/`k1s.yaml` |
| 5 | amb.2025.k1p_prior_with_activity | Held-back passive loss asked only when box 1, 2 or 3 has an amount | **Reverse**: ask every partnership K-1, as a tick (as `k1s.prior_any` already does for every S corporation K-1) | Low question cost; engine support for a blank-box activity unverified |
| 6 | T-326: D1..D14 of the TY2026 plan | Taken on the owner's behalf | **Confirm all 14**; D12 (2025 tree takes defect fixes only after 2026 adoption) is the one with real consequence and is sound | Each reversible by a later plan edit |

Background found for all six. Two items needed more than the brief named: question 3's only record is
`docs/provisional/lanes/scout-tail.md` section B (no task row, no DECISIONS entry); question 5 has a sibling in
BUG_INVENTORY.md:10428-10429 (item G residuals), also open.

---

## 1. D3: always elect to claim the foreign tax credit without Form 1116

### The question
When a filer meets the conditions of the election (all foreign income passive, reported on payee statements,
foreign tax at most $300, or $600 joint), the project now elects automatically and no longer asks. Should it keep
doing so? The cost: when foreign tax is more than the regular tax, the election credit is capped at the regular tax
and the excess is lost for good; on Form 1116 the excess would carry to other years.

### Options
- **A (current).** Elect whenever the conditions are met and no carryover is claimed into 2025.
- **B.** Elect automatically, except when foreign tax exceeds regular tax: then ask "keep the unused foreign tax for
  later years (Form 1116)?" or route to Form 1116 outright.
- **C.** Restore the question for everyone (`ftc.elect`).

### The law
- i1116 (2025) pp. 1–2, Election To Claim the Foreign Tax Credit Without Filing Form 1116: "By making this election,
  the foreign tax credit limitation (lines 15 through 23 of the form) won't apply to you." Conditions: passive
  category income only; "All the income and any foreign taxes paid on it were reported to you on a qualified payee
  statement"; "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)."
  Consequence: "You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to
  which the election applies (but carryovers to and from other years are unaffected)."
  [V: sources/2025/i1116.txt:35-70]
- i1116 p. 19: "You can carry back 1 year and then forward 10 years any foreign tax you paid or accrued ...
  (reduced as described under Line 12, later)" [V: sources/2025/i1116.txt:1291-1295].
- i1040gi (2025) p. 115, Schedule 3 line 1, condition 4: "You aren't filing Form 4563 or excluding income from
  sources within Puerto Rico." [V: sources/2025/i1040gi.txt:8241-8245]

Why the election is never worse this year: the election credit is the smaller of the foreign tax and the regular
tax; the Form 1116 credit is at most regular tax × (foreign taxable income / taxable income), so never more
[I: arithmetic of i1116 lines 19–21; the project's own label says so, `forms/2025/ftc.yaml:160-162` V]. The only
case where Form 1116 can win over time is foreign tax > regular tax, where Form 1116 carries the difference.

### Effect on real filers (hand-figured [I])
**Example 1, the typical case the trade-off touches.** Single, 30, wages $16,000, international bond fund
dividends $1,000 (ordinary), foreign tax $200 (1099-DIV box 7).
- AGI $17,000; standard deduction $15,750 [V: params/2025.yaml:1804]; taxable income $1,250; regular tax ≈ $126.
- Option A (election): credit $126, tax $0; $74 lost forever.
- Form 1116 path: line 7 net foreign income ≈ $1,000 − 15,750 × 1,000/17,000 = $74; limit ≈ $126 × 74/1,250 ≈ $7;
  carryover ≈ $193. But $200 tax on $74 net income is far over 37%, so the column is high-taxed: the project
  **refuses** this return on the Form 1116 path (`f1116.high_taxed`, `forms/2025/f1116.yaml:1233` region; refusal
  list V at f1116.yaml:1115-1240). Reversing D3 here turns a completed return into a refusal.

**Example 2, where Form 1116 could pay more over time.** Joint, wages $35,000, foreign qualified dividends $8,000
from an international stock fund, foreign tax $560.
- Taxable income $43,000 − $31,500 = $11,500; ordinary part $3,500 at 10% = $350; the $8,000 at 0%.
- Option A: credit $350, tax $0; $210 lost.
- Form 1116 (adjustment exception applies: foreign QD under $20,000, i1116 p. 9 [V: i1116.txt:580-592]):
  net foreign income ≈ 8,000 − 31,500 × 8/43 ≈ $2,140 (26%, not high-taxed); limit ≈ $350 × 2,140/11,500 ≈ $65;
  credit $65; ≈ $495 carried (first back to 2024, where the project refuses if 2024 had room, `f1116sb.carryback`).
- Net: A gives $350 now; Form 1116 gives $65 now plus up to $495 later **only if** later years have unused passive
  limit. For a fund investor whose dividends move into the 15% bracket, that headroom is plausible within a few
  years. Maximum loss from A in this example: about $210, spread over future years.

How many filers: foreign tax above regular tax with foreign tax ≤ $300/$600 means very low regular tax; the scout
called it "rare" [T: docs/provisional/lanes/scout-form-1116.md:78-81]. Not measured.

### What the project does now
- `ftc.elect` is a derived line, true unless `ftc.carryover_if_asked` [V: forms/2025/ftc.yaml:157-181].
- Recorded: DECISIONS.md X1-F1116 D3 [V: docs/provisional/DECISIONS.md:293]; second pass added D7 (a carryover in
  sends the filer to Form 1116) [V: DECISIONS.md:305; ambiguities/2025.yaml:2564-2581, status "for the owner"].
- Form 1116 path now prepares Schedule B (Form 1116) for a carryover generated [V: DECISIONS.md:302].

### Recommendation
**Confirm A.** In the rare case it matters, the alternative path usually refuses (Example 1); where it does not
(Example 2), the extra value is contingent and deferred. If the owner prefers to leave the choice to the filer,
option B costs one question asked only when `ftc.taxes_if_asked > ftc.regular_tax` and the election is available.
**Reversal cost:** low. B is one gated question plus a guard on `ftc.elect`; C re-adds the question, its default
and up to 470 fixture facts removed by x1-f1116 [T: docs/provisional/lanes/x1-f1116.md:20-26].

### 1b. BUG-0774 (was bug_pending/xint-ftc2555-01): Form 2555 filer denied the election
[V: /tmp/xint/assign.out:10; BUG_INVENTORY.md:9693-9702]
- **Question.** `ftc.needs1116` reads `sa.excluded_income`, which bundles Form 2555 with Form 4563 and Puerto Rico.
  The election's condition 4 names only Form 4563 and Puerto Rico; Form 2555 matters only through the line 12
  reduction ("Taxes on income excluded on Form 2555. Reduce taxes paid or accrued by the taxes allocable to any
  foreign earned income excluded on Form 2555" [V: i1116.txt:1289-1297, p. 19]).
- **Project now:** every Form 2555 filer with foreign tax goes to Form 1116 [V: forms/2025/ftc.yaml:371-374].
- **Effect:** a Form 2555 filer whose only foreign tax is on fund dividends (none on the excluded wages) gets the
  Form 1116 credit (≤ election credit) or a Form 1116 refusal, instead of the election. Example: $150 foreign tax on
  $3,000 of fund dividends, regular tax $4,000: election $150; Form 1116 limit ≈ 4,000 × (3,000 − share of
  deductions)/taxable income, which can fall below $150 when the excluded wages are not in the ratio [I]. Low.
- **Recommendation:** fix with D3's confirmation, as the entry proposes (a narrower Form 4563/Puerto Rico input; the
  election path asks the line 12 reduction). Reversal: trivial.
- **Unchecked, worth a look:** whether a filer with a real Form 2555 exclusion reaches a completed return at all
  (the Foreign Earned Income Tax Worksheet is named only in `forms/2025/qdcg.yaml:30,214` labels; I found refusals
  on Schedule A line 6, s8812, eic, f2441, f8863, f8880, sli, s1a, f8962 but not on the Form 1040 tax line). If not,
  BUG-0774 has almost no population [I].

---

## 2. New York item C on a joint return where only the spouse can be claimed

### The question
IT-201 item C asks "Can you be claimed as a dependent on another taxpayer's federal return?" with one box. On a joint
return where the spouse, not the taxpayer, could be claimed as someone's dependent, is item C Yes or No?

### Options
- **A (current).** Yes: any federal "you or your spouse" Yes makes item C Yes.
- **B.** No unless the taxpayer (or both spouses) can be claimed.
- **C.** Refuse where A and B give different returns (precedent: line 25, decision B1, "the project refuses both
  readings" [V: reviews/2025/transcription/adjudication/ny_it201.md:92]).

### The law
- IT-201-I (2025) p. 5, Item C: "If you can be claimed as a dependent on another taxpayer's federal return, you must
  mark an X in the Yes box. You must mark the Yes box even if the other taxpayer did not claim you as a dependent."
  [V: sources/ny/2025/ny_it201i.txt:292-299]. Silent on spouses.
- What item C changes on a joint return: line 40 NYS household credit ("If you marked the Yes box at item C ... you
  do not qualify", p. 12) [V: ny_it201i.txt:737]; line 48 NYC household credit [V: :848]; line 69 NYC school tax
  credit, fixed $125 joint [V: :1300-1312]; line 69a rate reduction [V: :1357]; the IT-214 first test (project
  `ny_it201.low_income`) [V: forms/ny/2025/ny_it201.yaml:2158-2162]. The dependent standard deduction applies to
  single filers only [V: ny_it201.yaml:992].
- Federal joint-return test: "You generally can't claim a married person as a dependent if that person files a joint
  return. Exception ... if that person and that person's spouse file the joint return only to claim a refund of income
  tax withheld or estimated tax paid." [V: sources/2025/p501.txt:897-912, p. 11]. So the case arises only on a
  refund-only joint return: no federal tax, and usually no NY tax.

### Effect on real filers (hand-figured [I])
Joint, full-year NYC residents. Spouse 1 wages $14,000; spouse 2, a 20-year-old student with $2,000 wages whom a
parent could claim; refund-only return. FAGI $16,000; NY standard deduction $16,050 → NY tax $0.
- Household credits (lines 40, 48): nonrefundable, tax is $0 → $0 under either reading.
- Line 69 NYC school tax credit (refundable): **A: $0; B: $125.** Line 69a: NYC taxable income $0 → $0 either way.
- IT-214 (refundable real property credit): under B the project asks the rent question (FAGI ≤ $18,000), whose Yes
  refuses [T: docs/provisional/lanes/ny.md:87]; under A it is never asked.
So the stake is about $125 of refund per affected couple, never an overstated refund under A. Population: very
small (refund-only joint returns where a parent could claim one spouse, in NY) [I].

### What the project does now
`ny_it201.item_c` = federal `sa.dependent` Yes, or the NY question after a federal No
[V: forms/ny/2025/ny_it201.yaml:431-443]; `sa.dependent` asks about "you or your spouse" together
[V: forms/2025/sa.yaml:187-193]; no per-spouse input exists. Registered as `amb.ny.2025.item_c`, but that entry
covers only the "not required to file" difference (decision B8), not the spouse facet
[V: ambiguities/ny/2025.yaml:70-81]. The xadj render adjudication flagged the spouse facet and noted that the earlier
premise "a federal Yes refuses" no longer holds now that dependent filers are computed
[V: reviews/2025/transcription/adjudication/ny_it201.md:94].

### Recommendation
**C, narrowly:** refuse when the return is joint, `sa.dependent` is Yes, and the readings differ in amount (NYC
resident, or FAGI ≤ $18,000 for IT-214); add the spouse facet to `amb.ny.2025.item_c`. A is defensible as the
conservative reading if the owner prefers coverage; B has no textual support I found. The owner may know DTF practice
here (a call or prior filing experience would settle it better than inference). **Reversal cost:** low (one gate; one
ambiguity entry; at most a few fixtures).

---

## 3. Farm depreciation parent model (Schedule F)

### The question
Schedule F is designed but not built [V: no forms/2025/sf.yaml]. Farm depreciation (line 14) and car and truck
expenses (line 10) need the existing depreciation and vehicle models, whose collections hang under Schedule C only
(`asset` and `scveh`: `collection.parent: sc`; the schema allows one parent) [T: scout-tail.md:323-327; one parent
confirmed in docs/2026-11-11_form8863_twin_study.md:165-166 T]. How should farms reach them?

### Options (scout-tail.md B.3 and B.8 item 2 [V: :323-328, :384-389], plus one I add)
- **(i)** Engine and schema allow a list of parents (spec 4.4 change, both evaluators including Lean).
- **(ii)** A farm is an `sc` entry of kind `farm`: no engine change, but every Schedule C line gains a kind guard.
- **(iii)** Refuse farm depreciation and actual car expenses in v1 ("kills most of the gain" [T]).
- **(iv)** (added) Copy the models under a farm parent and keep them in step with the twin check, as the owner chose
  for Form 8863 Part III (T-274, closed 2026-11-14: "both copies stay, kept in step by the twin check")
  [V: TASKS-DONE.md:251]. Schedule E took a narrow version of this (`rprop`, `rf4562`, 235 + 71 lines)
  [V: wc; scout-schedule-e.md:138-146]. Here the copy would be large: `asset.yaml` 2,227 lines, `scveh.yaml` 3,765 [V].

### The law
i4562 (2025) p. 11: farm 15- and 20-year property uses 150% declining balance; "For 3-, 5-, 7-, and 10-year property
used in a farming business and placed in service after 2017, see 3-, 5-, 7-, or 10-year property above" (200%)
[V: sources/2025/i4562.txt:803-814]; new farm machinery placed in service after 2017 is 5-year property
[V: i4562.txt:692-700]. Farm property is in the project's asset model already as a class [V: asset.yaml:77].
The law does not bear on the choice; it is architecture. It bears on (iii): most farms depreciate machinery.

### Effect on real filers (hand-figured [I])
Scout fixture F1 (single grain farmer, line 34 $76,000) [T: scout-tail.md:353] plus a $60,000 tractor bought and
placed in service in 2025: under (i), (ii) or (iv) line 14 can take it (100% special allowance if acquired after
January 19, 2025, already in the asset model per the 2026 change notes [T]); line 34 falls toward $16,000 and SE tax
by about $8,500 [I: 60,000 × 0.9235 × 0.153]. Under (iii) the return is refused. Schedule F's whole gain is
1.1% of returns, +0.5 points alone, +1.1 in ladder order [T: scout-tail.md:18].

### What the project does now
Nothing built; `scope.farm` refuses every farm [T: l9.md:63]. No task row and no DECISIONS entry exist for this
decision [V: grep of TASKS.md and DECISIONS.md for "farm"]. The scout's own order is "after Schedule E and the Form
4797 part of other Schedule 1" [V: scout-tail.md:18, :385].

### Recommendation
**Defer the choice until Schedule F is scheduled**, and record that deferral; nothing depends on it today. When it is
scheduled, prefer **(i)**: it has at least two customers (Schedule C and Schedule F; arguably Schedule E's rental
property too), unlike Form 8863's one-customer case that justified rejecting unification in T-274. Choose (iv) only if
the owner wants to avoid touching both evaluators again. Reject (ii) (guards on every Schedule C line, printed numbers
diverge) and (iii). **Reversal cost:** zero now; after a farm form ships, moving from (iv) or (ii) to (i) means id
changes and fixture rewrites of the T-274 size.

---

## 4. The K-1 decisions D-K1 to D-K16

### The question
The K-1 scout listed sixteen decisions [V: docs/provisional/lanes/scout-k1.md:432-452]. The owner decided D-K1; the
coordinator settled the rest "as the scout recommends" under delegation [V: docs/provisional/DECISIONS.md:129-150,
:153-167]. Confirm or reverse.

### The law (the core)
i1065sk1 (2025) p. 3: "These limitations and the order in which you must apply them are as follows: the basis
limitations, the at-risk limitations, the passive activity limitations, and the excess business loss limitations."
[V: sources/2025/i1065sk1.txt:158-164]. Limited partners: "you must meet item 1, 5, or 6 above to qualify as having
materially participated" (p. 9) [T: amb.2025.k1p_material_tests, ambiguities/2025.yaml:1961-1975].

### Each decision, as settled, with a recommendation
| Id | As settled | Rec. | Note |
|---|---|---|---|
| D-K1 | Form 7203 encoded (Parts I, III 35–38); debt basis, distributions above basis, carryovers refused (owner) | confirm | Owner's own; gates most S corporation coverage |
| D-K2 | Partnership basis asked ("does the loss exceed your basis?"), Yes refuses | confirm, watch | **Risk:** a wrong "No" gives an unlimited loss. Example: box 1 loss $20,000, basis $5,000, filer answers No: $15,000 excess deducted; at 22% tax understated ≈ $3,300 [I]. The alternative (Partner's Basis Worksheet) needs prior-year basis the filer rarely has |
| D-K3 | At-risk asked on any loss; Form 6198 cases refuse | confirm | |
| D-K4 | Publicly traded partnerships refused | confirm | Common among retail investors (MLPs); income-only PTPs are a later expansion |
| D-K5 | Material participation tests 1, 2/3, 5 asked; 4, 6, 7 refuse | confirm | Sibling lows open: BUG_INVENTORY.md:10428 (item G decides tests) |
| D-K6 | Box allow-list (1, 2, 3, 4a, 5, 6a/b, 8, 9a–c, 14 A, 15 O, 18 A, 19 A, 20 A/B/Z; others refuse) | confirm | [V: DECISIONS.md:138-140] |
| D-K7 | QBI with a partly suspended loss by prorate; prior-year release refuses; S corp basis part refuses | confirm | |
| D-K8 | Positive 14 A joins the SE attribution whole for QBI | confirm | |
| D-K9 | Estates and trusts income only; 9, 10, 11 and losses refuse | confirm | Final-year estate 11 A deductions are the commonest loss; a later add |
| D-K10 | Box 4b (guaranteed payments for capital) refused | confirm | |
| D-K11 | Placement at order 264 / 266 | confirm | |
| D-K12 | Coverage rows change ends (N9) | confirm | |
| D-K13 | Portfolio-only K-1 puts no row on Schedule E | confirm | `amb.2025.k1p_portfolio_no_sche` |
| D-K14 | Foreign partnerships, K-3, box 21 refused | confirm | Interacts with question 1: K-1 foreign tax stays out of the election |
| D-K15 | Timing with x1-sche's round | confirm (moot) | Already executed |
| D-K16 | Suffix lines per activity, no def | confirm | Refactor later if the def mechanism lands |

**Recommendation:** confirm all. The only one with a dollar risk on completed returns is D-K2; mitigate by help text
naming the two common reasons basis runs short (distributions, earlier losses), not by computation now.
**Reversal cost:** each decision is one refusal entry or question with its gate in `forms/2025/k1p.yaml` or
`k1s.yaml` and its bank entry [V: DECISIONS.md:150-151].

---

## 5. amb.2025.k1p_prior_with_activity

### The question
Should the "was a loss from this partnership held back on an earlier return (passive rules)?" question be asked of
every partnership K-1, or only when box 1, 2 or 3 shows an amount this year?

### Options
- **A (current).** Only when box 1, 2 or 3 has an amount.
- **B.** Every partnership K-1 (as a tick in the existing group).

### The law
- i8582 (2025) p. 2: "Prior-year unallowed losses. These are the losses from an activity that were disallowed under
  the PAL limitations in a prior year and carried forward to the tax year under section 469(b)."
  [V: sources/2025/i8582.txt:127-130]
- i8582 p. 10, Part IV column (c): "Enter the unallowed losses for the prior years for each activity. You find these
  amounts in Part VII, column (c), of your 2024 Form 8582." [V: i8582.txt:649-657]
A prior-year unallowed loss is a 2025 passive deduction of the activity whether or not the activity has income or loss
in 2025; it offsets passive income from other activities.

### Effect on real filers (hand-figured [I])
Single, W-2 $90,000. K-1 A (rental LP): box 2 income $8,000, passive. K-1 B (another LP): boxes 1–3 blank this year
(box 5 interest $40); the 2024 Form 8582 shows $5,000 unallowed for B's activity.
- Law: B's $5,000 offsets A's $8,000; net passive income $3,000. Taxable income $77,290.
- Project (A): B's question is not asked; taxable income $82,290; **tax overstated ≈ $1,100** (22% bracket).
The reading never overstates a deduction; it understates one [V: the entry says so, ambiguities/2025.yaml:1954-1960].

### What the project does now
`k1p.prior_any_if_activity` gates the question on `k1p.has_activity` (box 1, 2 or 3)
[V: forms/2025/k1p.yaml:1468-1520]. The S corporation side asks `k1s.prior_any` of every S corporation K-1, as a
tick in group `k1s_prior` [V: forms/2025/k1s.yaml:1363-1372; interview/2025/questions.yaml:6836-6840]. Status of the
entry: "Coordinator's decision ... open to the owner's review (a reading that understates a deduction)"
[V: ambiguities/2025.yaml:1959-1960]; the screen review listed it as open residual -12
[V: reviews/2025/screens/adjudication/xrel-k1p.md:26-28].

### Recommendation
**Reverse to B**, matching `k1s`: one more tick on the screen every partnership K-1 already sees; the question is
answered from the 2024 Form 8582, which the help names. **Reversal cost:** low for the question. **Unverified:** whether
`k1p`'s per-box prior-loss lines (`k1p.prior_b1_any` etc.) and the Form 8582 rows carry a loss for an activity whose
box is blank this year; if they key on `has_b1`/`has_b2`/`has_b3`, B also needs those rows opened, or a narrow refusal
("held-back loss on a K-1 with boxes 1–3 blank") as an interim step that at least stops the silent overstatement.

---

## 6. T-326: TY2026 preparation decisions taken on the owner's behalf

Source: docs/provisional/lanes/ty26-plan.md section 2 [V: :37-54]; task row TASKS.md:95 [V].

| # | One line | Rec. |
|---|---|---|
| D1 | Federal 2026 may be adopted before NY 2026: per-jurisdiction adoption list; NY checks skipped visibly | Confirm: NY publishes after the IRS |
| D2 | No draft `forms/2026` on main; preparation stays as checked operations until gating finals exist | Confirm |
| D3 | Shared forms' operations split into `changes/2026/<form>.<topic>.yaml`, one lane per file | Confirm (already in use: f1040.x1-digital.yaml etc. in git status) |
| D4 | Ambiguity entries become `add_ambiguity`/`set_ambiguity` operations | Confirm |
| D5 | Each new question carries its default and reason; adoption writes defaults and copies contract banks | Confirm |
| D6 | `placed_year` and similar enums extend by one year at adoption | Confirm |
| D7 | The 14 `age.*` parameters move by offset, marked derived | Confirm |
| D8 | Tax Computation Worksheet rows read from Rev. Proc. 2025-32, re-verified when i1040gi posts | Confirm |
| D9 | Draft-to-final flip per document as each final posts | Confirm |
| D10 | No paid reviews on drafts; one line-scoped round on finals | Confirm (matches the 2026-11-03 cost rule) |
| D11 | Wording-only changes in one Sonnet lane, split files | Confirm |
| D12 | After 2026 adoption the 2025 tree takes defect fixes only; a fix lands in 2026 and is ported only if it changes a 2025 return | **Confirm**; the substantive one. Note it governs BUG-0655 (2025 home storage test) |
| D13 | A Sonnet lane re-checks irs.gov for drafts and finals, then weekly | Confirm |
| D14 | Operation lanes claim forms they alone touch; shared forms unclaimed, 2025 lanes rerun the check and mend | Confirm |

The rest of T-326 (outside D1–D14, read only briefly [T]): Trump accounts as a refused answer of
`retirement.account` and exception 24 kept refused (ty26-o2.md:34-45: confirm); the reworded dependent care plan
maximum question (ty26-o4.md:40-47: "owner review recommended", read the prompt); the 40% bonus election dropped for
2026 (ty26-o9.md:41: confirm, P.L. 119-21 phase-down); BUG-0654 (oil and gas working interest counted as active for
the 2026 minimum QBI deduction: needs a question or a recorded argument); the second reading of
`amb.2026.gift_floor_base`, written from model knowledge (ty26-r3.md: verify against a source before confirming);
`year_carry.py` normalizing a document's own tax year without evidence (ty26-r2.md:125-130: confirm, mechanical).

---

## Provenance
Inspected: the files and line ranges cited [V] above, read in the xint worktree and `/tmp/xint/assign.out`; source
quotes read in `sources/2025/*.txt` and `sources/ny/2025/ny_it201i.txt`; page numbers computed from form-feed counts
in the extracted text. Inferred (unverified): every worked-example dollar figure (hand arithmetic, not engine runs;
Example 2 of question 1 approximates the Form 1116 line 3 apportionment), population sizes, whether Form 2555 filers
with an exclusion complete returns, and whether `k1p` can carry a prior loss for a blank-box activity.
Not re-checked: [T] items relayed from lane notes.
