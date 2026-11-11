// usage: node probe_all.mjs <repo> <returns.json>: at every state a random traversal reports complete with inputs still
// reachable, give each such input each candidate answer alone and record whether the status or any target value changes.
import { pathToFileURL } from "node:url";
import { readFileSync } from "node:fs";
const [repo, file] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js"); const gen = await imp("generate.js");
const { interviewStatus, questionTemplate, inputMeta, replay } = await imp("interview.js");
const { data, configs } = ir.loadContext(); const config = configs.full;
const rng = (seed) => { let a = seed >>> 0; return () => { a = (a + 0x6d2b79f5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
const agg = new Map(); let states = 0;
const bySeed = new Map(); for (const [s, i] of JSON.parse(readFileSync(file, "utf8"))) (bySeed.get(s) ?? bySeed.set(s, []).get(s)).push(i);
for (const [seed, idx] of bySeed) {
  const rs = gen.sampleReturns(data, Math.max(...idx) + 1, seed);
  for (const i of idx) {
    const c = { id: "x", inputs: rs[i] };
    const r = ir.runTask({ data, configs }, { kind: "walk", profile: "full", c });
    if (r.kind !== "walked") continue;
    const given = replay(config, [{ version: 1, tax_year: config.tax_year }, ...r.w.events]);
    for (let s = 0; s < 5; s++) {
      const rand = rng(seed * 1000 + i + s * 100003); let last = null, lastKey = null;
      try {
        ir.walk(data, config, (k) => (k in given ? { value: given[k] } : undefined), (open, current) => { last = current; lastKey = open[Math.floor(rand() * open.length)]; return lastKey; }, 800, (reach) => {
          const current = { ...last, [lastKey]: given[lastKey] }; states++;
          const before = ir.targetKey(data, config, current);
          for (const key of reach) {
            const meta = inputMeta(data, key);
            const cands = meta.type === "Bool" ? [true, false] : meta.type === "Enum" ? meta.values : [0, 1, 100000, 10000000, 100000000];
            const t = questionTemplate(key); const a = agg.get(t) ?? agg.set(t, { states: 0, refusing: 0, valueChanging: 0, gates: new Set(), example: null }).get(t);
            a.states++;
            let ref = false, val = false;
            for (const v of cands) { const st = interviewStatus(data, config, { ...current, [key]: v }); if (st.status === "refused") { ref = true; a.gates.add(questionTemplate(String(st.refusal?.gate ?? st.refusal?.form ?? "?"))); a.example ??= `${seed}.${i} ${key}=${JSON.stringify(v)}`; } else if (st.status === "complete" && ir.targetKey(data, config, { ...current, [key]: v }) !== before) val = true; }
            a.refusing += ref; a.valueChanging += val;
          }
        }, () => {});
      } catch (e) {}
    }
  }
}
console.log(`early-complete states probed: ${states}`);
for (const [t, a] of [...agg].sort()) console.log(`${t}: left reachable at ${a.states} state(s); an answer refuses at ${a.refusing}; an answer changes a value (still complete) at ${a.valueChanging}; gates ${[...a.gates].join(", ") || "-"}; e.g. ${a.example ?? "-"}`);
