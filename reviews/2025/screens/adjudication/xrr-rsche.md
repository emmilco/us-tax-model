# Screen and false-no adjudication, release rerun (lane xrr, family rsche)

Units: the royalty screens and gate that changed after the xint integration and were sampled again. These are
`royalty.business` and `royalty.depletion` (screens), and `gate:royalty.expenses_any` (screen and false-no). The family's
other units were already ruled. Tree: `.claude/worktrees/xint` (B1 plus expansion). The rulings are in
`/tmp/xrr/frag/rsche.screens.json` and `/tmp/xrr/frag/rsche.false_no.json`. Keys are `unruled:<unit>#1`, each with its
unit's current `subject_sha` and one entry per finding, for the lead to merge. `rulings.json` was not edited.
`python3 /tmp/xrr/xrr.py merge` (no `--write`) gives no REFUSED line for these keys.

Adjudicated by claude-opus-5-5 (judgment). Every encoding claim was checked against `forms/2025/royalty.yaml`, where
these were read:
- the `choose` of `royalty.line10`, `line16` and `line19` on `royalty.expenses_any`;
- the refusals at `royalty.line21`;
- the question sources.

The help and tick wording was checked in `interview/2025/questions.yaml` (the `royalty_rare` group). The quoted source
sentences were checked in `sources/2025/i1040se.cols.txt`, including the Line 18 geothermal sentence. No witness was
evaluated: the defects follow directly from a `choose` and from which questions exist.

**What changed since xrel.** The royalty questions are worded as in xrel. BUG-0889, BUG-0890 and BUG-0922 are all still
open (no Fix field), so the xrel dispositions stand. The new samples add no fact that moves the joint-return "you" finding
off presentation.

**Patterns, each ruled once and filed once (all existing entries; nothing new filed here):**
- `royalty.business` names four trades and only an oil or gas working interest. Other creators, NIL business income and
  mineral operating interests stay on Schedule E. Defect, low (BUG-0889).
- The royalty form has no at-risk screen for a loss. Both screens raised it. It is not either gate's question, but it is
  an open gap. Defect, low (BUG-0889).
- `royalty.expenses_any` asks "Did you pay any costs". Taxes the producer withheld, and charges an operator or agent
  kept from a payment reported gross, are answered No, so lines 16 and 19 are zero. Defect, medium, live (BUG-0890).
- A Yes to the cost question on capitalized costs reaches `royalty.amt10` and `amt19`, which do not exclude them.
  Defect, low (BUG-0922).

Classes as group 9: covered, accepted WIDE, model error, out of scope, presentation (wording only, or a rare case not
filed), defect, and open residual.

## Screen reviews

Samples: 3. Findings: 9. Classes: defect 6, presentation 2, accepted WIDE 1.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `royalty.business#1` | 0: defect (BUG-0889); 1: defect (BUG-0889); 2: defect (BUG-0889); 3: accepted WIDE; 4: presentation | defect: too few trades named, no at-risk screen (low) |
| `royalty.depletion#1` | 0: defect (BUG-0889); 1: presentation | no gate defect; the at-risk finding is BUG-0889 (low) |
| `gate:royalty.expenses_any#1` | 0: defect (BUG-0890); 1: defect (BUG-0922) | defect: withheld taxes answered No (medium); capitalized costs (low) |

Notes:
- `royalty.business#1` n3: the question already says "self-employed". A non-business author who answers Yes is refused
  at `royalty.line21` with the Schedule C remedy. That is a safe refusal.
- `royalty.depletion#1` n1: a geothermal deposit is mineral property (i1040se p. 7, Line 18). The question asks whether
  the filer claims depletion, and a No only forgoes a deduction the tool does not compute. Rare; wording only.
- `gate:royalty.expenses_any#1` n1: the sample says the lines get no amount from capitalized costs. That is wrong.
  `amt10` and `amt19` take them (BUG-0922).

## False-no reviews

Samples: 1. Findings: 5. Classes: defect 3, presentation 2.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:royalty.expenses_any#1` | 0: defect (BUG-0890); 1: defect (BUG-0890); 2: presentation; 3: presentation; 4: defect (BUG-0890) | defect: withheld taxes and netted charges answered No (medium) |

Notes:
- n2: a share of a tax-preparation fee. The gate's example "fees" reaches it. Wording only, as in xrel.
- n3: on a joint return the roster asks for royalties "you (or, on a joint return, your spouse)" received, and a cost
  the spouse paid is the couple's. The rental cost screens use the same "you". Wording only, as in xrel; no new fact.
- n4: an agent's or collecting society's fee kept before payment. BUG-0890's symptom names an agent's commission.

## Bugs

None filed here. Cited: BUG-0889 (low), BUG-0890 (medium) and BUG-0922 (low). The completeness adjudication of the
same family filed BUG-0925 and -02 (`reviews/2025/completeness/r10-xrr-rsche.findings.md`).
