# Proposed bug entries (T-100: Lean against spec 6.3)

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1: spec 6.3 claimed every atom is monotone or antitone in each argument, as tabulated; there was no table, and the claim is false

- **Caught by:** T-100 premise check (the README fact check, 2026-10-31, raised the row).
- **Source:** spec/spec.md section 6.3: "Each atom is monotone or antitone in each argument, as tabulated."
  This is a project claim. No IRS text is involved.
- **Symptom:** no table existed. For the evaluator's definitions, four atom arguments are neither monotone
  nor antitone:
  - `percent_floor` in `cap`: part 4005, whole 1000 gives 401 at cap 400 and 400 at cap 401; part 2,
    whole 1 gives 1 at cap 0 and 2 at cap 1.
  - `prorate` in `places`: $10 × 2/3 is $10.00 at 0 places and $7.00 at 1; $10 × 1/3 is $0.00 at 0 places
    and $3.00 at 1.
  - `multiply_rate` with a unit, and `round` half-up, in `unit`: 150 cents gives 200 at unit 100, 150 at
    unit 150 and 200 at unit 200.
  - `table_lookup` in `key` over the earned income credit tables, whose entries rise and then fall.

  Missing lemmas: the whole (`prorate`, `percent_floor`), the rate's denominator (`multiply_rate`) and any
  `table_lookup` property. No computed value is affected: cap, places and unit are data constants, and the
  EIC shape is the law's.
- **Fix:**
  - `Lemmas.lean` proves the antitone lemmas, the `tableBand` lemmas and `decide` counterexamples for each
    "neither".
  - `Atoms.lean` defines `tableBand`, and `Eval.lean`'s `bandTax` now runs through it.
  - Spec 6.3 replaces the sentence with a table of atom, argument, direction, condition and lemma.
- **Fix lines:** none (no form lines); files `lean/TaxFormalization/{Atoms,Eval,Lemmas}.lean`, `spec/spec.md` 6.3.
- **Siblings checked:** every atom in the spec 4 vocabulary (`engine/src/atoms.ts`), including
  `bracket_schedule`, which neither evaluator implements and no line uses. Also README lines 281–282 and
  docs/TRUST.md lines 67–71, which are stale and outside this package; replacement text is in REPORT.md.
- **Regression predictions:** no value changes. The TS/Lean comparison should show 0 differing cases and
  the fixtures should all pass. Both held: 2,042 cases, 0 differing; 1,442/1,442 fixtures.
- **Validation:** `lake build` with no `sorry`, and `#print axioms` showing only `propext`/`Quot.sound`;
  compare; test-fixtures.
- **Tags:** claim-accuracy; spec; lean; fixed
