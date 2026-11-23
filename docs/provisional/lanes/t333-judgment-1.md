# Lane note t333-judgment-1: T-333 judgment records, part 1 (Schedule E with Form 8582, Form 1116 with Schedule B, digital assets)

Written 2026-11-22 by scout claude-opus-5-5 (judgment, tax year 2025, jurisdiction us), carried into this note by lane
left (claude-sonnet-5-5, mechanical, 2025, us; worktree `.claude/worktrees/left`, branch `lane-left`, from `next`
9a2b3e9c). These are the judgment records that T-333 asks for (construction protocol section 2 items 3 and 4,
checklist item 7; coverage expansion protocol 8.8 item 12), for the lanes x1-sche, x1-f1116 and x1-digital. This is a
record of what the scout judged on that date, not guidance (`docs/provisional/README.md`).

**What lane left changed.** Only the citations. Every `Q:n` is now a line of `interview/2025/questions.yaml` in the
tree this note is committed on (the first line of the entry it names, or its range). `gate_frequencies.yaml:311-312`
and the `jr-verify.md` path were corrected, and the BUG_INVENTORY line in the earlier-draft list was replaced by where
the entries stand here. The judgments, shares, costs, tags and findings F1 to F4 are the scout's, unchanged.

**What the recheck found about the tree.** The scout read the `integrate-1` worktree (staged, not on `next`).
Against `next` these items of the records have no counterpart, so a reader of this tree will not find them; the
judgment is unchanged and each stands for the `integrate-1` wording:
- The `rental_use` group (`rental.business_incidental`, `rental.land_heavy`) and `f8582.prior_crd`: not in the question
  bank here. Q:181 here is the heading of `rprop_facts`.
- Wording quoted as present that is not in this tree: the `scope.rental` tick and help ("receive rent for", "Rent
  received in 2025 for an earlier year counts"; here the tick reads "Anything you own or lease rented or offered for
  rent, or royalties"); the home equity loan in the `rental_costs_a` tick (Q:7201 here reads "Other interest on loans
  for it"); the `rental.active` prompt "even if a manager did the daily work" (the help "Most owners answer Yes", Q:7189,
  is here); "Count it even from a year with no Form 1116" on `f1116.loss_accounts` (Q:850-858 here has no such
  sentence); and "Answer Yes also if its line 7 estimated a carryback to 2023 larger than the real one" on
  `ftc.carryover` (Q:1319-1320 here lacks it).
- Bug status written as fixed or closed in those records (BUG-0889, BUG-0890, BUG-0896, BUG-0910, BUG-0834 part 1,
  BUG-0938, BUG-0953, BUG-0964) is the status in `integrate-1`; in this tree those entries are open or unclosed.
- Everything else quoted from the question bank was found in this tree (a check of every quoted string of 20 or more
  characters against `interview/2025/` and `forms/2025/`, and of the cited line ranges by hand).

**Tags.** [C] means checked against the named file or page. [T] means testimony: a lane note, scout or earlier record,
not rechecked. [I] means my own judgment. Source pages are the form-feed pages of `sources/2025/<doc>.cols.txt`. For
p527, the page cited in `rental.yaml` agrees with this count.

**Format.** This follows construction protocol section 2, items 3 and 4, and checklist item 7, and coverage expansion
protocol 8.8 item 12. Effort ratings are on the owner's scale of 1 to 20 for answering and being right. They are all
[I] until the owner rates them (T-334). The N3 test is g < q·C, where g is the parent's cost, q is the share who answer
No, and C is the total cost of the children it spares.

**Earlier draft.** `docs/records/2026-11-16/nightplan/judgment-records.md` (xint tree) is an earlier draft for the same
areas. I treated it as testimony. Its line numbers are stale. Several of the bugs it cites are now closed:
- BUG-0889, BUG-0890, BUG-0896 and BUG-0910 are closed by a closure entry in the `integrate-1` tree (not in this tree, where the entries are open at `BUG_INVENTORY.md:10845`, `:10855`, `:10915` and `:11055`).
- Its candidate findings 4 (gift of crypto) and 5 (QBI safe harbor) are fixed in the int1 wording (Q:4004, Q:7546).
- The loss-account half of BUG-0834 is fixed in the int1 wording (Q:850-858).

**Share data in the tree:**
- `interview/2025/gate_frequencies.yaml` and `reports/2025/filer_coverage.md` (denominator 160,602,107 returns, tax
  year 2023).
- `tools/coverage/categories.json` has a `rental_royalty` category with no gates. The new gates of all three areas are
  in the report's list of unmeasured gates (`filer_coverage.md:20`).
- No count exists for Form 1116 filers, Form 8582 filers or digital-asset Yes answers.

---

## 1. Schedule E with Form 8582 (lane x1-sche)

**Typical filer.** One W-2 and one long-term single-family rental owned for years. Bank mortgage, MAGI under
$150,000 (scout `docs/provisional/lanes/scout-schedule-e.md` §4 [T]).

**Filer with nothing.** Leaves the `scope.rental` box unticked and meets no new step. The lane's walk of persona 01
shows no added step, but no before-walk was recorded (`x1-sche.md` §10 [T]).

### 1.1 Cost and share

Shares:
- `scope.rental` Yes: 5.9% of returns. SOI Table 1.4 columns 63 and 65 (rental and royalty net income 6,346,357; net
  loss 3,196,282) over 160,602,107 [C `gate_frequencies.yaml:311-312`, `filer_coverage.md:6`].
- Of those, about 33% have a net loss after combining all properties: 3,196,282 / 9,542,639 [C, same cells]. The scout
  gives 47% of rent returns with a rent-only loss [T, scout §1.4].
- Royalty-only figures (1.80 M with net income, 0.08 M with a loss) [T, scout §1.4]. Not rechecked: the xls cannot be
  read here.
- Every other share below is [I] unless marked.

| Parent (Q:) | Asked of | Share reaching (all returns) | Yes share | No cost g | Yes cost | N3 / note |
|---|---|---|---|---|---|---|
| `scope.rental` box, `own_income` (Q:1916) | everyone | 100% (one box) | 5.9% [data] | 1 | 1 | Off-ramp. A box, so the filer with nothing pays nothing new |
| `scope.rent_personal` (Q:7091), refuses | `scope.rental` Yes (`scope.rent_personal_if_rental`) | 5.9% [data] | under 5% [I]; no count | 1 to 2 | 1 (refusal) | Refusing child told at its topic (N11) |
| `$rental` roster (Q:7096) | `scope.rental` Yes | 5.9% | about 85 to 95% list a property; the rest are royalty-only [I, from the scout's royalty share] | 1 (empty list) | 2 per entry | |
| `rental.personal_any` (Q:7122; source F:rental.yaml) | each property | about 5.7% per return (rent) [T] | 10 to 15% [T, scout] | 2 | 3 | g 2 < 0.87 × C (days 3 + overlap 3) = 5.2: **pays** |
| `rental.short_stays` (Q:7138), parent of `stay7` | each property | same | 10 to 20% [T, scout] | 2 (5 if the filer must divide) | 5 | g 2 < 0.85 × C (stay7 2) = 1.7 is **false**: does not pay alone. It stays because it holds the 30-day fact that `rental.services` is read against (i8582 p. 3, exception 1b). Asking `stay7` alone would put a 7-day question to every landlord [I] |
| `rental_rare` group (heading Q:173; Q:7146-7185): services, under a tenth, not for profit, depletion, part of own home, held for sale | each property | same | under 3% [I] | 2 to 3 (six boxes) | 1 (refusal) | Catch-all screen (3.6) |
| `rental_use` group (heading Q:181 (heading of rprop_facts; the rental_use group is absent)): `rental.business_incidental`, `rental.land_heavy` | each property | same | under 2% [I] | 2 (both boxes have long help) | 1 (land_heavy refuses only with income and limited losses) | Group added after the lane (BUG-0953 fix). Not in `x1-sche.md` |
| `rental.active` (Q:7186) | each property | same | about 95% Yes [I] | 3 | 2 | Not a gate of children. It switches the loss between Form 8582 Part IV and Part V |
| `rental_costs_a/b/c` groups (Q:7191-7318) | each property | same | 3 to 6 boxes ticked [I] | 1 per box | 1, then the amount 2 to 5 | Boxes replace 13 "zero if none" amounts. Group c also holds three refusing boxes: `mortgage_excess`, `bought_lease`, `vehicle` |
| `rental.prior_any` (Q:7319), parent of `prior_amt`, `prior_not_active`, `prior_ws51` | each property | same | 15 to 25% of losing properties [T, scout] | 2 (5 with a loss history) | 5 | g 2 < 0.8 × C (amount 5 + 2 screens 3 + 3) = 8.8: **pays** |
| `$rprop` roster (Q:7337) | each property | same | about 95% list one or more [I] | 1 (empty, land only) | 5 + about 6 per entry (kind, month, year, basis 5 to 20, the exchanged screen, the `rprop_facts` group) | **Finding F1** |
| `rental.not_at_risk` (Q:7467), refuses | a property with a line 21 loss (`rental.has_loss`) | at most 33 to 47% of rental returns [data and T] | under 1% [I] | 3 (a 4-clause prompt) | 1 (refusal) | |
| `$royalty` roster (Q:7472) | `scope.rental` Yes | 5.9% | about 20% [T: 1.88 M royalty returns of 9.54 M] | 1 | 2 per entry | |
| `royalty_rare` group (Q:7478-7512) | each royalty | about 1.2% [T] | under 5% [I] | 2 | 1 (refusal) | |
| `royalty.expenses_any` (Q:7513) | each royalty | same | about 30% [I] | 2 | 3 | g 2 < 0.7 × C (three amounts at 2 = 6) = 4.2: **pays** |
| `rental_return` group (heading Q:185; Q:7533-7557): re_pro, grouped, qbi_business, accrual | `scope.rental` Yes, once | 5.9% | under 3% [I] | 2 (3 for a landlord with a QBI history) | 1 (refusal) | Catch-all screen |
| `f8582.prior_crd` (Q:absent in this tree) | as asked by its gate | not established | under 1% [I] | 2 | 1 (refusal) | Added after the lane. Its gate was not read |

### 1.2 Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `scope.rental` | Someone who received in 2025 rent for an earlier year | The source and tick now name "receive rent for" and "Rent received in 2025 for an earlier year counts" (Q:1920-1921; F:scope.yaml) [C] | guarded |
| `scope.rental` | A sublessor ("anything you own or lease") | the tick names "own or lease" [C] | guarded |
| `scope.rental` | Someone who rented out their own home for under 15 days | help: "even for a few days" [C]. The No costs nothing: i1040se p. 5, "rented the unit out for fewer than 15 days in 2025, do not report the rental income" [C] | harmless |
| `scope.rent_personal` | A landlord who also rents out equipment and reads the question as about the house | the prompt names "a car, a trailer or equipment" [C] | guarded |
| `rental.personal_any` | A relative paying below a fair rent; a co-owner's use; a home swap | the source names all three (F:rental.yaml, `rental.personal_any`); p527 p. 26, "A member of your family … unless the family member uses the dwelling unit as their main home and pays a fair rental price" [C] | guarded. BUG-0994 (open) is about the days question beneath it |
| `rental.personal_any` | A day the use was given to a charity (p527 p. 26, "Donation of use of the property") | the prompt's "did anyone stay free" covers it only by reading [I] | weak, low; not filed |
| `rental.short_stays` | An owner who thinks of the lease term rather than the average | help gives the division (Q:7139); i8582 p. 3, "dividing the total number of days in all rental periods by the number of rentals" [C] | guarded |
| `rental_rare` / under_tenth | An owner below 10% only for part of the year | the tick says "even briefly" (Q:7153); i8582 p. 4, "at any time during the tax year your interest … was less than 10%" [C] | guarded |
| `rental_costs_*` | Interest on a home equity loan spent on the rental | the tick now names it (Q:7201) | guarded (BUG-0938 wording) |
| `rental_costs_*` | Mortgage-acquisition costs; prepaid interest | help on amt13 and amt19 [C] | partly. BUG-0925 and BUG-0941 open |
| `rental.active` | A landlord who uses a manager and thinks that rules him out | the prompt: "even if a manager did the daily work"; help: "Most owners answer Yes" (Q:7189) [C]; i1040se p. 4, "without regular, continuous, and substantial involvement" [C] | guarded. A wrong No overpays (Part V) |
| `rental.prior_any` | A filer whose software held the loss back without saying so | help: "Look for Form 8582 in your 2024 return" (Q:7320) [C]; i8582 p. 10, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" [C] | guarded |
| `rental.prior_any` | A loss on the spouse's separate return | the source now says "even a separate one" (F:rental.yaml) [C] | guarded. BUG-0785 (open) also names a grouped activity; recheck it before fixing |
| `$rprop` (empty list) | A landlord who has never claimed depreciation | none. The prompt asks for what "you depreciate" and allows an empty list. No check ties a building kind to a non-empty list | **Finding F1** |
| `rental.not_at_risk` | A filer with a loan from a co-owner's company, or seller financing | the source and help name both (Q:7468-7470) [C] | guarded. BUG-0939 (open) is the narrower i1040se list |
| `royalty.expenses_any` | Severance or production taxes taken out of the check | the source names them (F:royalty.yaml) [C] | guarded (BUG-0890 closed) |
| `rental_return` / re_pro | A full-time agent who does not count their own rentals | help: "including running your own rentals" [C] | guarded. A wrong No overpays |
| `rental_return` / qbi_business | A landlord under the safe harbor | help names the safe harbor and the 2024 Form 8995 (Q:7546) [C] | guarded (earlier finding 5 fixed) |

### 1.3 Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `scope.rental` | A tenant who reads "rented" as renting from someone | about 3 wasted steps (`rent_personal`, empty roster, empty royalties) [I] |
| `scope.rent_personal` | **The landlord of a mobile home** ("trailer"). p527 p. 13: residential rental property is "a rental building or structure (including a mobile home)". p527 p. 25: a dwelling unit "includes a house, apartment, condominium, mobile home, boat" [C]. The prompt's word "trailer" (Q:7091, F:scope.yaml) invites a Yes, and the help speaks only of furniture | an unneeded refusal at `scope.schedule1`. **Finding F2** |
| `scope.rent_personal` | The landlord of a furnished house | help: furniture and appliances count as part of the home (Q:7092) [C]; guarded |
| `rental.kind` (a choice, not a parent) | A mobile-home landlord who picks "Something else" (Q:7103) | an unneeded refusal. Same cause as F2 |
| `rental_rare` / services | A long-term landlord who cleans shared areas | help excludes it (Q:7146) [C]; guarded |
| `rental.active` | An owner whose manager has full authority | the $25,000 allowance is applied wrongly and tax is understated. The help guards only the No side [I]. BUG-0836 (open) is a separate married-filing-separately issue |
| The refusing groups (`rental_rare`, `rental_use`, `rprop_facts`, `royalty_rare`, `rental_return`) and the vehicle, mortgage-excess and lease boxes | any misreading | an unneeded refusal only |

**Cross-area refusals worth recording** [C F:f1116.yaml `f1116.rental`; T `x1-sche.md` §1]:
- `sche.any` refuses EIC (`eic.step2_other`).
- `sche.any` refuses the whole Form 1116 path (`f1116.rental`).
- So a landlord with foreign tax above $300 is refused, and so is a low-income landlord who would claim EIC.

---

## 2. Form 1116 with Schedule B (Form 1116) (lane x1-f1116)

**Schedule B (Form 1040) (`sb`).** The expansion added no parent there. `forms/2025/sb.yaml` is not in the expansion
commit deca6831, and its last change is acde74b5 [C `git log`]. The `sb.*` bank entries are unchanged by these lanes.

**Typical filer.** A fund investor whose box-7 foreign tax is above $300 ($600 joint). i1116 p. 1: the election
requires that "Your total creditable foreign taxes aren't more than $300 ($600 if married filing a joint return)" [C].

**Filer with nothing.**
- Without foreign tax: no new step. The path opens only on `ftc.needs1116` (F:ftc.yaml) [C].
- An election filer: no new step either (`x1-f1116.md` §10 [T]).

**Shares:**
- Any foreign tax: 7.34% of returns (SOI Table 3.3 column 4, 11,791,525 returns [C `gate_frequencies.yaml:568-578`]).
- **No count exists of returns on the Form 1116 path.** The scout estimated 1 to 2.5% [T]. The lane estimated 0.2 to
  0.8% computed [T]. Archiving the SOI foreign tax credit tables is requested in `x1-f1116.md` §7.

### 2.1 Cost and share

| Parent (Q:) | Asked of | Share reaching | Yes share | No cost | Yes cost | N3 / note |
|---|---|---|---|---|---|---|
| `ftc.all_passive`, `ftc.statements`, `ftc.eligible` (Q:775-789) | any foreign tax | 7.34% [data] | over 95% Yes [I] | 2 to 5 | 1 | Not new. Before X1 they existed as screens for the election (g1-f6). A No now leads to the same refusal under a new name (`f1116.other_category`, `not_on_statement`, `not_creditable`) [C F:f1116.yaml]. Listed only because the path now hangs on them |
| `$f1116col` roster (Q:790) | path (`ftc.needs1116`) | 1 to 2.5% [T]; no data | n/a | n/a | 3, then 2 per entry | |
| `f1116col.kind` (Q:797), parent of the dividend and interest amounts | each entry | same | n/a | 1 | 1 | A choice. It spares 2 or 4 amounts. Pays [I] |
| `foreign_credit` group (heading Q:68): `foreign_gain`, `redetermination`, `reduction`, `loss_accounts` (Q:826-858) | path | same | under 3% [I] | 3 (four boxes, two with long help) | 1 (refusal) | Catch-all screen |
| `f1116sb.changed`, `f1116sb.split` (Q:859-874), same group | only with a carryover | well under 1% [I] | under 5% of those [I] | 2 | 1 (refusal) | |
| `ftc.carryover` (Q:1318; source F:ftc.yaml), parent of `$f1116sbyr` and the two boxes above | `ftc.carryover_ask`: `s3.foreign_any` (Q:1242), else `s3.prior_other_forms` (Q:1285) | at least 7.34% of those asked; plus 2024 returns with other forms [I] | under 5% [I] | 1 (never filed Form 1116) to 5 | 5 | g 1 < 0.95 × C (roster 5 + per-year amounts 5 + boxes 2 = 12): **pays** |
| `$f1116sbyr`, `.year`, `.amount` (Q:875-901) | carryover Yes | well under 1% | n/a | n/a | 5 + 5 per year | |
| `f1116sb.prior_year` (Q:902), five choices | only when a carryover is generated (`f1116sb.generated`) | well under 1% | n/a | n/a | 10 to 20 [I]: the choices are told apart by lines 23 and 24 of the 2024 Form 1116 (Q:912-913) | Rated in the earlier draft; ruled an effort matter for T-334, not a defect (`docs/records/2026-11-16/nightplan/jr-verify.md:17` [T]) |

### 2.2 Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `$f1116col` (too few entries, or tax left out) | A filer who lists the fund but not a directly held foreign share | two consistency checks: `f1116.tax_mismatch` (the columns' tax must equal `ftc.taxes`) and `f1116.income_over` (the columns' income must not exceed lines 3b/2b) [C F:f1116.yaml] | guarded mechanically |
| `f1116col.div_income` (an amount under the roster) | **A fund holder who enters box 1a (the whole dividend) instead of the fund's foreign-source share** | help: "A fund's year-end tax statement lists its foreign source income" (Q:805) [C]. `f1116.income_over` fires only above line 3b. i1116 p. 11: "Total all income, in the applicable category, passed through from the mutual fund or other RIC" [C] | **Finding F3**. The limit is overstated, so the credit can be overstated |
| `foreign_credit` / loss_accounts | A loss from a year with no Form 1116 | the prompt and help now name it: "Count it even from a year with no Form 1116" (Q:850-853) [C] | guarded. BUG-0834 part 1 is fixed in this wording. Part 2 (the carryback) is guarded below |
| `f1116sb.changed` | A carryback that differs from the estimate; a correction of line 8 | help names both (Q:859-862) [C] | guarded |
| `ftc.carryover` | A smaller-than-estimated carryback to 2023 | help: "Answer Yes also if its line 7 estimated a carryback to 2023 larger than the real one" (Q:1319-1320) [C] | guarded (BUG-0964 fix) |
| `ftc.carryover` | A carryover through a 2024 year when the tax was deducted, or the election was used | none | BUG-0827 (open, low) |
| `ftc.carryover` | A carryover filer with no 2025 foreign connection | `ftc.carryover_ask` falls back to `s3.prior_other_forms`. A 2024 Form 1116 is such a form [C F:ftc.yaml; Q:1289-1290] | guarded |
| `foreign_credit` / reduction | Tax on excluded income | the box names it (Q:842) [C] | guarded. Interplay with Form 2555 is BUG-0774 (open) |

### 2.3 Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `foreign_gain` | Someone who sold foreign shares through a U.S. broker | an unneeded refusal. Help: "usually counts as U.S. income" (Q:826) [C]; guarded |
| `ftc.carryover` | Someone who confuses it with a capital loss carryover | the roster, then `ftc.carryover_no_tax` refuses if there is no 2025 foreign tax; low |
| `f1116sb.split` | Joint before and joint now, with the same spouse | the prompt says "with someone you are not filing jointly with now" [C]; guarded |
| `f1116sb.prior_year` | A filer who cannot read lines 23 and 24 and picks a refusing answer | an unneeded refusal. Cost 10 to 20 (above) |

---

## 3. Digital assets (lane x1-digital)

**Typical filer.** Bought crypto on an exchange and sold or swapped some, with a Form 1099-DA [I].

**Filer with nothing.** Answers one new question, `f1040.digital_assets`. The lane's walk counts it as one step and 21
prompt words (`x1-digital.md` §10 [T]); the prompt is longer now. That step cannot be avoided: i1040gi p. 16, "Do not
leave the question unanswered. You must answer 'Yes' or 'No'" [C].

**Shares.** **No data.** No count of Yes answers is archived, and `x1-digital.md` §11 item 3 asks for one. The asset
sales screen is 13% of returns (`gate_frequencies.yaml:242-246` [C]). That share includes stocks, so it is only an
upper context, not a digital share.

### 3.1 Cost and share

| Parent (Q:) | Asked of | Share reaching | Yes share | No cost | Yes cost | N3 / note |
|---|---|---|---|---|---|---|
| `f1040.digital_assets` (Q:4004) | everyone | 100% | **no data**; 5 to 10% [I] | 1 (2 for a holder who only bought) | 1 | Printed question, required. Its child pays because g is spent anyway |
| `s1.digital_income` (Q:4010), parent of `s1.digital_amount` | `digital_assets` Yes (`s1.digital_income_if_assets`, F:s1.yaml) | 5 to 10% [I] | 10 to 20% [I] | 2 | 2 | g 2 < 0.85 × C (amount 3) = 2.55: **pays, narrowly** |

### 3.2 Who could answer No wrongly, and the guard

| Parent | Who | Guard | Status |
|---|---|---|---|
| `f1040.digital_assets` | A holder who was credited staking rewards or forked coins | the prompt names "a reward or new coins"; help names staking, mining, fork and airdrop (Q:4006) [C]; i1040gi p. 16, "Received new digital assets as a result of mining, staking, and similar activities" [C] | guarded (BUG-0896 closed) |
| `f1040.digital_assets` | Anyone with a sale under boxes G to L | the entry check `f1040.digital_conflict` refuses at line 7a [C F:f1040.yaml]. The `sales.box` labels send crypto to G to L only ("Crypto never goes under C or F", Q:1701-1702) [C] | guarded mechanically |
| `f1040.digital_assets` | Someone whose only event was paying for something with crypto | the prompt names "spend" [C] | guarded at the parent. See F4 for the sale question |
| `s1.digital_income` | A crypto prize or award | the list names staking, mining, fork and airdrop only (Q:4013-4014). A prize can still be entered at `s1.prizes` (Q:3928) [C]. i1040gi p. 15 lists "Received digital assets as a result of a reward or award" [C] | partly [I]. Which line is right (8i or 8v) is not settled here |
| `$sales` (Q:1685), beneath a Yes for spending | **A filer who said Yes because they paid with crypto** | only the help says "Swapping one crypto for another, or paying with it, is a sale" (Q:1686-1688). The prompt says "sell or trade", and no check ties a Yes to a sale entry | **Finding F4** (low). The gain on crypto spent is dropped |

### 3.3 Who could answer Yes wrongly, and the cost

| Parent | Who | Cost |
|---|---|---|
| `f1040.digital_assets` | A holder who only bought, or moved coins between their own wallets, or received a gift | help lists each as a No (Q:4006) [C]; i1040gi p. 16, the No list [C]. The cost is a printed Yes in error and one extra step; no tax changes |
| `s1.digital_income` | Someone who sold crypto, or was paid crypto as wages | help sends sales to the sales questions and wages to the W-2 (Q:4011-4012) [C]. If the help is not read, income is counted twice |

---

## 4. Findings for the bug inventory

I grepped `BUG_INVENTORY.md` and `bug_pending/` for each of these and found no existing entry.

- **F1 (low to medium), `$rprop`.** A landlord who has never claimed depreciation can truthfully leave the building
  list empty, because the prompt asks for each improvement "you depreciate" (Q:7337-7339). Depreciation is then
  dropped. No check ties a non-land `rental.kind` to a non-empty list. p527 p. 17: "If you didn't claim all the
  depreciation you were entitled to deduct, you must still reduce your basis in the property by the full amount of
  depreciation that you could have deducted" [C].
  - Fix candidates: word the prompt as "the building and each improvement (depreciation is allowed for them even if
    you never claimed it)", or refuse or ask when kind ≠ land and the list is empty.
  - The case of depreciation missed in earlier years (an accounting-method change) is neither asked nor refused [I].
- **F2 (low), `scope.rent_personal`.** The word "trailer" invites a Yes from a mobile-home landlord, who is then refused
  at `scope.schedule1` without need. A mobile home is residential rental property and a dwelling unit (p527 pp. 13,
  25; p946 p. 30) [C]. The same landlord may pick "Something else" at `rental.kind` (Q:7103).
  - Fix candidate: help "A mobile home or houseboat rented as a home is a building here: answer No for it", and a
    `rental.kind` label that names a mobile home.
  - A houseboat is not settled [I].
- **F3 (low to medium), `f1116col.div_income`.** A fund holder who enters the whole dividend in place of the fund's
  foreign-source share passes `f1116.income_over`. Line 1a, and so the limit, is overstated, and the credit with it
  where the limit should bind. The guard is help only (Q:805-807).
  - Fix candidate: a check of each column's foreign income against its tax. For example, refuse or ask again when the
    tax is under some small rate of the income [I; the threshold needs a source].
  - Or make the help the first sentence of the prompt.
- **F4 (low), `$sales` beneath a digital-asset Yes.** Spending crypto is a sale only in the help. The prompt is "sell
  or trade … crypto" (Q:1689-1690). A filer who answered Yes to `f1040.digital_assets` because they spent crypto may list no
  sale.
  - Fix candidate: add "or spend" to the `$sales` prompt.
  - Or add a check: digital Yes, no G to L sale and no line 8v, then ask once.

Effort notes, not defects:
- `rental.short_stays` does not pay for itself by N3 alone (it stays because it carries the 30-day fact).
- `f1116sb.prior_year` is rated 10 to 20. This belongs to T-334.

**Not done.** No walks or checks were run, so the walk figures are the lanes' [T]. The SOI royalty split was not
rechecked (the xls could not be read here). The gate of `f8582.prior_crd` was not read. The newer rental and rprop
refusing boxes (`rental_use`, `mortgage_excess`, `bought_lease`, `rprop.qip`, the `rprop.exchanged` widening) are
treated only as refusing boxes. They come from the round-F fix lane, not from x1-sche.
