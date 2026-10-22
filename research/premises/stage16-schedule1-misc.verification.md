> Adversarial verification of `stage16-schedule1-misc.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 6 errors and 7 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification of research/premises/stage16-schedule1-misc.md

Checker: read-only adversarial pass against `sources/2025/` and the repository at 1c465c2 (main). Nothing in the
repository was changed; no network; no model calls. Quotes were checked with a whitespace-, quote- and
line-break-hyphen-normalising search of `<doc>.cols.txt`, page by page (form-feed chunks); worksheet layout was read
in `<doc>.txt`.

## The cycle the integrating session could not confirm (IRA Deduction Worksheet and SSB Worksheet)

**Confirmed, on both extractions and in the YAML.**

- IRA worksheet line 3 does read Form 1040 line 9. `i1040gi.txt` lines 6977-6978 (p. 97, IRA Deduction Worksheet):
  "3. Enter the amount from Form 1040 or 1040-SR, / line 9". The same text is in `i1040gi.cols.txt` p. 97: "Enter the
  amount from Form 1040 or 1040-SR, line 9 . . . 3." Line 4 (layout line 6980): "lines 11 through 19a, plus 23 and
  25". The integrating session's hit was probably layout line 7099, which is the Student Loan Interest Worksheet's
  line 2 (p. 99), not the IRA worksheet's line 3.
- SSB worksheet line 6 does read Schedule 1 line 20. i1040gi p. 32 (layout line 2078): "6. Enter the total of the
  amounts from Schedule 1, lines 11 through 20, and 23 and 25". Line 3: "Combine the amounts from Form 1040 or
  1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8" (no 6b).
- Form 1040 line 9 contains 6b: f1040.yaml `f1040.line9` sums line1z, 2b, 3b, 4b, 5b, **6b**, 7a, 8; `f1040.line6b`
  is `copy ssb.line18`; `ssb.line3` sums f1040 lines 1z to 5b, 7a and 8; `ssb.line6` sums Schedule 1 lines.
- The checker's walk is structural: `engine/src/check.ts` `checkCycles` adds every `choose` guard operand and branch
  (`case "choose": for (const alt of expr.alternatives) { testOps(alt.guard); ... refs.push(alt.then)`), and also every
  refusal guard (`refs.push(...(line.refuses ?? []).map(r => r.when))`). So the chain ira.line3 -> f1040.line9 ->
  f1040.line6b -> ssb.line18 -> ... -> ssb.line6 -> s1.line20 -> ira.line12 -> ... -> ira.line3 would be a build error.
- The claim that no evaluation reaches it holds: p. 97 "If you checked "No" on line 1a (and "No" on line 1b ...), skip
  lines 2 through 6"; and the SSB exception (p. 31) "You made contributions to a traditional IRA for 2025 and you or
  your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub.
  590-A". The IRA pages (pp. 95-98) say nothing about social security; the cycle is closed only by the p. 31 exception.
- Encodings (a) and (b) both break it structurally, as far as a reading of the operands shows (not built). For (b),
  the twin's operands (line 7 limit by age, line 10 from W-2 box 1, `s1.line2a`, `person.sc_total`,
  `person.se_line13`, `person.s16`, line 11 input) do not reach `f1040.line9`.

One omission bears on D7 (listed under Errors, E1).

## Errors

**E1. R-IRA-1 is described as a new refusal; it already exists.** Map 5.2 ("both need the refusal R-IRA-1"), 6.1
R-IRA-1, D7 ("Refuse social security plus a traditional contribution plus coverage"). `forms/2025/ssb.yaml`
`ssb.pub915` (present at 6051ec0 as well) asks: 'Does any of these apply: you made contributions to a traditional IRA
for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment; ...' and
`ssb.line2` refuses `when: ssb.pub915` ("Pub. 915 or Pub. 590-A worksheet"). The D7 question is therefore not
whether to refuse but whether to keep the IRA clause as a self-reported question or derive it from the new
per-person coverage and contribution inputs (and split it out of `ssb.pub915`). Affects D7.

**E2. Line 25 (jury duty, 24a) is computed by the map's own scope but left out of three readers.** Map 3.4 line 4
("sum(s1.line11, 13, 15, 16, 17, 18, 19a) | lines 12, 14, 23, 25 refused"), 5.4 rows `sli.line3` ("add 18, 19a, 20")
and `ssb.line6` ("add 18, 19a and line 20"). The map recommends computing 24a and line 25 (3.6: line 25 "sum (24a
only)", "new"; D3 "8h with 24a"). The sources include line 25 in all three: IRA line 4, p. 97, "lines 11 through 19a,
plus 23 and 25"; SLI line 3, p. 99, "lines 11 through 20, and 23 and 25"; SSB line 6, p. 32, "lines 11 through 20,
and 23 and 25". Only line 23 stays refused. Affects D3 (and the 5.4 change list).

**E3. R-IRA-6 says combat pay is refused "(inherited)"; the existing refusal is local to other forms.**
`s8812.combat_pay` is a refusal guard only on `s8812` (line 414), `eic.step5_line4` (eic.yaml 796) and four
Form 2441 lines (f2441.yaml 565, 633, 984, 1044). A filer with nontaxable combat pay who claims none of the child
tax credit, the EIC or the dependent care credit is not refused today. IRA worksheet line 8 adds combat pay (p. 98,
"Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040,
line 1i"), so the IRA lines need their own `when: s8812.combat_pay` refusal. Affects D8 (refusal 6 is right; "no work
needed" is not).

**E4. R-EWP-1 says "Schedule B already refuses OID"; it refuses only OID not taken from a Form 1099-OID.**
`sb.yaml` `sb.unsupported`: 'Any nominee income, original issue discount reported in an amount other than on Form
1099-OID, ...'. OID reported on a Form 1099-OID passes the screen, so a Form 1099-OID early withdrawal penalty
(i1040gi p. 95, "The Form 1099-INT or Form 1099-OID you received will show the amount of any penalty") is not caught
by any existing refusal. Line 18 needs its own screen, or the per-payer input should accept the OID penalty. Affects
D2 (early withdrawal penalty).

**E5. The sales-tax branch of the refund rule is misstated.** Map 3.3, last sentence: "The sales-tax branch is
capped, not zeroed, by Pub. 525 (section 4.2, exception 4)." For an income-tax refund (the only kind on line 1),
i1040gi p. 88, Line 1, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn't
itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income
taxes"; p525 p. 24, Example 27: "Because you didn't choose to deduct the state income tax, you don't include the
state income tax refund in income." The cap (p525 p. 24, "limited to the excess of the tax you chose to deduct ...
over the tax you didn't choose to deduct") applies to an income-tax deducter (exception 4, p. 89) or to a sales-tax
refund (exception 2, refused). R-REF-1 ("Compute: line 1 is zero") is the correct reading; the 3.3 sentence
contradicts it. Affects D5 (the screen wording).

**E6 (minor locator).** Map 4.7: "Exceptions (p525 p. 21): student loans, deductible debt, price reductions, excluded
debt". Only "Student loans" (and the 2021-2025 rule) is on p. 21; "Deductible debt", "Price reduced after purchase"
and "Excluded debt" (a separate heading, with the bankruptcy and insolvency list) are on p. 22. No decision affected.

## Out of date after Stage 15

**O1. Coverage baseline.** Map 1.1, 1.2 and the greedy order use 65.32% "after Stage 15". `reports/2025/
filer_coverage.md` (regenerated at 8d7c0fd) now reads "**Estimated coverage: 64.7%**", and row 1: "Other Schedule 1
income and adjustments | 72.4% (+7.7) | +7.7" (the 6051ec0 report said 73.1% (+7.8)). Stage 15 left part of
`other_credits` refused (row 9, "+0.9"). Every absolute figure in the map (65.32, 73.10, 71.66, 70.73 and the greedy
endpoints) is about 0.6 to 0.7 points high; the increments (+7.78 for the group) are close to the report's +7.7. The
per-category gains and the +6.34 for the recommended set were not re-run (see Unverifiable). Affects D1 (the numbers
quoted, not the ranking).

**O2. The Stage 15 Form 8880 gate is `person.sav_trad`, and there is no separate R2 gate.** Map 5.3 item 1 ("its gate
id is in the landed Stage 15 encoding, not read here"; "Stage 15's R2 refusal (nondeductible contributions) goes with
it"). person.yaml: `person.sav_trad` 'Did you make contributions (other than rollover contributions) to a traditional
IRA for 2025, deductible or not, ...'; `person.sav_line1` is `copy person.sav_roth` and refuses `when:
person.sav_trad`. One question covers deductible and nondeductible contributions; the Roth input is `person.sav_roth`
(per person). Lifting the refusal means `person.sav_line1` becomes sum(`person.sav_roth`, the new traditional input)
and `person.sav_trad` is replaced by, or derived from, that input. Affects D10.

**O3. No Roth excess-contribution screen landed, so there is nothing to merge.** Map 5.3 item 3 ("Stage 15 planned its
own for Roth (Stage 15 map R3). Merge them."). No Form 5329 or Roth excess screen exists in forms/2025 (`person.
sav_excess` concerns W-2 box 12 elective deferrals). HANDOFF-STAGE-15.md, Open for the owner, item 4: "*Excess or
recharacterized Roth IRA contributions* have no screen of their own (the `s2.other` screen is relied on for Form 5329,
not verified). Should the traditional IRA screen also ask about them?" The shared screen in D10 / R-IRA-4 is new work,
and it is tied to an open owner question. Affects D8, D10.

**O4. `savers` is no longer gated on `scope.credits`.** Map 5.3 item 4 ("the estimator maps `savers` to
`scope.credits`"). `tools/coverage/categories.json` now: `"id": "savers", ... "gates": [], "refused": false, "label":
"Saver's credit (supported since Stage 15; its remaining refusals are unmeasured gates)"`. The map's warning still
holds and is stronger: once `ira_deduction` is ungated, a return with both is counted covered even if
`person.sav_trad` still refuses it. Affects D10, D11.

**O5. W-2 box 12 is now partly modelled.** Map 3.1 ("W-2 entries model boxes 1 to 7 only (w2.yaml); box 11, box 12
and box 13 are not modelled") and R-IRA-5 ("W-2 boxes 11 and 12 not modelled"). w2.yaml now has `w2.box10`,
`w2.box12_any` ('code D, E, F, G, H, S, AA, BB or EE'), `w2.box12_d` ... `w2.box12_ee`, `w2.box12_userra` (6051ec0
had 10 lines, box 1 to 7 only). Box 11, code Z, code Q and box 13 are still absent. The D8 alternative (a per-W-2
code Z or box 11 input) now follows an existing pattern and costs less than the map implies. Affects D8, and Q6
(a per-W-2 box 13 input would sit beside the new box 12 inputs).

**O6. A new rider on `scope.schedule1` is missing from 5.5.** Form 2441 (Stage 15) relies on the Schedule 1 screen
to refuse partnership dependent care benefits: f2441.yaml `f2441.line22` note, "Benefits from your own sole
proprietorship (Schedule C, sc.special) or partnership (Schedule K-1, scope.schedule1) are refused, so the answer is
No and line 22 is zero"; also the `f2441.line12` note and the form note. The 5.5 table does not list it. It stays
covered while Schedule E / K-1 stays in the residual question, but the narrowed question must keep K-1 partnership
income. Affects the `scope.schedule1` narrowing (5.4, 5.5).

**O7. Form 1040 line 1z now includes line 1e.** Stage 15 changed `f1040.line1z` from `copy f1040.line1a` to
sum(`line1a`, `line1e`) (taxable dependent care benefits, `f2441.line26`). This feeds `f1040.line9`, so IRA worksheet
line 3 (and encoding (a), which reads 1z) now passes through Form 2441 Part III. No cycle found (Form 2441 reads
`f1040.line11a` only in Part II; line 26 is `subtract_floor0(line23, line25)`), but the 5.1 order and the worksheet
line 8 question (are taxable dependent care benefits "wages" for the IRA compensation sum?) were written without it.

## Unverifiable

- The per-category gains, the +6.34 for the recommended set and the greedy order after Stage 15: not re-run here
  (running the estimator would write a cache; out of a read-only brief). Only the report's group total was compared.
- The split of the "Other income" count into column 91 (7,468,434) and column 93 (318,839): `xlrd` is not installed,
  so `soi-23in14ar.xls` could not be read. The sum, 7,787,273, matches the report and categories.json columns 91 and 93.
- Everything the map sources to unarchived documents (Pub. 504, Pub. 4681, Form W-2G, 1099-C, 5498, 1099-SA,
  Form 982): not archived (manifest has no entry for fw2g, p504, p4681, f1099c, f5498, f1099sa, f982, f4797, f2555,
  f172, p536, p54), as the map says.
- Whether `sa.excluded_income` fires on every return with Form 2555 (it is a guard on many Schedule A, 8812, 8880,
  EIC, 2441, SLI and Schedule 1-A lines, not on a scope line); R-IRA-14 "already refused elsewhere" depends on it.
- That encoding (b) passes the checker: read from the operands only, not built.

## Inferences the recommendations rest on (not errors, flagged for the owner)

- D9 / Q7: the "per-person floor (Pub. 590-A)" reading rests on p590a p. 7, "If you have a net loss from
  self-employment, don't subtract the loss from your salaries or wages when figuring your total compensation." The
  text speaks of "your" wages and is silent on netting one spouse's loss against the other's profit; the worksheet
  (p. 98, line 9, "If zero or less, enter -0-") floors the couple's total. Choosing per person departs from the
  printed worksheet on an inference.
- R-IRA-2 / Q1: the Stage 15 per-person `person.sav_roth` amount already exists, so "joint return with both kinds"
  can be tested from inputs rather than asked.

## Confirmed

About 200 quoted passages and headings searched mechanically, all found on the cited page except the locators noted
(E6; the two Schedule 2 line texts are on f1040s2 p. 2, where the map gives no page), plus about 40 project facts. Decision-critical ones:

- D7: IRA worksheet line 3 = Form 1040 line 9; SSB line 6 includes Schedule 1 line 20; line 9 includes 6b; the
  checker walks guards, branches and refusal guards; the p. 31 exception and the p. 97 skip make it unreachable.
- D1: Form 4797, Form 172, Form 2555 and the other refusal sources are not archived; i8960 p. 13 "Section 1411 NOL".
- D5: the refund worksheet text (p. 90) and the nine exceptions (p. 89), each item checked; the $14,600, $29,200,
  $21,900, $1,550 and $1,950 amounts and the MFS note.
- D8 / D9: the i1040gi p. 95 numbered list (items 2, 4, 5, 6, 7, 9, 10); line 2 amounts $89,000 / $146,000 /
  $246,000 / $10,000 (MFS); thresholds $10,000 and $20,000; rates 70/80/35/40%; $200 minimum and round up to $10;
  the $14,000 / $15,000 / $16,000 caution; p590a Tables 1-2 and 1-3 ($79,000 / $89,000, $126,000 / $146,000,
  $236,000 / $246,000); p590a pp. 6, 7, 9, 10, 11, 12, 13, 15, 16 and 54 quotations; p590a p. 13 Appendix B
  conditions (benefits, compensation, contributions, coverage).
- Form 8606 Part I lines 1, 2, 3, 14 and the i8606 pp. 2, 5, 8, 9 quotations.
- D13: f8889 lines 14a to 17b; i8889 pp. 8-9 exceptions; Schedule 2 lines 17c, 18, 21; `s2.line21` today sums lines
  4, 11, 12.
- D14: i1040sca p. 11 gambling losses; p525 p. 33; p529 p. 10 (Rev. December 2020, as stated).
- Project facts: `s1.line10` = sum(3, 7); `s1.line26` = sum(11, 13, 15, 16, 17, 21); `sli.line3` and `ssb.line6`
  sums and cites; `sa.line16` = copy `sa.zero` refused by `sa.unsupported`; `f8960.line10` = copy `f8960.zero`,
  `f8960.line11` = sum(9d, 10); `f8960.refund`; `f8889.unsupported` (taxable distributions plus five others);
  `s2.other` wording; `interest.amount` only; `retirement.special` wording; `person.age65` 'Were you born before
  January 2, 1961?'; `person.plan`, `person.box1`, `person.sc_total`, `person.se_line13`, `person.s16`,
  `person.simple_age`; status-keyed parameters resolve by `f1040.status` (eval.ts); the estimator stops on unknown
  gates (estimate.py line 203); the twelve categories and their gates in categories.json; every rider in 5.5
  (`eic.step2_other`, `eic.step5_line1`, `eic.clergy`, `s8812.eiw_3`, `s8812.eiw_4`, `s1a.line5_calc`,
  `s1a.line14b_calc`, the carloan note, the EIC Form 4797 cite); the shares and IRS counts against the report.
- PREMISES.md Stage 15 owner decision 1 quote; sources revisions (p529 Rev. December 2020, f1099g Rev. March 2024,
  i1099int January 2024).
