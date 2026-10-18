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

/-! ## `round`, rules `down` and `up` -/

/-- Rounding down gives a multiple of the unit. -/
theorem roundDownToUnit_multiple {x unit : Int} : unit ∣ roundDownToUnit x unit := by
  unfold roundDownToUnit; exact Int.dvd_mul_left _ _

/-- Rounding down gives the largest multiple of the unit at or below the value:
it is at most the value, and the value is less than it plus one unit. -/
theorem roundDownToUnit_rule {x unit : Int} (hu : 0 < unit) :
    roundDownToUnit x unit ≤ x ∧ x < roundDownToUnit x unit + unit := by
  unfold roundDownToUnit
  have h := Int.mul_ediv_add_emod x unit
  have h0 : 0 ≤ x % unit := Int.emod_nonneg _ (by omega)
  have h1 : x % unit < unit := Int.emod_lt_of_pos _ hu
  rw [Int.mul_comm (x / unit) unit]
  constructor <;> omega

/-- Rounding down moves a value by less than one unit, and never up. -/
theorem roundDownToUnit_moves_lt {x unit : Int} (hu : 0 < unit) :
    0 ≤ x - roundDownToUnit x unit ∧ x - roundDownToUnit x unit < unit := by
  obtain ⟨h1, h2⟩ := roundDownToUnit_rule (x := x) hu
  constructor <;> omega

/-- Rounding down is idempotent. -/
theorem roundDownToUnit_idem {x unit : Int} (hu : 0 < unit) :
    roundDownToUnit (roundDownToUnit x unit) unit = roundDownToUnit x unit := by
  unfold roundDownToUnit
  rw [Int.mul_ediv_cancel _ (by omega)]

/-- Rounding up gives a multiple of the unit. -/
theorem roundUpToUnit_multiple {x unit : Int} : unit ∣ roundUpToUnit x unit := by
  unfold roundUpToUnit; exact Int.dvd_mul_left _ _

/-- Rounding up gives the smallest multiple of the unit at or above the value:
it is at least the value, and less than the value plus one unit. -/
theorem roundUpToUnit_rule {x unit : Int} (hu : 0 < unit) :
    x ≤ roundUpToUnit x unit ∧ roundUpToUnit x unit < x + unit := by
  unfold roundUpToUnit
  have h := Int.mul_ediv_add_emod (x + unit - 1) unit
  have h0 : 0 ≤ (x + unit - 1) % unit := Int.emod_nonneg _ (by omega)
  have h1 : (x + unit - 1) % unit < unit := Int.emod_lt_of_pos _ hu
  rw [Int.mul_comm ((x + unit - 1) / unit) unit]
  constructor <;> omega

/-- Rounding up moves a value by less than one unit, and never down. -/
theorem roundUpToUnit_moves_lt {x unit : Int} (hu : 0 < unit) :
    0 ≤ roundUpToUnit x unit - x ∧ roundUpToUnit x unit - x < unit := by
  obtain ⟨h1, h2⟩ := roundUpToUnit_rule (x := x) hu
  constructor <;> omega

/-- Rounding up is idempotent. -/
theorem roundUpToUnit_idem {x unit : Int} (hu : 0 < unit) :
    roundUpToUnit (roundUpToUnit x unit) unit = roundUpToUnit x unit := by
  unfold roundUpToUnit
  have hu0 : unit ≠ 0 := by omega
  rw [show (x + unit - 1) / unit * unit + unit - 1 = (unit - 1) + unit * ((x + unit - 1) / unit) by
    rw [Int.mul_comm unit]; omega]
  rw [Int.add_mul_ediv_left _ _ hu0]
  rw [Int.ediv_eq_zero_of_lt (by omega) (by omega)]
  simp

/-- The `round` atom applies the rule it names. -/
theorem roundByRule_half_up {x unit : Int} :
    roundByRule "half_up" x unit = some (roundHalfUpToUnit x unit) := by
  simp [roundByRule]

theorem roundByRule_up {x unit : Int} :
    roundByRule "up" x unit = some (roundUpToUnit x unit) := by
  simp [roundByRule]

theorem roundByRule_down {x unit : Int} :
    roundByRule "down" x unit = some (roundDownToUnit x unit) := by
  simp [roundByRule]

/-! ## Monotonicity of the remaining argument positions (spec 6.3 table) -/

/-- `sum` is monotone in each operand: raising every operand (each operand's value
read through `f`, then through `g` with `f ≤ g` pointwise) does not lower the sum. -/
theorem sumList_mono {α : Type} (xs : List α) (f g : α → Int) (h : ∀ x, f x ≤ g x) :
    sumList (xs.map f) ≤ sumList (xs.map g) := by
  induction xs with
  | nil => exact Int.le_refl _
  | cons x xs ih => have := h x; simp only [List.map, sumList]; omega

/-- `subtract` is monotone in what it subtracts from. -/
theorem subtract_mono_from {a a' b : Int} (h : a ≤ a') : subtract a b ≤ subtract a' b := by
  unfold subtract; omega

/-- `subtract` is antitone in what it takes away. -/
theorem subtract_antitone_take {a b b' : Int} (h : b ≤ b') : subtract a b' ≤ subtract a b := by
  unfold subtract; omega

/-- `smaller_of` is monotone in its second operand. -/
theorem smallerOf_mono_right {a b b' : Int} (h : b ≤ b') : smallerOf a b ≤ smallerOf a b' := by
  unfold smallerOf; omega

/-- `larger_of` is monotone in its second operand. -/
theorem largerOf_mono_right {a b b' : Int} (h : b ≤ b') : largerOf a b ≤ largerOf a b' := by
  unfold largerOf; omega

/-- `multiply_rate` is monotone in the rate's numerator for an amount that is not negative. -/
theorem multiplyRateHalfUp_mono_rate {a num num' den : Int} (h : num ≤ num') (ha : 0 ≤ a)
    (hd : 0 < den) : multiplyRateHalfUp a num den ≤ multiplyRateHalfUp a num' den := by
  simp only [multiplyRateHalfUp]
  apply halfUpDiv_mono_num
  · exact Int.mul_le_mul_of_nonneg_left h ha
  · exact hd

/-- Each `round` rule is monotone in the value rounded. -/
theorem roundHalfUpToUnit_mono {x x' unit : Int} (h : x ≤ x') (hu : 0 < unit) :
    roundHalfUpToUnit x unit ≤ roundHalfUpToUnit x' unit := by
  unfold roundHalfUpToUnit
  apply Int.mul_le_mul_of_nonneg_right _ (by omega)
  exact Int.ediv_le_ediv (by omega) (by omega)

theorem roundUpToUnit_mono {x x' unit : Int} (h : x ≤ x') (hu : 0 < unit) :
    roundUpToUnit x unit ≤ roundUpToUnit x' unit := by
  unfold roundUpToUnit
  apply Int.mul_le_mul_of_nonneg_right _ (by omega)
  exact Int.ediv_le_ediv hu (by omega)

theorem roundDownToUnit_mono {x x' unit : Int} (h : x ≤ x') (hu : 0 < unit) :
    roundDownToUnit x unit ≤ roundDownToUnit x' unit := by
  unfold roundDownToUnit
  apply Int.mul_le_mul_of_nonneg_right _ (by omega)
  exact Int.ediv_le_ediv hu h

/-! ## `prorate` -/

theorem prorateRatio_nonneg (part whole s : Int) : 0 ≤ prorateRatio part whole s := by
  unfold prorateRatio; omega

theorem prorateRatio_le (part whole s : Int) (hs : 0 ≤ s) : prorateRatio part whole s ≤ s := by
  unfold prorateRatio; omega

theorem pow10_pos (places : Nat) : 0 < (10 : Int) ^ places := by
  exact Int.pow_pos (by decide)

/-- `prorate` of an amount that is not negative is not negative. -/
theorem prorate_nonneg {a part whole : Int} {places : Nat} (ha : 0 ≤ a) :
    0 ≤ prorate a part whole places := by
  unfold prorate
  exact multiplyRateHalfUp_nonneg ha (prorateRatio_nonneg _ _ _) (pow10_pos places)

/-- Multiplying by the whole scale gives the amount back. -/
theorem multiplyRateHalfUp_self {a s : Int} (hs : 0 < s) : multiplyRateHalfUp a s s = a := by
  unfold multiplyRateHalfUp halfUpDiv
  have h2s : 2 * s ≠ 0 := by omega
  rw [show 2 * (a * s) + s = s + 2 * s * a by rw [Int.mul_comm a s, ← Int.mul_assoc]; omega]
  rw [Int.add_mul_ediv_left s a h2s]
  rw [Int.ediv_eq_zero_of_lt (by omega) (by omega)]
  simp

/-- `prorate` never exceeds the amount (the ratio is at most 1). -/
theorem prorate_le_amount {a part whole : Int} {places : Nat} (ha : 0 ≤ a) :
    prorate a part whole places ≤ a := by
  unfold prorate
  have hs := pow10_pos places
  have hle := multiplyRateHalfUp_mono_rate (a := a) (den := (10 : Int) ^ places)
    (prorateRatio_le part whole _ (Int.le_of_lt hs)) ha hs
  rw [multiplyRateHalfUp_self hs] at hle
  exact hle

/-- `prorate` is monotone in the amount. -/
theorem prorate_mono_amount {a a' part whole : Int} {places : Nat} (h : a ≤ a') :
    prorate a part whole places ≤ prorate a' part whole places := by
  unfold prorate
  exact multiplyRateHalfUp_mono_amount h (prorateRatio_nonneg _ _ _) (pow10_pos places)

/-- `prorate` is monotone in the part, for an amount that is not negative and a positive whole. -/
theorem prorate_mono_part {a part part' whole : Int} {places : Nat} (h : part ≤ part')
    (ha : 0 ≤ a) (hw : 0 < whole) :
    prorate a part whole places ≤ prorate a part' whole places := by
  unfold prorate
  apply multiplyRateHalfUp_mono_rate _ ha (pow10_pos places)
  unfold prorateRatio
  have := multiplyRateHalfUp_mono_amount (num := (10 : Int) ^ places) h
    (Int.le_of_lt (pow10_pos places)) hw
  omega

/-! ## `multiply_count` -/

/-- An amount that is not negative, times a count, is not negative. -/
theorem multiplyCount_nonneg {a n : Int} (ha : 0 ≤ a) (hn : 0 ≤ n) : 0 ≤ multiplyCount a n := by
  unfold multiplyCount; exact Int.mul_nonneg ha hn

/-- Monotone in the amount for a count that is not negative. -/
theorem multiplyCount_mono_amount {a a' n : Int} (h : a ≤ a') (hn : 0 ≤ n) :
    multiplyCount a n ≤ multiplyCount a' n := by
  unfold multiplyCount; exact Int.mul_le_mul_of_nonneg_right h hn

/-- Monotone in the count for an amount that is not negative. -/
theorem multiplyCount_mono_count {a n n' : Int} (h : n ≤ n') (ha : 0 ≤ a) :
    multiplyCount a n ≤ multiplyCount a n' := by
  unfold multiplyCount; exact Int.mul_le_mul_of_nonneg_left h ha

/-- One more unit of the count adds the amount once: the atom is repeated addition. -/
theorem multiplyCount_succ (a n : Int) : multiplyCount a (n + 1) = multiplyCount a n + a := by
  unfold multiplyCount; rw [Int.mul_add, Int.mul_one]

/-- A count of zero gives zero. -/
theorem multiplyCount_zero (a : Int) : multiplyCount a 0 = 0 := by
  unfold multiplyCount; exact Int.mul_zero a

end TaxFormalization
