# Judgment records for the coverage expansion lanes of 2026-11-15 (T-333), draft

Lane judgment-records. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16.
Read only. Nothing in the repository was changed. No engine, walk, fixture or check runs, and no paid calls.
Paths are relative to the xint worktree `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint`.
Tags: **[C path:line]** means checked against that file. **[I]** means inferred, or this lane's judgment.
`Q:` stands for `interview/2025/questions.yaml`.

## Summary

- **What this is.** T-333 lists the judgment records that are missing (`TASKS.md:101` [C]). This file drafts them
  for the seven areas, in the order the brief gives. The format follows protocol 8.8 item 12 and construction
  protocol section 2 items 3 and 4, and checklist item 7 (`docs/2026-11-15_coverage_expansion_protocol.md:463`,
  `docs/2026-11-13_interview_construction_protocol.md:116-133, 341` [C]). The table layout copies the redraft records
  in `docs/provisional/lanes/l5b.md:160-192` and `l2a.md:154-169` [C]. Each new parent gets three things: who could
  answer No wrongly and what guards against it; who could answer Yes wrongly and what that costs; and the cost
  rating (No cost, Yes cost) on the owner's scale. Where the parent is in front of children, the record adds the N3
  test (g < q·C).
- **The records are written for the lane notes.** Each area section is meant to be pasted into section 12 of its
  lane's note. The notes are `x1-sche.md`, `x1-f1116.md`, `x1-digital.md`, `mfs-l1..l4.md`, `x2-dep.md`, `x2-s1o.md`
  and `x2-paynow2.md`. This lane did not write them there, because it works read only.
- **Most wrong-answer risks are already filed.** The release screen and false-no reviews filed most of the
  wrong-answer risks at these parents as BUG-0765..0922. The records cite those ids rather than restate them.
- **Candidate findings that are new.** They are not in `BUG_INVENTORY.md` as far as a grep found. Ranked:
  1. **(medium) `household.community_property` asks where *you lived*, but the rule turns on each spouse's
     *domicile*.** A separate return is now computed. On one, a filer outside a community property state whose
     spouse is domiciled in one answers No, and the return is computed with no community-income split. A filer
     domiciled in such a state who lived elsewhere in 2025 also answers No. A servicemember stationed there under
     orders answers Yes and is refused when the return could be prepared. Pub. 555 is now archived
     (`sources/2025/p555.cols.txt:57`), which BUG-0519 item 4 said it was not.
  2. **(low to medium) The `scope.recovery` tick reads in the wrong direction.** The tick says "Paid back a
     deduction or credit that lowered tax", under the heading "Did any of these happen to you". Read that way, the
     filer did the paying. A tick on the other side of the interview, "Paid back more than $3,000 of income from an
     earlier year" (Q:1232), uses the same verb for the filer's own repayment. Someone who got a property tax refund
     can therefore answer No, and the recovery is dropped from line 8z.
  3. **(low to medium) `sa.dependent` now changes the return instead of refusing it.** A filer who answers Yes
     wrongly now gets the limited standard deduction, where before the return was refused. The answer depends on a
     test that a 19-to-23-year-old student must apply alone, and no question guards it.
  4. **(low) `f1040.digital_assets` counts a gift received as a Yes.** The prompt asks whether the filer received
     crypto at all, so someone who received crypto as a gift or an inheritance answers Yes. The instructions count
     a receipt only "as a reward, award, or payment". The result is that the printed Digital Assets box is wrong.
  5. **(low) `sche.qbi_business`.** A landlord whose earlier software took the QBI deduction under the rental safe
     harbor may tick No, and the deduction is silently dropped. The landlord overpays.
  6. **(low, cost and not correctness) Three questions are rated 20.** They are `f1116sb.prior_year` (the choices
     are told apart by the line numbers of the 2024 Form 1116), `person.mw_earned` (its help says "figure the
     return both ways") and `f1116col.div_income` (it needs the fund's year-end statement). Each is asked only of a
     rare filer.
  7. **(low, inferred) `household.mfs_living` and estranged spouses under one roof.** Such a spouse may answer
     "Not at any time". This is not checked against a source sentence.
- **Not covered here.** The K-1 lanes (`x2-k1e`, `x2-k1p`, `x2-k1s`) are x2 lanes but not one of the seven areas.
  `scope.k1` still refuses every K-1 (`/tmp/nightplan/med-k1sche.md`, headline 2), so their parents cannot be
  reached yet. They need the same record before `scope.k1` is lifted. Batch K of x2-dep (Form 8615) was not built,
  so it has no record.
- **Status.** Shares are this lane's judgment unless marked *gf* (`interview/2025/gate_frequencies.yaml`). Costs
  are this lane's estimates on the owner's scale: 1 means known at once, 5 means a moment's thought or a glance at
  a paper, 20 means the filer must find out what is being asked. Per construction protocol 1.1 they are estimates
  until the owner rates them (T-334). No record was checked in a walk.

---

## 1. Schedule E (lane x1-sche): rentals, royalties and Form 8582

**The typical filer** [I, scout `docs/provisional/lanes/scout-schedule-e.md` section 4]. One W-2 and one long-term
single-family rental owned for years. A tenant all year, a mortgage with a Form 1098, property tax, insurance and
repairs. MAGI under $150,000. **The filer with nothing** answers the existing `own_income` tick and meets no new step.
*gf* `schedule_e` share 0.10, of which rental and royalty is about 5.9% of returns
(`interview/2025/gate_frequencies.yaml:302-309` [C]).

### Cost and share

| Parent (Q: line) | Asked of | Yes share | No cost | Yes cost | N3 |
|---|---|---|---|---|---|
| `scope.rental` tick (Q:1827) | everyone (box on `own_income`) | about 6% *gf* | 1 | 1 | a tick, so no N3; the off-ramp |
| `scope.rent_personal` (Q:6892) | rental Yes | 3% [I] | 1 | 1 (refuses) | refusing child; told at its topic (N11) |
| `$rental` roster (Q:6897) | rental Yes | not applicable | — | 2 per entry | |
| `rental.personal_any` (Q:6921; source `forms/2025/rental.yaml:97`) | each property | 10 to 15% [scout] | 2 | 3 | g 2 < 0.87 × C (days 3 + overlap 3 = 6), so 2 < 5.2: it pays |
| `rental.short_stays` (Q:6935; `rental.yaml:349`) | each property | 10 to 20% [scout] | 2 (5 for a filer who must divide) | 5 | g 2 < 0.85 × (stay7 2), so 2 < 1.7: **does not pay alone**. It stays because `stay7` without it would ask every landlord a 7-day question; read the two together as one choice [I] |
| `rental_rare` tick group (Q:6943-6972; heading Q:161) | each property | under 3% [I] | 2 (five ticks read) | 1 to 2 (refuses) | catch-all; tick group (3.6) |
| `rental.active` (Q:6973; `rental.yaml:456`) | each property | about 95% Yes [I] | 3 | 2 | not a gate of children; it switches Part V |
| `rental_costs_a/b/c` tick groups (Q:6982-7052) | each property | most tick 3 to 5 [I] | — | 1 per tick, then the amount 2 to 5 | ticks replace 13 "zero if none" amounts |
| `rental.prior_any` (Q:7095; `rental.yaml:1632`) | each property | 15 to 25% of losing properties [scout] | 2 (5 with a loss history) | 5 | g 2 < q 0.8 × C (amount 5 + prior_not_active 3 = 8), so 2 < 6.4: it pays |
| `$rprop` roster (Q:7106) | each property | about 95% list one or more [I] | — | 5 + 4 per entry (kind, month, year, basis 5 to 20) | |
| `rprop.screen` (Q:7185; `forms/2025/rprop.yaml:77`) | each entry | under 2% [I] | 2 | 1 (refuses) | refusing |
| `rental.not_at_risk` (Q:7189; `rental.yaml:1949`) | a property with a line 21 loss | under 1% [I] | 3 | 1 (refuses) | refusing |
| `$royalty` roster (Q:7193) | rental Yes | about 15% of the box [I] | 1 | 2 per entry | |
| `royalty_rare` ticks (Q:7202-7213) | each royalty | under 5% [I] | 1 | 1 (refuses) | |
| `royalty.expenses_any` (Q:7214) | each royalty | 30% [I] | 2 | 3 | g 2 < 0.7 × (three amounts at 2 = 6), so 2 < 4.2: it pays |
| `rental_return` ticks (Q:7226-7243; heading Q:171) | rental Yes, once | under 3% [I] | 2 (3 for a landlord with QBI history) | 1 (refuses) | catch-all |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `scope.rental` | someone who leases a place and sublets it ("anything you own") | none | BUG-0910 (open, low) |
| `scope.rental` | an owner who rented a home for a few days | help: "even for a few days" (Q:1831) [C]. A rental of under 15 days is left out anyway, so a No costs nothing | guarded |
| `scope.rent_personal` | a landlord of a furnished house, who answers No correctly | help: furniture counts as part of the home (Q:6895) [C] | guarded (the Yes side is the risk) |
| `rental.personal_any` | a relative paying below a fair rent; a home swap; a co-owner's use | the prompt names all three (`rental.yaml:103-104`) [C] | guarded |
| `rental.personal_any` | a home converted to a rental in 2025 (main-home days) | help names days it was your main home (Q:6925) [C]. The arithmetic is BUG-0775, and part of a home is BUG-0920 | BUG-0775 open (medium); BUG-0920 fixed; BUG-0772 open (low) |
| `rental.short_stays` | an owner who thinks of the length of a lease | help: divide days by stays (Q:6938) [C] | guarded |
| `rental_rare` / services | services given by a manager | none | BUG-0784 (open, low) |
| `rental_rare` / part_home | a part the filer used otherwise or lived in earlier | none | BUG-0782 (open, low) |
| `rental_rare` / under_tenth | ownership under 10% at some time, or in the loss year | none | BUG-0783 (open, low) |
| `rental_costs_*` | expenses the tenant paid; a prepaid premium; capitalized costs; accrual basis | none | BUG-0789 (open, medium), BUG-0787, BUG-0776, BUG-0786 (low) |
| `rental.prior_any` | a filer whose software held a loss back silently | help: "Look for Form 8582 in your 2024 return" (Q:7097) [C] | guarded |
| `rental.prior_any` | a loss on the spouse's separate earlier return; a grouped activity; a Worksheet 5-1 carryover | none | BUG-0785, BUG-0778 (open, low) |
| `$rprop` (empty list) | a landlord who never took depreciation | the prompt: "leave the list empty for land only" (Q:7108-7109) [C]. A house owner cannot leave it empty truthfully | guarded |
| `rprop.screen` | qualified improvement property; a like-kind or involuntary conversion building | BUG-0919 fixed (QIP refused); BUG-0891 open (low) | partly |
| `rental.not_at_risk` | a loan from a person with an interest in the activity | none | BUG-0781 (open, low) |
| `$royalty` / `royalty.expenses_any` | taxes the payer withheld; the net amount entered | BUG-0921 fixed (line 4); BUG-0890 open (medium) | partly |
| `royalty_rare` | capital-gain royalties; an at-risk loss; other business royalties | none | BUG-0889 (open, low) |
| `rental_return` / re_pro | not knowing which work counts | none | BUG-0892 (open, low) |
| `rental_return` / qbi_business | a landlord whose earlier software claimed QBI under the 250-hour safe harbor, who reads the tick as asking about a business | none. The tick (Q:7238-7243) [C] names the deduction, not the safe harbor's facts | **new finding 5 (low)**. The cost is a lost deduction (an overpayment), not a wrong refusal |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `scope.rental` | a tenant who reads "rented" as renting from someone | about 3 wasted steps (roster, then empty) [I] |
| `scope.rent_personal` | a landlord of a furnished house who misses the help | a refusal not needed; the help guards it |
| `rental.personal_any` | family renting at a fair rent as their main home; days spent on repairs | wrong division of expenses (a wrong return). The help guards it (Q:6924-6926) [C] |
| `rental.active` | an owner whose manager has full authority | the $25,000 allowance applied wrongly, so tax is understated. Help: "Answer No only if someone else made all these decisions" (Q:6976) [C], which is guarded only in reverse. On a separate return living together, the allowance applies even with a right answer (BUG-0836, open, medium) |
| `rental_rare`, `rprop.screen`, `rental_return`, `royalty_rare`, the vehicle tick | any misreading | a refusal not needed (cost of the refusal only) |

---

## 2. Form 1116 with Schedule B (Form 1116) (lane x1-f1116)

"Schedule B" is read here as Schedule B (Form 1116), the carryover schedule. Schedule B (Form 1040) brought in no
new parent in these lanes [I: the `sb.*` entries at Q:1700-1750 were not in the lane's list].

**The typical filer** [I, scout]. A fund investor with foreign tax in box 7 of a 1099-DIV above the $300 limit, or a
filer not all of whose income is passive. **The filer with nothing**: *gf* `ftc.taxes` 7.3% have any foreign tax
(`gate_frequencies.yaml:569-572` [C]). Everyone else meets no new step, because the Form 1116 path opens only on
`ftc.needs1116` (`forms/2025/ftc.yaml:338` [C]).

### Cost and share

| Parent | Asked of | Yes share | No cost | Yes cost | N3 |
|---|---|---|---|---|---|
| `$f1116col` roster (Q:722) | the Form 1116 path | not applicable | — | 3, then 2 per entry | |
| `f1116col.kind` (Q:729) | each entry | not applicable | 1 | 1 | |
| `f1116col.div_income` (Q:737) | each entry with dividends | not applicable | — | **20 for a fund** (the year-end statement), 2 for a foreign company | amount; not a gate |
| `foreign_credit` ticks: `foreign_gain`, `redetermination`, `reduction`, `loss_accounts` (Q:758-791; heading Q:62) | the path | under 3% [I] | 3 (four ticks, two with long help) | 1 (refuses) | catch-all; tick group |
| `f1116sb.changed`, `f1116sb.split` (Q:792-807) | only with a carryover | under 5% of those [I] | 2 | 1 (refuses) | catch-all |
| `ftc.carryover` (Q:1237; source `ftc.yaml:68`) | `ftc.carryover_ask` (any foreign tax, or a 2024 return with other forms) | under 5% of those asked [I] | 1 (filed no Form 1116) to 5 | 5 | g 1 < q 0.95 × C (roster 5 + 2 ticks 2 + amounts 5 = 12), so it pays |
| `$f1116sbyr`, `.year`, `.amount` (Q:808-834) | carryover Yes | not applicable | — | 5 + 5 per year | |
| `f1116sb.prior_year` (Q:835) | only when an excess is generated | not applicable | — | **10 to 20**: the choices are told apart by lines 23 and 24 of the 2024 Form 1116 | rare; **finding 6** (N6) |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `foreign_credit` / loss_accounts | a loss account with no earlier Form 1116 | the tick names "an earlier Form 1116" (Q:787) [C] | BUG-0834 (open, low) |
| `f1116sb.changed` | a carryover created by a smaller carryback | none | BUG-0834 (open, low) |
| `ftc.carryover` | a carryover through a 2024 deduction year or an election year | none | BUG-0827 (open, low) |
| `ftc.carryover` | a filer with a carryover who answered No to any foreign tax in 2025 | `ftc.carryover_ask` also asks of a 2024 return with other forms (`ftc.yaml:79-97`) [C]. With no 2025 foreign tax the return refuses at `ftc.carryover_no_tax` | guarded |
| `foreign_credit` / reduction | foreign tax on excluded income | the tick names it (Q:779) [C]. Form 2555 interplay: BUG-0769, BUG-0774 | partly |
| `$f1116col` (too few entries) | a filer who lists only some sources | the conflict check `f1116.tax_mismatch` (column taxes must equal `ftc.taxes`) and `f1116.income_over` (lane note `x1-f1116.md:107-109`) [C] | guarded mechanically |
| the path itself | a Schedule E filer (gross rents missing from line 3e) | refusal `f1116.rental` on `sche.any` (`forms/2025/f1116.yaml:118-125, 1151`) [C] | guarded |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `foreign_gain` | someone who sold foreign shares through a U.S. broker | a refusal not needed. Help: "usually counts as U.S. income" (Q:762) [C], so guarded |
| `ftc.carryover` | a filer who confuses it with a capital loss carryover | a roster step, then the refusal `ftc.carryover_no_tax` when there is no foreign tax; low |
| `f1116sb.split` | a joint-to-joint return after remarriage to the same spouse | a refusal not needed; rare |

---

## 3. Digital assets (lane x1-digital)

**The typical filer** [I]. Someone who bought crypto on an exchange and sold some (a Form 1099-DA). **The filer with
nothing** answers one new question, `f1040.digital_assets` (21 prompt words, one step; walk of persona 01
`x1-digital.md:139-141` [C]). That step is unavoidable: the printed Form 1040 question must be answered by
everyone (i1040gi, "Do not leave the question unanswered"; `sources/2025/i1040gi.txt:877-879` [C]).

### Cost and share

| Parent | Asked of | Yes share | No cost | Yes cost | N3 |
|---|---|---|---|---|---|
| `f1040.digital_assets` (Q:3894) | everyone | 5 to 10% [I; not counted, `x1-digital.md:152`] | 1 (2 for a holder who only bought) | 1 | not a choice (the printed question). Its child `s1.digital_income` pays: g 0 (already asked) |
| `s1.digital_income` (Q:3901) | `digital_assets` Yes | 10 to 20% of those [I] | 2 | 2 | g 2 < 0.85 × (amount 3), so 2 < 2.6: it pays narrowly |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `f1040.digital_assets` | a holder credited with staking or fork coins who "only held" | the help lists being paid and swapping (Q:3897) [C], not staking while holding | BUG-0896 (open, medium); airdrops too |
| `f1040.digital_assets` | someone who swapped a stablecoin and reads it as dollars | help: "swapping one coin for another ... is a Yes" (Q:3897-3898) [C] | partly [I] |
| `f1040.digital_assets` | anyone with a sale in box G to L | the entry check `f1040.digital_conflict` refuses at line 7a (`x1-digital.md:59-60`) [C] | guarded mechanically |
| `s1.digital_income` | a No at the parent hides this child, so 8v income is dropped with no refusal | only the parent's help | covered by BUG-0896 |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `f1040.digital_assets` | **someone who received crypto as a gift or inheritance**, and nothing else. The prompt asks "receive ... crypto" (Q:3899-3900) [C]. The instructions count a receipt only "as a reward, award, or payment for property or services" (`sources/2025/i1040gi-html.txt:1275` [C]) | the printed Digital Assets box shows Yes wrongly, and one more step. No tax changes, because `s1.digital_amount` help says a gift is not income (Q:3911) [C]. **New finding 4 (low).** The fix is wording: "receive (as pay or a reward), sell, trade, spend or give away" |

---

## 4. Married filing separately (lanes mfs-l1 to mfs-l4)

**The typical filer** [I]. Married, filing separately to keep finances apart, with wages and perhaps a child.
**The filer with nothing**: every filer not married filing separately meets no new step. Each new question is
gated on `f1040.status` being mfs (lane notes `mfs-l1.md:93-94`, `mfs-l2.md:69-72`, `mfs-l4.md:68-69` [C]). The MFS
share is about 2 to 3% of returns [I]. *gf* `household.married_dec31` is 0.3656 and `household.community_property`
is 0.2335 (`gate_frequencies.yaml:40-66` [C]).

### Cost and share

| Parent | Asked of | Share | No cost | Yes cost | Note |
|---|---|---|---|---|---|
| `household.community_property` (Q:2701), existing; its Yes now refuses only MFS | everyone (existing) | 23% *gf* | 1 | 1 (MFS: refuses) | **finding 1** |
| `household.mfs_living` (Q:2729), a choice of three | MFS, only where a line reads it | not applicable | 1 to 2 | — | |
| `sa.spouse_itemizes` (Q:1316) | MFS | 30% [I] | **5** ("Ask them if you do not know") | 1 | needs the spouse |
| `sa.spouse_extra` (Q:1289) | MFS, spouse not itemizing | under 1% | 3 (three-part conjunction) | 1 (refuses) | refusing |
| `sa.mortgage_over_limit_mfs` (Q:1358) | MFS with mortgage interest | 10% [I] | 3 | 1 (refuses) | refusing |
| `ira.mfs_spouse_covered` (Q:6392) | MFS, a traditional contribution, not covered, living together | 50% [I] | 3 to 5 | 2 | |
| `f2441.mfs_spouse_deemed` (Q:2584) | MFS with care costs or benefits | 5% [I] | 2 | 1 (refuses) | asked before the earnings amount, as a guard |
| `f2441.mfs_spouse_earned` (Q:2589) | the same | not applicable | — | 5 (the spouse's W-2) | |
| `f8962.mfs_exception` (Q:3101) | MFS with a Form 1095-A | 10% [I] | 2 | 3 (sensitive) | |
| `f8962.mfs_three_years` (Q:3106) | exception Yes | under 5% | 2 | 1 | |
| `f8889.mfs_spouse_hsa` (Q:4525) | MFS with family HSA coverage | 30% [I] | 2 | 1 (refuses) | |
| `dependent.other_only_spouse` (Q:2382) | MFS, a child also living with another relative | not applicable | 2 | 2 | No may refuse |
| `dependent.spouse_claims` (Q:2386) | the above, Yes | 30% [I] | 2 | 1 (refuses) | |
| `dependent.filer_parent` (Q:2390) | the above, No | about 95% Yes [I] | 1 (may refuse) | 1 | |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `household.community_property` | **(a)** a separate filer who lived outside the nine states while the spouse was domiciled in one. **(b)** a filer domiciled in such a state who lived elsewhere (abroad, or on assignment) all of 2025. The prompt asks where "you live" (Q:2703-2704) [C]. Pub. 555: "The law of the state ... where you are domiciled will determine if you have community property ... If you and your spouse ... have different domiciles, check the laws of each" (`sources/2025/p555.cols.txt:57` [C]) | none. The help speaks only of the states (Q:2705-2706) [C] | **new finding 1 (medium).** On MFS the return is now computed (refusal `household.mfs_community_property`, `forms/2025/household.yaml:1755` [C]), so a false No gives a wrong return. Before, every MFS return was refused. BUG-0519 item 4 (closed) left the spouse-outside case as an over-refusal because "Pub. 555 ... is not archived", which no longer holds |
| `household.mfs_living` | temporary absences | help (Q:2733-2734) [C] | guarded |
| `household.mfs_living` | spouses estranged but under one roof, choosing "Not at any time" | none | **finding 7 (low, [I])**: not checked against a source sentence |
| `sa.spouse_itemizes` | a filer who has not asked the spouse | help: "Ask them" (Q:1318-1319) [C] | partly |
| `sa.mortgage_over_limit_mfs` | a filer who counts only half of a joint loan | help: count the whole loan (Q:1361) [C] | guarded |
| `ira.mfs_spouse_covered` | a filer who does not know the spouse's plan | help names W-2 box 13 (Q:6394-6395) [C] | partly |
| `f2441.mfs_spouse_deemed` / earned | a spouse who is a student with no pay, entered as 0 earnings | the deemed question comes first (`mfs-l3.md:92-93`) [C]. Other gaps: BUG-0799 (open, low) | guarded |
| `f8962.mfs_exception` | a filer unsure whether emotional abuse counts | help (Q:3104) [C] | BUG-0798 (open, low) |
| `f8889.mfs_spouse_hsa` | a spouse with an empty HSA | help (Q:4527) [C]. The then-spouse case: BUG-0874 | partly |
| `dependent.other_claimant` (existing tick) | an MFS parent living with the other parent, who passes over the box | help: "On a separate return, your husband or wife counts" (Q:2359) [C]; the tick cannot hold it (`mfs-l4.md:110-112`) [C] | partly (an owner's walk item) |
| `dependent.other_only_spouse` | another parent of the child living there too | the help tells this filer to answer No | BUG-0864 (open, low) |
| estimated tax | how joint estimated payments are divided | none | BUG-0894 (open, low) |
| Form 8582 (no question) | lived together; allowance given anyway | none | BUG-0836 (open, medium) |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `household.community_property` | a servicemember (or the servicemember's spouse) stationed in one of the nine states but domiciled elsewhere; a student there | a refusal not needed on MFS (finding 1, second half) |
| `sa.spouse_itemizes` | a filer who guesses Yes | the standard deduction is zero; a wrong return in the IRS's favour [I] |
| `dependent.spouse_claims` | a parent unsure what the spouse will do | a refusal; help says "agree which of you will" (Q:2388) [C] |

---

## 5. Filers who can be claimed as a dependent (lane x2-dep)

The lane added **no new question** (`x2-dep.md:3-8, 28-31` [C]). Its effect on judgment is that the existing parent
`sa.dependent` (Q:1283, order 111) no longer refuses on Yes; the Yes now computes the dependent worksheet. The
record is therefore owed for `sa.dependent` under its new consequence.

**The typical filer**: a full-time student, aged 19 to 23, with a part-time W-2, whose parents claim them (persona
`14_dependent_student`; `x2-dep.md` section 10 [C]). *gf* share 4.69% (`gate_frequencies.yaml:75-78` [C]).

| Parent | Asked of | Yes share | No cost | Yes cost |
|---|---|---|---|---|
| `sa.dependent` (Q:1283) | everyone | 4.7% *gf* | 1 for most; **5 to 20 for ages 18 to 23** (the qualifying-child or qualifying-relative test) | 1 (parents claim) to 20 |

**Who could answer No wrongly.** A student whose parents *could* claim but do not. The guard is the help, "It is
whether they can, not whether they do" (Q:1286) [C]. A student who thinks support means rent alone has no guard.
The cost is a full standard deduction, so tax is understated. This is unchanged from before the lane, except that a
No was then the only way past the refusal. The lane removes that incentive, an improvement [I].

**Who could answer Yes wrongly** (new consequence). A student who is not a qualifying child (not a full-time
student in 5 months, or 24 and over) and whose gross income is over the qualifying-relative limit, so that no one can
claim them. The help pushes doubters toward Yes. The cost is a standard deduction limited to earned income plus $450
(`x2-dep.md:72-76` [C]). That costs money only where earned income is below about $15,300 or there is unearned
income [I]. **Finding 3 (low to medium)**: there is no child or guard. A possible remedy is a child beneath Yes, of the
form "Is that person your parent, and were you under 24 and a full-time student, or under 19, at the end of 2025?",
with a No opening the qualifying-relative income check. This is a sketch and has not been designed.

Related: `person.sav_claimed` (Q:6364) asks "actually claims", which keeps the education and saver's credits apart
from the "can claim" fact [C]. Its No-wrong person is a student who does not know whether the parents claimed; that
has no guard. `dependent.ptc_files` is BUG-0861 (open, medium).

---

## 6. Schedule 1 other income (lane x2-s1o)

**The typical filer** [I]: an itemizer for 2024 who got a property tax or mortgage interest refund (persona
`21_money_back_itemizer`). **The filer with nothing** meets no new step: every new question is beneath an existing
tick (`x2-s1o.md:181-183` [C]). Line 8u was taken back out at integration and is refused (T-336).

### Cost and share

| Parent | Asked of | Yes share | No cost | Yes cost | N3 |
|---|---|---|---|---|---|
| `scope.recovery` tick (Q:2000), no longer refusing | everyone (`money_b`) | 1 to 3% [I] | 1 (**3 when the direction is misread**) | 2 | tick |
| `rec_rare` ticks (heading Q:72) | recovery Yes | under 5% | 2 | 1 (refuses) | catch-all |
| `rec_kinds` ticks (heading Q:74) | recovery on the 2024-itemized path | not applicable | — | 1 per tick | replaces four "0 if none" amounts (`x2-s1o.md:84-86`) [C]: it pays |
| `scope.nol` tick (Q:2066), no longer refusing | everyone (`before_2025`) | 0.6% [I, `x2-s1o.md:186`] | 1 to 3 | 2 | |
| `nol_facts` ticks (Q:2081-2104) | NOL Yes | 10% [I] | 3 (four ticks; the joint ones need history) | 1 (refuses) | catch-all |
| `s1.ltc_payout` tick (Q:3886), now computed | everyone (`money_b`) | under 0.5% | 1 | 3 | |
| `f8853c.periodic` (source `forms/2025/f8853c.yaml:37`) | each insured | 50% [I] | 3 (the Form 1099-LTC box 3) | 3 | gate of the per diem lines |
| `s1.stock_options` / `options_amount` (Q:3786-3796) | an option or ESPP holder | 5% of holders [I] | 3 | 5 | |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `scope.recovery` | **someone who got a property tax or mortgage refund and reads the tick "Paid back a deduction or credit that lowered tax" as something they paid.** The heading is "Did any of these happen to you" (Q:54-55, 2004) [C]. The source says "were you ... paid back" (`forms/2025/scope.yaml:849-852`) [C], but the tick drops the passive voice | none. The help's examples ("a refund of property tax") point the right way but are optional (N10) | **new finding 2 (low to medium).** The cost of a false No is a recovery left out of line 8z: a wrong completed return. The sibling tick "Paid back more than $3,000 of income from an earlier year" (Q:1232, `s3.repaid_income`) uses the same verb for the opposite flow. A filer with such a repayment could tick `scope.recovery` (Yes wrongly; a cost of 3 to 5 steps, then likely a refusal in `rec_rare`). Suggested tick: "Got money back for something you deducted or took a credit for (not a state/local income tax refund)" (15 words) |
| `scope.recovery` | an itemizer for 2023 told to answer No by the 2024-only help; nonitemized, credit and sales tax recoveries | none | BUG-0908 (open, low) |
| `rec.two_returns` / `refund.itemized` | a joint couple where only the spouse itemized separately in 2024 | none | BUG-0899 (open, medium) |
| `scope.nol` | a disallowed excess business loss; a first-year carryforward; rental or K-1 losses | none | BUG-0907 (open, medium), BUG-0812 (open, low) |
| `s1.ltc_payout` | the insurer's checks went to the care facility | the tick says "paid by", and the help names Form 1099-LTC (Q:3890) [C] | partly [I] |
| `f8853c.*` | reimbursement, pre-1996 and others-paid questions narrower than their lines | none | BUG-0873 (open, medium), BUG-0916 (low) |
| `s1.inmate_wages` | work release; another correctional facility | none | BUG-0823 (open, low). The line is refused (T-336) |
| `s1.stock_options` | options exercised by a director, contractor, heir or former spouse | none | BUG-0826 (open, low) |
| `s1.hobby_any` (not this lane's, on the same screen) | a hobby that lost money | none | BUG-0822 (open, medium) |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `scope.recovery` | a filer who repaid income (the direction misread) | 3 to 5 steps and a likely refusal not needed (finding 2) |
| `scope.nol` | a capital loss carryover filer | `nol_facts` ticks and an amount; the help defines the NOL (Q:2070) [C]. A confusion is likely only among filers with both [I] |
| `nol_facts` / joint ticks | a married filer unsure of the loss year | a refusal not needed |

---

## 7. Pay not on a W-2 (lane x2-paynow2)

**The typical filer** [I]: a carer paid by a household with no W-2, or a server with unreported cash tips.
**The filer with nothing** answers the same single `other_pay` screen as before (`x2-paynow2.md:41-42` [C]; not
walked). *gf* `additional_medicare_items` 0.6% (`gate_frequencies.yaml:798-803` [C]).

### Cost and share

| Parent | Asked of | Yes share | No cost | Yes cost | N3 |
|---|---|---|---|---|---|
| `scope.pay_no_w2` tick (Q:1845), no longer refusing | everyone (`other_pay`) | about 1% [I] | 1 | 1 | tick. Opens `pay_kinds` (cost 2), so a No spares 2 to 10: it pays |
| `scope.medicaid_waiver` tick (Q:1851) | everyone (`other_pay`) | 0.2% [I] | 1 | 1 | |
| `pay_kinds` ticks: household, contractor, tips, strike, wages_no_form (Q:1857-1885; heading Q:43) | pay_no_w2 Yes | not applicable | — | 2 for the screen | not a catch-all; the filer picks which |
| `$f8919firm` + `.reason` (Q:1890-1906) | contractor Yes | not applicable | — | 5 (an SS-8 status) | |
| `$f4137row` + columns (Q:1916-1933) | tips Yes | not applicable | — | 5 to 20 (the tip log) | |
| `person.f4137_under20`, `tips_gov`, `tips_noncash` (Q:1934-1946) | tips Yes | under 10% [I] | 2 to 3 | 3 to 5 | |
| `person.mw_box1 / mw_not_box1 / mw_1099` (Q:1947-1957) | Medicaid Yes | not applicable | — | 5 (W-2 box 1 compared with box 12 code II) | amounts |
| `person.mw_business` (Q:1958) | a 1099 amount above 0 | under 10% | 2 | 1 (refuses) | |
| `person.mw_earned` (Q:1962), the election | Medicaid paid | not applicable | — | **20**: help says "If unsure, figure the return both ways" | **finding 6**: an owner decision to ask (`x2-paynow2.md:15` [C]). The tool could compute both and pick |
| `retirement.dis_all_early` (Q:3615) | a disability pension, code 3 | about 90% Yes [I] | 3 (a No refuses) | 2 | refusing on No; asked after `dis_early` |

### Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `scope.pay_no_w2` | lockout benefits; strike funds not from a union; noncash or small tips; an employer that issues no W-2 | none in the tick. `pay_kinds` names them only after a Yes | BUG-0906 (open, medium) |
| `scope.medicaid_waiver` | pay through an agency or fiscal agent | none | BUG-0904 (open, medium) |
| `scope.household_pay` (Q:1857) | a driver or groundskeeper; a live-in carer in a shared home | none | BUG-0903 (open, low) |
| `scope.contractor_pay` | a worker who believes they were an employee but files Schedule C out of habit | help: "and you are not reporting the pay as a business of your own" (Q:1867) [C] | guarded (it routes, it does not prevent) |
| `f4137row.col_c` | December 2024 tips reported in January 2025 | the help speaks only of December 2025 | BUG-0915 (open, low) |
| `retirement.dis_all_early` | (a No refuses, so a false No is a refusal not needed) | help (Q:3617) [C] | guarded |

### Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `scope.contractor_pay` | a true independent contractor | Form 8919 is filed wrongly and half the SE tax is shifted. Guard: the help's three conditions and the reason enum (Q:1896-1906) [C]. Note that `f8919firm.reason` is not asked as built, because no line reads it (`x2-paynow2.md:105-107` [C]), so the guard the enum gives may be absent. **Check in the walk** [I] |
| `scope.tips_unreported` | a server whose W-2 box 7 already holds all tips | the rows give column (d) equal to (c), so the result is zero, at a cost of about 4 steps [I] |
| `person.tips_gov` | a non-government worker | a refusal not needed; the refusal is told late (`x2-paynow2.md:108-110` [C]) |

---

## Findings, ranked (new only; known items are cited above by BUG id)

| Rank | Finding | Area | Evidence | Cost of the wrong answer | Sketch of remedy |
|---|---|---|---|---|---|
| 1 | `household.community_property` asks residence, but the rule is domicile, and the spouse's domicile counts | MFS | Q:2701-2706; `sources/2025/p555.cols.txt:57`; `forms/2025/household.yaml:1755` [C] | a separate return computed without the community-income split (wrong return); a servicemember over-refused | a child beneath an MFS No: "Was your husband or wife's permanent home (the place they mean to return to) in one of these states in 2025?" (Yes refuses). Help on the parent: "Count the state you treat as your permanent home". Needs a coverage row per case and a screen review of `household.mfs_community_property` |
| 2 | The `scope.recovery` tick verb reads as the filer paying | S1 other | Q:54-55, 2000-2006, 1232; `forms/2025/scope.yaml:849-852` [C] | a recovery dropped from 8z, or a refusal not needed | the tick "Got money back for something you deducted or took a credit for (not a state/local income tax refund)" |
| 3 | `sa.dependent` Yes now changes the deduction and has no guard | dependent filers | Q:1283-1286; `x2-dep.md:28-31` [C] | standard deduction limited wrongly (overpayment) | a child confirming the qualifying-child facts, or help naming the age and student tests; owner's walk |
| 4 | `f1040.digital_assets` counts a gift received as a Yes | digital | Q:3899-3900; `sources/2025/i1040gi-html.txt:1275` [C] | a wrong printed box; one more step | "receive as pay or a reward, sell, trade, spend or give away" |
| 5 | The `sche.qbi_business` tick misses landlords who used the safe harbor | Schedule E | Q:7238-7243 [C] | QBI deduction dropped (overpayment); the return is otherwise right | help: "Answer Yes if a rental's income was counted for the QBI deduction on your 2024 return" |
| 6 | Cost-20 questions | 1116, pay | Q:835-848, 1962-1965, 737-742 [C] | effort only | owner's ratings (T-334). For `mw_earned`, consider computing both ways |
| 7 | Estranged spouses under one roof at `household.mfs_living` | MFS | Q:2729-2738 [C]; rule not read [I] | the line 6d box and the 85% SSB base | read p915 and p501 "lived apart"; add help if confirmed |

## What was checked and what was not

- **Checked by reading** (path:line above): the bank entries, the form sources of the inputs named, the lane notes,
  TASKS.md T-333, the two protocols, gate_frequencies shares, Pub. 555 p. 2, i1040gi on digital assets, and the
  status of every cited BUG id (via `tools/bug_status.py`, read only).
- **Not checked**: any walk (draft-walk not run under the hard rules); whether each question is reached as its
  gating says; the K-1 lanes. The share and cost figures are judgment, except those marked *gf*. Findings 1 to 5
  were not run through the screen or false-no review tools (paid). They should go to the owner or a reviewer as
  candidates before any pending bug entry is written.
- **For pasting into the lane notes** (T-333's deliverable): each section above maps to section 12 of the named
  lane note. The MFS section splits by lane as follows: household to l1; `sa`/`ira` to l2; `f2441`/`f8962`/`f8889`
  to l3; `dependent` to l4.
