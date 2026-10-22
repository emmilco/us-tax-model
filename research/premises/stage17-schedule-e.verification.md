> Adversarial verification of `stage17-schedule-e.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 12 errors and 5 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification: research/premises/stage17-schedule-e.md

Checked read-only against `sources/2025/` (cols text, form-feed pages), `forms/2025/`, `params/2025.yaml`,
`engine/src/`, `spec/spec.md`, `tools/coverage/` and `reports/2025/filer_coverage.md` at HEAD 1c465c2.
Every double-quoted passage in the map was searched automatically in the archived page text: 346 quotes in total.
224 matched the cited document and page exactly. 121 are table cells with no inline locator, and each of those
was found in the form whose rows the table gives (f1040se pp. 1-2, f8582 p. 1, f1065sk1/f1120ssk p. 1, f1041sk1 p. 2).
One was a parsing artifact (nested curly quotes), and I checked it by hand (i1040se pp. 4, 6). No quote is
missing from the archive. The errors below are about meaning, project facts, internal cross-references, and
inferences.

## Errors

E1. **The list of lines `scope.schedule1` refuses is incomplete** (§1.1, bullet 1; also §5.2).
The map says the gate refuses "at `scope.ready`, `f1040.line8`, `s8812.eiw_4` and `eic.step2_other`".
`grep "when: scope.schedule1" forms/2025/` also finds `f1040.line10`, `s8812.eiw_3` (form "Earned Income Worksheet,
lines 2a–2e (statutory employee, farm or partnership income)"), `eic.step5_line1`, `eic.clergy`, `ssb.line6`,
`s1a.line5_calc` (form "Schedule 1-A, line 5 (qualified tips in a trade or business, with Schedule C, E or F)") and
`s1a.line14b_calc`. These refusals were already there at fcd2c26, so the map was wrong when written.
Narrowing the gate lifts all of them at once. That means `s1a.line5_calc` (tips in a Schedule E trade or business)
and `s8812.eiw_3` (partnership income) need their own new gates or their own computation. §5.2 lists only
`s1.sc_1a` and `s8812.eiw_2b`.
Affects: §5.2, and indirectly D13 and D15.

E2. **"`eic.step2_other` ... unchanged unless D15" is wrong** (§5.2, row `eic.step2_other`; D15).
`forms/2025/eic.yaml` defines `eic.step2_other` as `all(scope.schedule1 == false, scope.other_line16 == false)`
and refuses `when: scope.schedule1` with the remedy "Schedule E, rental of personal property and passive activity
income are outside this tool". Once the stage drops the Schedule E / K-1 clause from `scope.schedule1`, this line
stops refusing Schedule E filers. Keeping D15's recommendation, "keep refusing the EIC for Schedule E filers",
therefore takes a new gate on this line, such as a Schedule E or passive-activity Bool. Leaving the line unchanged
would compute the EIC without Pub. 596 Worksheet 1. Affects: D15.

E3. **The reason given for not reusing `asset` is false** (§3.0, bullet 1).
The map says `asset` "reads enclosing-entry lines of `sc` (`sc.one_cent`, `sc.hundred_cents`, `sc.fifty_cents`,
`sc.bonus_rate_40`, `sc.conv_hy`)". They are year parameters, not lines of `sc`: `asset.yaml` reads them as
`op: param, ref: sc.one_cent`, and they are defined in `params/2025.yaml` (for example line 1497, `sc.one_cent: type:
NonNegDollars, value: 1`). The only other things `asset.yaml` references are `mq.applies` (return level) and the param
`sales.zero`. What actually ties `asset` to `sc` is `collection.parent: sc` (asset.yaml line 1064), together with
the screen and enum limits. A new `rasset` is still needed for that reason, so D1's outcome holds but its stated
reason does not.
Affects: D1 (rationale only).

E4. **"The estimator counts the group as retired once `scope.schedule1` no longer refuses it" is wrong** (§1.1, paragraph
after the table; §5.2, last row). `tools/coverage/estimate.py` line 154 is `refused = [c for c in cats if c.get("refused",
True)]`. Whether a category counts as retired depends on the `refused` flag in `categories.json`, not on the gates
in the forms. Stage 15 retired its categories by editing that file (`"gates": [], "refused": false`, with a
label "supported since Stage 15; its remaining refusals are unmeasured gates"). The estimator also stops
(`SystemExit`) if `categories.json` names a gate that is not in the forms (lines 199-203). Stage 17 has to edit
`categories.json` the same way, and the §5.2 row should say so rather than "the new gates (unmeasured)".
Affects: §1.1 scope reasoning, §5.2.

E5. **Decision cross-references point at the wrong decisions** (§3.3, §3.4, §3.5, §6).
D14 is "Form 8582 display", but the map cites it as the code allow-list in: box 11 ("decision D14"), box 13 ("decision D14"),
box 15 ("D14"), box 20 ("if D14"), the 1041 box 14 F row ("(D14)") and R21 ("(D14)"). The allow-list is D13.
Box 28(c), foreign partnership, cites "decision D13", but foreign partnerships are in D10.
§3.3 ends "except a K-1 activity with a passive capital loss (decision D11)", but D11 is QBI, and no decision covers
the Part IX capital-loss case.
Affects: an owner ruling on D10, D11, D13 or D14 from these pointers would rule on the wrong item.

E6. **D13's allow-list contradicts the §3.4 box table.** The table computes 1065 box 15 code O (backup withholding
into `f1040.line25c`), and i1065sk1 p. 34 confirms "Code O. Backup withholding". It treats box 16 (K-3) as display
and box 17 as "covered by the existing `s2` AMT screen; help text". D13's recommended allow-list (1065 "boxes 1-9c,
14A, 18A-C, 19 ..., 20 A, B, N, Z, AJ"; "everything else refused by name") leaves out 15 O, 16 and 17. D13 also
puts 20 A and B in the recommended list, yet its alternative is "also ... 13H/20A into Form 4952", which overlaps,
while the table says "A, B into Form 4952 if D14".
Affects: D13.

E7. **§1.2 Compute item 1 contradicts D7 and R8 on land.** Item 1 computes "property types 1 to 4, and 8 with a
description" and so leaves out type 5 (Land; f1040se p. 1 type list). D7 recommends "compute land rental", and R8
says "compute land rental unless Form 8582 has a loss to offset".
Affects: D7 and the scope statement.

E8. **§1.2 and D6 disagree on Form 7203.** §1.2's Refuse list has "Form 7203 situations unless the owner adopts it
(see decision D6)", and §2.2 says Form 7203 is needed only "if decisions ... D6 choose to compute". D6's recommended
answer is to archive Form 7203 and compute Part I. That recommendation also rests on a document that is not
archived (`f7203` and `i7203` are absent from `manifest.json`), so it cannot be checked. Only the i1120ssk pp. 2-3
basis adjustments are archived.
Affects: D6.

E9. **Q2's counterexample does not hold for the rounding Pub. 527 uses** (§8 Q2; D4).
The map says rounding 10% to a whole day "would differ at, for example, 275 rental days and 28 personal days".
Pub. 527's example rounds down (p527 p. 27: 273 days rented, "10% of the total days rented to others at a fair
rental price is 27 days"). Personal days are a whole number p, so p > r/10 holds exactly when p > floor(r/10).
At 275/28 both tests give "used as a home". Rounding down therefore never differs from the exact test; only
rounding to the nearest day does (28 > 28 is false). D4's choice is unaffected, but the stated reason for it is wrong.

E10. **The rental QBI path collides with the R27 refusal** (D11 against §6 R27). D11 counts rentals as QBI "only on
a yes to the trade-or-business question". R27 refuses any rental real estate activity that is a trade or business,
because i1040se p. 7 says "If your rental real estate activity is a trade or business, you must file Form 8990 to deduct
any interest expenses of that rental real estate activity unless you meet one of the filing exceptions in the
Instructions for Form 8990". Form 8990 and its instructions are not archived. A section 162 rental that says yes
for QBI would be refused by R27 unless the Form 8990 exception is asked, and that exception cannot be cited from the
archive. The map does not address this interaction.
Affects: D11 and R27.

E11. **The rental section 179 rule is stated more broadly than the text** (§1.2 item 2, "No section 179 for rental
property"; R13, "not allowed for rental"). p946 p. 16 excludes "rental property (if renting property is not your
trade or business)". Refusing is still the safe choice, but the premise as written is not what the text says.
Affects: R13 (low).

E12. **The 31.5-year boundary is stated more narrowly than the text** (§3.2; D8, "years from ... May 13, 1993 (39)").
p946 p. 33 note 3 reads "31.5 years for property placed in service before May 13, 1993 (or before January 1, 1994, if
the purchase or construction of the property is under a binding contract in effect before May 13, 1993, or if
construction began before May 13, 1993)". A key of year plus month cannot separate May 1-12 from May 13-31, 1993,
and it cannot detect the binding-contract case. The encoding needs a question, or a refusal for property placed in
service in 1993.
Affects: D8.

## Out of date after Stage 15

O1. **Coverage figures** (§1.1). The map says the group is "step 3, `79.9% (+6.8)` after steps 1 and 2, `+4.3` if
covered alone now". The regenerated `reports/2025/filer_coverage.md` (64.7% overall) gives "| 2 | Rental, royalty,
partnership, S corporation, estate (Schedule E) | 79.1% (+6.7) | +4.8 |". The fcd2c26 report did read 79.9% / +6.8
/ +4.3, so the map was right when written. "Lower than 79.9%" should now read lower than 79.1%.

O2. **Roadmap numbering** (header paragraph, line 7). The map says "spec 2.4 roadmap item 3" and "Stage 16 (roadmap item 2, the
remaining Schedule 1 items)". `spec/spec.md` lines 92-93 now read "1. The remaining Schedule 1 income and
adjustments ... (72%)" and "2. Schedule E ... (79%)". The old item 3 carried "(80%, the first goal)". After
Stage 15, Schedule E no longer reaches the first goal; item 3, the premium tax credit, now does ("84%, the first goal").

O3. **The earned-income readers are no longer "moot"** (§5.2, row `person.eic_part1`, `person.eic_se_has`,
`person.eic_se`: "moot while the EIC is refused for Schedule E filers, D15"). Stage 15 added `person.dc_earned` and
`person.dc_earned_b` (person.yaml lines 1758-1780: "Form W-2 box 1, the person's share of line 1e, and Schedule SE
line 3 less the deduction on Schedule 1 line 15 (or the Schedule C profit ...)"), and both sum `person.eic_se`. Form
2441 is computed for Schedule E filers. Unless `person.eic_se` (or `dc_earned`) includes partnership SE earnings
(K-1 box 14 code A), a partner's dependent care credit is computed on understated earned income. This change is
required, not moot, whatever D15 decides.

O4. **The Earned Income Worksheet now feeds Credit Limit Worksheet B** (§5.2, row `s8812.eiw_2b`). Stage 15 added
`s8812.clwb_3`, which copies `s8812.eiw_7` ("Credit Limit Worksheet B, line 3. Enter your earned income from line 7 of
the Earned Income Worksheet"). Adding K-1 box 14 code A at `eiw_2b`, and lifting the `eiw_3` refusal (E1), now
changes Credit Limit Worksheet B as well. Stage 15's `f2441.line7` and `f8880.line8` (both `copy f1040.line11a`) are
correctly listed as AGI readers.

O5. **Minor.** The `scope.other_income` wording changed in Stage 15 (dependent care benefits are narrowed, and the
earned-income lines are now "1b to 1d and 1f to 1h"). The passive-activity clause the map quotes is unchanged and
still present. Also, `f1040.line1z` is now `sum(f1040.line1a, f1040.line1e)`, which the §4.5 MAGI build inherits
correctly by reading line 1z.

## Unverifiable

- **D6, Form 7203 Part I.** Its content, and whether "stock basis only" is a coherent cut, cannot be checked: Form 7203 is not archived.
- **D11 and Rev. Proc. 2019-38.** The safe-harbor conditions behind the rental QBI question are not archived. §2.2 nonetheless says that "only Pub. 596 and Form 7203 are needed by the recommended scope", and that is not true while D11 computes rental QBI.
- **D16 and Form 461.** Whether counting Schedule C plus Schedule E lines 26, 32 and 37 is "conservative" (for example, what Form 461 includes or excludes) cannot be checked: Form 461 is not archived.
- **Measured costs of the refusals.** The share of rentals needing Form 8582, Form 6198 or Form 7203, the share of S corporation shareholders with distributions ("likely few" income-only shareholders, D6), and the real estate professional count have no archived counts. The 4.3 M against 3.2 M comparison is the map's own labelled inference; both figures are confirmed as SOI cells.
- **Whether the IRS K-1 (1065, 1120-S) PDFs have a second page.** The archived text has one non-empty chunk each (confirmed), but the PDFs were not inspected.
- **Pub. 596 Worksheet 1** (D15). Not archived.

## Confirmed

About 345 quoted passages are present in the archive (224 at the exact cited page; 121 table cells on their form's page).
The decision-critical premises I confirmed:

- The SOI cells match the archived XLS, read with the estimator's header test: col 51 4,886,466; 53 4,336,173; 55/57 1,798,063/76,508; 59/61 325,953/67,356; 63 6,346,357; 65 3,196,282; 67/69 3,266,345/2,103,634; 71/73 4,138,040/1,415,974; 75/77 648,583/36,592. acg 55/57/111/113 are 495,780/560,758/1,219,800/766,861. Shares 5.9/3.5/0.4% are as in the report.
- `categories.json` has three `schedule_e` categories, each with the single gate `scope.schedule1`. `scope.other_income` is not listed for them, and it still asks about passive-activity income.
- The `scope.schedule1` text includes the Schedule E / K-1, rental-of-personal-property and Schedule F clauses as quoted.
- `f1040.line8` copies `s1.line10`. `s1.line10` is `sum(s1.line3, s1.line7)`. There is no `s1.line5`.
- `f8960.line4a`, `4b` and `7` copy zero and are typed NonNegDollars; `4c` is their sum.
- `sd.line5` and `sd.line12` copy zero behind `sd.other_forms`; `g28.line4`, `u1250.line5/10/11`, `s8812.eiw_2b` (copies `s1.line3`) and `s8812.eiw_4` are as stated.
- `person.se_line2` copies `person.sc_total`. The `person.se_screen` text has the K-1 box 14 code A clause. `qbi.unsupported` and `f8960.unsupported` are as quoted. `sc.passive` is false leads to `sc.screened`.
- `mq.q4` and `mq.total` sum `person.mq_*` over `sc`.
- `asset.screen` refuses real property and property placed before 2005. The enums `macrs_period` and `placed_year` (y2005-y2025) are as stated. `macrs_gds.yaml` holds Tables A-1 to A-5 plus the 15-year column of A-8 to A-12 only.
- `f1040.line2a` is `sum(tax_exempt_interest, div.box12)`. `sb.line2` sums over `interest`. `sb.line6` and `f1040.line3a` are supplied inputs. `f1040.line25c` and `f1040.line26` are supplied totals.
- `scope.ready` refuses `s3.mfs`. `sc.mileage_rate` is a 70-cent param. `qbi.threshold`, `s1.ebl_threshold`, `niit.threshold` and `se.*` exist.
- The engine has `multiply_count` (cents × Count, exact), `prorate` (half-up ratio to the stated places, clamped to [0, 1], whole > 0), `choose` (the checker requires money branches) and `keyed_lookup`. The dependency checker rejects cycles, so D3's "AGI less pieces" is a cycle by construction. The spec allows a collection entry to read only its enclosing entries (Q8).
- f8582 2025 Parts I-IX as described. Line 9 is zero when line 6 ≥ line 5 (the form's note), which matches `subtract_floor0`. The 2025 form has no separate worksheets.
- i8582: the Exception's conditions, the Line 6 MAGI exclusions and the $86,500 example, the routing of a prior-year loss without active participation in both years to Part V, Part VI/VII/VIII arithmetic, "must be the same as Part II, line 9", and the line-22 reporting. p925 p. 6 excludes "Passive activity income or loss included on Form 8582". i1040se p. 4 points MAGI to Pub. 925.
- The $25,000 allowance, the $100,000-$150,000 phase-out at 50%, and the MFS $12,500/$75,000/$50,000 amounts.
- The limitation order (basis, at-risk, passive, EBL) appears in both i1065sk1 p. 3 and i1120ssk.
- Limited partners: no active participation, and material participation only by tests 1, 5 or 6 (i1065sk1 pp. 9, 11).
- K-1 destinations as quoted: 1065 boxes 1-9c, 14A, 15 O (backup withholding, p. 34), 18A and 20 codes. 1120-S 17 V is the threshold of $197,300/$394,600; 17 AC is "Gross receipts for section 448(c)". The f1041sk1 p. 2 "Report on" column matches the table, including 13 A (line 26), 13 B (line 25c) and 14 H (Form 8960 line 7).
- S corporation income is not SE income. The basis "Part III" text in i1040se p. 8 is an erratum for Part II column (e), as the map says.
- Home test (more than the greater of 14 days or 10%), the under-15-day exclusion, the 7/70 division example, 85/99 (86%), and the p527 Worksheet 5-1 net-profit rule.
- The i4562 mid-month convention scope and the mid-quarter exclusion of real property. Tables A-6, A-7 and A-7a are on p946 pp. 73-74, with 3.182% for February year 1. The p527 3.636% year-6 example and its $213 loss.
- EIC Step 2 question 4 ("You are filing Schedule E ... Use Worksheet 1 in Pub. 596") is on i1040gi p. 40. It is reached only when investment income is at most $11,950 (or via Form 4797), which is narrower than "every Schedule E filer" but immaterial while the EIC is refused.
- Archived/not archived (`manifest.json`): every §2.1 document is present. p596, f7203, i7203, rp-19-38, f4797, i4797, f8582cr, i8582cr, f461, i461, f8990, i8990, f4835, p541, p534 and p535 are absent.
