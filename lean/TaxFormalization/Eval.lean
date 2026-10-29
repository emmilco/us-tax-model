/-
The reference evaluator: reads the canonical JSON and evaluates the Stage 1
slice with the same semantics as the TypeScript evaluator (integer cents,
half-up multiply via the proved Atoms functions).

The evaluator is a single function over an instruction dispatch, mirroring
the TypeScript evaluator's frame handling for parameterized def instances.
It is total: every recursive call spends one unit of a step budget (fuel),
so the recursion is structural on the budget, and an exhausted budget gives
the value "unknown: step budget exhausted". It is pure: the memo and the
cycle markers are the state of a state monad, so a result is a function of
the context, the budget, the frame, the instruction and the starting state.
-/

import Lean.Data.Json
import Std.Data.HashMap
import TaxFormalization.Atoms

namespace TaxFormalization

open Lean

structure Ctx where
  forms : Std.HashMap String Json
  params : Json
  tables : Std.HashMap String Json
  inputs : Json

/-- Evaluation state: line values already computed, and lines being computed
(a line met again while being computed is a cycle). -/
structure EvalState where
  memo : Std.HashMap String Json := ∅
  inflight : Std.HashMap String Bool := ∅

abbrev EvalM := StateM EvalState

structure Frame where
  docId : String
  doc : Json
  instKey : Option String
  bind : Json
  caller : Option Frame

inductive Cmd where
  | line (lineId : String)
  | operand (op : Json)
  | test (t : Json)
  | fresh (lineId : String)
  | expr (e : Json) (op : String)

-- ---------------------------------------------------------------------------
-- helpers (non-recursive)

private def objGet (j : Json) (k : String) : Option Json := (j.getObjVal? k).toOption
private def objGetD (j : Json) (k : String) (d : Json) : Json := (objGet j k).getD d
private def numGet (j : Json) (k : String) : Option Int := (objGet j k).bind (fun v => (v.getInt?).toOption)
private def strGet (j : Json) (k : String) : Option String := (objGet j k).bind (fun v => (v.getStr?).toOption)

def unknown (reason : String) : Json := Json.mkObj [("kind", Json.str "unknown"), ("reason", Json.str reason)]
def mkMoney (n : Int) : Json := Json.mkObj [("kind", Json.str "money"), ("cents", Json.num (JsonNumber.fromInt n))]
def mkCount (n : Int) : Json := Json.mkObj [("kind", Json.str "count"), ("value", Json.num (JsonNumber.fromInt n))]
def mkBool (b : Bool) : Json := Json.mkObj [("kind", Json.str "bool"), ("value", Json.bool b)]
def mkEnum (s : String) : Json := Json.mkObj [("kind", Json.str "enum"), ("value", Json.str s)]
def mkRate (n d : Int) : Json :=
  Json.mkObj [("kind", Json.str "rate"), ("num", Json.num (JsonNumber.fromInt n)), ("den", Json.num (JsonNumber.fromInt d))]

def kindOf (v : Json) : Option String := strGet v "kind"
def isUnknown (v : Json) : Bool := kindOf v == some "unknown" || kindOf v == some "refusal"
def isMoney (v : Json) : Bool := kindOf v == some "money"
def isRefusal (v : Json) : Bool := kindOf v == some "refusal"

/-- What an atom's evaluated operands leave it before it computes: the first refusal among
them in operand order, else the first unknown, else none (every operand is known). A refusal
outranks an unknown, so a refusal is not held back behind an operand whose value cannot change
the outcome. -/
def incompleteOperand (vs : List Json) : Option Json :=
  match vs.find? isRefusal with
  | some r => some r
  | none => vs.find? (fun v => kindOf v == some "unknown")
def isBool (v : Json) : Bool := kindOf v == some "bool"
def isEnum (v : Json) : Bool := kindOf v == some "enum"
def isRate (v : Json) : Bool := kindOf v == some "rate"
def moneyOf (v : Json) : Option Int := numGet v "cents"

def stripPrefix (pre s : String) : String :=
  if List.isPrefixOf pre.toList s.toList then String.ofList (s.toList.drop pre.toList.length) else s

def keyOf (frame : Frame) (lineId : String) : String :=
  (frame.instKey.getD frame.docId) ++ "." ++ stripPrefix (frame.docId ++ ".") lineId

def findLine (doc : Json) (lineId : String) : Option Json :=
  match objGet doc "lines" with
  | some (.arr lines) => lines.find? (fun l => objGet l "id" == some (Json.str lineId))
  | _ => none

def isParam (doc : Json) (lineId : String) : Bool :=
  match objGet doc "parameters" with
  | some (.arr ps) => ps.any (fun p => p == Json.str lineId)
  | _ => false

def columnIndex (table : Json) (status : String) : Option Nat :=
  match objGet table "columns" with
  | some (.arr cols) =>
    cols.findIdx? (fun c =>
      match objGet c "statuses" with
      | some (.arr sts) => sts.any (fun s => s.getStr?.toOption == some status)
      | _ => false)
  | _ => none

def bandTax (table : Json) (col : Nat) (cents : Int) : Option (Int × Int) :=
  match objGet table "bands" with
  | some (.arr bands) =>
    bands.findSome? (fun b =>
      match numGet b "at_least", numGet b "less_than", objGet b "tax" with
      | some lo, some hi, some (.arr taxes) =>
        if lo ≤ cents ∧ cents < hi then
          (taxes[col]?).bind (fun t => (t.getInt?).toOption.map (fun c => (lo, c)))
        else none
      | _, _, _ => none)
  | _ => none

/-- The bands of a rate table for one column, in order: the upper bound ("but not
over", none when open) and the rate. -/
def rateBandRows (table : Json) (col : Nat) : List (Option Int × Json) :=
  match objGet table "rate_bands" with
  | some (.arr bands) =>
    bands.toList.map (fun b =>
      let r := match objGet b "rates" with
        | some (.arr rs) => (rs[col]?).getD Json.null
        | _ => Json.null
      (numGet b "not_over", mkRate ((numGet r "num").getD 0) ((numGet r "den").getD 1)))
  | _ => []

/-- A keyed table's key as a normalized string: an enum value or a count. -/
def keyedKey (k : Json) : String :=
  match k with
  | .str s => "e:" ++ s
  | .num n => "c:" ++ toString n.mantissa
  | _ => ""

/-- A keyed table's entry as an evaluator value of the table's cell type. -/
def keyedCell (cell : String) (v : Json) : Json :=
  if cell == "Rate" then mkRate ((numGet v "num").getD 0) ((numGet v "den").getD 1)
  else if cell == "Count" then mkCount ((v.getInt?).toOption.getD 0)
  else if cell == "Dollars" || cell == "NonNegDollars" then mkMoney ((v.getInt?).toOption.getD 0)
  else mkEnum ((v.getStr?).toOption.getD "")

/-- The rows of a keyed table: normalized key tuple and entry. -/
def keyedRows (table : Json) : List (List String × Json) :=
  let cell := (strGet table "cell").getD ""
  match objGet table "rows" with
  | some (.arr rows) =>
    rows.toList.map (fun r =>
      let ks := match objGet r "keys" with
        | some (.arr ks) => ks.toList.map keyedKey
        | _ => []
      (ks, keyedCell cell (objGetD r "value" Json.null)))
  | _ => []

/-- The key of the enclosing entry of collection `docId` within an instance key
(segments `doc[key]` joined by dots), or none when `docId` does not enclose it. -/
def enclosingKey (instKey : Option String) (docId : String) : Option String :=
  match instKey with
  | none => none
  | some k =>
    let segs := k.splitOn "."
    match segs.findIdx? (fun seg => seg.startsWith (docId ++ "[")) with
    | some i => some (".".intercalate (segs.take (i + 1)))
    | none => none

def inputValue (v : Json) : Json :=
  match v with
  | .num n => mkMoney n.mantissa
  | .bool b => mkBool b
  | .str s => mkEnum s
  | _ => unknown "bad input value"

def constValue (v : Json) : Json := inputValue v

-- ---------------------------------------------------------------------------
-- parameters (non-recursive)

def evalParam (ctx : Ctx) (name : String) : Json :=
  let entry := objGetD ctx.params "values" Json.null
  match objGet entry name with
  | none => (unknown s!"parameter {name} missing")
  | some e =>
    match objGet e "value" with
    | some (.num n) => (if strGet e "type" == some "Count" then mkCount n.mantissa else mkMoney n.mantissa)
    | some (.bool b) => (mkBool b)
    | some (.str s) => (mkEnum s)
    | some v@(.obj _) =>
      match numGet v "num", numGet v "den" with
      | some n, some d => (mkRate n d)
      | _, _ =>
        -- status-keyed money
        match objGet ctx.inputs "f1040.status" with
        | some (.str status) =>
          match numGet v status with
          | some cents => (mkMoney cents)
          | none => (unknown s!"no value for status {status}")
        | _ => (unknown "filing status not supplied for status-keyed parameter")
    | _ => (unknown s!"parameter {name} has bad value")

/-- The step budget exhausted: the value an evaluation gives when it runs out of fuel. -/
def budgetExhausted : Json := unknown "step budget exhausted"

/-- The budget the entry point gives each line: far above the depth of any
evaluation of the forms (each recursive call spends one unit along one path),
so an exhausted budget would show as a disagreement in `compare`. -/
def stepBudget : Nat := 1000000

-- ---------------------------------------------------------------------------
-- the evaluator

def eval (ctx : Ctx) : Nat → Frame → Cmd → EvalM Json
  | 0, _, _ => pure budgetExhausted
  | fuel + 1, frame, .operand op => do
    match op with
    | .str ref => eval ctx fuel frame (.line ref)
    | _ =>
      match objGet op "param" with
      | some (.str p) => pure (evalParam ctx p)
      | _ =>
        match objGet op "const" with
        | some c => pure (if strGet op "type" == some "Count" then mkCount (c.getInt?.toOption.getD 0) else constValue c)
        | none => pure (unknown "bad operand")
  | fuel + 1, frame, .test t => do
    match objGet t "all" with
    | some (.arr ts) =>
      let mut missing : Option Json := none
      for x in ts do
        let v ← eval ctx fuel frame (.test x)
        if kindOf v == some "refusal" then return v
        if isUnknown v then
          missing := missing <|> some v
        else if objGet v "value" == some (Json.bool false) then return mkBool false
      return missing.getD (mkBool true)
    | _ =>
    match objGet t "any" with
    | some (.arr ts) =>
      let mut missing : Option Json := none
      for x in ts do
        let v ← eval ctx fuel frame (.test x)
        if kindOf v == some "refusal" then return v
        if isUnknown v then
          missing := missing <|> some v
        else if objGet v "value" == some (Json.bool true) then return mkBool true
      return missing.getD (mkBool false)
    | _ =>
    match objGet t "not" with
    | some inner =>
      let v ← eval ctx fuel frame (.test inner)
      if isUnknown v then return v
      if objGet v "value" == some (Json.bool true) then return mkBool false
      return mkBool true
    | none =>
      let keys := ["eq", "ne", "lt", "le", "gt", "ge"]
      match keys.find? (fun k => match objGet t k with | some (.arr #[_, _]) => true | _ => false) with
      | none => pure (unknown "test has no comparison")
      | some k =>
          match objGet t k with
          | some (.arr #[a, b]) => do
            let av ← eval ctx fuel frame (.operand a)
            let bv ← eval ctx fuel frame (.operand b)
            match numGet av "lowerBound", numGet bv "value" with
            | some lower, some bound =>
              let certain := if k == "gt" || k == "le" then lower > bound else if k == "ge" || k == "lt" then lower ≥ bound else lower > bound
              if certain then return mkBool (k == "gt" || k == "ge" || k == "ne")
            | _, _ => pure ()
            if let some x := incompleteOperand [av, bv] then pure x
            else if (isMoney av && isMoney bv) || (kindOf av == some "count" && kindOf bv == some "count") then
              let x := (if isMoney av then moneyOf av else numGet av "value").getD 0
              let y := (if isMoney bv then moneyOf bv else numGet bv "value").getD 0
              pure (mkBool (match k with
                | "eq" => x == y | "ne" => x != y | "lt" => x < y
                | "le" => x ≤ y | "gt" => x > y | _ => x ≥ y))
            else if isEnum av && isEnum bv then
              let x := (strGet av "value").getD ""
              let y := (strGet bv "value").getD ""
              pure (mkBool (match k with | "eq" => x == y | "ne" => x != y | _ => false))
            else if isBool av && isBool bv then
              let x := objGet av "value" == some (Json.bool true)
              let y := objGet bv "value" == some (Json.bool true)
              pure (mkBool (match k with | "eq" => x == y | "ne" => x != y | _ => false))
            else pure (unknown "comparison operand types")
          | _ => pure (unknown "test has no comparison")
  | fuel + 1, frame, .line lineId => do
    let key := keyOf frame lineId
    match (← get).memo.get? key with
    | some v => return v
    | none =>
      if (← get).inflight.get? key == some true then
        return unknown s!"cycle at {key}"
      modify (fun st => { st with inflight := st.inflight.insert key true })
      let result ← eval ctx fuel frame (.fresh lineId)
      -- An exhausted budget is not a value of the line, so it is not remembered.
      if result != budgetExhausted then
        modify (fun st => { st with memo := st.memo.insert key result })
      modify (fun st => { st with inflight := st.inflight.insert key false })
      return result
  | fuel + 1, frame, .fresh lineId => do
    match findLine frame.doc lineId with
    | some line =>
      match objGet line "refuses" with
      | some (.arr rs) =>
        for r in rs do
          let gate := (strGet r "when").getD ""
          let before ← get
          let gv ← eval ctx fuel frame (.line gate)
          if gv == budgetExhausted then return gv
          if kindOf gv == some "unknown" && objGet r "when_known" == some (Json.bool true) then
            set before
            continue
          if isUnknown gv then return gv
          if objGet gv "value" == some (Json.bool true) then
            return Json.mkObj [("kind", Json.str "refusal"), ("gate", Json.str (if (findLine frame.doc gate).isSome then keyOf frame gate else gate)),
              ("form", objGetD r "form" Json.null), ("remedy", objGetD r "remedy" Json.null), ("cite", objGetD r "cite" Json.null)]
      | _ => pure ()
      let expr := objGetD line "expr" Json.null
      let op := (strGet expr "op").getD ""
      if frame.instKey.isSome && isParam frame.doc lineId then
        match objGet frame.bind lineId with
        | some operand =>
          match frame.caller with
          | some caller => eval ctx fuel caller (.operand operand)
          | none => pure (unknown s!"unbound parameter {lineId}")
        | none => pure (unknown s!"unbound parameter {lineId}")
      else if op == "input" then
        match objGet ctx.inputs (keyOf frame lineId) with
        | some v => pure (if strGet line "type" == some "Count" then mkCount (v.getInt?.toOption.getD 0) else inputValue v)
        | none => pure (unknown s!"no input supplied for {lineId}")
      else eval ctx fuel frame (.expr expr op)
    | none =>
      -- cross-document reference
      let formId := (lineId.splitOn ".").headD ""
      match ctx.forms.get? formId with
      | some doc =>
        if (findLine doc lineId).isSome then
          -- a line of an enclosing collection entry is read in that entry
          let enclosing := if (objGet doc "collection").isSome then enclosingKey frame.instKey formId else none
          eval ctx fuel { docId := formId, doc := doc, instKey := enclosing, bind := Json.null, caller := none } (.line lineId)
        else pure (unknown s!"unresolved reference {lineId}")
      | none => pure (unknown s!"unresolved reference {lineId}")

  | fuel + 1, frame, .expr expr op => do
    match op with
    | "copy" =>
      match objGet expr "from" with
      | some (.str ref) => eval ctx fuel frame (.line ref)
      | some v@(.obj _) =>
        let defId := (strGet v "def").getD ""
        let bind := objGetD v "bind" (Json.mkObj [])
        let ln := (strGet v "line").getD ""
        match ctx.forms.get? defId with
        | some doc =>
          let parent := frame.instKey.getD "root"
          let key := parent ++ "|inst:" ++ defId ++ "#" ++ bind.compress
          -- Binding operands are evaluated in the caller frame for the record, as the TypeScript evaluator does.
          match bind with
          | .obj kvs => for (_, op) in kvs.toArray do let _ ← eval ctx fuel frame (.operand op)
          | _ => pure ()
          eval ctx fuel { docId := defId, doc, instKey := some key, bind, caller := some frame } (.line ln)
        | none => pure (unknown s!"def {defId} missing")
      | _ => pure (unknown "copy has no source")
    | "param" =>
      match strGet expr "ref" with
      | some p => pure (evalParam ctx p)
      | none => pure (unknown "param has no ref")
    | "sum_over" =>
      let col := (strGet expr "collection").getD ""
      match ctx.forms.get? col with
      | none => return unknown "missing collection"
      | some doc =>
        let nested := (objGet (objGetD doc "collection" Json.null) "parent").isSome
        let parent := if nested then frame.instKey.getD "" else ""
        let rosterKey := "$" ++ col ++ (if parent == "" then "" else "@" ++ parent)
        -- an implicit collection with no roster given has its one implicit entry
        let implicitKey := strGet (objGetD doc "collection" Json.null) "implicit"
        let roster : Option Json := match objGet ctx.inputs rosterKey, implicitKey with
          | some r, _ => some r
          | none, some k => some (Json.arr #[Json.str k])
          | none, none => none
        match roster with
        | some (.arr entries) =>
          let field := (strGet expr "field").getD ""
          let isCount := strGet ((findLine doc field).getD Json.null) "type" == some "Count"
          let mut total : Int := 0
          let mut missing : Option Json := none
          let sorted := entries.qsort (fun a b => a.compress < b.compress)
          for entry in sorted do
            let entryKey := entry.getStr?.toOption.getD ""
            let key := (if parent == "" then "" else parent ++ ".") ++ col ++ "[" ++ entryKey ++ "]"
            let inner : Frame := {docId := col, doc, instKey := some key, bind := Json.null, caller := some frame}
            let selected ← match objGet expr "where" with
              | some t => eval ctx fuel inner (.test t)
              | none => pure (mkBool true)
            if kindOf selected == some "refusal" then return selected
            if isUnknown selected then
              missing := missing <|> some selected
            else if objGet selected "value" == some (Json.bool true) then
              let v ← eval ctx fuel inner (.line field)
              if kindOf v == some "refusal" then return v
              if isUnknown v then
                missing := missing <|> some v
              else total := total + (if isCount then numGet v "value" else moneyOf v).getD 0
          match missing with
          | some v => return if isCount then Json.mkObj [("kind", Json.str "unknown"), ("reason", Json.str "partial count"), ("lowerBound", Json.num (JsonNumber.fromInt total))] else v
          | none => return if isCount then mkCount total else mkMoney total
        | _ => return unknown "collection roster not confirmed"
    | "sum" =>
      match objGet expr "of" with
      | some (.arr refs) =>
        -- All operands money, or all Counts (the checker allows nothing else).
        let mut total : Int := 0
        let mut unk : Option Json := none
        let mut wrong : Option Json := none
        let mut kind : Option String := none
        for r in refs do
          match r.getStr? with
          | .ok ref => do
            let v ← eval ctx fuel frame (.line ref)
            if kindOf v == some "refusal" then return v
            if isMoney v || kindOf v == some "count" then
              let k := if isMoney v then "money" else "count"
              if kind.isSome && kind != some k then
                if wrong.isNone then wrong := some (unknown "sum operands mix money and Counts")
              if kind.isNone then kind := some k
              total := total + (if isMoney v then (moneyOf v).getD 0 else (numGet v "value").getD 0)
            else if isUnknown v then
              if unk.isNone then unk := some v
            else
              if wrong.isNone then wrong := some (unknown s!"sum operand {ref} is not money or a Count")
          | .error _ => return unknown "sum operand not a reference"
        match unk, wrong with
        | some u, _ => return u
        | none, some w => return w
        | none, none => return (if kind == some "count" then mkCount total else mkMoney total)
      | _ => pure (unknown "sum has no operands")
    | "subtract" | "subtract_floor0" =>
      match strGet expr "from" with
      | some fromRef =>
        let fromV ← eval ctx fuel frame (.line fromRef)
        let takeJson := objGetD expr "take" Json.null
        let takeV ← eval ctx fuel frame (.operand takeJson)
        if let some x := incompleteOperand [fromV, takeV] then pure x
        else if isMoney fromV && isMoney takeV then
          let d := (moneyOf fromV).getD 0 - (moneyOf takeV).getD 0
          pure (mkMoney (if op == "subtract_floor0" then max 0 d else d))
        else pure (unknown "operands are not money")
      | none => pure (unknown "subtract has no minuend")
    | "smaller_of" | "larger_of" =>
      match objGet expr "of" with
      | some (.arr refs) =>
        let mut got : Array Json := #[]
        for r in refs do
          match r.getStr? with
          | .ok ref =>
            let v ← eval ctx fuel frame (.line ref)
            got := got.push v
            if isRefusal v then break
          | .error _ => return unknown "operand not a reference"
        if let some x := incompleteOperand got.toList then return x
        let mut vals : List Int := []
        for v in got do
          if !(isMoney v) then return unknown "operands are not money"
          vals := (moneyOf v).getD 0 :: vals
        match vals with
        | [] => pure (unknown "no operands")
        | x :: rest =>
          let allFold := rest.foldl (fun acc y => if op == "smaller_of" then min acc y else max acc y) x
          pure (mkMoney allFold)
      | _ => pure (unknown "no operands")
    | "multiply_count" =>
      match strGet expr "amount", strGet expr "count" with
      | some amtRef, some cntRef =>
        let amtV ← eval ctx fuel frame (.line amtRef)
        let cntV ← eval ctx fuel frame (.line cntRef)
        if let some x := incompleteOperand [amtV, cntV] then pure x
        else if isMoney amtV && kindOf cntV == some "count" then
          pure (mkMoney (multiplyCount ((moneyOf amtV).getD 0) ((numGet cntV "value").getD 0)))
        else pure (unknown "multiply_count operands wrong")
      | _, _ => pure (unknown "multiply_count needs an amount and a count")
    | "prorate" =>
      match strGet expr "amount", strGet expr "part" with
      | some amtRef, some partRef =>
        let amtV ← eval ctx fuel frame (.line amtRef)
        let partV ← eval ctx fuel frame (.line partRef)
        let wholeV ← eval ctx fuel frame (.operand (objGetD expr "whole" Json.null))
        if let some x := incompleteOperand [amtV, partV, wholeV] then pure x
        else if isMoney amtV && isMoney partV && isMoney wholeV && (moneyOf wholeV).getD 0 > 0 then
          let places := ((numGet expr "places").getD 0).toNat
          pure (mkMoney (prorate ((moneyOf amtV).getD 0) ((moneyOf partV).getD 0) ((moneyOf wholeV).getD 0) places))
        else pure (unknown "prorate operands wrong")
      | _, _ => pure (unknown "prorate needs an amount and a part")
    | "multiply_rate" =>
      match strGet expr "amount" with
      | some amtRef =>
        let amtV ← eval ctx fuel frame (.line amtRef)
        let rateV ← eval ctx fuel frame (.operand (objGetD expr "rate" Json.null))
        if let some x := incompleteOperand [amtV, rateV] then pure x
        else if isMoney amtV && isRate rateV then
          let a := (moneyOf amtV).getD 0
          let n := (numGet rateV "num").getD 0
          let d := (numGet rateV "den").getD 1
          match numGet expr "unit" with
          | some u =>
            if u > 0 then pure (mkMoney (multiplyRateToUnit a n d u))
            else pure (unknown "multiply_rate unit is not a positive integer")
          | none => pure (mkMoney (multiplyRateHalfUp a n d))
        else pure (unknown "multiply_rate operands wrong")
      | none => pure (unknown "multiply_rate has no amount")
    | "percent_floor" =>
      match strGet expr "part" with
      | some partRef =>
        let partV ← eval ctx fuel frame (.line partRef)
        let wholeV ← eval ctx fuel frame (.operand (objGetD expr "whole" Json.null))
        if let some x := incompleteOperand [partV, wholeV] then pure x
        else if isMoney partV && isMoney wholeV && (moneyOf wholeV).getD 0 > 0 then
          let cap := (numGet expr "cap").getD 0
          pure (mkCount (percentFloor ((moneyOf partV).getD 0) ((moneyOf wholeV).getD 0) cap))
        else pure (unknown "percent_floor operands wrong")
      | none => pure (unknown "percent_floor has no part")
    | "round" =>
      match strGet expr "of" with
      | some ofRef =>
        let v ← eval ctx fuel frame (.line ofRef)
        if isUnknown v then pure v
        else if !(isMoney v) then pure (unknown "round operand is not money")
        else
          let unit := (numGet expr "unit").getD 0
          if unit ≤ 0 then pure (unknown "round unit is not a positive integer")
          else
            match roundByRule ((strGet expr "rule").getD "") ((moneyOf v).getD 0) unit with
            | some r => pure (mkMoney r)
            | none => pure (unknown "round rule unknown")
      | none => pure (unknown "round has no operand")
    | "table_lookup" =>
      let tableId := (strGet expr "table").getD ""
      match ctx.tables.get? tableId with
      | none => pure (unknown s!"table {tableId} missing")
      | some table =>
        let keyV ← eval ctx fuel frame (.line ((strGet expr "key").getD ""))
        let statusV ← eval ctx fuel frame (.line ((strGet expr "status").getD ""))
        if let some x := incompleteOperand [keyV, statusV] then pure x
        else
          let status := (strGet statusV "value").getD ""
          match columnIndex table status with
          | none => pure (unknown s!"no column for {status}")
          | some col =>
            match bandTax table col ((moneyOf keyV).getD 0) with
            | some (_, c) => pure (mkMoney c)
            | none => pure (unknown s!"no band for {moneyOf keyV}")
    | "rate_lookup" =>
      let tableId := (strGet expr "table").getD ""
      match ctx.tables.get? tableId with
      | none => pure (unknown s!"table {tableId} missing")
      | some table =>
        let keyV ← eval ctx fuel frame (.line ((strGet expr "key").getD ""))
        if isRefusal keyV then pure keyV
        else
          let hasCols : Bool := match objGet table "columns" with
            | some (.arr cs) => cs.size != 0
            | _ => false
          let statusV? : Option Json ←
            if hasCols then some <$> eval ctx fuel frame (.line ((strGet expr "status").getD ""))
            else pure none
          let colE : Except Json Nat :=
            match incompleteOperand (keyV :: statusV?.toList) with
            | some x => Except.error x
            | none =>
              match statusV? with
              | some statusV =>
                let status := (strGet statusV "value").getD ""
                match columnIndex table status with
                | some c => Except.ok c
                | none => Except.error (unknown s!"no column for {status}")
              | none => Except.ok 0
          match colE with
          | Except.error e => pure e
          | Except.ok col =>
            match rateBand (rateBandRows table col) ((moneyOf keyV).getD 0) with
            | some v => pure v
            | none => pure (unknown s!"no band for {moneyOf keyV}")
    | "keyed_lookup" =>
      let tableId := (strGet expr "table").getD ""
      match ctx.tables.get? tableId with
      | none => pure (unknown s!"table {tableId} missing")
      | some table =>
        match objGet expr "keys" with
        | some (.arr refs) =>
          let mut got : Array Json := #[]
          for r in refs do
            match r.getStr? with
            | .ok ref => do
              let v ← eval ctx fuel frame (.line ref)
              got := got.push v
              if isRefusal v then break
            | .error _ => return unknown "keyed_lookup key not a reference"
          if let some x := incompleteOperand got.toList then return x
          let mut keys : List String := []
          for v in got do
            if isEnum v then keys := keys ++ ["e:" ++ (strGet v "value").getD ""]
            else if kindOf v == some "count" then keys := keys ++ ["c:" ++ toString ((numGet v "value").getD 0)]
            else return unknown "keyed_lookup key is not an enum or count"
          match keyedLookup (keyedRows table) keys with
          | some v => pure v
          | none => pure (unknown s!"no row of {tableId}")
        | _ => pure (unknown "keyed_lookup has no keys")
    | "choose" =>
      match objGet expr "alternatives" with
      | some (.arr alts) =>
        for alt in alts do
          let guard := objGetD alt "guard" Json.null
          let gv ← eval ctx fuel frame (.test guard)
          if isUnknown gv then return gv
          if objGet gv "value" == some (Json.bool true) then
            match objGet alt "then" with
            | some (.str ref) => return (← eval ctx fuel frame (.line ref))
            | some v@(.obj _) =>
              let defId := (strGet v "def").getD ""
              let bind := objGetD v "bind" (Json.mkObj [])
              let ln := (strGet v "line").getD ""
              match ctx.forms.get? defId with
              | some doc =>
                let parent := frame.instKey.getD "root"
                let key := parent ++ "|inst:" ++ defId ++ "#" ++ bind.compress
                -- Binding operands are evaluated in the caller frame for the record, as the TypeScript evaluator does.
                match bind with
                | .obj kvs => for (_, op) in kvs.toArray do let _ ← eval ctx fuel frame (.operand op)
                | _ => pure ()
                return (← eval ctx fuel { docId := defId, doc, instKey := some key, bind, caller := some frame } (.line ln))
              | none => return unknown s!"def {defId} missing"
            | _ => return unknown "choose branch missing"
        return unknown "no guard matched"
      | _ => pure (unknown "choose has no alternatives")
    | "test" => eval ctx fuel frame (.test expr)
    | _ => pure (unknown s!"atom {op} not implemented")

end TaxFormalization
