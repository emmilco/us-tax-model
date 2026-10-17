// Mutation tool: apply single-atom mutations to the Stage 1 data, run the
// checker and every fixture case against each mutant, and publish the
// mutation score with the surviving mutations listed.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { stableStringify } from "./util.js";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import { loadCases } from "./fixtures.js";
import { runChecks } from "./check.js";
import type { CanonicalData, Expr, FormDoc, Line } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const FIXTURES = join(ROOT, "fixtures", "2025", "stage1.json");

interface Mutation {
  id: string;
  kind: string;
  where: string;
  note?: string;
  apply: (data: CanonicalData) => void;
}

function cloneData(data: CanonicalData): CanonicalData {
  return JSON.parse(JSON.stringify(data)) as CanonicalData;
}

function allDocs(data: CanonicalData): FormDoc[] {
  return [...data.forms, ...data.defs];
}

function findLine(data: CanonicalData, id: string): Line | undefined {
  for (const doc of allDocs(data)) {
    const line = doc.lines.find((l) => l.id === id);
    if (line) return line;
  }
  return undefined;
}

function lineType(data: CanonicalData, doc: FormDoc, id: string): string | undefined {
  return doc.lines.find((l) => l.id === id)?.type;
}

function mutations(data: CanonicalData): Mutation[] {
  const out: Mutation[] = [];

  for (const doc of allDocs(data)) {
    doc.lines.forEach((line, idx) => {
      const expr = line.expr as Expr;
      const where = `${doc.id}.${line.id}`;

      if (expr.op === "sum_over" && expr.where) out.push({id:`filter.${where}`,kind:"remove collection filter",where,apply:d=>{const e=findLine(d,line.id)!.expr; if(e.op==="sum_over") delete e.where;}});
      for (let i=0;i<(line.refuses?.length??0);i++) out.push({id:`refusal.${where}.${i}`,kind:"remove refusal",where,apply:d=>{findLine(d,line.id)!.refuses!.splice(i,1);}});
      if (expr.op === "test" && "gt" in expr && expr.gt) out.push({id:`boundary.${where}`,kind:"replace strict greater-than with inclusive",where,apply:d=>{const e=findLine(d,line.id)!.expr as {op:"test";gt?:unknown;ge?:unknown};e.ge=e.gt;delete e.gt;}});
      if (expr.op === "smaller_of" || expr.op === "larger_of") {
        out.push({
          id: `minmax.${where}`,
          kind: "swap smaller_of/larger_of",
          where,
          apply: (d) => {
            const l = findLine(d, line.id)!;
            (l.expr as { op: string }).op = expr.op === "smaller_of" ? "larger_of" : "smaller_of";
          },
        });
      }
      if (expr.op === "round") {
        out.push({
          id: `roundrule.${where}`,
          kind: "change the rounding rule",
          where,
          apply: (d) => {
            const l = findLine(d, line.id)!;
            (l.expr as { rule: string }).rule = expr.rule === "up" ? "down" : "up";
          },
        });
      }
      if (expr.op === "subtract_floor0") {
        out.push({
          id: `floor.${where}`,
          kind: "drop the floor",
          where,
          apply: (d) => {
            const l = findLine(d, line.id)!;
            (l.expr as { op: string }).op = "subtract";
          },
        });
      }
      // Operand replacement: replace one referenced same-document line with the
      // nearest earlier same-typed line that the expression does not already use.
      const refs: string[] = [];
      if (expr.op === "sum" || expr.op === "smaller_of" || expr.op === "larger_of") refs.push(...expr.of);
      if (expr.op === "subtract" || expr.op === "subtract_floor0") {
        refs.push(expr.from);
        if (typeof expr.take === "string") refs.push(expr.take);
      }
      if (expr.op === "multiply_rate") refs.push(expr.amount);
      if (expr.op === "round") refs.push(expr.of);
      if (expr.op === "copy" && typeof expr.from === "string") refs.push(expr.from);
      for (const ref of refs) {
        if (!ref.startsWith(doc.id + ".")) continue; // same-document only
        const candidate = [...doc.lines]
          .slice(0, idx)
          .reverse()
          .find((l) => l.type === line.type && l.id !== ref && !refs.includes(l.id) && l.expr.op !== "input");
        if (!candidate) continue;
        out.push({
          id: `operand.${where}.${ref.split(".").pop()}`,
          kind: "replace an operand",
          where,
          note: `${ref} -> ${candidate.id} (${candidate.type})`,
          apply: (d) => {
            const l = findLine(d, line.id)!;
            const e = l.expr as Expr & { of?: string[]; from?: string; take?: string | object; amount?: string };
            if (e.of) e.of = e.of.map((r) => (r === ref ? candidate.id : r));
            if (e.from === ref) e.from = candidate.id;
            if (e.take === ref) e.take = candidate.id;
            if (e.amount === ref) e.amount = candidate.id;
          },
        });
      }
    });
  }

  // Parameter shifts: money +$1 (100 cents); rates +1 percentage point.
  for (const [name, entry] of Object.entries(data.params.values)) {
    if (entry.type === "Rate") {
      out.push({
        id: `param.${name}.+1pt`,
        kind: "shift a rate parameter (+1 point)",
        where: name,
        apply: (d) => {
          const v = d.params.values[name]!.value as { num: number; den: number };
          v.num += 1;
        },
      });
    } else if (entry.type === "Dollars" || entry.type === "NonNegDollars") {
      out.push({
        id: `param.${name}.\$1`,
        kind: "shift a money parameter (+$1)",
        where: name,
        apply: (d) => {
          const e = d.params.values[name]!;
          if (typeof e.value === "number") {
            e.value += 100;
          } else {
            const m = e.value as Record<string, number>;
            for (const k of Object.keys(m)) m[k] = (m[k] ?? 0) + 100;
          }
        },
      });
    }
  }

  return out;
}

// Survivors that are provably equivalent mutants, with the reason. The score
// is reported raw and adjusted (equivalents excluded from the denominator).
const EQUIVALENT: Record<string, string> = {
  "operand.qdcg.qdcg.line8.line7":
    "Provably equivalent: line 8 is min(line 5, line 7) and line 7 is min(line 1, line 6) with line 5 ≤ line 1; " +
    "min(line 5, min(line 1, line 6)) = min(line 5, line 6), so substituting line 6 for line 7 cannot change any value.",
  "operand.qdcg.qdcg.line12.line11":
    "Provably equivalent: line 11 is 'Enter the amount from line 9' (a copy), so the substituted operand is the same value at every input.",
  "operand.sd.sd.line5.zero": "Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.",
  "operand.sd.sd.line6.zero": "Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.",
  "operand.sd.sd.line11.zero": "Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.",
  "operand.sd.sd.line12.zero": "Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.",
  "operand.sd.sd.line14.zero": "Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.",
  "operand.sd.sd.line7.line4": "Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.",
  "operand.sd.sd.line7.line5": "Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.",
  "operand.sd.sd.line7.line6": "Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.",
};

// Copy-chain equivalence is checked under the containing line's already-false
// refusal gates. This recognizes aliases, not numerical agreement on samples.
function aliasEquivalence(data: CanonicalData, mutation: Mutation): string | undefined {
  if (mutation.kind!=="replace an operand" || !mutation.note) return undefined;
  const match=/^(\S+) -> (\S+) /.exec(mutation.note);
  if(!match)return undefined;
  const parent=findLine(data,mutation.where.slice(mutation.where.indexOf(".")+1));
  if(!parent)return undefined;
  const known=new Set((parent.refuses??[]).map(r=>r.when));
  const normalize=(id:string, falseGates:Set<string>, seen:Set<string>):unknown=>{
    if(seen.has(id))return {cycle:id};
    const l=findLine(data,id);if(!l)return {unresolved:id};
    const next=new Set(seen);next.add(id);
    const guards=(l.refuses??[]).filter(r=>!falseGates.has(r.when));
    const context=new Set([...falseGates,...guards.map(r=>r.when)]);
    const expr=l.expr;
    const value=expr.op==="copy"&&typeof expr.from==="string" ? normalize(expr.from,context,next)
      : expr.op==="param" ? {parameter:data.params.values[expr.ref]?.value,type:l.type}
      : {line:id};
    return guards.length?{guards,value}:value;
  };
  if(stableStringify(normalize(match[1]!,known,new Set()))!==stableStringify(normalize(match[2]!,known,new Set())))return undefined;
  return `Copy-chain identity: ${match[1]} and ${match[2]} expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.`;
}

export function runMutation(): number {
  const baseline = loadCanonical();
  const fixtureFile = loadCases();
  const targets = baseline.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));

  const normal = (v: { kind: string; cents?: number; value?: unknown }): string =>
    v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}` : `${v.kind}:${JSON.stringify(v.value)}`;

  // A mismatching baseline must never make every mutant look killed.
  for (const c of fixtureFile.cases) {
    const result=evaluate(baseline,c.inputs,targets);
    for (const [key,expected] of Object.entries(c.expect ?? {})) {
      const actual=result.derivations.get(key)?.value;
      if (!actual || normal(actual)!==normal(expected)) throw new Error(`mutation baseline mismatch: ${c.id} ${key}`);
    }
  }
  const muts = mutations(baseline);
  const survivors: Mutation[] = [];
  let killedByCheck = 0;
  let killedByFixtures = 0;

  for (const m of muts) {
    const data = cloneData(baseline);
    m.apply(data);
    const check = runChecks(data);
    if (check.errors.length > 0) {
      killedByCheck++;
      continue;
    }
    let killed = false;
    for (const c of fixtureFile.cases) {
      const result = evaluate(data, c.inputs, targets);
      for (const [key, expected] of Object.entries(c.expect ?? {})) {
        const der = result.derivations.get(key);
        if (!der || normal(der.value) !== normal(expected)) {
          killed = true;
          break;
        }
      }
      if (killed) break;
    }
    if (killed) killedByFixtures++;
    else survivors.push(m);
  }

  const total = muts.length;
  const killed = killedByCheck + killedByFixtures;
  const score = total === 0 ? 0 : killed / total;
  for(const survivor of survivors) {
    const reason=aliasEquivalence(baseline,survivor);
    if(reason)EQUIVALENT[survivor.id]=reason;
  }
  const equivalentSurvivors = survivors.filter((s) => s.id in EQUIVALENT);
  const unexplained = survivors.filter((s) => !(s.id in EQUIVALENT));
  const adjusted = total - equivalentSurvivors.length === 0 ? 1 : killed / (total - equivalentSurvivors.length);

  const report: string[] = [];
  report.push("# Mutation score — implemented worksheets");
  report.push("");
  report.push("Single-atom mutations applied to the canonical data; a mutant is killed if the");
  report.push("build-time checker fails on it or if any fixture case's value changes. Fixture");
  report.push("expectations are the recorded values checked in the previous run (the same values");
  report.push("the fixture test compares).");
  report.push("");
  report.push("| Metric | Value |");
  report.push("| --- | --- |");
  report.push(`| Mutants | ${total} |`);
  report.push(`| Killed by the checker | ${killedByCheck} |`);
  report.push(`| Killed by fixtures | ${killedByFixtures} |`);
  report.push(`| Surviving | ${survivors.length} (${equivalentSurvivors.length} provably equivalent) |`);
  report.push(`| Mutation score (raw) | ${(score * 100).toFixed(1)}% |`);
  report.push(`| Mutation score (equivalent mutants excluded) | ${(adjusted * 100).toFixed(1)}% |`);
  report.push("");
  if (equivalentSurvivors.length > 0) {
    report.push("## Surviving — classified equivalent");
    report.push("");
    for (const s of equivalentSurvivors) {
      report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${EQUIVALENT[s.id]}`);
    }
    report.push("");
  }
  if (unexplained.length > 0) {
    report.push("## Surviving — not yet explained");
    report.push("");
    report.push("| Mutant | Kind | Location | Note |");
    report.push("| --- | --- | --- | --- |");
    for (const s of unexplained) {
      report.push(`| ${s.id} | ${s.kind} | ${s.where} | ${s.note ?? ""} |`);
    }
    report.push("");
  }
  const outDir = join(ROOT, "reports", "2025");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "mutation.md"), report.join("\n"));
  console.log(`mutation: ${total} mutants, killed by checker ${killedByCheck}, by fixtures ${killedByFixtures}, surviving ${survivors.length} (${equivalentSurvivors.length} equivalent; score ${(score * 100).toFixed(1)}%, adjusted ${(adjusted * 100).toFixed(1)}%)`);
  console.log(`report: reports/2025/mutation.md`);
  return unexplained.length === 0 ? 0 : 1;
}
