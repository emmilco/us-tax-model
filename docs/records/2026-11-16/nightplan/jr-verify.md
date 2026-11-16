# jr-verify: screen and false-no rulings on the 7 candidate findings of judgment-records.md

Lane jr-verify. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16.
Read only; nothing in the repository changed; no paid calls, no walks, no engine runs.
Paths relative to the xint worktree. `Q:` = `interview/2025/questions.yaml`. [C path:line] = checked against that
file; [I] = inferred or this lane's judgment.

## Summary

| # | Candidate | Ruling | Severity | Already an entry? |
|---|---|---|---|---|
| 1 | `household.community_property` asks residence; rule is each spouse's domicile | **REAL** | **medium** | No (BUG-0519 item 4 / BUG-0732 is the opposite side, the over-refusal). The ambiguity `amb.2025.mfs_community_property` covers only the over-refusal side and its text is now stale |
| 2 | `scope.recovery` tick verb reads as the filer paying | **REAL** | low | No. BUG-0640 (fixed source wording) and BUG-0908 (help's 2024 test) are siblings, not duplicates. The release screen review saw only the source sentence, not the tick |
| 3 | `sa.dependent` Yes now computes and has no guard | **REAL** | low | No |
| 4 | `f1040.digital_assets` prompt counts a gift or inheritance received as a Yes | **REAL** | low | No. BUG-0896 (medium, open) is the false-No side of the same bank entry; the fixes should land together |
| 5 | `sche.qbi_business` tick drops the safe-harbor example | **REAL** | low | No bug entry. `/tmp/nightplan/interview.md:336` already proposes moving the example to help |
| 6 | Cost-20 questions (`f1116sb.prior_year`, `f1116col.div_income`, `person.mw_earned`) | **NOT A DEFECT** | — | Effort ratings belong to T-334; `mw_earned`'s compute-both-ways is an owner decision already recorded |
| 7 | Estranged spouses under one roof at `household.mfs_living` | **REAL (low), with a residual ambiguity** | low | No. `amb.2025.mfs_lived_apart` covers temporary absences only |

- **BUG-0519 item 4: no Reopens entry needed.** BUG-0732 kept the `cp_married` over-refusal because "Pub. 555 ... is
  not archived". That reason no longer holds, but Pub. 555 confirms the outcome: it does not make the
  spouse-outside case computable (details below). The new entry for candidate 1 records the corrected reason.
  Nothing needs reopening.
- Draft pending entries for 1, 2, 3, 4, 5 and 7 are below, in the format of BUG-0923 to BUG-0926 (`Proposed fix:`
  per tools/README.md:767-768). The rulings come from reading only. No walk confirmed reachability.

---

## Candidate 1 (priority): `household.community_property`. REAL, medium

**What the filer sees** [C Q:2701-2707]:
> prompt: "At any time in 2025, did you live in Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas,
> Washington or Wisconsin?"
> help: "In these nine states a married couple's income belongs to both of them by law (community property). If you
> are married and file apart from your husband or wife, a Yes ends the interview here."

The form source says the same thing: "Did you live in a community property state ... at any time in 2025?"
[C forms/2025/household.yaml:669-678].

**Readers** [C household.yaml]: three refusals read this one answer:
- `household.mfs_community_property` (MFS: `then: household.community_property`) [C :1755-1795]
- `household.hoh_cp_married` (HOH, married at year end) [C :680-702]
- `household.cp_not_joint` / `cp_unmarried` (marriage ended in 2025) [C :1460-1510]

**Source** (Pub. 555, now in xint as `sources/2025/p555.*`, status A in git):
- "The law of the state, or the law of the foreign country, where you are domiciled will determine if you have
  community property, community income, or both. If you and your spouse (or your RDP) have different domiciles,
  check the laws of each to see if you have community property, community income, or both." [C p555.cols.txt:57]
- "Your domicile is a permanent legal home that you intend to use for an indefinite or unlimited period, and to
  which, when absent, you intend to return. ... The amount of time spent in one place doesn't always explain the
  difference between home and domicile." [C p555.cols.txt:57-59, 62]
- "Active military pay earned while married and domiciled in a community property state is also community income.
  This income is considered to be received half by the member of the Armed Forces and half by the spouse."
  [C p555.cols.txt:144]

**False-No readings.**
- (a) **The filer's own domicile is in a community property state, but the filer lived elsewhere all of 2025.** The
  paradigm case is a Texas-domiciled servicemember stationed in Virginia, or that servicemember's spouse. Another is
  a Californian on a long work assignment abroad. Asked where they "live", such a filer truthfully answers No. The
  help speaks only of "these nine states" and never says domicile counts. Pub. 555 line 144 makes the military pay
  community income, half reported by each spouse. On MFS the return is now computed (before the expansion every MFS
  return was refused), so the separate return reports the whole of the filer's pay and none of the spouse's half. The
  result is a wrong completed return. The same false No escapes the HOH-married and marriage-ended refusals; they
  are siblings with the same defect, but each is reached only by a married-apart or recently divorced filer.
- (b) **The filer was never domiciled in a CP state, but the spouse was.** Pub. 555 says to "check the laws of each".
  The tool cannot do that, and the question never asks about the spouse. Spouses who lived apart all year and meet
  the four conditions disregard community law for earned income (p555.cols.txt:207-227), but community income from
  property is still split ("their share of the interest income from community property", :227). So refusing is the
  consistent treatment. As built, the case is computed silently.

**False-Yes reading (not a defect).** A servicemember or student who is domiciled elsewhere and lives in a CP state
answers Yes and is refused. `amb.2025.mfs_community_property` already records this over-refusal as accepted: "'Lived
in' is broader than 'domicile': a filer who lived in one of the states only temporarily is refused too, which errs
toward refusing (... D1 ...)" [C ambiguities/2025.yaml:1469-1472]. It stays.

**Ambiguity entry.** `amb.2025.mfs_community_property` [C ambiguities/2025.yaml:1458-1476] covers only the
over-refusal side, and its `text_at_issue` says "Pub. 555 and Form 8958 are not archived". Both are now in
`sources/2025/` (`p555.*`, `f8958.*`) [C ls]. The under-refusal side has no entry. No reading of the source makes a
domiciled filer's community income disappear because the filer lived elsewhere, so this is a defect, not an
ambiguity.

**Severity: medium.** It produces a wrong completed return with no refusal, but only for a narrow population: MFS is
about 2 to 3% of returns [I, judgment-records.md:207], and within it a domicile/residence split is uncommon. That is
about the same scale as the other MFS mediums (BUG-0899, BUG-0907).

**Dup check.** `grep -i domicil BUG_INVENTORY.md` finds only New York residence entries (:7164, :9411, :10477)
[C]. `grep -i community` finds BUG-0220, BUG-0255, BUG-0278 and BUG-0519/0732, none on domicile [C]. No hits in
`/tmp/nightplan/med-*.md` [C grep] or `bug_pending/` [C].

### BUG-0519 item 4: is a Reopens entry needed? No.

BUG-0519 item 4 reads "household.cp_married (a spouse living outside the state; over-refusal)" [C
BUG_INVENTORY.md:6940]. BUG-0732 closed BUG-0519 and left item 4 unchanged: "whether that spouse's income is
community income turns on Pub. 555, which is not archived, so the refusal stays (a recorded over-refusal, low)" [C
:9193]. Read now, Pub. 555 keeps that refusal in place:
- Different domiciles mean "check the laws of each" (:57). The tool has no state-law rule to apply.
- Spouses who lived apart all year and meet the four conditions (:207-215) still split community income from
  property (:227). Spouses who do not meet them "must treat your income according to the laws of your state" (:228).
- After the community ends, each spouse is "taxed on half the community income for the part of the year before the
  community ends" (:236). That is exactly the period `cp_married` asks about.

The disposition (over-refusal kept) is therefore still right. Only its stated ground is stale. A `Reopens:` field
would reopen the entry for a fix that the source does not support. The proposed entry below instead records the
corrected ground in its Source and Symptom. If the coordinator prefers a separate record, a `Closure=won't fix`
closure of the item is possible, but the item is already closed (by BUG-0732), so I recommend against it.

### Draft pending entry (candidate 1)

```
## BUG-NEW-<PREFIX>-<NN> — household.community_property asks where the filer lived, but community income turns on each spouse's domicile; a separate return is computed without the split

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 1), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p555 p. 2, Domicile, "The law of the state, or the law of the foreign country, where you are domiciled will determine if you have community property, community income, or both. If you and your spouse (or your RDP) have different domiciles, check the laws of each"; "Your domicile is a permanent legal home that you intend to use for an indefinite or unlimited period, and to which, when absent, you intend to return"; p555 p. 5, Military retirement pay, "Active military pay earned while married and domiciled in a community property state is also community income. This income is considered to be received half by the member of the Armed Forces and half by the spouse."
- **Symptom:** The interview prompt of household.community_property asks "At any time in 2025, did you live in Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?" and its help speaks only of the nine states. A married filer domiciled in one of them who lived elsewhere all of 2025 (a servicemember on orders, or that servicemember's spouse; a long assignment abroad) answers No, and a filer whose spouse alone is domiciled in one is never asked about the spouse. On a separate return household.mfs_community_property is then false and the return is computed from the filer's own income with no community-income split (Form 8958): a wrong completed return. The same answer escapes household.hoh_cp_married and household.cp_not_joint. The opposite case (lived in a state while domiciled elsewhere) is refused, as amb.2025.mfs_community_property accepts. Pub. 555 is now archived; it confirms rather than removes the over-refusal kept in BUG-0732 item (4) (different domiciles: "check the laws of each"; spouses apart all year still split community income from property, p555 p. 8), so that item is not reopened. Not executed; read from the question and the source.
- **Where:** forms/2025/household.yaml household.community_property (label, source, cite); interview/2025/questions.yaml household.community_property (prompt, help); a new input beneath it; household.mfs_community_property, household.hoh_cp_married, household.cp_not_joint (readers); ambiguities/2025.yaml amb.2025.mfs_community_property (text_at_issue says Pub. 555 and Form 8958 are not archived).
- **Proposed fix:** (1) household.community_property prompt: "At any time in 2025, did you live in, or have your permanent home in, Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?"; help, first sentence added: "Your permanent home is the state you mean to return to when away, for example the state you keep as home while on military orders elsewhere." Label and source to match; cite p555 p. 2, Domicile. (2) A new input household.spouse_cp_domicile, asked only when married, not filing jointly and household.community_property is No: "Was your husband or wife's permanent home (the state they mean to return to) in one of those states at any time in 2025?" with help "Community income then depends on the law of each of your states (Pub. 555). A Yes ends the interview here."; the three readers refuse on it as on household.community_property. (3) amb.2025.mfs_community_property: text_at_issue drops "Pub. 555 and Form 8958 are not archived", cites p555 p. 2, Domicile. Coverage rows: an MFS filer domiciled in Texas living in Virginia (refused), an MFS filer whose spouse is domiciled in California (refused), an MFS filer in Oregon with spouse in Oregon (computed). Reviews due: question and screen reviews of household.community_property and the new input; transcription of household.
- **Proposed fix lines:** household.community_property, household.spouse_cp_domicile (new), household.spouse_cp_domicile_if_apart (new gate), household.mfs_community_property, household.hoh_cp_married, household.cp_not_joint
- **Severity:** medium
- **Tags:** screen; false-no; community-property; married-filing-separately; household
```

Notes on the fix [I]:
- (1) adds refusals only. It also catches the HOH and marriage-ended cases, which is the correct direction by
  p555:57.
- An alternative is to ask domicile only, which would remove the accepted over-refusal. It would undo design D1 and
  ask a harder question of all 23% of Yes filers. I do not recommend it without the owner.
- The new child's N3 cost is small: it is asked only of non-joint married filers who answered No, and one tick
  refuses.
- Exact gate ids are a sketch. Gate naming follows the `_if_` pattern of `cp_married_if_ever_married`.

---

## Candidate 2: `scope.recovery` tick. REAL, low

**Filer sees** [C Q:54-55, 2000-2005]: the heading "Did any of these happen to you (or, on a joint return, your
spouse)?", then the tick "Paid back a deduction or credit that lowered tax (not state/local refund)". The help
(optional; N10) gives as examples "a refund of property tax, mortgage interest refunded (Form 1098 box 4), or a
medical bill repaid by insurance".

**Source** [C forms/2025/scope.yaml:849-852]: the source asks "were you ... paid back an amount whose deduction or
credit ... lowered your tax". p525 p. 24: "A recovery is a return of an amount you deducted or took a credit for in
an earlier year".

**Ruling.** Under "happen to you", a tick that starts with the verb reads as something the filer did. "Paid back a
deduction" then means the filer repaid something, which is the opposite flow. The same bank uses "Paid back more
than $3,000 of income from an earlier year" (Q:1232, `s3.repaid_income`) [C] for the filer's own repayment. Two
readings follow:
- A false No: a property-tax refund recipient skips the tick, so the recovery is left out of line 8z and the
  completed return is wrong.
- A false Yes: a repayer ticks it, which costs 3 to 5 steps and probably an unneeded refusal at `rec_rare`.

The source sentence is passive and right; only the tick lost the passive voice. The release screen review of
`gate:scope.recovery` was shown the source sentence, not the tick [C
.transcription/screens/gate_scope.recovery.prompt.txt:15]. Its response even flagged "or even as the filer repaying
someone" for "paid back" [C .transcription/screens/gate_scope.recovery.0c93e1a2c867.1.response.txt:19]. BUG-0908
took that response's findings 0, 5 and 6, not this one. That tick labels, not prompts, are what a filer sees in a
tick group is [I] from the group structure.

**Severity low.** The help's examples point the right way, and a recovery also needs a 2024 itemized deduction.

```
## BUG-NEW-<PREFIX>-<NN> — scope.recovery: the tick "Paid back a deduction or credit" reads as the filer paying, the opposite of a recovery

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 2), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p525 p. 24, Recoveries, "A recovery is a return of an amount you deducted or took a credit for in an earlier year".
- **Symptom:** Under the heading "Did any of these happen to you (or, on a joint return, your spouse)?" the tick of scope.recovery reads "Paid back a deduction or credit that lowered tax (not state/local refund)", which reads as something the filer paid; the label and source ("were you ... paid back an amount") are passive and right. The same tick group's sibling bank uses "Paid back more than $3,000 of income from an earlier year" (s3.repaid_income) for the filer's own repayment. A filer who got a property tax or mortgage interest refund can leave it unticked, so the recovery is left out of Schedule 1 line 8z; a filer who repaid income can tick it and be refused at rec_rare without need. The release screen review read the source sentence, not the tick. Not executed; read from the bank.
- **Where:** interview/2025/questions.yaml input scope.recovery (tick, order 161, seq 6, group money_b).
- **Proposed fix:** Tick: "Got money back for something you deducted or took a credit for (not a state/local income tax refund)". No change to the label, source or help. Reviews due: the tick-group render of money_b (tick length) and the next sampled screen review of gate:scope.recovery, shown the tick.
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-no; wording; tick; recovery
```

Note: the proposed tick is 17 words. Check it against the tick length norm before landing [I; the norm was not
read in this lane].

---

## Candidate 3: `sa.dependent`. REAL, low

**Filer sees** [C Q:1283-1288]:
> "Can a parent or anyone else claim you (or, on a joint return, your spouse) as a dependent on their 2025 return?"
> help: "It is whether they can, not whether they do. Answer No if that person need not file a return and files none,
> or files only to get back tax withheld."

**What a Yes now does.** It no longer refuses (`docs/provisional/lanes/x2-dep.md:28-31` [C]). It now drives:
- the limited standard deduction (`sa.dep_*`) [C x2-dep.md]
- the EIC's `eic.step4` false [C forms/2025/eic.yaml:918, 960-968]
- the saver's credit student test [C forms/2025/person.yaml:3772]
- the dependent and f2441 tests [C dependent.yaml:965, f2441.yaml:288]
- `f8962.dependent_filer` (a refusal) [C f8962.yaml:57]

**Source.** p501: "If your gross income was $5,200 or more, you usually can't be claimed as a dependent unless you
are a qualifying child" [C sources/2025/p501.cols.txt:131]; the qualifying relative gross income test is "less than
$5,200" [C :518, :755].

**Ruling.** The question asks for a legal conclusion and its help gives none of the tests. Before the expansion a
wrong Yes was harmless in effect, because it led to a refusal. Now it reduces the deduction and denies credits:
- A filer aged 19 to 23 who supports themselves, or an adult relative earning $5,200 or more, can believe a parent
  "can" claim them and answer Yes.
- The deduction effect bites only when earned income plus $450 is below the standard deduction and there is unearned
  income [I].
- EIC and saver's-credit losses do not depend on that.

The wrong-No direction (a claimable student answering No) is older and was already computed. Severity low: the
printed Form 1040 question is the same sentence, and the help's first line addresses the common confusion.

```
## BUG-NEW-<PREFIX>-<NN> — sa.dependent: a Yes now limits the standard deduction and denies credits, and the help gives none of the tests that decide whether someone can claim the filer

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 3), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** p501 p. 5, "If your gross income was $5,200 or more, you usually can't be claimed as a dependent unless you are a qualifying child"; p501, Qualifying Child (age test: under 19 at the end of the year, or under 24 and a student; the support test) and Qualifying Relative (gross income less than $5,200; more than half of support).
- **Symptom:** sa.dependent asks "Can a parent or anyone else claim you (or, on a joint return, your spouse) as a dependent on their 2025 return?" with help only on "can, not do" and on a person who need not file. A Yes no longer refuses: it computes the dependent standard deduction worksheet (sa.dep_*), makes eic.step4 false, enters the saver's credit student test and refuses Form 8962 (f8962.dependent_filer). A filer aged 19 to 23 who pays over half their own support, or an adult with gross income of $5,200 or more who is no one's qualifying child, can answer Yes, limiting the deduction (where earned income plus $450 is below it and there is other income) or losing the earned income or saver's credit. Not executed; read from the question and the source.
- **Where:** interview/2025/questions.yaml input sa.dependent (help).
- **Proposed fix:** Help, added after the first sentence: "Someone can claim you only if you are their qualifying child (for example, under 19 at the end of 2025, or under 24 and a full-time student, who lived with them over half the year and did not pay over half of your own support) or you had gross income under $5,200 and they paid over half of your support." Check each clause against p501 Table 2 before landing. Reviews due: question and screen reviews of sa.dependent.
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-yes; wording; dependent-filer
```

[I] The help sketch is about 60 words, long by N10 and probably over the redraft's help length. A child question
("Are you under 24 and were you a student ...?") is the costlier alternative. The candidate left this choice to the
owner's walk, and so do I.

---

## Candidate 4: `f1040.digital_assets`. REAL, low

**Filer sees** [C Q:3894-3900]:
> prompt "In 2025, did you (or, on a joint return, your spouse) receive, sell, trade, spend or give away crypto or
> another digital asset?"
> help "Buying crypto with dollars and holding it, or moving it between your own wallets, is a No. Being paid in
> crypto, swapping one coin for another, or paying for something with it is a Yes."

The form label keeps the qualifier: "receive a digital asset (as a reward, award, or payment for property or
services)" [C forms/2025/f1040.yaml:18-22].

**Source** [C sources/2025/i1040gi-html.txt:1275]: "Check the 'Yes' box ... if at any time during 2025, you (a)
received (as a reward, award, or payment for property or services); or (b) sold, exchanged, or otherwise disposed of
a digital asset". Its examples list receipts only as payment, reward or award, mining or staking, and a hard fork
[C :1276-1284].

**Ruling.** The prompt drops the parenthetical, so a gift or inheritance received alone answers Yes. The effect is the
printed Digital Assets box shown as Yes when the instructions call for No, plus one step (`s1.digital_income`). No
tax changes (`s1.digital_amount` help: "A gift or an inheritance of crypto is not income", Q:3911 [C]). "Give
away" is rightly a Yes (a disposition).

**Dup check.** BUG-0896 [C BUG_INVENTORY.md:10915-10925] is the false-No side of the same help and is still open,
with a proposed help rewrite; `/tmp/nightplan/med-income.md:315-340` drafts its patch. They are distinct defects on
one bank entry, so they should land in one change.

```
## BUG-NEW-<PREFIX>-<NN> — f1040.digital_assets: the prompt counts crypto received as a gift or inheritance as a Yes, so the printed Digital Assets box is checked Yes wrongly

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 4), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i1040gi p. 16, Digital Assets, "Check the 'Yes' box ... if at any time during 2025, you (a) received (as a reward, award, or payment for property or services); or (b) sold, exchanged, or otherwise disposed of a digital asset".
- **Symptom:** The interview prompt asks "In 2025, did you (or, on a joint return, your spouse) receive, sell, trade, spend or give away crypto or another digital asset?"; the form label keeps "(as a reward, award, or payment for property or services)" but the prompt drops it. A filer whose only 2025 event was receiving crypto as a gift or an inheritance answers Yes: the printed Digital Assets question on Form 1040 page 1 shows Yes where the instructions call for No, and s1.digital_income is asked without need. No tax amount changes (s1.digital_amount help excludes gifts). The same bank entry carries BUG-0896 (the false-No side); the two fixes touch the same help. Not executed; read from the question and the source.
- **Where:** interview/2025/questions.yaml input f1040.digital_assets (prompt, help).
- **Proposed fix:** Prompt: "In 2025, did you (or, on a joint return, your spouse) get crypto or another digital asset as pay or a reward, or sell, trade, spend or give any away?" Help, added: "Crypto you got as a gift or an inheritance is a No by itself." Land with the BUG-0896 help change; reviews due: question, screen and false-no reviews of gate:f1040.digital_assets.
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-yes; wording; digital-assets; printed-answer
```

[I] The BUG-0896 rewording covers staking, forks and airdrops, so "pay or a reward" together with that help covers
the whole i1040gi Yes list.

---

## Candidate 5: `sche.qbi_business`. REAL, low

**Filer sees** [C Q:7238-7243]: the tick "A rental treated as a business for the qualified business income
deduction". Help: "A Yes ends the interview here."

The source adds an example: "Do you treat a rental as a business for the qualified business income deduction (for
example, 250 hours or more a year of rental services, with separate books)?" [C forms/2025/sche.yaml:40-51].

**Source** [C sources/2025/i8995.cols.txt:24, 28, 66]:
- "Rev. Proc. 2019-38 provides a safe harbor under which a rental real estate enterprise will be treated as a trade
  or business for purposes of the QBI deduction."
- "Rental real estate that doesn't meet the requirements of the safe harbor may still be treated as a trade or
  business ... if it's a section 162 trade or business."
- "If you're relying on the safe harbor ..., enter each enterprise as identified on the statement required for use
  on the safe harbor."

The 250-hour figure is not in i8995. It comes from Rev. Proc. 2019-38, which is not archived [I, `ls sources/2025`
shows no rp-2019-38].

**Ruling.** The tick drops the only concrete test its source carries, and the help gives none. A landlord whose 2024
return listed the rental on Form 8995 (often prepared by software) can read the tick as asking about "a business" and
answer No. The rental QBI is then dropped. That is an overpayment, and the tool computes where it should refuse. A
false Yes only refuses. `/tmp/nightplan/interview.md:336` already proposes moving the example to help, so the fix
overlaps that proposal.

```
## BUG-NEW-<PREFIX>-<NN> — sche.qbi_business: the tick drops its source's example, so a landlord who claimed rental QBI can answer No

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 5), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i8995 p. 1, Trade or business, "Rev. Proc. 2019-38 provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business for purposes of the QBI deduction" and "Rental real estate that doesn't meet the requirements of the safe harbor may still be treated as a trade or business ... if it's a section 162 trade or business"; Line 1, "If you're relying on the safe harbor ..., enter each enterprise as identified on the statement required for use on the safe harbor."
- **Symptom:** The tick of sche.qbi_business reads "A rental treated as a business for the qualified business income deduction" with help "A Yes ends the interview here."; the source's example "(for example, 250 hours or more a year of rental services, with separate books)" is not shown. A landlord whose earlier return listed the rental on Form 8995 or 8995-A, or attached the safe harbor statement, may not know the rental was "treated as a business" and answers No; the return is then computed with no QBI for the rental (an overpayment) where a Yes would refuse. Not executed; read from the bank and the source.
- **Where:** interview/2025/questions.yaml input sche.qbi_business (help).
- **Proposed fix:** Help: "Answer Yes if your 2024 Form 8995 or 8995-A listed a rental, if you attach the rental real estate safe harbor statement (usually 250 hours or more a year of rental services, with separate books), or if the rental is run as a business. A Yes ends the interview here." The 250-hour figure is from Rev. Proc. 2019-38, not archived: keep it as the source's own example or archive the procedure. Reviews due: screen review of sche.qbi_business.
- **Proposed fix lines:** none (bank only)
- **Severity:** low
- **Tags:** screen; false-no; wording; schedule-e; qbi
```

[I] "listed a rental on 2024 Form 8995" is a proxy, not the rule: the safe harbor is chosen year by year. It points
the right way and only adds refusals.

---

## Candidate 6: cost-20 questions. NOT A DEFECT

[C Q:835-848 `f1116sb.prior_year`; Q:737-742 `f1116col.div_income`; Q:1962-1965 `person.mw_earned`, help "If
unsure, figure the return both ways."]
- Each question asks for a figure or an election that the source requires. None has a wrong-answer path that its
  wording creates.
- High answer effort is a matter for the owner's cost ratings (T-334, `TASKS.md:102` [C]). It is not a bug.
- For `mw_earned`, having the tool compute both ways and pick is a feature or design choice. It is already recorded
  as an owner decision in the lane note (`docs/provisional/lanes/x2-paynow2.md:15` row 3 [C], per
  judgment-records.md:350).
- No entry is drafted. Route to T-334 and the owner's decision list.

---

## Candidate 7: `household.mfs_living` and estranged spouses under one roof. REAL, low, with a residual ambiguity

**Filer sees** [C Q:2729-2738]:
> "In 2025, when did your husband or wife live with you?"
> help: "Time away for work, school, medical care or military service, when you expected to come back, counts as
> living together."
> choices: together_late / apart_last6 / apart_all_year ("Not at any time in 2025")

**Source** (the candidate had not read it; now read):
- i1040gi p. 15: "You lived apart from your spouse for the last 6 months of 2025. Temporary absences for special
  circumstances ... count as time lived in the home." [C sources/2025/i1040gi.cols.txt:277]
- p501 HOH test: "Your spouse didn't live in your home during the last 6 months of the tax year." [C
  sources/2025/p501.cols.txt:333]
- p915 only restates the line 6d rule ("lived apart from your spouse for all of 2025") and gives no definition [C
  p915.cols.txt:33, 196].

**Ruling.** For the 6-month test (`mfs_apart_last6`), the archived text measures "living apart" by the home ("lived
in the home", "didn't live in your home"). Spouses who are estranged but share a home therefore did not live apart.
"When did your husband or wife live with you?" can be answered "Not at any time" by an estranged spouse in a shared
house (a false apart), so the case is REAL, low. The cost of that false answer:
- the line 6d box, and the SSB base (`amb.2025.mfs_lived_apart`)
- the f8582 special allowance (BUG-0836's proposed `f8582.mfs_together`, BUG_INVENTORY.md:10318-10320 [C])
- HOH and the EIC separated-spouse rule, through the 6-month test

For the all-year test (line 6d, SSB, IRA), the archived text does not define "apart". The house reading is the
natural extension [I], but it is unconfirmed. `amb.2025.mfs_lived_apart` [C ambiguities/2025.yaml:1477-1484] covers
temporary absences only, so the one-roof case should be added to it as a reading.

```
## BUG-NEW-<PREFIX>-<NN> — household.mfs_living: an estranged husband or wife sharing the home can be answered as not living with the filer

- **Caught by:** judgment record of the coverage expansion lanes (T-333, candidate 7), ruled in lane jr-verify (claude-opus-5-5, judgment), 2026-11-16; read only, not a paid review.
- **Source:** i1040gi p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025. Temporary absences for special circumstances ... count as time lived in the home"; p501, Head of Household, Considered Unmarried, "Your spouse didn't live in your home during the last 6 months of the tax year."
- **Symptom:** household.mfs_living asks "In 2025, when did your husband or wife live with you?" and its help covers only temporary absences. A separated filer whose husband or wife still lived in the same home can answer "Not at any time in 2025" or "Only before July", though the sources measure living apart by the home. The answer then checks the line 6d box and lowers the social security base (household.mfs_apart_all_year), and passes the 6-month tests read through household.mfs_apart_last6. The all-year test has no archived definition (amb.2025.mfs_lived_apart); the one-roof reading should be added there. Not executed; read from the question and the source.
- **Where:** interview/2025/questions.yaml input household.mfs_living (help); ambiguities/2025.yaml amb.2025.mfs_lived_apart (readings).
- **Proposed fix:** Help, added: "If you shared a home, count that as living together, even if you were separated." Add to amb.2025.mfs_lived_apart the one-roof reading, chosen as living together, citing the two sentences above. Reviews due: question review of household.mfs_living.
- **Proposed fix lines:** none (bank and ambiguity only)
- **Severity:** low
- **Tags:** screen; wording; married-filing-separately; household
```

---

## What was checked and what was not

- **Checked** (path:line above): every bank entry quoted; the form sources of community_property, its three readers,
  scope.recovery, sche.qbi_business and f1040.digital_assets; p555, i1040gi, i1040gi-html, i8995, p501 and p915 text
  quoted; the ambiguity entries; BUG-0519, BUG-0640, BUG-0732, BUG-0896, BUG-0908 and BUG-0922..0926; the
  conventions in tools/README.md:748-790; the earlier screen logs of gate:scope.recovery and sa.dependent; grep of
  BUG_INVENTORY.md, bug_pending/, med-*.md, interview.md and wording-redteam.md for duplicates.
- **Not checked**:
  - Reachability and gating were not walked.
  - Tick and help word-count norms were not read; the proposed wording may need trimming.
  - p501 Table 2 clauses for candidate 3 were checked only for the $5,200 figure.
  - Rev. Proc. 2019-38 is not archived.
  - The new gate ids in candidate 1 are sketches.
  - `Caught by` wording and the pending PREFIX are for the coordinator to set.
