// usage: node trace.mjs <repo> <witnesses.json>   witnesses: [{template, cls: "out"|"random"|"unread"|"early", seed, i}]
// For each witness: finds a state at which the template's input is reachable and unanswered (bank-order walk for out and
// unread; the tool's random traversals for random and early), and prints the "frontier" lines there: lines one of whose
// operands is unknown for want of that input while the line itself is decided, or is unknown for want of another input,
// or has operands waiting on two or more different inputs. Those are the lines that read the input past another operand.
import { pathToFileURL } from "node:url";
import { readFileSync } from "node:fs";
const [repo, file] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js"); const gen = await imp("generate.js");
const { interviewStatus, questionTemplate, inputMeta } = await imp("interview.js");
const { evaluate } = await imp("eval.js");
const { data, configs } = ir.loadContext(); const config = configs.full;
const wit = JSON.parse(readFileSync(file, "utf8"));
const cache = new Map();
const returnsOf = (seed, n) => { const k = `${seed}`; if (!cache.has(k) || cache.get(k).length < n) cache.set(k, gen.sampleReturns(data, n, seed)); return cache.get(k); };
const tmplOfLine = (id) => id.replace(/\[[^\]]*\]/g, "").split(".").slice(-2).join(".");
function frontier(current, key) {
  const ders = evaluate(data, current, config.targets).derivations;
  const out = [];
  for (const [id, d] of ders) {
    const ops = d.operands ?? [];
    const onX = ops.filter((o) => o.value.kind === "unknown" && o.value.input === key);
    if (!onX.length || d.op === "input") continue;
    const others = [...new Set(ops.filter((o) => o.value.kind === "unknown" && o.value.input && o.value.input !== key).map((o) => o.value.input))];
    const decided = d.value.kind !== "unknown";
    const viaOther = d.value.kind === "unknown" && d.value.input !== key;
    if (decided || viaOther || others.length) out.push({ line: id, op: d.op, value: d.value.kind === "unknown" ? `unknown(${d.value.input ?? d.value.reason})` : JSON.stringify(d.value), reads: onX.map((o) => o.ref), alsoWaiting: others, operands: ops.map((o) => `${o.ref}=${o.value.kind === "unknown" ? "?" + (o.value.input ?? "") : o.value.kind === "bool" ? o.value.value : o.value.kind === "money" ? o.value.cents : o.value.kind === "count" ? o.value.value : o.value.kind === "enum" ? o.value.value : o.value.kind}`) });
  }
  return out;
}
for (const w of wit) {
  const inputs = returnsOf(w.seed, 50)[w.i];
  const c = { id: `s${w.seed}.${w.i}`, inputs };
  const r = ir.runTask({ data, configs }, { kind: "walk", profile: "full", c });
  const res = { ...w, found: false };
  const match = (k) => questionTemplate(k).endsWith(w.template) || tmplOfLine(k) === w.template;
  if (w.cls === "out" || w.cls === "unread") {
    // replay the bank-order walk state by state
    let current = structuredClone(config.initial);
    for (let n = 0; n <= r.w.events.length && !res.found; n++) {
      const st = interviewStatus(data, config, current);
      const keys = st.reachableInputs.filter((k) => !(k in current) && match(k));
      const want = w.cls === "out" ? keys.filter((k) => k in r.classes.outOfOrder) : keys.filter((k) => r.classes.askedUnread.includes(k));
      if (want.length) { res.found = true; res.key = want[0]; res.state = n; res.hiddenBy = r.classes.outOfOrder[want[0]]; res.frontier = frontier(current, want[0]); res.next = r.w.events[n]?.input; }
      const e = r.w.events[n]; if (e) current = { ...current, [e.input]: e.value };
    }
    if (w.cls === "unread" && res.found) {
      // the state at completion: which decided lines made it moot
      const ders = evaluate(data, r.w.inputs, config.targets).derivations;
      res.readAtEnd = ders.has(res.key);
    }
  } else {
    const given = (await imp("interview.js")).replay(config, [{ version: 1, tax_year: config.tax_year }, ...r.w.events]);
    const rng = (seed) => { let a = seed >>> 0; return () => { a = (a + 0x6d2b79f5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
    for (let s = 0; s < 5 && !res.found; s++) {
      const rand = rng(w.seed * 1000 + w.i + s * 100003);
      let last = null, lastKey = null;
      const answers = (k, current) => { if (k in given) return { value: given[k] }; if (w.cls === "random" && !res.found && match(k)) { res.found = true; res.key = k; res.traversal = s; res.frontier = frontier(current, k); } return undefined; };
      try {
        ir.walk(data, config, answers, (open, current) => { last = current; lastKey = open[Math.floor(rand() * open.length)]; return lastKey; }, 800, (reach) => {
          if (w.cls !== "early" || res.found) return;
          const keys = reach.filter(match); if (!keys.length) return;
          const current = { ...last, [lastKey]: given[lastKey] };
          res.found = true; res.key = keys[0]; res.traversal = s; res.frontier = frontier(current, keys[0]);
          // Probe: does any answer to the input left reachable change the status or a target value of this "complete" state?
          const meta = inputMeta(data, keys[0]);
          const cands = meta.type === "Bool" ? [true, false] : meta.type === "Enum" ? meta.values : [0, 1, 100000, 10000000, 100000000];
          const before = ir.targetKey(data, config, current);
          res.probe = cands.map((v) => { const st = interviewStatus(data, config, { ...current, [keys[0]]: v }); return { v, status: st.status, gate: st.refusal ? (st.refusal.gate ?? st.refusal.form ?? "refusal") : null, sameValues: ir.targetKey(data, config, { ...current, [keys[0]]: v }) === before }; });
          res.others = reach.filter((k) => k !== keys[0]);
        }, () => {});
      } catch (e) { res.error = String(e); }
    }
  }
  console.log(JSON.stringify(res));
}
