// Mutation tool: apply single-atom mutations to the Stage 1 data, run the
// checker and every fixture case against each mutant, and publish the
// mutation score with the surviving mutations listed.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { availableParallelism } from "node:os";
import { join, resolve } from "node:path";
import { Worker } from "node:worker_threads";
import { createHash } from "node:crypto";
import { stableStringify } from "./util.js";
import { loadCanonical } from "./canonical.js";
import { allTargets, evaluate } from "./eval.js";
import { loadCases } from "./fixtures.js";
import { runChecks } from "./check.js";
import type { CanonicalData, Expr, FormDoc, Line } from "./types.js";
import { YEAR, yearPath } from "./year.js";

const ROOT = resolve(import.meta.dirname, "../..");
const FIXTURES = yearPath("fixtures", "stage1.json");

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
      if (expr.op === "prorate") refs.push(expr.amount, expr.part);
      if (expr.op === "keyed_lookup") refs.push(...expr.keys);
      if (expr.op === "rate_lookup") refs.push(expr.key, ...(expr.status ? [expr.status] : []));
      if (expr.op === "copy" && typeof expr.from === "string") refs.push(expr.from);
      for (const ref of refs) {
        if (!ref.startsWith(doc.id + ".")) continue; // same-document only
        // A lookup key is replaced by a line of the key's own type (an enum, a count or an amount), not the result's.
        const wantType = expr.op === "keyed_lookup" || expr.op === "rate_lookup" ? doc.lines.find((l) => l.id === ref)?.type : line.type;
        const candidate = [...doc.lines]
          .slice(0, idx)
          .reverse()
          .find((l) => l.type === wantType && l.id !== ref && !refs.includes(l.id) && l.expr.op !== "input");
        if (!candidate) continue;
        out.push({
          id: `operand.${where}.${ref.split(".").pop()}`,
          kind: "replace an operand",
          where,
          note: `${ref} -> ${candidate.id} (${candidate.type})`,
          apply: (d) => {
            const l = findLine(d, line.id)!;
            const e = l.expr as Expr & { of?: string[] | string; from?: string; take?: string | object; amount?: string; count?: string; part?: string };
            if (Array.isArray(e.of)) e.of = e.of.map((r) => (r === ref ? candidate.id : r));
            else if (e.of === ref) e.of = candidate.id; // round takes one operand
            if (e.from === ref) e.from = candidate.id;
            if (e.take === ref) e.take = candidate.id;
            if (e.amount === ref) e.amount = candidate.id;
            if (e.count === ref) e.count = candidate.id;
            if (e.part === ref) e.part = candidate.id;
            const rk = e as { key?: string; status?: string };
            if (rk.key === ref) rk.key = candidate.id;
            if (rk.status === ref) rk.status = candidate.id;
            const k = e as { keys?: string[] };
            if (Array.isArray(k.keys)) k.keys = k.keys.map((r) => (r === ref ? candidate.id : r));
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

  // Rate tables: each band's upper bound +$1; each band's rates +1 percentage point,
  // exactly (num/den + 1/100), kept at most 1.
  for (const table of data.tables) {
    if (table.kind !== "rate_bands") continue;
    (table.rate_bands ?? []).forEach((band, i) => {
      if (band.not_over !== null) {
        out.push({
          id: `table.${table.id}.band${i}.\$1`,
          kind: "shift a rate band bound (+$1)",
          where: table.id,
          apply: (d) => {
            const bands = d.tables.find((t) => t.id === table.id)!.rate_bands!;
            bands[i]!.not_over! += 100;
            bands[i + 1]!.over! += 100;
          },
        });
      }
      out.push({
        id: `table.${table.id}.band${i}.+1pt`,
        kind: "shift a rate band's rates (+1 point)",
        where: table.id,
        apply: (d) => {
          for (const r of d.tables.find((t) => t.id === table.id)!.rate_bands![i]!.rates) {
            r.num = Math.min(100 * r.den, 100 * r.num + r.den);
            r.den = 100 * r.den;
          }
        },
      });
    });
  }

  return out;
}

// Survivors that are provably equivalent mutants, with the reason. The score
// is reported raw and adjusted (equivalents excluded from the denominator).
const EQUIVALENT: Record<string, string> = {
  "boundary.eic.eic.self_employed": "With no Schedule C (the only case the boundary changes, a count of zero), Worksheet B's line 4b is the Step 5 earned income plus zero, and line 6 is that amount floored at zero; the Step 5 earned income is line 1z of Form 1040 (Step 5 lines 2 and 4 are zero in this tool) and is never negative, so eic.line1, eic.earned_for_limit and the Schedule 8812 chart amount take the same value on either route.",
  "boundary.person.person.files_se": "The boundary changes only the case where Schedule SE line 4c is zero; then lines 6, 12 and 13 are zero, so Part 1 of Worksheet B (person.sc_total less person.se_line13) equals Part 2 (person.sc_total).",
  "boundary.sc.sc.ho_over": "At exactly 300 square feet both branches give the same amount: $5 times the square feet used and $5 times 300.",
  "boundary.se.positive": "The boundary changes only the case where line 3 is zero, where 92.35% of line 3 and line 3 itself are both zero.",
  "operand.eic.eic.wsb_4b.earned_income": "eic.earned_income is Step 5 line 3 plus line 4, and line 4 (nontaxable combat pay) is zero in this tool (eic.zero, refused otherwise), so the two operands are equal at every input.",
  "operand.eic.eic.wsb_6.zero": "Both operands are the zero line: Step 5 line 4 copies eic.zero (combat pay is refused).",
  "operand.person.person.sep_s1.sc_total": "person.se_line2 copies person.sc_total, adding only the Schedule SE refusal; step 1 is read only by step 3, which also reads step 2 (person.se_line13), and step 2 refuses exactly when person.se_line2 does, so step 3 and everything after it are the same.",
  "operand.person.person.simple_catchup.simple_regular": "person.simple_regular is the smaller of the deferral and the $16,500 limit, so the deferral less it, floored at zero, equals the deferral less $16,500 floored at zero at every input.",
  "operand.s179.s179.line13.line12": "Line 12 is the smaller of lines 9 + 10 and line 11, so (lines 9 + 10) less line 12, floored at zero, equals (lines 9 + 10) less line 11, floored at zero, at every input.",
  "operand.s8812.s8812.eiw_3.zero": "Both operands are zero: Earned Income Worksheet line 1b (nontaxable combat pay) copies the zero line in this tool, refused otherwise.",
  "operand.sc.sc.ho_both.zero": "sc.ho_both is reached only when sc.ho_both_limits holds, and then it is a refusal whatever its expression: its value is never read.",
  "operand.sc.sc.ho_limited.ho_line4": "sc.ho_limited is reached only with no section 179 election and line 4 more than line 29 before section 179 (sc.ho_unlimited false); then the floored line 29 is below line 4, which is at most $1,500 (sc.ho_line4_cap), so the smaller of the floored line 29 and either amount is the floored line 29.",
  "operand.scveh.scveh.d5.l5": "For a 2019 vehicle (the only one whose year-5 deduction is read) the year-4 and year-5 limits are both $5,760 (tables/2025/auto_limit.yaml), and every 5-year column of the GDS tables has a year-4 rate at least its year-5 rate (hy, mq1, mq2 equal; mq3 12.24 and 11.30; mq4 13.68 and 10.94), so min(min(l4, t4), t5) = min(l5, t5).",
  "operand.scveh.scveh.d6.l6": "For a 2019 vehicle the year-5 and year-6 limits are both $5,760, and every 5-year column has a year-5 rate at least its year-6 rate, so min(min(l5, t5), t6) = min(l6, t6).",
  "operand.scveh.scveh.l5.k5": "The 2019 rows for years 4 and 5 of tables/2025/auto_limit.yaml hold the same limit, $5,760, and only a 2019 vehicle's year-5 limit is read.",
  "operand.scveh.scveh.l6.k6": "The 2019 rows for years 5 and 6 of tables/2025/auto_limit.yaml hold the same limit, $5,760, and only a 2019 vehicle's year-6 limit is read.",
  "operand.scveh.scveh.line17.line16": "scveh.bonus_allowed is the smaller of line 16 and line 11, so line 11 less it, floored at zero, equals line 11 less line 16, floored at zero, at every input.",
  "operand.f8889.f8889.family_year.family_under55": "f8889.family_year is read only under the last-month rule with family coverage on December 1, where the filer is married with family coverage, so line 3 is the family amount without the additional contribution amount (f8889.age55_line3 is false), line 4 is zero (Archer MSAs are refused) and line 5 equals f8889.family_under55.",
  "operand.f8889.f8889.self_year.self_amount": "f8889.self_year is read only under the last-month rule, by f8889.self_all and, with family coverage on December 1, by f8889.self_dec_year; the only reader of both is Step 4 (f8889.step4_total = self_all - self_in_family), where the two copies cancel, and with self-only coverage on December 1 the spouse rule does not apply, so Step 4 is not read.",
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
  "boundary.eic.eic.wsb_4b_positive": {
    reason: "The inclusive test differs only at Worksheet B line 4b = 0. wsb_4b_positive is read only by the line 5 stop, an all-test that requires self-employment before it and, after it, Step 5 question 3 to be No; for a self-employed filer question 3 compares line 4b with the EIC limit, so at line 4b = 0 it asks whether 0 < limit, which holds for every limit (all are positive). The stop is therefore false on both routes, and question 3 reads only lines the stop has already evaluated without refusal, so no refusal is newly reached.",
    holds: (d) => {
      const limits = Object.entries(d.params.values).filter(([k]) => /^eic\.limit\d\./.test(k));
      if (limits.length < 8 || !limits.every(([, p]) => typeof p.value === "number" && p.value > 0)) return false;
      if (stableStringify(readersOf(d, "eic.wsb_4b_positive")) !== stableStringify(["eic.wsb_line5_stop"])) return false;
      const s5 = findLine(d, "eic.step5_income"); const efl = findLine(d, "eic.earned_for_limit"); const stop = findLine(d, "eic.wsb_line5_stop");
      if (!s5 || !efl || !stop || s5.expr.op !== "test" || !("lt" in s5.expr)) return false;
      if (stableStringify((s5.expr as { lt: unknown }).lt) !== stableStringify(["eic.earned_for_limit", "eic.limit"])) return false;
      if (efl.expr.op !== "choose") return false;
      const se = (efl.expr.alternatives as { guard: unknown; then: string }[]).find((a) => stableStringify(a.guard).includes("\"eic.self_employed\"") && stableStringify(a.guard).includes("true"));
      if (!se || se.then !== "eic.wsb_4b") return false;
      const refs = operandRefs(d, stop.expr);
      const i = refs.indexOf("eic.self_employed"), j = refs.indexOf("eic.wsb_4b_positive"), k = refs.indexOf("eic.step5_income");
      return stop.expr.op === "test" && "all" in stop.expr && i >= 0 && i < j && j < k;
    },
  },
  "filter.person.person.hsa_step1": hsaSplitSum("person.hsa_step1", "household.hsa_step1_sum"),
  "filter.person.person.hsa_share": hsaSplitSum("person.hsa_share", "household.hsa_share_sum"),
  "refusal.retirement.retirement.amount_a.0": firstReadCarries("retirement.amount_a", 0, ["retirement.show_a", "retirement.has_rollover", "retirement.rolled"]),
  "refusal.retirement.retirement.amount_a.1": firstReadCarries("retirement.amount_a", 1, ["retirement.show_a", "retirement.has_rollover", "retirement.rolled"]),
  "refusal.ssb.ssb.line6.0": firstReadCarries("ssb.line6", 0, ["ssb.line5", "ssb.line3", "f1040.line8"], "ssb.line7"),
  "boundary.s1a.s1a.line10_over": s1aStepSkip("s1a.line10_over", "s1a.line8", "s1a.line9", "s1a.line10_pos", "s1a.line12", "s1a.line13_figured", "s1a.line7", "s1a.line13_amount"),
  "boundary.s1a.s1a.line18_over": s1aStepSkip("s1a.line18_over", "s1a.line16", "s1a.line17", "s1a.line18_pos", "s1a.line20", "s1a.line21_figured", "s1a.line15", "s1a.line21_amount"),
  "boundary.s1a.s1a.line27_over": s1aStepSkip("s1a.line27_over", "s1a.line25", "s1a.line26", "s1a.line27_pos", "s1a.line29", "s1a.line30_figured", "s1a.line24", "s1a.line30_amount"),
  "boundary.s1a.s1a.line33_over": s1aStepSkip("s1a.line33_over", "s1a.line31", "s1a.line32", "s1a.line33_pos", "s1a.line34", "s1a.line35_figured", "s1a.senior_amount", "s1a.line35_calc"),
  "operand.s1a.s1a.line6_calc.line5": s1aPartGate("s1a.line5", "s1a.part2"),
  "operand.s1a.s1a.line7_calc.line6": s1aPartGate("s1a.line6", "s1a.part2"),
  "operand.s1a.s1a.line10_calc.line8": s1aPartGate("s1a.line8", "s1a.part2"),
  "operand.s1a.s1a.line10_pos.line9": s1aPartGate("s1a.line9", "s1a.part2"),
  "operand.s1a.s1a.line13_figured.line12": s1aPartGate("s1a.line12", "s1a.part2"),
  "operand.s1a.s1a.line14c_calc.line14b": s1aPartGate("s1a.line14b", "s1a.part3"),
  "operand.s1a.s1a.line18_calc.line16": s1aPartGate("s1a.line16", "s1a.part3"),
  "operand.s1a.s1a.line18_pos.line17": s1aPartGate("s1a.line17", "s1a.part3"),
  "operand.s1a.s1a.line21_figured.line20": s1aPartGate("s1a.line20", "s1a.part3"),
  "operand.s1a.s1a.line27_calc.line25": s1aPartGate("s1a.line25", "s1a.part4"),
  "operand.s1a.s1a.line27_pos.line26": s1aPartGate("s1a.line26", "s1a.part4"),
  "operand.s1a.s1a.line30_figured.line29": s1aPartGate("s1a.line29", "s1a.part4"),
  "operand.s1a.s1a.line33_calc.line31": s1aPartGate("s1a.line31", "s1a.part5"),
  "operand.s1a.s1a.line33_pos.line32": s1aPartGate("s1a.line32", "s1a.part5"),
  "operand.s1a.s1a.line35_figured.line34": s1aPartGate("s1a.line34", "s1a.part5"),
  "operand.s1a.s1a.line24_calc.line23": s1aPartGate("s1a.line23", "s1a.part4", "s1a.line23_total"),
  "operand.s1a.s1a.line4c_one.line4a": s1aOneEmployer("line 4a, read by the one-employer step, is itself the column (b) total there"),
  "operand.s1a.s1a.line4c_one.line4b": s1aOneEmployer("line 4b is zero (Form 4137 is refused), so the larger of line 4a and the column (b) total is the column (b) total, which line 4a is"),
  "boundary.sli.sli.over": prorateSkip("The test 'line 4 more than line 5' made inclusive adds only the case line 4 = line 5"),
  "operand.sli.sli.line9.line8": prorateSkip("Reading the prorated line directly instead of line 8 differs only when line 4 is not more than line 5"),
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

function unreadTable(data: CanonicalData, mutation: Mutation): string | undefined {
  if (!mutation.id.startsWith("table.")) return undefined;
  const name = mutation.where;
  if (allDocs(data).some((doc) => doc.lines.some((l) => (l.expr as { table?: string }).table === name))) return undefined;
  return `Unread table: no line of any form or definition looks up ${name}, so changing it cannot change any value.`;
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

// The Student Loan Interest Deduction Worksheet skips lines 6 and 7 (line 8 is zero) when line 4 is
// not more than line 5. The prorated line's part is line 6 = line 4 - line 5, which is then zero or
// negative, and `prorate` keeps its ratio at 0 or more, so the prorated line is zero there too: the
// skip and the formula agree, and a mutant that crosses between them changes no value.
// A Schedule 1-A printed line inside a part is a gate: $0 when the part does not apply, otherwise
// its "_calc" helper. Equivalences about the figure look through the gate.
function s1aFigure(d: CanonicalData, id: string): Line | undefined {
  const l = findLine(d, id);
  if (l?.expr.op !== "choose") return l;
  const thens = l.expr.alternatives.map((a) => a.then);
  return thens.length === 2 && thens.includes("s1a.zero") && thens.includes(id + "_calc") ? findLine(d, id + "_calc") : l;
}

// Inside a Schedule 1-A part, a helper reads a gated printed line or the figure behind the gate.
// They differ only when the part does not apply; then every reader of the part's chain is a
// printed line of the part (itself $0) or the part's result line (13, 21, 30, 36a), which is $0
// under the same conditions before it reads the chain.
function hsaSplitSum(perPerson: string, total: string) {
  return {
    reason: `${perPerson} keeps only a Form 8889 that uses the spouse rule of line 6. Its total ${total} is read only by f8889.allocation_bad, which is reached only on a form that uses the rule and which already holds when exactly one form uses it (household.hsa_split_count is 1); when both forms use it the filter keeps every form. So dropping the filter changes no value that is read.`,
    holds: (d: CanonicalData): boolean => {
      const bad = findLine(d, "f8889.allocation_bad");
      const share = findLine(d, "f8889.share");
      return readersOf(d, total).join() === "f8889.allocation_bad" && readersOf(d, perPerson).join() === total
        && !!bad && JSON.stringify(bad.expr).includes('"household.hsa_split_count",{"const":1')
        && !!share && (share.refuses ?? []).some((r) => r.when === "f8889.allocation_bad")
        && readersOf(d, "f8889.share").join() === "f8889.line6_split";
    },
  };
}

function s1aPartGate(gated: string, flag: string, figure = gated + "_calc") {
  return {
    reason: `${gated} is ${figure} when ${flag} holds and $0 otherwise; the chain that reads it is reached only through the part's result line, which is $0 when the part does not apply, so reading ${figure} instead changes no value.`,
    holds: (d: CanonicalData): boolean => {
      const g = findLine(d, gated), f = findLine(d, flag);
      if (!g || !f || g.expr.op !== "choose" || f.expr.op !== "test") return false;
      const thens = g.expr.alternatives.map((a) => a.then);
      const viaFlag = g.expr.alternatives.every((a) => stableStringify(a.guard).includes(`"${flag}"`));
      const direct = thens.length === 2 && thens.includes("s1a.zero") && thens.includes(figure) && viaFlag;
      // line 23 is gated by the car loan question itself, which Part IV's flag is.
      const byClaim = thens.length === 2 && thens.includes("s1a.zero") && thens.includes(figure) && stableStringify(f.expr) === stableStringify({ op: "test", eq: ["s1a.carloan", { const: true }] })
        && g.expr.alternatives.every((a) => stableStringify(a.guard).includes('"s1a.carloan"'));
      return direct || byClaim;
    },
  };
}

// Schedule 1-A phase-outs: 'line A more than line B' chooses between the capped amount and the
// figured amount (the cap less a reduction of the excess). Made inclusive, the test adds only
// A = B, where the excess is zero, so the reduction and the figured amount's subtraction are zero.
function s1aStepSkip(over: string, magi: string, base: string, pos: string, cut: string, figured: string, cap: string, chooser: string) {
  return {
    reason: `The test '${magi} more than ${base}' made inclusive adds only ${magi} = ${base}; there ${pos} is zero, the reduction ${cut} is zero (zero in whole $1,000 steps, or 6% of zero), and ${figured} (${cap} less ${cut}) equals ${cap}, the value the other branch gives.`,
    holds: (d: CanonicalData): boolean => {
      const o = findLine(d, over), p = findLine(d, pos), c = s1aFigure(d, cut), f = findLine(d, figured), ch = findLine(d, chooser);
      if (!o || !p || !c || !f || !ch) return false;
      if (o.expr.op !== "test" || !("gt" in o.expr) || stableStringify(o.expr.gt) !== stableStringify([magi, base])) return false;
      if (p.expr.op !== "subtract_floor0" || p.expr.from !== magi || p.expr.take !== base) return false;
      if (c.expr.op !== "multiply_rate") return false;
      const amt = typeof c.expr.amount === "string" ? findLine(d, c.expr.amount) : undefined;
      const fromPos = c.expr.amount === pos || (amt?.expr.op === "round" && amt.expr.of === pos);
      if (!fromPos || f.expr.op !== "subtract_floor0" || f.expr.from !== cap || f.expr.take !== cut) return false;
      if (ch.expr.op !== "choose") return false;
      const thens = ch.expr.alternatives.map((a) => a.then);
      return thens.length === 2 && thens.includes(cap) && thens.includes(figured);
    },
  };
}

// Schedule 1-A line 4c with one employer is the larger of lines 4a and 4b, where line 4a is the
// worksheet column (b) total and line 4b is zero.
function s1aOneEmployer(what: string) {
  return {
    reason: `Read only when there is one employer (line 4c's choice): ${what}. No value can change.`,
    holds: (d: CanonicalData): boolean => {
      const one = findLine(d, "s1a.line4c_one"), a = s1aFigure(d, "s1a.line4a"), b = s1aFigure(d, "s1a.line4b"), c = s1aFigure(d, "s1a.line4c");
      if (!one || !a || !b || !c || one.expr.op !== "larger_of" || stableStringify(one.expr.of) !== stableStringify(["s1a.line4a", "s1a.line4b"])) return false;
      if (b.expr.op !== "param" || d.params.values[b.expr.ref]?.value !== 0) return false;
      if (a.expr.op !== "choose" || c.expr.op !== "choose") return false;
      const aOne = a.expr.alternatives.find((x) => stableStringify(x.guard).includes('"s1a.tip_multi"') && stableStringify(x.guard).includes("false"));
      const cOne = c.expr.alternatives.find((x) => x.then === "s1a.line4c_one");
      return aOne?.then === "s1a.tip_reported" && !!cOne && stableStringify(cOne.guard) === stableStringify(aOne.guard);
    },
  };
}

function prorateSkip(what: string) {
  return {
    reason: `${what}; there line 6 (line 4 less line 5) is zero or negative, the prorate ratio is kept at 0, and the prorated amount equals the skip branch's zero.`,
    holds: (d: CanonicalData): boolean => {
      const l8 = findLine(d, "sli.line8"), fig = findLine(d, "sli.line8_figured"), l6 = findLine(d, "sli.line6"), over = findLine(d, "sli.over"), zero = findLine(d, "sli.zero");
      if (!l8 || !fig || !l6 || !over || !zero) return false;
      if (fig.expr.op !== "prorate" || fig.expr.part !== "sli.line6") return false;
      if (l6.expr.op !== "subtract" || l6.expr.from !== "sli.line4" || l6.expr.take !== "sli.line5") return false;
      if (over.expr.op !== "test" || !("gt" in over.expr) || stableStringify(over.expr.gt) !== stableStringify(["sli.line4", "sli.line5"])) return false;
      if (zero.expr.op !== "param" || d.params.values[zero.expr.ref]?.value !== 0) return false;
      if (l8.expr.op !== "choose") return false;
      const thens = l8.expr.alternatives.map((a) => a.then);
      return thens.length === 2 && thens.includes("sli.line8_figured") && thens.includes("sli.zero");
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

const normal = (v: { kind: string; cents?: number; value?: unknown; num?: number; den?: number }): string =>
  v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
    : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;

type Outcome = "check" | "fixtures" | "survives";

// What happens to one mutant: the checker rejects it, a fixture value changes, or it survives.
function outcome(baseline: CanonicalData, cases: ReturnType<typeof loadCases>["cases"], m: Mutation): Outcome {
  const data = cloneData(baseline);
  m.apply(data);
  if (runChecks(data).errors.length > 0) return "check";
  for (const c of cases) {
    const result = evaluate(data, c.inputs, allTargets(data, c.inputs));
    for (const [key, expected] of Object.entries(c.expect ?? {})) {
      const der = result.derivations.get(key);
      if (!der || normal(der.value) !== normal(expected)) return "fixtures";
    }
  }
  return "survives";
}

function mutantsDigest(muts: Mutation[]): string {
  return createHash("sha256").update(muts.map((m) => m.id).join("\n")).digest("hex");
}

// One worker's share: every `count`-th mutant from `index`, with a digest of the whole
// mutant list so the main thread can confirm every worker split the same list.
export function mutantShare(index: number, count: number): { digest: string; outcomes: [number, Outcome][] } {
  const baseline = loadCanonical();
  const cases = loadCases().cases;
  const muts = mutations(baseline);
  const outcomes: [number, Outcome][] = [];
  for (let i = index; i < muts.length; i += count) outcomes.push([i, outcome(baseline, cases, muts[i]!)]);
  return { digest: mutantsDigest(muts), outcomes };
}

// Workers: MUTATE_WORKERS, or the core count less six (left for the steps check-all runs
// beside this one); one means no workers.
function workerCount(): number {
  const set = Number(process.env.MUTATE_WORKERS);
  return Number.isInteger(set) && set > 0 ? set : Math.max(1, availableParallelism() - 6);
}

async function outcomesOf(baseline: CanonicalData, cases: ReturnType<typeof loadCases>["cases"], muts: Mutation[]): Promise<Outcome[]> {
  const count = workerCount();
  if (count === 1) return muts.map((m) => outcome(baseline, cases, m));
  const digest = mutantsDigest(muts);
  const shares = await Promise.all(Array.from({ length: count }, (_, index) => new Promise<ReturnType<typeof mutantShare>>((done, fail) => {
    const w = new Worker(new URL("./mutate-worker.js", import.meta.url), { workerData: { year: YEAR, index, count } });
    w.once("message", done);
    w.once("error", fail);
    w.once("exit", (code) => { if (code !== 0) fail(new Error(`mutation worker ${index} exited with ${code}`)); });
  })));
  const all: Outcome[] = new Array(muts.length);
  for (const share of shares) {
    if (share.digest !== digest) throw new Error("mutation worker built a different mutant list");
    for (const [i, o] of share.outcomes) all[i] = o;
  }
  if (all.some((o) => o === undefined)) throw new Error("mutation workers left mutants unevaluated");
  return all;
}

export async function runMutation(): Promise<number> {
  const baseline = loadCanonical();
  const fixtureFile = loadCases();

  // A mismatching baseline must never make every mutant look killed.
  for (const c of fixtureFile.cases) {
    const result=evaluate(baseline,c.inputs,allTargets(baseline,c.inputs));
    for (const [key,expected] of Object.entries(c.expect ?? {})) {
      const actual=result.derivations.get(key)?.value;
      if (!actual || normal(actual)!==normal(expected)) throw new Error(`mutation baseline mismatch: ${c.id} ${key}`);
    }
  }
  const muts = mutations(baseline);
  const survivors: Mutation[] = [];
  let killedByCheck = 0;
  let killedByFixtures = 0;

  const outcomes = await outcomesOf(baseline, fixtureFile.cases, muts);
  muts.forEach((m, i) => {
    if (outcomes[i] === "check") killedByCheck++;
    else if (outcomes[i] === "fixtures") killedByFixtures++;
    else survivors.push(m);
  });

  const total = muts.length;
  const killed = killedByCheck + killedByFixtures;
  const score = total === 0 ? 0 : killed / total;
  for(const survivor of survivors) {
    const reason=aliasEquivalence(baseline,survivor) ?? sharedGateEquivalence(baseline,survivor) ?? unreadParameter(baseline,survivor) ?? unreadTable(baseline,survivor);
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
  const outDir = yearPath("reports");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "mutation.md"), report.join("\n"));
  console.log(`mutation: ${total} mutants, killed by checker ${killedByCheck}, by fixtures ${killedByFixtures}, surviving ${survivors.length} (${equivalentSurvivors.length} equivalent; score ${(score * 100).toFixed(1)}%, adjusted ${(adjusted * 100).toFixed(1)}%)`);
  console.log(`report: reports/${YEAR}/mutation.md`);
  return unexplained.length === 0 ? 0 : 1;
}
