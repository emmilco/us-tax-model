# Stage 2 modeling proposal

Status: approved by the owner on 2026-10-14; implementation and validation underway.
Prepared 2026-10-14 after the Stage 2 intent readback was approved. The owner
also authorized proceeding beyond Stage 2 if confidence warrants it.

## Evidence inspected

- `sources/2025/i1040gi.txt`, printed page 117, Schedule 3 line 11:
  more than one employer, wages above $176,100, withholding above $10,918.20;
  any one employer's overcollection goes to employer adjustment, or Form 843
  if the employer does not adjust it. Amounts are figured separately per spouse.
- `sources/2025/f1040s3.txt`: line 15 adds lines 9–12 and 14 and transfers
  to Form 1040 line 31. Line 11 is not the whole Schedule 3 total by definition.
- `sources/2025/fw2.txt`: employee identity, employer EIN, and boxes 1–8.
- `sources/2025/iw2w3.txt`, printed page 18: box 3 excludes social security
  tips; boxes 3 and 7 together have the $176,100 limit. Box 4 includes social
  security tax on tips and has the $10,918.20 limit. Box 1 excludes some
  deferrals included in box 3. This independently confirms both constants.

These are local archived-source inspections, not advice about an actual return.
Implementation citations will resolve revisions and hashes through the manifest.

## 1. Refusal scope — recommend a refused credit that blocks completion

When any employer's social security withholding exceeds $10,918.20, return a
cited refusal value for the credit and propagate it to dependent totals.
Keep independent computed lines available for inspection, but mark the return
incomplete and stop the interview with the remedy. Do not substitute zero.

The explanation names the employer entry, amount and threshold, asks for an
employer adjustment, and names Form 843 if the employer does not adjust the
overcollection. It must not imply that Form 843 is always required immediately.
This is a tool limitation on completing the credit in this situation, not an
IRS prohibition on computing the rest of the return.

One employer at or below the limit gives zero credit, not a refusal. Check
overcollection even when the multi-employer eligibility condition is false.
For multiple employers including an overcollecting employer, the initial tool
stops on that same refusal; it does not guess how to split a claim and a credit.

## 2. Collection encoding and binding

Recommend typed collection declarations pointing to reusable entry forms.
Instances have stable keys, not positional array indices. W-2 employer entries
are keyed within a person; person identity is an explicit binding. Identity keys
are structural metadata, not a new string arithmetic type or atom.

Illustrative aggregation syntax (not yet schema):

```yaml
expr:
  op: sum_over
  collection: w2
  field: w2.box4
  where:
    op: test
    eq: [{ entry_key: person }, { binding: person }]
```

Entry-local references resolve inside the selected entry; outer bindings are
explicit. Ordinary line references keep their existing meaning. A collection
roster must be explicitly closed before an aggregate is known: an unanswered
roster is unknown, whereas a confirmed empty roster sums to zero.

Add the already specified `Count` type and typed count literals. Each employer
entry supplies a structural count of one, allowing employer counts and counts
of overcollecting employers through `sum_over`, without adding a count atom.
Do not count W-2 sheets as different employers. Repeated employer identities
must be consolidated explicitly or rejected for correction, never overwritten.

The checker verifies entry types, binding types, numeric summed fields, Boolean
filters, and dependency cycles including filter, guard and instance-binding
edges. Filters are predicates, so exhaustiveness means a defined Boolean result
for each known entry; mutually exclusive/exhaustive branch checks apply to
`choose`. Unknown filter inputs make the affected aggregation unknown.

## 3. Person structure

Recommend a persons collection, with employer collections associated with its
keys, and a per-person credit definition. The return aggregates those credits
explicitly. The interview initially creates only `taxpayer`; married statuses
requiring spouse handling receive a cited scope refusal. Test the generic
collection machinery with two synthetic people to establish separation, while
keeping that path unavailable in the production interview. Enabling another
person later should change data and questions, not evaluator semantics.

## 4. Interview checks

Implement all three section 6.4 checks for the Stage 2 interview: finite answer
combinations end in completion or cited refusal; answer permutations produce
the same result; and questions are limited to reachable inputs. Include
unknown answers, corrections through appended events, and early refusal.

Enumerate the finite status/Boolean domains. Exercise monetary boundaries and
representative roster sizes separately; do not present finite testing as a
proof over arbitrary amounts or unbounded collections. A correction has an
explicit event order; permutation invariance applies to the same final answers,
not to reversing contradictory corrections.

Question wording, ordering, collection controls and citations are data. The
engine derives needed inputs from the chosen targets and current answers.
No automatic zero defaults for unanswered boxes or other Schedule 3 lines.

## 5. Gate structure

Recommend this precedence, expressed as cited Bool lines, `choose`, and refusal
metadata (no new refusal atom):

1. Unsupported filing/person or document scope produces a cited refusal.
2. Any employer over the withholding limit produces the refusal in section 1.
3. More than one employer AND per-person social security wages above the wage
   base selects the excess computation.
4. That computation is total withholding minus the withholding limit, floored
   at zero; the other branch is zero.

For W-2 social security wages, propose summing boxes 3 plus 7, rather than box 1,
based on the inspected W-2 instructions. Record this mapping explicitly as an
interpretation: page 117 itself says only "total wages". Railroad retirement
inputs must be detected and refused in this Social Security-only stage, rather
than treating box 14 as box 4. Read the relevant archived railroad instructions
before encoding that refusal.

Schedule 3 line 15 retains its actual printed sum, with other component inputs
explicitly resolved or left unknown. Its result flows to Form 1040 line 31;
do not silently zero unrelated credits and payments to force completion.

## Baseline and implementation findings

`npm run check-all` passed with the installed dependencies: 59/59 CLI fixtures,
64 tracked guards observed, 100 mutants (98 killed, 2 classified equivalent),
and TypeScript/Lean agreement on 259 cases and 8,547 values. This does not
replace the outstanding owner render review or human class B expectations.

The current evaluator stores money as JavaScript numbers and uses floating
arithmetic for rate multiplication, despite the stated integer-only design.
Stage 2 should use exact integer intermediates and checked JSON conversions,
including aggregation overflow checks, rather than extending that discrepancy.
The current cycle walk also omits test and choose-guard dependencies; extend
it as part of the collection/guard checks and include negative CLI fixtures.

The owner approved this proposal. The binding syntax was made concrete as nested
collections: `collection.parent` binds each employer collection to its current
person, so no redundant person filter or identity arithmetic is needed. Filters
still use entry-local typed comparisons. Rosters use `$collection@parentKey`
and input keys include stable entry keys.

After the ruling,
implement and validate Stage 2, publish its review artifacts and report any
remaining evidence gaps before deciding whether confidence supports Stage 3.
