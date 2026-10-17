# Engine differential

Class C evidence at scale (spec 6.5): generated single-filer returns are
computed by the project and by two independent engines maintained by other
people, and compared line by line. Every difference must carry an identified
cause or the run fails. This is the only check in the pipeline whose reading
of the tax law does not come from a language model reading the archived text.

## Engines

| Engine | Version pinned | License | Precision | Runs where |
|---|---|---|---|---|
| PolicyEngine-US | `requirements.txt` | AGPL-3.0 | float32 | `.engines/venv`, git-ignored |
| Tax-Calculator (PSL) | `requirements.txt` | CC0 | float64 | `.engines/venv`, git-ignored |

Nothing in the repository imports either engine. `setup.sh` is the one
network step; it installs them into `.engines/venv`. `run.sh` skips, visibly,
when that environment does not exist, so `check-all` still runs offline on a
fresh clone; the check is only claimed where the engines are installed.

## Pipeline

```
tools/engines/run.sh                  (ENGINE_CASES=1000 ENGINE_SEED=20260101 by default)
  generate_cases.py  -> .engines/work/cases.json     random in-scope returns, integer cents
  main.js eval --batch -> .engines/work/project.json  the project's lines and derivations
  run_engines.py     -> .engines/work/engines.json   each engine's lines, in cents
  compare.py         -> reports/2025/engine_differential.md ; exit 1 on any unexplained difference
```

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

## Categories

- **exact** — equal to the cent.
- **table-adjusted** — equal to the project's tax lines recomputed with every
  Tax Table lookup replaced by the rate schedule, keeping the worksheet path
  and re-taking its smaller-of. Engines compute from the schedule where the
  form prescribes the table; the recomputation is in `compare.py` and uses the
  project's own pinned table and schedule.
- **float** — within two units in the last place of the engine's floating
  point representation, derived from its precision.
- **excluded** — the engine cannot model a feature of the case. Each rule
  names the feature, the lines and the reason (`run_engines.py`, the
  `*_LIMITATIONS` lists). Some features are read off the project's own values,
  for example whether Form 4952 limited the investment interest deduction.
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
