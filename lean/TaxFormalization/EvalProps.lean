/-
Termination and determinism of the reference evaluator (spec section 6.3).

`eval` is a total function: Lean accepts it only because every recursive call
spends one unit of the step budget, so the recursion is structural on the
budget. It runs in a pure state monad, so its result is a function of its
arguments and the starting state. The theorems below state both facts; their
force comes from the definition being accepted as total, not from the proofs.
-/

import TaxFormalization.Eval

namespace TaxFormalization

/-- Evaluation terminates: for every context, budget, frame, instruction and
starting state there is a result (value and final state). -/
theorem eval_terminates (ctx : Ctx) (n : Nat) (frame : Frame) (cmd : Cmd) (st : EvalState) :
    ∃ r, (eval ctx n frame cmd).run st = r :=
  ⟨_, rfl⟩

/-- Evaluation is deterministic: two runs on the same arguments and starting
state give the same value and the same final state. -/
theorem eval_deterministic (ctx : Ctx) (n : Nat) (frame : Frame) (cmd : Cmd) (st : EvalState)
    {r₁ r₂ : Id (Lean.Json × EvalState)}
    (h₁ : (eval ctx n frame cmd).run st = r₁) (h₂ : (eval ctx n frame cmd).run st = r₂) :
    r₁ = r₂ := by
  rw [← h₁, ← h₂]

/-- An exhausted budget gives the budget-exhausted value and leaves the state unchanged. -/
theorem eval_zero (ctx : Ctx) (frame : Frame) (cmd : Cmd) (st : EvalState) :
    (eval ctx 0 frame cmd).run st = (budgetExhausted, st) :=
  rfl

end TaxFormalization
