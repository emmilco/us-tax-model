## BUG-NEW-lane-mutargs-03 — Closure: BUG-1124 is fixed

- **Closes:** BUG-1124
- **Closure:** fixed
- **Caught by:** lane mutargs (claude-opus-5-5, judgment), 2026-11-24.
- **Resolution:** fixtures/2025/f2441.json mut.f2441.attrib_gate_benefits_open_no_credit (the scout's draft, inputs unchanged): joint return, W-2 wages $40,000 and $30,000, one child aged 6, care asked, $0 of care expenses, f2441.benefits unanswered. Predicted by hand before evaluation from Form 2441 lines 30 and 31 and i2441 p. 4: line 31 $0, attrib_gate false, line 5 $30,000; the evaluator agrees. Under the mutant (attrib_gate reads line 3) the gate and line 5 are unknown, so the case kills it. The keyed argument and its ANSWERED_ONLY entry are removed from engine/src/mutate.ts (an argument for a killed mutant is stale). No form line changed.
- **Siblings checked:** python3 tools/siblings.py f2441.attrib_gate: its readers f2441.line4 and f2441.line5 (line 5 now asserted by the case); the other lines on the same i2441 heading are unaffected by a fixture.
- **Evidence:** evaluate() of the case on the canonical build and on the mutated data (operand.f2441.f2441.attrib_gate.line31.all.3.gt.0): base line31 $0, attrib_gate false, line5 $30,000; mutant attrib_gate and line5 unknown (no input supplied for f2441.benefits). test-fixtures 2746/2746.
- **Tags:** fixtures, f2441, mutation, fixed
