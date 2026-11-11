/-
Reference evaluator entry point:
  lake exe taxeval -- [--canonical <dir> | --year N] [--budget N]  < cases  > answers

Without --canonical, reads ../canonical/<year>/, the year being --year or else the
newest adopted year in ../years.json.

Reads the canonical build once. Then reads standard input to its end, one case per
line, {"id": <string>, "inputs": {<answers>}}, and writes one answer per line read,
in the order read, each as soon as it is computed:
  {"id": <id>, "values": {"lineId": value, ...}}   the case's values, or
  {"id": <id>, "failed": <reason>}                 when it has none (a line ran out of the
                                                   step budget, or the inputs are not an object).
A line that is not a case with an id is answered {"id": null, "failed": <reason>}.
The exit status is 0 when every line read was answered.

The values are every line of every form, and every line of every confirmed collection
entry (the TypeScript evaluator's `allTargets`), for comparison with the TypeScript
evaluator. A case's answer is `answerCase` of the build, the budget and the line: a pure
function, so no case's evaluation can reach another's.
-/

import TaxFormalization.Eval
import TaxFormalization.Lemmas
import TaxFormalization.EvalProps

open Lean (Json)

namespace TaxFormalization

def readDocs (dir : System.FilePath) : IO (Std.HashMap String Json) := do
  let entries ← dir.readDir
  let mut map : Std.HashMap String Json := ∅
  for e in entries do
    if e.fileName.endsWith ".json" then
      let txt ← IO.FS.readFile e.path
      match Json.parse txt with
      | .ok j =>
        let doc :=
          match (j.getObjVal? "form").toOption with
          | some d => some d
          | none =>
            match (j.getObjVal? "def").toOption with
            | some d => some d
            | none => ((j.getObjVal? "table").toOption)
        match doc with
        | some d =>
          match (d.getObjVal? "id").toOption with
          | some idJson =>
            match idJson.getStr?.toOption with
            | some id => map := map.insert id d
            | none => pure ()
          | none => pure ()
        | none => pure ()
      | .error _ => pure ()
  return map

/-- The canonical build as the evaluator reads it: all of an evaluation's context that
does not come from the case. -/
structure Build where
  forms : Std.HashMap String Json
  params : Json
  tables : Std.HashMap String Json

def readBuild (canon : System.FilePath) : IO Build := do
  let forms ← readDocs canon
  let tables ← readDocs (canon / "tables")
  let paramsRaw ← IO.FS.readFile (canon / "params.json")
  let fedParams :=
    match Json.parse paramsRaw with
    | .ok j => (j.getObjVal? "params").toOption.getD Json.null
    | .error _ => Json.null
  -- New York parameters (decision C1, docs/ny/DECISIONS.md) are written to params-ny.json by the
  -- build; their `values` are merged into the federal ones, as engine/src/canonical.ts does.
  let nyPath := canon / "params-ny.json"
  let params ← if ← nyPath.pathExists then do
      let nyRaw ← IO.FS.readFile nyPath
      let nyValues :=
        match Json.parse nyRaw with
        | .ok j => ((j.getObjVal? "params").toOption.bind (fun p => (p.getObjVal? "values").toOption)).getD (Json.mkObj [])
        | .error _ => Json.mkObj []
      let fedValues := (fedParams.getObjVal? "values").toOption.getD (Json.mkObj [])
      pure (fedParams.setObjVal! "values" (fedValues.mergeObj nyValues))
    else pure fedParams
  return { forms, params, tables }

/-- The confirmed entries of collection `docId`: `<collection>[<key>]` for a top-level
collection, nested under each confirmed entry of the parent collection otherwise; a roster
not given confirms no entry, except that an implicit collection then has its one implicit entry. -/
partial def instancesOf (forms : Std.HashMap String Json) (inputs : Json) (docId : String) : List String :=
  match forms.get? docId with
  | none => []
  | some doc =>
    let coll := (doc.getObjVal? "collection").toOption.getD Json.null
    let parentId := ((coll.getObjVal? "parent").toOption.bind (fun v => v.getStr?.toOption))
    let entriesUnder (parent : Option String) : List String :=
      let rosterKey := "$" ++ docId ++ (match parent with | some p => "@" ++ p | none => "")
      let implicitKey := (coll.getObjVal? "implicit").toOption.bind (fun v => v.getStr?.toOption)
      let roster : Option Json := match (inputs.getObjVal? rosterKey).toOption, implicitKey with
        | some r, _ => some r
        | none, some k => some (Json.arr #[Json.str k])
        | none, none => none
      match roster with
      | some (.arr keys) =>
        let names := (keys.toList.filterMap (fun k => k.getStr?.toOption)).toArray.qsort (· < ·)
        names.toList.map (fun k => (match parent with | some p => p ++ "." | none => "") ++ docId ++ "[" ++ k ++ "]")
      | _ => []
    match parentId with
    | none => entriesUnder none
    | some pid => (instancesOf forms inputs pid).flatMap (fun p => entriesUnder (some p))

/-- The values of one return: every line of every form and every line of every confirmed
collection entry, as an object keyed by line; or none when a line ran out of the budget,
which has no value. The memo and the cycle markers begin empty here and end here. -/
def evaluateCase (build : Build) (budget : Nat) (inputs : Json) : Option Json := Id.run do
  let forms := build.forms
  let ctx : Ctx := { forms, params := build.params, tables := build.tables, inputs }
  let mut st : EvalState := {}
  let mut pairs : List (String × Json) := []
  for (docId, doc) in forms.toList do
    if (doc.getObjVal? "collection").isOk || (doc.getObjValAs? String "kind").toOption == some "def" then continue
    match doc.getObjVal? "lines" with
    | .ok (.arr lines) =>
      for l in lines do
        match ((l.getObjVal? "id").toOption.bind (fun v => v.getStr?.toOption)) with
        | some id =>
          let (v, st') := (eval ctx budget { docId, doc, instKey := none, bind := Json.null, caller := none } (.line id)).run st
          st := st'
          pairs := (id, v) :: pairs
        | none => pure ()
    | _ => pure ()
  -- Every line of every confirmed collection entry, as the TypeScript evaluator's allTargets.
  for (docId, doc) in forms.toList do
    if !(doc.getObjVal? "collection").isOk then continue
    for inst in instancesOf forms inputs docId do
      match doc.getObjVal? "lines" with
      | .ok (.arr lines) =>
        for l in lines do
          match ((l.getObjVal? "id").toOption.bind (fun v => v.getStr?.toOption)) with
          | some id =>
            let (_, st') := (eval ctx budget { docId, doc, instKey := some inst, bind := Json.null, caller := none } (.line id)).run st
            st := st'
          | none => pure ()
      | _ => pure ()
  for (key, value) in st.memo.toList do
    if key.contains '[' then pairs := (key, value) :: pairs
  -- A line that ran out of budget has no value; refuse to report it as one.
  if pairs.any (fun p => p.2 == budgetExhausted) then return none
  let sorted := pairs.toArray.qsort (fun a b => a.1 < b.1)
  return some (Json.mkObj sorted.toList)

/-- The answer to one line of standard input. -/
def answerCase (build : Build) (budget : Nat) (line : String) : Json :=
  let failed (id : Json) (reason : String) := Json.mkObj [("id", id), ("failed", Json.str reason)]
  match Json.parse line with
  | .error e => failed Json.null s!"the line is not JSON: {e}"
  | .ok case =>
    match (case.getObjVal? "id").toOption.bind (fun v => v.getStr?.toOption) with
    | none => failed Json.null "the line has no id"
    | some id =>
      match (case.getObjVal? "inputs").toOption with
      | some (.obj inputs) =>
        match evaluateCase build budget (.obj inputs) with
        | some values => Json.mkObj [("id", Json.str id), ("values", values)]
        | none => failed (Json.str id) s!"step budget of {budget} exhausted"
      | _ => failed (Json.str id) "the case has no inputs object"

structure Options where
  canonical : Option String := none
  year : Option String := none
  budget : Nat := stepBudget

def usage : String := "usage: taxeval [--canonical <dir> | --year N] [--budget N]  < cases  > answers"

def parseArgs : List String → Options → Except String Options
  | [], o => .ok o
  | "--canonical" :: v :: rest, o => parseArgs rest { o with canonical := some v }
  | "--year" :: v :: rest, o => parseArgs rest { o with year := some v }
  | "--budget" :: v :: rest, o =>
    match v.toNat? with
    | some n => parseArgs rest { o with budget := n }
    | none => .error s!"--budget: expected a number, got '{v}'"
  | arg :: _, _ => .error s!"unexpected argument '{arg}'"

end TaxFormalization

open TaxFormalization

def main (args : List String) : IO UInt32 := do
  match parseArgs args {} with
  | .error e =>
    IO.eprintln e
    IO.eprintln usage
    return 2
  | .ok options =>
    let canonDir ← match options.canonical, options.year with
      | some c, _ => pure c
      | none, some y => pure s!"../canonical/{y}"
      | none, none => do
        let adopted := (Json.parse (← IO.FS.readFile "../years.json")).bind (·.getObjValAs? (Array Nat) "adopted")
        match adopted with
        | .ok years =>
          match years.toList.max? with
          | some y => pure s!"../canonical/{y}"
          | none => throw (IO.userError "years.json lists no adopted year; pass --year")
        | .error e => throw (IO.userError s!"years.json: {e}")
    let build ← readBuild canonDir
    let stdin ← IO.getStdin
    let stdout ← IO.getStdout
    repeat
      let line ← stdin.getLine
      if line.isEmpty then break
      stdout.putStrLn (answerCase build options.budget line).compress
      stdout.flush
    return 0
