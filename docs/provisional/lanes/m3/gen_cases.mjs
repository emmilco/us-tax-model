// Lane m3: write mutation fixture cases from a table (docs/provisional/lanes/m3/cases.json) and merge them, by id,
// into fixtures/2025/mutation.json. Each row names a base (an existing case of mutation.json, whose inputs are taken)
// or "none" (inputs from the row alone), the inputs set (`set`) and dropped (`drop`, unasked questions left
// unanswered), and the expected lines with the value predicted by hand before running: {"refusal": "<gate>"},
// {"bool": true}, {"money": <cents>}, {"unknown": true}. The script evaluates the case, stops on any prediction the
// evaluator does not give, and writes the evaluator's value for each expected line (a refusal value carries the
// form, remedy and citation the refusing line states). Usage: node gen_cases.mjs [--check]  (--check: no write)
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { execFileSync } from "node:child_process";
const ROOT = resolve(import.meta.dirname, "../../../..");
const dist = (m) => import(resolve(ROOT, "engine/dist", m));
const { loadCanonical } = await dist("canonical.js");
const { evaluate } = await dist("eval.js");
const { resolveCase } = await dist("fixture-inputs.js");
const data = loadCanonical();
const file = resolve(ROOT, "fixtures/2025/mutation.json");
const fixture = JSON.parse(readFileSync(file, "utf8"));
const rows = JSON.parse(readFileSync(resolve(import.meta.dirname, "cases.json"), "utf8"));
const byId = new Map(fixture.cases.map((c) => [c.id, c]));
const out = [];
let bad = 0;
for (const r of rows) {
  let inputs = {};
  if (r.base !== "none") {
    const base = byId.get(r.base);
    if (!base) { console.error(`${r.id}: no base case ${r.base}`); bad++; continue; }
    inputs = structuredClone(base.inputs);
  }
  for (const [k, v] of Object.entries(r.set ?? {})) inputs[k] = v;
  for (const k of r.drop ?? []) { if (!(k in inputs)) { console.error(`${r.id}: drop ${k}: not stated`); bad++; } delete inputs[k]; }
  const resolved = resolveCase({ id: r.id, inputs }, "mutation.json", data, "federal");
  const targets = Object.keys(r.expect);
  const result = evaluate(data, resolved, targets);
  const expect = {};
  for (const [line, want] of Object.entries(r.expect)) {
    const v = result.derivations.get(line)?.value;
    const ok = v && ("refusal" in want ? v.kind === "refusal" && v.gate === want.refusal
      : "bool" in want ? v.kind === "bool" && v.value === want.bool
      : "money" in want ? v.kind === "money" && v.cents === want.money
      : "unknown" in want ? v.kind === "unknown" : false);
    if (!ok) { console.error(`${r.id}: ${line}: predicted ${JSON.stringify(want)}, evaluator gives ${JSON.stringify(v)}`); bad++; }
    expect[line] = v;
  }
  out.push({ id: r.id, covers: r.covers, evidence: r.evidence ?? "synthetic regression (not class B)", evidence_note: r.note, inputs, expect });
}
if (bad) { console.error(`${bad} problems; nothing written`); process.exit(1); }
if (process.argv.includes("--check")) { console.log(`${out.length} cases checked`); process.exit(0); }
// Merge by id in Python so the file keeps json.dumps(indent=2, ensure_ascii=False) exactly.
execFileSync("python3", ["-I", "-c", `
import json,sys
f=sys.argv[1]; new=json.loads(sys.stdin.read())
d=json.load(open(f))
ids={c['id']:i for i,c in enumerate(d['cases'])}
for c in new:
    if c['id'] in ids: d['cases'][ids[c['id']]]=c
    else: d['cases'].append(c)
open(f,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\\n')
`, file], { input: JSON.stringify(out) });
console.log(`${out.length} cases written`);
