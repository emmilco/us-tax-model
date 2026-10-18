// Data-level properties (spec 6.3), checked over generated returns with
// fast-check. Each property states what must hold for every input; a failure
// is reported with the shrunk counterexample and fails the run. The report
// also records how often each property applied, so a property that never
// applies cannot pass silently.
import fc from "fast-check";
import { mkdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { evaluate, evaluateAll } from "./eval.js";
import type { EvalResult, Value } from "./eval.js";
import { returnArbitrary, sampleReturns } from "./generate.js";
import { branchKeys } from "./branches.js";
import type { CanonicalData, Expr, Inputs, TestExpr } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const SEED = 7;
const RUNS = Number(process.env["PROPERTY_RUNS"] ?? 400);

interface Verdict { applicable: boolean; ok: boolean; detail?: string }

interface PropertyResult {
  id: string;
  statement: string;
  runs: number;
  applicable: number;
  observations: string[];
  failure?: { detail: string; inputs: unknown };
}

function cents(v: Value | undefined): number | null { return v && v.kind === "money" ? v.cents : null; }
function same(a: Value | undefined, b: Value | undefined): boolean {
  if (!a || !b) return a === b;
  if (a.kind !== b.kind) return false;
  if (a.kind === "money") return a.cents === (b as { cents: number }).cents;
  if (a.kind === "refusal") return a.gate === (b as { gate: string }).gate;
  if (a.kind === "unknown") return true;
  return JSON.stringify(a) === JSON.stringify(b);
}
function money(v: Value | undefined): string { const c = cents(v); return c === null ? (v?.kind ?? "absent") : (c / 100).toFixed(2); }

/** Deep copy of the data with one document's lines rewritten. */
function variant(data: CanonicalData, docId: string, rewrite: (lineId: string, expr: Expr) => Expr | null): { data: CanonicalData; rewritten: string[] } {
  const copy = structuredClone(data);
  const doc = copy.forms.find((d) => d.id === docId);
  if (!doc) throw new Error(`variant: no document ${docId}`);
  const rewritten: string[] = [];
  for (const line of doc.lines) {
    const next = rewrite(line.id, line.expr as Expr);
    if (next) { line.expr = next; rewritten.push(line.id); }
  }
  return { data: copy, rewritten };
}

function topRate(data: CanonicalData): { num: number; den: number } {
  const schedule = data.tables.find((t) => t.kind === "bracket_schedule");
  let best = { num: 0, den: 1 };
  for (const rows of Object.values(schedule?.schedules ?? {})) for (const r of rows) if (r.rate.num * best.den > best.num * r.rate.den) best = r.rate;
  return best;
}

/** Run one property over the corpus; on failure, shrink with fast-check for the smallest counterexample. */
function runProperty<T>(id: string, statement: string, arb: fc.Arbitrary<T>, check: (t: T) => Verdict, observations: string[] = []): PropertyResult {
  const result: PropertyResult = { id, statement, runs: 0, applicable: 0, observations };
  const sample = fc.sample(arb, { seed: SEED, numRuns: RUNS });
  let failed = false;
  for (const t of sample) {
    result.runs++;
    const v = check(t);
    if (v.applicable) result.applicable++;
    if (!v.ok) { failed = true; break; }
  }
  if (failed) {
    const details = fc.check(fc.property(arb, (t) => check(t).ok), { seed: SEED, numRuns: RUNS });
    const ce = details.counterexample ? details.counterexample[0] : sample[result.runs - 1]!;
    result.failure = { detail: check(ce).detail ?? "property returned false", inputs: ce };
  }
  return result;
}

export function runProperties(): number {
  const data = loadCanonical();
  const arb = returnArbitrary(data);
  const results: PropertyResult[] = [];

  // 1. Schedule D Tax Worksheet skip rule. The project encodes each skipped
  // line as its own zero; the reading that computes every line unconditionally
  // (the second transcription's) must give the same tax, and the component
  // lines that feed line 45 must be zero whenever they are skipped.
  {
    const skipped = new Map<string, number>(); // gated line -> index of the zero alternative
    const sdtw = variant(data, "sdtw", (id, expr) => {
      if (expr.op !== "choose" || expr.alternatives.length !== 2) return null;
      const zero = expr.alternatives.findIndex((a) => a.then === "sdtw.zero");
      const raw = expr.alternatives.find((a) => typeof a.then === "string" && a.then.startsWith("sdtw.raw"));
      if (zero < 0 || !raw) return null;
      skipped.set(id, zero);
      return { op: "copy", from: raw.then as string };
    });
    const components = ["sdtw.line30", "sdtw.line31", "sdtw.line33", "sdtw.line34", "sdtw.line39", "sdtw.line40", "sdtw.line42", "sdtw.line43"];
    const outputs = ["sdtw.line45", "sdtw.line47", "f1040.line16"];
    const targets = [...data.forms.find((d) => d.id === "sdtw")!.lines.map((l) => l.id), "f1040.line16"];
    const counts = { routed: 0, after22: 0, after32only: 0, no1250: 0, no28: 0 };
    const obs: string[] = [];
    const r = runProperty("sdtw_skip_rule", "Computing lines 23–43 of the Schedule D Tax Worksheet unconditionally gives the same lines 45, 47 and Form 1040 line 16 as skipping them, and every skipped component of line 41 and line 45 is zero when computed anyway.", arb, (inputs) => {
      const project = evaluate(data, inputs, targets);
      const line47 = project.derivations.get("sdtw.line47")?.value;
      if (!line47 || line47.kind !== "money") return { applicable: false, ok: true };
      const uncond = evaluate(sdtw.data, inputs, targets);
      const gate = project.derivations.get("f1040.line16")?.notes.some((n) => n.includes("sdtw")) ?? false;
      if (gate) counts.routed++;
      const bool = (id: string) => { const v = project.derivations.get(id)?.value; return v?.kind === "bool" ? v.value : null; };
      if (bool("sdtw.after22") === false) counts.after22++;
      if (bool("sdtw.after22") === true && bool("sdtw.after32") === false) counts.after32only++;
      if (bool("sdtw.after32") === true && bool("sdtw.use1250") === false) counts.no1250++;
      if (bool("sdtw.after32") === true && bool("sdtw.use28") === false) counts.no28++;
      for (const id of outputs) {
        if (!same(project.derivations.get(id)?.value, uncond.derivations.get(id)?.value))
          return { applicable: true, ok: false, detail: `${id}: skipping gives ${money(project.derivations.get(id)?.value)}, computing unconditionally gives ${money(uncond.derivations.get(id)?.value)}` };
      }
      for (const id of components) {
        const der = project.derivations.get(id);
        if (!der || der.takenGuardIndex !== skipped.get(id)) continue;
        const u = cents(uncond.derivations.get(id)?.value);
        if (u !== 0) return { applicable: true, ok: false, detail: `${id} is skipped but computes to ${money(uncond.derivations.get(id)?.value)} unconditionally` };
      }
      return { applicable: true, ok: true };
    }, obs);
    obs.push(`Rewritten lines (skip rule removed in the variant): ${sdtw.rewritten.length} — ${sdtw.rewritten.map((l) => l.replace("sdtw.line", "")).join(", ")}.`);
    obs.push(`Cases where Form 1040 line 16 came from this worksheet: ${counts.routed}. Cases with lines 1 and 16 equal (lines 23–43 skipped): ${counts.after22}; lines 1 and 32 equal with lines 1 and 16 different (lines 33–43 skipped): ${counts.after32only}; Schedule D line 19 zero after line 32 (lines 35–40 skipped): ${counts.no1250}; lines 41–43 skipped after line 32: ${counts.no28}.`);
    if (sdtw.rewritten.length === 0) r.failure = { detail: "no skip-gated lines found in sdtw; the property no longer matches the data", inputs: null };
    results.push(r);
  }

  // 2. Tax is non-negative, never exceeds the top rate on taxable income, and
  // the selected method never exceeds the ordinary computation.
  {
    const rate = topRate(data);
    const targets = ["f1040.line15", "f1040.line16", "sdtw.line46"];
    results.push(runProperty("tax_bounds", `Form 1040 line 16 is non-negative, at most the top rate (${rate.num}/${rate.den}) on taxable income plus one Tax Table band ($50), and at most the tax on all taxable income from the Tax Table or Tax Computation Worksheet.`, arb, (inputs) => {
      const r = evaluate(data, inputs, targets);
      const tax = cents(r.derivations.get("f1040.line16")?.value);
      const ti = cents(r.derivations.get("f1040.line15")?.value);
      const ordinary = cents(r.derivations.get("sdtw.line46")?.value);
      if (tax === null || ti === null || ordinary === null) return { applicable: false, ok: true };
      if (tax < 0) return { applicable: true, ok: false, detail: `line 16 is ${money(r.derivations.get("f1040.line16")?.value)}` };
      const bound = Math.ceil((ti + 5000) * rate.num / rate.den);
      if (tax > bound) return { applicable: true, ok: false, detail: `line 16 ${tax} cents exceeds ${bound} cents on taxable income ${ti}` };
      if (tax > ordinary) return { applicable: true, ok: false, detail: `line 16 ${tax} cents exceeds the ordinary computation ${ordinary} cents` };
      return { applicable: true, ok: true };
    }));
  }

  // 3. The standard-or-itemized choice never selects the larger tax. The
  // variant itemizes exactly when elected, so forcing the election either way
  // gives the two alternatives; the project's choice must not exceed either.
  {
    const sa = variant(data, "sa", (id) => id === "sa.itemizes" ? ({ op: "test", eq: ["sa.elect_itemize", { const: true }] } as TestExpr) : null);
    const targets = ["f1040.line16", "f1040.line24", "sa.mfs_spouse_itemizes"];
    let worseTotal = 0;
    const obs: string[] = [];
    const r = runProperty("deduction_choice", "With no election to itemize and no spouse itemizing, Form 1040 line 16 under the project's standard-or-itemized choice is at most line 16 under either deduction forced.", arb, (inputs) => {
      const base = { ...inputs, "sa.elect_itemize": false };
      const project = evaluate(data, base, targets);
      const mfs = project.derivations.get("sa.mfs_spouse_itemizes")?.value;
      const tax = cents(project.derivations.get("f1040.line16")?.value);
      if (tax === null || mfs?.kind !== "bool" || mfs.value) return { applicable: false, ok: true };
      const standard = evaluate(sa.data, base, targets);
      const itemized = evaluate(sa.data, { ...base, "sa.elect_itemize": true }, targets);
      const s = cents(standard.derivations.get("f1040.line16")?.value);
      const i = cents(itemized.derivations.get("f1040.line16")?.value);
      if (s === null || i === null) return { applicable: false, ok: true };
      const total = cents(project.derivations.get("f1040.line24")?.value);
      const st = cents(standard.derivations.get("f1040.line24")?.value);
      const it = cents(itemized.derivations.get("f1040.line24")?.value);
      if (total !== null && st !== null && it !== null && total > Math.min(st, it)) worseTotal++;
      if (tax > Math.min(s, i)) return { applicable: true, ok: false, detail: `project line 16 ${tax} cents; standard ${s}; itemized ${i}` };
      return { applicable: true, ok: true };
    }, obs);
    obs.push(`Cases where total tax (line 24) under the project's choice exceeded the better alternative: ${worseTotal}.`);
    if (sa.rewritten.length !== 1) r.failure = { detail: "sa.itemizes not found; the property no longer matches the data", inputs: null };
    results.push(r);
  }

  // 4. A refusal never becomes a number: a line whose evaluated operands
  // include a refusal is itself a refusal.
  results.push(runProperty("refusal_propagates", "No line computes a value from an operand that is a refusal; every line evaluated from a refused operand is a refusal.", arb, (inputs) => {
    const r = evaluateAll(data, inputs);
    let anyRefusal = false;
    for (const der of r.derivations.values()) {
      if (der.value.kind === "refusal") anyRefusal = true;
      const fromRefusal = der.operands.some((o) => o.value.kind === "refusal") || der.guardsNotTaken.some((g) => g.value.kind === "refusal");
      if (fromRefusal && der.value.kind !== "refusal") return { applicable: true, ok: false, detail: `${der.line} (${der.op}) has value ${der.value.kind} from a refused operand` };
    }
    return { applicable: anyRefusal, ok: true };
  }));

  // 5. Tax does not decrease as wages rise, other inputs fixed. Raising box 1
  // of the first W-2 raises ordinary income without changing the method gates.
  {
    let worseTotal = 0;
    const obs: string[] = [];
    const targets = ["f1040.line16", "f1040.line24"];
    const r = runProperty("tax_monotone", "Raising W-2 box 1 of the first employer, all else fixed, never lowers Form 1040 line 16.", fc.tuple(arb, fc.integer({ min: 1, max: 5_000_000 })), ([inputs, delta]) => {
      const roster = inputs["$w2@person[taxpayer]"] as string[];
      const key = `person[taxpayer].w2[${roster[0]}].box1`;
      const more = { ...inputs, [key]: (inputs[key] as number) + delta };
      const a = evaluate(data, inputs, targets);
      const b = evaluate(data, more, targets);
      const ta = cents(a.derivations.get("f1040.line16")?.value);
      const tb = cents(b.derivations.get("f1040.line16")?.value);
      if (ta === null || tb === null) return { applicable: false, ok: true };
      const xa = cents(a.derivations.get("f1040.line24")?.value);
      const xb = cents(b.derivations.get("f1040.line24")?.value);
      if (xa !== null && xb !== null && xb < xa) worseTotal++;
      if (tb < ta) return { applicable: true, ok: false, detail: `line 16 falls from ${ta} to ${tb} cents when ${key} rises by ${delta} cents` };
      return { applicable: true, ok: true };
    }, obs);
    obs.push(`Cases where total tax (line 24) fell as wages rose: ${worseTotal}.`);
    results.push(r);
  }

  // 6. Within one computation method: the Qualified Dividends and Capital Gain
  // Tax Worksheet's tax (line 25) and the Schedule D Tax Worksheet's tax (line
  // 47) each do not decrease as wages rise, all else fixed. Both are evaluated
  // directly, whichever method Form 1040 line 16 uses.
  {
    const counts = { qdcg: 0, sdtw: 0 };
    const obs: string[] = [];
    const targets = ["qdcg.line25", "sdtw.line47"];
    const r = runProperty("tax_monotone_by_method", "Raising W-2 box 1 of the first employer, all else fixed, never lowers the Qualified Dividends and Capital Gain Tax Worksheet line 25 or the Schedule D Tax Worksheet line 47, each where it is computed on both returns.", fc.tuple(arb, fc.integer({ min: 1, max: 5_000_000 })), ([inputs, delta]) => {
      const roster = inputs["$w2@person[taxpayer]"] as string[];
      const key = `person[taxpayer].w2[${roster[0]}].box1`;
      const more = { ...inputs, [key]: (inputs[key] as number) + delta };
      const a = evaluate(data, inputs, targets);
      const b = evaluate(data, more, targets);
      let applicable = false;
      for (const [id, k] of [["qdcg.line25", "qdcg"], ["sdtw.line47", "sdtw"]] as const) {
        const ta = cents(a.derivations.get(id)?.value);
        const tb = cents(b.derivations.get(id)?.value);
        if (ta === null || tb === null) continue;
        applicable = true; counts[k]++;
        if (tb < ta) return { applicable: true, ok: false, detail: `${id} falls from ${ta} to ${tb} cents when ${key} rises by ${delta} cents` };
      }
      return { applicable, ok: true };
    }, obs);
    obs.push(`Cases compared: QDCG worksheet line 25 ${counts.qdcg}, Schedule D Tax Worksheet line 47 ${counts.sdtw}.`);
    results.push(r);
  }

  // Branch coverage of the generated corpus: which choose guards and
  // arithmetic sides the generator reaches. Informational; feeds class M.
  const corpus = sampleReturns(data, RUNS, SEED);
  const seen = new Map<string, number>();
  for (const inputs of corpus) {
    const r: EvalResult = evaluateAll(data, inputs);
    for (const der of r.derivations.values()) { const b = branchKeys(der); for (const k of [...b.sides, ...b.guards]) seen.set(k, (seen.get(k) ?? 0) + 1); }
  }
  const unreached: string[] = [];
  let total = 0;
  for (const doc of data.forms) for (const line of doc.lines) {
    const expr = line.expr as Expr;
    const keys: string[] = [];
    if (expr.op === "choose") expr.alternatives.forEach((_, i) => keys.push(`${line.id}#${i}`));
    if (line.type === "Bool") keys.push(`${line.id}:false`, `${line.id}:true`);
    if (expr.op === "subtract_floor0") keys.push(`${line.id}:floor`, `${line.id}:positive`);
    if (expr.op === "smaller_of" || expr.op === "larger_of") keys.push(`${line.id}:left`, `${line.id}:right`);
    for (const k of keys) { total++; if (!seen.has(k)) unreached.push(k); }
  }

  // Report.
  const failures = results.filter((r) => r.failure);
  const out: string[] = [];
  out.push("# Data-level properties", "");
  out.push(`Properties of spec 6.3 checked over ${RUNS} generated returns (fast-check, seed ${SEED}, every filing status). "Applicable" counts the cases where the property's premise held and its values were computed; a refusal or an unknown makes a case inapplicable. A failure is reported with the smallest counterexample fast-check found.`, "");
  out.push("| Property | Statement | Cases | Applicable | Result |", "| --- | --- | --- | --- | --- |");
  for (const r of results) out.push(`| ${r.id} | ${r.statement} | ${r.runs} | ${r.applicable} | ${r.failure ? "**FAIL**" : r.applicable === 0 ? "**never applicable**" : "holds"} |`);
  out.push("");
  for (const r of results) {
    if (r.observations.length === 0 && !r.failure) continue;
    out.push(`## ${r.id}`, "");
    for (const o of r.observations) out.push(`- ${o}`);
    if (r.failure) {
      out.push("", `**Counterexample:** ${r.failure.detail}`, "", "```json", JSON.stringify(r.failure.inputs, null, 1), "```");
    }
    out.push("");
  }
  out.push("## Branch coverage of the generated corpus", "");
  out.push(`${total - unreached.length} of ${total} branches (choose guards, Bool lines both ways, floor and positive sides of subtract_floor0, left and right of smaller_of and larger_of) reached by the ${corpus.length} generated returns. Unreached:`, "");
  for (const k of unreached) out.push(`- ${k}`);
  out.push("");
  mkdirSync(join(ROOT, "reports", "2025"), { recursive: true });
  writeFileSync(join(ROOT, "reports", "2025", "properties.md"), out.join("\n"));
  const neverApplicable = results.filter((r) => r.applicable === 0 && !r.failure);
  console.log(`properties: ${results.length} properties over ${RUNS} generated returns; ${failures.length} failing, ${neverApplicable.length} never applicable; branches reached ${total - unreached.length}/${total}`);
  for (const r of failures) console.log(`  FAIL ${r.id}: ${r.failure!.detail}`);
  for (const r of neverApplicable) console.log(`  NEVER APPLICABLE ${r.id}`);
  console.log("report: reports/2025/properties.md");
  return failures.length + neverApplicable.length === 0 ? 0 : 1;
}
