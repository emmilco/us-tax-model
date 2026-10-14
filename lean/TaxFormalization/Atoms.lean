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

end TaxFormalization
