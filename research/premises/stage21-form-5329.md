> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: `retirement` is a return-level collection with no owner; distribution code 1 falls under `other` in `retirement_code`; the 3.2% share.
> **Verified after Stage 15:** see `stage21-form-5329.verification.md` (8 errors, 4 items out of date), which supersedes this map where they differ.

# Premise map: Stage 21, Form 5329 (additional taxes on qualified plans and other tax-favored accounts)

Roadmap item 7 of spec 2.4 ("The additional tax on qualified retirement plans, Form 5329 (95%, the target)"). Coverage category `form5329`, gates `retirement.special` and `s2.other`.

Read-only research by a Claude Code agent, from the archived snapshots in `sources/2025/` and the repository as of commit 6051ec0 (working tree). Nothing in the repository was changed. Locators: `doc p. N, heading, "quote"`, where page N is the N-th form-feed chunk of `<doc>.cols.txt` (this is not always the printed page number; for i1040gi chunk 112 is printed page 112, but this was not checked for every page cited). Everything here is testimony for the authoring stage, not a verified encoding.

Assumption about order: roadmap items 1 to 6 (Stage 15 credits, the remaining Schedule 1 items including the IRA deduction, Schedule E, the premium tax credit, the education credits, the capital loss carryover) land before this stage, as spec 2.4 orders them. Where a recommendation depends on one of them it says so.

---

## 1. Scope

### 1.1 What the category measures

- `tools/coverage/categories.json`, entry `form5329`: group `retirement_penalty`, gates `["retirement.special", "s2.other"]`, IRS cell `soi-23in33ar` column 76, header "Penalty tax on qualified retirement plans".
- `reports/2025/filer_coverage.md`: "Additional tax on qualified plans (Form 5329) | ... | 3.2% | 5,092,999 | — | IRS count only (independence assumed)". Step 7 of the gain order: "95.1% (+3.0)", "+1.9" if covered alone now.
- Checked in the spreadsheet (read with the project's `.engines/venv` pandas): row "All returns", column 76 = 5,092,999 returns, column 77 ("Amount") = 6,380,591. SOI amounts are in thousands of dollars (convention, not checked in this file), so about $6.4 billion, an average near $1,250 per return. That average is consistent with the count being mostly the 10% tax on early distributions (an average early distribution near $12,500), not the 6% taxes; this is an inference, the SOI cell does not split the parts of Form 5329.
- The SOI cell counts Schedule 2 line 8 whether or not Form 5329 was attached (inference from the header; the line 8 exception path files no form). There is no microdata predicate for this category ("—").

### 1.2 What the two gates refuse today (checked in `forms/2025/`)

`retirement.special` (forms/2025/retirement.yaml, per Form 1099-R entry, a single Bool input) refuses, among others: "an early distribution with no known exception (code 1, J or S)"; "a disability pension received before minimum retirement age, or a pension partly excludable because you were disabled as a result of a terrorist attack"; "a corrective distribution of excess deferrals or contributions"; "a qualified charitable distribution or HSA funding distribution"; "nondeductible contributions to any traditional IRA"; "a conversion or recharacterization (Form 8606)"; "a 2024 or 2025 IRA contribution returned to you, or excess contributions for an earlier year returned to you in 2025"; "a rollover to a Roth IRA or designated Roth account"; "a lump-sum distribution you may report on Form 4972"; "a nonqualified annuity"; the retired public safety officer exclusion; a death benefit exclusion; a plan loan offset; Form RRB-1099-R; the Civil Service alternative annuity; and annuities under the General Rule or starting before November 19, 1996.

Also relevant and **not** named in the category: `retirement.bad_code` refuses every box 7 code outside `retirement_code` = {normal_7, death_4, early_exception_2, direct_rollover_G, qualified_roth_Q, other} (params/2025.yaml `enums.retirement_code`). **Code 1, code 3 and code S are all `other` today**, so a code 1 entry is refused twice: by `retirement.special` (if the filer answers it) and by `retirement.bad_code`.

| Situation refused by `retirement.special` | Retired by Form 5329? |
|---|---|
| Early distribution, no known exception, code 1 | **Yes** (Part I, or the Schedule 2 line 8 direct path) |
| Code S (SIMPLE IRA, first 2 years) | **Yes** if the 25% rate is encoded (Part I line 4) |
| Code J (Roth IRA, no known exception) | No: Part I line 1 for a Roth IRA reads Form 8606 line 25c (i5329 p. 3) |
| Disability pension before minimum retirement age | No: Form 1040 line 1h (i1040gi p. 25), wages, not Form 5329 |
| Corrective distributions, returned IRA contributions | No in a first build (Form 8606, line 1h, the 2026 Form 1099-R code P problem) |
| QCD, HSA funding distribution, conversions, Roth rollovers, 4972, loan offsets, RRB, Pub. 721, General Rule | No |

`s2.other` (forms/2025/s2.yaml, return-level Bool) asks in one question about "the alternative minimum tax" (no: that is `s2.amt`), "repayment of excess advance premium tax credit or of a clean vehicle credit, household employment taxes, the additional tax on early retirement or HSA distributions (often called a penalty), uncollected social security or Medicare tax on tips or group-term life insurance ..., tax on unreported tips (Form 4137), or interest on deferred tax". It is also the gate of the categories `ptc` and `schedule2_other` (categories.json), and it refuses Schedule 8812 line 22 (forms/2025/s8812.yaml), Schedule 1-A line 4b (forms/2025/s1a.yaml) and `tipjob` column (c) (forms/2025/tipjob.yaml). It cannot be deleted; its wording must lose the Form 5329 items this stage computes and keep the rest (including "the additional tax on ... HSA distributions", which is Form 8889 Part II and Schedule 2 line 17c, not Form 5329).

Other existing gates this stage touches: `f8889.excess` ("Form 5329 (excess HSA contributions) or excess employer contributions", unmeasured) and the prior-year-excess clause of `f8889.unsupported`.

### 1.3 Recommended scope

**Include now:**

1. Part I for box 7 codes 1 and S (with code 2, 4, 7, G, Q handled as today: no additional tax), with the filer's exceptions entered per Form 1099-R entry, the 25% SIMPLE rate, and the "Form 5329 not required" path (Schedule 2 line 8 with its box checked). This is the bulk of the 5.1 million returns (inference, 1.1).
2. Schedule 2 line 8 and its sum into line 21.
3. Part VII for **current-year** HSA excess contributions made by the filer (from the existing Form 8889 lines), which retires `f8889.excess` for that case. Excess employer contributions only if Schedule 1 "other income" exists by then (roadmap item 2), because they are also income (p969 p. 8, below).
4. A structural change: each Form 1099-R entry must belong to a person (Form 5329 is per person on a joint return). See decision D1.

**Refuse (cited), leave for later:** Part II (education and ABLE distributions; it needs Schedule 1 lines 8z and 8q and the education rules of item 5), Parts III and IV (excess IRA contributions; feasible once item 2 has the IRA contribution inputs, but they need prior-year Form 5329 carryovers, account values, and the Roth modified AGI worksheet; see D9), Part V (Coverdell), Part VI (Archer MSA, Form 8853 not prepared), Part VIII (ABLE), Part IX (required minimum distributions, the correction window and the reasonable-cause waiver), the SEPP recapture tax, designated Roth account recapture (code B with box 10), Roth IRA distributions (code J or T, Form 8606), prior-year HSA excess (line 42), and qualified disaster recovery distributions (Form 8915-F).

Reasoning: Part I with code 1 is the common case and its arithmetic is two lines; every other part is either much rarer (no SOI split exists, so this is inference) or depends on forms the project does not prepare. This follows the Stage 15 pattern as the research brief summarises it: "refuse rare and hard situations, compute common ones".

Optional cheap addition (D8): box 7 code 3 (disability) for an **IRA** entry (fully on line 4b, no additional tax, exception 03 shown by the code). Code 3 from a plan stays refused (line 1h when under minimum retirement age, T-002).

---

## 2. Sources

Archived and used: `f5329` (3 pages), `i5329` (10), `f1040s2` (2), `i1040gi` (Schedule 2 line 8 at p. 112; lines 1h, 4a-5b at pp. 25-28), `f1099r` (box 7 codes, pp. 7 and 9), `i1099r` (Table 1, Guide to Distribution Codes, pp. 18-20; box 7 rules p. 15), `p590b` (early distributions and exceptions, pp. 24-28), `p590a` (excess contributions p. 35, Roth limits pp. 40-43), `p969` (HSA excess p. 8), `f8889`, `i8889` (line 13 and excess contributions, pp. 7-8), `f1040sa` (via the existing `sa` lines).

**Not archived** (needed or cited by the archived text; IRS URLs, not fetched):

| Document | Why | URL |
|---|---|---|
| Pub. 575 (2025) | Annuity exceptions, designated Roth recapture, in-plan Roth rollover (i5329 p. 3, exception 16) | https://www.irs.gov/pub/irs-pdf/p575.pdf |
| Pub. 721 | Exception 17 (phased retirement annuities) | https://www.irs.gov/pub/irs-pdf/p721.pdf |
| Form 8915-F and instructions | Qualified disaster recovery distributions are outside Part I (i5329 p. 2) | https://www.irs.gov/pub/irs-pdf/f8915f.pdf, https://www.irs.gov/pub/irs-pdf/i8915f.pdf |
| Notice 2024-55 | Exceptions 22 and 23 (domestic abuse, emergency) | https://www.irs.gov/pub/irs-drop/n-24-55.pdf |
| Notice 2024-02 | Exception 20 (terminal illness) | https://www.irs.gov/pub/irs-drop/n-24-02.pdf |
| Notice 2020-68 | Exception 19 (birth or adoption) | https://www.irs.gov/pub/irs-drop/n-20-68.pdf |
| Instructions for Forms 1099-SA and 5498-SA | HSA distribution and contribution reporting (only if Part VII grows) | https://www.irs.gov/pub/irs-pdf/i1099sa.pdf |
| Form 8853 and instructions | Part VI (refused) | https://www.irs.gov/pub/irs-pdf/f8853.pdf |
| Pub. 907 | ABLE accounts (Parts II and VIII, refused) | https://www.irs.gov/pub/irs-pdf/p907.pdf |

The refusals can cite i5329 alone; the unarchived documents matter only if their parts are computed.

---

## 3. Line map

### 3.0 Structure

- i5329 p. 2, Joint returns: "If both you and your spouse are required to file Form 5329, complete a separate form for each of you. Include the combined tax on Schedule 2 (Form 1040), line 8."
- So Form 5329 is per person. In this project that means lines on `person` (or an implicit one-per-person collection under `person`, as Form 4562 is under Schedule C; spec 4.4). Schedule 2 line 8 is return-level, a `sum_over person`.
- **The obstacle:** `retirement` is a return-level collection with no parent and no owner field (retirement.yaml `collection:` has no `parent`). The checker allows `sum_over` only over a collection whose parent is the evaluating document (engine/src/check.ts, `sum_over`: "collection parent binding mismatch"), so a person cannot total its own Forms 1099-R today. See D1.

### 3.1 Header and pre-Part I text (f5329 p. 1)

| Item | Text (f5329 p. 1) | Encoding |
|---|---|---|
| Name | "Name of individual subject to additional tax. If married filing jointly, see instructions." | per person |
| Exception path | "If you only owe the additional 10% tax on the full amount of the early distributions, you may be able to report this tax directly on Schedule 2 (Form 1040), line 8, without filing Form 5329. See instructions." | new Bool `f5329.required` per person and a return-level box for Schedule 2 line 8 (3.4) |

### 3.2 Part I, Additional Tax on Early Distributions

Part heading (f5329 p. 1): "Complete this part if you took a taxable distribution (other than a qualified disaster recovery distribution) before you reached age 59½ from a qualified retirement plan (including an IRA) or modified endowment contract (unless you are reporting this tax directly on Schedule 2 (Form 1040)—see above)."

Per Form 1099-R entry (new lines on `retirement`):

| New line | Meaning | Atom | Source |
|---|---|---|---|
| `retirement.early` (Bool) | code is `early_1` or `simple_S` | `test` | f1099r p. 7, Box 7, "1—Early distribution, no known exception (in most cases, under age 59½)"; f1099r p. 9, "S—Early distribution from a SIMPLE IRA in first 2 years, no known exception (under age 59½)" |
| `retirement.exception` (Enum, new `early_exception` = e01..e23, none) | the exception number the filer claims for this entry | `input`, asked when `retirement.early` | i5329 p. 5, Line 2, "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." |
| `retirement.excepted_claimed` | amount of this distribution's taxable part the exception covers | `input` | i5329 p. 5, Line 2, "Enter on line 2 the amount that you can exclude." |
| `retirement.excepted` | the claimed amount, capped (by the taxable amount; by fixed caps per D4; for 05 by the medical excess per D5) | `smaller_of` chain or `choose` by exception | as D4/D5 |
| `retirement.early_taxable` | taxable amount of an early entry, else 0 | `choose` on `retirement.early` → `retirement.taxable` / zero | i5329 p. 3, Line 1; the TIP in i5329 p. 1, "If you rolled over part or all of a distribution from a qualified retirement plan, the part rolled over isn't subject" |
| `retirement.subject` | `early_taxable − excepted`, floor 0 | `subtract_floor0` | f5329 line 3 per entry |
| `retirement.subject_simple` | `subject` when code S, else 0 | `choose` | i5329 p. 5, Line 4 |

Per person (Form 5329 lines):

| Line | Printed text (f5329 p. 1) | Computes | Supplied by |
|---|---|---|---|
| 1 | "Early distributions includible in income (see instructions). For Roth IRA distributions, see instructions" | Σ `retirement.early_taxable` over the person's entries | retirement (after D1). Roth IRA entries never reach here (code J refused). |
| 2 | "Early distributions included on line 1 that are not subject to the additional tax (see instructions). Enter the appropriate exception number from the instructions:" | Σ `retirement.excepted` | new per-entry inputs. The printed exception number: D6. |
| 3 | "Amount subject to additional tax. Subtract line 2 from line 1" | `subtract` (never negative, since each excepted ≤ its early_taxable) | |
| 4 | "Additional tax. Enter 10% (0.10) of line 3. Include this amount on Schedule 2 (Form 1040), line 8" with "Caution: If any part of the amount on line 3 was a distribution from a SIMPLE IRA, you may have to include 25% of that amount on line 4 instead of 10%. See instructions." | 10% × (line 3 − S part) + 25% × S part: helpers `f5329.line3_simple` (Σ `retirement.subject_simple`), `f5329.line3_other` (`subtract`), two `multiply_rate`, a `sum` | params `f5329.early_rate`, `f5329.simple_rate` |

i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7."

New per-entry inputs, all on `retirement` (asked only when `retirement.early`): the exception number and amount (above); for exception 12 nothing more (the amount is the part received at or after 59½, i5329 p. 5, exception 12, "Include on line 2 the amount you received when you were age"); for exception 09 the person's earlier first-home distributions (a per-person input, D4); a new screen `retirement.early_special` (D3).

### 3.3 Part VII, HSAs (recommended in scope for current-year excess only)

On the person's `f8889` entry (f8889 has `collection.parent: person`). Printed text f5329 p. 2.

| Line | Printed text | Computes | Supplied by / new input |
|---|---|---|---|
| 42 | "Enter the excess contributions from line 48 of your 2024 Form 5329. If zero, go to line 47" | 0 (prior-year excess refused, as `f8889.unsupported` does now) | — |
| 43 | "If the contributions to your HSAs for 2025 are less than the maximum allowable contribution, see instructions. Otherwise, enter -0-" | 0 when line 42 is 0 (its only use is reducing line 42) | i5329 p. 8, Line 43 |
| 44 | "2025 distributions from your HSAs from Form 8889, line 16" | 0 (Form 8889 Part II refused) | — |
| 45 | "Add lines 43 and 44" | sum | |
| 46 | "Prior year excess contributions. Subtract line 45 from line 42. If zero or less, enter -0-" | 0 | |
| 47 | "Excess contributions for 2025 (see instructions)" | (f8889.line2 − f8889.line13) + employer excess (f8889.line11 − f8889.line8, floor 0) − amounts withdrawn by the due date (D7) | existing `f8889.line2`, `.line13`, `.line11`, `.line8`; new input for withdrawals |
| 48 | "Total excess contributions. Add lines 46 and 47" | sum | |
| 49 | "Additional tax. Enter 6% (0.06) of the smaller of line 48 or the value of your HSAs on December 31, 2025 (including 2025 contributions made in 2026). Include this amount on Schedule 2 (Form 1040), line 8." | `smaller_of` then `multiply_rate` | new input: value of the person's HSAs at December 31, 2025 (asked only when line 48 > 0); param `f5329.excess_rate` |

i5329 p. 8, Line 47: "Enter the excess of your contributions (made by you or on your behalf) to your HSAs for 2025 from Form 8889, line 2 (unless withdrawn—discussed next), over your contribution limit (Form 8889, line 12). Also include on line 47 any excess contributions your employer made."

Note the instruction (i5329 p. 8) says "over your contribution limit (Form 8889, line 12)", while the existing `f8889.excess` tests `f8889.line2 > f8889.line12` and i8889 p. 8 says "subtract your deductible contributions (line 13) from your actual contributions (line 2)". With `f8889.line13 = smaller_of(line2, line12)` the two agree (line 2 − line 13 = line 2 − line 12 when positive). Checked in f8889.yaml (`f8889.line13_figured`).

### 3.4 Schedule 2 line 8

f1040s2 p. 1, line 8: "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required. If not required, check here".

i1040gi p. 112, Line 8, Exception: "If only item (1) applies and distribution code 1 is correctly shown in box 7 of all your Forms 1099-R, you don't have to file Form 5329. Instead, multiply the taxable amount of the distribution by 10% (0.10) and enter the result on line 8. The taxable amount of the distribution is the part of the distribution you reported on Form 1040, 1040-SR, or 1040-NR, line 4b or 5b, or on Form 4972. Also check the box on line 8 to indicate that you don't have to file Form 5329. But you must file Form 5329 if distribution code 1 is incorrectly shown in box 7 of Form 1099-R or you qualify for an exception".

New lines:

- `s2.line8` = `sum_over person` of (`f5329.line4` + Part VII line 49). Arithmetic is the same on both paths (with no exception, line 4 = 10% of the taxable code 1 amounts).
- `s2.line8_box` (Bool, display): true when line 8 > 0 and no person requires Form 5329, where `f5329.required` = any entry with code S, any `retirement.excepted` > 0, or line 49 > 0. Proposed reading for joint returns: D10.

### 3.5 Parts not computed (refusal text and the triggering facts)

| Part | Printed heading (f5329) | Refusal trigger (new per-person or per-entry inputs) |
|---|---|---|
| II | "Additional Tax on Certain Distributions From Education Accounts and ABLE Accounts." | taxable Coverdell, QTP or ABLE distribution (already refused as Schedule 1 other income by `scope.schedule1`) |
| III | "Additional Tax on Excess Contributions to Traditional IRAs." | contributed more than allowed for 2025, or an amount on line 17 of the 2024 Form 5329 |
| IV | "Additional Tax on Excess Contributions to Roth IRAs." | same for Roth, line 25 of 2024 |
| V | "Additional Tax on Excess Contributions to Coverdell ESAs." | as printed |
| VI | "Additional Tax on Excess Contributions to Archer MSAs." | already refused by `f8889.unsupported` (Archer MSA contributions) |
| VIII | "Additional Tax on Excess Contributions to an ABLE Account." | as printed |
| IX | "Additional Tax on Excess Accumulation in Qualified Retirement Plans (Including IRAs)." | did not receive the full required minimum distribution |

A single new per-person screen `f5329.unsupported` can carry all of these, worded from the part headings, plus the Part I special cases of D3. That gate is unmeasured by the estimate (no SOI split).

---

## 4. Rules

### 4.1 Who must file (i5329 p. 1, Who Must File)

- "You received a distribution subject to the tax on early distributions from a qualified retirement plan (other than a Roth IRA). However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don't have to file Form 5329."
- "You received a distribution subject to the tax on early distributions from a qualified retirement plan (other than a Roth IRA) and you meet an exception to the tax on early distributions from the list shown later, but box 7 of your Form 1099-R doesn't indicate an exception or the exception doesn't apply to the entire distribution."
- "In general, you must file Form 5329 to report an exception to the 10% additional tax on an early distribution from a qualified retirement plan, including an IRA."

### 4.2 Definitions

- Qualified retirement plan, i5329 p. 1: "A qualified retirement plan includes: • A qualified pension, profit-sharing, or stock bonus plan (including a 401(k) plan); • A tax-sheltered annuity contract (403(b) plan); • A qualified annuity plan; and • An IRA." So "qualified retirement plan distributions" in the exception list include IRAs unless the exception says otherwise.
- Not subject to the additional tax at all (i5329 p. 3): "A qualified HSA funding distribution from an IRA", conversions, Roth rollovers, in-plan Roth rollovers, certain excess IRA contributions, "A distribution of excess deferrals", excess aggregate contributions, and "A distribution from an eligible governmental section 457 deferred compensation plan to the extent the distribution isn't attributable to an amount transferred from a qualified retirement plan." Each of these is either refused by `retirement.special` today or comes with a code other than 1 or S (i1099r p. 18, Code 2 bullets).
- Disaster distributions, i5329 p. 2 (TIP): "Qualified disaster recovery distributions aren't subject to ... the additional 10% tax (or the 25% additional tax for ... certain distributions from traditional SIMPLE and Roth SIMPLE IRAs) on early distributions and aren't required to be reported on Form 5329." The current `retirement.special` question does **not** mention disaster distributions, though its refusal names "8915-F" (checked in retirement.yaml). Once code 1 is computed this becomes a silent overstatement unless a screen asks (D3).

### 4.3 Box 7 codes the payer uses (i1099r Table 1, pp. 18-20)

- Code 1, i1099r p. 18: "Use Code 1 only if the participant has not reached age 59 1 / 2 , and you do not ... know if any of the exceptions under Code 2, 3, or 4 apply. However, use Code 1 even if the distribution is made for medical expenses, health insurance premiums, qualified higher education expenses, a first-time home purchase, a qualified reservist distribution, a qualified birth or adoption distribution, an emergency personal expense distribution, a terminally ill individual distribution, or an eligible distribution to a domestic abuse victim". (The quote checker may not match the "59 1 / 2" spacing; quoted as extracted.) So the exceptions a code 1 filer must claim on Form 5329 are exactly 05, 07, 08, 09, 11, 19, 20, 22, 23, plus any the payer did not know of (01, 02, 03, 06 and so on) and 12 when the code is wrong.
- Code 1 also, i1099r p. 18: "Code 1 must also be used even if a taxpayer is age 59 1 / 2 or older and they modify a series of substantially equal periodic payments". That is the SEPP recapture, reported differently (p590b p. 26, "Report the recapture tax (including the interest on the deferral periods) on line 4 of Form 5329. Attach an explanation to the form. Don't write the explanation next to the line or enter any amount for the recapture on line 1 or 3 of the form."). Refuse (D3).
- Code 2, i1099r p. 18: "Use Code 2 only if the participant has not reached age 59 1 / 2 and you know the ... distribution is the any of the following." (the bullets: Roth conversion, IRS levy, governmental 457(b), separation at 55, public safety employees, SEPP, EACA withdrawals, other 72(q), (t), (u) or (v) exceptions).
- Code 4, i1099r p. 18: "Use Code 4 regardless of the age of the participant to indicate payment to a ... decedent's beneficiary, including an estate or trust." Exception 04 (death) then applies.
- Code 7, i1099r p. 19: "Use Code 7: (a) for a normal distribution from a plan, including a traditional IRA, section 401(k), or section 403(b) plan, if the employee/taxpayer is at least age 59 1 / 2".
- Code S, i1099r p. 20: "Use Code S only if the distribution is from a SIMPLE IRA in the first 2 years, the ... employee/taxpayer has not reached age 59 1 / 2 , and none of the exceptions under section 72(t) are known to apply when the distribution is made." (extraction splits "J" into the sentence; the allowed combination is J... not relevant.)
- Two codes: i1099r p. 15: "Enter a maximum of two alphanumeric codes in box 7." Combinations with 1 (1 and 8, 1 and B, 1 and D, 1 and K, 1 and L, 1 and M, 1 and P, per Table 1 "8, B, D, K, L, M, or P") stay `other` and refused.

### 4.4 The exceptions (i5329 p. 5, "Exceptions to the Additional Tax on Early Distributions")

| No. | Text (abridged; i5329 p. 5) | Plan or IRA | Detectable from inputs | Cap in archived text |
|---|---|---|---|---|
| 01 | "Qualified retirement plan distributions (doesn't apply to IRAs) you received after separation from service when the separation from service occurs in or after the year you reach age 55" (50 for public safety, or 25 years) | plan only | filer fact | none |
| 02 | "Distributions made as part of a series of substantially equal periodic payments" | both | filer fact | none |
| 03 | "Distributions due to total and permanent disability." | both | code 3 shows it; else filer fact | none |
| 04 | "Distributions due to death (doesn't apply to modified endowment contracts)." | both | code 4 | none |
| 05 | "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." | both | **computable** from `sa.line4` (D5) | the medical excess |
| 06 | "Qualified retirement plan distributions made to an alternate payee under a qualified domestic relations order (doesn't apply to IRAs)." | plan only | filer fact | none |
| 07 | "IRA distributions made to certain unemployed individuals for health insurance premiums." | IRA only | filer fact (p590b p. 25 conditions) | premiums paid (filer) |
| 08 | "IRA distributions made for qualified higher education expenses." | IRA only | filer fact | expenses (filer) |
| 09 | "IRA distributions made for the purchase of a first home, up to $10,000." | IRA only | filer fact + prior use | $10,000 lifetime (p590b p. 27, item 3) |
| 10 | "Qualified retirement plan distributions made due to an IRS levy." | both | usually code 2 | none |
| 11 | "Qualified distributions to reservists while serving on active duty for at least 180 days." | both | filer fact | none stated |
| 12 | "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R." | both | filer fact (age at receipt) | the part received at or after 59½ |
| 13 | "Distributions from a section 457 plan, which aren't from a rollover from a qualified retirement plan." | 457 | filer fact | none |
| 14 | pre-March 1, 1986 written election (three conditions) | plan | filer fact | none |
| 15 | "Distributions that are dividends paid with respect to stock described in section 404(k)." | plan | code U, which is `other` today | none |
| 16 | annuity investment before August 14, 1982; "see Tax on Early Distributions under Special Additional Taxes in Pub. 575" | annuity | refuse (Pub. 575 not archived; annuity contracts outside the plan path) | — |
| 17 | "Distributions that are phased retirement annuity payments made to federal employees." | plan | filer fact; Pub. 721 not archived | none |
| 18 | "Permissible withdrawals under section 414(w) from eligible automatic contribution arrangements." | plan | usually code 2; these go on line 1h (f1099r p. 7, Box 1) which is refused | — |
| 19 | "Qualified birth or adoption distributions. A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000" | both | filer fact; statement attached | $5,000 (per child per i5329; "per taxpayer" per p590b p. 28; Q3) |
| 20 | "Distributions due to terminal illness." | both | filer fact | none |
| 21 | "Corrective distributions of the income on excess contributions distributed before the due date of the tax return" | IRA | code 8/P combinations, refused | — |
| 22 | "Qualified distributions to victims of domestic abuse." | both | filer fact | p590b p. 28: "the lesser of $10,300 for 2025 or 50% of the present value of the IRA" |
| 23 | "Distributions for eligible emergency expense distributions." | both | filer fact | p590b p. 28: "the lesser of $1,000 or your total interest in the IRA minus $1,000"; one per calendar year |
| 99 | "Enter this exception number if more than one exception applies." | | | |

Supporting rule text:

- Medical, p590b p. 25: "You can only take into account unreimbursed medical expenses that you would be able to include in figuring a deduction for medical expenses on Schedule A (Form 1040). You don't have to itemize your deductions to take advantage of this exception to the 10% additional tax." and "Adjusted gross income (AGI). This is the amount on Form 1040, 1040-SR, or 1040-NR, line 11a."
- Health insurance, p590b p. 25: the four conditions beginning "You lost your job." and "for 12 consecutive weeks because you lost your job."
- Higher education, p590b p. 26: "The part not subject to the tax is ... generally the amount that isn't more than the qualified higher education expenses (defined next) for the year". The 2025 p590b also lists "Additional qualified education expenses in connection with elementary and secondary tuition" (p. 26) under this IRA exception (Q4).
- First home, p590b p. 27: "When added to all your prior qualified first-time homebuyer distributions, if any, total qualifying distributions can't be more than $10,000." and the TIP "If both you and your spouse are first-time homebuyers (defined later), each of you can receive distributions up to $10,000 for a first home without having to pay the 10% additional tax."
- Repayments of exceptions 19, 20, 22, 23 go on Form 8606 (p590b p. 2: "repaid, in whole or part, emergency personal expense distributions, qualified birth or adoption distributions, a domestic abuse victim distribution, or a terminally ill individual distribution. If you have, file Form 8606.") Refuse a repayment.

### 4.5 HSA excess (Part VII)

- p969 p. 8, Excess contributions: "Excess contributions aren't deductible. Excess contributions made by your employer are included in your gross income. If the excess contribution isn't included in Form W-2, box 1 you must report the excess as "Other income" on your tax return. Generally, you must pay a 6% excise tax on excess contributions."
- Withdrawal, i8889 p. 8: "you can withdraw some or all of your excess contributions for 2025 and they will be treated as if they had not been contributed if: • You make the withdrawal by the due date, including extensions, of your 2025 tax return" ... "You also withdraw any income earned on the withdrawn contributions and include the earnings in "Other income" on your tax return for the year you withdraw the contributions and earnings."
- i5329 p. 8, Line 43: "Also include on your 2025 Form 8889, line 13, the smaller of: • Form 5329, line 43; or • The excess, if any, of Form 5329, line 42, over Form 5329, line 44." Only with a prior-year excess (refused).

### 4.6 Excess IRA contributions (Parts III and IV, for D9)

- p590a p. 35: "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year." and "The tax can't be more than 6% of the combined value of all your IRAs as of the end of your tax year."
- i5329 p. 6, Line 10: "Also include on line 11a or 11b of the IRA Deduction Worksheet—Schedule 1, Line 20, in the Instructions for Form 1040, the smaller of: • Form 5329, line 10; or • The excess, if any, of Form 5329, line 9, over the sum of Form 5329, lines 11 and 12". A Part III with a prior-year excess feeds the IRA deduction (Schedule 1, AGI). Line 10 depends on compensation and contributions, not AGI, so no cycle (inferred).
- i5329 p. 7, Line 19, Roth limit "may be further reduced or eliminated if your modified AGI for Roth IRA purposes is over: • $236,000 if married filing jointly or qualifying surviving spouse; • $150,000 if single, head of household, or married filing separately and you didn't live with your spouse at any time in 2025". The reduction is Pub. 590-A Worksheets 2-1 and 2-2 (p590a pp. 41, 43), which use `prorate` (line 5, "rounded to at least three places") and `round` up to $10 with a $200 floor (line 8, "Round the result up to the nearest $10. If the result is less than $200, enter $200"). Both atoms exist.

### 4.7 Part IX (for the record)

i5329 p. 9: "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." and "The additional tax is reduced to 10% of the excess accumulation if you meet certain requirements." The reduced rate depends on a distribution "during the correction window" (i5329 p. 10) and a waiver may be requested ("Enter "RC" and the amount of the shortfall you want waived in parentheses", i5329 p. 10). Refuse.

---

## 5. Ordering and every existing line that changes

Form 5329 taxes are Schedule 2 Part II "Other Taxes". They enter `s2.line21` → `f1040.line23` → `f1040.line24` (total tax) → the amount owed or refund. Nothing in the project reads them back into AGI, taxable income, `f1040.line18` (the credit-limit base of Schedule 3, Schedule 8812 and the Stage 15 credit limit worksheets) or the earned income credit (checked: the only readers of `f1040.line24` are within f1040.yaml, lines 851 and 881; `s2.line21` is read only by `f1040.line23` and listed in interview/stage4-2025.yaml). Form 5329 reads AGI (exception 05) and the taxable amounts, so there is no cycle.

Lines and definitions that change:

| Id | Change |
|---|---|
| params `enums.retirement_code` | add `early_1`, `simple_S` (and `disability_3` if D8); update its citation |
| `retirement.code` | the question's list of codes |
| `retirement.bad_code` | unchanged test (`other`), but its refusal remedy "a distribution code other than 7, 4, 2, G or Q" changes; add `simple_S` only with `account = traditional_ira` (a SIMPLE IRA is reported with the IRA box; i1099r p. 15 "Enter an "X" in the IRA/SEP/SIMPLE checkbox") — proposed gate that code S on a `plan` entry is refused |
| `retirement.special` | delete "an early distribution with no known exception (code 1, J or S)" from the question (code J stays refused by `bad_code`'s Roth test); keep the rest. The coverage category then loses this gate (`categories.json` edit) |
| new `retirement.early_special` (or added to `f5329.unsupported`) | disaster recovery distribution (Form 8915-F), SEPP modified (recapture), annuity contract or MEC early distribution, repayment of an exception 19/20/22/23 distribution |
| `retirement` collection | gain `parent: person` (D1), or an owner field; fixtures of Stage 10 re-keyed |
| `f1040.line4a`, `.line4b`, `.line4c`, `.line5a`, `.line5b`, `.line5c` | if D1 re-parents: become `sum_over person` of new person-level sums (the pattern of `f1040.line1a` over `person.box1`) |
| Stage 15 Form 8880 line 4 | if D1 re-parents: its return-level `sum_over retirement` becomes a `sum_over person` of a person-level sum (on a joint return both spouses' amounts go in both columns, so the return-level total is still what it needs) |
| `s2.other` | reworded: remove "the additional tax on early retirement" distributions and "excess contributions to an HSA" from what it asks; keep "additional tax on HSA distributions" (line 17c) and the rest; add a pointer that Form 5329 Part I and current-year HSA excess are computed |
| new `s2.line8` | `sum_over person` of person-level Form 5329 total |
| new `s2.line8_box` | display Bool |
| `s2.line21` | `sum` gains `s2.line8` (printed "Add lines 4, 7 through 16, 18, and 19") |
| `f8889.excess` | split: own excess → computed (Part VII); employer excess → still refused unless Schedule 1 other income exists |
| `f8889.unsupported` | unchanged (prior-year excess, distributions, QHFD stay refused) |
| new `sa.line4` reader | exception 05 reads `sa.line4` (medical expenses less 7.5% of AGI) |
| `interview/questions-2025.yaml` | the new per-entry questions, ordered after `retirement.taxable` inputs; the HSA year-end value; `f5329.unsupported` |
| `tools/coverage/categories.json` | `form5329` gates replaced by the residual gates (`f5329.unsupported`, the narrowed `s2.other`), or the category marked retired |
| ambiguity register | D5, D6, D10 and Q1 to Q6 readings |

Estimated tax penalty: i1040gi p. 65 excludes "Forms 8828, 4137, 5329 (Parts III through IX only), and 8919" from "tax shown on your return". The project does not compute the penalty (spec 2.2), so nothing changes; note it if Form 2210 is ever encoded.

---

## 6. Refuse-or-compute candidates

| Situation | Why hard | Recommendation |
|---|---|---|
| Code 1, no exception | none | **Compute** (direct Schedule 2 path) |
| Code 1 with one exception per entry | needs per-entry inputs; account-type validity | **Compute**; refuse 01/06 on IRA entries and 07/08/09 on plan entries |
| More than one exception on one entry | one amount per exception; code 99 | Refuse in a first build, or allow two amount inputs (D6) |
| Exception 05, medical | joint allocation across spouses; itemizing irrelevant | **Compute** cap from `sa.line4`; refuse when both spouses claim 05 (D5) |
| Exceptions 09, 19, 22, 23 | caps depend on prior use or account value | Cap the fixed dollar amounts; filer attests the rest (D4) |
| Exception 12 (code wrong, age 59½ or more) | age at receipt | **Compute** from the filer's amount |
| Code S | 25% rate; exceptions split between S and non-S | **Compute** (per-entry exceptions make the split exact) |
| Code 2 where the exception covers only part | needs the uncovered amount | Refuse (rare) |
| Code 7 or 4 when the filer was in fact under 59½ / not a beneficiary | payer error | Refuse via the screen |
| SEPP modified (recapture) | prior-year tax plus interest | Refuse |
| Qualified disaster recovery distribution | Form 8915-F | Refuse (screen; also a gap today) |
| Designated Roth account (code B), recapture (box 10) | Pub. 575 | Refuse (code B is `other` today) |
| Roth IRA nonqualified (J, T) | Form 8606 | Refuse (today) |
| Code 3 IRA | none | Compute if D8 |
| Part VII, current-year own excess | year-end value input | **Compute** |
| Part VII, employer excess | also "Other income" | Compute only if Schedule 1 line 8z exists; else refuse |
| Part VII, excess withdrawn by the due date | earnings are other income | Accept withdrawn amount as reducing line 47; refuse when earnings > 0 and no line 8z (D7) |
| Part VII, prior-year excess | lines 42-46, Form 8889 line 16 | Refuse (today) |
| Parts III/IV | carryovers, values, Roth MAGI worksheet, 2026 code P forms | Refuse first; candidate later (D9) |
| Parts II, V, VI, VIII, IX | other forms or rare | Refuse |

---

## 7. Parameters for `params/2025.yaml` (cents; Rate as num/den)

| Name | Value | Locator |
|---|---|---|
| `f5329.early_rate` | Rate 10/100 | f5329 p. 1, line 4, "Additional tax. Enter 10% (0.10) of line 3."; i1040gi p. 112, "multiply the taxable amount of the distribution by 10% (0.10)" |
| `f5329.simple_rate` | Rate 25/100 | i5329 p. 5, Line 4, "you must multiply that amount by 25% instead of 10%" |
| `f5329.excess_rate` | Rate 6/100 | f5329 p. 2, line 49, "Enter 6% (0.06) of the smaller of line 48" (same at lines 17, 25, 33, 41, 51) |
| `f5329.first_home_cap` | 1000000 | i5329 p. 5, exception 09, "up to $10,000"; p590b p. 27 |
| `f5329.birth_adoption_cap` | 500000 | i5329 p. 5, exception 19, "a distribution of up to $5,000" |
| `f5329.abuse_cap` (if D4) | 1030000 | p590b p. 28, "the lesser of $10,300 for 2025" |
| `f5329.emergency_cap` (if D4) | 100000 | p590b p. 28, "the lesser of $1,000" |
| `sa.medical_rate` | existing (7.5%) | reused by exception 05; i5329 p. 5, exception 05, "minus 7.5% of your adjusted gross income" |
| For D9 only: IRA limits | 700000 / 800000 | i5329 p. 6, Line 10, "$7,000 ($8,000 if age 50 or older at the end of 2025)" (likely added by roadmap item 2) |
| For D9 only: Roth phase-out starts | 23600000 (mfj, qss) / 15000000 (single, hoh, mfs apart) / 0 (mfs together) | i5329 p. 7, Line 19 |
| For D9 only: Roth phase-out widths | 1000000 (mfj, qss, mfs together) / 1500000 | p590a p. 43, Worksheet 2-2, line 4 |
| Part IX rates (not needed if refused) | 25/100, 10/100 | f5329 p. 3, lines 54a and 54b |

---

## 8. Open questions (readings the text leaves undecided)

- **Q1. Which distributions go on line 1 when the form is filed.** i5329 p. 3, Line 1 says "Enter the amount of early distributions includible in income", which on its face includes code 2 distributions already excepted by the payer; the form is filed for code 1 exceptions. Including code 2 amounts on lines 1 and 2 changes no tax. Proposed reading: only code 1 and S entries; record it.
- **Q2. "All your Forms 1099-R" on a joint return.** i1040gi p. 112 lets the filer skip Form 5329 if code 1 is correct on "all your Forms 1099-R". When one spouse must file Form 5329 (an exception) and the other has only code 1 with no exception, does the second spouse file a Form 5329 too, and is the line 8 box checked? Proposed: prepare a Form 5329 for each person with an early distribution whenever any person must file, and leave the box unchecked; the tax is the same either way.
- **Q3. The $5,000 birth or adoption cap.** i5329 p. 5 says "a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted" (per child), p590b p. 28 says "must not exceed $5,000 per taxpayer". Proposed: per child per person (cap × number of children born or adopted, a Count input), noting the p590b phrasing.
- **Q4. K-12 expenses under the IRA higher-education exception.** p590b p. 26 lists "Additional qualified education expenses in connection with elementary and secondary tuition" under the IRA exception; i5329 exception 08 says only "qualified higher education expenses". This may be an editorial carry-over from the QTP rules. Proposed: take the filer's amount as stated and record the tension; do not compute it.
- **Q5. Medical exception on a joint return.** Exception 05 is "up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI)". On a joint return AGI and the Schedule A medical amount are joint; the text does not say whether both spouses' Forms 5329 may each use the whole excess. Proposed: refuse when both spouses claim 05 with a combined claim above the excess; when one spouse claims it, cap at `sa.line4`.
- **Q6. Rounding.** Line 4 is 10% of line 3 in cents; the project rounds `multiply_rate` half-up to the cent. Per person (the form) versus per distribution (i1040gi's "multiply the taxable amount of the distribution") can differ by a cent on the direct path. Proposed: per person, as the form does.
- **Q7. Is `sa.line1` always asked?** Exception 05 needs unreimbursed medical expenses whether or not the filer itemizes. Not checked whether the interview asks Schedule A line 1 of a filer taking the standard deduction; the authoring stage must check, and if not, ask a per-return medical input only when an entry claims 05.

---

## 9. Draft owner decision batch

Each item: the recommended answer first, then the alternative.

- **D1. Who owns a Form 1099-R.** Recommended: give `retirement` the parent `person` (one roster per person, like Form W-2), moving Form 1040 lines 4a to 5c to `sum_over person`, and re-keying the Stage 10 fixtures. Alternative: an owner Enum on each entry and return-level per-role sums (two copies of every Form 5329 line, one per role), which avoids moving the collection but duplicates the form.
- **D2. Scope.** Recommended: Part I (codes 1 and S, per-entry exceptions, the direct path), Schedule 2 line 8, Part VII for the current year's own excess; everything else refused with citations. Alternative: also Parts III and IV (see D9), or Part I only.
- **D3. The special-cases screen for early distributions.** Recommended: a new per-entry screen, asked for code 1 or S, covering a qualified disaster recovery distribution, a modified SEPP (recapture), a distribution from an annuity contract or modified endowment contract, a repayment of an exception distribution, an exception that covers only part of a code 2 distribution, and a code 7 or 4 that is wrong. Alternative: fold these into `retirement.special`. Either way the disaster-distribution gap in the present screen is closed.
- **D4. Exception caps.** Recommended: the per-entry amount is capped by the entry's taxable amount; exception 05 by the medical excess (D5); 09 by $10,000 less a per-person input of earlier first-home distributions; 19 by $5,000 times a count of children (Q3); 22 at $10,300 and 23 at $1,000 (the account-value parts attested by the filer); the others as the filer enters them, with a notice. Alternative: no computed caps (the filer's amount, capped only by the taxable amount).
- **D5. Medical exception.** Recommended: compute the cap from `sa.line4`, refuse when both spouses claim more than it in total (Q5). Alternative: let each spouse use the whole excess.
- **D6. The exception number on line 2 and more than one exception.** Recommended: one exception per Form 1099-R entry (Enum input); the values sheet shows each entry's number and the rendering says to enter 99 when a person's entries differ; refuse two exceptions on one entry. Alternative: a per-person printed-number input, or two exception slots per entry.
- **D7. HSA excess.** Recommended: Part VII line 47 from the existing Form 8889 lines, less a new input of the excess withdrawn by the due date; a year-end value input; refuse excess employer contributions and withdrawn earnings unless Schedule 1 other income exists by then. Alternative: keep `f8889.excess` refusing everything.
- **D8. Code 3 for an IRA.** Recommended: accept (line 4b, no additional tax). Alternative: keep refusing code 3.
- **D9. Parts III and IV.** Recommended: refuse in this stage; revisit when the IRA deduction stage has the contribution and compensation inputs (the Roth worksheet's atoms exist). Alternative: compute current-year excess only (lines 15 and 23, with the year-end value) and refuse carryovers.
- **D10. Joint returns and the line 8 box.** Recommended: Q2's reading (any person files, then every person with an early distribution gets a Form 5329; box checked only when no one files). Alternative: per person, the second spouse's tax entered directly on line 8 next to the first spouse's Form 5329.
- **D11. Readings Q1, Q3, Q4, Q6.** Recommended: as proposed in section 8, each recorded in the ambiguity register. Alternative: refuse the situation instead of reading it (Q3 and Q4 only).
- **D12. Coverage bookkeeping.** Recommended: replace the category's gates with the residual gates (`f5329.unsupported` and the narrowed `s2.other`) and leave the IRS count, noting that the count includes the refused parts (an over-statement of what is retired). Alternative: drop the category as retired.

Twelve decisions; D1, D2 and D3 are the ones that shape the build.

---

## 10. Verified vs inferred

**Checked against the archived text** (read in `sources/2025/*.cols.txt` and `.txt`, and with `check_quotes.py`): every Form 5329 line text quoted (f5329 pp. 1-3, layout file); the i5329 Who Must File, definitions, Line 1, Line 2 exception table (layout file p. 5, numbers matched to texts), Line 4, Parts III to IX instructions; Schedule 2 line 8 (f1040s2 p. 1) and its instruction (i1040gi p. 112); the box 7 codes (f1099r pp. 7, 9) and Table 1 (i1099r pp. 18-20); the p590b exception texts and caps (pp. 24-28); p590a excess and Roth worksheet text (pp. 35, 40-43); p969 p. 8; i8889 pp. 7-8; the estimated-penalty exclusion (i1040gi p. 65).

**Checked against the repository:** the category entry and its share (categories.json, filer_coverage.md); the SOI cell values (spreadsheet); the `retirement` lines, the `retirement_code` enum and that codes 1, 3, S are `other`; `retirement` has no parent; the checker's `sum_over` parent rule (engine/src/check.ts); `s2.yaml` lines and that `s2.line21` sums only lines 4, 11, 12; the other readers of `s2.other`; `f8889` lines 2, 8, 11, 12, 13, `f8889.excess` and `collection.parent: person`; `sa.line1`, `sa.line3`, `sa.line4`, `sa.medical_rate`; the `round` atom with `rule: up` in use (s8812.yaml).

**Inferred, not checked:** that most of the 5.1 million returns are code 1 early distributions (from the average amount only); that the SOI amount is in thousands; that roadmap items 1 to 6 land first with the shapes assumed (in particular Schedule 1 line 8z and the IRA contribution inputs); that the Schedule A medical input is asked of non-itemizers (Q7); that the evaluator (not only the checker) would accept a re-parented `retirement` without other changes; the page-number convention for i1040gi beyond p. 112; anything in the unarchived documents of section 2, notably the statutory basis for the joint-return medical reading (Q5), which is my inference.

**Quote check** (`python3 -I /tmp/premises/check_quotes.py`, run on the final file). Every remaining miss is one of:
(a) project text, not IRS text: the `retirement.special`, `retirement.bad_code`, `s2.other` and `f8889.excess`
wording (forms/2025/*.yaml; several wrap across YAML lines, so a flat grep misses them), the coverage report and
categories.json strings, the checker message in engine/src/check.ts, the spec 2.4 roadmap phrase and the brief's
phrase; (b) IRS text quoted on a line that also names another document, so the checker searched the wrong one:
the Part VII table rows (the quotes are f5329 p. 2, found there), the Part VI heading (f5329 p. 2), and the
exception-table rows 07, 09, 18, 22, 23 (the quotes are i5329 p. 5, found there; the other document named on the
row is the cap source). Passages the extraction interleaves (the i1099r Table 1 column of allowed code
combinations, the i5329 TIP boxes, a p590b page break) are quoted in parts joined by "...", and those parts match.
