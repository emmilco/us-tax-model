/-
Reference evaluator entry point:
  lake exe taxeval -- [--canonical <dir> | --year N] --inputs <file.json> --out <file.json> [--budget N]

Without --canonical, reads ../canonical/<year>/, the year being --year or else the
newest adopted year in ../years.json.

Evaluates every line of every form, and every line of every confirmed collection
entry (the TypeScript evaluator's `allTargets`), from the canonical JSON and writes
{ "lineId": value, ... } for comparison with the TypeScript evaluator.
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

end TaxFormalization

open TaxFormalization

def main (args : List String) : IO UInt32 := do
  let rec parseArgs : List String → Option String × Option String × Option String × Option String × Nat
    | "--inputs" :: v :: rest =>
      let (_, o, c, y, b) := parseArgs rest
      (some v, o, c, y, b)
    | "--out" :: v :: rest =>
      let (i, _, c, y, b) := parseArgs rest
      (i, some v, c, y, b)
    | "--canonical" :: v :: rest =>
      let (i, o, _, y, b) := parseArgs rest
      (i, o, some v, y, b)
    | "--year" :: v :: rest =>
      let (i, o, c, _, b) := parseArgs rest
      (i, o, c, some v, b)
    | "--budget" :: v :: rest =>
      let (i, o, c, y, _) := parseArgs rest
      (i, o, c, y, v.toNat?.getD stepBudget)
    | _ :: rest => parseArgs rest
    | [] => (none, none, none, none, stepBudget)
  let (inputsPath, outPath, canonArg, yearArg, budget) := parseArgs args
  let canonDir ← match canonArg, yearArg with
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
  match inputsPath, outPath with
  | some inp, some outp => do
    let canon : System.FilePath := canonDir
    let forms ← readDocs canon
    let tables ← readDocs (canon / "tables")
    let paramsRaw ← IO.FS.readFile (canon / "params.json")
    let params :=
      match Json.parse paramsRaw with
      | .ok j => (j.getObjVal? "params").toOption.getD Json.null
      | .error _ => Json.null
    let inputsRaw ← IO.FS.readFile inp
    let inputs :=
      match Json.parse inputsRaw with
      | .ok j => j
      | .error e => panic! s!"inputs parse error: {e}"
    let ctx : Ctx := { forms, params, tables, inputs }
    let mut st : EvalState := {}
    let mut pairs : List (String × Json) := []
    let mut count : Nat := 0
    for (docId, candidate) in forms.toList do
      if (candidate.getObjVal? "collection").isOk || (candidate.getObjValAs? String "kind").toOption == some "def" then continue
      match forms.get? docId with
      | none => pure ()
      | some doc =>
        match doc.getObjVal? "lines" with
        | .ok (.arr lines) =>
          for l in lines do
            match (l.getObjVal? "id").toOption with
            | some idJson =>
              match idJson.getStr?.toOption with
              | some id =>
                let (v, st') := (eval ctx budget { docId, doc, instKey := none, bind := Json.null, caller := none } (.line id)).run st
                st := st'
                pairs := (id, v) :: pairs
                count := count + 1
              | none => pure ()
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
              count := count + 1
            | none => pure ()
        | _ => pure ()
    for (key, value) in st.memo.toList do
      if key.contains '[' then pairs := (key, value) :: pairs
    -- A line that ran out of budget has no value; refuse to report it as one.
    if pairs.any (fun p => p.2 == budgetExhausted) then
      IO.eprintln s!"step budget of {budget} exhausted"
      return 3
    let sorted := pairs.toArray.qsort (fun a b => a.1 < b.1)
    let out := Json.mkObj sorted.toList
    IO.FS.writeFile outp (out.compress ++ "\n")
    IO.println s!"lean evaluated {count} lines"
    return 0
  | _, _ =>
    IO.println "usage: taxeval --canonical <dir> --inputs <file> --out <file> [--budget N]"
    return 2
