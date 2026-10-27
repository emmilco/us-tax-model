# Equivalence review — the 89 argued mutation survivors

Integrity plan item 1.6, part one. Each argued equivalence in `engine/src/mutate.ts` is classified
by the shape of its argument, mapped to the evaluation-order rules of `spec/spec.md` section 4.7,
and checked for whether its `holds` predicate verifies the structural premises its prose states.
This review does not judge whether the arguments are true; that is the second reader's task under
the plan. It judges only what is checked mechanically and what is left to prose.

Maintenance update, 2026-10-23 (BUG-0116): removed the eight dead entries and nine prose fallbacks
identified below. Each of the eight mutants was re-probed and killed by fixtures; the nine remaining
survivors are still proved by the mechanical copy-chain check. A fresh mutation run retains 2,278
mutants, 235 checker kills, 1,915 fixture kills and 128 equivalent survivors (94.4% raw, 100% adjusted).
The registered tables now contain 15 prose entries and 57 conditional entries. The 89-row table
below preserves the original audit baseline; independent review and further mechanization remain open.

## What was found before the rows

- **The 89 are two tables, not one.** `EQUIVALENT_IF` has 60 keyed entries, each with `reason`
  and `holds`. The other 29 are in `EQUIVALENT`, a table of prose reasons with no `holds` at all;
  they are accepted on every run without any check against the data. The plan's "89 arguments"
  is the union.
- **Eight entries are dead.** Their mutants are now killed by fixtures (probed this run against the
  current data and the fixture cases), so the entry is never consulted:
  `operand.s8812.s8812.line13.clw_a5` (its `holds` also fails on the current data),
  `filter.person.person.hsa_share`, `operand.s1a.s1a.line4c_one.line4a`,
  `boundary.person.person.files_se`, `operand.sc.sc.ho_both.zero`,
  `operand.sc.sc.ho_limited.ho_line4`, `operand.f8889.f8889.family_year.family_under55`,
  `operand.f8889.f8889.self_year.self_amount`. They are marked *stale* below.
- **Nine prose entries are superseded at run time.** `runMutation` tries `aliasEquivalence` first
  and overwrites the prose reason when the copy-chain rule accepts the mutant; the current report
  shows the copy-chain text for `operand.qdcg.qdcg.line12.line11` and the eight `operand.sd.sd.*`
  entries. The prose is a silent fallback: if the chains ever stop matching, the prose text would
  take over without anyone noticing that the mechanical check had lapsed.
- **Live counts.** 57 `EQUIVALENT_IF` entries are live (the 57 "structural conditions re-checked"
  lines in `reports/2025/mutation.md`); 15 prose entries are live and prose-only.
- **What the run observes.** The mutation run compares only the fixture expectations, which are
  recorded for `f1040.*` and `qdcg.*` keys and omit unknowns and refusals (spec 4.7.7). Many
  arguments say "no value can change"; the run checks only that no recorded Form 1040 or QDCG
  value changes. Several arguments (the `skipGated` dozen, `s1aPartGate`, `agiFirst`) are true
  as "no value that is read changes" while the mutated line's own value does change; it is simply
  not observed. The second reader should hold each argument to the claim it makes.

## Shapes

| Shape | Meaning |
| --- | --- |
| copy-chain identity | both operands expand, through copies, to the same source with the same remaining gates (the `aliasEquivalence` rule) |
| shared-gate | the replaced operand and another operand of the same reader carry the same gate, so whichever refuses the result is the same refusal, and when none does the operands are equal |
| first-read-carries | a removed refusal entry is redundant because a line read first (first operand, first conjunct, or a sum operand) carries the same gate and refuses before the entry could decide |
| skip-gated | the mutated line is read only under a gate that makes the two operands equal (a `choose` branch, a worksheet part, a skip rule) |
| zero-behind-gates | an operand is $0 behind refusal gates, and either the gate is carried elsewhere on the route or the zero is absorbed arithmetically |
| algebraic identity | min/max/floor/rate arithmetic makes the two expressions equal at every input (including boundary cases where both branches coincide) |
| status-scoped | the lines differ only for a filing status, year or table row that the route cannot reach |
| filter-redundant | a `sum_over` filter keeps every entry that is ever read |
| other | an argument of none of these shapes (table plateaus, empty rosters, value-level boundary cases) |

Rules cited are spec 4.7 subsections: 4.7.1 gates at line entry; 4.7.2 `all`/`any`/`not` and
comparisons; 4.7.3 `choose`; 4.7.4 operand order and the incompleteness rule; 4.7.5 `sum_over`;
4.7.6 memoization; 4.7.7 other (every line is a target; observation scope; arithmetic).

## The rows

`holds` column: **yes** = every structural premise the prose states is checked; **partly** = some
premise the prose rests on is not checked (named); **none** = prose table, nothing checked.
Mechanization: **candidate** = a generic structural rule like copy-chain could accept it with the
primitives `mutate.ts` already has (`normalizeChain`, `readersOf`, `operandRefs`, `gateOf`,
`gateImplies`); **new primitive** = needs a kind of reasoning the tool does not have; **prose** =
inherently an argument about values, better killed by a fixture than mechanized.

| # | Mutant | Table | Shape | 4.7 rules | `holds` vs prose | Mechanization |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `operand.eic.eic.step5_line4.zero` | IF | zero-behind-gates (gate carried by an earlier sum operand's chain) | 4.7.1, 4.7.4 (sum stops at first refusal), 4.7.7 copy | partly: checks line 4 and line 2 copy `eic.zero`, line 3 takes line 2, `earned_income` sums [line 3, line 4] in that order, line 2's gates are all `scope.other_income`; unchecked: that line 4 has its own combat-pay gate (the prose's first clause), that `earned_income` is line 4's only reader, that the replacement is line 2 (the mutation note is not read) | candidate: shared-gate extended to a gate carried by an earlier operand's chain |
| 2 | `refusal.eic.eic.step1_resident.0` | IF | first-read-carries | 4.7.1, 4.7.2 (first conjunct), 4.7.6, 4.7.7 (observed values) | partly: checks the entry's gate, that some line reachable from `f1040.line11b` carries a gate with the same `when`, `eic.eligible` reads `below_top` first, `below_top` reads `line11b` first; unchecked: that the carrier lies on every evaluated path (the search walks every operand, `choose` branches not taken included), that form/remedy/cite agree, that Form 1040 reaches EIC only through `eic.eligible` | new primitive: path dominance (every evaluated path from the observed lines passes a carrier) |
| 3 | `refusal.eic.eic.step5_line2.0` | IF | first-read-carries | as 2 | as 2 | as 2 |
| 4 | `refusal.eic.eic.step2_other.0` | IF | first-read-carries | as 2 | as 2 | as 2 |
| 5 | `refusal.eic.eic.step5_line1.0` | IF | first-read-carries | as 2 | as 2 | as 2 |
| 6 | `param.eic.ws_threshold0.other.$1` | IF | other (lookup plateau) | 4.7.4 (`smaller_of`), `table_lookup` | partly: checks that the bands covering [amount, amount + $1) print the column maximum; unchecked: everything about the worksheet lines (line 5 is the lookup keyed on line 3, line 6 is min(line 5, line 2), line 2 never exceeds the maximum, a blank line 5 leaves line 6 = line 2) | new primitive: parameter shift inside a lookup plateau with min absorption |
| 7 | `param.eic.ws_threshold0.joint.$1` | IF | other | as 6 | as 6 | as 6 |
| 8 | `param.eic.ws_threshold1.joint.$1` | IF | other | as 6 | as 6 | as 6 |
| 9 | `operand.s8812.s8812.line13.clw_a5` | IF | zero-behind-gates | 4.7.4 (subtract, first operand), 4.7.1 | **stale**: `holds` fails on the current data and the mutant is killed by fixtures; as written, partly (carrier matched by `when` only) | remove the entry |
| 10 | `boundary.eic.eic.wsb_4b_positive` | IF | other (boundary at $0, argued value-wise) | 4.7.2 (`all` order and early stop), 4.7.3 | partly: checks eight positive `eic.limitN` parameters, the sole reader, `step5_income`'s comparison, the SE branch of `earned_for_limit`, conjunct order in the stop; unchecked: that `eic.limit` reads those parameters, that `wsb_4b_positive` is `wsb_4b > 0`, the "no refusal newly reached" clause | prose; a fixture at line 4b = $0 would settle it |
| 11 | `filter.person.person.hsa_step1` | IF | filter-redundant | 4.7.5, 4.7.1, 4.7.6 | partly: checks reader chains, that `allocation_bad` mentions `hsa_split_count == 1`, that `share` is gated by `allocation_bad` and read only by `line6_split`; unchecked: the filter's own predicate, that `allocation_bad` is reached only on a form using the rule, the both-forms case | prose |
| 12 | `filter.person.person.hsa_share` | IF | filter-redundant | as 11 | **stale**: killed by fixtures; as written, as 11 | remove the entry |
| 13 | `refusal.ssb.ssb.line6.0` | IF | first-read-carries (with reader) | 4.7.1, 4.7.4 (first operand; a sum reaches every operand up to a refusal), 4.7.6 | yes: sole reader, reader reads the chain head first, each link is a first operand or any sum operand, the last carries the same `when` (form/remedy/cite deliberately not compared: the entry fires on neither route) | candidate: discover the chain generically for every remove-refusal survivor |
| 14 | `boundary.s1a.s1a.line10_over` | IF | algebraic identity (boundary at equality; excess zero) | 4.7.3, 4.7.7 arithmetic (rate × 0, round of 0, floor) | partly: checks the whole expression chain (`gt` operands, `pos`, `cut`, `figured`, the chooser's `then`s); unchecked: which guard selects which branch, that `cut`'s rate is a known parameter | fixture at MAGI = base; a rule needs a new primitive (both branches evaluated symbolically at the boundary) |
| 15 | `boundary.s1a.s1a.line18_over` | IF | algebraic identity | as 14 | as 14 | as 14 |
| 16 | `boundary.s1a.s1a.line27_over` | IF | algebraic identity | as 14 | as 14 | as 14 |
| 17 | `boundary.s1a.s1a.line33_over` | IF | algebraic identity | as 14 | as 14 | as 14 |
| 18 | `operand.s1a.s1a.line6_calc.line5` | IF | skip-gated | 4.7.3, 4.7.6, 4.7.7 (observation scope) | partly, weak: checks only that the gated line is a two-way `choose` between `s1a.zero` and its figure on the part flag; the load-bearing clause ("the chain that reads it is reached only through the part's result line, which is $0 when the part does not apply") is not checked: no reader check, no gate implication | candidate: extend `skipGated` to a reader chain (every transitive reader up to the part's result line gated by the same flag) |
| 19 | `operand.s1a.s1a.line7_calc.line6` | IF | skip-gated | as 18 | as 18 | as 18 |
| 20 | `operand.s1a.s1a.line10_calc.line8` | IF | skip-gated | as 18 | as 18 | as 18 |
| 21 | `operand.s1a.s1a.line10_pos.line9` | IF | skip-gated | as 18 | as 18 | as 18 |
| 22 | `operand.s1a.s1a.line13_figured.line12` | IF | skip-gated | as 18 | as 18 | as 18 |
| 23 | `operand.s1a.s1a.line14c_calc.line14b` | IF | skip-gated | as 18 | as 18 | as 18 |
| 24 | `operand.s1a.s1a.line18_calc.line16` | IF | skip-gated | as 18 | as 18 | as 18 |
| 25 | `operand.s1a.s1a.line18_pos.line17` | IF | skip-gated | as 18 | as 18 | as 18 |
| 26 | `operand.s1a.s1a.line21_figured.line20` | IF | skip-gated | as 18 | as 18 | as 18 |
| 27 | `operand.s1a.s1a.line27_calc.line25` | IF | skip-gated | as 18 | as 18 | as 18 |
| 28 | `operand.s1a.s1a.line27_pos.line26` | IF | skip-gated | as 18 | as 18 | as 18 |
| 29 | `operand.s1a.s1a.line30_figured.line29` | IF | skip-gated | as 18 | as 18 | as 18 |
| 30 | `operand.s1a.s1a.line33_calc.line31` | IF | skip-gated | as 18 | as 18 | as 18 |
| 31 | `operand.s1a.s1a.line33_pos.line32` | IF | skip-gated | as 18 | as 18 | as 18 |
| 32 | `operand.s1a.s1a.line35_figured.line34` | IF | skip-gated | as 18 | as 18 | as 18 |
| 33 | `operand.s1a.s1a.line24_calc.line23` | IF | skip-gated | as 18 (the flag is the car-loan question itself) | as 18 | as 18 |
| 34 | `operand.s1a.s1a.line4c_one.line4a` | IF | skip-gated (branch-scoped) | 4.7.3 | **stale**: killed by fixtures; as written, as 35 | remove the entry |
| 35 | `operand.s1a.s1a.line4c_one.line4b` | IF | skip-gated (branch-scoped) with max(a, 0) = a | 4.7.3, 4.7.4 | partly: checks `line4c_one` = `larger_of` [4a, 4b], 4b's figure is the zero parameter, 4a and 4c choose on the same one-employer guard; unchecked: that `line4c_one` is read only by `line4c`, that line 4a is non-negative (its type is not checked), that line 4b's Form 4137 gate cannot fire on this route | new primitive: branch-scoped evaluation |
| 36 | `boundary.sli.sli.over` | IF | algebraic identity (prorate ratio clamped at 0) | 4.7.3, 4.7.7 arithmetic (prorate clamp) | partly: checks line 8 chooses between figured and zero, figured prorates line 6, line 6 = line 4 − line 5, `over` is line 4 > line 5, zero parameter; unchecked: guard-to-branch binding, that the prorate's `whole` is positive (otherwise `prorate` is unknown, not $0) | fixture at line 4 = line 5; rule needs the symbolic-boundary primitive |
| 37 | `operand.sli.sli.line9.line8` | IF | algebraic identity | as 36 | as 36 | as 36 |
| 38 | `refusal.dependent.dependent.qualifying_relative.2` | IF | first-read-carries (through `any`/`all` first conjuncts) | 4.7.1, 4.7.2 (first conjunct; refusal stops), 4.7.6, 4.7.7 (every line is a target: the gate still fires when `qualifying_relative` is evaluated as a target, unobserved) | yes: entry identical as a whole record on `qualifying_child`, sole-reader chain, first-conjunct reads | candidate: `firstReadCarries` with generic chain discovery (first-conjunct links are already first operands) |
| 39 | `operand.sdtw.sdtw.raw27.line26` | IF | skip-gated | 4.7.3, 4.7.6, 4.7.7 (copy-chain normal form; the raw line's own value changes when the gate is false, unobserved) | yes: sole reader, reader is the gate taking the raw line, gate implication, chain normalization of the wrapped operand | already mechanical in form; run `skipGated` discovery over every operand survivor instead of keying it per mutant |
| 40 | `operand.sdtw.sdtw.raw28.line22` | IF | skip-gated | as 39 | yes | as 39 |
| 41 | `operand.sdtw.sdtw.raw29.line27` | IF | skip-gated | as 39 | yes | as 39 |
| 42 | `operand.sdtw.sdtw.raw30.line29` | IF | skip-gated | as 39 | yes | as 39 |
| 43 | `operand.sdtw.sdtw.raw31.line30` | IF | skip-gated | as 39 | yes | as 39 |
| 44 | `operand.sdtw.sdtw.raw33.line32` | IF | skip-gated | as 39 | yes | as 39 |
| 45 | `operand.sdtw.sdtw.raw34.line33` | IF | skip-gated | as 39 | yes | as 39 |
| 46 | `operand.sdtw.sdtw.raw38.line37` | IF | skip-gated | as 39 | yes | as 39 |
| 47 | `operand.sdtw.sdtw.raw39.line38` | IF | skip-gated | as 39 | yes | as 39 |
| 48 | `operand.sdtw.sdtw.raw40.line39` | IF | skip-gated | as 39 | yes | as 39 |
| 49 | `operand.sdtw.sdtw.raw42.line41` | IF | skip-gated | as 39 | yes | as 39 |
| 50 | `operand.sdtw.sdtw.raw43.line42` | IF | skip-gated | as 39 | yes | as 39 |
| 51 | `operand.sdtw.sdtw.line45.line43` | IF | skip-gated with rate × $0 | 4.7.3, 4.7.4 (pass-through), 4.7.7 arithmetic | partly: checks both gates are the same line, `raw43` is `multiply_rate` of line 42; unchecked: that the rate is a known parameter (minor) | candidate: `skipGated` plus zero absorption through `multiply_rate` |
| 52 | `operand.sdtw.sdtw.line17.line16` | IF | algebraic identity (min nesting; non-negativity) | 4.7.4 (`smaller_of` order; subtract's first operand) | yes: every stated structural premise is checked, including line 1's type | new primitive: order/lattice reasoning with non-negativity |
| 53 | `operand.f8959.f8959.line18.line17` | IF | zero-behind-gates (through floor and rate) | 4.7.4 (first operand), 4.7.1, 4.7.7 arithmetic | yes (rate knownness unchecked, minor) | candidate: zero-behind-gates propagated through `subtract_floor0` and `multiply_rate` |
| 54 | `operand.f8960.f8960.line8.line5d` | IF | shared-gate (zeros behind gates carried by the first operand) | 4.7.4 (sum: first operand, stop at refusal), 4.7.1 | yes: first operand, nested sum, gated zeros whose entries equal line 1's record for record | candidate: `sharedGateEquivalence` extended through a nested sum |
| 55 | `operand.f8960.f8960.line9d.line9c` | IF | shared-gate (sum of chain-identical gated zeros) | 4.7.4, 4.7.1 | yes | candidate: "a sum whose operands each normalize to the replaced gated zero" |
| 56 | `refusal.f4952.f4952.required.2` | IF | first-read-carries (no reader; entry last) | 4.7.1 (entry must be last), 4.7.4 (first operand) | yes | candidate: generic chain discovery (as 13) |
| 57 | `operand.f2441.f2441.line25.line24` | IF | algebraic identity (min with ungated $0; a − 0) | 4.7.4 | yes | candidate: the floor-minus-min pattern rule (see 60) |
| 58 | `refusal.retirement.retirement.amount_a.1` | IF | first-read-carries (next gate takes over; last conjunct of an `all`) | 4.7.1 (non-last entry removed), 4.7.2 ([unknown, refusal] is a refusal; a deciding false), 4.7.4, 4.7.6 | partly: checks the gate list exactly, the first two entries identical to `rolled`'s, that `annuity_rollover` is an `all` whose last conjunct's text mentions `has_rollover`, that `has_rollover` reads `rolled` first, and the first-read chain `amount_a → show_a → has_rollover → rolled`; unchecked: that the last conjunct reads `has_rollover` directly (text match only), and the case of an earlier conjunct unknown while `rolled` does not refuse | new primitive: gate-list rewriting (removal of entry i is neutral when the next gate's evaluation reaches an identical carrier) |
| 59 | `operand.person.person.dc_earned.eic_se` | IF | other (empty roster sums to $0 along a chain) | 4.7.5 (confirmed empty roster is $0; unconfirmed is unknown), 4.7.3, 4.7.2 | yes: every clause has a structural check | prose; a fixture with the Schedule C roster confirmed empty would exercise it |
| 60 | `operand.f5695.f5695.line16.line15` | IF | algebraic identity (a − min(a, b), floored, = a − b, floored) | 4.7.4 (operand order identical on both routes) | yes | candidate: pattern rule "floor-minus-min": `subtract_floor0{from: A, take: L}` with L an ungated `smaller_of` of A and B, B substituted for L |
| 61 | `boundary.eic.eic.self_employed` | prose | other (boundary at count 0; non-negativity) | 4.7.3, 4.7.2 | none | prose; fixture with no Schedule C |
| 62 | `boundary.person.person.files_se` | prose | other | 4.7.3 | **stale**: killed by fixtures | remove the entry |
| 63 | `boundary.sc.sc.ho_over` | prose | algebraic identity (both branches equal at 300 sq ft) | 4.7.3, 4.7.7 arithmetic | none | fixture at 300; rule needs the symbolic-boundary primitive |
| 64 | `boundary.se.positive` | prose | algebraic identity (rate × $0) | 4.7.3, 4.7.7 arithmetic | none | fixture at line 3 = $0; or the symbolic-boundary primitive |
| 65 | `operand.eic.eic.wsb_4b.earned_income` | prose | zero-behind-gates | 4.7.4, 4.7.1 | none; the prose does not address line 4's combat-pay gate, which is the difference between `earned_income` and line 3 when it fires | candidate for a gated-zero-summand rule once the gate is carried on the route; second reader first |
| 66 | `operand.eic.eic.wsb_6.zero` | prose | zero-behind-gates | 4.7.7 copy, 4.7.1 | none; `aliasEquivalence` did not accept it, so the two chains differ in gates and the prose does not say why that is harmless | as 65 |
| 67 | `operand.person.person.sep_s1.sc_total` | prose | shared-gate (copy adding a gate; the gate carried by the only reader's other operand) | 4.7.1, 4.7.4, 4.7.6 | none | candidate: `sharedGateEquivalence` extended to the reader's other operands beyond `sum` |
| 68 | `operand.person.person.simple_catchup.simple_regular` | prose | algebraic identity (floor-minus-min) | 4.7.4 | none | candidate: the floor-minus-min pattern rule (60) |
| 69 | `operand.s179.s179.line13.line12` | prose | algebraic identity (floor-minus-min, A a sum line) | 4.7.4 | none | candidate: the floor-minus-min pattern rule, if "lines 9 + 10" is one line |
| 70 | `operand.s8812.s8812.eiw_3.zero` | prose | zero-behind-gates | 4.7.7 copy, 4.7.1 | none; gate not addressed | as 65 |
| 71 | `operand.sc.sc.ho_both.zero` | prose | status-scoped (the line is a refusal wherever reached) | 4.7.1 | **stale**: killed by fixtures | remove the entry |
| 72 | `operand.sc.sc.ho_limited.ho_line4` | prose | algebraic identity (min with a bound) | 4.7.3, 4.7.4 | **stale**: killed by fixtures | remove the entry |
| 73 | `operand.scveh.scveh.d5.l5` | prose | status-scoped (only a 2019 vehicle reaches the line; `auto_limit` rows equal; GDS rates ordered) | 4.7.3, 4.7.4, `keyed_lookup` | none; depends on table data that changes by year | a `holds` on the table rows at least; the reach scope needs a new primitive |
| 74 | `operand.scveh.scveh.d6.l6` | prose | status-scoped | as 73 | none | as 73 |
| 75 | `operand.scveh.scveh.l5.k5` | prose | status-scoped | as 73 | none | as 73 |
| 76 | `operand.scveh.scveh.l6.k6` | prose | status-scoped | as 73 | none | as 73 |
| 77 | `operand.scveh.scveh.line17.line16` | prose | algebraic identity (floor-minus-min, min operands in the other order) | 4.7.4 (the min's operand order differs from the subtraction's; unknowns compare by kind) | none | candidate: the floor-minus-min pattern rule (60) |
| 78 | `operand.f8889.f8889.family_year.family_under55` | prose | status-scoped | 4.7.3 | **stale**: killed by fixtures | remove the entry |
| 79 | `operand.f8889.f8889.self_year.self_amount` | prose | status-scoped | 4.7.3, 4.7.6 | **stale**: killed by fixtures | remove the entry |
| 80 | `operand.qdcg.qdcg.line8.line7` | prose | algebraic identity (min nesting with line 5 ≤ line 1) | 4.7.4 | none | new primitive: lattice reasoning with an order premise |
| 81 | `operand.qdcg.qdcg.line12.line11` | prose | copy-chain identity | 4.7.7 copy, 4.7.1, 4.7.6 | none, but **superseded**: `aliasEquivalence` accepts it on every run | already mechanical; the prose entry can go |
| 82 | `operand.sd.sd.line5.zero` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 83 | `operand.sd.sd.line6.zero` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 84 | `operand.sd.sd.line11.zero` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 85 | `operand.sd.sd.line12.zero` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 86 | `operand.sd.sd.line14.zero` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 87 | `operand.sd.sd.line7.line4` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 88 | `operand.sd.sd.line7.line5` | prose | copy-chain identity | as 81 | superseded | as 81 |
| 89 | `operand.sd.sd.line7.line6` | prose | copy-chain identity | as 81 | superseded | as 81 |

## Summary

**Counts per shape** (primary shape; 89 entries):

| Shape | Entries | Of which stale | Of which superseded |
| --- | --- | --- | --- |
| skip-gated | 31 (18–35, 39–51) | 1 (34) | 0 |
| algebraic identity | 16 (14–17, 36, 37, 52, 57, 60, 63, 64, 68, 69, 72, 77, 80) | 1 (72) | 0 |
| copy-chain identity | 9 (81–89) | 0 | 9 |
| first-read-carries | 8 (2–5, 13, 38, 56, 58) | 0 | 0 |
| status-scoped | 7 (71, 73–76, 78, 79) | 3 (71, 78, 79) | 0 |
| other | 7 (6–8, 10, 59, 61, 62) | 1 (62) | 0 |
| zero-behind-gates | 6 (1, 9, 53, 65, 66, 70) | 1 (9) | 0 |
| shared-gate | 3 (54, 55, 67) | 0 | 0 |
| filter-redundant | 2 (11, 12) | 1 (12) | 0 |

**`holds` against prose** (60 `EQUIVALENT_IF` entries): yes 22 (13, 38, 39–50, 52–57, 59, 60);
partly 38 (1–12, 14–37, 51, 58). The 29 prose entries check nothing. After removing the 8 stale
and 9 superseded entries: 57 live with `holds` (22 yes, 35 partly) and 15 live prose-only. The
plan's done criterion (at most 20 prose-only) is met on the live count already; the part that is
not met is that 35 of the 57 `holds` predicates check less than their prose claims.

**Candidates for mechanization**, with the rule each needs (primitives already in `mutate.ts`
unless stated):

| Rule | Entries | What it needs |
| --- | --- | --- |
| Generic `skipGated` discovery: for every operand survivor, find the sole reader, its gate, and the wrapped operand; no per-mutant key | 39–50 | nothing new; run the existing helper over all survivors |
| `skipGated` over a reader chain: every transitive reader up to a result line gated by the same flag | 18–33 | a reader-chain walk with `gateImplies` at each step |
| `skipGated` plus zero absorption through `multiply_rate` and `subtract_floor0` | 51, 53 | a "zero in, zero out" table for the atoms, keyed on `zeroBehindGates` |
| Generic `firstReadCarries` discovery: for every remove-refusal survivor, search first-read chains (first operand, first conjunct, any sum operand) to a carrier of the same entry | 13, 38, 56 | a bounded search over `operandRefs` with the existing `reads` relation |
| `sharedGateEquivalence` through a nested sum and across the reader's other operands | 54, 55, 1, 67 | `normalizeChain` applied to each operand of a sum operand; gate carried by an earlier operand's chain |
| Floor-minus-min pattern: `subtract_floor0{from: A, take: L}`, L an ungated `smaller_of` of A and B, B substituted for L | 60, 57, 68, 69, 77 | a structural matcher only; 57 is the special case B = ungated $0 |
| Gated-zero summand: a sum operand that is $0 behind gate G, when G is carried on every route to the reader | 65, 66, 70 | the same carrier search as first-read-carries; the second reader must first say whether the gate is in fact carried |

**Needs a new primitive** (not reachable with structural matching): path dominance for 2–5; the
lookup plateau for 6–8; symbolic evaluation at a boundary for 14–17, 36, 37, 63, 64 (each is
also killable by one fixture at the boundary); lattice reasoning with non-negativity or an order
premise for 52, 80; branch-scoped evaluation for 35; gate-list rewriting for 58; table-row
equality plus reach scope for 73–76.

**Inherently prose**: 10, 11, 59, 61 (and the stale 12, 62). Under the plan these are killed by a
fixture or kept with a named reviewer, not improved as arguments.

**Entries whose `holds` is weaker than their prose — the second reader's starting list**, in the
order the gap matters:

1. 18–33 (`s1aPartGate`, 16 entries): the reader-chain premise, the whole of the argument, is unchecked.
2. 2–5 (`agiFirst`): the carrier may sit on a `choose` branch the route never takes; entry identity is by `when` only.
3. 6–8 (`thresholdAtPlateau`): nothing about the worksheet lines is checked, only the table.
4. 58 (`retirement.amount_a`): the last-conjunct read is a text match; one case is unstated.
5. 1, 35, 51, 10, 11, 14–17, 36, 37: one or two named premises each.
6. The 15 live prose-only entries, 65, 66 and 70 first (their gate is not addressed), then 73–76 (year-dependent table data), 61, 63, 64, 67, 68, 69, 77, 80.

**Housekeeping for the owner** (not done here; `mutate.ts` was not touched): remove the 8 stale
entries; remove or demote the 9 superseded prose entries so that a lapse of the copy-chain rule
shows as "unexplained" rather than falling back to prose; and consider whether `EQUIVALENT`
(prose, no `holds`) should accept new entries at all, which the plan's "no new prose-only entry"
rule already implies.

## Provenance

Inspected: `engine/src/eval.ts` in full and `lean/TaxFormalization/Eval.lean` in full (every
rule and line number in spec 4.7 was read from those files this session); `engine/src/mutate.ts`
lines 1–921 (both tables and every helper); `engine/src/check.ts` lines 75–95 (the Bool-gate
rule); `engine/src/fixtures.ts` lines 52–75 (what expectations are recorded); `engine/src/compare.ts`
line 106–109 (unknowns compared by kind); `interview/README.md` lines 101–107 (the lower-bound
rule); `BUG_INVENTORY.md` BUG-0079 and BUG-0083; `reports/2025/mutation.md`. Run this session
against the current build: every `holds` predicate (59 hold, `operand.s8812.s8812.line13.clw_a5`
fails); the mutation outcome of the 8 entries absent from the report (all "fixtures"); a scan of
the canonical data for the reachability of divergences D2 and D6 (no gated parameter line, no
non-reference operand in the positions Lean restricts) and D1 (no non-Bool gate).

Inferred (unverified): the shape assigned to each entry is a reading of its prose, not a check of
its truth; the "candidate" judgments estimate what a structural rule could accept and were not
prototyped; the claim that D1, D3 and D4 are unreachable rests on the checker's type rules as
read, not on a proof; the Lean line numbers were not re-verified by compiling Lean.

## Second reading — Claude Opus 5.5 (second reader, 2026-10-27)

Integrity plan item 1.6, part two (plan revision item C5). Reviewer for every verdict below:
**Claude Opus 5.5 (second reader, 2026-10-27)**. The first reading above classified the arguments and
said what their `holds` predicates check; this reading asks whether each argument is *true*: is the
mutant equivalent on every reachable input, where reachable includes partial answers (the question
bank says "Unknown may be null; do not guess", and the interview stops at the first refusal).

### Method

- **Differential search.** Each of the 72 entries that were live at the start of this reading (56
  `EQUIVALENT_IF`, 15 prose, and `filter.person.person.hsa_step1`, which turned out dead) was applied to
  the current data and evaluated, with every line a target, against the base data on an input bank:
  the 1,099 fixture cases, 1,500 generated returns (`engine/src/generate.ts`, seed 7) and, for each
  generated return, a partial variant with each scalar answer withheld with probability 0.15. Every
  line whose value differs on both sides (refusals compared whole, unknowns as one token, spec 4.7)
  was recorded with a witness, split into printed lines and `(helper)` lines.
- **Reading.** Each argument was then read against the YAML and the evaluator (`engine/src/eval.ts`),
  case by case on the incomplete values (spec 4.7.1 to 4.7.4), whether or not the search found a
  difference; a $1 parameter window or an equality boundary is not hit by random returns, so those
  verdicts rest on the reading.
- **Observation standard.** An argument holds when no printed line (any line not printed `(helper)`)
  can change; a change in a helper's own value is allowed and is said so. "Read only by X" bounds only
  values read through X: when the mutated line is itself printed, its own value is observed (spec 4.7.7).
- **Counterexamples.** A witness was reduced to a realistic case (an existing fixture's inputs with
  one or two answers changed or left unanswered in interview order), the side the archived IRS text
  supports was decided from the quoted sentence, and when the project's side is right a fixture case
  was added (below). When the deciding difference is only an unknown against a known value (fixtures
  never assert an unknown, and an asserted key counts as evidence in `reports/2025/evidence.md`), or
  when the reading is doubtful, the case is listed as a proposed finding instead.

### Verdicts

**72 entries: 59 hold, 12 fail with a counterexample, 1 dead, 0 undecided.** Of the 12 failures, 9 are
fixture gaps now closed by 8 new fixture cases; 3 are proposed findings and remain survivors, listed as
"not yet explained" in `reports/2025/mutation.md`.

Row numbers are those of the 89-row table above. *Disposition* says how the mutant is now accounted
for: a structural rule (applied to every survivor, below), a keyed `holds` predicate, a killing fixture,
or an open finding.

| # | Mutant | Was | Verdict | Reasoning or counterexample | Disposition |
| --- | --- | --- | --- | --- | --- |
| 1 | `operand.eic.eic.step5_line4.zero` | IF | **fails** | The mutated line is printed (Step 5, line 4). Other-income screen Yes, combat pay No: base $0, mutant the Medicaid-waiver refusal of line 2. Full input. | killed: `stage9.eic.refuse.other_income` |
| 2 | `refusal.eic.eic.step1_resident.0` | IF | **fails** | The carrier (Form 1040 line 8's other-income entry) is not on every path: with the Schedule 1 screen unanswered, line 8's first gate is unknown, line 11b is unknown, and `eic.eligible` (`[unknown, …, refusal]`) refuses only through this entry. Base: line 27a refuses (Step 1, question 4); mutant: line 27a $0, line 27c unchecked. Interview-order partial input. | killed: `stage9.eic.refuse.other_income.schedule1_unanswered` |
| 3 | `refusal.eic.eic.step5_line2.0` | IF | **fails** | Printed Step 5 line 2 is decided by its own entry: other-income screen Yes, base refusal (Medicaid waiver), mutant $0. Full input. Also differs on line 27a in partial inputs. | killed: `stage9.eic.refuse.other_income` |
| 4 | `refusal.eic.eic.step2_other.0` | IF | **fails** | Removing the first entry lets the second (`scope.other_line16`) decide while the Schedule 1 screen is unanswered (BUG-0083 ordering): on the inputs of `stage16.cleanup.refuse.f1040_line16`, the single filer's separated-spouses box goes from false to an EIC Step 2 refusal, and line 34's refusal record changes. | killed: `stage9.eic.refuse.f1040_line16.separated_spouses` |
| 5 | `refusal.eic.eic.step5_line1.0` | IF | **fails** | Printed Step 5 line 1 is decided by its own entry: Schedule 1 screen Yes, base refusal (clergy), mutant $4,000 (line 1z). Full input. | killed: `stage9.eic.refuse.clergy_schedule1.step5` |
| 6–8 | `param.eic.ws_threshold*.$1` | IF | holds | Line 3 in [T, T + $1): base line 5 is the plateau maximum and line 6 is min(maximum, line 2) = line 2; mutant leaves line 5 blank and line 6 = line 2. All operands known in the window. Only the helpers `eic.line5_blank` and `eic.show5` (whether line 5 is shown) differ; probed at AGI $10,620. | IF; `holds` now also checks the blank test, the after-line-4 binding and the smaller-of |
| 10 | `boundary.eic.eic.wsb_4b_positive` | IF | holds | At line 4b = $0 both routes make the line-5 stop false when the status is known. Prose overstated: with the status unanswered the stop is false in the base (`[unknown, …, false]`) and unknown in the mutant, but line 27c's first disjunct is then unknown too, so no printed line changes. | IF, unchanged |
| 11 | `filter.person.person.hsa_step1` | IF | dead | The mutant is killed by the current fixtures; the entry was never consulted. | removed |
| 13 | `refusal.ssb.ssb.line6.0` | IF | **fails** | Line 7 is unaffected, but printed worksheet line 6 is decided by its own entry: Schedule 1 screen Yes, base refusal, mutant $0. Full input. | killed: `stage10.ss.refuse.schedule1` |
| 14–17 | `boundary.s1a.s1a.line{10,18,27,33}_over` | IF | holds | At A = B the excess, the reduction and the subtraction are zero; the test is read only by its chooser. | IF; `holds` now also checks the sole reader, the guard-to-branch binding, a known rate and an ungated chain |
| 18–33 | `operand.s1a.s1a.*` (16) | IF | holds | Every printed reader of the mutated helper is reached only through choices whose guards imply the part's flag, where the gated line equals its figure. The search found helper-only differences. | structural rule *guarded figure* (keyed entries removed) |
| 35 | `operand.s1a.s1a.line4c_one.line4b` | IF | holds | As 18–33 (line 4c takes `line4c_one` only under Part II). | structural rule *guarded figure* |
| 36–37 | `boundary.sli.sli.over`, `operand.sli.sli.line9.line8` | IF | holds | At line 4 ≤ line 5 the prorated amount is $0 (ratio clamped at 0; the divisor is a positive parameter for every status), equal to the skip's zero; incomplete operands propagate identically. | IF; `holds` now also checks the sole reader, the binding, the divisor and an ungated chain |
| 38 | `refusal.dependent.dependent.qualifying_relative.2` | IF | **fails** | The qualifying-child test refuses first only when its earlier gates are answered. With the tie-breaker question unanswered (interview order), the qualifying-child test is unknown and only this entry refuses: base `claimed` and line 19 refuse (Married person rules), mutant unknown. | killed: `stage8.refuse.dependent.married.other_claimant_unanswered` |
| 39–50 | `operand.sdtw.sdtw.raw*` (12) | IF | holds | Skip-gated: the helper is read only where its gate holds, and there the operands are equal. | structural rule *guarded figure* (keyed entries removed) |
| 51 | `operand.sdtw.sdtw.line45.line43` | IF | holds | 28% of $0 is $0; incomplete values pass through the rate. | IF; `holds` now also checks the known rate and ungated lines |
| 52 | `operand.sdtw.sdtw.line17.line16` | IF | holds | As argued (line 14 ≤ line 1). | IF, unchanged |
| 53 | `operand.f8959.f8959.line18.line17` | IF | holds | As argued. | IF, unchanged |
| 54–55 | `operand.f8960.f8960.line8.line5d`, `…line9d.line9c` | IF | holds | As argued. | IF, unchanged |
| 56 | `refusal.f4952.f4952.required.2` | IF | **fails** | With the alternative-allocation question unanswered, the base is unknown (its last gate). The mutant evaluates the expression: the election copy is unknown on the identical gate, but the `any`-test goes on, so line 1 decides it true or refuses ahead of the unknown (spec 4.7.2). Witnesses differ only as unknown against a known value or refusal, or as one refusal record against another. | **open finding P2**; entry removed |
| 57 | `operand.f2441.f2441.line25.line24` | IF | holds | Floor-minus-min with B the ungated zero. | structural rule *floor-minus-min* |
| 58 | `refusal.retirement.retirement.amount_a.1` | IF | **fails** | The case the first reading flagged: a Roth IRA with the 1099-R code unanswered. Base: the bad-code gate is unknown, so amount A and Form 1040 line 4a are unknown. Mutant: the annuity-rollover gate is false, and `show_a`'s `any`-test remembers the unknown rollover disjunct and is decided true by `roth`, so line 4a is box 1. Only an unknown distinguishes the two. | **open finding P1**; entry removed |
| 59 | `operand.person.person.dc_earned.eic_se` | IF | holds | As argued (no difference on the bank; each clause re-read). | IF, unchanged |
| 60 | `operand.f5695.f5695.line16.line15` | IF | holds | Floor-minus-min. | structural rule *floor-minus-min* |
| 61 | `boundary.eic.eic.self_employed` | prose | **fails** | The prose missed the Worksheet B line 5 stop. With no Schedule C, earned income not under the limit and AGI under it, the mutant treats the filer as self-employed and checks line 27c. Full input (generated return 828; fixture uses wages $20,000 and student loan interest $2,500). | killed: `stage9.eic.no_schedule_c.earned_over_limit` |
| 63 | `boundary.sc.sc.ho_over` | prose | holds | At the cap, rate × square feet = rate × cap; the test is read only by line 4. | new keyed `holds` (`boundaryAgrees`) |
| 64 | `boundary.se.positive` | prose | holds | At line 3 = $0 both branches are $0; the test is read only by line 4a. | new keyed `holds` (`boundaryAgrees`) |
| 65 | `operand.eic.eic.wsb_4b.earned_income` | prose | **fails** | "Line 4 is zero, refused otherwise": when it is refused the two operands differ. A self-employed filer with combat pay: base Worksheet B line 4b, Worksheet A line 1 and Form 1040 line 27a refuse; mutant $12,081.58 and a $538 credit. Full input. | killed: `stage14.eic.wsb_combat_pay` |
| 66 | `operand.eic.eic.wsb_6.zero` | prose | holds | Line 4b (read first) reaches Step 5 line 4 through ungated sums, so when line 4 refuses or is unknown, line 4b already is. | structural rule *gated zero carried earlier* |
| 67 | `operand.person.person.sep_s1.sc_total` | prose | **fails** | Step 2 does not "refuse exactly when" Step 1's replacement does: printed SEP Step 1 is $100,000 in the base and a refusal in the mutant (Schedule C, SE screen Yes). For people without a Schedule C, Steps 1–21 go from $0 to a refusal or unknown. Which side is right is a reading question. | **open finding P3**; entry removed |
| 68 | `operand.person.person.simple_catchup.simple_regular` | prose | holds | Floor-minus-min. | structural rule *floor-minus-min* |
| 69 | `operand.s179.s179.line13.line12` | prose | holds | Floor-minus-min (A is the helper for lines 9 + 10). | structural rule *floor-minus-min* |
| 70 | `operand.s8812.s8812.eiw_3.zero` | prose | holds | Line 3's first operand (the line 1a + 1b + 2b sum) reaches line 1b through an ungated sum. | structural rule *gated zero carried earlier* |
| 73–76 | `operand.scveh.scveh.{d5.l5,d6.l6,l5.k5,l6.k6}` | prose | holds | Only a 2019 vehicle's lines reach a printed line (through `macrs_pass`'s 2019 branch). For it the year 4–6 limits are $5,760 and every 5-year GDS column's rates do not increase over years 4–6. Helper-only differences for other vehicles. | new keyed `holds` (`vehicle2019`: path dominance, table rows, rates, structure) |
| 77 | `operand.scveh.scveh.line17.line16` | prose | holds | Floor-minus-min (min operands in the other order). | structural rule *floor-minus-min* |
| 80 | `operand.qdcg.qdcg.line8.line7` | prose | holds | Line 5 ≤ line 1 (line 5 is line 1 less a non-negative line 4, floored; line 1 is non-negative). | new keyed `holds` (`minNesting`) |

**What the failures have in common.** Eight of the twelve rest on "read only by X" (or "refuses
first") while the mutated line is itself printed, or while the carrier sits behind an earlier gate
that can be unknown. The first-read-carries shape is sound only when every gate on the carrier's path is
answered. Spec 4.7.1 (an unknown gate ends the list, BUG-0083) and 4.7.2 (a later deciding conjunct, or a
refusal, outranks an unknown) are exactly the rules these arguments skipped.

### Fixture cases added

Each kills the mutants named, is predicted from the quoted source sentence in its `evidence_note`, and
asserts only known values and refusals.

| Case | File | Kills |
| --- | --- | --- |
| `stage9.eic.no_schedule_c.earned_over_limit` | `fixtures/2025/stage9.json` | `boundary.eic.eic.self_employed` |
| `stage14.eic.wsb_combat_pay` | `fixtures/2025/stage14.json` | `operand.eic.eic.wsb_4b.earned_income` |
| `stage9.eic.refuse.other_income` | `fixtures/2025/stage9.json` | `refusal.eic.eic.step5_line2.0`, `operand.eic.eic.step5_line4.zero` |
| `stage9.eic.refuse.other_income.schedule1_unanswered` | `fixtures/2025/stage9.json` | `refusal.eic.eic.step1_resident.0` |
| `stage9.eic.refuse.clergy_schedule1.step5` | `fixtures/2025/stage9.json` | `refusal.eic.eic.step5_line1.0` |
| `stage9.eic.refuse.f1040_line16.separated_spouses` | `fixtures/2025/stage9.json` | `refusal.eic.eic.step2_other.0` |
| `stage10.ss.refuse.schedule1` | `fixtures/2025/stage10.json` | `refusal.ssb.ssb.line6.0` |
| `stage8.refuse.dependent.married.other_claimant_unanswered` | `fixtures/2025/stage8.json` | `refusal.dependent.dependent.qualifying_relative.2` |

### Mechanization

Three structural rules in `engine/src/mutate.ts` are now applied to every survivor, after copy-chain and
shared-gate. Each is checked against the current data on every run, and each first requires that
neither operand depends on the mutated line. Without that guard, a probe over all 2,286 mutants found
the guarded-figure rule accepting three scveh mutants the fixtures kill, because the replacement reads
the mutated line.

- **Floor-minus-min**: `subtract_floor0{from A, take M}` with M an ungated `smaller_of` of A and B, in
  either order and either direction of replacement. Covers 57, 60, 68, 69, 77.
- **Guarded figure** (path dominance): the replaced operand is a two-way choice "its figure when F", the
  replacement is that figure, and every reader path from the mutated helper to a printed line, a refusal
  gate or a display condition passes choices whose guards together imply F. The rule reasons about
  conjuncts, `eq` against `ne`, and flags defined as all-tests. Covers 18–33, 35 and 39–50; it supersedes
  the keyed `s1aPartGate`, `s1aOneEmployer` and `skipGated` entries.
- **Gated zero carried earlier**: an ungated zero operand replaced by the same zero behind gates, when an
  earlier operand reaches the gated zero through ungated arithmetic. Covers 66 and 70.

Soundness probe: the structural rules accept 93 of the 2,286 mutants, every one a survivor of the
fixtures. The new keyed predicates are `boundaryAgrees` (63, 64), `minNesting` (80) and `vehicle2019`
(73–76; it uses the same path-dominance walk). The weak predicates of 6–8, 14–17, 36–37 and 51 were
strengthened as listed in the table.

**Prose-only entries: 15 before, 0 after.** The `EQUIVALENT` prose table is gone. The run's map of
reasons is filled only by the structural rules and by `EQUIVALENT_IF` entries whose `holds` passes, so
there is no place left to add a prose-only argument. Equivalent survivors are now 116: 93 by structural
rules (46 copy-chain, 3 shared-gate, 8 unread-parameter, 5 floor-minus-min, 29 guarded-figure, 2
carried-zero) and 23 by keyed `holds`. The plan's done-when (at most 20 prose-only, each with its
reviewer; no new prose-only entry) is met with 0.

### Proposed findings (not fixed here)

- **P1 — `refusal.retirement.retirement.amount_a.1` survives and is not equivalent.** Only an unknown
  (Form 1040 line 4a before the 1099-R code is answered) tells the routes apart. The project's unknown
  is right under spec 4.7.1, since an answer of code "other" would refuse. Options for the owner: an
  expectation form for unknowns that the evidence report does not count, or a property over partial
  answers.
- **P2 — `refusal.f4952.f4952.required.2` survives and is not equivalent.** Same situation, with the
  Form 4952 alternative-allocation question unanswered. The only witnesses with a known base differ by
  which of two true refusals is shown.
- **P3 — `operand.person.person.sep_s1.sc_total`: possible project defect.** The SEP Deduction Worksheet's
  Step 1 (`person.sep_s1`) copies the Schedule C total even when the Schedule SE screen is Yes or
  unanswered. Pub. 560 (2025), Deduction Worksheet for Self-Employed, Step 1 reads: "Enter your net profit
  from Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34;* or Schedule K-1 (Form 1065),*
  box 14, code A." The screen covers exactly such non-Schedule-C self-employment income, so the printed
  Step 1 may be understated where the mutant refuses. The worksheet's later steps already refuse through
  Step 2, so no deduction changes. Needs the owner's reading of whose earned income a SEP covers before
  a fixture is chosen.
- **P4 — the mutation step cannot fail check-all.** `runMutation` returns 1 when a survivor is
  unexplained, but `engine/src/main.ts` calls `await runMutation()` and discards the status. P1–P3 are
  listed under "Surviving — not yet explained" and the step still passes. Proposed:
  `process.exit(await runMutation())`, once P1–P3 are dispositioned.

### Provenance (second reading)

Inspected: `engine/src/mutate.ts` in full (before and after this change); `engine/src/eval.ts` lines
40–135 and 380–475 (targets, sum, subtract, min/max, multiply, prorate, round); `engine/src/check.ts`
lines 160–300 (the NonNegDollars proof); `engine/src/fixtures.ts` lines 20–117 and 230–262;
`engine/src/fixture-inputs.ts`; `engine/src/main.ts` lines 120–135; spec 4.7; the canonical expression
of every line named in the table (printed by a script from `canonical/2025`); `interview/questions-2025.yaml`
(order of the scope and dependent questions) and `interview/README.md` line 51; the archived sentences
quoted in the fixture notes (`sources/2025/i1040gi-html.txt`, `f1040.txt`, `p560.txt`). Run against the
current build: the differential search described above (72 mutants × 4,099 inputs); the killing check of
the 12 failing mutants against all fixtures after the 8 cases were added (9 killed, 3 surviving, every
baseline expectation unchanged); the structural-rule soundness probe (93 accepted, none killed); the
classification of the 128 former survivors under the new tables (116 equivalent, 12 not: the 9 now killed
and P1–P3); a probe of entry 6 in its $1 window (no_child.4000 with wages $10,000 and interest $620, AGI
exactly $10,620: line 6 and line 27a $649 on both routes, only `eic.line5_blank` and `eic.show5` differ);
`npm run mutate` (2,286 mutants: 235 killed by the checker, 1,932 by fixtures, 119 surviving, of which 116
equivalent and 3, P1–P3, not yet explained; adjusted score 99.9%); `npm run check-all` (green;
fixtures 1,107/1,107; refusal reach 262 refusal fixtures).

Inferred (unverified): the holds verdicts for 7, 8, 14–17, 36–37, 63 and 64 rest on reading the boundary
or $1 window, which the random bank does not hit (6 was probed once in its window); the bank is a sample, so "no printed difference found" for
the other holds verdicts is evidence alongside the reading, not proof; the path-dominance rule is argued
from spec 4.7.3 and tested by the probe and the bank, not proved; the interview-order claims for the two
partial cases rest on the bank's `order` values and README line 51 ("asked in bank order, then by key"), not
on driving the interview tool.
