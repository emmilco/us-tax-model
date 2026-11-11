// usage: node collections.mjs <repo> [flip] > out.jsonl
// Prototype of "minimal returns with one entry per collection": the tool's minimal return (every answer closed), with
// each roster the closed walk asks given one entry, alone (rosters nested under that entry are given one entry too).
// With `flip`, also each such return with one Bool or enum answer of the entry given another value, alone. Each return is
// walked in bank order and in 3 random orders with the tool's own walk; prints the reach and early-completion
// templates per return, and the time.
import { pathToFileURL } from "node:url";
const [repo, flip] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js");
const { questionTemplate, inputMeta } = await imp("interview.js");
const { data, configs } = ir.loadContext(); const config = configs.full;
const closed = ir.minimalAnswers(data, config, "full", null);
const T = (ks) => [...new Set(ks.map(questionTemplate))].sort();
const fallback = (key) => { if (key.startsWith("$")) return []; const m = inputMeta(data, key); return m.type === "Bool" ? false : m.type === "Enum" ? m.values[0] : 0; };
const rng = (seed) => { let a = seed >>> 0; return () => { a = (a + 0x6d2b79f5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
function answersFor(roster, over) {
  return (key, current) => {
    if (key in over) return { value: over[key] };
    if (key.startsWith("$")) {
      const t = questionTemplate(key);
      if (t === "$person") return { value: ["taxpayer"] };
      if (t === roster || key.includes("[e1]")) return { value: ["e1"] };
      return { value: [] };
    }
    return closed(key, current) ?? { value: fallback(key) };
  };
}
function run(id, answers) {
  const t0 = performance.now();
  const row = { id };
  try {
    const leaks = [];
    const w = ir.walk(data, config, answers, ir.bankOrder(config), 800, (r) => leaks.push(...r));
    row.status = w.status; row.asked = w.events.length; row.early = T(leaks);
    if (w.status === "complete") {
      const read = ir.readInputs(data, config, w.inputs); const asked = new Set(w.events.map((e) => e.input));
      row.unread = T([...asked].filter((k) => !read.has(k))); row.out = T(Object.keys(w.exposed).filter((k) => !asked.has(k)));
      const given = Object.fromEntries(w.events.map((e) => [e.input, e.value])); const reached = new Set(); const early = [];
      for (let s = 0; s < 3; s++) {
        const rand = rng(11000 + s * 100003);
        try { const r = ir.walk(data, config, (k) => (k in given ? { value: given[k] } : undefined), (open) => open[Math.floor(rand() * open.length)], 800, (x) => early.push(...x), (k) => reached.add(k)); if (r.status !== w.status || r.valuesKey !== w.valuesKey) row.orderError = true; } catch (e) { row.randomError = String(e).slice(0, 200); }
      }
      row.reached = T([...reached]); row.randomEarly = T(early);
    }
    row.events = w.events;
  } catch (e) { row.error = String(e).slice(0, 200); }
  row.ms = Math.round(performance.now() - t0);
  return row;
}
const t0 = performance.now();
const base = run("closed", answersFor(null, {}));
const rosters = T((base.events ?? []).filter((e) => e.input.startsWith("$")).map((e) => e.input)).filter((r) => r !== "$person");
let n = 0;
const print = (row) => { n++; const { events, ...rest } = row; console.log(JSON.stringify(rest)); };
print(base);
// rosters nested under an entry are found from the one-entry walks themselves
const seen = new Set(rosters); const queue = [...rosters];
while (queue.length) {
  const roster = queue.shift();
  const row = run(`${roster}=one`, answersFor(roster, {}));
  print(row);
  for (const r of T((row.events ?? []).filter((e) => e.input.startsWith("$")).map((e) => e.input))) if (!seen.has(r) && r !== "$person") { seen.add(r); /* nested rosters are opened with their parent */ }
  if (!flip || !row.events) continue;
  for (const e of row.events) {
    if (!e.input.includes("[e1]") || e.input.startsWith("$")) continue;
    const m = inputMeta(data, e.input);
    const others = m.type === "Bool" ? [!e.value] : m.type === "Enum" ? m.values.filter((v) => v !== e.value) : m.type.includes("Dollars") ? [100000] : [];
    for (const v of others) print(run(`${roster}=one, ${questionTemplate(e.input)}=${JSON.stringify(v)}`, answersFor(roster, { [e.input]: v })));
  }
}
console.error(`${n} returns in ${((performance.now() - t0) / 1000).toFixed(1)} s (one thread); rosters opened: ${rosters.join(", ")}`);
