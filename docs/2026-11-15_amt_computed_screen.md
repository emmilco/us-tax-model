# The alternative minimum tax as a computed screen (T-307)

Written 2026-11-15 by lane g1-f7b (claude-opus-5-5, judgment, year 2025, jurisdiction us), before the build. Decision
D2 of `docs/provisional/lanes/g1-plan.md` (adopted): replace the question every filer is asked, `s2.amt_owed` ("Do you
owe alternative minimum tax for 2025, or have to file Form 6251 for it?"), with arithmetic from lines the tool already
has. Sources: `sources/2025/i6251.*` and `sources/2025/f6251.*` (archived; nothing fetched), i1040gi p. 112 (Line 2).

Labels: **[V]** read in the archived source or the tree; **[I]** inferred.

## 1. What has to be decided

i1040gi Line 2 sends the filer to i6251 "to see if you must file the form" [V]. i6251, Who Must File [V]: attach Form
6251 if any of

1. line 7 is greater than line 10;
2. a general business credit with Form 3800 line 6 or line 25 above zero;
3. a credit on Form 8834, the personal part of Form 8911, or Form 8801;
4. lines 2c through 3 total a negative amount and line 7 would be greater than line 10 without them.

AMT is owed only if line 9 (line 7 less the AMT foreign tax credit, line 8) exceeds line 10, so statement 1 false
implies no AMT. The tool refuses Form 6251 wherever it is needed, so the screen must be true exactly when some
statement may be true, and may be false only when every statement is shown false.

Statements 2 and 3 cannot arise on a return the tool completes [V]: Forms 3800, 8801, 8834 and 8911 credits, and
credits carried from 2024, are refused (`scope.yaml` lines 1242 to 1294, the 2024 forms question at s3.yaml line 829).
Statements 1 and 4 need lines 7 and 10.

## 2. Which lines of Form 6251 a completed return can reach

Each Part I line, against what the tool accepts:

| Line | Item | On a return the tool completes |
|---|---|---|
| 1a, 1b | Form 1040 line 14 less Schedule 1-A line 37; line 11b less 1a | computed [V] (f1040.line14, s1a.line37, f1040.line11b) |
| 2a | Schedule A line 7, or the standard deduction (line 12e) | computed (sa.itemizes, sa.line7, f1040.line12e) |
| 2b | tax refunds on Schedule 1 line 1 or 8z, negative | line 1 computed (s1.line1); the 8z refunds are left out, which only raises the bound |
| 2c | investment interest, AMT less regular | zero unless private activity bond interest or another adjustment changes the AMT Form 4952 [V i6251 p. 2]; covered by 2g's question and by the bound below [I] |
| 2d | depletion | refused (sc.special) [V] |
| 2e, 2f | net operating loss | refused (scope.nol) [V] |
| 2g | specified private activity bond interest | 1099-DIV box 13 refused (div.amt) [V]; **1099-INT box 9 not caught by anything but `s2.amt_owed`** [V grep] |
| 2h | section 1202 stock | refused (sales.yaml line 627, div.section1202) [V] |
| 2i | incentive stock options | asked today: `s2.iso`, `s2.iso_vested` (kept) |
| 2j | estates and trusts (K-1) | refused (scope K-1 question) [V] |
| 2k | disposition of property | business property dispositions refused (asset, scveh) [V]; for stock, the AMT basis of ISO shares is higher, so the adjustment is negative [V i6251 p. 4 example]; a negative adjustment cannot make the screen wrong (section 3) |
| 2l | post-1986 depreciation | **in scope**: the asset form depreciates 3-, 5-, 7- and 10-year property with the 200% declining balance tables [V asset.yaml], which the AMT refigures at 150% unless the property was eligible for the special allowance [V i6251 p. 5] |
| 2m, 2n | passive activities, at-risk | refused (sc passive and at-risk screens, Schedule E, K-1) [V] |
| 2o, 2q, 2t | circulation costs, mining costs, intangible drilling costs | **not refused by any screen** [V grep]; rare business costs |
| 2p | long-term contracts | refused (sc.yaml line 84) [V] |
| 2r | research costs | no adjustment for an activity with material participation [V i6251 p. 7]; passive Schedule C refused |
| 2s | pre-1987 installment sales | installment method refused (sc.special) [V] |
| 3 | other: mortgage interest on a home that is not a principal residence and not a "qualified dwelling" (a boat or recreational vehicle) [V i6251 p. 8] | **in scope**: sa.home_other lets interest on a loan secured by a boat or camper reach line 8a [V sa.yaml 611] |
| 3 | related adjustments (section 179, SE health insurance, SE retirement, IRA deduction) | arise only beside another adjustment such as 2l [V i6251 p. 9] |
| 3 | pre-1987 depreciation, pollution control, tax shelter farms, disaster loss standard deduction, Form 8990 | outside the tool (assets placed in service 2005 to 2025 only; Schedule F, Form 8990 refused) [V] |

Part II: line 5 is the Exemption Worksheet (computable). Line 7 is either the flat 26%/28% computation or Part III;
Form 2555 is refused (bank, line 725 help) [V]. Line 8 needs AMT Form 1116 unless the simplified election was made
(i6251 p. 10) [V], but statements 1 and 4 do not read line 8. Line 10: Form 1040 line 16 plus Schedule 2 line 1z less
Schedule 3 line 1; Forms 4972 and 8978 and Schedule J are refused [V f1040.yaml 609, scope.yaml]. The screen uses line
10 **without line 1z** (the excess advance premium tax credit repayment), which is never negative, so line 10 is
understated and the screen can only refuse more. Reading line 1z would make the screen evaluate Form 8962 and report its
refusals in place of the other Schedule 2 screen's (fixture stage18.refuse.s2_other_before_8962).

## 3. The screen

**An upper bound on AMTI.** Let `A = line 1b + line 2a − (Schedule 1 line 1) + PAB + D + R`, where every added term
is zero or more:

- PAB: the 1099-INT box 9 amount (asked; section 4);
- D: the regular MACRS deduction of the year on property this tool depreciates with the 200% tables (Form 4562
  line 17, line 19 for 3-, 5-, 7- and 10-year property, and line 26 column (h) for listed property, summed over every
  business). The AMT deduction is never below zero, so the line 2l adjustment is at most D. D is loose: 15- and 20-year
  property placed before 2025 and property that was eligible for the special allowance are in it, though they have no
  adjustment. Loose here means a refusal where Form 6251 might not have been needed, never a missed one;
- R: when D > 0, the regular section 179 deduction (s179.line12), SE health insurance (s1.line17), SE retirement
  (s1.line16) and IRA deduction (s1.line20). A related adjustment's AMT deduction is never below zero, so each item's
  positive related adjustment is at most its regular deduction. Related adjustments arise only beside an adjustment,
  which here means beside 2l (2c through business interest, 2d, 2h and 2k through 2t are refused or, for 2k on stock,
  do not reach these limits [I]).

A is at least the true line 4 (every omitted item is negative or zero) and at least the line 4 "without lines 2c
through 3" of statement 4. Lines 5 to 7 are nondecreasing in line 4: the exemption shrinks as line 4 grows; the flat
computation rises; Part III with the regular-tax worksheet amounts adds each further dollar at a rate of zero or more
(checked line by line) [I]. So `line 7 of A ≤ line 10` shows statements 1 and 4 false.

**Line 7 of A.** Part III is used when the return used the Qualified Dividends and Capital Gain Tax Worksheet or the
Schedule D Tax Worksheet (f1040.gate.qdcg_applies), as Form 6251 line 7 directs. Its lines 13, 14, 15, 20 and 27 are
taken from the regular-tax worksheets. That is exact when none of i6251's Part III statements apply (p. 12, "None of
the statements apply"). Where an AMT gain differs (statement 1, ISO shares sold), the AMT gain is smaller, and
computing with the regular gain keeps every dollar in, taxed at a rate of zero or more, so the result is still an upper
bound [I]. Statement 3 (K-1 from an estate) is refused. Without Part III the flat computation is used. It is itself an
upper bound in every case, because line 40 is the smaller of lines 38 and 39.

**The test.** `s2.amt_computed` is true when line 7 of A is greater than line 10. Line 8 is not read: the screen
answers "must file", which is the stronger of the two questions.

## 4. What is still asked, and of whom

The arithmetic cannot see three things. Each is asked beneath the fact that makes it possible, and the first two only
where the answer could change the result. That is when the flat bound, with the item counted at its largest
(all tax-exempt interest; all home mortgage interest), gives line 7 above line 10:

| Input | Asked when | Typical answer | On Yes |
|---|---|---|---|
| `s2.amt_pab` (amount): box 9 of the filer's Forms 1099-INT | tax-exempt interest > 0 and the bound could cross | 0 | enters A exactly |
| `s2.amt_boat`: mortgage interest deducted for a boat or camper that is not the main home | itemizing, mortgage interest > 0, and the bound could cross | No | refuses (the share is not known; counting all interest is the case that crossed) |
| `s2.amt_business`: circulation costs of a periodical, mining exploration or development costs, or oil, gas or geothermal drilling costs deducted | a Schedule C on the return | No | refuses (the amount is unbounded) |

`s2.iso` and `s2.iso_vested` stay as they are.

`s2.amt_owed` stops being asked. Under technique 3.1 of the construction protocol its id stays as a derived line, true
when one of the three items above is true. Every refusal that names the gate `s2.amt` keeps its line, form, wording and
remedy.

**Who could answer No wrongly.** For PAB, a filer who adds box 9 to box 8; the prompt asks for box 9 itself, a box on
the paper in hand. For the boat, a filer whose second home is a houseboat or motor home, which the label names. For the
business item, a publisher of a newsletter who does not think of it as a periodical; the label says "newsletter".

## 5. Costs and shares (agent's estimates, to be overruled)

Before: every filer reads one 25-word question (cost about 20 each way: the filer cannot know). After: filers with no
Schedule C, no tax-exempt interest and no mortgage interest read nothing. A Schedule C filer reads one short question
(cost 1 to 2). PAB and boat questions reach only filers whose flat bound crosses line 10. On the personas that is a
filer with roughly $200,000 or more of income before the exemption, so a few percent [I].

Over-refusal: the bound refuses (a) business filers with 200%-DB property not eligible for the special allowance
(converted personal property; related-party purchases) whose AMT is near the line, (b) by R, high-income business
filers with such property and large section 179 or retirement deductions, and (c) any filer whose regular tax is
genuinely below the tentative minimum tax. In (c) the refusal is right. A future refinement would compute the 150% DB
deduction from Pub. 946's tables; it was not built here.

## 6. What this does not show

The monotonicity of Part III under the regular-amount substitution is argued, not proved by a machine. The adjustment
inventory in section 2 rests on the screens named; a screen that is later loosened could let an adjustment in unseen.
The new `amt.*` parameters in `params/2025.yaml` have no 2026 values yet. The 2026 law is recalled, not read in an
archived source, as changing the exemption phase-out rate and thresholds [I, unverified]. The 2026 track must stage them
and check that the 25% phase-out rate still holds (outside this lane).
