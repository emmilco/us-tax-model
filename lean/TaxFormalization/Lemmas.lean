/-
Lemmas for the atoms used in Stage 1, over the integers
(spec section 6.3: non-negativity, monotonicity, rounding properties).
-/

import TaxFormalization.Atoms

namespace TaxFormalization

theorem sumList_nonneg (xs : List Int) (h : ∀ x ∈ xs, 0 ≤ x) : 0 ≤ sumList xs := by
  induction xs with
  | nil => decide
  | cons y ys ih =>
    have hy : 0 ≤ y := h y (by simp)
    have hys : ∀ x ∈ ys, 0 ≤ x := fun x hx => h x (by simp [hx])
    simpa [sumList] using Int.add_nonneg hy (ih hys)

theorem sumOver_nonneg {α : Type} (xs : List α) (field : α → Int) (keep : α → Bool)
    (h : ∀ x ∈ xs, 0 ≤ field x) : 0 ≤ sumOver xs field keep := by
  apply sumList_nonneg
  intro y hy
  obtain ⟨x, hx, rfl⟩ := List.mem_map.mp hy
  exact h x ((List.mem_filter.mp hx).1)

theorem sumOver_mono {α : Type} (xs : List α) (f g : α → Int) (keep : α → Bool)
    (h : ∀ x, f x ≤ g x) : sumOver xs f keep ≤ sumOver xs g keep := by
  induction xs with
  | nil => simp [sumOver, sumList]
  | cons x xs ih =>
    by_cases hk : keep x = true
    · simp [sumOver, hk, sumList] at *
      have hx := h x
      omega
    · simpa [sumOver, List.filter_cons, hk, sumList] using ih

theorem subtractFloor0_nonneg (a b : Int) : 0 ≤ subtractFloor0 a b := by
  simp only [subtractFloor0]
  omega

theorem subtractFloor0_mono_from {a a' b : Int} (h : a ≤ a') :
    subtractFloor0 a b ≤ subtractFloor0 a' b := by
  simp only [subtractFloor0]
  omega

theorem subtractFloor0_antitone_take {a b b' : Int} (h : b ≤ b') :
    subtractFloor0 a b' ≤ subtractFloor0 a b := by
  simp only [subtractFloor0]
  omega

theorem smallerOf_nonneg {a b : Int} (ha : 0 ≤ a) (hb : 0 ≤ b) : 0 ≤ smallerOf a b := by
  simp only [smallerOf]
  omega

theorem smallerOf_mono_left {a a' b : Int} (h : a ≤ a') : smallerOf a b ≤ smallerOf a' b := by
  simp only [smallerOf]
  omega

theorem largerOf_nonneg {a b : Int} (ha : 0 ≤ a) : 0 ≤ largerOf a b := by
  simp only [largerOf]
  omega

theorem largerOf_mono_left {a a' b : Int} (h : a ≤ a') : largerOf a b ≤ largerOf a' b := by
  simp only [largerOf]
  omega

theorem largerOf_ge_left (a b : Int) : a ≤ largerOf a b := by
  simp only [largerOf]
  omega

theorem halfUpDiv_mono_num {n n' d : Int} (h : n ≤ n') (hd : 0 < d) :
    halfUpDiv n d ≤ halfUpDiv n' d := by
  simp only [halfUpDiv]
  exact Int.ediv_le_ediv (show (0 : Int) < 2 * d by omega) (show 2 * n + d ≤ 2 * n' + d by omega)

theorem multiplyRateHalfUp_nonneg {a num den : Int} (ha : 0 ≤ a) (hn : 0 ≤ num) (hd : 0 < den) :
    0 ≤ multiplyRateHalfUp a num den := by
  simp only [multiplyRateHalfUp, halfUpDiv]
  apply Int.ediv_nonneg
  · exact Int.add_nonneg (Int.mul_nonneg (show (0 : Int) ≤ 2 by omega) (Int.mul_nonneg ha hn)) (by omega)
  · omega

theorem multiplyRateHalfUp_mono_amount {a a' num den : Int} (h : a ≤ a') (hn : 0 ≤ num)
    (hd : 0 < den) :
    multiplyRateHalfUp a num den ≤ multiplyRateHalfUp a' num den := by
  simp only [multiplyRateHalfUp]
  apply halfUpDiv_mono_num
  · exact Int.mul_le_mul_of_nonneg_right h hn
  · exact hd

/-- The rounding rule moves a value by at most half a unit on each side. -/
theorem roundHalfUpToUnit_half_rule {x unit : Int} (hu : 0 < unit) :
    2 * (roundHalfUpToUnit x unit - x) ≤ unit ∧ 2 * (x - roundHalfUpToUnit x unit) ≤ unit := by
  generalize hKdef : (2 * x + unit) / (2 * unit) = K
  generalize hMdef : (2 * x + unit) % (2 * unit) = M
  have hKM : 2 * unit * K + M = 2 * x + unit := by
    have := Int.mul_ediv_add_emod (2 * x + unit) (2 * unit)
    simpa [hKdef, hMdef] using this
  have hM0 : 0 ≤ M := by
    rw [← hMdef]
    exact Int.emod_nonneg _ (by omega)
  have hMLt : M < 2 * unit := by
    rw [← hMdef]
    exact Int.emod_lt_of_pos _ (by omega)
  have hround : roundHalfUpToUnit x unit = K * unit := by
    simp only [roundHalfUpToUnit]
    rw [hKdef]
  constructor
  · rw [hround, Int.mul_comm K unit]
    have e : 2 * (unit * K - x) = 2 * unit * K - 2 * x := by
      rw [Int.mul_sub, ← Int.mul_assoc]
    rw [e]
    omega
  · rw [hround, Int.mul_comm K unit]
    have e : 2 * (x - unit * K) = 2 * x - 2 * unit * K := by
      rw [Int.mul_sub, ← Int.mul_assoc]
    rw [e]
    omega

/-- The rounding rule moves a value by less than one unit. -/
theorem roundHalfUpToUnit_moves_lt {x unit : Int} (hu : 0 < unit) :
    roundHalfUpToUnit x unit - x < unit ∧ x - roundHalfUpToUnit x unit < unit := by
  obtain ⟨h1, h2⟩ := roundHalfUpToUnit_half_rule (x := x) hu
  constructor <;> omega

/-- Rounding is idempotent. -/
theorem roundHalfUpToUnit_idem {x unit : Int} (hu : 0 < unit) :
    roundHalfUpToUnit (roundHalfUpToUnit x unit) unit = roundHalfUpToUnit x unit := by
  have h2u : 2 * unit ≠ 0 := by omega
  simp only [roundHalfUpToUnit]
  rw [show 2 * ((2 * x + unit) / (2 * unit) * unit) + unit
        = unit + 2 * unit * ((2 * x + unit) / (2 * unit)) by
    rw [Int.mul_comm ((2 * x + unit) / (2 * unit)) unit]
    rw [← Int.mul_assoc]
    rw [Int.add_comm]]
  rw [Int.add_mul_ediv_left unit ((2 * x + unit) / (2 * unit)) h2u]
  rw [Int.ediv_eq_zero_of_lt (show 0 ≤ unit by omega) (show unit < 2 * unit by omega)]
  simp

end TaxFormalization
