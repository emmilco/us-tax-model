# Handoff: Stage 14 (self-employment), in progress

Read `HANDOFF.md` first, then `TASKS.md`, then this file. `HANDOFF-STAGE-13.md`
describes the stage before and holds the owner-confirmed Stage 14 scope (its
"Next" section; TASKS.md T-039).

## Sources archived

Added to `tools/sources-2025.json` and archived by `fetch_sources.py`, each with
its printed revision recorded in the manifest:

- Forms and instructions: `f1040sc`, `i1040sc`, `f1040sse`, `i1040sse`, `f4562`,
  `i4562`, `f7206`, `i7206` (all 2025 revisions).
- Publications for 2025 returns: `p334` (small business), `p946` (depreciation),
  `p463` (car expenses), `p587` (business use of home), `p560` (SEP/SIMPLE).
- `n-25-05`: Notice 2025-5, the 2025 standard mileage rates.
- Statistics of Income: `soi-nonfarm-sp` (the sole proprietorship statistics
  page), `soi-23sp02is` (Table 2, income statements, tax year 2023) and
  `soi-20sp04ra` (Table 4, returns with Schedule C attached, tax year 2020).

Not yet archived: Notice 2026-11 (special depreciation for property acquired after
January 19, 2025), which Pub. 463 cites; whether Form 4562 needs it is a question
for the premise check.

## Feature prevalence (measured from the SOI tables)

The published tables do not count returns per Schedule C line; Table 2 gives
amounts only. The owner accepted dollar shares as the proxy for line-level
features, with the confirmed slice unchanged.

Table 2, tax year 2023, all nonfarm sole proprietorships (31,125,909 returns;
total business deductions $1,687.3 billion):

| Item | Amount ($ billion) | Share of total deductions |
|---|---|---|
| Cost of sales and operations (Part III) | 560.0 | 33.2% |
| Car and truck expenses | 150.2 | 8.9% |
| Depreciation | 77.9 | 4.6% |
| Home office, both methods | 14.4 | 0.9% |

Table 4, tax year 2020, individual returns with Schedule C attached (28,353,367):

| Item | Returns | Share |
|---|---|---|
| Self-employment tax (and its deductible part) | 18,492,379 | 65.2% |
| Qualified business income deduction | 12,499,340 | 44.1% |
| Schedule C net loss | 7,750,203 | 27.3% |
| Self-employed health insurance deduction | 2,503,312 | 8.8% |
| Payments to a Keogh plan (SEP, SIMPLE, qualified plans) | 739,308 | 2.6% |
| Married filing separately | 566,596 | 2.0% |
| Predetermined estimated tax penalty | 3,899,939 | 13.8% |

The estimated tax penalty is out of scope by spec (the tool says the IRS will
figure it). Net losses are common enough that the loss paths (Schedule SE, the
earned-income readers) are part of the build, not an edge case. These counts are
for 2020 and 2023; the 2025 shares are assumed similar.
