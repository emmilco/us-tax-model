# Differential records (class C)

Independent-calculator records for the whole-return cases in
`fixtures/2025/stage5.json`. The calculators run outside this repository; the
records here are their outputs, compared offline against the computed values.

## Procedure (per calculator per case)

1. Open the calculator for tax year 2025. The named choices are FreeTaxUSA and
   OLT; any two named, versioned calculators are acceptable.
2. Enter the case using the entry sheet at
   `reports/2025/differential.<case>.md` — synthetic data only.
3. Read back the lines the calculator shows, in integer cents.
4. Save the record here as `<calculator>.<case>.json`:

```json
{
  "calculator": "FreeTaxUSA",
  "version": "2025 tax year, accessed 2026-10-16",
  "case": "stage5.return.owed",
  "values": { "f1040.line15": 10895000 },
  "investigations": {}
}
```

5. Run `node engine/dist/main.js differential` (or `npm run check-all`).
   A recorded value that differs from the computed value fails the run unless
   `investigations` carries a cited cause for that line.

Never enter personal return data into a calculator for this exercise.
