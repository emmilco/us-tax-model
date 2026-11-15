// usage: node search.mjs <worktree> <ids.json> [--ny]   prints {caseId: [passing candidate combos]}
import { readFileSync } from "node:fs";
import { isDeepStrictEqual } from "node:util";
import { join } from "node:path";
const root = process.argv[2];
const ids = new Set(JSON.parse(readFileSync(process.argv[3], "utf8")));
const ny = process.argv.includes("--ny");
const { loadCanonical } = await import(join(root, "engine/dist/canonical.js"));
const fi = await import(join(root, "engine/dist/fixture-inputs.js"));
const { evaluateAll } = await import(join(root, "engine/dist/eval.js"));
const { resultToJson } = await import(join(root, "engine/dist/output.js"));
const data = loadCanonical();
const j = ny ? "ny" : "federal";
const dir = join(root, ny ? "fixtures/ny/2025" : "fixtures/2025");
const CANDS = [{y:1980},{y:1970},{y:1950},{y:1960,d:false},{y:1960,d:true},{y:1961,j:true,d:false},{y:1961,j:true,d:true},{y:2001,j:false},{y:2004},{y:2007,j:false},{y:2009},{y:2012},
  {y:2001,j:true},{y:2002,j:true},{y:2007,j:true},{y:2008,j:true},{y:1976,a:true},{y:1976,a:false},{y:2010,u:true},{y:2010,u:false}];
const NEW = ["birth_year","born_jan1","under16_at_year_end","age50_at_year_end","died_at_64"];
function keys(p, c) {
  const o = { [`person[${p}].birth_year`]: c.y };
  if ([1961,2001,2002,2007,2008].includes(c.y)) o[`person[${p}].born_jan1`] = c.j ?? false;
  if (c.y === 2010) o[`person[${p}].under16_at_year_end`] = c.u ?? true;
  if (c.y === 1976) o[`person[${p}].age50_at_year_end`] = c.a ?? false;
  if (c.y === 1960 || (c.y === 1961 && c.j)) o[`person[${p}].died_at_64`] = c.d ?? false;
  return o;
}
const out = {};
for (const f of fi.caseFiles(dir)) {
  const cases = JSON.parse(readFileSync(join(dir, f), "utf8")).cases;
  for (const c of cases) {
    if (!ids.has(c.id)) continue;
    const roster = Array.isArray(c.inputs["$person"]) ? c.inputs["$person"] : ["taxpayer"];
    const base = Object.fromEntries(Object.entries(c.inputs).filter(([k]) => !NEW.some((n) => /^person\[[^\]]+\]\./.test(k) && k.endsWith("." + n))));
    const combos = roster.length === 1 ? CANDS.map((a) => [a]) : CANDS.flatMap((a) => CANDS.map((b) => [a, b]));
    const pass = [];
    for (const combo of combos) {
      const inputs = { ...base };
      roster.slice(0, 2).forEach((p, i) => Object.assign(inputs, keys(p, combo[i])));
      let ok = true;
      try {
        const resolved = fi.resolveCase({ id: c.id, inputs }, f, data, j);
        const parsed = JSON.parse(resultToJson(evaluateAll(data, resolved)));
        for (const [k, e] of Object.entries(c.expect ?? {})) { const a = parsed.values[k]?.value; if (!a || !isDeepStrictEqual(a, e)) { ok = false; break; } }
      } catch (e) { ok = false; }
      if (ok) { pass.push(Object.fromEntries(roster.slice(0, 2).map((p, i) => [p, combo[i]]))); if (pass.length >= 40) break; }
    }
    out[c.id] = pass;
  }
}
console.log(JSON.stringify(out));
