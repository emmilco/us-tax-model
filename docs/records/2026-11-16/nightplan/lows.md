# Lows triage (lane lows-triage)

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16. Read only on xint. Nothing run except
`tools/bug_status.py --open` and small read-only parsing scripts in /tmp/nightplan/scratch/lows/.

Labels: **[C path:line]** = checked against that file in xint; **[C]** = checked, path given in the row;
**[U]** = unchecked (the entry's own claim, relayed, not reproduced); **[I]** = inferred.
"Ride" = the drafted patch in /tmp/nightplan/patches/v2/ (or round 2 where no v2 exists: sche-a has only a round-2 .md,
v2/sche-a.patch exists) that touches the same bank entry, input or form file, so the low can land in that patch's
review round instead of making a new one. A ride is **by entry** when the patch edits the same input or its
neighbour in the bank, **by file** when it edits only the same form file (weaker: still a re-review of that form).

## Summary

- **Scope.** `bug_status.py --open` lists 200 entries. 157 are in scope: severity low (by `Severity:` or, in older
  entries, by a `low` tag or "(low)" in the title) or no severity at all. 43 are medium or high and out of scope.
- **Closure candidates (9).** Fixed or obsolete in xint, but still open in the inventory:
  BUG-0092, 0465, 0532, 0729, 0757, 0647, 0893 checked against files; BUG-0894 and BUG-0781 close when their patch
  lands (inc-m34 and sche-a). Details in section 3.
- **Ride-alongs.** About 95 of the 157 lows touch a form or bank entry that a drafted patch already changes.
  The best yield by patch: **sche-a** (17 rental, royalty and asset lows), **inc-m12** (about 25 s1, scope, person
  and tip lows), **older-ny** (11 New York lows), **older-scha / 0817b** (11 Schedule A lows), **inc-m34**
  (9 lows: f8853c, s2, refund, f1040 payments), **older-credits** (about 12 dependent, f5695 and retirement lows),
  **int-p18** (6 sales and sd lows), **int-n10** (4 k1p, k1s, rental and rprop lows), **int-amt** (3).
- **Quick-win batch (section 4).** 46 lows are S effort and wording only (bank help or prompt). Of these, 31 ride
  with a patch by entry. The other 15 have no patch and form one lane.
- **Upgrade to medium (section 5).** BUG-0656 (the federal mutate step fails until its 83 survivors are killed or
  explained, so it gates a release), BUG-0795 (treaty-exempt income stays in wages, AGI and earned income), and
  BUG-0871 (IRA basis from an after-tax plan rollover read as No, so the distribution is overtaxed). Possibly also
  BUG-0762 and BUG-0799.
- **One cross-patch interaction to watch.** int-amt makes `f1040.tax_exempt_interest` a gated amount. BUG-0857's New
  York out-of-state bond gate reads it. Fix 0857 in the same round, or at least re-walk the New York bond questions
  after int-amt [I].
- **Partly fixed by patches already drafted:** BUG-0555 (older-credits changes line 21a's tense and the panel tick's
  year), BUG-0888 and BUG-0845 (int-n10 widens the k1s and k1p at-risk prompts), BUG-0565 item (1) (sche-a names the
  sibling). The residuals ride with the same patch.

## 1. Triage, one line per entry, grouped by form

Columns: id | what | still real? | effort | ride.

### Rental, royalty, rprop, sche, asset (forms/2025/rental.yaml, royalty.yaml, rprop.yaml, sche.yaml, asset.yaml)

- BUG-0772 | personal-use days: main-home exclusion omits a shorter rental ended by a sale | real [I: v2/int-n10.patch:91 new prompt still says "12 months in a row" only] | S wording | **int-n10** (rental.days_personal prompt) by entry; or sche-a by file
- BUG-0776 | rental cost questions do not exclude capitalized legal fees and capital purchases | real [U] | S wording | **sche-a** by entry (rental.amt10 hunk)
- BUG-0777 | mortgage interest not allocated by use of the loan proceeds | real [U] | S wording | **sche-a** by entry (rental.amt12)
- BUG-0778 | Worksheet 5-1 carryover neither asked nor refused | real [U] | M (new rental_rare tick + refusal) | **sche-a** by entry (rental_rare group hunk)
- BUG-0779 | Form 8582 exceptions 3 to 6 and dealer property not screened | real [U] | M (tick + refusal) | **sche-a** (rental_rare; f8582.exception hunk)
- BUG-0781 | rental at-risk question reaches only nonrecourse loans from non-lenders | **fixed by sche-a when it lands** [C v2/sche-a.patch: new rental.not_at_risk source adds guarantee/stop-loss and "lent by someone with a stake in it"] | — | **sche-a**: record the closure with it
- BUG-0782 | part-of-property refusal misses a part used otherwise or lived in earlier in 2025 | real [U] | S wording (source + tick) | **sche-a** (rental_rare)
- BUG-0783 | 10% ownership: no "at any time"; not asked for the loss year | real [U] | S wording | **sche-a** (rental_rare / f8582 file)
- BUG-0784 | services question answerable No when a manager provides them | real [U] | S wording | **sche-a** (rental_rare)
- BUG-0785 | held-back loss question omits spouse's separate return and grouped activity | real [U] | S wording | **sche-a** (f8582 / rental file)
- BUG-0786 | accrual-method landlord not asked | real [U] | S (refusing tick) | **sche-a** (rental_rare)
- BUG-0787 | prepaid insurance's 2025 part excluded | real [U] | S wording | **sche-a** by entry (rental.amt9 hunk)
- BUG-0788 | citations name Line 8/9/15 instructions i1040se lacks | real [U] | S citation, no value change | **sche-a** (rental.yaml file)
- BUG-0925 | prepaid interest and points taken in year paid | real [U] | S wording | **sche-a** by entry (rental.amt12/amt13 hunk)
- BUG-0926 | co-owner under shared equity financing counted as personal use | real [U] | S wording | **int-n10** (rental.personal_any) by entry
- BUG-0889 | royalty: no screen for at-risk loss, capital-gain royalties, other business royalties, depreciation, car/travel | real [C sche-a.md:205 "Royalty has no at-risk question: BUG-0889, open"] | M (ticks + refusals) | **sche-a** (royalty_rare hunk)
- BUG-0922 | royalty expense questions do not exclude capitalized costs | real [I: v2/sche-a.patch royalty.amt19 new source adds "taken out of your payments" but no capital exclusion] | S wording | **sche-a** by entry (royalty.amt19)
- BUG-0891 | rprop: building from a like-kind exchange or involuntary conversion | real [U] | S (screen list item, refuses) | **int-n10** by file (rprop.kind prompt)
- BUG-0892 | sche.re_pro: which work is a real estate business | real [U] | S help | none (sche-a by file family only)
- BUG-0565 | Form 4562 asset wording lows (listed property, unadjusted basis, whole percent, calendar quarters, 521 coop) | real [C sche-a.md:39 names item (1)'s sibling as not patched] | S to M | **sche-a** by entry (asset.listed)
- BUG-0791 | asset.industry asks about the business, not the item | real [U] | S wording (tick) | **sche-a** by file (asset.yaml)

### Schedule C, vehicles, carloan (sc, scveh, carloan)

- BUG-0530 | Schedule C screens: over-refusals and rare gaps (8 items) | real [U] | M | none
- BUG-0780 | sc.special names the lease inclusion amount only by its term | real [U] | S wording | none (quick-win lane)
- BUG-0559 | Schedule C vehicle question lows (line 43 date, binding contract, shared vehicles, ...) | real [U] | M | none
- BUG-0792 | earlier-year low-use question does not prorate a converted vehicle | real [U] | S help | none (quick-win lane)
- BUG-0515 | carloan wording lows (rebates, refinancing chains, assumed loans) | real [U] | S to M | none
- BUG-0734 | 2026 draft carloan.original_use derived from carloan.vehicle (heir) | real, 2026 only [U] | S, at 2026 adoption | none: do at the 2026 adoption

### Schedule 1, scope screens, tips (s1, scope, tipjob, f4137row, oi8z)

- BUG-0809 | professional-gambler screen asks "the way a living is made" | real [C interview/2025/questions.yaml:3822] | S wording | **inc-m12** by entry (gambling winnings / s1.gambling_pro coverage rows)
- BUG-0811 | alimony gate and amount wording | real [U] | S wording | **inc-m12** by file (s1 bank)
- BUG-0812 | NOL questions: joint carryback year; scope.nol lacks excess business loss | real [U] | S wording | **sche-a** by entry (s1.nol_amount hunk; also 0907's scope.nol wording there)
- BUG-0813 | unemployment gate help points to the form | real [U] | S help | **inc-m12** by file
- BUG-0814 | Alaska dividend gate has no help | real [U] | S help | **inc-m12** by file
- BUG-0804 | line 8z damages: emotional-distress medical, pre-1995 awards, attorney fees | real [U] | S help (+ optional refusal M) | **inc-m12** by file (s1 other income)
- BUG-0823 | s1.inmate_wages "jail or prison" misses work release / other facilities | real [C interview/2025/questions.yaml:3802 tick "while in a jail or prison"]; the line 8u half of its fix is moot after the revert (see 0893) | S wording | **inc-m12** by entry (money_b group, beside the hobby/prize hunks)
- BUG-0824 | jury pay gate misses jury-pool days | real [U] | S wording | **inc-m12** (money_b)
- BUG-0825 | scholarship gate misses research fellowships / stipends | real [U] | S wording | **inc-m12** (money_b)
- BUG-0893 | inmate W-2 wages counted on line 1a and line 8u | **obsolete** [C forms/2025/s1.yaml: no s1.line8u, no s1.inmate_amount (0 matches); BUG-0766 Fix: line 8u reverted, inmate pay refuses at s1.line8_other] | — | closure (premise removed; T-336)
- BUG-0713 | personal-property rental not for profit refused through scope.rental | real [C forms/2025/scope.yaml:393] | M (coverage intake, by the entry's own disposition) | none
- BUG-0719 | scope.excess_deferral counts 457(b) against the 401(k) limit | real [U] | S wording | **inc-m12** by file (scope.yaml)
- BUG-0771 | scope.other_income cites lines 1b/1c/1d/1h quotes of pay now computed | unchecked [U: locator not found in a quick read of scope.yaml:1229+] | S citation | **inc-m12** by file (scope.yaml; same pay lines it edits)
- BUG-0795 | treaty-exempt income neither asked nor refused | real [U] | M (scope screen item + refusal) | **inc-m12** by file. **Upgrade candidate** (section 5)
- BUG-0902 | armed forces gate: surviving spouse moving under orders; Coast Guard | real [U] | S wording | **inc-m12** by file
- BUG-0903 | household pay gate: driver, groundskeeper, live-in carer | real [U] | S wording | **inc-m12** by entry (scope.household_pay coverage rows) or **inc-m34** (household employee 0901)
- BUG-0908 | recovery gate help tied to 2024; missing examples | real [U] | S help | **inc-m34** by entry family (rec/refund hunks)
- BUG-0909 | religious work gate: orders, housing/offerings, officiants | real [U] | S wording | **inc-m12** by file
- BUG-0910 | rental gate "anything you own" misses a lease-and-sublet | real [C forms/2025/scope.yaml:393,396] | S wording | **inc-m12** by file; touch with 0713 (same input)
- BUG-0915 | f4137row col (c): December 2024 tips reported in January 2025 | real [U] | S wording | **inc-m12** by file (tipjob) / int-n10 (person.f4137_under20)

### Person screens, retirement, IRA, SSB, student loans (person, retirement, ira, ssb, sli, f5329)

- BUG-0865 | Form 5329 screen lines cite Parts II and IX only; x_edu_account label vs question | real [U] | S citation/label | **inc-m12** by file (person.yaml)
- BUG-0866 | education/ABLE questions miss for-2025 Coverdell in 2026 etc. | real [U] | S wording | **inc-m12** by file
- BUG-0867 | no January 1 birthday rule in dependent.age and age questions | real [U] | S help | **older-credits** by file (dependent bank)
- BUG-0868 | eligible educator: which school year's 900 hours | real [U] | S help | **inc-m12** by file
- BUG-0869 | person.edu_over: course materials and term timing | real [U] | S wording | **older-credits** by entry (f8863.ban / person.edu_fulltime hunk)
- BUG-0872 | person.died_at_64 "final return" wording | real [U] | S wording | **inc-m12** by file
- BUG-0508 | combined-ages question assumes one beneficiary | real but nearly covered [C forms/2025/retirement.yaml:978 retirement.ben_shared asks "shared among more than one beneficiary"]; residual is the combined_age help only | S help | **older-credits** by file (person.rmd_missed is the nearest hunk)
- BUG-0558 | retirement lows: box 5 omission, months range, Roth-to-Roth rollover box | real [U] | S | none
- BUG-0871 | ira_basis asks only own undeducted contributions | real [U] | S wording | none. **Upgrade candidate**
- BUG-0875 | beneficiary questions: former employee, death before annuity start | real [U] | S wording | none
- BUG-0878 | disability question; code 4 surviving spouse treating IRA as own | real [U] | S wording | none
- BUG-0881 | retirement/IRA wording lows (4 items) | real [U] | S wording | none
- BUG-0879 | ssb.any: repaid but received none answers No | real [U] | S wording | none
- BUG-0876 | sli.any: loan not named a student loan | real [C interview/2025/questions.yaml:4623 help unchanged] | S help | none

### Dependents, household, EIC (dependent, household, eic, f1040 refusals)

- BUG-0568 | dependent question wording lows (over-refusals, rare omissions) | real [U] | M (several entries) | **older-credits** by file (dependent bank)
- BUG-0729 | dependent.us_half military sentence names only you | **fixed** [C interview/2025/questions.yaml:2493 help reads "while you (or, on a joint return, your spouse) are abroad on military duty"] | — | closure
- BUG-0863 | marriage questions' help dropped federal marriage definitions | real [U] | S help | **older-credits** by file (household.credit_disallowed hunk)
- BUG-0864 | dependent.other_only_spouse help "another parent" | real [U] | S help | **older-credits** by file
- BUG-0765 | widowed-in-2025 remedy says a separate return is unsupported | real [C forms/2025/f1040.yaml:564-566] | S wording + one fixture's expected remedy | none (int-amt edits f1040.yaml by file, but a different area)
- BUG-0465 | zero-income return complete with four EIC inputs reachable | **fixed** [C forms/2025/eic.yaml:1206-1224 eic.eligible is now a choose on eic.reached_step5; C tools/interview_rules_baseline.json:3-6 early_completion holds no EIC input] | — | closure
- BUG-0606 | test-data defaults give contradictory birth-date answers | real [U] | M | int-amt by file (fixtures/2025/defaults.json); keep a separate commit
- BUG-0605 | two fixture cases refuse only because a default is untruthful | real [U] | S to M | none
- BUG-0753 | three class M cases rest on an impossible young dependent | real [U] | S (restate facts) | int-amt by file (classm.json); separate commit

### Schedule A, ftc election (sa, gift, ftc)

- BUG-0458 | sa.excluded_income asks PR exclusion only as a bona fide resident | real [C forms/2025/sa.yaml:180,183] | S wording | **older-scha-0817b** by entry (it edits sa.excluded_income)
- BUG-0924 | sa.excluded_income help steers 2024 foreign pay received in 2025 to No | real [U] | S wording | **older-scha-0817b** by entry. Fix with 0458
- BUG-0774 | ftc election denied to a qualifying Form 2555 filer | real [U] | M (new narrower input) | **older-scha-0817b** by input (reads sa.excluded_income); fix with 0458/0924
- BUG-0768 | Schedule A line 6 drops deductible noncreditable foreign tax | real [U] | M (input + refusal) | **older-scha** by file (sa.yaml)
- BUG-0801 | line 1 omits a would-be dependent's medical costs | real [U] | S wording | **older-scha** by file
- BUG-0802 | line 6 GST on income distributions not asked | real [U] | S to M (question + sa.unsupported) | **older-scha** by file
- BUG-0807 | land contract home not named as owned | real [U] | S help | **older-scha** by entry (sa.line5c hunk is its neighbour)
- BUG-0816 | personal property tax help: mixed weight/value fees | real [U] | S help | **older-scha** by file
- BUG-0818 | gift.deduction omits capital-gain-property reductions and right-to-use rule | real [U] | S wording | **older-scha** by entry (gift.deduction hunk)
- BUG-0819 | medical gate misses estate-paid costs for a decedent | real [U] | S help | **older-scha** by file
- BUG-0820 | sa.spouse_extra: blind definition, spouse died after 65 | real [U] | S wording | **older-scha** by file

### Schedule B, Schedule D, sales, capital loss carryover (sb, sd, sales, clcw)

- BUG-0509 | aggregate-eligibility "no corrections" unexplained | real [C interview/2025/questions.yaml:1674-1675 prompt says "you are correcting nothing"; forms/2025/sales.yaml:270] | S help | **int-p18** by entry (sales.aggregate_eligible reordered)
- BUG-0575 | broker basis not tied to box 1e; securities futures in wash sale | real [U] | S wording | **int-p18** by entry (sales.reported_basis, sales.wash_loss)
- BUG-0829 | gifted digital asset without donor records; unstated interest | real [U] | S wording | **int-p18** by entry (sales.correct_basis, sales.box)
- BUG-0835 | sale gate omits oil, gas or mineral property | real [U] | S wording | **int-p18** by entry (sd.sold_other)
- BUG-0184 | sd lines 4, 5, 11, 12 labels say "/carryover" screening | real [C forms/2025/sd.yaml:1622,1640,1703,1721] | S label (stales sd reviews, per the entry) | **int-p18** by file only (bank, not sd.yaml); best at sd.yaml's next real change
- BUG-0502 | carryover questions name only 1040/1040-SR | real [C interview/2025/questions.yaml:2190 help "Form 1040 or 1040-SR"] | S help | **int-p18** by family (sales block); otherwise quick-win lane
- BUG-0595 | sb.line8 misses an owner of a foreign trust who is not grantor/transferor | real [U]; owner decision 2026-11-10 to follow the printed line | M (needs i3520 archived) | none; pair with 0759
- BUG-0759 | sb.line8 clauses no archived page supports | real [U] | S to M (archive i3520, cite or drop clauses) | none; pair with 0595
- BUG-0831 | foreign-connection gates narrower than the questions they open | real [U] | S wording | **int-amt / inc-m34** by file (sb.ordinary_dividends hunks)
- BUG-0832 | bond help excludes CDs; nominee help joint only | real [U] | S help | **int-amt** by family (interest_dividends group)

### Investment, partnerships, S corporations, QBI (k1p, k1s, f7203, qbi, f8995)

- BUG-0839 | k1p fiscal-year partnership not asked | real [U] | M | none; fix with 0884
- BUG-0840 | k1p.t6 omits other capital-not-material service businesses | real [U] | S wording | none
- BUG-0844 | k1p box 1 nonpassive exceptions not screened | real [U] | M (tick + refusal) | none
- BUG-0845 | k1p basis, distribution, at-risk lows | partly addressed [C v2/int-n10.patch:9,15 new k1p basis and at-risk prompts]; residual (dist_over, item K1) real [I] | S | **int-n10** by entry
- BUG-0846 | k1p box question lows (STMT, K-3 on request, territory, 9b/9c, code Z) | real [U] | S to M | none
- BUG-0847 | k1p item G, LLC members, earlier-year tests | real [U]; needs owner decision | M | none
- BUG-0883 | k1s held-back box 2 loss routing; prior passive credits | real [U] | M | none
- BUG-0884 | k1s fiscal-year S corporation not asked | real [U] | M | none; fix with 0839
- BUG-0887 | k1s box questions: STMT and K-3 on request | real [U] | S wording | **int-n10** by file (k1s.past_years hunk)
- BUG-0888 | k1s.not_at_risk misses property, contributions, stop-loss, interested lender | partly addressed [C v2/int-n10.patch:71 new prompt: "money borrowed on terms that protect you from loss, or borrowed from another owner"]; property/contributions and a non-owner interested lender remain [I] | S | **int-n10** by entry
- BUG-0848 | Form 7203 question lows | real [U] | S help | none
- BUG-0849 | qbi.prior_form drops a pre-2024 carryforward | real [U] | S to M | none
- BUG-0100 | f8995 line 11 floored at zero (sign only, display) | real [C forms/2025/qbi.yaml:254-259 NonNegDollars, subtract_floor0] | S (type + fixture) | none
- BUG-0654 | 2026: sc material participation admits oil/gas exception the minimum QBI deduction does not | real, 2026 only [U] | S, at 2026 adoption | none

### Foreign tax, NIIT (f1116, f1116sb, ftc, f8960)

- BUG-0827 | foreign tax carryover through a deduction/election year not reduced | real [U] | M | none
- BUG-0834 | f1116 screens miss a loss account without a form; smaller carryback | real [U] | S wording | none
- BUG-0912 | f1116 line 18 shown when line 17 is zero or less | real [C forms/2025/f1116.yaml f1116.line18 has no shown_when] | S (shown_when helper) | none
- BUG-0828 | 6013(g) joint return NIIT without the election | real [U] | S (help on scope.nonresident) | **inc-m12** by file (scope.yaml)
- BUG-0560 | f8960.prior_2i help ties the adjustment to 2024 NIIT | real [U] | S help | none

### Payments, refunds, AMT, Schedule 2 and 3 (f1040, refund, rec, s2, s3, f8853c)

- BUG-0894 | MFS: how to divide joint estimated payments | **fixed by inc-m34 when it lands** [C patches/inc-m34.md:75,88,223] | — | **inc-m34**: record the closure with it
- BUG-0898 | other-withholding help omits Forms 8805 and 8288-A | real [C interview/2025/questions.yaml:625 help names K-1 and 1042-S only; the form source at forms/2025/f1040.yaml:885-887 already names both] | S help | **inc-m34** by entry (paid_already group, f1040.estimated_any)
- BUG-0570 | refund election amounts unbounded; line 3a builder wording | real [U] | S (wording) + M (bound) | **int-amt** by entry (f1040.line3a bank hunk) and **inc-m34** (f1040.line35a hunk)
- BUG-0895 | state refund worksheet used for a 2024 dual-status alien | real [U] | S wording (one bullet) | **inc-m34** by family (refund.itemized hunk; refund.exc_who at questions.yaml:4021)
- BUG-0821 | s2.lookback asks only a contract finished in 2025 | real [U] | S wording | **inc-m34** by file (s2.yaml)
- BUG-0826 | s2.options_any only "from an employer" | real [U] | S wording | **inc-m34** by file (s2)
- BUG-0680 | s2 HSA testing-period question misstates the IRA transfer period | real [U] | S wording | **inc-m34** by file (s2)
- BUG-0764 | AMT screen takes line 7 at 26/28% at zero taxable income (over-refusal) | real [C forms/2025/s2.yaml:688-697 choose on f1040.gate.qdcg_applies] | S expr + M fixture | **inc-m34** by file (s2.yaml, amt_boat / amb.amt_transient); also kills two 0656 mutants
- BUG-0656 | 83 surviving mutants of the goal-1 round | real [U] | L (mutation lane) | none. **Upgrade candidate**
- BUG-0916 | f8853c line 22 narrows qualified LTC services | real [U] | S wording | **inc-m34** by file (v2 edits forms/2025/f8853c.yaml)
- BUG-0917 | f8853c line 25 floor without a registered reading | real [U] | S (ambiguity entry) | **inc-m34** by entry (it adds amb.2025.f8853c_line24_public beside it)
- BUG-0923 | f8853c entry question and line 17: assigned per diem payments | real [U] | S help | **inc-m34** by entry (f8853c.line17 hunk)
- BUG-0761 | s3 line 7 says every line 6 credit is refused there (8978) | real [U] | S (refuses entry) | none
- BUG-0620 | credit questions that replaced the credits screen: length, placement, 3 wide refusals | real [U] | L | none

### Credits (f2441, f5695, f8962, f1095a, f8889, f8863)

- BUG-0681 | f2441 asks again whether the spouse died | real [C forms/2025/f2441.yaml:114 f2441.spouse_died still an input] | M (derived line + fixture restatement) | none
- BUG-0760 | f2441 line 2 box uses dc.providers_listed | real [C forms/2025/f2441.yaml:388,597; params/2025.yaml:1394 has no persons_listed] | S (param + expr, no value change) | none
- BUG-0799 | f2441 benefits gate omits spouse's business, partnership, disabled spouse; MFS spouse "loss" | real [U] | S wording | none (possible upgrade)
- BUG-0554 | f5695 "all other"/"such" questions lean on the preceding one | real [U] | S wording (8 entries) | **older-credits** by file (f5695 bank)
- BUG-0555 | f5695 Part II lows | partly fixed by older-credits [C v2/older-credits.patch: line 21a prompt now "lived in during 2025"; panel tick "put in in 2024 or 2025"]; audit timing, door ranking, overlap remain [I] | S | **older-credits** by entry
- BUG-0794 | f5695 line 18a: structural or finished-surface components | real [U] | S help | **older-credits** by file
- BUG-0386 | backlog-round lows umbrella (asset, f5695, ltc, s1, sales, household, dc_count, sc, scveh) | real [U] (T-211) | per item | split: f5695 #3-6 -> older-credits; sales #2/#3 -> int-p18; asset -> sche-a; ltc -> inc-m34 (f8853c)
- BUG-0504 | year-of-marriage question refuses some ineligible filers | real [U]; but see 0690 | M | none; pair with 0690
- BUG-0690 | 0504's fix would expose unmodeled column (b) / line 10 rules | real [U]; owner decision | M | none
- BUG-0770 | f8962 columns (a), (b) shown for a separate filer without Exception 2 | real [U] | S (shown_when helpers on 26 lines) | none
- BUG-0798 | f8962 "immigrant"; MFS abuse help partial list | real [C interview/2025/questions.yaml:3493 "lawfully present immigrant"] | S wording | **older-credits** by entry family (f8962.estimate_100 hunk)
- BUG-0532 | 1095-A VOID question names only an original | **fixed by the redraft** [C interview/2025/questions.yaml:2851 "did the Marketplace later send another form, marked VOID or CORRECTED, for the same plan"] | — | closure
- BUG-0092 | f8889 tests marital status by filing status | **fixed** [C forms/2025/f8889.yaml:1024-1040, 1107-1121 read household.married] | — | closure (draft already in patches/older-ny.md:135)
- BUG-0874 | f8889 then-spouse question tense; MFS spouse HSA present tense | real [U] | S wording | none
- BUG-0877 | f8889 lows: 2% S corp HSA; LTC premium limit; rollover HSA date | real [U] | S help | none

### New York (forms/ny/2025, interview/ny/2025)

- BUG-0852 | SCRA elections not asked of MFS civilian spouse, PHS, NOAA | real [U] | M (new NY question) | **older-ny** by file
- BUG-0853 | NY estimated-tax gate and late-installment wording | real [U] | S wording | **older-ny** by file
- BUG-0854 | NY use-tax question own purchases only | real [U] | S wording | **older-ny** by file
- BUG-0855 | NY special accrual question wording | real [U] | S wording | **older-ny** by file
- BUG-0856 | NY real property credit question | real [U] | S wording | **older-ny** by file
- BUG-0857 | NY out-of-state bond gate reads federal line 2a (net of premium) | real [U] | S to M | **int-amt** by input (it re-gates f1040.tax_exempt_interest) and older-ny by file
- BUG-0858 | NY U.S.-obligation list and heading | real [U] | S wording | **older-ny** by file
- BUG-0859 | NY inflation-check gate reads only Schedule 1 line 9 | real [U] | S (gate expr) | **older-ny** by entry family (gov_pension gate hunks)
- BUG-0860 | NY public-job question: work vs W-2 from public employer | real [U] | S wording | **older-ny** by entry (gov_pension hunk)
- BUG-0762 | NY household credit MFS gates test this return's AGI only | real [U] | M (question + gate) | **older-ny** by file. Possible upgrade
- BUG-0763 | IT-2 boxes 17a and NYC 19 shown $0 | real [U] | S (shown_when) | **older-ny** by file (ny_it2 not touched; weak)
- BUG-0750 | NY W-2 record lacks the W-2c box | real [U] | S | **older-ny** by file (weak)
- BUG-0424 | first NY reviews' lows umbrella | real [U] (T-244) | per item | **older-ny**

### Engine, tools, tests, year change

- BUG-0079 | refusal can wait behind an unknown operand (binary atoms) | real [U] | M (both evaluators + property test) | none
- BUG-0625 | server test connection reset under load | real [U] | M (diagnosis) | none
- BUG-0800 | screen/false-no prompts state a false-gate's polarity backwards | real [U] | S (tool) | none
- BUG-0757 | slice interview profiles still built (closes 0432) | **done** [C interview/2025/ has no social-security.yaml, sales.yaml, stage4.yaml]; listed open only because its result is in a `Resolution:` field, which tools/bug_status.py:72 reads as a proposal | — | closure (bookkeeping)
- BUG-0647 | 2026 TCW joint 12% row | **done as a 2026 operation** [C changes/2026/tcw.yaml:6 `change: BUG-0647`]; open because `Year change:` is not a fix field (tools/bug_status.py:71) | — | closure (bookkeeping), or leave open until 2026 adoption if the owner prefers

## 2. By drafted patch (what each patch could carry)

- **v2/sche-a.patch**: 0776, 0777, 0778, 0779, 0782, 0783, 0784, 0785, 0786, 0787, 0788, 0925 (rental); 0889, 0922
  (royalty); 0565, 0791 (asset); 0812 (s1.nol_amount); closes 0781. Wording ones are S; 0778, 0779, 0889 are M.
- **v2/int-n10.patch**: 0772, 0926 (rental days), 0845, 0888 residuals, 0887, 0891. Note sche-a.md's warning that
  int-n10's rental.not_at_risk prompt conflicts with sche-a; settle that first.
- **v2/inc-m12.patch**: 0809, 0811, 0813, 0814, 0804, 0823, 0824, 0825 (s1 gates); 0719, 0771, 0795, 0828, 0902,
  0903, 0909, 0910 (scope); 0865, 0866, 0868, 0872 (person); 0915 (tips).
- **v2/inc-m34.patch**: 0898, 0570 (line 35a part), 0895, 0908, 0821, 0826, 0680, 0764 (s2), 0916, 0917, 0923
  (f8853c); closes 0894.
- **v2/older-credits.patch**: 0554, 0555, 0794 (f5695); 0568, 0863, 0864, 0867 (dependent/household); 0869;
  0798 (f8962); 0508 (help only).
- **v2/older-scha.patch / older-scha-0817b**: 0458, 0924, 0774 (sa.excluded_income family); 0768, 0801, 0802,
  0807, 0816, 0818, 0819, 0820.
- **v2/older-ny.patch**: 0852 to 0860, 0762, 0763, 0750, 0424; record 0092 closure (already drafted).
- **v2/int-p18.patch**: 0509, 0575, 0829, 0835, 0502, 0386 (sales items).
- **v2/int-amt.patch**: 0570 (line 3a part), 0832, 0831, 0857 (interaction), and by file only 0606, 0753.
- **No patch** (wait for the form's next change, or the quick-win lane): k1p/k1s structural (0839, 0844, 0846,
  0847, 0883, 0884), 0840, 0848, 0849, 0100, f1116 (0827, 0834, 0912), 0560, f8889 (0874, 0877), retirement
  (0558, 0871, 0875, 0878, 0881), 0876, 0879, sc/scveh/carloan (0530, 0559, 0780, 0792, 0515), f8962 (0504,
  0690, 0770), f2441 (0681, 0760, 0799), s3 (0761, 0620), 0765, 0892, 0595, 0759, 0184, 0605, engine and tools
  (0079, 0625, 0800, 0656), 2026 (0654, 0734), 0713.

## 3. Closure candidates (with evidence)

| Entry | Evidence | Kind |
|---|---|---|
| BUG-0092 | f8889.married_family and f8889.age55_unmarried now read household.married [C forms/2025/f8889.yaml:1024-1040, 1107-1121]. Closure text already drafted in patches/older-ny.md:135-150 | fixed |
| BUG-0465 | eic.eligible is a choose on eic.reached_step5, not an `all` [C forms/2025/eic.yaml:1206-1224]; the interview-rules baseline's early_completion holds only sa.elect_itemize and person.work_ssn [C tools/interview_rules_baseline.json:3-6] | fixed (gate wave) |
| BUG-0532 | the redrafted prompt names "another form, marked VOID or CORRECTED, for the same plan" [C interview/2025/questions.yaml:2851] | fixed (redraft) |
| BUG-0729 | dependent.us_half help includes "(or, on a joint return, your spouse)" in its military sentence [C interview/2025/questions.yaml:2493] | fixed (redraft) |
| BUG-0757 | the profiles are gone [C ls interview/2025/]; the entry is open only because `Resolution:` is a proposal field [C tools/bug_status.py:72] | bookkeeping: add `Tool change:` or a closure record |
| BUG-0647 | changes/2026/tcw.yaml:6 carries `change: BUG-0647`; `Year change:` is not a fix field [C tools/bug_status.py:71] | bookkeeping; owner may prefer to keep it open until the 2026 adoption |
| BUG-0893 | s1.line8u and s1.inmate_amount no longer exist [C forms/2025/s1.yaml, 0 matches]; BUG-0766's Fix reverted line 8u | obsolete (premise removed; the compute case is TASKS T-336) |
| BUG-0894 | fixed in the inc-m34 patch's line 26 help [C patches/inc-m34.md:88,223] | close when inc-m34 lands |
| BUG-0781 | v2/sche-a.patch rewrites rental.not_at_risk to cover guarantees, stop-loss and a lender with a stake [C v2/sche-a.patch] | close when sche-a lands (sche-a.md does not name 0781; add it) |

Near-closures, not proposed: BUG-0508 (retirement.ben_shared now asks the shared-pension case [C
forms/2025/retirement.yaml:978]; only the combined_age help is left), BUG-0555, BUG-0845, BUG-0888 (partly fixed by
drafted patches; close in part at landing).

## 4. Quick-win batch (S effort, wording only)

Rule: the project's lows wait for the form's next substantive change. So the batch is split.

**4a. Ride with a patch by entry (fold into that patch's lane; no extra review round):**
- sche-a: 0776, 0777, 0782, 0783, 0784, 0785, 0786 (one tick), 0787, 0788 (citation), 0922, 0925
- int-n10: 0772, 0926
- inc-m12: 0809, 0823, 0824, 0825
- inc-m34: 0898, 0917 (ambiguity entry), 0923
- older-credits: 0555 residual, 0869
- older-scha / 0817b: 0458, 0924, 0807, 0818
- int-p18: 0509, 0575, 0829, 0835

**4b. Ride by file only (same form's reviews rerun anyway):** 0811, 0813, 0814, 0804, 0719, 0771, 0902, 0903,
0909, 0910, 0865, 0866, 0868, 0872, 0915, 0828 (inc-m12); 0821, 0826, 0680, 0895, 0908, 0916 (inc-m34); 0554,
0794, 0863, 0864, 0867, 0798 (older-credits); 0801, 0816, 0819, 0820 (older-scha); 0853 to 0856, 0858, 0860
(older-ny); 0812 (sche-a); 0891, 0887 (int-n10); 0502 (int-p18); 0832 (int-amt).

**4c. No patch: one quick-win lane if the owner wants them before the forms change (else they wait):**
0780 (sc.special), 0792 (scveh help), 0876 (sli help), 0879 (ssb.any), 0871, 0875, 0878, 0881 (retirement and IRA
wording), 0874, 0877 (f8889), 0799 (f2441), 0840 (k1p.t6), 0848 (f7203 help), 0834 (f1116 wording), 0560
(f8960 help), 0892 (sche.re_pro help), 0765 (remedy text + one fixture expected value). These span about 9 forms. By
the cost rule each needs that form's review rerun, so this lane makes about 9 review rounds for lows. The rule
argues against running it now. The exceptions are 0871 (if upgraded) and 0765, which is a wrong remedy on a reachable
refusal.

Non-wording S items that are safe and cheap but not wording (no value change): 0760 (param), 0912 (shown_when),
0770 (shown_when), 0763 (shown_when), 0184 (label), 0100 (type + fixture).

## 5. Upgrade to medium

- **BUG-0656** (no severity). Its own Workaround says "the federal mutate step fails until each is killed or
  explained" [U, relayed]. If mutate is a release gate, this blocks a release and is not a low. Check whether
  the 83 survivors are now held in a baseline. BUG-0764's fix kills two of them.
- **BUG-0795** (low). Treaty-exempt income is neither asked nor refused, so it stays in wages, AGI and earned
  income (Schedule 8812 and EIC readers). It is amount-affecting, and the population (students, researchers and
  teachers on treaties) is not vanishingly rare. A refusal is M effort and rides with inc-m12 (scope.yaml).
- **BUG-0871** (low). After-tax money rolled from a work plan into a traditional IRA is a common pattern. Read as
  No, it makes the whole distribution taxable. It is amount-affecting and the fix is S wording.
- **Possible:** BUG-0762 (NY MFS household credit at zero, amount-affecting, rare), and BUG-0799 (dependent care
  benefits from the filer's own business or partnership not counted, amount-affecting).
- **Keep low:** 0764 (over-refusal only) and 0828 (rare).

## 6. Limits

- Most "real" verdicts are **[U]**: an entry dated 2026-11-15 or later is taken as current. Only about 25 entries
  were spot-checked against files, with priority on the older ones (2026-10-22 to 2026-11-10). The interview redraft
  (2026-11-13) landed after those and could have fixed them silently. Of the 11 older entries checked, 3 were fixed
  (0092, 0465, 0532, plus 0729 from the newer set). Not every old wording low was checked: 0515, 0530, 0554,
  0555, 0558, 0559, 0560, 0565, 0568 and 0575 are worth a two-minute check each against the redrafted bank before
  they are scheduled.
- "Ride" pairings come from the ids each v2 patch's hunks touch (parsed from the patches). The patches' content was
  not re-reviewed.
