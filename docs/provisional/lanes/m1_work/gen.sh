#!/bin/bash
# Make engine/dist/_m1_mutate.js: the built mutate.js with its private helpers exported, and a runner limited to forms.
D=/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist
cp $D/mutate.js $D/_m1_mutate.js
cat >> $D/_m1_mutate.js <<'EOT'

export async function m1Run(forms, workers) {
  const baseline = loadCanonical();
  const all = selectMutants(mutations(baseline));
  const mine = all.filter((m) => forms.includes(m.where.split(".")[0]));
  const cases = judgingCases(baseline);
  const res = [];
  for (const m of mine) {
    const o = outcome(baseline, cases, m);
    res.push({ m, o });
  }
  const surv = res.filter((r) => r.o === "survives").map((r) => r.m);
  const survIds = new Set(surv.map((s) => s.id));
  const out = { total: mine.length, killed: res.filter(r=>r.o!=="survives").length, unexplained: [], equivalent: [] };
  for (const s of surv) {
    const reason = equivalenceReason(baseline, s);
    if (reason) out.equivalent.push(s.id);
    else out.unexplained.push(`${s.id} | ${s.kind} | ${s.note ?? ""}`);
  }
  // stale arguments about my forms: need the full survivor set only for my forms' ids
  const table = Object.fromEntries(Object.entries(EQUIVALENT_IF).filter(([id]) => mine.some(m=>m.id===id) || forms.some(f => id.split(".")[1] === f)));
  out.stale = staleEquivalences(table, new Set([...ANSWERED_ONLY].filter(id => id in table)), baseline, all, survIds);
  return out;
}
EOT
cat >> $D/_m1_mutate.js <<'EOT'
export function m1Probe(spec) {
  // spec: {inputs?: obj, base?: caseId, set?: obj, del?: [], show?: [keys], mutants?: [ids], expect?: obj}
  const baseline = loadCanonical();
  let inputs = spec.inputs;
  if (!inputs) {
    const [file, cid] = spec.base.includes(":") ? spec.base.split(":") : ["mutation.json", spec.base];
    const raw = loadFixtureCases("federal", baseline).find((c) => c.file === file && c.id === cid);
    if (!raw) throw new Error("no base " + spec.base);
    inputs = { ...raw.inputs };
  }
  for (const k of spec.del ?? []) delete inputs[k];
  Object.assign(inputs, spec.set ?? {});
  const show = (data) => {
    const r = evaluate(data, inputs, allTargets(data, inputs));
    const o = {};
    for (const k of spec.show ?? []) { const v = r.derivations.get(k)?.value; o[k] = v ? normal(v) : "(none)"; }
    return o;
  };
  const unk = (data) => { const r = evaluate(data, inputs, allTargets(data, inputs)); let n = 0, rf = 0; for (const [k, d] of r.derivations) { if (d.value?.kind === "unknown") n++; if (d.value?.kind === "refusal") rf++; } return `${n} unknown, ${rf} refusals of ${r.derivations.size}`; };
  const out = { baseline: show(baseline), completeness: unk(baseline), mutants: {} };
  const muts = mutations(baseline);
  for (const id of spec.mutants ?? []) {
    const m = muts.find((x) => x.id === id);
    if (!m) { out.mutants[id] = "NO SUCH MUTANT"; continue; }
    const d = cloneData(baseline); m.apply(d);
    const s = show(d);
    out.mutants[id] = Object.fromEntries(Object.entries(s).filter(([k, v]) => v !== out.baseline[k]));
  }
  return { out, inputs };
}
EOT
cat >> $D/_m1_mutate.js <<'EOT'
export function m1Killers(ids) {
  const baseline = loadCanonical();
  const cases = judgingCases(baseline);
  const muts = mutations(baseline);
  const out = {};
  for (const id of ids) {
    const m = muts.find((x) => x.id === id);
    const data = cloneData(baseline); m.apply(data);
    if (runChecks(data).errors.length > 0) { out[id] = ["check"]; continue; }
    const k = [];
    for (const c of cases.all) {
      const result = evaluate(data, c.inputs, c.targets ?? allTargets(data, c.inputs));
      for (const [key, expected] of Object.entries(c.expect ?? {})) {
        const der = result.derivations.get(key);
        if (!der || normal(der.value) !== normal(expected)) { k.push(`${c.file}:${c.id} ${key} expected ${normal(expected)} got ${der ? normal(der.value) : "none"}`); break; }
      }
    }
    out[id] = k;
  }
  return out;
}
EOT
cat >> $D/_m1_mutate.js <<'EOT'
// Build each spec's inputs from its base (a case of any federal fixture file, with defaults resolved), check that the
// baseline gives every expected value, and that each named mutant changes at least one expected value.
export function m1Check(specs) {
  const baseline = loadCanonical();
  const all = loadFixtureCases("federal", baseline);
  const muts = mutations(baseline);
  const res = [];
  for (const s of specs) {
    const [file, cid] = s.base.includes(":") ? s.base.split(":") : ["mutation.json", s.base];
    const raw = all.find((c) => c.file === file && c.id === cid);
    if (!raw) { res.push({ id: s.id, error: "no base " + s.base }); continue; }
    const inputs = { ...raw.inputs };
    for (const k of s.del ?? []) { if (!(k in inputs)) res.push({ id: s.id, warn: "del of absent " + k }); delete inputs[k]; }
    Object.assign(inputs, s.set ?? {});
    const ev = (data) => { const r = evaluate(data, inputs, allTargets(data, inputs)); return Object.fromEntries(Object.keys(s.expect).map((k) => { const v = r.derivations.get(k)?.value; return [k, v ? normal(v) : "(none)"]; })); };
    const base = ev(baseline);
    const mismatch = Object.entries(s.expect).filter(([k, v]) => base[k] !== normal(v)).map(([k, v]) => `${k}: expected ${normal(v)} got ${base[k]}`);
    const kills = {};
    for (const id of s.kills ?? []) {
      const m = muts.find((x) => x.id === id);
      if (!m) { kills[id] = "NO SUCH MUTANT"; continue; }
      const d = cloneData(baseline); m.apply(d);
      if (runChecks(d).errors.length > 0) { kills[id] = "check"; continue; }
      const mv = ev(d);
      const diff = Object.keys(s.expect).filter((k) => mv[k] !== base[k]).map((k) => `${k} ${base[k]}->${mv[k]}`);
      kills[id] = diff.length ? diff.join("; ") : "SURVIVES";
    }
    res.push({ id: s.id, mismatch, kills, inputs });
  }
  return res;
}
EOT
cat >> $D/_m1_mutate.js <<'EOT'
export function m1Scan(keys, fileFilter) {
  const baseline = loadCanonical();
  const out = [];
  for (const c of loadFixtureCases("federal", baseline)) {
    if (fileFilter && !c.file.startsWith(fileFilter)) continue;
    if (c.evidence === "M") continue;
    const r = evaluate(baseline, c.inputs, allTargets(baseline, c.inputs));
    out.push([c.file + ":" + c.id, ...keys.map((k) => { const v = r.derivations.get(k)?.value; return v ? (v.kind === "money" ? "money:" + v.cents : v.kind === "bool" ? "bool:" + v.value : v.kind) : "-"; })]);
  }
  return out;
}
EOT
