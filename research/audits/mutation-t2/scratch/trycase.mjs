// Evaluate spec cases (not written to the repo) against the baseline and the mutants they list in "kills".
// usage: MUTATE_TIER=2 node /tmp/mut2/trycase.mjs <spec.json>
import { readFileSync, readdirSync } from "node:fs";
const ROOT = "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/agent-a6e970022fe3a8b6b/";
process.chdir(ROOT);
const { mutations } = await import(ROOT + "engine/dist/mutate.js");
const { loadCanonical } = await import(ROOT + "engine/dist/canonical.js");
const { evaluate, allTargets } = await import(ROOT + "engine/dist/eval.js");
const { resolveInputs } = await import(ROOT + "engine/dist/fixture-inputs.js");
const { stableStringify } = await import(ROOT + "engine/dist/util.js");
const normal = (v) => v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
  : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;
const corpus = new Map();
for (const f of readdirSync(ROOT + "fixtures/2025")) {
  if (!f.endsWith(".json")) continue;
  try { for (const c of JSON.parse(readFileSync(ROOT + "fixtures/2025/" + f, "utf8")).cases ?? []) corpus.set(c.id, c); } catch {}
}
const data = loadCanonical();
const muts = new Map(mutations(data).map((m) => [m.id, m]));
const specs = [].concat(JSON.parse(readFileSync(process.argv[2], "utf8")));
for (const s of specs) {
  const src = corpus.get(s.from);
  if (!src) { console.log("NO SOURCE CASE", s.from); continue; }
  let inputs = { ...src.inputs };
  for (const k of s.drop ?? []) delete inputs[k];
  for (const p of s.drop_prefix ?? []) for (const k of Object.keys(inputs)) if (k.startsWith(p)) delete inputs[k];
  Object.assign(inputs, s.set ?? {});
  try { inputs = resolveInputs(inputs, data.params, s.id); } catch (e) { console.log("INPUT ERROR", s.id, e.message); continue; }
  let r;
  try { r = evaluate(data, inputs, allTargets(data, inputs)); } catch (e) { console.log("EVAL ERROR", s.id, e.message); continue; }
  const bad = Object.entries(s.expect).filter(([k, e]) => { const d = r.derivations.get(k); return !d || normal(d.value) !== normal(e); });
  console.log(bad.length ? "MISMATCH" : "ok", s.id);
  for (const [k, e] of bad) console.log("   ", k, "expected", normal(e).slice(0, 80), "got", r.derivations.get(k) ? normal(r.derivations.get(k).value).slice(0, 200) : "NOT EVALUATED");
  for (const id of s.kills ?? []) {
    const m = muts.get(id); if (!m) { console.log("   no such mutant", id); continue; }
    const d2 = JSON.parse(JSON.stringify(data)); m.apply(d2);
    const r2 = evaluate(d2, inputs, allTargets(d2, inputs));
    const k = Object.entries(s.expect).filter(([k, e]) => { const d = r2.derivations.get(k); return !d || normal(d.value) !== normal(e); }).map(([k]) => k);
    console.log("   ", k.length ? "KILLS" : "does not kill", id, k.slice(0, 3).join(","));
  }
}
