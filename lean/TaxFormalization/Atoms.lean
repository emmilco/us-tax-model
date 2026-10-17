/-
Atom semantics over the integers, mirroring the TypeScript evaluator exactly.
Money is integer cents; rates are integer pairs; the only rounding is
half-up (amb.2025.multiplication_subcent) and explicit whole-unit rounding.
-/

namespace TaxFormalization

/-- Sum of a list of amounts. -/
def sumList : List Int → Int
  | [] => 0
  | x :: xs => x + sumList xs

/-- Sum one column of a collection selected by a Boolean predicate. -/
def sumOver {α : Type} (xs : List α) (field : α → Int) (keep : α → Bool) : Int :=
  sumList ((xs.filter keep).map field)

/-- Signed subtraction. -/
def subtract (a b : Int) : Int := a - b

/-- Subtract; if zero or less, zero. -/
def subtractFloor0 (a b : Int) : Int := max 0 (a - b)

/-- Minimum of two amounts. -/
def smallerOf (a b : Int) : Int := min a b

/-- Maximum of two amounts. -/
def largerOf (a b : Int) : Int := max a b

/-- Half-up division toward +infinity: floor((2n + d) / (2d)) for d > 0.
    (Lean's integer division is floor division, so this is the intended rule.) -/
def halfUpDiv (n d : Int) : Int := (2 * n + d) / (2 * d)

/-- Amount times a rate, half-up at the cent. -/
def multiplyRateHalfUp (a num den : Int) : Int := halfUpDiv (a * num) den

/-- Round to the nearest unit, half-up (the printed whole-dollar rule with
    unit = 100). -/
def roundHalfUpToUnit (x unit : Int) : Int := ((2 * x + unit) / (2 * unit)) * unit

/-- Round up to the next multiple of the unit (the "next multiple of $1,000"
    rule of Schedule 8812, line 10); a multiple stays where it is. -/
def roundUpToUnit (x unit : Int) : Int := ((x + unit - 1) / unit) * unit

/-- Round down to a multiple of the unit. -/
def roundDownToUnit (x unit : Int) : Int := (x / unit) * unit

/-- The `round` atom: rule "half_up", "up" or "down"; none otherwise. -/
def roundByRule (rule : String) (x unit : Int) : Option Int :=
  if rule == "half_up" then some (roundHalfUpToUnit x unit)
  else if rule == "up" then some (roundUpToUnit x unit)
  else if rule == "down" then some (roundDownToUnit x unit)
  else none

end TaxFormalization
