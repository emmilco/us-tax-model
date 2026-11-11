// usage: node differential.mjs <base repo> <patched repo> <n> <seed> : status and target values of n generated federal
// returns (every answer stated) and of every federal and New York fixture's inputs, base against patched
import { pathToFileURL } from "node:url";
const [A, B, nS, seedS] = process.argv.slice(2);
const load = async (repo) => { const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href); const ir = await imp("interview-rules.js"); const gen = await imp("generate.js"); const { interviewStatus } = await imp("interview.js"); const fx = await imp("fixture-inputs.js"); return { ir, gen, interviewStatus, fx, ctx: ir.loadContext() }; };
const a = await load(A), b = await load(B);
const key = (m, profile, inputs) => { const config = m.ctx.configs[profile]; return m.interviewStatus(m.ctx.data, config, inputs).status + "|" + m.ir.targetKey(m.ctx.data, config, inputs); };
const rs = a.gen.sampleReturns(a.ctx.data, Number(nS), Number(seedS));
let diff = 0, complete = 0; const first = [];
rs.forEach((inputs, i) => { const x = key(a, "full", inputs), y = key(b, "full", inputs); if (x.startsWith("complete")) complete++; if (x !== y) { diff++; if (first.length < 5) first.push(`generated ${seedS}.${i}: ${x.split("|")[0]} -> ${y.split("|")[0]}`); } });
console.log(`generated returns (seed ${seedS}): ${rs.length} compared, ${complete} complete on base, ${diff} differ ${first.join("; ")}`);
for (const [j, profile] of [["us", "full"], ["ny", "ny"]]) {
  let n = 0, d = 0; const ex = [];
  let cases; try { cases = a.fx.loadFixtureCases(j === "us" ? "federal" : "ny", a.ctx.data); } catch (e) { console.log(`fixtures ${j}: not loaded (${String(e).slice(0, 120)})`); continue; }
  for (const c of cases) { n++; const x = key(a, profile, c.inputs), y = key(b, profile, c.inputs); if (x !== y) { d++; if (ex.length < 8) ex.push(`${c.id}: ${x.split("|")[0]} -> ${y.split("|")[0]}`); } }
  console.log(`fixtures ${j} (inputs evaluated on the ${profile} profile's targets): ${n} compared, ${d} differ ${ex.join("; ")}`);
}
