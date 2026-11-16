# Screen and false-no adjudication, lane xrel, family cred (2025, us)

Adjudicated by claude-opus-5-5 (judgment), 2026-11-15, against the B1 plus expansion tree. Rulings are in `/tmp/xrel/frag/cred.screens.json` and `/tmp/xrel/frag/cred.false_no.json`, merged by the lane lead. Two screen samples (`f5695.joint_occupancy#1`, `s8812.puerto_rico#1`) were already ruled and are not repeated.

## Screens

33 samples: 18 with a defect, 15 without. Findings by class:

| Class | Findings |
|---|---|
| defect | 33 |
| accepted WIDE | 25 |
| presentation | 11 |
| covered | 9 |
| model error | 6 |
| out of scope | 1 |

| Sample | Disposition | Findings (n: class, bug) |
|---|---|---|
| `f2441.mfs_spouse_deemed#1` | no gate defect; WIDE only | 0: accepted WIDE; 1: accepted WIDE |
| `f2441.plans_differ#1` | no gate defect; finding 0 is the owner's ruling amb.2025.dc_plan_maximum | 0: covered; 1: presentation; 2: presentation |
| `f2441.prior_year#1` | no gate defect; WIDE only | 0: accepted WIDE |
| `f5695.b_new_home#1` | no gate defect; wording lows | 0: presentation; 1: presentation; 2: covered |
| `f5695.business_use#1` | no gate defect; WIDE only | 0: accepted WIDE |
| `f5695.construction_later#1` | no gate defect; WIDE and an IRS-undefined term | 0: accepted WIDE; 1: presentation |
| `f5695.line17e#1` | no gate defect; covered by f5695.b_new_home | 0: covered; 1: covered |
| `f5695.line7a#1` | no gate defect; WIDE accepted | 0: accepted WIDE; 1: presentation |
| `f8863.ban#1` | no gate defect; wording lows | 0: presentation; 1: presentation |
| `s8812.combat_pay#1` | no gate defect; WIDE only | 0: accepted WIDE |
| `gate:eic.lived_with_relative#1` | defect: stepsiblings and older step relatives are not named | 0: defect (BUG-0793); 1: defect (BUG-0793); 2: accepted WIDE |
| `gate:f1095a.b_wrong_asked#1` | no gate defect; the month-by-month path collects the corrected column B | 0: covered |
| `gate:f2441.benefits#1` | defect: a partnership's dependent care program is not named | 0: defect (BUG-0799) |
| `gate:f2441.care_other_or_claimable#1` | no gate defect | 0: covered; 1: accepted WIDE; 2: accepted WIDE |
| `gate:f5695.any#1` | defect: the opening question drops the construction timing rule and the association share | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: covered; 3: presentation; 4: accepted WIDE |
| `gate:f5695.biomass_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: covered; 2: defect (BUG-0796); 3: accepted WIDE |
| `gate:f5695.central_ac_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: accepted WIDE |
| `gate:f5695.doors_if_any#1` | defect: association share (BUG-0796) | 0: defect (BUG-0796); 1: accepted WIDE; 2: accepted WIDE |
| `gate:f5695.furnace_if_any#1` | defect: association share (BUG-0796) | 0: model error; 1: defect (BUG-0796); 2: accepted WIDE |
| `gate:f5695.geothermal_if_any#1` | defect: construction and reconstruction timing, association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796) |
| `gate:f5695.heat_pump_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: accepted WIDE |
| `gate:f5695.hp_water_heater_if_any#1` | defect: association share (BUG-0796) | 0: defect (BUG-0796); 1: accepted WIDE |
| `gate:f5695.line21a#1` | defect: line 21a asks about a home you live in now | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: out of scope |
| `gate:f5695.line5a_if_any#1` | defect: construction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: accepted WIDE |
| `gate:f5695.panel_if_any#1` | defect: the enabling-property consecutive-year choice is lost behind the 2025 frame | 0: defect (BUG-0796); 1: accepted WIDE |
| `gate:f5695.sec_a_claimed#1` | no gate defect | 0: covered |
| `gate:f5695.solar_if_any#1` | defect: construction and reconstruction timing, association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: accepted WIDE |
| `gate:f5695.solar_water_if_any#1` | defect: construction and reconstruction timing, association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: accepted WIDE |
| `gate:f5695.water_heater_if_any#1` | defect: association share (BUG-0796) | 0: model error; 1: defect (BUG-0796); 2: accepted WIDE |
| `gate:f5695.wind_if_any#1` | defect: construction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: presentation |
| `gate:f5695.windows_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: model error; 3: accepted WIDE |
| `gate:f8962.income_100#1` | no gate defect; the review prompt states the gate backwards | 0: model error (BUG-0800); 1: model error (BUG-0800); 2: model error (BUG-0800) |
| `gate:f8962.other_coverage#1` | no gate defect | 0: presentation; 1: accepted WIDE |

## False-no

32 samples: 25 with a defect, 7 without. Findings by class:

| Class | Findings |
|---|---|
| defect | 58 |
| presentation | 35 |
| covered | 21 |
| model error | 16 |
| out of scope | 15 |
| accepted WIDE | 4 |
| open residual | 1 |

| Sample | Disposition | Findings (n: class, bug) |
|---|---|---|
| `gate:eic.lived_with_relative#1` | defect: stepsiblings, older step relatives and the absence and birth or death rules are not stated | 0: defect (BUG-0793); 1: defect (BUG-0793); 2: defect (BUG-0793); 3: defect (BUG-0793); 4: presentation |
| `gate:f1095a.b_wrong_asked#1` | no gate defect; the month-by-month path collects the corrected column B | 0: covered; 1: covered; 2: covered |
| `gate:f2441.benefits#1` | defect: a spouse's own business, a partnership's program and care of a disabled spouse are not named | 0: defect (BUG-0799); 1: defect (BUG-0799); 2: presentation; 3: covered; 4: defect (BUG-0799) |
| `gate:f2441.care_other_or_claimable#1` | no gate defect | 0: covered; 1: covered; 2: covered; 3: out of scope |
| `gate:f2441.mfs_married#1` | defect: the spouse-earnings question says zero 'if they had a loss' | 0: model error; 1: defect (BUG-0799); 2: defect (BUG-0799); 3: covered |
| `gate:f5695.any#1` | defect: construction and reconstruction timing and the association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: presentation; 4: presentation; 5: covered; 6: covered |
| `gate:f5695.audit_if_any#1` | defect: association share (BUG-0796) | 0: defect (BUG-0796); 1: presentation; 2: presentation; 3: presentation |
| `gate:f5695.biomass_if_any#1` | no new defect; association share is BUG-0796 | 0: accepted WIDE; 1: covered; 2: out of scope; 3: defect (BUG-0796); 4: presentation |
| `gate:f5695.carry_if_prior#1` | no gate defect; wording lows | 0: model error; 1: presentation; 2: covered |
| `gate:f5695.central_ac_if_any#1` | defect: association share and the consecutive-year choice (BUG-0796) | 0: model error; 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope; 4: accepted WIDE |
| `gate:f5695.doors_if_any#1` | defect: association share and reconstruction timing (BUG-0796) | 0: model error; 1: model error; 2: defect (BUG-0796); 3: defect (BUG-0796); 4: out of scope |
| `gate:f5695.furnace_if_any#1` | defect: association share and reconstruction timing (BUG-0796) | 0: model error; 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope; 4: presentation; 5: presentation |
| `gate:f5695.geothermal_if_any#1` | defect: construction and reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope; 4: model error; 5: presentation |
| `gate:f5695.heat_pump_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: model error; 3: out of scope |
| `gate:f5695.hp_water_heater_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: out of scope; 3: model error; 4: presentation; 5: accepted WIDE |
| `gate:f5695.insulation_if_any#1` | defect: association share and reconstruction timing (BUG-0796) | 0: defect (BUG-0796); 1: model error; 2: covered; 3: defect (BUG-0796) |
| `gate:f5695.line17b#1` | defect: association share (BUG-0796) | 0: presentation; 1: presentation; 2: defect (BUG-0796) |
| `gate:f5695.line21a#1` | defect: line 21a asks about a home you live in now (BUG-0796) | 0: defect (BUG-0796); 1: out of scope; 2: defect (BUG-0796); 3: model error |
| `gate:f5695.line5a_if_any#1` | defect: construction and reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: model error; 3: defect (BUG-0796); 4: presentation |
| `gate:f5695.panel_if_any#1` | defect: the consecutive-year choice and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: presentation; 3: defect (BUG-0796); 4: out of scope |
| `gate:f5695.part2_any#1` | defect: association share (BUG-0796) | 0: defect (BUG-0796); 1: model error |
| `gate:f5695.solar_if_any#1` | defect: construction and reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope; 4: covered; 5: covered |
| `gate:f5695.solar_water_if_any#1` | defect: construction and reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope; 4: presentation |
| `gate:f5695.water_heater_if_any#1` | defect: reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: accepted WIDE; 3: out of scope |
| `gate:f5695.wind_if_any#1` | defect: construction and reconstruction timing and association share (BUG-0796) | 0: defect (BUG-0796); 1: defect (BUG-0796); 2: defect (BUG-0796); 3: presentation; 4: out of scope; 5: presentation |
| `gate:f5695.windows_if_any#1` | defect: association share and reconstruction timing (BUG-0796) | 0: model error; 1: defect (BUG-0796); 2: defect (BUG-0796); 3: out of scope |
| `gate:f8863.aoc_claimed#1` | defect: the ban question's help tells a filer whose ban has run out to answer No | 0: open residual (BUG-0797); 1: defect (BUG-0797); 2: defect (BUG-0797); 3: presentation; 4: presentation |
| `gate:f8962.aptc#1` | no gate defect | 0: covered; 1: covered; 2: presentation |
| `gate:f8962.income_100#1` | defect: 'immigrant' and the month are not stated; the inverted-gate finding is the prompt's framing | 0: model error (BUG-0800); 1: defect (BUG-0798); 2: presentation; 3: defect (BUG-0798) |
| `gate:f8962.job_offer_if_other_coverage#1` | no gate defect; wording lows | 0: model error; 1: presentation; 2: presentation; 3: presentation; 4: covered; 5: presentation |
| `gate:f8962.mfs_ask#1` | defect: the abuse exception's help lists only some forms of abuse | 0: covered; 1: covered; 2: defect (BUG-0798); 3: defect (BUG-0798); 4: presentation |
| `gate:f8962.other_coverage#1` | no gate defect | 0: covered; 1: presentation; 2: presentation; 3: presentation; 4: presentation; 5: presentation; 6: presentation |

## Defects (pending)

- BUG-0793 (medium): EIC lived-with-relative screen omits stepsiblings and older step or foster relatives; help also omits the relative's temporary absence and the birth or death rule.
- BUG-0796 (medium): the redrafted `f5695.any` opening and kind ticks drop the construction and reconstruction timing rule (undoing the BUG-0552 fix of BUG-0580) and the condominium or cooperative share (undoing the BUG-0553 fix), lose the enabling-property consecutive-year choice, and `f5695.line21a` asks about a home 'you live in' now. This one entry carries most of the f5695 gate findings.
- BUG-0797 (medium): `f8863.ban` help tells a filer whose ban has run out to answer No, though Form 8862 is still required; the spouse reading is recorded open.
- BUG-0798 (low): `f8962.alien_below` says 'immigrant' and no month; `f8962.mfs_exception` help lists only some forms of abuse and not abuse of a child or family member.
- BUG-0799 (low): `f2441.benefits` omits a spouse's own business, a partnership's program (K-1 box 13 code O) and care of a disabled spouse; `f2441.mfs_spouse_earned` says zero 'if they had a loss'.
- BUG-0800 (low, tooling): the screen and false-no prompts state a gate reached through a 'guard = false' branch backwards; both reviews of `gate:f8962.income_100` reported an inverted gate that the fixture `stage18.refuse.alien_below_100` shows is correct.

## Recurring patterns

- 'to save or make energy' (motive) findings read the line label; the filer sees the tick 'Had solar, insulation, windows, doors or heating equipment installed at home' with help naming furnaces, boilers, wood stoves, panels and audits: model error.
- Spouses with separate main homes: refused by `f5695.separate_homes`; the group heading names the spouse: out of scope.
- Efficiency-tier and main-home WIDE findings: the amount questions state the test: accepted WIDE.
- `gate:f1095a.b_wrong_asked`: a form not printed the same every month is entered month by month, and `f1095a.in_b_*` ask for the corrected premium; `f1095a.annual_ok` applies line 10 to the corrected months: covered.
