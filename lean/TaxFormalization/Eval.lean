/-
The reference evaluator: reads the canonical JSON and evaluates the Stage 1
slice with the same semantics as the TypeScript evaluator (integer cents,
half-up multiply via the proved Atoms functions).

The evaluator is a single partial recursive function over an instruction
dispatch, mirroring the TypeScript evaluator's frame handling for
parameterized def instances.
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
  memo : IO.Ref (Std.HashMap String Json)
  inflight : IO.Ref (Std.HashMap String Bool)

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

-- ---------------------------------------------------------------------------
-- helpers (non-recursive)

private def objGet (j : Json) (k : String) : Option Json := (j.getObjVal? k).toOption
private def objGetD (j : Json) (k : String) (d : Json) : Json := (objGet j k).getD d
private def numGet (j : Json) (k : String) : Option Int := (objGet j k).bind (fun v => (v.getInt?).toOption)
private def strGet (j : Json) (k : String) : Option String := (objGet j k).bind (fun v => (v.getStr?).toOption)

def unknown (reason : String) : Json := Json.mkObj [("kind", Json.str "unknown"), ("reason", Json.str reason)]
def mkMoney (n : Int) : Json := Json.mkObj [("kind", Json.str "money"), ("cents", Json.num (JsonNumber.fromInt n))]
def mkBool (b : Bool) : Json := Json.mkObj [("kind", Json.str "bool"), ("value", Json.bool b)]
def mkEnum (s : String) : Json := Json.mkObj [("kind", Json.str "enum"), ("value", Json.str s)]
def mkRate (n d : Int) : Json :=
  Json.mkObj [("kind", Json.str "rate"), ("num", Json.num (JsonNumber.fromInt n)), ("den", Json.num (JsonNumber.fromInt d))]

def kindOf (v : Json) : Option String := strGet v "kind"
def isUnknown (v : Json) : Bool := kindOf v == some "unknown"
def isMoney (v : Json) : Bool := kindOf v == some "money"
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

def inputValue (v : Json) : Json :=
  match v with
  | .num n => mkMoney n.mantissa
  | .bool b => mkBool b
  | .str s => mkEnum s
  | _ => unknown "bad input value"

def constValue (v : Json) : Json := inputValue v

-- ---------------------------------------------------------------------------
-- the evaluator

partial def eval (ctx : Ctx) (frame : Frame) : Cmd → IO Json
  | .operand op => do
    match op with
    | .str ref => eval ctx frame (.line ref)
    | _ =>
      match objGet op "param" with
      | some (.str p) => evalParam ctx p
      | _ =>
        match objGet op "const" with
        | some c => pure (constValue c)
        | none => pure (unknown "bad operand")
  | .test t => do
    match objGet t "all" with
    | some (.arr ts) =>
      for x in ts do
        let v ← eval ctx frame (.test x)
        if isUnknown v then return v
        if !(isBool v) then return unknown "guard not bool"
        if objGet v "value" == some (Json.bool false) then return mkBool false
      return mkBool true
    | _ =>
    match objGet t "any" with
    | some (.arr ts) =>
      for x in ts do
        let v ← eval ctx frame (.test x)
        if isUnknown v then return v
        if !(isBool v) then return unknown "guard not bool"
        if objGet v "value" == some (Json.bool true) then return mkBool true
      return mkBool false
    | _ =>
    match objGet t "not" with
    | some inner =>
      let v ← eval ctx frame (.test inner)
      if isUnknown v then return v
      if objGet v "value" == some (Json.bool true) then return mkBool false
      return mkBool true
    | none =>
      let keys := ["eq", "ne", "lt", "le", "gt", "ge"]
      let rec go : List String → IO Json
        | [] => pure (unknown "test has no comparison")
        | k :: rest => do
          match objGet t k with
          | some (.arr #[a, b]) => do
            let av ← eval ctx frame (.operand a)
            let bv ← eval ctx frame (.operand b)
            if isUnknown av then pure av
            else if isUnknown bv then pure bv
            else if isMoney av && isMoney bv then
              let x := (moneyOf av).getD 0
              let y := (moneyOf bv).getD 0
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
          | _ => go rest
      go keys
  | .line lineId => do
    let key := keyOf frame lineId
    match (← ctx.memo.get).get? key with
    | some v => return v
    | none =>
      if (← ctx.inflight.get).get? key == some true then
        return unknown s!"cycle at {key}"
      ctx.inflight.modify (fun m => m.insert key true)
      let result ← evalFresh ctx frame lineId
      ctx.memo.modify (fun m => m.insert key result)
      ctx.inflight.modify (fun m => m.insert key false)
      return result
where
  evalParam (ctx : Ctx) (name : String) : IO Json := do
    let entry := objGetD ctx.params "values" Json.null
    match objGet entry name with
    | none => pure (unknown s!"parameter {name} missing")
    | some e =>
      match objGet e "value" with
      | some (.num n) => pure (mkMoney n.mantissa)
      | some (.bool b) => pure (mkBool b)
      | some v@(.obj _) =>
        match numGet v "num", numGet v "den" with
        | some n, some d => pure (mkRate n d)
        | _, _ =>
          -- status-keyed money
          match objGet ctx.inputs "f1040.status" with
          | some (.str status) =>
            match numGet v status with
            | some cents => pure (mkMoney cents)
            | none => pure (unknown s!"no value for status {status}")
          | _ => pure (unknown "filing status not supplied for status-keyed parameter")
      | _ => pure (unknown s!"parameter {name} has bad value")

  evalFresh (ctx : Ctx) (frame : Frame) (lineId : String) : IO Json := do
    match findLine frame.doc lineId with
    | some line =>
      let expr := objGetD line "expr" Json.null
      let op := (strGet expr "op").getD ""
      if frame.instKey.isSome && isParam frame.doc lineId then
        match objGet frame.bind lineId with
        | some operand =>
          match frame.caller with
          | some caller => eval ctx caller (.operand operand)
          | none => pure (unknown s!"unbound parameter {lineId}")
        | none => pure (unknown s!"unbound parameter {lineId}")
      else if op == "input" then
        match objGet ctx.inputs lineId with
        | some v => pure (inputValue v)
        | none => pure (unknown s!"no input supplied for {lineId}")
      else evalExpr ctx frame expr op line
    | none =>
      -- cross-document reference
      let formId := (lineId.splitOn ".").headD ""
      match ctx.forms.get? formId with
      | some doc =>
        if (findLine doc lineId).isSome then
          eval ctx { docId := formId, doc := doc, instKey := none, bind := Json.null, caller := none } (.line lineId)
        else pure (unknown s!"unresolved reference {lineId}")
      | none => pure (unknown s!"unresolved reference {lineId}")

  evalExpr (ctx : Ctx) (frame : Frame) (expr : Json) (op : String) (_line : Json) : IO Json := do
    match op with
    | "copy" =>
      match objGet expr "from" with
      | some (.str ref) => eval ctx frame (.line ref)
      | some v@(.obj _) =>
        let defId := (strGet v "def").getD ""
        let bind := objGetD v "bind" (Json.mkObj [])
        let ln := (strGet v "line").getD ""
        match ctx.forms.get? defId with
        | some doc =>
          let parent := frame.instKey.getD "root"
          let key := parent ++ "|inst:" ++ defId ++ "#" ++ bind.compress
          eval ctx { docId := defId, doc, instKey := some key, bind, caller := some frame } (.line ln)
        | none => pure (unknown s!"def {defId} missing")
      | _ => pure (unknown "copy has no source")
    | "param" =>
      match strGet expr "ref" with
      | some p => evalParam ctx p
      | none => pure (unknown "param has no ref")
    | "sum" =>
      match objGet expr "of" with
      | some (.arr refs) =>
        let mut total : Int := 0
        let mut unk : Option Json := none
        for r in refs do
          match r.getStr? with
          | .ok ref => do
            let v ← eval ctx frame (.line ref)
            if isMoney v then
              total := total + (moneyOf v).getD 0
            else if isUnknown v then
              if unk.isNone then unk := some v
            else
              return unknown s!"sum operand {ref} is not money"
          | .error _ => return unknown "sum operand not a reference"
        match unk with
        | some u => return u
        | none => return mkMoney total
      | _ => pure (unknown "sum has no operands")
    | "subtract" | "subtract_floor0" =>
      match strGet expr "from" with
      | some fromRef =>
        let fromV ← eval ctx frame (.line fromRef)
        let takeJson := objGetD expr "take" Json.null
        let takeV ← eval ctx frame (.operand takeJson)
        if isUnknown fromV then pure fromV
        else if isUnknown takeV then pure takeV
        else if isMoney fromV && isMoney takeV then
          let d := (moneyOf fromV).getD 0 - (moneyOf takeV).getD 0
          pure (mkMoney (if op == "subtract_floor0" then max 0 d else d))
        else pure (unknown "operands are not money")
      | none => pure (unknown "subtract has no minuend")
    | "smaller_of" | "larger_of" =>
      match objGet expr "of" with
      | some (.arr refs) =>
        let mut vals : List Int := []
        for r in refs do
          match r.getStr? with
          | .ok ref =>
            let v ← eval ctx frame (.line ref)
            if isUnknown v then return v
            if !(isMoney v) then return unknown "operands are not money"
            vals := (moneyOf v).getD 0 :: vals
          | .error _ => return unknown "operand not a reference"
        match vals with
        | [] => pure (unknown "no operands")
        | x :: rest =>
          let allFold := rest.foldl (fun acc y => if op == "smaller_of" then min acc y else max acc y) x
          pure (mkMoney allFold)
      | _ => pure (unknown "no operands")
    | "multiply_rate" =>
      match strGet expr "amount" with
      | some amtRef =>
        let amtV ← eval ctx frame (.line amtRef)
        let rateV ← eval ctx frame (.operand (objGetD expr "rate" Json.null))
        if isUnknown amtV then pure amtV
        else if isUnknown rateV then pure rateV
        else if isMoney amtV && isRate rateV then
          let a := (moneyOf amtV).getD 0
          let n := (numGet rateV "num").getD 0
          let d := (numGet rateV "den").getD 1
          pure (mkMoney (multiplyRateHalfUp a n d))
        else pure (unknown "multiply_rate operands wrong")
      | none => pure (unknown "multiply_rate has no amount")
    | "table_lookup" =>
      let tableId := (strGet expr "table").getD ""
      match ctx.tables.get? tableId with
      | none => pure (unknown s!"table {tableId} missing")
      | some table =>
        let keyV ← eval ctx frame (.line ((strGet expr "key").getD ""))
        let statusV ← eval ctx frame (.line ((strGet expr "status").getD ""))
        if isUnknown keyV then pure keyV
        else if isUnknown statusV then pure statusV
        else
          let status := (strGet statusV "value").getD ""
          match columnIndex table status with
          | none => pure (unknown s!"no column for {status}")
          | some col =>
            match bandTax table col ((moneyOf keyV).getD 0) with
            | some (_, c) => pure (mkMoney c)
            | none => pure (unknown s!"no band for {moneyOf keyV}")
    | "choose" =>
      match objGet expr "alternatives" with
      | some (.arr alts) =>
        for alt in alts do
          let guard := objGetD alt "guard" Json.null
          let gv ← eval ctx frame (.test guard)
          if isUnknown gv then return gv
          if objGet gv "value" == some (Json.bool true) then
            match objGet alt "then" with
            | some (.str ref) => return (← eval ctx frame (.line ref))
            | some v@(.obj _) =>
              let defId := (strGet v "def").getD ""
              let bind := objGetD v "bind" (Json.mkObj [])
              let ln := (strGet v "line").getD ""
              match ctx.forms.get? defId with
              | some doc =>
                let parent := frame.instKey.getD "root"
                let key := parent ++ "|inst:" ++ defId ++ "#" ++ bind.compress
                return (← eval ctx { docId := defId, doc, instKey := some key, bind, caller := some frame } (.line ln))
              | none => return unknown s!"def {defId} missing"
            | _ => return unknown "choose branch missing"
        return unknown "no guard matched"
      | _ => pure (unknown "choose has no alternatives")
    | "test" => eval ctx frame (.test expr)
    | _ => pure (unknown s!"atom {op} not implemented")

end TaxFormalization
