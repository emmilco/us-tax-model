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

/-- The `multiply_count` atom: an amount in cents times a whole number (for example a monthly
    amount times the number of months). Exact; no rounding. -/
def multiplyCount (a n : Int) : Int := a * n

/-- The ratio of `prorate`: part / whole on a scale of `s` units (s = 10 ^ places),
half-up, and kept between 0 and s (between 0 and 1.000). -/
def prorateRatio (part whole s : Int) : Int := max 0 (min s (multiplyRateHalfUp part s whole))

/-- The `prorate` atom: amount times (part / whole), the ratio rounded half-up to
`places` decimal places and kept between 0 and 1, the product half-up to the cent
(the Student Loan Interest Deduction Worksheet, lines 7 and 8). -/
def prorate (a part whole : Int) (places : Nat) : Int :=
  multiplyRateHalfUp a (prorateRatio part whole ((10 : Int) ^ places)) ((10 : Int) ^ places)

/-- The `keyed_lookup` atom: the entry of the first row whose key tuple equals
`keys`, or none when no row has it. Keys are normalized strings (an enum value or a
count); the build-time checker requires a table's key tuples to be distinct. -/
def keyedLookup {V : Type} (rows : List (List String × V)) (keys : List String) : Option V :=
  (rows.find? (fun r => r.1 == keys)).map Prod.snd

/-- Whether a band whose upper bound ("but not over") is `hi` holds `key` once every
earlier band has been passed over; `none` is an open upper end. -/
def bandHolds (hi : Option Int) (key : Int) : Bool :=
  match hi with
  | none => true
  | some h => decide (key ≤ h)

/-- The `rate_lookup` atom: the rate of the first band, in order, whose upper bound is
at least `key`, or none when there is none. The build-time checker requires the bands
of a table to be contiguous with increasing bounds, the first open below and the last
open above, so the first such band is the one with over < key ≤ not over. -/
def rateBand {V : Type} (bands : List (Option Int × V)) (key : Int) : Option V :=
  (bands.find? (fun b => bandHolds b.1 key)).map Prod.snd

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
