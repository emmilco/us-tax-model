// usage: node minimal.mjs <repo> <overrides.json> [random seeds]
// Walks the full profile in bank order answering each question from overrides.json, else with the tool's own
// "minimal return" closed answer (minimalAnswers, every gate closed). Prints the 1095-A/8962 questions asked, the
// tool's reach classes, and what random-order traversals reach.
import { pathToFileURL } from "node:url";
import { readFileSync } from "node:fs";
const [repo, file, nSeeds] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js");
const { interviewStatus, questionTemplate } = await imp("interview.js");
const { evaluate } = await imp("eval.js");
const { data, configs } = ir.loadContext();
const config = configs.full;
if (process.env.PLANT) {
  const doc = data.forms.find((f) => f.id === "f8962");
  const bz = doc.lines.find((l) => l.id === "f8962.b_zero");
  const no = doc.lines.find((l) => l.id === "f8962.no");
  console.log("planted: f8962.b_zero as a choose on f8962.show_applicable; f8962.no is", JSON.stringify(no.expr));
  const inner = bz.expr.all[1];
  doc.lines.push({ ...bz, id: "f8962.b_zero_months", expr: inner });
  const g = (v) => ({ op: "test", eq: ["f8962.show_applicable", { const: v }] });
  bz.expr = { op: "choose", alternatives: [{ guard: g(false), then: "f8962.no" }, { guard: g(true), then: "f8962.b_zero_months" }] };
}
const over = JSON.parse(readFileSync(file, "utf8"));
const closed = ir.minimalAnswers(data, config, "full", null);
const answers = (key, current) => (key in over ? { value: over[key] } : closed(key, current));
const leaks = [];
const w = ir.walk(data, config, answers, ir.bankOrder(config), 800, (r) => leaks.push(r));
console.log(`bank-order walk: ${w.status}, ${w.events.length} questions asked, early-completion leaks ${leaks.length}`);
const show = (k) => /f1095a|f8962/.test(k);
console.log("asked (1095-A / 8962), in order:"); for (const e of w.events) if (show(e.input)) console.log(`   ${e.input} = ${JSON.stringify(e.value)}`);
const read = ir.readInputs(data, config, w.inputs);
const asked = new Set(w.events.map((e) => e.input));
console.log("asked in bank order and unread by the complete return:", [...asked].filter((k) => !read.has(k)).sort().join(", ") || "none");
console.log("reachable before the answer that hides it, never asked in bank order:");
for (const [k, by] of Object.entries(w.exposed)) if (!asked.has(k)) console.log(`   ${k}, until ${by} was answered`);
const vals = evaluate(data, w.inputs, ["f8962.line5", "f8962.applicable", "f8962.aptc", "f8962.filing", "f8962.line10", "f8962.line24", "f8962.line26", "f8962.line29", "f8962.show_jan", "f1040.line11", "f1040.line37"]).values;
const want = new Set(["f8962.line5","f8962.applicable","f8962.aptc","f8962.filing","f8962.line10","f8962.line24","f8962.line26","f8962.line29","f8962.show_jan","f8962.show_dec","f1040.line11","f1040.line37"]);
for (const [k, v] of vals) if (want.has(k)) console.log(`   ${k}: ${JSON.stringify(v)}`);
let a = 1;
const rng = (seed) => () => { seed = (seed + 0x6d2b79f5) >>> 0; let t = seed; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
const given = Object.fromEntries(w.events.map((e) => [e.input, e.value]));
const reached = new Map();
for (let s = 0; s < Number(nSeeds ?? 5); s++) {
  const rand = rng(11000 + s * 100003);
  const r = ir.walk(data, config, (k) => (k in given ? { value: given[k] } : undefined), (open) => open[Math.floor(rand() * open.length)], 800, () => {}, (k) => reached.set(k, (reached.get(k) ?? 0) + 1));
  if (r.status !== w.status || r.valuesKey !== w.valuesKey) console.log(`   random order ${s}: different status or values`);
}
console.log(`random orders reach, beyond the bank-order questions: ${[...reached.keys()].sort().join(", ") || "none"}`);
