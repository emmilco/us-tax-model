# Screen and false-no adjudication, release round (lane xrel, family k1p)

Units: the screens and gates of `f7203`, `k1p` and `qbi` sampled for the release. Tree: `.claude/worktrees/xint` (B1
plus expansion). The rulings are in `/tmp/xrel/frag/k1p.screens.json` and `/tmp/xrel/frag/k1p.false_no.json` (keys
`unruled:<unit>#1`, each with its unit's current `subject_sha`, and one entry per finding), for the lead to merge.
`rulings.json` was not edited. `python3 /tmp/xrel/xrel.py merge` (no `--write`) gives no REFUSED line for these keys.

Adjudicated by claude-opus-5-5 (judgment). Every quote was checked against `sources/2025/*.txt`, and every encoding
claim against `forms/2025/*.yaml` (gate expressions read), the interview help in `interview/2025/questions.yaml` and
evaluations. The witnesses are listed in `reviews/2025/completeness/r9-xrel-k1p.findings.md`. W4 is the test 5
witness used here.

**Reachability.** Every K-1 still refuses at `scope.k1`, so the k1p, k1s and f7203 defects are latent until the
integration lane wires the K-1 totals. `qbi.prior_form` and Form 8582 are live.

**Patterns, each ruled once in the tables and filed once:**
- Box 10, 11, 12, 13 (other than AE), 15 (other than O) and 21 items are refused at their own ticks. Findings about
  losses, deductions or trading items there are covered.
- A statement split by activity comes with box 22 or 23 checked, and `k1p.r_b2223` refuses it. Covered.
- Tests 5 and 6 are never asked of a partner who did no work in 2025: `k1p.ask_five` needs `k1p.under500`, which
  needs `k1p.work`. Defect, medium (-02). W4 shows box 1 income becoming passive.
- The participation questions say "(or, on a joint return, your spouse)". Spouse participation counts on any return
  (i8582 p. 5), and married filing separately is now in scope. Defect, medium (-03).
- Fiscal-year partnerships: the questions use calendar 2025. Defect, low (-04).
- "Show an amount" read against a code printed with STMT or `*`. Defect, low (-11), with the other box-tick lows.
- Item G decides the tests and active participation (non-manager LLC members, limited partners who also held a
  general interest), and the registered reading `amb.2025.k1p_prior_with_activity` leaves the held-back loss of a
  K-1 with boxes 1 to 3 blank unasked. Open residual, for the owner's review (-12). These choices understate
  deductions.
- `f7203.required` leaves out three Who Must File triggers: disposition, loan repayment and basis carryover. Each is
  refused on the K-1 by an ungated screen (`k1s.disposed`, `k1s.box16ef_if_16`, `k1s.basis_carry`). Covered.

Classes as group 9: covered, accepted WIDE, model error, out of scope, presentation (wording only, or a rare case
not filed), defect, and open residual (a registered or owner-level reading). The bug numbers in the tables are the
suffixes of the pending entries xrelk1p-NN, numbered at integration in order: -01 is BUG-0836 and -14 is BUG-0849.

## Screen reviews

Samples: 44. Findings: 127. Classes: defect 43, covered 28, accepted WIDE 22, presentation 16, open residual 12, model error 5, out of scope 1.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `f7203.election#1` | 0: defect (-13); 1: accepted WIDE; 2: presentation (-13) | defect: the election help names only an earlier return (low) |
| `f7203.loans#1` | 0: defect (-13); 1: defect (-13); 2: presentation; 3: presentation | defect: guarantee payments and open-account advances are steered to No (low) |
| `k1p.b19_other#1` | 0: covered | no gate defect; code A above basis is asked at k1p.dist_over |
| `k1p.basis_short#1` | 0: out of scope; 1: defect (-06); 2: defect (-10); 3: accepted WIDE; 4: presentation | defect: no screen for basis carryovers; basis definition omits items (low/medium) |
| `k1p.dist_over#1` | 0: defect (-10); 1: defect (-10); 2: accepted WIDE; 3: presentation | defect: 'money you took out' omits marketable securities and deemed distributions (low) |
| `k1p.not_at_risk#1` | 0: defect (-10); 1: defect (-10); 2: defect (-10); 3: accepted WIDE; 4: accepted WIDE; 5: covered; 6: presentation | defect: at-risk question misses the partnership's nonrecourse debt and other protections (low) |
| `k1p.prior_not_active#1` | 0: defect (-12); 1: defect (-12); 2: accepted WIDE; 3: presentation | defect: earlier-year test omits the limited-partner bar and 'at any time' (low) |
| `k1p.r_b10#1` | 0: covered | no gate defect; per-activity section 1231 amounts mean more than one activity |
| `k1p.r_b11#1` | 0: defect (-11) | defect: a code with STMT can be answered as no amount (low) |
| `k1p.r_b13#1` | 0: defect (-11) | defect: a code with STMT can be answered as no amount (low) |
| `k1p.r_b14bc#1` | 0: accepted WIDE; 1: defect (-11) | no gate defect beyond the STMT wording; code C without the optional method is a safe over-refusal |
| `k1p.r_b15#1` | 0: defect (-11) | defect: a code with STMT can be answered as no amount (low) |
| `k1p.r_b16#1` | 0: defect (-11); 1: covered; 2: presentation | defect: a Schedule K-3 received on request is not caught (low) |
| `k1p.r_b17#1` | 0: defect (-11); 1: presentation | defect: a code with STMT can be answered as no amount (low) |
| `k1p.r_b20#1` | 0: defect (-11); 1: accepted WIDE; 2: presentation | defect: cooperative items on code Z pass (low); informational codes over-refuse safely |
| `k1p.r_b2223#1` | 0: model error; 1: presentation; 2: model error | no gate defect |
| `k1p.r_b4b#1` | 0: presentation | no gate defect |
| `k1p.r_disposed#1` | 0: covered; 1: defect (-10); 2: presentation; 3: covered | defect only for a deemed distribution above basis (low); other cases are asked elsewhere |
| `k1p.r_foreign#1` | 0: defect (-11) | defect: territory partnerships not named as foreign (low) |
| `k1p.t4#1` | 0: accepted WIDE; 1: accepted WIDE; 2: accepted WIDE; 3: presentation; 4: defect (-04) | no gate defect beyond the fiscal-year period; the WIDE cases refuse safely |
| `k1p.t6#1` | 0: defect (-05) | defect: test 6 omits the capital-not-material catch-all (low) |
| `k1p.t7#1` | 0: defect (-04); 1: accepted WIDE; 2: covered | defect: calendar 2025 instead of the partnership's year (low) |
| `k1p.trader#1` | 0: covered; 1: accepted WIDE; 2: accepted WIDE; 3: presentation | no gate defect |
| `k1p.z_other#1` | 0: defect (-11); 1: defect (-11); 2: defect (-11) | defect: cooperative items without a payment pass (low) |
| `gate:f7203.required#1` | 0: covered; 1: covered; 2: covered; 3: covered; 4: accepted WIDE | no gate defect; every Who Must File trigger the gate leaves out is refused on the K-1 |
| `gate:k1p.any_loss#1` | 0: covered; 1: covered; 2: covered; 3: defect (-10); 4: accepted WIDE | no gate defect for the boxes, which are refused; carryovers and basis wording filed |
| `gate:k1p.ask_active#1` | 0: open residual (-12); 1: accepted WIDE | open residual: item G decides active participation (owner review) |
| `gate:k1p.ask_five#1` | 0: defect (-02); 1: defect (-03) | defect: test 5 never asked of a partner who did no 2025 work (medium) |
| `gate:k1p.ask_nearly_all#1` | 0: open residual (-12); 1: model error; 2: accepted WIDE | open residual for a limited partner with a general interest; otherwise no defect |
| `gate:k1p.ask_other#1` | 0: model error; 1: accepted WIDE | no gate defect |
| `gate:k1p.ask_other_gp#1` | 0: open residual (-12); 1: defect (-03); 2: model error; 3: accepted WIDE | open residual (item G) and defect (spouse on a separate return) |
| `gate:k1p.decisions_if_asked#1` | 0: presentation; 1: open residual (-12); 2: defect (-03) | open residual (item G) and defect (spouse on a separate return) |
| `gate:k1p.gp_under500#1` | 0: open residual (-12); 1: defect (-03) | open residual (item G) and defect (spouse on a separate return) |
| `gate:k1p.has_activity#1` | 0: open residual (-12); 1: covered; 2: open residual (-12) | open residual: registered reading on held-back losses of a K-1 with boxes 1 to 3 blank |
| `gate:k1p.has_b1#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect |
| `gate:k1p.has_b19#1` | 0: defect (-11); 1: accepted WIDE | defect: a code with a zero or STMT amount can be answered as no amount (low) |
| `gate:k1p.has_b9a#1` | 0: covered; 1: defect (-11); 2: defect (-11) | defect: box 9b with box 9a netting to zero is not asked (low) |
| `gate:k1p.has_b9bc_if_9a#1` | 0: covered; 1: defect (-11); 2: defect (-11) | defect: box 9b with box 9a netting to zero is not asked (low) |
| `gate:k1p.prior_any_if_activity#1` | 0: open residual (-12); 1: covered; 2: covered | open residual: registered reading on held-back losses of a K-1 with boxes 1 to 3 blank |
| `gate:k1p.prior_b1_any_if#1` | 0: open residual (-12); 1: covered | open residual: registered reading on held-back losses of a K-1 with boxes 1 to 3 blank |
| `gate:k1p.prior_b2_any_if#1` | 0: open residual (-12); 1: covered | open residual: registered reading on held-back losses of a K-1 with boxes 1 to 3 blank |
| `gate:k1p.prior_b3_any_if#1` | 0: open residual (-12); 1: open residual (-12) | open residual: registered reading on held-back losses of a K-1 with boxes 1 to 3 blank |
| `gate:k1p.work_if_b1#1` | 0: defect (-08); 1: covered; 2: defect (-04); 3: defect (-03); 4: covered | defects: box 2 real estate professional (medium), fiscal year (low), spouse on a separate return (medium) |
| `gate:qbi.prior_form#1` | 0: covered; 1: defect (-14); 2: covered; 3: defect (-14) | defect: a carryforward from a Form 8995 earlier than 2024 is dropped (low) |

## False-no reviews

Samples: 28. Findings: 138. Classes: defect 48, presentation 35, covered 31, open residual 16, model error 6, accepted WIDE 1, out of scope 1.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:f7203.required#1` | 0: covered; 1: covered; 2: covered; 3: covered | no false no: each trigger is refused on the K-1 |
| `gate:k1p.any_loss#1` | 0: covered; 1: covered; 2: covered; 3: defect (-06); 4: covered; 5: defect (-10); 6: defect (-10) | false no only for carryovers and the basis/at-risk wording; the boxes are refused |
| `gate:k1p.ask_active#1` | 0: open residual (-12); 1: open residual (-12); 2: open residual (-12) | open residual (item G; held-back loss with box 2 blank) |
| `gate:k1p.ask_five#1` | 0: defect (-02); 1: presentation; 2: defect (-03); 3: model error; 4: presentation | false no: retired partner (medium) and spouse on a separate return (medium) |
| `gate:k1p.ask_nearly_all#1` | 0: defect (-04); 1: covered; 2: open residual (-12); 3: covered; 4: model error | false no only for the fiscal year and item G cases |
| `gate:k1p.ask_other#1` | 0: defect (-05); 1: defect (-03); 2: presentation; 3: defect (-02); 4: defect (-02); 5: defect (-04); 6: presentation; 7: covered | false no: test 6 catch-all, retired partner, spouse, fiscal year |
| `gate:k1p.ask_other_gp#1` | 0: open residual (-12); 1: open residual (-12); 2: defect (-03); 3: defect (-03); 4: defect (-04); 5: presentation; 6: covered | open residual (item G); defects for spouse on a separate return and fiscal year |
| `gate:k1p.ask_prior_active#1` | 0: covered; 1: model error; 2: defect (-12); 3: presentation; 4: accepted WIDE | false no only for the limited-partner and at-any-time wording |
| `gate:k1p.decisions_if_asked#1` | 0: presentation; 1: open residual (-12); 2: open residual (-12); 3: open residual (-12); 4: covered; 5: presentation | open residual (item G, blank box 2); no false no on a joint return |
| `gate:k1p.gp_under500#1` | 0: defect (-04); 1: defect (-03); 2: defect (-03); 3: covered; 4: covered; 5: open residual (-12); 6: open residual (-12); 7: defect (-08) | false no: fiscal year, spouse on a separate return, real estate professional; item G open |
| `gate:k1p.has_activity#1` | 0: open residual (-12); 1: covered; 2: defect (-11); 3: presentation; 4: presentation; 5: out of scope | open residual: registered reading; STMT wording filed |
| `gate:k1p.has_b1#1` | 0: covered; 1: covered; 2: covered; 3: defect (-02); 4: defect (-04); 5: defect (-03); 6: presentation | false no: retired partner, fiscal year, spouse on a separate return |
| `gate:k1p.has_b14a#1` | 0: presentation; 1: presentation; 2: defect (-11); 3: presentation | false no only for STMT |
| `gate:k1p.has_b15o#1` | 0: defect (-11); 1: presentation; 2: model error | false no only for STMT |
| `gate:k1p.has_b18a#1` | 0: defect (-11); 1: presentation; 2: model error | false no only for STMT |
| `gate:k1p.has_b19#1` | 0: defect (-11); 1: defect (-10); 2: defect (-11); 3: presentation | false no: STMT or zero code; deemed distributions |
| `gate:k1p.has_b20z#1` | 0: defect (-11); 1: defect (-11); 2: defect (-11); 3: defect (-11) | false no: STMT and cooperative items (low) |
| `gate:k1p.has_b5#1` | 0: defect (-11); 1: presentation | false no only for STMT |
| `gate:k1p.has_b6a#1` | 0: defect (-11); 1: defect (-11); 2: presentation | false no only for STMT |
| `gate:k1p.has_b8#1` | 0: defect (-11); 1: presentation; 2: model error | false no only for STMT |
| `gate:k1p.has_b9a#1` | 0: defect (-11); 1: covered; 2: defect (-11); 3: defect (-11) | false no: box 9b with 9a netting to zero; STMT (low) |
| `gate:k1p.has_b9bc_if_9a#1` | 0: defect (-11); 1: defect (-11); 2: presentation | false no: box 9b with 9a netting to zero; 9c STMT not refused (low) |
| `gate:k1p.prior_any_if_activity#1` | 0: open residual (-12); 1: presentation; 2: covered; 3: covered | open residual: registered reading |
| `gate:k1p.prior_b1_any_if#1` | 0: covered; 1: open residual (-12); 2: presentation; 3: presentation; 4: presentation | open residual: registered reading |
| `gate:k1p.prior_b2_any_if#1` | 0: covered; 1: open residual (-12); 2: presentation; 3: presentation; 4: presentation; 5: presentation | open residual: registered reading |
| `gate:k1p.prior_b3_any_if#1` | 0: open residual (-12); 1: covered; 2: presentation; 3: presentation; 4: presentation; 5: presentation | open residual: registered reading |
| `gate:k1p.work_if_b1#1` | 0: defect (-04); 1: defect (-08); 2: defect (-03); 3: covered; 4: covered; 5: covered | false no: fiscal year, real estate professional, spouse on a separate return |
| `gate:qbi.prior_form#1` | 0: defect (-14); 1: defect (-14); 2: covered; 3: covered; 4: presentation; 5: defect (-14); 6: presentation | false no: carryforward from a year before 2024 (low) |

## Defects and open residuals filed (pending)

| Pending id | Severity | Title |
| --- | --- | --- |
| BUG-0836 | medium | Form 8582: a married-filing-separately filer who lived with the spouse gets the rental special allowance and the filing exception |
| BUG-0837 | medium | k1p: tests 5 and 6 are never asked of a partner who did no work in the business in 2025 |
| BUG-0838 | medium | k1p: the participation questions count the spouse only on a joint return |
| BUG-0839 | low | k1p: a fiscal-year partnership is not asked about, and the participation questions use calendar 2025 |
| BUG-0840 | low | k1p.t6 lists eight service fields and omits any other business in which capital is not a material income-producing factor |
| BUG-0841 | medium | k1p: no screen for the partner's own Schedule E items (unreimbursed partnership expenses, interest to buy the interest, basis or at-risk carryovers, the prior-year fuel credit) |
| BUG-0842 | medium | K-1 integration: the excess business loss limit and the QBI share of a suspended loss are not applied to partnership amounts |
| BUG-0843 | medium | k1p: a real estate professional's or personal-use rental in box 2 is treated as passive |
| BUG-0844 | low | k1p: box 1 nonpassive exceptions not screened (oil or gas working interest held as general partner; significant participation income) |
| BUG-0845 | low | k1p basis, distribution and at-risk questions: lows in the basis definition and the at-risk cases |
| BUG-0846 | low | k1p box questions: lows (STMT entries, K-3 received on request, territory partnerships, box 9b or 9c with box 9a blank, cooperative items on code Z) |
| BUG-0847 | low | k1p item G and active participation: non-manager LLC members, limited partners holding a general interest, and the earlier-year tests (owner review) |
| BUG-0848 | low | Form 7203 questions: lows (line 2 property and compensation stock, payments under a guarantee, open-account advances, an election made with this return) |
| BUG-0849 | low | qbi.prior_form: a carryforward from a Form 8995 earlier than 2024 is dropped |
