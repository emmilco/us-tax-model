/-
Reference evaluator entry point:
  lake exe taxeval -- --canonical <dir> --inputs <file.json> --out <file.json>

Evaluates every line of f1040 and qdcg from the canonical JSON and writes
{ "lineId": value, ... } for comparison with the TypeScript evaluator.
-/

import TaxFormalization.Eval
import TaxFormalization.Lemmas

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

end TaxFormalization

open TaxFormalization

def main (args : List String) : IO UInt32 := do
  let rec parseArgs : List String → Option String × Option String × String
    | "--inputs" :: v :: rest =>
      let (_, o, c) := parseArgs rest
      (some v, o, c)
    | "--out" :: v :: rest =>
      let (i, _, c) := parseArgs rest
      (i, some v, c)
    | "--canonical" :: v :: rest =>
      let (i, o, _) := parseArgs rest
      (i, o, v)
    | _ :: rest => parseArgs rest
    | [] => (none, none, "../canonical/2025")
  let (inputsPath, outPath, canonDir) := parseArgs args
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
    let memo ← IO.mkRef (∅ : Std.HashMap String Json)
    let inflight ← IO.mkRef (∅ : Std.HashMap String Bool)
    let ctx : Ctx := { forms, params, tables, inputs, memo, inflight }
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
                let v ← eval ctx { docId, doc, instKey := none, bind := Json.null, caller := none } (.line id)
                pairs := (id, v) :: pairs
                count := count + 1
              | none => pure ()
            | none => pure ()
        | _ => pure ()
    for (key, value) in (← memo.get).toList do
      if key.contains '[' then pairs := (key, value) :: pairs
    let sorted := pairs.toArray.qsort (fun a b => a.1 < b.1)
    let out := Json.mkObj sorted.toList
    IO.FS.writeFile outp (out.compress ++ "\n")
    IO.println s!"lean evaluated {count} lines"
    return 0
  | _, _ =>
    IO.println "usage: taxeval --canonical <dir> --inputs <file> --out <file>"
    return 2
