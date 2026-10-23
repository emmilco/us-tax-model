# Engine differential

Class C evidence at scale (spec 6.5): generated returns (single, head of household and married filing jointly) are
computed by the project and by three independent engines maintained by other
people, and compared line by line. Every difference must carry an identified
cause or the run fails. This is the only check in the pipeline whose reading
of the tax law does not come from a language model reading the archived text.

## Engines

| Engine | Version pinned | License | Precision | Runs where |
|---|---|---|---|---|
| PolicyEngine-US | `requirements.txt` | AGPL-3.0 | float32 | `.engines/venv`, git-ignored |
| Tax-Calculator (PSL) | `requirements.txt` | CC0 | float64 | `.engines/venv`, git-ignored |
| OpenTaxSolver (OTS) | the package in `.engines/opentaxsolver-src/` (its `0_README.txt`) | GPL-2.0 | decimal2: doubles, printed to the cent | `.engines/opentaxsolver-src/<package>/bin`, built by `setup.sh`, git-ignored |

Nothing in the repository imports any engine. `setup.sh` is the one network
step for the Python engines; it installs them into `.engines/venv`. `run.sh`
skips, visibly, when that environment does not exist, so `check-all` still
runs offline on a fresh clone; the check is only claimed where the engines are
installed. OpenTaxSolver's package cannot be fetched by a script (see below);
`run_engines.py` leaves that engine out, visibly, when it is not built.

### OpenTaxSolver: download, build, version swap

OTS is a set of C programs, one per form, each reading one text file and
writing `<input>_out.txt`; there is no API. The package is published on
SourceForge, which answers every scripted download (curl, wget, urllib) with a
browser challenge, so the download is manual:

1. In a browser, open https://sourceforge.net/projects/opentaxsolver/files/ and
   download the Linux package for the tax year, `OpenTaxSolver<year>_<version>_linux64.tgz`
   (every platform package carries `src/`, `tax_form_files/` and prebuilt binaries;
   the Linux one is chosen because its ELF binaries cannot run here by accident).
2. Save it into `.engines/opentaxsolver-src/` and run `tools/engines/setup.sh`
   again: it checks the SHA-256 against `KNOWN_SHA256` in the script (a hash not
   listed is built with a warning and printed, to be added once checked),
   extracts the tarball beside itself and builds every program with
   `make -C src -B all`, replacing the shipped binaries with native ones.
3. A new release is a new tarball and a rerun of `setup.sh`; no code changes. The
   adapter (`ots_adapter.py`) uses the newest extracted package by name, reads the
   version from its `0_README.txt` and records, beside it, the version the Form
   1040 program prints about itself (23.06 ships a program that says v23.05).
   Limitations that are defects of one release are declared under that version in
   `limitations()` and drop away when another release is installed. Remove the
   older package directory once the newer one is built.

Package run so far: 23.06 (SHA-256 `0cc7e540...18e5e6b`, recorded in `setup.sh`),
taken from the tenforty repository's verbatim vendoring of the release because
SourceForge blocked the fetch.

### OpenTaxSolver: what the adapter does

`ots_adapter.run_ots` fills the shipped templates by key (the input grammar is
positional, so an input is always the whole template with values substituted),
runs the programs with the working directory outside the OTS tree and paths as
arguments, in the order the results flow: Schedule C, Schedule SE, Form 8889,
Form 8959, Form 1040 (pass 1), Form 8960, Form 8995 (which imports the pass-1
output and the Schedule C output by file name), Form 1040 (pass 2, with the QBI
deduction, the NIIT and the foreign tax credit), Form 2441 (imports the pass-2
output), Schedule 8812, Form 1040 (pass 3, final). It parses `LABEL = value`
lines and the three worksheet print formats; a few labels the program prints only
when nonzero are read as zero when absent, and worksheet lines only when the
engine ran the worksheet.

Lines reached (project ids): Form 1040 lines 1z, 6b, 7a, 8, 9, 10, 11b, 12e, 13a,
13b, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25d, 28, 32, 33, 34, 37 and the
pre-credit total; Schedule 1 lines 9, 10, 21, 26; Schedule 1-A lines 13, 21, 30,
37, 38; Schedule 2 line 21; Schedule 3 lines 2 and 8; Schedule A lines 3, 4, 5d,
5e, 7, 8e, 10, 14, 17, the standard deduction and the deduction taken; Schedule D
lines 1b, 2, 8b, 9 (all four columns), 7, 13, 15, 16, 18, 19, 21; the Qualified
Dividends and Capital Gain Tax Worksheet lines 1 to 25; the Schedule D Tax
Worksheet lines 1 to 47; the Social Security Benefits Worksheet lines 1 to 18;
Schedule C lines 7, 28, 29, 31; Schedule SE lines 4c, 6, 12, 13 (the filer's);
Form 8889 lines 12 and 13; Form 8959 lines 7, 13, 17, 18, 21, 22, 24; Form 8960
lines 8, 11, 12, 15, 16, 17; Form 8995 lines 2, 4, 5, 8, 9, 10, 11, 13, 14, 15 and
the QBI deduction; Form 2441 lines 3, 4, 6, 7, 9a, 9c, 10, 11; Schedule 8812 lines
5, 7, 8, 10, 11, 12, 14, 16a, 16b, 17, 19, 20, 27.

Pass-throughs (inputs the adapter supplies that the project computes; each is
declared in `OTS_PASS_THROUGH["components"]` and is not an engine assertion for
that component): Form 8889 line 3 (the limit, from the coverage facts) and line
7; Schedule 1 lines 11 (educator, after the $300 limit) and 20 (the IRA
contributions, no worksheet); Schedule 3 line 1 (the smaller of the foreign tax
and the engine's own line 16); Form 8960 lines 5a and 13 (the engine's own Form
1040 lines 7a and 11a) and 9a (the investment interest paid when the engine
itemized); Form 8995 line 12 (net capital gain plus qualified dividends, from the
facts); Schedule 8812 line 13 (Credit Limit Worksheet A from the engine's own
lines) and line 18a (earned income from the engine's own lines 1z and Schedule
SE); Form 2441 earned income (the engine's own line 1z and Schedule SE by file
import); Schedule D line 19 (Form 1099-DIV box 2b, not the Unrecaptured Section
1250 Gain Worksheet result).

Not computed by OTS, so not mapped (`OTS_PASS_THROUGH["unmapped"]`): the EIC,
Form 8880, Form 5695, the IRA Deduction Worksheet, the State and Local Income
Tax Refund Worksheet, the Unrecaptured Section 1250 Gain Worksheet, the excess
social security credit, Form 4952's limit (Schedule A line 9 is taken as
entered; Schedule D Tax Worksheet lines 3 and 4 are zero), Form 8995-A. Every
one is a limitation in `limitations()` on the lines it moves, keyed by a
generator feature or one derived from the project's values (`eic`,
`savers_credit`, `residential_clean_energy`, `home_improvement`, `ira_phaseout`,
`sli_phaseout`, `section_1250_netted`, `investment_interest_limited`,
`excess_social_security`, `negative_agi`, `three_or_more_children`), or by a fact
the adapter reports about the engine's own run (`ots_amt`: the engine computed a
Form 6251 tax, which the project excludes). Release 23.06 adds two
version-keyed limitations the 23.07 revision history reports fixed: the Schedule
D Tax Worksheet line 19 ceiling (197,390 for 197,300) and the lines 33 to 43
condition (`special_gains`), and Schedule 1-A line 28's truncation and line
29's $300 multiplier (`car_loan_interest`). Two more engine defects are worked
around or declared without a version: the Form 8995 template's row iii name
line carries a stray `;`, which the program reads as a business name and
auto-calculates the Schedule C income twice (the adapter blanks the key); and
Schedule 8812 takes the Part II-A route at exactly $5,100 on line 16b where the
form sends three qualifying children to Part II-B (`three_or_more_children`).

OTS uses the Tax Table below $100,000 as the form does (its `TaxRateFunction`
quantizes to the table's bands and rounds; checked against every cell of the
pinned table), so its tax lines are compared `exact`, never `table-adjusted`.
It holds fractions of a cent through its arithmetic and prints to the cent; the
project rounds each rate multiplication to the cent, so differences of a cent
per such multiplication appear and are the `subcent` category, with the count
of multiplications declared per line in `OTS_SUBCENT`.

## Pipeline

```
tools/engines/run.sh                  (ENGINE_CASES=1000 ENGINE_SEED=20260101 by default)
  generate_cases.py  -> .engines/work/cases.json     random in-scope returns, integer cents
  main.js eval --batch -> .engines/work/project.json  the project's lines and derivations
  run_engines.py     -> .engines/work/engines.json   each engine's lines, in cents
  compare.py         -> reports/2025/engine_differential.md and engine_differential.json (per engine and line:
                        cases compared, nonzero, excluded, unexplained; read by the evidence report) ; exit 1 on any unexplained difference
```

Tax-Calculator runs with `exact_calculations=True`, so its phase-outs follow the printed $1,000 steps (Schedule 1-A lines 11, 19 and 28; Schedule 8812 line 10) rather than its smoothed default. Generated filers are 40, or 66 to 85 for the enhanced deduction for seniors; PolicyEngine-US is told they are not enrolled in Medicare, since medical expenses are all supplied.

The generator produces the project's interview inputs and, separately, the
economic facts an engine needs (net short- and long-term gain, totals). The
facts are derived from the same raw amounts without the project's Form 8949
or Schedule D logic, so the engines do not inherit the project's reading.

## What is compared

Adjusted gross income, the chosen deduction, itemized total, standard
deduction, the QBI deduction, taxable income, the tax on line 16, the foreign
tax credit, Form 8959 and Form 8960, total tax (line 24), and the pre-credit
total (line 18 + line 23). The excess Social Security credit is compared by no
engine: neither computes it from per-employer withholding.

Per-form result lines (`PE_MAP` and `TC_MAP` in `run_engines.py`; only lines
the engine computes are mapped):

| Project line | PolicyEngine-US | Tax-Calculator |
|---|---|---|
| Form 2441 line 9c (credit before the limit) | `cdcc_potential` | not exposed (F2441 keeps line 9a internal) |
| Form 2441 line 11; Schedule 3 line 2 | `cdcc` | `c07180` |
| Form 8880 line 10 (credit before the limit) | `savers_credit_potential` | `e07240` is an input |
| Form 8880 line 12 (Schedule 3 line 4 is a copy) | `savers_credit` | `e07240` is an input |
| Form 5695 lines 13, 15; Schedule 3 line 5a | `residential_clean_energy_credit_potential`, `residential_clean_energy_credit` | `e07260` is an input |
| Form 5695 lines 30, 32; Schedule 3 line 5b | `energy_efficient_home_improvement_credit_potential`, `energy_efficient_home_improvement_credit` | `e07260` is an input |
| Schedule 8812 line 12 (credit after the phase-out) | `ctc` | not exposed (`c07220` + `odc` is line 14) |
| EIC Step 5 earned income (`eic.earned_income`); Worksheet A/B line 1 (`eic.line1`) | `eitc_earned_income` | `earned` |
| Schedule 1 line 20 (IRA deduction) | `traditional_ira_deduction` | `e03150` is an input |
| Schedule SE lines 12 and 13 (the filer's) | `self_employment_tax`, `self_employment_tax_ald_person` (person level) | `setax`, `c03260` |
| Schedule 1-A lines 13, 21, 30, 37 | `tip_income_deduction`, `overtime_income_deduction`, `auto_loan_interest_deduction`, `additional_senior_deduction` | the same names; `senior_deduction` |

Form 8889 line 13 is an input to both engines (`health_savings_account_ald`,
`e03290`) and is not mapped. Schedule 8812 lines 14 and 27, the EIC, the
taxable social security benefits (`ssb.line18`) and Schedule 1-A line 38 are
reached through the Form 1040 lines that copy them (19, 28, 27a, 6b, 13b). Each
engine's unmapped result lines and the reason are declared in
`*_PASS_THROUGH["unmapped"]` and printed in the report.

Form 2441 and Form 5695 lines are unknown on returns that do not file the form;
Schedule 3 lines 2, 5a and 5b carry the zero and are compared on every return.

## Not-computed floor

`compare.py` fails the run when, on any mapped line, the project left more
than `NOT_COMPUTED_FLOOR` (5%) of an engine's cases without a money value (a
refusal, an unknown input, a non-money value). `NOT_COMPUTED_ALLOW` names the
lines whose value is legitimately unknown where a named input is false (Form
2441 lines without care expenses, Form 5695 Part I and Part II lines without
the part's costs); those cases do not count, and the share is measured on the
rest. The report prints the raw and the counted "not computed" numbers per
line and the share; the JSON summary records the floor, the allow-list and
any line over it (`not_computed_floor`). Project refusals (Form 8995-A above
the QBI threshold on about 2% of self-employed returns) are counted, so the
floor also bounds how much of the generated population the project refuses.

## Categories

- **exact** — equal to the cent.
- **table-adjusted** — equal to the project's tax lines recomputed with every
  Tax Table lookup replaced by the rate schedule, keeping the worksheet path
  and re-taking its smaller-of. Engines compute from the schedule where the
  form prescribes the table; the recomputation is in `compare.py` and uses the
  project's own pinned table and schedule.
- **float** — within two units in the last place of the engine's floating
  point representation, derived from its precision.
- **subcent** — OpenTaxSolver only: within one cent per unrounded rate
  multiplication the adapter declares for the line, where the project rounds
  each product to the cent (amb.2025.multiplication_subcent).
- **excluded** — the engine cannot model a feature of the case. Each rule
  names the feature, the lines and the reason (`run_engines.py`, the
  `*_LIMITATIONS` lists; `ots_adapter.limitations()`). Some features are read
  off the project's own values, for example whether Form 4952 limited the
  investment interest deduction; `salt_exceeds_agi` requires a positive
  Schedule A line 5d, so a negative AGI alone does not fire it; an engine's
  adapter may report features of its own run (`features` in engines.json).
- **explained** — a remaining difference with a cited cause recorded in
  `fixtures/2025/differential/engine_investigations.json`
  (`{engine, line, case|feature, cause, cite}`).
- **UNEXPLAINED** — fails the run.

## Engine semantics the adapters account for

- Capital gain distributions go into net long-term gain for both engines:
  PolicyEngine's distributions input does not reach income, and
  Tax-Calculator's `e01100` is the no-Schedule-D path that bypasses loss netting.
- Form 1099-DIV box 2d is given to PolicyEngine as a collectibles gain before
  netting, so its 28% Rate Gain Worksheet netting runs.
- PolicyEngine's foreign tax credit is a supplied amount under a Form 1116
  style limit, so the comparison with it is made before credits.
- PolicyEngine books the Additional Medicare Tax as payroll tax and holds the
  net investment income tax outside its income-tax-before-credits total; both
  are added back for the total-tax lines.
- Tax-Calculator zeroes the standard deduction for itemizers; the chosen
  deduction is `standard + c04470`. It treats a unit owing no tax under
  either deduction as taking the standard deduction, so the itemized total is
  read from a second pass with the standard deduction zeroed, and the
  deduction choice is excluded only on returns with no tax either way.
- PolicyEngine takes unrecaptured section 1250 gain as an already-netted
  input, where the project's worksheet nets it against the short-term loss;
  it limits the state and local tax deduction to adjusted gross income; and
  neither engine deducts Form 4952 investment interest on Form 8960 line 9a.
  Each is a stated limitation keyed by a feature read off the project's values.
- Form 5695 costs are supplied net of subsidies and rebates, as the form
  takes them; PolicyEngine is told its modeled Department of Energy home
  electrification rebate covers nothing
  (`high_efficiency_electric_home_rebate_percent_covered` = 0), since it would
  otherwise net that rebate out of the insulation and heat pump costs.
  PolicyEngine counts the furnace credit twice (its qualified-expenditures list
  names `capped_qualified_furnace_or_hot_water_boiler_credit` twice) and takes
  the larger of the $1,200-capped total and the heat pump credit where Form
  5695 line 30 adds them; both are limitations keyed by generator features
  (`furnace`, `heat_pump_with_improvements`). Its saver's credit rate is zero
  for a negative AGI, where the Form 8880 table's first row has no lower bound
  (`negative_agi`, read off the project's AGI).
- Tax-Calculator takes the Form 5695 credits as one input (`e07260`), given
  as the generator's amounts before the limits figured from the costs, and
  applies them after the child tax credit while subtracting them whole in
  Credit Limit Worksheet A; lines 19 and 28 are excluded where that moves line
  14 (`rce_displaces_ctc`, `savers_displaces_ctc`, read off the project's
  Schedule 8812). It has no saver's credit, so total tax is not compared on
  returns with one (`savers_credit`), and it takes the IRA contributions as
  the deduction (`e03150`), so returns whose deduction the IRA Deduction
  Worksheet phased out are not compared on any AGI-dependent line
  (`ira_phaseout`, read off Schedule 1 line 20 against the contributions).
- Both engines' earned income for the EIC includes self-employment earnings
  less half the self-employment tax; Step 5 earned income holds wages only, so
  it is compared on returns without self-employment and Worksheet B line 6
  (`eic.line1`) on every return.
- Care expenses reach PolicyEngine as an SPM-unit input prorated over the
  unit's children (`spm_unit_pre_subsidy_childcare_expenses`); the generator
  pays care only for children under 13, so the proration changes nothing.
- The credits limited by the tax (Form 2441 line 11, Form 8880 line 12, Form
  5695 lines 15 and 32, Schedule 3 lines 2, 4, 5a and 5b) inherit every
  limitation that sets Form 1040 line 16 aside, and `compare.py` recomputes
  them along the project's own credit-limit chain for the `table-adjusted`
  category, including Schedule 8812 Credit Limit Worksheet B.

## Dependents and head of household (Stage 8)

The generator adds up to three children who qualify in full (under 17, or 17–23
full-time students for the credit for other dependents) and files head of
household on half of the cases with a qualifying child. PolicyEngine-US gets
each child as a person in the unit with age and student status and the unit's
filing status; Tax-Calculator gets `MARS`, `XTOT`, `n24`, `nu18`, `n1820`,
`n21` and a fixed `credit_claim_urn` of zero, because it otherwise zeroes the
additional child tax credit by a random take-up model that is not on the form.
Form 1040 line 19 is compared with PolicyEngine as the smaller of its credit
after phase-out and its limiting tax liability (its `non_refundable_ctc` is the
remainder after the refundable part), and with Tax-Calculator as `c07220` plus
`odc`; line 28 with `refundable_ctc` and `c11070`; Schedule 8812 line 12, the
credit after the phase-out, with PolicyEngine's `ctc` (Tax-Calculator does not
expose it). The Tax Table adjustment is carried through Schedule 8812's credit
limit. Both engines step the phase-out by whole $1,000 (PolicyEngine's
`ctc_phase_out` takes the ceiling; Tax-Calculator under `exact_calculations`),
and PolicyEngine takes the 17–23-year-old students as dependents through
`tax_unit_role_input`, so neither needs a limitation here.

