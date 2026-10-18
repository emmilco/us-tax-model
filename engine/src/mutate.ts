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
      if (expr.op === "multiply_count") refs.push(expr.amount, expr.count);
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
            const e = l.expr as Expr & { of?: string[] | string; from?: string; take?: string | object; amount?: string; count?: string };
            if (Array.isArray(e.of)) e.of = e.of.map((r) => (r === ref ? candidate.id : r));
            else if (e.of === ref) e.of = candidate.id; // round takes one operand
            if (e.from === ref) e.from = candidate.id;
            if (e.take === ref) e.take = candidate.id;
            if (e.amount === ref) e.amount = candidate.id;
            if (e.count === ref) e.count = candidate.id;
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

// The copy-chain normal form of a line: copies are followed to a parameter or a computed
// line, and each refusal gate met on the way is kept unless it is already known false.
function normalizeChain(data: CanonicalData, id: string, falseGates: Set<string> = new Set(), seen: Set<string> = new Set()): unknown {
  if (seen.has(id)) return { cycle: id };
  const l = findLine(data, id); if (!l) return { unresolved: id };
  const next = new Set(seen); next.add(id);
  const guards = (l.refuses ?? []).filter((r) => !falseGates.has(r.when));
  const context = new Set([...falseGates, ...guards.map((r) => r.when)]);
  const expr = l.expr;
  const value = expr.op === "copy" && typeof expr.from === "string" ? normalizeChain(data, expr.from, context, next)
    : expr.op === "param" ? { parameter: data.params.values[expr.ref]?.value, type: l.type }
    : { line: id };
  return guards.length ? { guards, value } : value;
}

function stripGuards(n: unknown): unknown {
  return n !== null && typeof n === "object" && "guards" in n ? stripGuards((n as unknown as { value: unknown }).value) : n;
}

function gateWhens(n: unknown): string[] {
  if (n === null || typeof n !== "object" || !("guards" in n)) return [];
  const g = n as { guards: { when: string }[]; value: unknown };
  return [...g.guards.map((r) => r.when), ...gateWhens(g.value)];
}

function lineOf(mutation: Mutation): string {
  return mutation.where.slice(mutation.where.indexOf(".") + 1);
}

// Every line id an expression reads, in evaluation order (parameter references,
// collection names and constants are not lines).
function operandRefs(data: CanonicalData, expr: unknown): string[] {
  const ids = new Set(allDocs(data).flatMap((doc) => doc.lines.map((l) => l.id)));
  const out: string[] = [];
  const skip = new Set(["ref", "collection", "const", "cite", "type", "op", "unit", "rule", "source", "label"]);
  const walk = (node: unknown): void => {
    if (typeof node === "string") { if (ids.has(node)) out.push(node); return; }
    if (Array.isArray(node)) { for (const n of node) walk(n); return; }
    if (node !== null && typeof node === "object") for (const [k, v] of Object.entries(node)) if (!skip.has(k)) walk(v);
  };
  walk(expr);
  return out;
}

function readersOf(data: CanonicalData, id: string): string[] {
  return allDocs(data).flatMap((doc) => doc.lines.filter((l) => operandRefs(data, l.expr).includes(id)).map((l) => l.id));
}

// Copy-chain equivalence is checked under the containing line's already-false
// refusal gates. This recognizes aliases, not numerical agreement on samples.
function aliasEquivalence(data: CanonicalData, mutation: Mutation): string | undefined {
  if (mutation.kind!=="replace an operand" || !mutation.note) return undefined;
  const match=/^(\S+) -> (\S+) /.exec(mutation.note);
  if(!match)return undefined;
  const parent=findLine(data,lineOf(mutation));
  if(!parent)return undefined;
  const known=new Set((parent.refuses??[]).map(r=>r.when));
  if(stableStringify(normalizeChain(data,match[1]!,known))!==stableStringify(normalizeChain(data,match[2]!,known)))return undefined;
  return `Copy-chain identity: ${match[1]} and ${match[2]} expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.`;
}

// A sum operand that is a value behind refusal gates, replaced by the same value without
// them, cannot change the sum when every other gated operand of the sum carries the
// identical gates: whichever operand refuses, the refusal is the same object, and when
// none refuses the two operands are equal. Checked structurally on every run.
function sharedGateEquivalence(data: CanonicalData, mutation: Mutation): string | undefined {
  if (mutation.kind !== "replace an operand" || !mutation.note) return undefined;
  const match = /^(\S+) -> (\S+) /.exec(mutation.note);
  if (!match) return undefined;
  const [, x, y] = match as unknown as [string, string, string];
  const parent = findLine(data, lineOf(mutation));
  if (!parent || parent.expr.op !== "sum") return undefined;
  const known = new Set((parent.refuses ?? []).map((r) => r.when));
  const nx = normalizeChain(data, x, known); const ny = normalizeChain(data, y, known);
  if (stableStringify(nx) === stableStringify(ny)) return undefined; // an alias, not this rule
  if (stableStringify(stripGuards(nx)) !== stableStringify(ny)) return undefined;
  const others = (parent.expr.of as string[]).filter((o) => o !== x);
  const gated = others.filter((o) => gateWhens(normalizeChain(data, o, known)).length > 0);
  if (gated.length === 0) return undefined;
  if (!gated.every((o) => stableStringify(normalizeChain(data, o, known)) === stableStringify(nx))) return undefined;
  return `Shared-gate identity: ${x} and ${gated.join(", ")} are the same value behind the same refusal gates (${[...new Set(gateWhens(nx))].join(", ")}) with identical refusal text, and ${y} is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.`;
}

// Equivalences that need an argument about evaluation order or reachability. Each is
// accepted only while the structural facts it rests on hold in the current data; when
// they lapse, the mutant is reported as unexplained again.
const EQUIVALENT_IF: Record<string, { reason: string; holds: (data: CanonicalData) => boolean }> = {
  "operand.eic.eic.step5_line4.zero": {
    reason: "Step 5 line 4 keeps its own combat-pay refusal whatever it reads; the substituted line 2 is the same zero (a copy of eic.zero) carrying only the gate scope.other_income, and earned income adds line 3 (line 1 less line 2) before line 4, so when that gate is true line 3 has already refused with the same refusal. No value can change.",
    holds: (d) => {
      const l4 = findLine(d, "eic.step5_line4"), l2 = findLine(d, "eic.step5_line2"), l3 = findLine(d, "eic.step5_line3"), ei = findLine(d, "eic.earned_income");
      if (!l4 || !l2 || !l3 || !ei || l4.expr.op !== "copy" || l2.expr.op !== "copy" || l4.expr.from !== "eic.zero" || l2.expr.from !== "eic.zero") return false;
      if (l3.expr.op !== "subtract" || l3.expr.take !== "eic.step5_line2" || ei.expr.op !== "sum") return false;
      const of = ei.expr.of as string[];
      return of[0] === "eic.step5_line3" && of[1] === "eic.step5_line4" && (l2.refuses ?? []).every((r) => r.when === "scope.other_income");
    },
  },
  "refusal.eic.eic.step1_resident.0": agiFirst("scope.other_income", "eic.step1_resident", 0),
  "refusal.eic.eic.step5_line2.0": agiFirst("scope.other_income", "eic.step5_line2", 0),
  "refusal.eic.eic.step2_other.0": agiFirst("scope.schedule1", "eic.step2_other", 0),
  "refusal.eic.eic.step5_line1.0": agiFirst("scope.schedule1", "eic.step5_line1", 0),
  "param.eic.ws_threshold0.other.$1": thresholdAtPlateau("eic.ws_threshold0.other", ["eic_0"], 0),
  "param.eic.ws_threshold0.joint.$1": thresholdAtPlateau("eic.ws_threshold0.joint", ["eic_0"], 1),
  "param.eic.ws_threshold1.joint.$1": thresholdAtPlateau("eic.ws_threshold1.joint", ["eic_1", "eic_2", "eic_3"], 1),
  "operand.s8812.s8812.line13.clw_a5": {
    reason: "Credit Limit Worksheet A line 5 is line 3 less line 4, and line 4 is zero behind the same gate that line 2, an operand of line 3, carries. When the gate fires, line 3 already refuses and the subtraction returns its first operand's refusal; when it does not, line 4 is zero. Line 13 therefore reads the same value from line 5 as from line 3 on every input.",
    holds: (d) => {
      const a5 = findLine(d, "s8812.clw_a5"); const a3 = findLine(d, "s8812.clw_a3");
      if (!a5 || !a3 || a5.expr.op !== "subtract" || a5.expr.from !== "s8812.clw_a3" || a5.expr.take !== "s8812.clw_a4" || a3.expr.op !== "subtract") return false;
      const n4 = normalizeChain(d, "s8812.clw_a4");
      const whens = gateWhens(n4);
      const zero = stripGuards(n4) as { parameter?: unknown };
      if (whens.length === 0 || zero.parameter !== 0) return false;
      const carriers = [a3, findLine(d, a3.expr.from), typeof a3.expr.take === "string" ? findLine(d, a3.expr.take) : undefined];
      return whens.every((w) => carriers.some((l) => (l?.refuses ?? []).some((r) => r.when === w)));
    },
  },
  "refusal.retirement.retirement.amount_a.0": firstReadCarries("retirement.amount_a", 0, ["retirement.show_a", "retirement.has_rollover", "retirement.rolled"]),
  "refusal.retirement.retirement.amount_a.1": firstReadCarries("retirement.amount_a", 1, ["retirement.show_a", "retirement.has_rollover", "retirement.rolled"]),
  "refusal.ssb.ssb.line6.0": firstReadCarries("ssb.line6", 0, ["ssb.line5", "ssb.line3", "f1040.line8"], "ssb.line7"),
  "refusal.dependent.dependent.qualifying_relative.2": {
    reason: "The married gate on the qualifying-relative test duplicates, word for word, the married gate on the qualifying-child test. The qualifying-relative test is read only by qr_dependent, which is read only by claimed, whose any-test evaluates qc_dependent, and so qualifying_child, before qr_dependent; for a married person qualifying_child refuses first with the same refusal, so this gate never fires.",
    holds: (d) => {
      const qr = findLine(d, "dependent.qualifying_relative"); const qc = findLine(d, "dependent.qualifying_child");
      const entry = qr?.refuses?.[2];
      if (!qr || !qc || !entry || entry.when !== "dependent.married") return false;
      if (!(qc.refuses ?? []).some((r) => stableStringify(r) === stableStringify(entry))) return false;
      if (stableStringify(readersOf(d, "dependent.qualifying_relative")) !== stableStringify(["dependent.qr_dependent"])) return false;
      if (stableStringify(readersOf(d, "dependent.qr_dependent")) !== stableStringify(["dependent.claimed"])) return false;
      const claimed = findLine(d, "dependent.claimed"); const qcd = findLine(d, "dependent.qc_dependent");
      if (!claimed || !qcd || claimed.expr.op !== "test" || !("any" in claimed.expr) || qcd.expr.op !== "test" || !("all" in qcd.expr)) return false;
      return operandRefs(d, claimed.expr)[0] === "dependent.qc_dependent" && operandRefs(d, qcd.expr)[0] === "dependent.qualifying_child";
    },
  },
};

// A shifted parameter that no line of any form or definition reads cannot change a value;
// such parameters serve the cross-checks (for example the Rev. Proc. amounts behind the EIC
// Table check). Checked on every run against the current data.
function unreadParameter(data: CanonicalData, mutation: Mutation): string | undefined {
  if (!mutation.id.startsWith("param.")) return undefined;
  const name = mutation.where;
  const reads = (node: unknown): boolean => {
    if (Array.isArray(node)) return node.some(reads);
    if (node === null || typeof node !== "object") return false;
    const o = node as Record<string, unknown>;
    if (o["param"] === name || (o["op"] === "param" && o["ref"] === name)) return true;
    return Object.values(o).some(reads);
  };
  const tableBound = name === "ordinary.table_boundary";
  if (tableBound || allDocs(data).some((doc) => doc.lines.some((l) => reads(l.expr)))) return undefined;
  return `Unread parameter: no line of any form or definition reads ${name}; it serves a cross-check outside the computation, so shifting it cannot change any value.`;
}

// A refusal entry that cannot change any value because another line carrying the same gate
// refuses first or identically. Without a reader: the line's expression reads chain[0] first
// and each chain line reads the next first, and the last carries the identical entry (gate,
// form, remedy and cite), so removing the entry turns the line's own refusal into the same
// refusal arriving through the chain. With a reader: the line is read only by that reader,
// the reader reads chain[0] first, chain[i] reads chain[i+1] (first operand, or any operand of
// a sum, which evaluates every operand and returns a refusal ahead of an unknown), and the last
// carries the same gate; the reader then returns that refusal before the line's own could reach it.
function firstReadCarries(line: string, index: number, chain: string[], reader?: string) {
  return {
    reason: reader
      ? `${line} is read only by ${reader}, which reads ${chain.join(" -> ")} first; ${chain[chain.length - 1]} refuses on the same gate, so whenever it is true ${reader} returns a refusal from that chain (or an earlier one) and the entry on ${line} never decides a value.`
      : `${line} reads ${chain.join(" -> ")} first, and ${chain[chain.length - 1]} carries the identical refusal entry, so without the entry on ${line} the same refusal arrives through the chain.`,
    holds: (d: CanonicalData): boolean => {
      const l = findLine(d, line); const entry = l?.refuses?.[index];
      const last = findLine(d, chain[chain.length - 1]!);
      const same = (r: { when: string }): boolean => reader ? r.when === entry!.when : stableStringify(r) === stableStringify(entry);
      if (!l || !entry || !last || !(last.refuses ?? []).some(same)) return false;
      const reads = (from: string, to: string, anySumOperand: boolean): boolean => {
        const x = findLine(d, from); if (!x) return false;
        const refs = operandRefs(d, x.expr);
        return refs[0] === to || (anySumOperand && x.expr.op === "sum" && refs.includes(to));
      };
      if (reader) {
        if (stableStringify(readersOf(d, line)) !== stableStringify([reader]) || !reads(reader, chain[0]!, false)) return false;
      } else if (!reads(line, chain[0]!, false)) return false;
      for (let i = 0; i + 1 < chain.length; i++) if (!reads(chain[i]!, chain[i + 1]!, !!reader)) return false;
      return true;
    },
  };
}

// The EIC's first test reads Form 1040 line 11b. A refusal gate that already refuses a line
// line 11b reads ends the EIC with that refusal before any EIC line carrying the same gate is
// reached from Form 1040, so removing the EIC copy of the gate changes no Form 1040 line.
function agiFirst(gate: string, line: string, index: number) {
  return {
    reason: `The gate ${gate} also refuses a line that Form 1040 line 11b reads, and eic.eligible tests eic.below_top (which reads line 11b) first, so the return's EIC refuses through line 11b whenever ${gate} is true; the copy of the gate on ${line} adds nothing to any Form 1040 line.`,
    holds: (d: CanonicalData): boolean => {
      const l = findLine(d, line); if (!l || l.refuses?.[index]?.when !== gate) return false;
      const seen = new Set<string>(); const stack = ["f1040.line11b"]; let found = false;
      while (stack.length) { const id = stack.pop()!; if (seen.has(id)) continue; seen.add(id); const x = findLine(d, id); if (!x) continue; if ((x.refuses ?? []).some((r) => r.when === gate)) found = true; stack.push(...operandRefs(d, x.expr)); }
      const el = findLine(d, "eic.eligible"); const bt = findLine(d, "eic.below_top");
      return found && !!el && !!bt && operandRefs(d, el.expr)[0] === "eic.below_top" && operandRefs(d, bt.expr)[0] === "f1040.line11b";
    },
  };
}

// A Worksheet A line 5 amount whose EIC Table band prints the maximum credit in every column
// that uses it: with line 3 inside [amount, amount + $1) the lookup returns the maximum, line 6
// takes the smaller of it and line 2 (never above the maximum), so blank or not, line 6 is line 2.
function thresholdAtPlateau(param: string, tables: string[], col: number) {
  return {
    reason: `Line 5 amount ${param}: in ${tables.join(", ")} the bands covering [${param}, ${param} + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way.`,
    holds: (d: CanonicalData): boolean => {
      const v = d.params.values[param]?.value; if (typeof v !== "number") return false;
      return tables.every((t) => {
        const tb = d.tables.find((x) => x.id === t); if (!tb?.bands) return false;
        const max = Math.max(...tb.bands.map((b) => b.tax[col]!));
        const cover = tb.bands.filter((b) => b.at_least < v + 100 && b.less_than > v);
        return cover.length > 0 && cover.every((b) => b.tax[col] === max);
      });
    },
  };
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
    const reason=aliasEquivalence(baseline,survivor) ?? sharedGateEquivalence(baseline,survivor) ?? unreadParameter(baseline,survivor);
    if(reason)EQUIVALENT[survivor.id]=reason;
    const conditional=EQUIVALENT_IF[survivor.id];
    if(conditional && conditional.holds(baseline))EQUIVALENT[survivor.id]=conditional.reason+" (structural conditions re-checked this run.)";
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
