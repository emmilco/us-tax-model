# Lane patch-inc-m12: drafted patch for plan lanes M2 (scope, person) and M1 (s1, tipjob)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Plan: /tmp/nightplan/med-income.md.
**Nothing was run except YAML/JSON parsing and `git apply` on scratch copies.** No build, no fixture run, no coverage
walk, no review. Every behavioural claim below is either checked against a file (path:line) or marked inferred.

## Summary

- **Three patch files**, made from copies of xint as it stood on 2026-11-16. Before the diffs were made, the a/ copies
  were compared byte for byte with xint and matched. Paths are relative to the repo root:
  - `/tmp/nightplan/patches/inc-m12.patch`: **everything** (M2, M1 and BUG-0810 Option B).
  - `/tmp/nightplan/patches/inc-m12.base.patch`: M2 and M1 **without** BUG-0810 (0904, 0905, 0906, 0806, 0808, 0822, 0896).
  - `/tmp/nightplan/patches/inc-m12.cod.patch`: BUG-0810 Option B only (the tick-box screen).
  - Checked on scratch copies: base then cod, cod then base, and combined each applies cleanly with `git apply`, and
    base+cod gives the same tree as combined. **To drop 0810 Option B, apply `inc-m12.base.patch` instead of
    `inc-m12.patch`.** For Option A (the longer prompt), do that and make the one-line bank edit given under 0810 below.
- **BUG-0907 (scope.nol) is left out**, as briefed. The s1.nol_amount help is not touched either.
- **Follows the plan's wording exactly**, with the guards it adds: no "from a union" plus the unemployment exclusion
  (0906); "even at a loss" plus the personal-use sale guard (0822); the airdrop named, with no "similar reward" (0896).
- **Departures from the plan** (each explained below): (1) the coverage row ids are lower case and in the files'
  own prefixes (`pay.`, `scope.`, `other.`); (2) the plan's `tips.mixed_occupation`, `pay.noncash_tips_only` and
  `crypto.staking_only` rows **already exist** (`jobs.tips_other_work`, `pay.tips_noncash_only`, `other.digital_income`),
  so no duplicates were added; (3) for 0810 the canceled-debt block moves to **seq 32 to 42 of order 161**, because
  seqs 15 to 31 are taken, mostly by f8853c and rec, which belong to lane M4; (4) for 0810 the form source of each box
  keeps the precision the old seven-item source had, which the 12-word ticks cannot carry ("or is otherwise excluded
  (Form 982)", "or any other amount, such as an unpaid medical bill").
- **Three wording concerns about the plan's verbatim text.** Flagged, not changed: 0808 drops "small winnings, no tax
  form" from the help; 0905 drops "held outside a U.S. fund" from the tick; and the source for 0896 covers only
  airdrops after a fork. See "Concerns".

## Hunks, by entry

### M2: BUG-0906, strike or lockout pay, pay not on a W-2
- `forms/2025/scope.yaml` scope.pay_no_w2 label and source (xint F:456, F:459): "wages, tips or strike benefits" becomes
  "wages, tips, or strike or lockout benefits".
- `forms/2025/scope.yaml` scope.strike_pay label and source (F:566, F:569): "from a union" is dropped.
- `forms/2025/person.yaml` person.strike source (F:1481): "from a union" is dropped, and "Leave out true gifts and
  state unemployment pay." is added. This is the plan's guard against counting unemployment insurance twice, on 1h and
  on Schedule 1 line 7 [the double count is inferred, as in the plan]. The label is unchanged and already says
  "Strike or lockout benefits you received (other than bona fide gifts)".
- Bank scope.pay_no_w2 (Q:1849-1850): new tick "Wages, tips, or strike or lockout pay not on a W-2" (11 words). The
  new help (38 words) adds "tips given as tickets or goods".
- Bank scope.strike_pay (Q:1879): new tick "Strike or lockout pay", and a new help (25 words) that names a union or strike
  fund and excludes gifts and state unemployment pay.

### M2: BUG-0904, Medicaid waiver pay through an agency
- `forms/2025/scope.yaml` scope.medicaid_waiver label and source (F:631, F:634): the plan's 30-word text, "paid under
  Medicaid, directly or through an agency or care plan, to care for someone who lived in your home with you".
- Bank (Q:1855-1856): new tick "Medicaid pay, through any agency, for care of someone living with you" (12 words).
  New help: the plan's 41 words (code II in box 12; care in the other person's home is not this).

### M2: BUG-0905, foreign shares (options, warrants, ADRs, funds set up abroad)
- `forms/2025/scope.yaml` scope.foreign_shares label and source (F:988, F:991): adds "or options or warrants to buy
  them", and the exclusion becomes "other than through a fund set up in the United States".
- Bank (Q:2043-2044): new tick "Shares, options or warrants of a company or fund set up abroad" (12 words). New help
  (36 words): ADRs, a fund set up abroad, and shares held for the filer by a partnership, trust, estate, foreign
  pension or insurance policy.

### M1: BUG-0806, tipjob.listed ("any of these tips")
- `forms/2025/tipjob.yaml` tipjob.listed label (F:41-42) is now "Were any of the tips from this employer received in an
  occupation on the IRS list…". The source (F:46-47) is now "Did you get any of these tips for work on the IRS list…".
- Bank tipjob.listed help (Q:4673-4674): the plan's 33 words, "If none of the work you got tips for here is on it…".
- Sibling read: the tipjob.other_work source ("Did you also get tips from this employer for other work that is not
  on that list?", tipjob.yaml F:59) and its tick already fit the new reading. No change.

### M1: BUG-0808, winnings received, not won
- Bank s1.winnings_any (Q:4265-4272): the prompt becomes "receive gambling or lottery winnings, or a prize or award?"
  (21 words). The help is the plan's 40 words (a yearly installment, a sale of future payments, a year you lost more,
  prizes in goods).
- Bank s1.gambling_winnings help (Q:3815-3816): the plan's 40 words. It names the installment and the sale of future
  payments and drops "Losses are asked with deductions". The prompt there still says "before subtracting any losses".
- No form change. The s1.gambling_winnings source already names "a lump sum from selling a right to future lottery
  payments" (s1.yaml F:677-680).

### M1: BUG-0822, hobby income even at a loss
- Bank s1.hobby_any (Q:3874-3880): new tick "Money or goods from a hobby or pastime, even at a loss" (12 words); new
  prompt (29 words); a new help (23 words) with the guard against personal-use sales ("…is not this; it is asked with
  sales").
- Bank s1.hobby_income help (Q:3884): "Give everything it brought in, with goods at what they were worth. The costs of a
  hobby are not subtracted." (20 words).
- No form change. The s1.hobby_any source ("receive income … from an activity not engaged in for profit", s1.yaml F:928)
  is already right.

### M1: BUG-0896, crypto (staking, forks, airdrops)
- Bank f1040.digital_assets help (Q:3897-3898): the plan's 39 words, now naming staking rewards and new coins from a
  fork or airdrop as a Yes.
- Bank s1.digital_income: the prompt (33 words) adds "from a fork (a coin split in two), or from an airdrop", and the
  help adds "A gift of crypto from a person is not counted." (37 words in all).
- `forms/2025/s1.yaml` s1.digital_income label and source (F:562, F:565) add "or from an airdrop", as the plan
  recommends. Its cite locator adds rr-2019-24 Holding (2), quoted from `sources/2025/rr-2019-24.txt:213-217`
  [checked]. **This is a form change.** It makes the s1 transcription and render reviews due. Drop the two s1.yaml
  hunks for digital_income if the bank-only form is preferred.
- 2026 operations: `changes/2026/f1040.x1-digital.yaml` changes only `f1040.digital_assets` `cite.locator`. That
  field is not touched here [checked]. No 2026 operation names any other line or bank entry this patch edits
  [checked by grep over changes/2026/*.yaml].

### BUG-0810 Option B: the canceled-debt screen as two tick groups (inc-m12.cod.patch)
The plan recommends Option B (protocol 3.1). What the patch does:
- `forms/2025/s1.yaml`: s1.cod_unsupported keeps its id and `printed: (gate)`. It becomes a derived Bool
  (`op: test`, `any:` over ten item lines), with the same cite as before and a new label ending "(true when any of the
  canceled-debt screening questions is answered Yes)". Its one reader is the refusal on s1.cod_refused (F:1363), which
  is unchanged.
- Ten new input lines, each with its own p4681 cite. Each cite page was checked against the page split of
  `sources/2025/p4681.cols.txt`:
  - cod_why group: `s1.cod_bankrupt` (also carries "otherwise excluded … (Form 982)"), `s1.cod_student_home`,
    `s1.cod_gift`, `s1.cod_price_cut`, `s1.cod_stockholder`, `s1.cod_business`.
  - cod_how group: `s1.cod_property`, `s1.cod_interest` (also carries "any other amount, such as an unpaid medical
    bill"), `s1.cod_not_liable`, `s1.cod_joint_other`.
  - Each source is a question with the spouse phrase where it says "you".
- The items have no `gated_by`. They are read only through s1.cod_refused, which is reached only when s1.has_cod is
  true (s1.cod_figured, F:1371-1390 [checked]). `any` returns true on the first true item even when the others are
  unknown (engine/src/eval.ts:793-803 [checked]), so a Yes in the first group refuses without the second group.
- Bank: two groups, `cod_why` (6 boxes) and `cod_how` (4 boxes). Both have the plan's heading, "Does any of these apply
  to a canceled debt?". The ticks are the plan's, all 12 words or fewer. Each help ends "A Yes ends the interview
  here."; the bankrupt, interest and not-liable helps add a short gloss. The old s1.cod_unsupported bank entry is
  removed.
- **Order:** s1.cod_amount moves from seq 14 to 32, and the boxes take seq 33 to 42. The tick-group contract forbids
  any other question's seq inside a group's range (interview/README.md:582-585), and seq 15 to 31 are taken by
  `$f8853c`, f8853c.* and rec.* [checked by listing order 161]. Effect: a filer who ticked a canceled debt and a
  long-term care payout or a recovery now answers the canceled-debt questions after those topics, not before. The
  alternative is to keep cod at 14 to 24 and add 10 to the seq of the 15 f8853c and rec entries. Those entries are lane
  M4's (it edits their prompts), so that would conflict with M4.
- Fixtures (restated inputs, protocol 3.1(c); **no expected value or refusal edited**):
  - `fixtures/2025/defaults.json`: the s1.cod_unsupported default is replaced by ten closed defaults (false). The
    build needs exactly one default per input template (engine/src/fixture-inputs.ts:285-306).
  - `s1.json` case `stage16.refuse.s1.cod_unsupported` and `f1040.json` case `stage20.refuse.excluded_canceled_debt`:
    `"s1.cod_unsupported": true` becomes `"s1.cod_bankrupt": true`. The expected refusals still name
    `gate: s1.cod_unsupported`, since the refusal's `when` is unchanged. The evidence_note of the s1 case is reworded
    to say which box.
  - The files that take no defaults (classm.json, classm.gpt.json, classm.deepseek.json, mutation.json;
    engine/src/fixture-inputs.ts:439-443) hold 134 lines of `"s1.cod_unsupported": false`. They must go, because the
    engine rejects an input that is not declared (engine/src/eval.ts:865). In the 133 cases where s1.cod_amount is 0,
    the screen is never read, so the line is just dropped. In `classm.s1.1` (cod_amount 500000) it becomes ten
    `false` lines. Every case was checked to state s1.cod_amount.
  - `engine/src/generate.ts:192`: in the generator's FIXED set, s1.cod_unsupported is replaced by the ten items. They
    stay undrawn, as the old input was, so the property generator's draw sequence does not change [inferred from
    generate.ts:385].
- Coverage (`interview/2025/coverage/other.yaml`): the existing row `other.canceled_debt_exception` has its answers
  restated (`s1.cod_bankrupt: true` in place of `s1.cod_unsupported: true`); its expected end is unchanged. Five rows
  are added, one per newly named situation, each ending `refused: s1.cod_unsupported`:
  `other.canceled_debt_student_loan`, `_main_home`, `_gift`, `_seller_price_cut` and `_stockholder`. Each answers the
  earlier boxes of its group No.
- **Option A instead** (bank only; it breaks N10 at about 80 words): apply `inc-m12.base.patch`. Then, in the
  s1.cod_unsupported bank prompt (Q:4172-4174), insert before "; it was a business, rental or farm debt" the text
  "; it was a student loan or your main home's mortgage; it was forgiven as a gift, by the seller of what you bought,
  or by a company you own shares in".

## Coverage rows added, with predicted ends

Every `proceeds` value below equals an answer the row gives, so the predictions are the answers themselves. The rows
test the path, not a computation.

| Row (file) | Answers (beyond the set) | Expected end |
|---|---|---|
| `pay.lockout_benefits` (pay_not_w2) | set pay_no_w2; other pay kinds No; strike_pay true; person.strike 120000 | proceeds person.strike 120000 |
| `pay.strike_fund_nonunion` (pay_not_w2) | the same; person.strike 80000 | proceeds person.strike 80000 |
| `pay.medicaid_agency_code_ii` (pay_not_w2) | set medicaid; mw_box1 0, mw_not_box1 2400000, mw_1099 0, mw_earned false | proceeds mw_not_box1 2400000 |
| `scope.foreign_warrants` (coverage/scope) | foreign_shares true, pfic true | refused scope.other_line16 (as `scope.pfic`) |
| `other.lottery_installment` (other) | set won; the answers of `other.gambling_winnings` with gambling_winnings 100000 | proceeds s1.gambling_winnings 100000 |
| `other.lottery_rights_sale` (other) | the same with 150000 | proceeds 150000 |
| `other.hobby_at_loss` (other) | hobby_any true, hobby_income 60000 | proceeds 60000 |
| `other.digital_airdrop` (other) | digital_assets true, digital_income true, digital_amount 20000 | proceeds 20000 |
| 0810: five `other.canceled_debt_*` rows | cod_any true, amount, earlier boxes No, the named box true | refused s1.cod_unsupported |

**Unverified, so run before trusting:**
- The lottery rows copy the saver's-credit answers of `other.gambling_winnings`. Their amounts were kept small
  ($1,000 and $1,500) so that AGI stays near that row's (it has $37,500 of prizes) and the same saver's-credit
  questions are asked. If the walk asks a different set, change the answers. Never change the end.
- `pay.medicaid_agency_code_ii` answers mw_earned false where the existing row answers true. I did not check whether
  false opens another question.
- The 0810 rows assume the coverage walk refuses as soon as the true box is answered, as `any` would give. If the
  walk instead needs every box of the screen answered first, add `false` for the later boxes of the group.

## Concerns about the plan's verbatim wording (owner or reviewer to decide)
1. **0808 help.** The plan's help drops "small winnings, winnings with no tax form", which the current help has. Those
   are the commonest reasons to answer No wrongly. Restoring "small or with no form" costs about 5 words and takes the
   help to about 45. Not changed.
2. **0905 tick.** "Shares, options or warrants of a company or fund set up abroad" no longer says "held outside a U.S.
   fund". Someone with a U.S. fund of foreign stocks might tick it, under the heading "have any of these outside the
   United States". The children scope.pfic and scope.cfc only refuse on a Yes, so the cost is extra steps, not a wrong
   value [inferred]. The help and the form source keep the exclusion.
3. **0896 airdrop.** The archived ruling covers an airdrop *after a hard fork*
   (`sources/2025/rr-2019-24.txt:213-217`). A non-fork airdrop rests on i1040gi's "similar activities" [inferred, as in
   the plan]. The new text sends a non-fork airdrop to line 8v.
4. **0904 tense.** "someone who lived in your home with you" (the plan's source) replaces "lives". The children's help
   (person.mw_box1, Q:1949) still says "lives in your home with you". Harmless; it is a sibling for the next pass.

## Siblings checked
- tipjob.other_work source and tick (tipjob.yaml F:53-64; Q:4675-4680): consistent, unchanged.
- scope.tips_unreported tick already names noncash tips (Q:1872): unchanged.
- person.strike label already has no union restriction (person.yaml F:1481): unchanged.
- s1.gambling_winnings source names the sale of future payments (s1.yaml F:677-680): unchanged.
- s1.hobby_any source (s1.yaml F:928-934): unchanged.
- f1040.digital_assets form source: unchanged. Only its bank help changes.
- `tools/siblings.py` was **not run** (read-only lane). Run `tools/siblings.py scope.pay_no_w2`, `scope.strike_pay`,
  `scope.medicaid_waiver`, `scope.foreign_shares`, `tipjob.listed`, `s1.winnings_any`, `s1.hobby_any`,
  `s1.digital_income` and `s1.cod_unsupported` at apply time.
- Not updated, to check at apply time: `tools/coverage/tree.json:242` and `docs/COVERAGE.md:1069` describe
  s1.cod_unsupported in their own words; they are still true. `research/ty2026/worklist.json:57341` lists
  s1.cod_unsupported. Whether the 2026 worklist needs rows for the ten new lines was not checked.

## What to run to verify (in the lane's worktree, after applying)
1. The build (`node engine/dist/main.js` build step via `tools/check_all.sh --quick` or the build alone). It checks
   wording, tick labels and headings, the spouse phrase, and defaults.
2. `node engine/dist/main.js test-fixtures`. For 0810: the two restated refusing cases and classm.s1.1 must pass
   unchanged.
3. `node engine/dist/main.js interview-coverage`, then `--write`. The report quotes wording, so it must be rewritten.
4. `node engine/dist/main.js tick-groups`, especially the new cod_why and cod_how groups and the changed ticks in
   other_pay, money_a and outside_us.
5. `node engine/dist/main.js draft-walk`. No persona has a canceled debt [checked: no `cod_` in
   interview/2025/personas], so the walks should be unchanged except for wording.
6. `tools/check_all.sh` once, at the end.

## Reviews made due (one per form per round, after all of that form's fixes)
- **scope**: transcription and render of the changed lines (pay_no_w2, strike_pay, medicaid_waiver, foreign_shares).
- **person**: transcription and render (person.strike).
- **tipjob**: transcription and render (tipjob.listed label and source).
- **s1**: transcription and render (s1.digital_income label, source and cite). With 0810 Option B, also the ten new
  lines and the rewritten s1.cod_unsupported, plus **class M for s1** (a model change).
- Question, screen and false-no reviews of these gates: scope.pay_no_w2, scope.strike_pay_if_pay, scope.medicaid_waiver,
  scope.foreign_shares, tipjob.listed, s1.winnings_any, s1.hobby_any, f1040.digital_assets and s1.digital_income.
- Question reviews of s1.gambling_winnings and s1.hobby_income.
- With 0810 Option B: screen and false-no reviews of each new box and of both groups. The screen review must be run on
  the *asked* wording.
- All are paid. Estimate first; runs above $3.00 need `--approve-cost`.

## Pending bug-entry text
None proposed. The concerns above are wording judgments on the plan, not defects found in the tree.

## Not done
- No check of any kind was run (hard rule for tonight).
- Coordinator's note on BUG-0901 (the Schedule H sources): not in this lane (0901 is M4). Ignored.
