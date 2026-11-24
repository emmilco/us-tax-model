// Mutation tool: apply single-atom mutations to the Stage 1 data, run the
// checker and every fixture case against each mutant, and publish the
// mutation score with the surviving mutations listed.

import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { defaultWorkers } from "./pool.js";
import { join, resolve } from "node:path";
import { Worker } from "node:worker_threads";
import { createHash } from "node:crypto";
import { stableStringify } from "./util.js";
import { loadCanonical } from "./canonical.js";
import { allTargets, evaluate, GATE_PENDING, multiplyRateHalfUp } from "./eval.js";
import type { FixtureCase } from "./fixtures.js";
import { loadFixtureCases } from "./fixture-inputs.js";
import fc from "fast-check";
import { federalDocuments, nyReturnArbitrary, sampleReturns } from "./generate.js";
import { runChecks } from "./check.js";
import { interviewStatus, loadInterview, type InterviewData } from "./interview.js";
import type { CanonicalData, Expr, FormDoc, Line, ParamEntry, TableDoc, ValueType } from "./types.js";
import { NY_MODE, YEAR } from "./year.js";
import { nyPath, reportName, reportPath, yearPath } from "./year.js";

const ROOT = resolve(import.meta.dirname, "../..");

interface Mutation {
  id: string;
  kind: string;
  where: string;
  note?: string;
  /** For an operand replacement, the line the mutant reads in place of the replaced operand. */
  replacement?: string;
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

type OperandSite = { ref: string; kind: string; path: (string | number)[]; wantType: string | undefined; tier: number };
// Every operand position is a site: keyed_lookup keys, rate_lookup and table_lookup key and status
// included. Sites of tier 2 and above (choose branch values, string operands of test expressions)
// are mutated up to the tier named by MUTATE_TIER (default 3).
const SITE_TIER = ((t) => (Number.isFinite(t) ? t : 3))(Number(process.env.MUTATE_TIER ?? 3));

/** String line references inside a test expression, with their paths, through nested tests. */
function testSites(test: any, path: (string | number)[], out: OperandSite[], typeOf: (ref: unknown) => string | undefined): void {
  if (test === null || typeof test !== "object") return;
  for (const key of ["eq", "ne", "lt", "le", "gt", "ge"]) {
    const pair = test[key];
    if (Array.isArray(pair)) pair.forEach((ref: unknown, i: number) => {
      if (typeof ref === "string") out.push({ ref, kind: "test", path: [...path, key, i], wantType: typeOf(ref), tier: 3 });
    });
  }
  for (const key of ["all", "any"]) if (Array.isArray(test[key])) test[key].forEach((t: unknown, i: number) => testSites(t, [...path, key, i], out, typeOf));
  if (test.not) testSites(test.not, [...path, "not"], out, typeOf);
}

/** Every string line reference in an expression position the mutator can replace. */
function collectOperandSites(expr: any, lineType: string, doc: FormDoc): OperandSite[] {
  const sites: OperandSite[] = [];
  const typeOf = (ref: unknown): string | undefined =>
    typeof ref === "string" ? doc.lines.find((l) => l.id === ref)?.type : undefined;
  const push = (ref: unknown, kind: string, path: (string | number)[], wantType: string | undefined, tier = 0) => {
    if (typeof ref === "string") sites.push({ ref, kind, path, wantType, tier });
  };
  switch (expr?.op) {
    case "sum": case "smaller_of": case "larger_of":
      (expr.of ?? []).forEach((ref: any, i: number) => push(ref, "of", ["of", i], lineType));
      break;
    case "subtract": case "subtract_floor0":
      push(expr.from, "from", ["from"], lineType);
      push(expr.take, "take", ["take"], lineType);
      break;
    case "multiply_rate":
      push(expr.amount, "amount", ["amount"], lineType);
      push(expr.rate, "rate", ["rate"], typeOf(expr.rate));
      break;
    case "round":
      push(expr.of, "of", ["of"], lineType);
      break;
    case "multiply_count":
      push(expr.amount, "amount", ["amount"], lineType);
      push(expr.count, "count", ["count"], lineType);
      break;
    case "prorate":
      push(expr.amount, "amount", ["amount"], lineType);
      push(expr.part, "part", ["part"], lineType);
      push(expr.whole, "whole", ["whole"], typeOf(expr.whole));
      break;
    case "percent_floor":
      push(expr.part, "part", ["part"], lineType);
      push(expr.whole, "whole", ["whole"], typeOf(expr.whole));
      break;
    case "keyed_lookup":
      (expr.keys ?? []).forEach((ref: any, i: number) => push(ref, "keys", ["keys", i], typeOf(ref)));
      break;
    case "rate_lookup":
      push(expr.key, "key", ["key"], typeOf(expr.key));
      push(expr.status, "status", ["status"], typeOf(expr.status));
      break;
    case "table_lookup":
      push(expr.key, "key", ["key"], typeOf(expr.key));
      push(expr.status, "status", ["status"], typeOf(expr.status));
      break;
    case "choose":
      (expr.alternatives ?? []).forEach((alt: any, i: number) => {
        push(alt.then, `then${i}`, ["alternatives", i, "then"], lineType, 2);
        testSites(alt.guard, ["alternatives", i, "guard"], sites, typeOf);
      });
      break;
    case "test":
      testSites(expr, [], sites, typeOf);
      break;
    case "copy":
      if (typeof expr.from === "string") push(expr.from, "from", ["from"], lineType);
      else if (expr.from && typeof expr.from === "object" && expr.from.bind && typeof expr.from.bind === "object") {
        for (const [key, value] of Object.entries(expr.from.bind)) {
          push(value, "bind", ["from", "bind", key], typeOf(value));
        }
      }
      break;
  }
  return sites;
}

/** Replace the value at a nested path in an expression. */
function replaceAtPath(root: unknown, path: (string | number)[], value: string): void {
  let cursor: any = root;
  for (let i = 0; i < path.length - 1; i++) cursor = cursor[path[i]!];
  cursor[path[path.length - 1]!] = value;
}

export function mutations(data: CanonicalData): Mutation[] {
  const out: Mutation[] = [];

  for (const doc of allDocs(data)) {
    doc.lines.forEach((line, idx) => {
      const expr = line.expr as Expr;
      const where = `${doc.id}.${line.id}`;
      // The mutated line in the clone, found in its own document: def-local ids repeat across defs.
      const own = (d: CanonicalData): Line => allDocs(d).find((x) => x.id === doc.id)!.lines[idx]!;

      if (expr.op === "sum_over" && expr.where) out.push({id:`filter.${where}`,kind:"remove collection filter",where,apply:d=>{const e=own(d).expr; if(e.op==="sum_over") delete e.where;}});
      for (let i=0;i<(line.refuses?.length??0);i++) out.push({id:`refusal.${where}.${i}`,kind:"remove refusal",where,apply:d=>{own(d).refuses!.splice(i,1);}});
      for (let i=0;i<(line.refuses?.length??0);i++) if (line.refuses![i]!.when_known) out.push({id:`consistency.${where}.${i}`,kind:"require unanswered consistency check",where,apply:d=>{delete own(d).refuses![i]!.when_known;}});
      if (expr.op === "test" && "gt" in expr && expr.gt) out.push({id:`boundary.${where}`,kind:"replace strict greater-than with inclusive",where,apply:d=>{const e=own(d).expr as {op:"test";gt?:unknown;ge?:unknown};e.ge=e.gt;delete e.gt;}});
      if (expr.op === "smaller_of" || expr.op === "larger_of") {
        out.push({
          id: `minmax.${where}`,
          kind: "swap smaller_of/larger_of",
          where,
          apply: (d) => {
            const l = own(d);
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
            const l = own(d);
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
            const l = own(d);
            (l.expr as { op: string }).op = "subtract";
          },
        });
      }
      // Operand replacement: replace one referenced same-document line with the
      // nearest earlier same-typed line that the expression does not already use.
      const allSites = collectOperandSites(expr, line.type, doc);
      const refs = new Set(allSites.map((s) => s.ref));
      for (const site of allSites.filter((s) => s.tier <= SITE_TIER)) {
        const ref = site.ref;
        if (!ref.startsWith(doc.id + ".")) continue; // same-document only
        const wantType = site.wantType ?? line.type;
        const candidate = [...doc.lines]
          .slice(0, idx)
          .reverse()
          .find((l) => l.type === wantType && l.id !== ref && !refs.has(l.id) && l.expr.op !== "input");
        if (!candidate) continue;
        const existing = site.kind === "of" || site.kind === "from" || site.kind === "take"
          || site.kind === "amount" || site.kind === "count" || site.kind === "part"
          || site.kind === "keys" || (site.kind === "key" && expr.op === "rate_lookup")
          || (site.kind === "status" && expr.op === "rate_lookup");
        const id = existing
          ? `operand.${where}.${ref.split(".").pop()}`
          : site.kind === "test"
            ? `operand.${where}.${ref.split(".").pop()}.${site.path.map((p) => (p === "alternatives" ? "alt" : p)).join(".")}`
            : `operand.${where}.${ref.split(".").pop()}.${site.kind}`;
        out.push({
          id,
          kind: "replace an operand",
          where,
          note: `${ref} -> ${candidate.id} (${candidate.type})`,
          replacement: candidate.id,
          apply: (d) => {
            replaceAtPath(own(d).expr, site.path, candidate.id);
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

// Survivors classified equivalent, with the reason, filled at run time by the structural rules and
// by the conditional table below. There is no table of prose-only arguments: an equivalence is either
// checked against the current data on every run or the survivor is killed by a fixture. The score
// is reported raw and adjusted (equivalents excluded from the denominator).
const EQUIVALENT: Record<string, string> = {};

// Keyed arguments whose own text proves equivalence only on returns where the answers they name are given: a
// return with those answers withheld can tell the mutant apart (spec 4.7.3), so these are reported apart from the
// mutants proven equivalent on every input, and the score is stated both with and without them excluded. They do
// not fail the run.
export const ANSWERED_ONLY = new Set([
  "operand.sdtw.sdtw.line4.zero.then1",
  "operand.dependent.dependent.dc_line2c.dc_incapable.all.1.eq.0",
  "operand.eic.eic.step5_income.earned_for_limit.lt.0",
  "operand.s8812.s8812.line18a.chart_eic.then0",
  "operand.f8880.f8880.line3a_counted.zero.then1",
  "operand.rental.rental.home.home_pers10_if_any.all.1.gt.0",
  "operand.rec.rec.to_line1.zero.then1",
  "operand.person.person.f4137_line6.zero.then1",
  "operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0",
  "operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0",
]);

// The copy-chain normal form of a line: copies are followed to a parameter or a computed
// line, and each refusal gate met on the way is kept unless it is already known false.
function normalizeChain(data: CanonicalData, id: string, falseGates: Set<string> = new Set(), seen: Set<string> = new Set()): unknown {
  if (seen.has(id)) return { cycle: id };
  const l = findLine(data, id); if (!l) return { unresolved: id };
  const next = new Set(seen); next.add(id);
  const guards = (l.refuses ?? []).filter((r) => !falseGates.has(r.when));
  const context = new Set([...falseGates, ...guards.filter(r => !r.when_known).map((r) => r.when)]);
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
const lineIdSets = new WeakMap<CanonicalData, Set<string>>();

function operandRefs(data: CanonicalData, expr: unknown): string[] {
  let ids = lineIdSets.get(data);
  if (!ids) { ids = new Set(allDocs(data).flatMap((doc) => doc.lines.map((l) => l.id))); lineIdSets.set(data, ids); }
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
  const known=new Set((parent.refuses??[]).filter(r=>!r.when_known).map(r=>r.when));
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
  const known = new Set((parent.refuses ?? []).filter(r=>!r.when_known).map((r) => r.when));
  const nx = normalizeChain(data, x, known); const ny = normalizeChain(data, y, known);
  if (stableStringify(nx) === stableStringify(ny)) return undefined; // an alias, not this rule
  if (stableStringify(stripGuards(nx)) !== stableStringify(ny)) return undefined;
  const others = (parent.expr.of as string[]).filter((o) => o !== x);
  const gated = others.filter((o) => gateWhens(normalizeChain(data, o, known)).length > 0);
  if (gated.length === 0) return undefined;
  if (!gated.every((o) => stableStringify(normalizeChain(data, o, known)) === stableStringify(nx))) return undefined;
  return `Shared-gate identity: ${x} and ${gated.join(", ")} are the same value behind the same refusal gates (${[...new Set(gateWhens(nx))].join(", ")}) with identical refusal text, and ${y} is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.`;
}

// The replaced operand and its replacement, from an operand mutation's note.
function replacedPair(mutation: Mutation): [string, string] | undefined {
  if (mutation.kind !== "replace an operand" || !mutation.note) return undefined;
  const match = /^(\S+) -> (\S+) /.exec(mutation.note);
  return match ? [match[1]!, match[2]!] : undefined;
}

function docOfLine(data: CanonicalData, id: string): FormDoc | undefined {
  return allDocs(data).find((doc) => doc.lines.some((l) => l.id === id));
}

// Whether line `id` reads `target`, directly or through its operands or refusal gates. A rule that
// compares the two operands of a mutated line is sound only when neither depends on that line.
function dependsOn(data: CanonicalData, id: string, target: string, seen: Set<string> = new Set()): boolean {
  if (id === target) return true;
  if (seen.has(id)) return false;
  seen.add(id);
  const l = findLine(data, id);
  if (!l) return false;
  return [...operandRefs(data, l.expr), ...(l.refuses ?? []).map((r) => r.when)].some((r) => dependsOn(data, r, target, seen));
}

function independentOperands(data: CanonicalData, mutation: Mutation, pair: [string, string]): boolean {
  const line = lineOf(mutation);
  return !dependsOn(data, pair[0], line) && !dependsOn(data, pair[1], line);
}

// A line no value sheet prints: its own value may change under a mutation without being observed.
function isHelper(data: CanonicalData, id: string): boolean {
  return findLine(data, id)?.printed === "(helper)";
}

// Floor-minus-min: subtract_floor0{from: A, take: M} with M an ungated smaller_of of A and B (either
// order) has the same value as subtract_floor0{from: A, take: B}: max(0, A - min(A, B)) = max(0, A - B)
// for known amounts, and both read A first and then B (directly or through M, which stops at a refused
// A), so the same refusal, or an unknown, wins (spec 4.7.4). Accepted in either direction.
function floorMinusMin(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const [x, y] = pair;
  const e = findLine(data, lineOf(mutation))?.expr;
  if (e?.op !== "subtract_floor0" || typeof e.from !== "string" || e.take !== x) return undefined;
  const a = e.from;
  const minOf = (m: string, b: string): boolean => {
    const l = findLine(data, m);
    if (!l || (l.refuses ?? []).length || l.expr.op !== "smaller_of") return false;
    const of = l.expr.of as unknown[];
    return of.length === 2 && a !== b && of.includes(a) && of.includes(b);
  };
  if (!minOf(x, y) && !minOf(y, x)) return undefined;
  return `Floor-minus-min identity: ${lineOf(mutation)} is ${a} less ${x}, floored at zero, and one of ${x} and ${y} is the ungated smaller of ${a} and the other, so ${a} less either, floored at zero, is the same at every input; ${a} is read first on both routes and the other operand second, so the same refusal or unknown wins.`;
}

// A choose whose guard is unknown evaluates every alternative it may still take and is a refusal when every
// one of them is (spec 4.7.3). So a value taken as an alternative's `then` reaches the choose's value where that
// guard is unknown as well as where it is true, though only through whether it is a refusal and which. An
// argument resting on "a value an alternative takes is read only where its guard holds" also holds where the
// guard is unknown when one of these does:
//  - refusalBlind: the two values compared never refuse (neverRefuses), so neither is ever a refusal;
//  - unknownGuardSafe: the choose's guards each compare one and the same reference R for equality with a Bool or
//    enum constant, so they are unknown exactly when R is, and then every alternative is possible; and either
//    both values compared are quiet while R is unknown, or another alternative's value is, so that the choose
//    is never a refusal on every way there and is R's unknown on both routes.
// A line is quiet while R is unknown (quietWhile) when it never refuses; or its refusal gates are among the
// mutated line's own (already false, or the line not reached, where its expression is evaluated) and it is a
// choose of the same document whose guards compare R in the same way and one of whose alternatives is quiet
// (so it is R's unknown, never every way refused), or an atom that passes on its operands' refusals (copy,
// round, sum, subtract, subtract_floor0, smaller_of, larger_of, multiply_rate, multiply_count) all of whose
// line operands are quiet. Anything else is not decided, and the argument is not made.
function refusalBlind(data: CanonicalData, a: string, b: string): boolean {
  return neverRefuses(data, a) && neverRefuses(data, b);
}

function guardRef(guards: unknown[]): string | undefined {
  let ref: string | undefined;
  for (let g of guards) {
    while (g && typeof g === "object" && "not" in g) g = (g as { not: unknown }).not;
    const eq = (g as { eq?: unknown[] } | null)?.eq;
    if (!Array.isArray(eq) || eq.length !== 2) return undefined;
    const [a, b] = eq;
    const r = typeof a === "string" ? a : typeof b === "string" ? b : undefined;
    const c = (typeof a === "string" ? b : a) as { const?: unknown } | null;
    if (r === undefined || !c || typeof c !== "object" || !(typeof c.const === "boolean" || typeof c.const === "string")) return undefined;
    if (ref !== undefined && r !== ref) return undefined;
    ref = r;
  }
  return ref;
}

const QUIET_OPS = new Set(["copy", "round", "sum", "subtract", "subtract_floor0", "smaller_of", "larger_of", "multiply_rate", "multiply_count"]);

function quietWhile(data: CanonicalData, id: string, ref: string, home: FormDoc, known: Set<string>, avoid: string | undefined, depth = 0): boolean {
  if (id === avoid || depth > 20) return false;
  if (neverRefuses(data, id) && (avoid === undefined || !dependsOn(data, id, avoid))) return true;
  const l = findLine(data, id);
  if (!l || docOfLine(data, id) !== home || !(l.refuses ?? []).every((r) => known.has(r.when))) return false;
  const e = l.expr as Record<string, unknown>;
  if (e.op === "choose") {
    const alts = e.alternatives as { guard: unknown; then: unknown }[];
    return guardRef(alts.map((a) => a.guard)) === ref && alts.some((a) => typeof a.then === "string" && quietWhile(data, a.then, ref, home, known, avoid, depth + 1));
  }
  if (!QUIET_OPS.has(e.op as string) || (e.op === "copy" && typeof e.from !== "string")) return false;
  return operandRefs(data, e).every((r) => quietWhile(data, r, ref, home, known, avoid, depth + 1));
}

// Whether a choose line's unknown guards leave it the same unknown whatever alternatives `ks` take: one of its other
// alternatives is quiet while the guards' reference is unknown. `avoid` is a line that alternative must not read.
function otherQuiet(data: CanonicalData, line: Line, ks: Set<number>, avoid?: string): boolean {
  if (line.expr.op !== "choose") return false;
  const alts = line.expr.alternatives as { guard: unknown; then: unknown }[];
  const ref = guardRef(alts.map((a) => a.guard));
  const home = docOfLine(data, line.id);
  if (ref === undefined || !home) return false;
  const known = new Set((line.refuses ?? []).map((r) => r.when));
  return alts.some((a, i) => !ks.has(i) && typeof a.then === "string" && quietWhile(data, a.then, ref, home, known, avoid));
}

// The side condition for replacing alternative k's value `a` by `b` in choose `line` (see above).
function unknownGuardSafe(data: CanonicalData, line: Line, k: number, a: string, b: string): boolean {
  if (refusalBlind(data, a, b) || otherQuiet(data, line, new Set([k]))) return true;
  if (line.expr.op !== "choose") return false;
  const ref = guardRef((line.expr.alternatives as { guard: unknown }[]).map((x) => x.guard));
  const home = docOfLine(data, line.id);
  if (ref === undefined || !home) return false;
  const known = new Set((line.refuses ?? []).map((r) => r.when));
  return quietWhile(data, a, ref, home, known, line.id) && quietWhile(data, b, ref, home, known, line.id);
}

// Self-test of unknownGuardSafe on a synthetic form: replacing a $0 alternative by a sibling choose on the same flag
// with a $0 alternative is accepted; by a line behind a refusal gate of its own, or by a choose on another flag, it is
// not, and the evaluator confirms that the refused replacement makes the line a refusal where the base is unknown.
export function unknownGuardSelfTest(): string[] {
  const cite = { doc: "t", locator: "t" };
  const line = (id: string, type: string, expr: unknown, extra: Record<string, unknown> = {}) => ({ id: `t.${id}`, printed: id, label: id, type, expr, cite, ...extra });
  const input = (id: string, type = "NonNegDollars") => line(id, type, { op: "input", source: id });
  const on = (flag: string, then: string, other: string) => ({ op: "choose", alternatives: [
    { guard: { op: "test", eq: [`t.${flag}`, { const: true }] }, then: `t.${then}` },
    { guard: { op: "test", eq: [`t.${flag}`, { const: false }] }, then: `t.${other}` }] });
  const gate = { when: "t.bad", form: "t", remedy: "t", cite };
  const lines = [input("flag", "Bool"), input("other", "Bool"), input("bad", "Bool"), input("amount"),
    line("zero", "NonNegDollars", { op: "param", ref: "t.zero" }),
    line("refused", "NonNegDollars", { op: "copy", from: "t.amount" }, { refuses: [gate] }),
    line("figure", "NonNegDollars", { op: "copy", from: "t.refused" }),
    line("sibling", "NonNegDollars", on("flag", "figure", "zero")),
    line("elsewhere", "NonNegDollars", on("other", "figure", "zero")),
    line("mutated", "NonNegDollars", on("flag", "figure", "zero"))];
  const d = { tax_year: YEAR, forms: [{ id: "t", kind: "form", tax_year: YEAR, title: "t", lines }], defs: [], tables: [],
    params: { tax_year: YEAR, values: { "t.zero": { type: "NonNegDollars", value: 0 } }, enums: {} }, register: { entries: [] } } as unknown as CanonicalData;
  const l = findLine(d, "t.mutated")!;
  const problems: string[] = [];
  const want: [string, boolean][] = [["t.sibling", true], ["t.refused", false], ["t.elsewhere", false]];
  for (const [b, w] of want) if (unknownGuardSafe(d, l, 1, "t.zero", b) !== w) problems.push(`unknownGuardSafe(t.mutated, t.zero -> ${b}) is ${!w}, expected ${w}`);
  const mutant = cloneData(d);
  (findLine(mutant, "t.mutated")!.expr as { alternatives: { then: string }[] }).alternatives[1]!.then = "t.refused";
  const inputs = { "t.other": false, "t.bad": true, "t.amount": 100 };
  const base = evaluate(d, inputs, ["t.mutated"]).values.get("t.mutated")?.kind;
  const mut = evaluate(mutant, inputs, ["t.mutated"]).values.get("t.mutated")?.kind;
  if (base !== "unknown" || mut !== "refusal") problems.push(`with the flag unanswered the base is ${base} and the rejected mutant ${mut}; expected unknown and refusal`);
  return problems;
}

// Self-test of the reasoning through a Bool or enum choose: a form with an enum input E (a, b, c), a Bool input y,
// a false parameter, the gate G = choose[E = a -> false, E = b -> y, E = c -> y] and the enum choose K =
// choose[y = true -> E, y = false -> the parameter a]. G true settles E not a and y true, and implies E != a; G false
// settles neither; E = a settles G false; y true and E = b settle K to b, and K = b with y false is impossible, so K = b
// settles y true. Each fact is also checked against the evaluator on every complete answer.
export function scalarChooseSelfTest(): string[] {
  const cite = { doc: "t", locator: "t" };
  const line = (id: string, type: string, expr: unknown) => ({ id: `t.${id}`, printed: "(helper)", label: id, type, expr, cite });
  const eqc = (r: string, c: unknown) => ({ op: "test", eq: [`t.${r}`, { const: c }] });
  const data = { tax_year: YEAR, forms: [{ id: "t", kind: "form", tax_year: YEAR, title: "t", lines: [
    line("E", "Enum(tv)", { op: "input", source: "E" }), line("y", "Bool", { op: "input", source: "y" }),
    line("no", "Bool", { op: "param", ref: "t.no" }), line("ea", "Enum(tv)", { op: "param", ref: "t.a" }),
    line("G", "Bool", { op: "choose", alternatives: [{ guard: eqc("E", "a"), then: "t.no" }, { guard: eqc("E", "b"), then: "t.y" }, { guard: eqc("E", "c"), then: "t.y" }] }),
    line("K", "Enum(tv)", { op: "choose", alternatives: [{ guard: eqc("y", true), then: "t.E" }, { guard: eqc("y", false), then: "t.ea" }] })] }],
    defs: [], tables: [], register: { entries: [] },
    params: { tax_year: YEAR, values: { "t.no": { type: "Bool", value: false }, "t.a": { type: "Enum(tv)", value: "a" } }, enums: { tv: { values: ["a", "b", "c"] } } } } as unknown as CanonicalData;
  const problems: string[] = [];
  const want = (what: string, got: unknown, expected: unknown) => { if (got !== expected) problems.push(`${what}: ${String(got)}, expected ${String(expected)}`); };
  const gTrue = guardFacts(data, eqc("G", true));
  want("G true settles E = a", decides(eqc("E", "a"), gTrue), false);
  want("G true settles y", decides(eqc("y", true), gTrue), true);
  want("G true implies E != a", testImplies(data, eqc("G", true), { op: "test", ne: ["t.E", { const: "a" }] }), true);
  const gFalse = guardFacts(data, eqc("G", false));
  want("G false leaves E = a open", decides(eqc("E", "a"), gFalse), undefined);
  want("G false leaves y open", decides(eqc("y", true), gFalse), undefined);
  want("E = a settles G", decides(eqc("G", true), guardFacts(data, eqc("E", "a"))), false);
  want("E = b alone leaves G open", decides(eqc("G", true), guardFacts(data, eqc("E", "b"))), undefined);
  const yb = guardFacts(data, { op: "test", all: [eqc("y", true), eqc("E", "b")] });
  want("y true and E = b settle K = b", decides(eqc("K", "b"), yb), true);
  want("K = b settles y", decides(eqc("y", true), guardFacts(data, eqc("K", "b"))), true);
  want("K = a leaves y open", decides(eqc("y", true), guardFacts(data, eqc("K", "a"))), undefined);
  // Every settled fact holds in the evaluator on every complete answer where its premise holds.
  for (const e of ["a", "b", "c"]) for (const y of [true, false]) {
    const vals = evaluate(data, { "t.E": e, "t.y": y } as never, ["t.G", "t.K"]).values;
    const g = (vals.get("t.G") as { value?: unknown })?.value, k = (vals.get("t.K") as { value?: unknown })?.value;
    if (g === true && (e === "a" || y !== true)) problems.push(`the evaluator gives G true at E = ${e}, y = ${y}`);
    if (k === "b" && y !== true) problems.push(`the evaluator gives K = b at y = ${y}`);
    if (e === "a" && g !== false) problems.push(`the evaluator gives G ${String(g)} at E = a`);
  }
  return problems;
}

// Self-test of path dominance through `refusalsSame`: on a synthetic form, a helper H reads a gated figure (a
// choice on flag f between the figure and $0) and a printed line takes, on f true, a choice that reads H in its
// guards. Replacing H's operand by the figure must not be accepted as a guarded figure: where f is unanswered the
// guard's value differs between the routes and turns into a refusal on one of them, which the evaluator confirms.
// As a control, the same form with that reader a copy of H (refusal-transparent) is accepted.
export function guardedFigureSelfTest(): string[] {
  const cite = { doc: "t", locator: "t" };
  const line = (id: string, type: string, expr: unknown, extra: Record<string, unknown> = {}) => ({ id: `t.${id}`, printed: "(helper)", label: id, type, expr, cite, ...extra });
  const input = (id: string, type = "NonNegDollars") => line(id, type, { op: "input", source: id });
  const eqc = (r: string, c: unknown) => ({ op: "test", eq: [`t.${r}`, { const: c }] });
  const gate = { when: "t.g", form: "t", remedy: "t", cite };
  const form = (reader: unknown) => {
    const lines = [input("f", "Bool"), input("g", "Bool"), input("amt"), input("amt2"), input("xi"),
      line("zero", "NonNegDollars", { op: "param", ref: "t.zero" }),
      line("figure", "NonNegDollars", { op: "copy", from: "t.xi" }),
      line("gated", "NonNegDollars", { op: "choose", alternatives: [{ guard: eqc("f", true), then: "t.figure" }, { guard: eqc("f", false), then: "t.zero" }] }),
      line("H", "NonNegDollars", { op: "copy", from: "t.gated" }),
      line("bad", "NonNegDollars", { op: "copy", from: "t.amt" }, { refuses: [gate] }),
      line("zero2", "NonNegDollars", { op: "param", ref: "t.zero" }),
      line("T", "NonNegDollars", reader),
      line("bad2", "NonNegDollars", { op: "copy", from: "t.amt2" }, { refuses: [gate] }),
      line("Rd", "NonNegDollars", { op: "choose", alternatives: [{ guard: eqc("f", true), then: "t.T" }, { guard: eqc("f", false), then: "t.bad2" }] }, { printed: "1" })];
    return { tax_year: YEAR, forms: [{ id: "t", kind: "form", tax_year: YEAR, title: "t", lines }], defs: [], tables: [],
      params: { tax_year: YEAR, values: { "t.zero": { type: "NonNegDollars", value: 0 } }, enums: {} }, register: { entries: [] } } as unknown as CanonicalData;
  };
  const problems: string[] = [];
  const guarded = form({ op: "choose", alternatives: [
    { guard: { op: "test", gt: ["t.H", { const: 10000 }] }, then: "t.bad" },
    { guard: { op: "test", le: ["t.H", { const: 10000 }] }, then: "t.zero2" }] });
  const m = mutations(guarded).find((x) => x.id === "operand.t.t.H.gated");
  if (!m) return ["the synthetic mutant operand.t.t.H.gated was not generated"];
  const reason = structuralReason(guarded, m);
  if (reason) problems.push(`operand.t.t.H.gated is accepted (${reason.slice(0, 60)}...), expected rejected`);
  const mut = cloneData(guarded); m.apply(mut);
  const inputs = { "t.g": true, "t.amt": 100, "t.amt2": 100, "t.xi": 20000 };
  const b = evaluate(guarded, inputs, ["t.Rd"]).values.get("t.Rd")?.kind, v = evaluate(mut, inputs, ["t.Rd"]).values.get("t.Rd")?.kind;
  if (b !== "unknown" || v !== "refusal") problems.push(`with t.f unanswered the base t.Rd is ${b} and the mutant ${v}; expected unknown and refusal`);
  const copied = form({ op: "copy", from: "t.H" });
  const c = mutations(copied).find((x) => x.id === "operand.t.t.H.gated");
  if (!c || !structuralReason(copied, c)?.startsWith("Guarded figure")) problems.push("the control (the reader a copy of H) is not accepted as a guarded figure");
  return problems;
}

// The facts a reader adds to a path: when a choose takes the line only as the value of some
// alternatives (never in a guard), the disjunction of those alternatives' guards holds wherever it
// reads the line. Readers through a refusal gate or a display condition add nothing. `hidden` records
// whether the choose's unknown guards hide those alternatives' values (otherQuiet); a fact on a step that
// does not is used only for a value whose refusals the mutant leaves unchanged (refusalBlind), and only while
// the chain from that value is refusal-transparent. `transparent` records that the reader passes the read
// line's refusals on unchanged and makes no other refusal from its value: an ungated reader that is an atom
// of TRANSPARENT_OPS reading it as an operand, or an ungated choose taking it only as a line-valued
// alternative (never in a guard). A choose alternative that is a def instance binding the read line is not
// a direct take: it gives no fact and is not transparent.
type ReaderStep = { reader: Line; doc: FormDoc; fact: unknown[] | undefined; hidden: boolean; transparent: boolean };
const TRANSPARENT_OPS = new Set(["copy", "round", "sum", "subtract", "subtract_floor0", "smaller_of", "larger_of", "multiply_rate", "multiply_count", "prorate"]);
const readerIndexes = new WeakMap<CanonicalData, Map<string, ReaderStep[]>>();

function readerSteps(data: CanonicalData, id: string): ReaderStep[] {
  let index = readerIndexes.get(data);
  if (!index) {
    index = new Map();
    for (const doc of allDocs(data)) for (const l of doc.lines) {
      const expr = new Set(operandRefs(data, l.expr));
      const gates = new Set([...(l.refuses ?? []).map((r) => r.when), ...(l.shown_when ? [l.shown_when] : [])]);
      const alts = l.expr.op === "choose" ? (l.expr.alternatives as { guard: unknown; then: unknown }[]).map((a) => ({ guard: a.guard, inGuard: new Set(operandRefs(data, a.guard)), inThen: new Set(operandRefs(data, a.then)), direct: typeof a.then === "string" })) : undefined;
      const ungated = !(l.refuses ?? []).length;
      for (const read of new Set([...expr, ...gates])) {
        let fact: unknown[] | undefined;
        let hidden = false;
        let transparent = false;
        if (!gates.has(read) && alts) {
          const taking = alts.filter((a) => a.inThen.has(read));
          if (!alts.some((a) => a.inGuard.has(read)) && taking.length && taking.every((a) => a.direct)) {
            fact = taking.map((a) => a.guard);
            hidden = otherQuiet(data, l, new Set(alts.flatMap((a, i) => a.inThen.has(read) ? [i] : [])), read);
            transparent = ungated;
          }
        } else if (!gates.has(read) && ungated && TRANSPARENT_OPS.has(l.expr.op) && (l.expr.op !== "copy" || typeof (l.expr as { from: unknown }).from === "string")) {
          transparent = true;
        }
        const list = index.get(read) ?? [];
        list.push({ reader: l, doc, fact, hidden, transparent });
        index.set(read, list);
      }
    }
    readerIndexes.set(data, index);
  }
  return index.get(id) ?? [];
}

// A Bool or enum line that is a choose whose alternatives are all lines: each alternative's guard, the line it
// takes, and, where that line is a parameter (a gate's else), the parameter's value. The line's value, where it is
// complete, is the value of the alternative taken, the first whose guard is true (spec 4.7.3); so a value v of the
// line means some alternative that can give v (a line, or a parameter equal to v) was taken, its guard true.
type ScalarAlt = { guard: unknown; then: string; fixed?: boolean | string };
function scalarChoose(data: CanonicalData, id: string): ScalarAlt[] | undefined {
  const l = findLine(data, id);
  if (!l || !(l.type === "Bool" || l.type.startsWith("Enum(")) || l.expr.op !== "choose") return undefined;
  const alts = l.expr.alternatives as { guard: unknown; then: unknown }[];
  if (!alts.every((a) => typeof a.then === "string")) return undefined;
  return alts.map((a) => {
    const n = normalizeChain(data, a.then as string) as { parameter?: unknown };
    return { guard: a.guard, then: a.then as string, ...(typeof n.parameter === "boolean" || typeof n.parameter === "string" ? { fixed: n.parameter } : {}) };
  });
}

// Whether test g, known true, makes test c true: the same test; eq(x, v) against ne(x, w) with
// constants v and w different; a conjunct of an all-test; eq(G, true) for an ungated test line G
// whose own test does; or eq(G, true) for an ungated Bool choose G (scalarChoose) where every
// alternative that can give true has a guard that does, or takes a line L for which eq(L, true) does.
function testImplies(data: CanonicalData, g: unknown, c: unknown, depth = 0): boolean {
  if (depth > 8) return false;
  if (stableStringify(g) === stableStringify(c)) return true;
  const gt = g as { eq?: unknown[]; all?: unknown[] }, ct = c as { ne?: unknown[] };
  const isConst = (v: unknown): boolean => v !== null && typeof v === "object" && "const" in v;
  if (Array.isArray(gt.eq) && Array.isArray(ct.ne) && gt.eq[0] === ct.ne[0] && typeof gt.eq[0] === "string"
    && isConst(gt.eq[1]) && isConst(ct.ne[1]) && stableStringify(gt.eq[1]) !== stableStringify(ct.ne[1])) return true;
  if (Array.isArray(gt.all)) return gt.all.some((x) => testImplies(data, x, c, depth + 1));
  if (Array.isArray(gt.eq) && typeof gt.eq[0] === "string" && stableStringify(gt.eq[1]) === stableStringify({ const: true })) {
    const line = findLine(data, gt.eq[0]);
    if (line && !(line.refuses ?? []).length && line.expr.op === "test") return testImplies(data, line.expr, c, depth + 1);
    const alts = line && line.type === "Bool" && !(line.refuses ?? []).length ? scalarChoose(data, line.id) : undefined;
    if (alts) {
      const possible = alts.filter((a) => a.fixed !== false);
      return possible.length > 0 && possible.every((a) => testImplies(data, a.guard, c, depth + 1)
        || (a.fixed === undefined && testImplies(data, { op: "test", eq: [a.then, { const: true }] }, c, depth + 1)));
    }
  }
  return false;
}

// Whether the facts on a path make the Bool line `flag` true: some fact implies flag == true, or
// flag is an ungated all-test (or single comparison) each of whose conjuncts some fact implies.
function flagHolds(data: CanonicalData, facts: unknown[][], flag: string): boolean {
  const implied = (c: unknown): boolean => facts.some((fact) => fact.every((g) => testImplies(data, g, c)));
  if (implied({ op: "test", eq: [flag, { const: true }] })) return true;
  const f = findLine(data, flag);
  if (!f || (f.refuses ?? []).length) return false;
  // An ungated Bool choose: the facts of single-guard steps, together, settle it true (decides).
  if (f.type === "Bool" && scalarChoose(data, flag)) {
    const single = facts.filter((fact) => fact.length === 1).map((fact) => fact[0]);
    return single.length > 0 && decides({ op: "test", eq: [flag, { const: true }] }, guardFacts(data, { op: "test", all: single })) === true;
  }
  if (f.expr.op !== "test") return false;
  const conjuncts = Array.isArray((f.expr as { all?: unknown[] }).all) ? (f.expr as { all: unknown[] }).all : [f.expr];
  return conjuncts.length > 0 && conjuncts.every(implied);
}

// Path dominance: every chain of readers from `start` to a printed line (or to a refusal gate or
// display condition) passes through choose alternatives whose guards, taken together, make `flag`
// true. Guards count only on readers in start's own document (one frame); readers elsewhere carry
// the facts already gathered. Then a value read from start by any printed line is read only where
// flag holds (spec 4.7.3: a choose does not take an alternative whose guard is false) or, as a way of
// a choose whose guard is unknown, only through its refusals: a step counts only when its choose hides
// the alternatives' values (`hidden`), or, when `refusalsSame` says start refuses alike on both routes,
// when every reader between start and that choose is refusal-transparent (`transparent`), so the line
// the choose reads refuses alike on both routes too. A reader that reads the value in a guard, a
// comparison or a gate, or through a def instance, ends that transparency.
function dominatedBy(data: CanonicalData, start: string, flag: string, refusalsSame = false): boolean {
  const home = docOfLine(data, start);
  if (!home || home.kind === "def") return false;
  const seen = new Set<string>();
  const stack: { id: string; facts: unknown[][]; clear: boolean }[] = [{ id: start, facts: [], clear: refusalsSame }];
  let steps = 0;
  while (stack.length) {
    const { id, facts, clear } = stack.pop()!;
    for (const { reader, doc, fact, hidden, transparent } of readerSteps(data, id)) {
      const next = fact && (hidden || clear) && doc.id === home.id ? [...facts, fact] : facts;
      if (flagHolds(data, next, flag)) continue;
      if (reader.printed !== "(helper)") return false;
      const nextClear = clear && transparent;
      const key = `${reader.id}|${nextClear}|${stableStringify(next)}`;
      if (seen.has(key)) continue;
      seen.add(key);
      if (++steps > 5000) return false;
      stack.push({ id: reader.id, facts: next, clear: nextClear });
    }
  }
  return true;
}

// A two-way choose on Bool line F (guards F == true and F == false, in either order) with no refusal
// gates of its own: where F holds, its value is its true branch's.
function flagGate(data: CanonicalData, id: string): { flag: string; then: string } | undefined {
  const l = findLine(data, id);
  if (!l || (l.refuses ?? []).length || l.expr.op !== "choose" || l.expr.alternatives.length !== 2) return undefined;
  const on = (g: unknown, v: boolean): string | undefined => {
    const eq = (g as { eq?: unknown[] }).eq;
    return Array.isArray(eq) && typeof eq[0] === "string" && stableStringify(eq[1]) === stableStringify({ const: v }) ? eq[0] : undefined;
  };
  const [a, b] = l.expr.alternatives as { guard: unknown; then: unknown }[];
  const trueAlt = on(a!.guard, true) ? a! : b!, falseAlt = trueAlt === a ? b! : a!;
  const flag = on(trueAlt.guard, true);
  if (!flag || on(falseAlt.guard, false) !== flag || typeof trueAlt.then !== "string") return undefined;
  return { flag, then: trueAlt.then };
}

// Guarded figure: the replaced operand is a gated line, "its figure when F holds", and the replacement
// is that figure (or the reverse); the mutated line is a helper, and every printed line reads it only
// where F holds (path dominance). Where F holds the two operands are the same value, so no printed value
// changes; where F does not hold only the helper's own value can.
function guardedFigure(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const line = lineOf(mutation);
  if (!isHelper(data, line)) return undefined;
  for (const [gated, figure] of [pair, [pair[1], pair[0]] as [string, string]]) {
    const g = flagGate(data, gated);
    if (!g || stableStringify(normalizeChain(data, g.then)) !== stableStringify(normalizeChain(data, figure))) continue;
    if (!dominatedBy(data, line, g.flag, refusalBlind(data, gated, figure))) continue;
    return `Guarded figure: ${gated} is ${figure} wherever ${g.flag} holds, and every printed line reads ${line} (a helper) only through choices whose guards make ${g.flag} true, which, where a guard is unknown, are that unknown whatever ${line} is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where ${g.flag} does not hold only ${line}'s own, unprinted value can differ.`;
  }
  return undefined;
}

// Arithmetic atoms that evaluate every operand they reach and return a refusal or an unknown when an
// operand has one (spec 4.7.4); a line of one of these with no refusal gates of its own is incomplete
// whenever an operand is, and refused whenever an operand is refused.
const CARRY_OPS = new Set(["sum", "subtract", "subtract_floor0", "smaller_of", "larger_of", "multiply_rate", "multiply_count", "round", "prorate", "copy"]);

function carries(data: CanonicalData, from: string, target: string, depth = 0): boolean {
  if (from === target) return true;
  const l = findLine(data, from);
  if (depth > 12 || !l || (l.refuses ?? []).length || !CARRY_OPS.has(l.expr.op)) return false;
  if (l.expr.op === "copy" && typeof l.expr.from !== "string") return false;
  return operandRefs(data, l.expr).some((r) => carries(data, r, target, depth + 1));
}

// Gated zero carried earlier: an ungated zero operand is replaced by a zero behind refusal gates, and
// an operand evaluated before it reaches the gated zero through ungated arithmetic. When the gated zero
// refuses (or is unknown) that earlier operand already does, and is returned first; otherwise the two
// operands are both zero. The mutated line's own value is the same at every input.
function carriedZero(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const [x, y] = pair;
  const e = findLine(data, lineOf(mutation))?.expr;
  if (!e) return undefined;
  const order = e.op === "sum" || e.op === "smaller_of" || e.op === "larger_of" ? (e.of as unknown[])
    : e.op === "subtract" || e.op === "subtract_floor0" ? [e.from, e.take] : undefined;
  if (!order) return undefined;
  const nx = normalizeChain(data, x), ny = normalizeChain(data, y);
  if (!zeroBehindGates(data, x) || gateWhens(nx).length || !zeroBehindGates(data, y) || !gateWhens(ny).length) return undefined;
  const i = order.indexOf(x);
  const carrier = order.slice(0, Math.max(0, i)).find((o): o is string => typeof o === "string" && carries(data, o, y));
  if (i < 0 || !carrier) return undefined;
  return `Gated zero carried earlier: ${x} is an ungated zero and ${y} the same zero behind refusal gates (${[...new Set(gateWhens(ny))].join(", ")}); ${carrier}, read first, reaches ${y} through ungated arithmetic, so whenever ${y} refuses or is unknown ${carrier} already is, and is returned first, and otherwise both operands are zero.`;
}

// Guard facts: what a choose alternative's guard, known true, establishes. For each line compared with
// a constant (or a numeric parameter) it records an exact value or an interval, but only through a
// comparison whose result implies the line is complete: a count with a lower bound can make gt, ge and ne
// true, and lt, le and eq false, while it is still unknown (the evaluator's lower-bound rule). A guard
// eq(F, true) or eq(F, false) on an ungated test line F adds what F's own test, true or false, says.
type Bound = { eq?: string; not?: string[]; lo?: number; hi?: number; loStrict?: boolean; hiStrict?: boolean };
type GuardFacts = { data: CanonicalData; same: Set<string>; known: Map<string, Bound>; rel?: Set<string> };

const NEGATE: Record<string, string> = { eq: "ne", ne: "eq", lt: "ge", le: "gt", gt: "le", ge: "lt" };

// A comparison of a line with a constant or a scalar parameter, normalized to the line first.
function comparison(data: CanonicalData, t: unknown): { key: string; line: string; v: unknown; count: boolean } | undefined {
  const flip: Record<string, string> = { eq: "eq", ne: "ne", lt: "gt", le: "ge", gt: "lt", ge: "le" };
  const constOf = (x: unknown): { v: unknown; count: boolean } | undefined => {
    if (x === null || typeof x !== "object") return undefined;
    if ("const" in x) return { v: (x as { const: unknown }).const, count: (x as { type?: string }).type === "Count" };
    const ref = (x as { param?: string }).param;
    const pv = ref === undefined ? undefined : data.params.values[ref];
    return pv && typeof pv.value === "number" ? { v: pv.value, count: pv.type === "Count" } : undefined;
  };
  for (const key of Object.keys(flip)) {
    const pair = (t as Record<string, unknown>)[key];
    if (!Array.isArray(pair)) continue;
    const k1 = constOf(pair[1]), k0 = constOf(pair[0]);
    if (typeof pair[0] === "string" && k1) return { key, line: pair[0], ...k1 };
    if (typeof pair[1] === "string" && k0) return { key: flip[key]!, line: pair[1], ...k0 };
  }
  return undefined;
}

function addComparison(facts: GuardFacts, key: string, line: string, v: unknown, count: boolean, truth: boolean): void {
  const k = truth ? key : NEGATE[key]!;
  const complete = !count || (truth ? ["eq", "lt", "le"].includes(key) : ["gt", "ge", "ne"].includes(key));
  if (!complete) return;
  const f = facts.known.get(line) ?? {};
  if (k === "eq") f.eq = stableStringify(v);
  else if (k === "ne") f.not = [...(f.not ?? []), stableStringify(v)];
  else if (typeof v === "number") {
    if (k === "lt" || k === "le") { if (f.hi === undefined || v < f.hi) { f.hi = v; f.hiStrict = k === "lt"; } }
    else if (f.lo === undefined || v > f.lo) { f.lo = v; f.loStrict = k === "gt"; }
  } else return;
  facts.known.set(line, f);
}

function addTest(facts: GuardFacts, t: unknown, truth: boolean, depth: number): void {
  if (depth > 6) return;
  const all = (t as { all?: unknown[] }).all;
  if (truth && Array.isArray(all)) { all.forEach((c) => addTest(facts, c, true, depth + 1)); return; }
  const any = (t as { any?: unknown[] }).any;
  if (!truth && Array.isArray(any)) { any.forEach((c) => addTest(facts, c, false, depth + 1)); return; }
  if (truth) facts.same.add(stableStringify(t));
  const cmp = comparison(facts.data, t);
  if (!cmp) { addRelation(facts, t, truth); return; }
  addComparison(facts, cmp.key, cmp.line, cmp.v, cmp.count, truth);
  // A Bool line with a settled value: follow copies to the test line it reads. A line's value is its
  // expression's only when its refusal gates were all false (4.7.1), so gates do not stop this.
  let flag = findLine(facts.data, cmp.line);
  for (let i = 0; i < 8 && flag?.expr.op === "copy" && typeof flag.expr.from === "string"; i++) flag = findLine(facts.data, flag.expr.from);
  if (flag && flag.expr.op === "test" && (cmp.key === "eq" || cmp.key === "ne") && typeof cmp.v === "boolean") {
    // eq(F, v) true, or ne(F, v) false, means F is v; the other two mean F is not v.
    addTest(facts, flag.expr, ((cmp.key === "eq") === truth) === cmp.v, depth + 1);
  }
  // A Bool or enum choose with a settled value (eq or ne against a constant): the alternative taken can give that
  // value (or, for "not v", a value other than v). With one such alternative its guard held and, for a line, the line
  // compares the same way; with several taking one line, that line does; with several whose guards each test one
  // enum line E against a value, E is complete and has none of the other values of its enum.
  const alts = flag && (cmp.key === "eq" || cmp.key === "ne") && (typeof cmp.v === "boolean" || typeof cmp.v === "string") ? scalarChoose(facts.data, flag.id) : undefined;
  if (alts) {
    const is = (cmp.key === "eq") === truth;
    const possible = alts.filter((a) => a.fixed === undefined || (a.fixed === cmp.v) === is);
    const same = (then: string): unknown => ({ op: "test", [is ? "eq" : "ne"]: [then, { const: cmp.v }] });
    if (possible.length === 1) {
      addTest(facts, possible[0]!.guard, true, depth + 1);
      if (possible[0]!.fixed === undefined) addTest(facts, same(possible[0]!.then), true, depth + 1);
    } else if (possible.length > 1) {
      if (possible.every((a) => a.fixed === undefined && a.then === possible[0]!.then)) addTest(facts, same(possible[0]!.then), true, depth + 1);
      const eqs = possible.map((a) => comparison(facts.data, a.guard));
      const e0 = eqs[0]?.line, ty = e0 ? findLine(facts.data, e0)?.type ?? "" : "";
      if (e0 && ty.startsWith("Enum(") && eqs.every((c) => c?.key === "eq" && c.line === e0 && typeof c.v === "string")) {
        const taken = new Set(eqs.map((c) => c!.v as string));
        for (const v of facts.data.params.enums[ty.slice(5, -1)]?.values ?? []) if (!taken.has(v)) addComparison(facts, "ne", e0, v, false, true);
      }
    }
  }
}

// A settled comparison of two lines, neither a count (so no lower bound can settle it early): both lines
// are complete, and their order is recorded as "le|a|b" (a <= b) or "lt|a|b" (a < b).
function addRelation(facts: GuardFacts, t: unknown, truth: boolean): void {
  const o = t as Record<string, unknown>;
  for (const key of ["eq", "ne"]) {
    const pair = o[key];
    if (!Array.isArray(pair) || typeof pair[0] !== "string" || typeof pair[1] !== "string" || (key === "eq") !== truth) continue;
    if ([pair[0], pair[1]].some((x) => { const ty = findLine(facts.data, x)?.type; return !ty || ty === "Count"; })) return;
    facts.rel ??= new Set();
    facts.rel.add(`eq|${pair[0]}|${pair[1]}`);
    return;
  }
  for (const key of ["lt", "le", "gt", "ge"]) {
    const pair = o[key];
    if (!Array.isArray(pair) || typeof pair[0] !== "string" || typeof pair[1] !== "string") continue;
    if ([pair[0], pair[1]].some((x) => { const ty = findLine(facts.data, x)?.type; return !ty || ty === "Count"; })) return;
    const k = truth ? key : NEGATE[key]!;
    const [a, b] = k === "lt" || k === "le" ? [pair[0], pair[1]] : [pair[1], pair[0]];
    facts.rel ??= new Set();
    facts.rel.add(`le|${a}|${b}`);
    if (k === "lt" || k === "gt") facts.rel.add(`lt|${a}|${b}`);
    return;
  }
}

function guardFacts(data: CanonicalData, g: unknown): GuardFacts {
  const facts: GuardFacts = { data, same: new Set(), known: new Map() };
  addTest(facts, g, true, 0);
  return facts;
}

// The value test t must have wherever the facts hold, or undefined when they do not settle it. A settled
// value is one the evaluator returns: every line it depends on is known from the facts, and an all-test
// (any-test) is false (true) only at a conjunct settled so after earlier ones all settled the other way.
function decides(t: unknown, facts: GuardFacts, depth = 0): boolean | undefined {
  if (depth > 8) return undefined;
  if (facts.same.has(stableStringify(t))) return true;
  const o = t as { all?: unknown[]; any?: unknown[]; not?: unknown };
  if (Array.isArray(o.all) || Array.isArray(o.any)) {
    const isAll = Array.isArray(o.all);
    for (const x of (o.all ?? o.any)!) {
      const v = decides(x, facts, depth + 1);
      if (v === undefined) return undefined;
      if (v !== isAll) return !isAll;
    }
    return isAll;
  }
  if (o.not !== undefined) { const v = decides(o.not, facts, depth + 1); return v === undefined ? undefined : !v; }
  const cmp = comparison(facts.data, t);
  if (!cmp) return undefined;
  const v = cmp.v;
  const f = facts.known.get(cmp.line);
  if (!f) {
    const flag = findLine(facts.data, cmp.line);
    if (flag && !(flag.refuses ?? []).length && flag.expr.op === "test" && typeof v === "boolean" && (cmp.key === "eq" || cmp.key === "ne")) {
      const fv = decides(flag.expr, facts, depth + 1);
      return fv === undefined ? undefined : (cmp.key === "eq") === (fv === v);
    }
    // An ungated Bool or enum choose: its guards settled in order up to the first true one, and that
    // alternative's value settled (a parameter's, or the comparison of the line it takes).
    const alts = flag && !(flag.refuses ?? []).length && (typeof v === "boolean" || typeof v === "string") && (cmp.key === "eq" || cmp.key === "ne")
      ? scalarChoose(facts.data, cmp.line) : undefined;
    for (const a of alts ?? []) {
      const g = decides(a.guard, facts, depth + 1);
      if (g === undefined) return undefined;
      if (!g) continue;
      if (a.fixed !== undefined) return (cmp.key === "eq") === (a.fixed === v);
      return decides({ op: "test", [cmp.key]: [a.then, { const: v }] }, facts, depth + 1);
    }
    return undefined;
  }
  if (f.eq !== undefined) {
    const x = JSON.parse(f.eq) as unknown;
    if (cmp.key === "eq") return stableStringify(x) === stableStringify(v);
    if (cmp.key === "ne") return stableStringify(x) !== stableStringify(v);
    if (typeof x !== "number" || typeof v !== "number") return undefined;
    return cmp.key === "lt" ? x < v : cmp.key === "le" ? x <= v : cmp.key === "gt" ? x > v : x >= v;
  }
  if (f.not?.includes(stableStringify(v)) && (cmp.key === "eq" || cmp.key === "ne")) return cmp.key === "ne";
  if (typeof v !== "number") return undefined;
  const below = (n: number) => f.hi !== undefined && (f.hi < n || (f.hi === n && !!f.hiStrict));
  const belowEq = (n: number) => f.hi !== undefined && f.hi <= n;
  const above = (n: number) => f.lo !== undefined && (f.lo > n || (f.lo === n && !!f.loStrict));
  const aboveEq = (n: number) => f.lo !== undefined && f.lo >= n;
  switch (cmp.key) {
    case "lt": return below(v) ? true : aboveEq(v) ? false : undefined;
    case "le": return belowEq(v) ? true : above(v) ? false : undefined;
    case "gt": return above(v) ? true : belowEq(v) ? false : undefined;
    case "ge": return aboveEq(v) ? true : below(v) ? false : undefined;
    case "eq": return below(v) || above(v) ? false : undefined;
    case "ne": return below(v) || above(v) ? true : undefined;
  }
  return undefined;
}

const ZERO_OPS = new Set(["sum", "subtract", "subtract_floor0", "round", "smaller_of", "larger_of"]);

// The value a line has wherever the facts hold, as a normal form. Lines whose refusal gates are all among
// the mutated line's own gates (already evaluated false when its expression is reached) count as ungated.
// A choose the facts settle is replaced by its taken branch; a copy by its source; a non-negative line the
// facts bound at zero, a zero parameter, and arithmetic of zeros (and a rate or count of a zero amount by
// a parameter) are the zero; anything else is its copy-chain normal form.
function underGuard(data: CanonicalData, id: string, facts: GuardFacts, known: Set<string>, depth = 0): string {
  const ZERO = "ZERO";
  const l = findLine(data, id);
  const plain = (): string => {
    const n = normalizeChain(data, id, known) as { parameter?: unknown };
    return n.parameter === 0 ? ZERO : stableStringify(n);
  };
  if (!l || depth > 10 || !(l.refuses ?? []).every((r) => known.has(r.when))) return plain();
  const f = facts.known.get(id);
  if (f && (l.type === "NonNegDollars" || l.type === "Count") && (f.eq === "0" || (f.hi === 0 && !f.hiStrict))) return ZERO;
  const e = l.expr as Record<string, unknown>;
  if (e.op === "choose") {
    for (const alt of e.alternatives as { guard: unknown; then: unknown }[]) {
      const v = decides(alt.guard, facts);
      if (v === undefined) break;
      if (v) return typeof alt.then === "string" ? underGuard(data, alt.then, facts, known, depth + 1) : plain();
    }
    return plain();
  }
  if (e.op === "copy" && typeof e.from === "string") return underGuard(data, e.from, facts, known, depth + 1);
  if (e.op === "param") return plain();
  const sub = (x: unknown): string | undefined => typeof x === "string" ? underGuard(data, x, facts, known, depth + 1) : undefined;
  const fixed = (x: unknown): boolean => x !== null && typeof x === "object" && ("param" in x || "const" in x);
  if (ZERO_OPS.has(e.op as string)) {
    const ops = e.op === "sum" || e.op === "smaller_of" || e.op === "larger_of" ? (e.of as unknown[]) : e.op === "round" ? [e.of] : [e.from, e.take];
    if (ops.every((x) => fixed(x) ? (x as { const?: unknown }).const === 0 || data.params.values[(x as { param: string }).param]?.value === 0 : sub(x) === ZERO)) return ZERO;
  }
  if (e.op === "multiply_rate" || e.op === "multiply_count") {
    const other = e.op === "multiply_rate" ? e.rate : e.count;
    const otherFixed = fixed(other) || (typeof other === "string" && (normalizeChain(data, other, known) as { parameter?: unknown }).parameter !== undefined);
    if (sub(e.amount) === ZERO && otherFixed) return ZERO;
  }
  return plain();
}

// Branch value settled by its guard: a choose alternative's value X is replaced by Y, and where that
// alternative's guard holds (so its earlier guards are false and every line the guard compares is
// complete), X and Y reduce to the same value under the facts the guard gives, so the mutated line's
// value is unchanged at every input.
function settledBranch(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const m = /\.then(\d+)$/.exec(mutation.id); if (!m) return undefined;
  const line = findLine(data, lineOf(mutation));
  if (line?.expr.op !== "choose") return undefined;
  const alt = (line.expr.alternatives as { guard: unknown; then: unknown }[])[Number(m[1])];
  if (!alt || alt.then !== pair[0]) return undefined;
  const facts = guardFacts(data, alt.guard);
  const known = new Set((line.refuses ?? []).filter((r) => !r.when_known).map((r) => r.when));
  const a = underGuard(data, pair[0], facts, known), b = underGuard(data, pair[1], facts, known);
  if (a !== b) return undefined;
  const blind = refusalBlind(data, pair[0], pair[1]);
  if (!unknownGuardSafe(data, line, Number(m[1]), pair[0], pair[1])) return undefined;
  return `Branch settled by its guard: where ${lineOf(mutation)} takes alternative ${m[1]} (guard ${stableStringify(alt.guard)}), the lines that guard compares are complete and fix the choices that ${pair[0]} and ${pair[1]} make, and both reduce to ${a === "ZERO" ? "the zero" : "the same value"} (through settled choices, copies${a === "ZERO" ? " and arithmetic of zeros" : ""}, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since ${blind ? `neither ${pair[0]} nor ${pair[1]} ever refuses` : "the values compared, or another alternative still possible, cannot refuse while the guard is unknown"} (spec 4.7.3); so the mutated line is unchanged at every input.`;
}

// Unreachable alternative: the mutated line is a helper, and every printed line reads it only through
// choices whose guards make some ungated Bool line F (a test, or a choose) true (path dominance, as for a guarded figure);
// F true settles the replaced alternative's guard false, so wherever a printed value depends on the
// helper that alternative is not taken, and its value is never read there.
function unreachableAlternative(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair) return undefined;
  const m = /\.then(\d+)$/.exec(mutation.id); if (!m) return undefined;
  const id = lineOf(mutation), line = findLine(data, id), doc = docOfLine(data, id);
  if (!line || !doc || line.expr.op !== "choose" || !isHelper(data, id)) return undefined;
  const alt = (line.expr.alternatives as { guard: unknown; then: unknown }[])[Number(m[1])];
  if (!alt || alt.then !== pair[0]) return undefined;
  const blind = refusalBlind(data, pair[0], pair[1]);
  if (!unknownGuardSafe(data, line, Number(m[1]), pair[0], pair[1])) return undefined;
  for (const f of doc.lines) {
    if (f.type !== "Bool" || !(f.expr.op === "test" || scalarChoose(data, f.id)) || (f.refuses ?? []).length) continue;
    if (decides(alt.guard, guardFacts(data, { op: "test", eq: [f.id, { const: true }] })) !== false) continue;
    if (!dominatedBy(data, id, f.id, blind)) continue;
    return `Unreachable alternative: ${id} is a helper that every printed line reads only through choices whose guards make ${f.id} true, and ${f.id} true makes the guard of alternative ${m[1]} (${stableStringify(alt.guard)}) false; where ${id}'s guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (${blind ? `neither ${pair[0]} nor ${pair[1]} ever refuses` : "the values compared, or another alternative still possible, cannot refuse while the guard is unknown"}; spec 4.7.3); so wherever a printed value depends on ${id} that alternative is not taken, and replacing its value changes no printed value.`;
  }
  return undefined;
}

// Case split. An abstract value of a line, under the facts of a path and an assignment of some split
// lines: a complete known value (its normal form: cents, a Boolean or an enum value), the line's own
// value not reduced further (the same value on both routes, complete or not), or exactly the
// incomplete value (an unknown or a refusal) of split line s.
type Abs = { k: "known"; v: string } | { k: "line"; v: string } | { k: "inc"; s: string };
const INC = "\u0000incomplete";
type SplitEnv = { facts: GuardFacts; known: Set<string>; split: Map<string, unknown>; memo?: Map<string, Abs> };
const kn = (v: unknown): Abs => ({ k: "known", v: JSON.stringify(v) });

// A parameter's value when it is complete whatever the inputs: a scalar or a rate, not a value keyed by
// filing status (which reads f1040.status).
function fixedParam(data: CanonicalData, ref: string | undefined): unknown {
  const pv = ref === undefined ? undefined : data.params.values[ref]?.value;
  if (pv === undefined || pv === null) return undefined;
  if (typeof pv === "object" && !("num" in pv && "den" in pv)) return undefined;
  return pv;
}

function absOperand(data: CanonicalData, x: unknown, env: SplitEnv, depth: number): Abs | undefined {
  if (typeof x === "string") return absLine(data, x, env, depth);
  if (x === null || typeof x !== "object") return undefined;
  if ("const" in x) return kn((x as { const: unknown }).const);
  const pv = fixedParam(data, (x as { param?: string }).param);
  return pv === undefined ? undefined : kn(pv);
}

// A test's value under the environment (spec 4.7.2): true, false, the split line's incomplete value, or
// undefined when the environment does not settle it. An incomplete conjunct settles an all-test (any-test)
// only when every later conjunct is settled and does not decide, since a refusal ends the test at once and
// an unknown lets a later deciding conjunct win. A comparison evaluates both sides, so an incomplete side
// is its value only when the other side is complete or the same incomplete value. Split lines are Bool or
// enum lines, whose incomplete values carry no count lower bound (4.7.5).
function absTest(data: CanonicalData, t: unknown, env: SplitEnv, depth: number): boolean | { inc: string } | undefined {
  if (depth > 60) return undefined;
  if (env.facts.same.has(stableStringify(t))) return true;
  const o = t as { all?: unknown[]; any?: unknown[]; not?: unknown } & Record<string, unknown>;
  if (Array.isArray(o.all) || Array.isArray(o.any)) {
    const isAll = Array.isArray(o.all);
    let inc: { inc: string } | undefined;
    // A conjunct not settled but reading only lines that can never refuse is a value or an unknown, and
    // a later deciding conjunct wins over either (4.7.2).
    let soft = false;
    for (const x of (o.all ?? o.any)!) {
      const v = absTest(data, x, env, depth + 1);
      if (v === undefined) {
        if (operandRefs(data, x).every((r) => neverRefuses(data, r) && !env.split.has(r))) { soft = true; continue; }
        return undefined;
      }
      if (typeof v === "object") { if (inc && inc.inc !== v.inc) return undefined; inc = v; continue; }
      if (v !== isAll) return inc ? undefined : !isAll;
    }
    return soft ? undefined : inc ?? isAll;
  }
  if (o.not !== undefined) { const v = absTest(data, o.not, env, depth + 1); return typeof v === "boolean" ? !v : v; }
  for (const key of ["eq", "ne", "lt", "le", "gt", "ge"]) {
    const pair = o[key];
    if (!Array.isArray(pair)) continue;
    const a = absOperand(data, pair[0], env, depth + 1), b = absOperand(data, pair[1], env, depth + 1);
    if (a?.k === "inc" || b?.k === "inc") {
      const s = a?.k === "inc" ? a.s : (b as { s: string }).s;
      const fits = (x: Abs | undefined): boolean => x?.k === "known" || (x?.k === "inc" && x.s === s);
      return fits(a) && fits(b) ? { inc: s } : undefined;
    }
    if (a?.k === "known" && b?.k === "known") {
      const x = JSON.parse(a.v) as unknown, y = JSON.parse(b.v) as unknown;
      if (key === "eq") return a.v === b.v;
      if (key === "ne") return a.v !== b.v;
      if (typeof x !== "number" || typeof y !== "number") return undefined;
      return key === "lt" ? x < y : key === "le" ? x <= y : key === "gt" ? x > y : x >= y;
    }
    break;
  }
  return decides(t, env.facts);
}

// Whether a line's value can never be a refusal: it has no refusal gates, and it is an input, a parameter,
// or an atom (a sum over a collection included, with its filter) reading only such lines.
const neverRefusesMemo = new WeakMap<CanonicalData, Map<string, boolean>>();
function neverRefuses(data: CanonicalData, id: string, depth = 0): boolean {
  let memo = neverRefusesMemo.get(data);
  if (!memo) { memo = new Map(); neverRefusesMemo.set(data, memo); }
  const hit = memo.get(id);
  if (hit !== undefined) return hit;
  const l = findLine(data, id);
  let v = false;
  if (l && depth < 30 && !(l.refuses ?? []).length) {
    const e = l.expr as Record<string, unknown>;
    if (e.op === "input" || e.op === "param") v = true;
    else if (e.op !== "copy" || typeof e.from === "string") {
      const isDefCall = JSON.stringify(e).includes('"def"');
      v = !isDefCall && operandRefs(data, e).every((r) => neverRefuses(data, r, depth + 1));
    }
  }
  memo.set(id, v);
  return v;
}

function absLine(data: CanonicalData, id: string, env: SplitEnv, depth: number): Abs {
  const hit = env.memo?.get(id);
  if (hit) return hit;
  const v = absLineRaw(data, id, env, depth);
  if (depth <= 60) env.memo?.set(id, v);
  return v;
}

function absLineRaw(data: CanonicalData, id: string, env: SplitEnv, depth: number): Abs {
  if (env.split.has(id)) {
    const v = env.split.get(id);
    return v === INC ? { k: "inc", s: id } : kn(v);
  }
  const n = normalizeChain(data, id, env.known) as { parameter?: unknown };
  const fixed = n.parameter !== undefined && (typeof n.parameter !== "object" || (n.parameter !== null && "num" in n.parameter));
  const opaque: Abs = fixed ? kn(n.parameter) : { k: "line", v: stableStringify(n) };
  const l = findLine(data, id);
  if (!l || depth > 60) return opaque;
  const f = env.facts.known.get(id);
  if (f?.eq !== undefined) return kn(JSON.parse(f.eq));
  if (f && (l.type === "NonNegDollars" || l.type === "Count") && f.hi === 0 && !f.hiStrict) return kn(0);
  for (const r of l.refuses ?? []) {
    if (env.known.has(r.when)) continue;
    if (r.when_known) return opaque;
    const g = absLine(data, r.when, env, depth + 1);
    if (g.k === "known" && g.v === "false") continue;
    return g.k === "inc" ? g : opaque;
  }
  // A line that is never negative and, by a settled comparison, not more than a complete zero is zero.
  if (["NonNegDollars", "Count"].includes(l.type)) {
    for (const r of env.facts.rel ?? []) {
      if (!r.startsWith(`le|${id}|`)) continue;
      const z = absLine(data, r.slice(4 + id.length), env, depth + 1);
      if (z.k === "known" && z.v === "0") return kn(0);
    }
  }
  // An equality settled by a comparison of two complete lines: the line is its partner's value.
  const partner = [...(env.facts.rel ?? [])].find((r) => r.startsWith(`eq|${id}|`));
  if (partner) return absLine(data, partner.slice(4 + id.length), env, depth + 1);
  const e = l.expr as Record<string, unknown>;
  // An atom's value is a function of its operands' values (and of its fixed fields), read in a fixed
  // order: the same atom applied to the same abstract values is the same value, refusals and unknowns
  // included (spec 4.7.2 to 4.7.4).
  const atom = (vals: (Abs | undefined)[]): Abs => vals.some((v) => v === undefined) ? opaque
    : { k: "line", v: "atom:" + createHash("sha256").update(stableStringify({ shape: Object.fromEntries(Object.entries(e).filter(([k]) => !["of", "from", "take", "amount", "rate", "count", "key", "status", "keys", "cite", "alternatives"].includes(k))), vals })).digest("hex").slice(0, 32) };
  // A test or guard not settled: the test itself, with the abstract values of the lines it reads.
  const testForm = (t: unknown): Abs | undefined => {
    const refs = operandRefs(data, t);
    const vals = refs.map((r) => absLine(data, r, env, depth + 1));
    return { k: "line", v: stableStringify({ t, vals }) };
  };
  if (e.op === "choose") {
    const parts: (Abs | undefined)[] = [];
    const alts = e.alternatives as { guard: unknown; then: unknown }[];
    for (const [i, alt] of alts.entries()) {
      const g = absTest(data, alt.guard, env, depth + 1);
      if (typeof g === "object") {
        // Past an unknown guard every alternative still possible is evaluated (spec 4.7.3): the line is the
        // guard's incomplete value when it can never refuse on every way, and otherwise a function of that
        // value and of the guards and values of the alternatives from this one on.
        const inc: Abs = { k: "inc", s: g.inc };
        if (otherQuiet(data, l, new Set())) return parts.length ? atom([...parts, inc]) : inc;
        return atom([...parts, inc, ...alts.slice(i).flatMap((a) => [testForm(a.guard), typeof a.then === "string" ? absLine(data, a.then, env, depth + 1) : undefined])]);
      }
      if (g === false) continue;
      const then = typeof alt.then === "string" ? absLine(data, alt.then, env, depth + 1) : undefined;
      if (g === true) return parts.length ? atom([...parts, then]) : then ?? opaque;
      parts.push(testForm(alt.guard), then);
    }
    return parts.length ? atom(parts) : opaque;
  }
  if (e.op === "copy") return typeof e.from === "string" ? absLine(data, e.from, env, depth + 1) : opaque;
  if (e.op === "test") {
    const v = absTest(data, e, env, depth + 1);
    return v === undefined ? atom([testForm(e)]) : typeof v === "object" ? { k: "inc", s: v.inc } : kn(v);
  }
  // A sum over a collection whose roster the facts show to be empty: a count, in the same document, of a
  // positive constant per entry with no filter is complete and not more than zero, so the roster was
  // confirmed and has no entries, and every sum over it is zero (4.7.5).
  if (e.op === "sum_over") {
    const home = docOfLine(data, id)?.id;
    for (const [other, b] of env.facts.known) {
      if (!(b.eq === "0\n" || b.eq === "0" || (b.hi !== undefined && b.hi <= 0))) continue;
      const ol = findLine(data, other);
      const oe = ol?.expr as Record<string, unknown> | undefined;
      if (!ol || oe?.op !== "sum_over" || oe.where || oe.collection !== e.collection || docOfLine(data, other)?.id !== home || (ol.refuses ?? []).length) continue;
      const per = typeof oe.field === "string" ? normalizeChain(data, oe.field) as { parameter?: unknown } : undefined;
      if (typeof per?.parameter === "number" && per.parameter > 0) return kn(0);
    }
  }
  if (e.op === "table_lookup" || e.op === "rate_lookup") return atom([absOperand(data, e.key, env, depth + 1), e.status === undefined ? kn(null) : absOperand(data, e.status, env, depth + 1)]);
  if (e.op === "keyed_lookup") return atom(((e.keys ?? []) as unknown[]).map((x) => absOperand(data, x, env, depth + 1)));
  const ops = ZERO_OPS.has(e.op as string) ? (e.op === "sum" || e.op === "smaller_of" || e.op === "larger_of" ? (e.of as unknown[]) : e.op === "round" ? [e.of] : [e.from, e.take])
    : e.op === "multiply_rate" ? [e.amount, e.rate] : e.op === "multiply_count" ? [e.amount, e.count] : undefined;
  if (!ops) return opaque;
  const vals = ops.map((x) => absOperand(data, x, env, depth + 1));
  const inc = vals.find((v) => v?.k === "inc") as { s: string } | undefined;
  if (inc && vals.every((v) => v?.k === "known" || (v?.k === "inc" && v.s === inc.s))) return { k: "inc", s: inc.s };
  // A subtraction of the same two values, in the same order, as an incomplete split comparison: both
  // evaluate both operands and return the first refusal, else the first unknown (4.7.2, 4.7.4), so the
  // subtraction is that incomplete value.
  if ((e.op === "subtract" || e.op === "subtract_floor0") && vals.length === 2) {
    for (const [s, v] of env.split) {
      if (v !== INC) continue;
      const sl = findLine(data, s);
      if (!sl || (sl.refuses ?? []).length || sl.expr.op !== "test") continue;
      const se = sl.expr as Record<string, unknown>;
      const pair = ["eq", "ne", "lt", "le", "gt", "ge"].map((k) => se[k]).find(Array.isArray) as unknown[] | undefined;
      if (!pair || typeof pair[0] !== "string" || typeof pair[1] !== "string") continue;
      if ([pair[0], pair[1]].some((x) => (findLine(data, x)?.type ?? "Count") === "Count")) continue;
      const sa = absOperand(data, pair[0], env, depth + 1), sb = absOperand(data, pair[1], env, depth + 1);
      if (stableStringify([sa, sb]) === stableStringify(vals)) return { k: "inc", s };
    }
  }
  // Atoms of complete amounts (cents) are computed: sums, differences, floors at zero and smaller/larger.
  const nums = vals.map((v) => v?.k === "known" ? JSON.parse(v.v) as unknown : undefined);
  if (nums.length && nums.every((n) => typeof n === "number")) {
    const ns = nums as number[];
    if (e.op === "sum") return kn(ns.reduce((a, b) => a + b, 0));
    if (e.op === "smaller_of") return kn(Math.min(...ns));
    if (e.op === "larger_of") return kn(Math.max(...ns));
    if (e.op === "subtract") return kn(ns[0]! - ns[1]!);
    if (e.op === "subtract_floor0") return kn(Math.max(0, ns[0]! - ns[1]!));
  }
  // The smaller (larger) of two lines whose order a settled comparison fixed, both complete, is the
  // first (second) of the ordered pair.
  if ((e.op === "smaller_of" || e.op === "larger_of") && ops.length === 2 && typeof ops[0] === "string" && typeof ops[1] === "string") {
    const [p, q] = ops as [string, string];
    const le = (a: string, b: string): boolean => !!env.facts.rel?.has(`le|${a}|${b}`);
    if (le(p, q)) return absLine(data, e.op === "smaller_of" ? p : q, env, depth + 1);
    if (le(q, p)) return absLine(data, e.op === "smaller_of" ? q : p, env, depth + 1);
  }
  // The smaller or larger of equal values is that value.
  if ((e.op === "smaller_of" || e.op === "larger_of") && vals.length > 0 && vals.every((v) => v !== undefined && stableStringify(v) === stableStringify(vals[0]))) return vals[0]!;
  const zero = (v: Abs | undefined): boolean => v?.k === "known" && v.v === "0";
  if (ZERO_OPS.has(e.op as string) ? vals.every(zero) : zero(vals[0]) && vals[1]?.k === "known") return kn(0);
  // A from-line not more than the take-line (both complete, by a settled comparison) floors to zero.
  if (e.op === "subtract_floor0" && typeof e.from === "string" && typeof e.take === "string" && env.facts.rel?.has(`le|${e.from}|${e.take}`)) return kn(0);
  // Arithmetic with complete zeros is its one other operand: a sum of it and zeros, it less a zero, and
  // (for a line that is never negative) it less a zero floored at zero. The zeros are complete, so an
  // incomplete operand is the result on both routes.
  const rest = ops.filter((_, i) => !zero(vals[i]));
  const only = rest.length === 1 && typeof rest[0] === "string" ? rest[0] : undefined;
  const nonNeg = (x: string): boolean => ["NonNegDollars", "Count"].includes(findLine(data, x)?.type ?? "");
  if (only && (e.op === "sum" || ((e.op === "subtract" || (e.op === "subtract_floor0" && nonNeg(only))) && e.from === only))) return absLine(data, only, env, depth + 1);
  // Otherwise the atom applied to its operands' abstract values: the same atom of the same values, read in
  // the same order, is the same value, refusals and unknowns included (spec 4.7.4).
  if (vals.some((v) => v === undefined)) return opaque;
  const shape = Object.fromEntries(Object.entries(e).filter(([k]) => !["of", "from", "take", "amount", "rate", "count", "cite"].includes(k)));
  return { k: "line", v: "atom:" + createHash("sha256").update(stableStringify({ shape, vals })).digest("hex").slice(0, 32) };
}

// The facts with split line s set to v: a test line's own test, true or false, adds what it establishes; a Bool
// or enum choose (scalarChoose) at a value adds what that value establishes about the alternative taken.
function factsWith(data: CanonicalData, facts: GuardFacts, s: string, v: unknown): GuardFacts {
  const l = findLine(data, s);
  const isTest = typeof v === "boolean" && l?.expr.op === "test";
  const isChoose = (typeof v === "boolean" || (typeof v === "string" && v !== INC)) && !!scalarChoose(data, s);
  if (!isTest && !isChoose) return facts;
  const next: GuardFacts = { data, same: new Set(facts.same), known: new Map([...facts.known].map(([k, b]): [string, Bound] => [k, b.not ? { ...b, not: [...b.not] } : { ...b }])), rel: new Set(facts.rel ?? []) };
  if (isTest) addTest(next, l!.expr, v as boolean, 0);
  else addTest(next, { op: "test", eq: [s, { const: v }] }, true, 0);
  return next;
}

// The guards that hold wherever a helper's value reaches a printed line: while the line has exactly one
// reader, in its own document, which takes it only as the value of one alternative whose value its unknown
// guards hide (or, with `refusalsSame`, an ungated choose taking it as a line-valued alternative, as for
// dominatedBy), that alternative's guard, and then its reader's.
function pathGuards(data: CanonicalData, id: string, refusalsSame = false, depth = 0): unknown[] {
  if (depth > 8 || !isHelper(data, id)) return [];
  const steps = readerSteps(data, id);
  if (steps.length !== 1) return [];
  const s = steps[0]!;
  if (!s.fact || !s.fact.length || !(s.hidden || (refusalsSame && s.transparent)) || s.doc.id !== docOfLine(data, id)?.id) return [];
  if (s.fact.length === 1) return [s.fact[0], ...pathGuards(data, s.reader.id, refusalsSame, depth + 1)];
  // Several alternatives that each test one enum line against a value: the line is complete and has
  // none of the other values.
  const eqs = s.fact.map((g) => comparison(data, g));
  const enumLine = eqs[0]?.line, ty = enumLine ? findLine(data, enumLine)?.type ?? "" : "";
  if (!enumLine || !ty.startsWith("Enum(") || !eqs.every((c) => c?.key === "eq" && c.line === enumLine && typeof c.v === "string")) return [];
  const taken = new Set(eqs.map((c) => c!.v as string));
  const others = (data.params.enums[ty.slice(5, -1)]?.values ?? []).filter((v) => !taken.has(v));
  if (!others.length) return [];
  return [{ op: "test", all: others.map((v) => ({ op: "test", ne: [enumLine, { const: v }] })) }, ...pathGuards(data, s.reader.id, refusalsSame, depth + 1)];
}

// Split candidates: Bool and enum lines compared in the guards of chooses reachable from the operands.
function splitCandidates(data: CanonicalData, roots: string[]): string[] {
  const out: string[] = [];
  const seen = new Set<string>();
  const walk = (id: string, depth: number): void => {
    if (depth > 8 || seen.has(id)) return;
    seen.add(id);
    const l = findLine(data, id);
    if (!l) return;
    const e = l.expr as Record<string, unknown>;
    const tests = e.op === "choose" ? (e.alternatives as { guard: unknown }[]).map((a) => a.guard) : e.op === "test" ? [e] : [];
    for (const t of tests) for (const r of operandRefs(data, t)) {
      const ty = findLine(data, r)?.type ?? "";
      if ((ty === "Bool" || ty.startsWith("Enum(")) && !out.includes(r)) out.push(r);
    }
    for (const r of operandRefs(data, e)) walk(r, depth + 1);
  };
  roots.forEach((r) => walk(r, 0));
  return out.slice(0, 12);
}

// Branch value equal under a case split: a choose alternative's value X is replaced by Y. Under the facts
// that hold where the alternative is taken (its guard, and for a helper the guards on its one reader path
// to a printed line), X and Y are evaluated abstractly; where that does not settle them, a Bool or enum line
// S that their choices test is split into each of its values and "incomplete" (S's own unknown or refusal,
// which a choose guard, a comparison against complete values and a gate pass on unchanged), up to three
// splits deep. The mutant is equivalent when X and Y have the same abstract value in every case.
function caseSplitBranch(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const m = /\.then(\d+)$/.exec(mutation.id); if (!m) return undefined;
  const id = lineOf(mutation), line = findLine(data, id);
  if (line?.expr.op !== "choose") return undefined;
  const alt = (line.expr.alternatives as { guard: unknown; then: unknown }[])[Number(m[1])];
  if (!alt || alt.then !== pair[0]) return undefined;
  const blind = refusalBlind(data, pair[0], pair[1]);
  if (!unknownGuardSafe(data, line, Number(m[1]), pair[0], pair[1])) return undefined;
  const path = pathGuards(data, id, blind);
  const facts = guardFacts(data, { op: "test", all: [alt.guard, ...path] });
  const known = new Set((line.refuses ?? []).filter((r) => !r.when_known).map((r) => r.when));
  const candidates = splitCandidates(data, pair);
  const domain = (s: string): unknown[] => {
    const t = findLine(data, s)!.type;
    return t === "Bool" ? [true, false, INC] : [...(data.params.enums[t.slice(5, -1)]?.values ?? []), INC];
  };
  const used: string[] = [];
  let cases = 0;
  const prove = (f: GuardFacts, split: Map<string, unknown>, left: number): boolean => {
    if (++cases > 2000) return false;
    const env: SplitEnv = { facts: f, known, split, memo: new Map() };
    const a = absLine(data, pair[0], env, 0), b = absLine(data, pair[1], env, 0);
    if (a.k === b.k && (a.k === "inc" ? a.s === (b as { s: string }).s : a.v === (b as { v: string }).v)) return true;
    if (left === 0) return false;
    for (const s of candidates) {
      if (split.has(s) || absLine(data, s, env, 0).k !== "line") continue;
      if (domain(s).every((v) => prove(factsWith(data, f, s, v), new Map([...split, [s, v]]), left - 1))) { if (!used.includes(s)) used.push(s); return true; }
    }
    return false;
  };
  if (!prove(facts, new Map(), 3)) return undefined;
  return `Branch equal under a case split: where ${id} takes alternative ${m[1]} (guard ${stableStringify(alt.guard)})${path.length ? ` and its value can reach a printed line (guards ${path.map((g) => stableStringify(g)).join(", ")} on its one reader path)` : ""}, ${pair[0]} and ${pair[1]} have the same value${used.length ? ` in every case of ${used.join(", ")} (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged)` : ""}, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so ${path.length ? "no printed value changes" : "the mutated line is unchanged at every input"}.`;
}

// The conjuncts an all-test evaluates, in order: a conjunct `L == true`, with L a line of the same
// document (no def parameters) that has no refusal gates and is itself an all-test, is replaced by L's
// conjuncts, as is an inline all-test; anything else is one conjunct. An all-test returns the first
// refusal or false it meets, else an unknown if any conjunct was unknown, else true; a nested all-test
// returns the same thing to `== true`, which passes a refusal or unknown on, so the line and its
// expansion have the same value (unknowns compare equal, as in outcome()). Undefined on a cycle.
function conjunctsOf(data: CanonicalData, doc: FormDoc, expr: unknown, seen: Set<string>): string[] | undefined {
  const e = expr as { op?: string; all?: unknown[]; eq?: unknown[] };
  if (e?.op !== "test" || !Array.isArray(e.all)) return undefined;
  const out: string[] = [];
  for (const t of e.all) {
    const c = t as { op?: string; all?: unknown[]; eq?: unknown[] };
    const ref = c?.op === "test" && Array.isArray(c.eq) && typeof c.eq[0] === "string" && stableStringify(c.eq[1]) === stableStringify({ const: true }) ? c.eq[0] : undefined;
    const inner = ref ? doc.lines.find((l) => l.id === ref) : undefined;
    if (ref && seen.has(ref)) return undefined;
    const expand = c?.op === "test" && Array.isArray(c.all) ? conjunctsOf(data, doc, c, seen)
      : inner && !(inner.refuses ?? []).length && inner.expr.op === "test" && "all" in inner.expr ? conjunctsOf(data, doc, inner.expr, new Set([...seen, ref!])) : null;
    if (expand === undefined) return undefined;
    if (expand) out.push(...expand); else out.push(stableStringify(c));
  }
  return out;
}

// Conjunct prefix: an operand of an all-test's conjunct replaced by a line whose conjuncts, read where
// the operand stood, repeat only conjuncts the test reads anyway and in the same first-read order. A
// conjunct met again has the value it had the first time (true or unknown, or the test would have
// stopped), so the all-test meets the same first refusal or false, or ends unknown or true, at every
// input. Checked on the expanded conjuncts of the mutated line before and after the mutation.
function conjunctPrefix(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair || !independentOperands(data, mutation, pair)) return undefined;
  const id = lineOf(mutation), doc = docOfLine(data, id), line = findLine(data, id);
  if (!doc || !line || (doc.parameters ?? []).length) return undefined;
  const before = conjunctsOf(data, doc, line.expr, new Set([id]));
  const mutated = cloneData(data); mutation.apply(mutated);
  const mdoc = docOfLine(mutated, id), mline = findLine(mutated, id);
  const after = mdoc && mline ? conjunctsOf(mutated, mdoc, mline.expr, new Set([id])) : undefined;
  if (!before || !after || stableStringify(before) === stableStringify(after)) return undefined;
  const firstRead = after.filter((c, i) => after.indexOf(c) === i);
  if (stableStringify(firstRead) !== stableStringify(before)) return undefined;
  return `Conjunct prefix: ${pair[1]} expands to conjuncts that ${id} reads anyway, in the same first-read order (${pair[0]} among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.`;
}

// The structural rules, checked against the current data for every survivor: the first that accepts
// it gives the reason.
export function structuralReason(data: CanonicalData, mutation: Mutation): string | undefined {
  return aliasEquivalence(data, mutation) ?? sharedGateEquivalence(data, mutation) ?? floorMinusMin(data, mutation)
    ?? carriedZero(data, mutation) ?? settledBranch(data, mutation) ?? unreachableAlternative(data, mutation) ?? caseSplitBranch(data, mutation) ?? guardedFigure(data, mutation) ?? unreadParameter(data, mutation) ?? unreadTable(data, mutation)
    ?? conjunctPrefix(data, mutation) ?? unobservedLine(data, mutation);
}

// Equivalences that need an argument about evaluation order or reachability. Each is
// accepted only while the structural facts it rests on hold in the current data; when
// they lapse, the mutant is reported as unexplained again, and an argument that explains no surviving mutant fails
// the run (staleEquivalences).
// A keyed conditional argument. `reads`, set on every pinned argument, is the line the argument says the
// mutant reads: a mutant id names only the replaced operand, and the replacement is the nearest earlier
// same-typed line, so a line inserted between them retargets the id while the premise digest is unchanged.
// `premises`, set on every argument that holds by a premise digest, is the list it digests.
type Conditional = { reason: string; holds: (data: CanonicalData) => boolean; reads?: string; premises?: string[] };

// ---- New York (forms/ny): rate schedules, tax computation worksheets and zero lines ----

function defOf(d: CanonicalData, id: string): FormDoc | undefined {
  return d.defs.find((x) => x.id === id);
}

function localLine(def: FormDoc, id: string): Line | undefined {
  return def.lines.find((l) => l.id === id);
}

function paramMoney(d: CanonicalData, name: string | undefined): number | undefined {
  const v = name === undefined ? undefined : d.params.values[name]?.value;
  return typeof v === "number" ? v : undefined;
}

function paramRefOf(x: unknown): string | undefined {
  return (x as { param?: string } | undefined)?.param;
}

// Every site in a form or def line that binds def `defId`: the line, the def it sits in (undefined for a form line) and its bindings.
function defBindings(d: CanonicalData, defId: string): { scope: FormDoc | undefined; line: Line; bind: Record<string, unknown> }[] {
  const out: { scope: FormDoc | undefined; line: Line; bind: Record<string, unknown> }[] = [];
  const walk = (n: unknown, scope: FormDoc | undefined, line: Line): void => {
    if (Array.isArray(n)) { for (const x of n) walk(x, scope, line); return; }
    if (n === null || typeof n !== "object") return;
    const o = n as Record<string, unknown>;
    if (o["def"] === defId && o["bind"] && typeof o["bind"] === "object") out.push({ scope, line, bind: o["bind"] as Record<string, unknown> });
    for (const v of Object.values(o)) walk(v, scope, line);
  };
  for (const f of d.forms) for (const l of f.lines) walk(l.expr, undefined, l);
  for (const f of d.defs) for (const l of f.lines) walk(l.expr, f, l);
  return out;
}

// Every line of any form or def that reads parameter `name` (as an operand or a `param` line).
function paramReaders(d: CanonicalData, name: string): { scope: FormDoc; line: Line }[] {
  const reads = (n: unknown): boolean => {
    if (Array.isArray(n)) return n.some(reads);
    if (n === null || typeof n !== "object") return false;
    const o = n as Record<string, unknown>;
    if (o["param"] === name || (o["op"] === "param" && o["ref"] === name)) return true;
    return Object.values(o).some(reads);
  };
  return allDocs(d).flatMap((scope) => scope.lines.filter((l) => reads(l.expr) || (l.refuses ?? []).some((r) => reads(r))).map((line) => ({ scope, line })));
}

// A money parameter (Dollars or NonNegDollars, a number or a status-keyed record of numbers) whose every value is a
// multiple of 100 cents. Counts, rates and other types are not money, whatever their value.
function wholeParam(d: CanonicalData, name: string): boolean {
  const entry = d.params.values[name];
  if (entry?.type !== "Dollars" && entry?.type !== "NonNegDollars") return false;
  const v = entry.value;
  if (typeof v === "number") return v % 100 === 0;
  return v !== null && typeof v === "object" && Object.values(v as Record<string, unknown>).every((x) => typeof x === "number" && x % 100 === 0);
}

// Self-test of wholeParam on synthetic parameters: whole-dollar money (a number and a status-keyed record) is whole;
// a Count, a Rate, and money with cents are not. Returns the problems found.
export function wholeParamSelfTest(): string[] {
  const values: Record<string, { type: string; value: unknown }> = {
    dollars: { type: "Dollars", value: 100 }, nonneg: { type: "NonNegDollars", value: 0 }, keyed: { type: "Dollars", value: { single: 800000, mfj: 1605000 } },
    count: { type: "Count", value: 100 }, rate: { type: "Rate", value: { num: 100, den: 1 } }, cents: { type: "Dollars", value: 150 }, keyedCents: { type: "Dollars", value: { single: 800000, mfj: 50 } },
  };
  const d = { params: { values } } as unknown as CanonicalData;
  const want: Record<string, boolean> = { dollars: true, nonneg: true, keyed: true, count: false, rate: false, cents: false, keyedCents: false };
  return Object.entries(want).filter(([n, w]) => wholeParam(d, n) !== w).map(([n, w]) => `wholeParam(${n}) is ${!w}, expected ${w}`);
}

// A value that is a whole number of dollars (a multiple of 100 cents) wherever it is complete: a rounding to
// whole dollars, a whole-dollar parameter or constant, or sums, differences, copies, counts of and choices among
// such values. A def parameter is whole when every binding of it, traced to its caller, is.
function wholeRef(d: CanonicalData, scope: FormDoc | undefined, ref: unknown, depth = 0): boolean {
  if (depth > 80) return false;
  if (typeof ref !== "string") {
    const p = paramRefOf(ref);
    if (p !== undefined) return wholeParam(d, p);
    const c = (ref as { const?: unknown } | undefined)?.const;
    return typeof c === "number" && c % 100 === 0;
  }
  if (scope) {
    const l = localLine(scope, ref);
    if (!l) return false;
    if (l.expr.op === "input" && (scope.parameters ?? []).includes(ref)) {
      const sites = defBindings(d, scope.id);
      return sites.length > 0 && sites.every((s) => ref in s.bind && wholeRef(d, s.scope, s.bind[ref], depth + 1));
    }
    return wholeExpr(d, scope, l.expr as unknown as Record<string, unknown>, depth + 1);
  }
  const l = d.forms.flatMap((f) => f.lines).find((x) => x.id === ref);
  return !!l && wholeExpr(d, undefined, l.expr as unknown as Record<string, unknown>, depth + 1);
}

function wholeExpr(d: CanonicalData, scope: FormDoc | undefined, e: Record<string, unknown>, depth: number): boolean {
  const w = (x: unknown): boolean => wholeRef(d, scope, x, depth);
  switch (e["op"]) {
    case "round": return typeof e["unit"] === "number" && e["unit"] % 100 === 0;
    case "param": return wholeParam(d, e["ref"] as string);
    case "copy": return typeof e["from"] === "string" && w(e["from"]);
    case "sum": return Array.isArray(e["of"]) && (e["of"] as unknown[]).every(w);
    case "subtract": case "subtract_floor0": return w(e["from"]) && w(e["take"]);
    case "multiply_count": return w(e["amount"]);
    case "choose": return (e["alternatives"] as { then: unknown }[]).every((a) => w(a.then));
    default: return false;
  }
}

// One band of a rate-schedule def: `<g>.b<k>.excess` (amount less the band's lower bound, floored), `.product`
// (the excess times the band's rate, rounded once to the whole dollar), `.base` and `.tax` (base plus product),
// none gated. Returns the band's parameters, or undefined when the def is not of that shape.
function bandShape(d: CanonicalData, def: FormDoc, g: string, k: number): { over: number; num: number; den: number; base: number; lines: string[] } | undefined {
  const p = `${g}.b${k}`;
  const ex = localLine(def, `${p}.excess`), pr = localLine(def, `${p}.product`), ba = localLine(def, `${p}.base`), tx = localLine(def, `${p}.tax`);
  if (!ex || !pr || !ba || !tx || [ex, pr, ba, tx].some((l) => (l.refuses ?? []).length)) return undefined;
  const e = ex.expr as unknown as Record<string, unknown>, r = pr.expr as unknown as Record<string, unknown>, b = ba.expr as unknown as Record<string, unknown>, t = tx.expr as unknown as Record<string, unknown>;
  if (e["op"] !== "subtract_floor0" || e["from"] !== "amount") return undefined;
  if (r["op"] !== "multiply_rate" || r["amount"] !== `${p}.excess` || r["unit"] !== 100) return undefined;
  if (b["op"] !== "param" || t["op"] !== "sum" || stableStringify([...(t["of"] as string[])].sort()) !== stableStringify([`${p}.base`, `${p}.product`])) return undefined;
  const over = paramMoney(d, paramRefOf(e["take"])), base = paramMoney(d, b["ref"] as string);
  const rate = d.params.values[paramRefOf(r["rate"]) ?? ""]?.value as { num?: number; den?: number } | undefined;
  if (over === undefined || base === undefined || typeof rate?.num !== "number" || typeof rate.den !== "number") return undefined;
  return { over, num: rate.num, den: rate.den, base, lines: [`${p}.excess`, `${p}.product`, `${p}.base`, `${p}.tax`] };
}

function bandTax(s: { over: number; num: number; den: number; base: number }, cents: number): number {
  return s.base + multiplyRateHalfUp(Math.max(cents - s.over, 0), s.num, s.den * 100) * 100;
}

// `<g>.result`: a choose whose alternative k-1 takes band k under all[amount above the previous edge (or at least 0),
// amount at most edge k] and whose last alternative takes the last band above the last edge. Returns the bands' edges
// (parameter names, the last undefined) or undefined when the result line is not of that shape.
function bandEdges(def: FormDoc, g: string): (string | undefined)[] | undefined {
  const res = localLine(def, `${g}.result`);
  if (!res || res.expr.op !== "choose" || (res.refuses ?? []).length) return undefined;
  const alts = res.expr.alternatives as { guard: unknown; then: unknown }[];
  const edges: (string | undefined)[] = [];
  for (let i = 0; i < alts.length; i++) {
    const a = alts[i]!, k = i + 1, prev = edges[i - 1];
    if (a.then !== `${g}.b${k}.tax`) return undefined;
    const lower = i === 0 ? { op: "test", ge: ["amount", { const: 0 }] } : { op: "test", gt: ["amount", { param: prev }] };
    if (i === alts.length - 1) {
      if (stableStringify(a.guard) !== stableStringify(lower)) return undefined;
      edges.push(undefined);
    } else {
      const all = (a.guard as { all?: unknown[] }).all;
      const le = (all?.[1] as { le?: unknown[] } | undefined)?.le;
      const edge = paramRefOf(le?.[1]);
      if (!all || all.length !== 2 || stableStringify(all[0]) !== stableStringify(lower) || le?.[0] !== "amount" || edge === undefined) return undefined;
      edges.push(edge);
    }
  }
  return edges;
}

function defAmountsWhole(d: CanonicalData, defId: string): boolean {
  const sites = defBindings(d, defId);
  return sites.length > 0 && sites.every((s) => "amount" in s.bind && wholeRef(d, s.scope, s.bind["amount"]));
}

// A band edge +$1 in a rate-schedule def: the edge is read only by the two guards of `<g>.result` that choose band k
// (amount at most the edge) or band k+1 (above it), so the mutant moves only amounts in (edge, edge + $1] from band
// k+1 to band k. Every amount the def is bound to is whole dollars, so only edge + $1 moves, and there the two
// bands' taxes are equal (computed from the current parameters on every run): the def's tax is unchanged at every input.
function bandEdge(defId: string, g: string, k: number) {
  const param = `${defId === "ny_rs" ? "ny.rs" : "ny.city"}.${g}.b${k}.upper`;
  return {
    reason: `Band edge ${param}: in def ${defId} it is read only by ${g}.result's guards choosing band ${k} (amount at most the edge) and band ${k + 1} (amount above it), so +$1 moves only amounts in (edge, edge + $1] from band ${k + 1} to band ${k}. Every binding of the def's amount is a whole-dollar line (each traced through copies, sums, differences, roundings to whole dollars and whole-dollar parameters, and through the worksheet defs' ti to Form IT-201 line 38, or to line 47), so only edge + $1 moves, and there band ${k}'s tax (base plus rate times the excess, rounded once to the whole dollar) equals band ${k + 1}'s, computed from the current parameters on every run: the def's tax is the same at every input, and so is every line that reads it.`,
    holds: (d: CanonicalData): boolean => {
      const def = defOf(d, defId), v = paramMoney(d, param);
      if (!def || v === undefined) return false;
      const edges = bandEdges(def, g), a = bandShape(d, def, g, k), b = bandShape(d, def, g, k + 1);
      if (!edges || edges[k - 1] !== param || !a || !b) return false;
      const readers = paramReaders(d, param);
      if (readers.length !== 1 || readers[0]!.scope.id !== defId || readers[0]!.line.id !== `${g}.result`) return false;
      return defAmountsWhole(d, defId) && bandTax(a, v + 100) === bandTax(b, v + 100);
    },
  };
}

function nyEquivalences(): Record<string, Conditional> {
  const out: Record<string, Conditional> = {};
  const edges: [string, string, number[]][] = [
    ["ny_rs", "single", [1, 2, 3, 4, 5, 6, 8]], ["ny_rs", "mfj", [1, 2, 3, 4, 5, 6, 7, 8]], ["ny_rs", "hoh", [1, 2, 3, 4, 5, 6, 8]],
    ["ny_city_rs", "single", [1, 2, 3]], ["ny_city_rs", "mfj", [1, 2, 3]], ["ny_city_rs", "hoh", [1, 2, 3]],
  ];
  for (const [def, g, ks] of edges) for (const k of ks) out[`param.${def === "ny_rs" ? "ny.rs" : "ny.city"}.${g}.b${k}.upper.$1`] = bandEdge(def, g, k);
  const mctmt = (param: string, line: string, what: string, digest: string): Conditional => {
    const lines = ["ny_it201.line54a", "ny_it201.line54b", "ny_it201.line54c", "ny_it201.line54d", "param:ny.zero"];
    return {
      premises: lines,
      reason: `${param} is read only by ${line}, the rate times ${what}, which is the parameter ny.zero ($0) behind ${what}'s MCTMT refusal gate (gate.mctmt, a refusal of ${what} where the MCTMT applies): with the gate a known false the product is $0 at any rate, and otherwise ${line} is ${what}'s refusal or unknown on both routes. (Premises pinned: ${lines.join(", ")}.)`,
      holds: (d) => premiseDigest(d, lines) === digest && d.params.values["ny.zero"]?.value === 0
        && stableStringify(paramReaders(d, param).map((r) => r.line.id)) === stableStringify([line]),
    };
  };
  out["param.ny.mctmt.zone1.+1pt"] = mctmt("ny.mctmt.zone1", "ny_it201.line54c", "line 54a", NY_MCTMT_DIGEST);
  out["param.ny.mctmt.zone2.+1pt"] = mctmt("ny.mctmt.zone2", "ny_it201.line54d", "line 54b", NY_MCTMT_DIGEST);
  const zeros = ["ny_it201.line54a", "ny_it201.line54b", "ny_it201.line54c", "ny_it201.line54d", "ny_it201.line55", "ny_it201.line56", "ny_it201.line57", "ny_it201.line54e", "ny_it201.line58", "param:ny.zero"];
  const zeroWhy = "Lines 55, 56 and 57 are the parameter ny.zero ($0, checked) with no refusal gate, so each is a complete $0 at every input. Lines 54a and 54b are ny.zero behind the same MCTMT refusal gate (gate.mctmt), and lines 54c and 54d are line 54a and line 54b times their zone's rate, rounded: with the gate a known false all four are a complete $0; otherwise 54a and 54b are the gate's refusal or unknown, and 54c and 54d carry it";
  out["operand.ny_it201.ny_it201.line54e.line54d"] = zeroPinned(`${zeroWhy}. Line 54e sums line 54c and line 54d; the mutant sums line 54c and line 54b. Line 54c is read first on both routes: with the gate not a known false it is the gate's refusal or unknown, which is the sum's value on both routes; with the gate a known false the second operand is $0 on both.`, zeros, NY_ZERO_DIGEST, "ny_it201.line54b");
  for (const n of [55, 56, 57]) out[`operand.ny_it201.ny_it201.line58.line${n}`] = zeroPinned(`${zeroWhy}. Line 58 sums lines 54, 54e, 55, 56 and 57; the mutant reads line 54d in place of line ${n}. With the gate a known false line 54d is a complete $0, the same as line ${n}, in the same position. Otherwise line 54e, in position 2 ahead of the replaced operand, already carries the gate's refusal or unknown (its first operand is line 54c), so the sum meets the same first refusal or unknown (from line 54 or 54e) on both routes.`, zeros, NY_ZERO_DIGEST, "ny_it201.line54d");
  for (const [i, status] of [[0, "single"], [2, "mfs"], [3, "hoh"], [4, "qss"]] as const) {
    out[`operand.ny_it201.ny_it201.gate.spouse_nonresident.no.then${i}`] = pinned(`gate.spouse_nonresident is a choice on the filing status: mfj takes spouse_not_resident, every other status takes ny_it201.no (the parameter ny.false); the mutant reads gate.part_year_city in place of ny_it201.no for ${status}. gate.spouse_nonresident is read only by ny_it201.line1, as its third refusal gate, after gate.part_year_city (the second); gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so gate.spouse_nonresident is read only where gate.part_year_city is a memoized false in the same frame (spec 4.7.6), the value of ny_it201.no. Where the status is unknown every alternative is a way (spec 4.7.3): ny_it201.no and the memoized gate.part_year_city are not refusals, and spouse_not_resident compares an input with no refusal gates, so the gate is the status's unknown on both routes.`,
      ["ny_it201.gate.spouse_nonresident", "ny_it201.line1", "ny_it201.gate.part_year_city", "ny_it201.ask.city_resident", "ny_it201.spouse_not_resident", "ny_it201.ask.spouse_resident", "ny_it201.no", "f1040.status", "param:ny.false"], "9e6619bae9d94b3a", "ny_it201.gate.part_year_city");
  }
  out["operand.ny_it201.ny_it201.line79.zero.then1"] = pinned("ny_it201.line79 is a choice on has_overpayment, the test 'line 77 more than $0': true takes line79_wanted, false takes ny_it201.zero (the parameter ny.zero, $0); the mutant takes line 77 in place of ny_it201.zero. has_overpayment is a known false only where line 77 is a known value not more than $0; line 77 is NonNegDollars, so it is $0, the value ny.zero gives. Where line 77 is a refusal or unknown, so is the guard: a refusal ends the choose on both routes; an unknown leaves both alternatives as ways (spec 4.7.3), and neither ny.zero nor line 77 (then unknown, not a refusal) refuses, so line 79 is the guard's unknown on both routes.", ["ny_it201.line79", "ny_it201.line79_wanted", "ny_it201.has_overpayment", "ny_it201.apply_if_overpaid", "ny_it201.line77", "ny_it201.zero", "ny_it201.no", "ny_it201.ask.apply_any", "ny_it201.line79_amount", "ny_it201.gate.line79_over", "ny_it201.line78", "param:ny.zero", "param:ny.false"], "031bca71628bd876", "ny_it201.line77");
  out["operand.ny_it201.ny_it201.gate.line79_over.line79.gt.0"] = pinned("ny_it201.line79 is a choice on has_overpayment (line 77 more than $0): true takes line79_wanted, false takes ny_it201.zero (the parameter ny.zero, $0). line79_wanted is a choice on apply_if_overpaid, itself a choice on has_overpayment (true: the input ask.apply_any; false: ny_it201.no, the parameter ny.false): true takes the input line79_amount, false takes ny_it201.zero. So line79 equals line79_wanted on every input: with has_overpayment true line79 is line79_wanted; with it false apply_if_overpaid is false and line79_wanted is $0, as line79 is; with it a refusal both are that refusal (a refused guard ends a choose, spec 4.7.3); with it unknown, line79 is its unknown (its other way, ny.zero, never refuses) and so is apply_if_overpaid (ny_it201.no never refuses), and line79_wanted is apply_if_overpaid's unknown, that same unknown, as its other way ny.zero never refuses. gate.line79_over compares line 79 with line 77; the mutant compares line79_wanted with line 77, which is the same comparison of equal values.", ["ny_it201.line79", "ny_it201.line79_wanted", "ny_it201.has_overpayment", "ny_it201.apply_if_overpaid", "ny_it201.line77", "ny_it201.zero", "ny_it201.no", "ny_it201.ask.apply_any", "ny_it201.line79_amount", "ny_it201.gate.line79_over", "ny_it201.line78", "param:ny.zero", "param:ny.false"], "031bca71628bd876", "ny_it201.line79_wanted");
  out["operand.ny_it201.ny_it201.line78.line79"] = pinned("ny_it201.line79 is a choice on has_overpayment (line 77 more than $0): true takes line79_wanted, false takes ny_it201.zero (the parameter ny.zero, $0). line79_wanted is a choice on apply_if_overpaid, itself a choice on has_overpayment (true: the input ask.apply_any; false: ny_it201.no, the parameter ny.false): true takes the input line79_amount, false takes ny_it201.zero. So line79 equals line79_wanted on every input: with has_overpayment true line79 is line79_wanted; with it false apply_if_overpaid is false and line79_wanted is $0, as line79 is; with it a refusal both are that refusal (a refused guard ends a choose, spec 4.7.3); with it unknown, line79 is its unknown (its other way, ny.zero, never refuses) and so is apply_if_overpaid (ny_it201.no never refuses), and line79_wanted is apply_if_overpaid's unknown, that same unknown, as its other way ny.zero never refuses. line 78 is line 77 less line 79, floored at zero, behind gate.line79_over; the mutant subtracts line79_wanted, an equal value.", ["ny_it201.line79", "ny_it201.line79_wanted", "ny_it201.has_overpayment", "ny_it201.apply_if_overpaid", "ny_it201.line77", "ny_it201.zero", "ny_it201.no", "ny_it201.ask.apply_any", "ny_it201.line79_amount", "ny_it201.gate.line79_over", "ny_it201.line78", "param:ny.zero", "param:ny.false"], "031bca71628bd876", "ny_it201.line79_wanted");
  out["operand.ny_it201.ny_it201.est_penalty_balance.no.then1"] = pinned("est_penalty_balance is a choice on tax_due_positive (tax_due more than $0): true takes est_below_safe_harbor, false takes ny_it201.no (the parameter ny.false); the mutant reads gate.other_withholding in place of ny_it201.no. tax_due is line 62 less line 76, floored at zero, which evaluates both operands, a refusal in either outranking an unknown (spec 4.7.4); line 76 is a sum, which returns the first refusal among its operands and is a known value only when every operand is, among them line 72, whose only refusal gate is gate.other_withholding. gate.other_withholding is a choice on has_other_payments (an any-test of federal lines) between the input ask.other_withholding and ny_it201.no. Where the gate is true, a refusal or unknown, line 72 is that refusal or unknown at entry (spec 4.7.1), so line 76 and tax_due are not known values and tax_due_positive is not a known false; where the gate is a refusal or true, line 72, line 76, tax_due and tax_due_positive are refusals, and the guard's refusal ends the choose on both routes. So wherever tax_due_positive is known false gate.other_withholding is a memoized false in the same frame (spec 4.7.6), the value of ny_it201.no; and wherever tax_due_positive is unknown, gate.other_withholding is false or unknown, never a refusal, as ny_it201.no never is, so both alternatives being ways (spec 4.7.3) est_penalty_balance is that unknown on both routes.", ["ny_it201.est_penalty_balance", "ny_it201.tax_due_positive", "ny_it201.tax_due", "ny_it201.line76", "ny_it201.line72", "ny_it201.gate.other_withholding", "ny_it201.has_other_payments", "ny_it201.ask.other_withholding", "ny_it201.no", "param:ny.false"], "f1bb5dcc707de5a0", "ny_it201.gate.other_withholding");
  return out;
}

function zeroPinned(reason: string, lines: string[], digest: string, reads: string): Conditional & { reads: string } {
  const p = pinned(reason, lines, digest, reads);
  return { reason: p.reason, reads: p.reads, premises: lines, holds: (d) => p.holds(d) && d.params.values["ny.zero"]?.value === 0 };
}

const NY_MCTMT_DIGEST = "626157771c65f92b";
const NY_ZERO_DIGEST = "86ec057ccccbf26d";

export const EQUIVALENT_IF: Record<string, Conditional> = {
  // Spec 4.7.3, a choose with an unknown guard: the alternative's value is a way there as well as where its guard holds.
  "operand.s1a.s1a.line13_claim.line13_ssn.then0": pinned("s1a.line13_claim's single alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is single, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.line10_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.line13_amount is s1a.tips_capped, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_ssn", "s1a.line13_amount", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_over", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tip_ssn_count", "s1a.tips", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "7454f11e16c78323", "s1a.line13_amount"),
  "operand.s1a.s1a.line13_claim.line13_ssn.then1": pinned("s1a.line13_claim's mfj alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is mfj, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.line10_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.line13_amount is s1a.tips_capped, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_ssn", "s1a.line13_amount", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_over", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tip_ssn_count", "s1a.tips", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "7454f11e16c78323", "s1a.line13_amount"),
  "operand.s1a.s1a.line13_claim.zero.then2": pinned("s1a.line13_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.line13_amount. s1a.line13_claim is read only by s1a.tips_deduction, in its s1a.tips-true alternative. Where s1a.tips is unknown the claim line is a way of its reader (spec 4.7.3), whose other alternative, s1a.zero, never refuses, so that reader is s1a.tips's unknown on both routes whatever the claim line is. With s1a.tips true and the status known to be mfs, s1a.part2 (s1a.part2_ssn, whose mfs alternative is s1a.no, false) is false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold each take s1a.zero, s1a.line10_over is false and s1a.line13_amount is s1a.tips_capped, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.tip_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.tip_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.tip_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.tip_ssn is false or unknown and s1a.line13_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes.",
    ["s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_ssn", "s1a.line13_amount", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_over", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tip_ssn_count", "s1a.tips", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "7454f11e16c78323", "s1a.line13_amount"),
  "operand.s1a.s1a.line13_claim.line13_ssn.then3": pinned("s1a.line13_claim's hoh alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is hoh, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.line10_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.line13_amount is s1a.tips_capped, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_ssn", "s1a.line13_amount", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_over", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tip_ssn_count", "s1a.tips", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "7454f11e16c78323", "s1a.line13_amount"),
  "operand.s1a.s1a.line13_claim.line13_ssn.then4": pinned("s1a.line13_claim's qss alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is qss, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.line10_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.line13_amount is s1a.tips_capped, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_ssn", "s1a.line13_amount", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_over", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tip_ssn_count", "s1a.tips", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "7454f11e16c78323", "s1a.line13_amount"),
  "operand.s1a.s1a.line13_ssn.zero.then0": pinned("s1a.line13_ssn's s1a.tip_ssn-false alternative is s1a.zero; the mutant reads s1a.line13_figured, s1a.tips_capped less s1a.tips_reduction, floored at zero. s1a.line13_ssn is read only by s1a.line13_claim, and s1a.line13_claim only by s1a.tips_deduction, in its s1a.tips-true alternative; where s1a.tips is unknown s1a.tips_deduction is a choice whose other way, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever s1a.line13_ssn is (spec 4.7.3). Where s1a.tips is true, s1a.part2 is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs and s1a.no (false) for mfs. With s1a.tip_ssn known false and the status known, s1a.part2 is false, so s1a.tips_capped and s1a.tips_reduction take s1a.zero and s1a.line13_figured is $0. With s1a.tip_ssn known false and the status unknown, s1a.part2 is that unknown, never a refusal, and so are s1a.tips_capped, s1a.tips_reduction and s1a.line13_figured (each a choice on s1a.part2 with an s1a.zero alternative, or their difference); s1a.line13_claim is then a choice on the unknown status whose mfs alternative, s1a.zero, never refuses, so it is the status's unknown on both routes. Where s1a.tip_ssn is unknown, s1a.part2 is false or unknown (s1a.tips and the status are inputs, s1a.no a parameter), so s1a.tips_capped and s1a.tips_reduction are $0 or that unknown, never a refusal, and so is s1a.line13_figured; the base's s1a.zero is not a refusal either, so s1a.line13_ssn is s1a.tip_ssn's unknown on both routes.",
    ["s1a.line13_ssn", "s1a.line13_claim", "s1a.tips_deduction", "s1a.line13_figured", "s1a.tips_capped", "s1a.tips_reduction", "s1a.part2", "s1a.part2_ssn", "s1a.no", "param:household.no", "s1a.tip_ssn", "s1a.tips", "s1a.tip_ssn_count", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "e7c08f643dee35fa", "s1a.line13_figured"),
  "operand.s1a.s1a.line21_claim.line21_ssn.then0": pinned("s1a.line21_claim's single alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is single, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.line18_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.line21_amount is s1a.ot_capped, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_ssn", "s1a.line21_amount", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_over", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.ot_ssn_count", "s1a.overtime", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "0d5d530bb91d5da2", "s1a.line21_amount"),
  "operand.s1a.s1a.line21_claim.line21_ssn.then1": pinned("s1a.line21_claim's mfj alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is mfj, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.line18_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.line21_amount is s1a.ot_capped, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_ssn", "s1a.line21_amount", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_over", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.ot_ssn_count", "s1a.overtime", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "0d5d530bb91d5da2", "s1a.line21_amount"),
  "operand.s1a.s1a.line21_claim.zero.then2": pinned("s1a.line21_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.line21_amount. s1a.line21_claim is read only by s1a.ot_deduction, in its s1a.overtime-true alternative. Where s1a.overtime is unknown the claim line is a way of its reader (spec 4.7.3), whose other alternative, s1a.zero, never refuses, so that reader is s1a.overtime's unknown on both routes whatever the claim line is. With s1a.overtime true and the status known to be mfs, s1a.part3 (s1a.part3_ssn, whose mfs alternative is s1a.no, false) is false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold each take s1a.zero, s1a.line18_over is false and s1a.line21_amount is s1a.ot_capped, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.ot_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.ot_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.ot_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.ot_ssn is false or unknown and s1a.line21_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes.",
    ["s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_ssn", "s1a.line21_amount", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_over", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.ot_ssn_count", "s1a.overtime", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "0d5d530bb91d5da2", "s1a.line21_amount"),
  "operand.s1a.s1a.line21_claim.line21_ssn.then3": pinned("s1a.line21_claim's hoh alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is hoh, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.line18_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.line21_amount is s1a.ot_capped, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_ssn", "s1a.line21_amount", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_over", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.ot_ssn_count", "s1a.overtime", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "0d5d530bb91d5da2", "s1a.line21_amount"),
  "operand.s1a.s1a.line21_claim.line21_ssn.then4": pinned("s1a.line21_claim's qss alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is qss, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.line18_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.line21_amount is s1a.ot_capped, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3).",
    ["s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_ssn", "s1a.line21_amount", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_over", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.ot_ssn_count", "s1a.overtime", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "0d5d530bb91d5da2", "s1a.line21_amount"),
  "operand.s1a.s1a.line21_ssn.zero.then0": pinned("s1a.line21_ssn's s1a.ot_ssn-false alternative is s1a.zero; the mutant reads s1a.line21_figured, s1a.ot_capped less s1a.ot_reduction, floored at zero. s1a.line21_ssn is read only by s1a.line21_claim, and s1a.line21_claim only by s1a.ot_deduction, in its s1a.overtime-true alternative; where s1a.overtime is unknown s1a.ot_deduction is a choice whose other way, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever s1a.line21_ssn is (spec 4.7.3). Where s1a.overtime is true, s1a.part3 is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs and s1a.no (false) for mfs. With s1a.ot_ssn known false and the status known, s1a.part3 is false, so s1a.ot_capped and s1a.ot_reduction take s1a.zero and s1a.line21_figured is $0. With s1a.ot_ssn known false and the status unknown, s1a.part3 is that unknown, never a refusal, and so are s1a.ot_capped, s1a.ot_reduction and s1a.line21_figured (each a choice on s1a.part3 with an s1a.zero alternative, or their difference); s1a.line21_claim is then a choice on the unknown status whose mfs alternative, s1a.zero, never refuses, so it is the status's unknown on both routes. Where s1a.ot_ssn is unknown, s1a.part3 is false or unknown (s1a.overtime and the status are inputs, s1a.no a parameter), so s1a.ot_capped and s1a.ot_reduction are $0 or that unknown, never a refusal, and so is s1a.line21_figured; the base's s1a.zero is not a refusal either, so s1a.line21_ssn is s1a.ot_ssn's unknown on both routes.",
    ["s1a.line21_ssn", "s1a.line21_claim", "s1a.ot_deduction", "s1a.line21_figured", "s1a.ot_capped", "s1a.ot_reduction", "s1a.part3", "s1a.part3_ssn", "s1a.no", "param:household.no", "s1a.ot_ssn", "s1a.overtime", "s1a.ot_ssn_count", "household.taxpayer_work_ssn", "household.taxpayer_work_ssn_count", "s1a.zero"], "d9c8bf35b915e837", "s1a.line21_figured"),
  "operand.s1a.s1a.line36a_claim.zero.then2": pinned("s1a.line36a_claim's married-filing-separately alternative is s1a.zero; the mutant reads s1a.senior_phased, a choice on s1a.part5 (all[senior_any, status not mfs]) between s1a.zero and line35_calc. With the status known to be mfs, part5 is false and line35 is s1a.zero: the two values agree. Where the status is unknown both are ways (spec 4.7.3): part5 is false or unknown (senior_any compares s1a.senior_count with 0, and senior_count counts the person entries whose person.senior_work_ssn is true, a choice on person.age65 between the input work_ssn and person.no (a parameter); age65 is an any-test on the input birth_year and born_jan1_if_cut_year, a choice on birth_cut_year (tests of birth_year) between the input born_jan1 and person.no; none has a refusal gate), so line35 is $0 or that unknown, never a refusal, as the base's s1a.zero is; the claim line is then the status's unknown on both routes.",
    ["s1a.line36a_claim", "s1a.senior_phased", "s1a.part5", "s1a.senior_any", "s1a.senior_count", "person.senior_work_ssn", "person.work_ssn", "person.age65", "person.birth_year", "person.born_jan1_if_cut_year", "person.birth_cut_year", "person.born_jan1", "person.no", "s1a.zero"], "2dac128ca75bf2d0", "s1a.senior_phased"),
  "operand.s1a.s1a.vli_deduction.zero.then0": pinned("s1a.vli_deduction's carloan-false alternative is s1a.zero; the mutant reads s1a.line30_figured, line24 less line29, floored at zero, both choices on s1a.part4 (carloan true) between s1a.zero and their figures. With carloan known false, part4 is false and both are $0, so line30_figured is $0. Where carloan is unknown, part4 is that unknown, line24 and line29 are $0 or unknown, never a refusal (spec 4.7.3), and so is line30_figured; s1a.vli_deduction is then carloan's unknown on both routes.",
    ["s1a.vli_deduction", "s1a.line30_figured", "s1a.vli_capped", "s1a.vli_reduction", "s1a.part4", "s1a.carloan", "s1a.zero"], "0bd05f2d7d11efc2", "s1a.line30_figured"),
  "operand.eic.eic.line1.earned_income.then0": pinned("eic.line1 chooses on self_employed: false takes earned_income, true takes wsb_6 (wsb_4b floored at zero, no gates). The mutant reads earned_for_limit in the false alternative, a choice on the same guards that takes earned_income when self_employed is false and wsb_4b when true. With self_employed known false both are earned_income, the same memoized value. Where self_employed is unknown both lines evaluate both alternatives (spec 4.7.3): earned_for_limit is a refusal exactly when earned_income and wsb_4b both refuse, then earned_income's; wsb_6 refuses exactly when wsb_4b does. So the base line 1 is a refusal exactly when earned_income and wsb_4b refuse, then earned_income's, and so is the mutant (its first way is earned_for_limit, that same refusal); otherwise both are self_employed's unknown.",
    ["eic.line1", "eic.earned_for_limit", "eic.earned_income", "eic.wsb_6", "eic.wsb_4b", "eic.self_employed", "eic.zero"], "62141d5ded1cc113", "eic.earned_for_limit"),
  "operand.person.person.se_line6.zero.then1": pinned("person.se_line6's has_sc-false alternative is person.zero; the mutant reads person.s179_listed, a sum of sc.f29 over the person's Schedule C entries. With has_sc known false the roster is confirmed and empty, so s179_listed is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; se_line6's own gate, se_rrta, is then unknown, so se_line6 is that unknown at line entry and its expression, the only part the mutant changes, is not evaluated (spec 4.7.1).",
    ["person.se_line6", "person.s179_listed", "person.has_sc", "person.sc_count", "person.se_rrta", "person.sc_rrta_count", "person.zero", "sc.one", "param:sc.one"], "296f8429df2a2ffe", "person.s179_listed"),
  "operand.person.person.eic_se.zero.then1": pinned("person.eic_se's has_sc-false alternative is person.zero; the mutant reads person.eic_part1, sc_total less se_line13. With has_sc known false the roster is confirmed and empty, sc_total is $0 and se_line13 takes person.zero, so eic_part1 is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; sc_total, a sum over that roster, is unknown, and se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry; eic_part1 is then unknown, never a refusal, as the base's person.zero is not, and eic_se is has_sc's unknown on both routes (spec 4.7.3).",
    ["person.eic_se", "person.eic_part1", "person.sc_total", "person.se_line13", "person.has_sc", "person.sc_count", "person.se_rrta", "person.sc_rrta_count", "person.zero", "sc.one", "param:sc.one"], "495d24215b1cd831", "person.eic_part1"),
  "operand.person.person.ira_se.zero.then1": pinned("person.ira_se's has_sc-false alternative is person.zero; the mutant reads person.ira_se_take, the sum of se_line13 and s16. With has_sc known false both take person.zero, so the sum is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry, and s16 is a choice on has_sc with a person.zero alternative, so it is unknown (spec 4.7.3); ira_se_take is then unknown, never a refusal, and ira_se is has_sc's unknown on both routes.",
    ["person.ira_se", "person.ira_se_take", "person.se_line13", "person.s16", "person.has_sc", "person.sc_count", "person.se_rrta", "person.sc_rrta_count", "person.zero", "sc.one", "param:sc.one"], "15b01a7c6f5448ca", "person.ira_se_take"),
  "boundary.person.person.has_educator_expenses": pinnedRefusal("has_educator_expenses is educator_expenses_if_educator more than $0, read only by educator_deduction, a choice on it (true: educator_eligible_amount; false: person.zero). The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). The inclusive test differs only where educator_expenses_if_educator is a known $0, so where eligible_educator is known: the base takes person.zero ($0); the mutant takes educator_eligible_amount, a choice on the same eligible_educator whose true alternative is educator_limited, the smaller of educator_expenses_if_educator ($0) and educator_max ($300), $0, and whose false alternative is person.zero, $0. educator_deduction is $0 on both routes.",
    ["person.educator_deduction", "person.has_educator_expenses", "person.educator_eligible_amount", "person.educator_expenses_if_educator", "person.educator_limited", "person.educator_max", "person.eligible_educator", "person.educator_expenses", "person.zero", "param:s1.educator_max", "param:ss.zero", "param:sales.zero"], "fb6ddaa17b0d400e"),
  "operand.person.person.has_educator_expenses.educator_expenses_if_educator.gt.0": pinned("has_educator_expenses is educator_expenses_if_educator more than $0, read only by educator_deduction, a choice on it (true: educator_eligible_amount; false: person.zero); the mutant tests educator_max ($300) more than $0, always true, so its educator_deduction is always educator_eligible_amount. The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). Where the base test is true both routes take educator_eligible_amount. Where it is false educator_expenses_if_educator is a known $0 and eligible_educator is known: the base takes person.zero ($0), and educator_eligible_amount is educator_limited, the smaller of $0 and $300, or person.zero, $0 either way. Where it is unknown, educator_expenses_if_educator is unknown and the base's educator_deduction is that unknown (no way refuses); on the mutant's route educator_eligible_amount is unknown too: with eligible_educator unknown it is that guard's unknown, and with eligible_educator true it is educator_limited, the smaller of an unknown and $300, unknown (spec 4.7.4).",
    ["person.educator_deduction", "person.has_educator_expenses", "person.educator_eligible_amount", "person.educator_expenses_if_educator", "person.educator_limited", "person.educator_max", "person.eligible_educator", "person.educator_expenses", "person.zero", "param:s1.educator_max", "param:ss.zero", "param:sales.zero"], "fb6ddaa17b0d400e", "person.educator_max"),
  "operand.person.person.educator_eligible_amount.zero.then1": pinned("educator_eligible_amount's eligible_educator-false alternative is person.zero; the mutant reads educator_max ($300). educator_eligible_amount is read only by educator_deduction, in its has_educator_expenses-true alternative. The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). With eligible_educator a known false (memoized, spec 4.7.6) educator_expenses_if_educator is person.zero, $0, so has_educator_expenses (educator_expenses_if_educator more than $0) is false and educator_deduction takes person.zero without reading educator_eligible_amount. The mutated alternative is otherwise a way only with eligible_educator unknown; educator_expenses_if_educator is then unknown, so has_educator_expenses is unknown and educator_deduction is that unknown on both routes, no way refusing.",
    ["person.educator_deduction", "person.has_educator_expenses", "person.educator_eligible_amount", "person.educator_expenses_if_educator", "person.educator_limited", "person.educator_max", "person.eligible_educator", "person.educator_expenses", "person.zero", "param:s1.educator_max", "param:ss.zero", "param:sales.zero"], "fb6ddaa17b0d400e", "person.educator_max"),
  "operand.sc.sc.f7206_line9.zero.then1": pinned("sc.f7206_line9's f7206_has-false alternative is sc.zero; the mutant reads sc.f7206_line8, line 4 less line 7, floored at zero. f7206_has is line 4 (profit_pos, sc.result floored at zero) more than sc.zero. With it known false line 4 is $0 and line 7 takes sc.zero, so line 8 is $0. Where f7206_has is unknown, line 4 is unknown (a refused line 4 refuses the guard and both routes alike), and line 7, a choice on f7206_has with an sc.zero alternative, is unknown (spec 4.7.3); line 8 is then unknown, never a refusal, and line 9 is f7206_has's unknown on both routes.",
    ["sc.f7206_line9", "sc.f7206_line8", "sc.f7206_line4", "sc.f7206_line7", "sc.f7206_has", "sc.profit_pos", "sc.zero"], "c2a54dd6d46c2592", "sc.f7206_line8"),
  "operand.sd.sd.to1040.line21.then0": pinned("sd.to1040's has_loss-true alternative is sd.line21, a choice on the same has_loss taking limited_loss (the larger of line 16 and the loss-limit parameter) or sd.zero; the mutant reads limited_loss. With has_loss known true line 21 is limited_loss, the same memoized value. has_loss compares line 16 with 0, so where it is unknown line 16 is unknown (a refused line 16 refuses the guard and both routes alike): limited_loss is then unknown, line 21 is unknown (spec 4.7.3) and so is the other alternative, line 16; neither route is a refusal on every way, and to1040 is has_loss's unknown on both.",
    ["sd.to1040", "sd.line21", "sd.limited_loss", "sd.line16", "sd.has_loss", "sd.zero"], "c01d6cc58d96a57d", "sd.limited_loss"),
  "operand.ssb.ssb.line16.line16_together.then0": pinned("ssb.line16's mfs_together-true alternative is line16_together, line 7 times 85%; the mutant reads line 15, line 11 times 85%, line 11 being line 9 less line 10 and line 9 line 7 less line 8, each floored at zero. mfs_together is all[status mfs, lived_apart false]; then line 8 and line 10 take mfs_base and mfs_adjust with lived_apart false, ssb.zero, so line 11 is line 7 and the two values agree. Lines 8 and 10 choose on the status, and mfs_base and mfs_adjust on lived_apart, among parameters only, so they are never refusals; line 15 is therefore a refusal exactly when line 7 is, with line 7's refusal, as line16_together is. Where mfs_together is unknown both alternatives are ways (spec 4.7.3): the first way refuses on both routes alike, and the other, line16_sum, is the same line, so line 16 is the same on both.",
    ["ssb.line16", "ssb.line16_together", "ssb.line15", "ssb.line11", "ssb.line9", "ssb.line10", "ssb.line8", "ssb.mfs_base", "ssb.mfs_adjust", "ssb.line7", "ssb.mfs_together", "ssb.lived_apart", "ssb.zero"], "491faf09ac42603e", "ssb.line15"),
  "operand.ssb.ssb.line18.zero.then1": pinned("ssb.line18 is a choice on has_benefits, the test 'line 1 more than sales.zero ($0)': true takes line18_figured, false takes ssb.zero (the parameter sales.zero, $0); the mutant takes line 17, line 1 times 85% (ssb.rate85), in place of ssb.zero. has_benefits is a known false only where line 1 is a known value not more than $0; line 1 is NonNegDollars, so it is $0, and $0 times 85% is $0, the value ssb.zero gives. Line 1 copies benefits_if_any and has no refusal gate, nor has line 17; where line 1 is unknown or a refusal, so is the guard: a refusal ends the choose on both routes; an unknown leaves both alternatives as ways (spec 4.7.3), and neither ssb.zero nor line 17 (then unknown, not a refusal) refuses, so line 18 is the guard's unknown on both routes.",
    ["ssb.line18", "ssb.line18_figured", "ssb.has_benefits", "ssb.line1", "ssb.line17", "ssb.zero", "param:sales.zero", "param:ssb.rate85"], "5128822d423669a0", "ssb.line17"),
  "param.eic.ws_threshold0.other.$1": thresholdAtPlateau("eic.ws_threshold0.other", ["eic_0"], 0),
  "param.eic.ws_threshold0.joint.$1": thresholdAtPlateau("eic.ws_threshold0.joint", ["eic_0"], 1),
  "param.eic.ws_threshold1.joint.$1": thresholdAtPlateau("eic.ws_threshold1.joint", ["eic_1", "eic_2", "eic_3"], 1),
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
  "boundary.s1a.s1a.line10_over": s1aStepSkip("s1a.line10_over", "s1a.tips_magi", "s1a.tips_threshold", "s1a.line10_pos", "s1a.tips_reduction", "s1a.line13_figured", "s1a.tips_capped", "s1a.line13_amount"),
  "boundary.s1a.s1a.line18_over": s1aStepSkip("s1a.line18_over", "s1a.ot_magi", "s1a.ot_threshold", "s1a.line18_pos", "s1a.ot_reduction", "s1a.line21_figured", "s1a.ot_capped", "s1a.line21_amount"),
  "boundary.s1a.s1a.line27_over": s1aStepSkip("s1a.line27_over", "s1a.vli_magi", "s1a.vli_threshold", "s1a.line27_pos", "s1a.vli_reduction", "s1a.line30_figured", "s1a.vli_capped", "s1a.line30_amount"),
  "boundary.s1a.s1a.line33_over": s1aStepSkip("s1a.line33_over", "s1a.senior_magi", "s1a.senior_threshold", "s1a.line33_pos", "s1a.senior_reduction", "s1a.line35_figured", "s1a.senior_amount", "s1a.line35_calc"),
  "boundary.sli.sli.over": prorateSkip("The test 'line 4 more than line 5' made inclusive adds only the case line 4 = line 5"),
  "operand.sli.sli.line9.line8": prorateSkip("Reading the prorated line directly instead of line 8 differs only when line 4 is not more than line 5"),
  "operand.sdtw.sdtw.line45.line43": {
    reason: "Line 43 is its helper (28% of line 42) when sdtw.use28 holds and $0 otherwise, and line 42 is $0 under the same gate; so when the gate is false the helper is 28% of $0, and when it is unknown or refused line 42 and line 43 return the gate's value, which the rate passes through. Line 45 reads the same value either way.",
    holds: (d) => {
      const g43 = gateOf(d, "sdtw.line43"), g42 = gateOf(d, "sdtw.line42"), raw = exprOf(d, "sdtw.raw43");
      return !!g43 && !!g42 && g43.then === "sdtw.raw43" && g42.gate === g43.gate && raw?.op === "multiply_rate" && raw.amount === "sdtw.line42"
        && knownRate(d, raw.rate) && ungated(d, "sdtw.raw43", "sdtw.line43", "sdtw.line42");
    },
  },
  "operand.sdtw.sdtw.line17.line16": {
    reason: "Line 17 is min(line 14, line 16) and line 16 is min(line 1, line 15). Line 13 is line 10 less min(line 9, line 11), and line 10 is line 6 plus line 9 with both floored at zero, so line 13 is not negative and line 14 (line 1 less line 13, floored) is at most line 1, which is not negative. Then min(line 14, min(line 1, line 15)) = min(line 14, line 15); and line 14 reads line 1 first, so a refusal or unknown in line 1 reaches line 17 through line 14 on both routes.",
    holds: (d) => {
      const e = (id: string) => exprOf(d, id);
      const l17 = e("sdtw.line17"), l16 = e("sdtw.line16"), l14 = e("sdtw.line14"), l13 = e("sdtw.line13"), l12 = e("sdtw.line12"), l10 = e("sdtw.line10");
      return l17?.op === "smaller_of" && stableStringify(l17.of) === stableStringify(["sdtw.line14", "sdtw.line16"])
        && l16?.op === "smaller_of" && stableStringify(l16.of) === stableStringify(["sdtw.line1", "sdtw.line15"])
        && l14?.op === "subtract_floor0" && l14.from === "sdtw.line1" && l14.take === "sdtw.line13"
        && l13?.op === "subtract" && l13.from === "sdtw.line10" && l13.take === "sdtw.line12"
        && l12?.op === "smaller_of" && (l12.of as string[])[0] === "sdtw.line9"
        && l10?.op === "sum" && stableStringify(l10.of) === stableStringify(["sdtw.line6", "sdtw.line9"])
        && e("sdtw.line6")?.op === "subtract_floor0" && e("sdtw.line9")?.op === "subtract_floor0"
        && findLine(d, "sdtw.line1")?.type === "NonNegDollars";
    },
  },
  "operand.f8959.f8959.total_tax.rrta_tax": {
    reason: "Line 17 is 0.9% of line 16, and line 16 is line 14 less line 15 floored at zero, where line 14 is $0 behind its refusal gate and line 15 is not negative; so line 16 and line 17 are both $0, and when line 14 refuses or is unknown both carry its value (line 16 reads line 14 first, and the rate passes it through).",
    holds: (d) => {
      const l17 = exprOf(d, "f8959.rrta_tax"), l16 = exprOf(d, "f8959.rrta_excess"), l15 = findLine(d, "f8959.rrta_threshold");
      return l17?.op === "multiply_rate" && l17.amount === "f8959.rrta_excess" && l16?.op === "subtract_floor0" && l16.from === "f8959.rrta_comp" && l16.take === "f8959.rrta_threshold"
        && zeroBehindGates(d, "f8959.rrta_comp") && l15?.type === "NonNegDollars";
    },
  },
  "operand.person.person.dc_earned.eic_se": {
    reason: "person.eic_se is person.eic_se_has when the person has a Schedule C and $0 otherwise. With no Schedule C every sum over the person's Schedule C entries is $0, so the Schedule SE railroad gate is false, line 4c is $0, files_se is false and eic_se_has is the empty Schedule C total, $0; with the roster unanswered both routes are unknown. The replacement changes no value.",
    holds: (d) => {
      const se = gateOf(d, "person.eic_se"), has = exprOf(d, "person.has_sc"), seHas = exprOf(d, "person.eic_se_has"), files = exprOf(d, "person.files_se");
      const l4c = findLine(d, "person.se_line4c"), rrta = exprOf(d, "person.se_rrta");
      const overSc = (id: string) => { const e = exprOf(d, id); return e?.op === "sum_over" && e.collection === "sc"; };
      if (!se || se.gate !== "person.has_sc" || se.then !== "person.eic_se_has" || has?.op !== "test" || stableStringify(has.gt) !== stableStringify(["person.sc_count", { const: 0, type: "Count" }]) || !overSc("person.sc_count")) return false;
      const alts = (seHas?.op === "choose" ? seHas.alternatives : []) as { guard: unknown; then: unknown }[];
      const onFalse = alts.find((a) => stableStringify(a.guard).includes('"person.files_se"') && stableStringify(a.guard).includes("false"));
      if (alts.length !== 2 || onFalse?.then !== "person.sc_total" || !overSc("person.sc_total")) return false;
      if (files?.op !== "test" || (files.gt as unknown[])?.[0] !== "person.se_line4c") return false;
      const l4cAlts = (exprOf(d, "person.se_line4c")?.alternatives ?? []) as { guard: unknown; then: unknown }[];
      const noSc = l4cAlts.find((a) => stableStringify(a.guard) === stableStringify({ op: "test", eq: ["person.has_sc", { const: false }] }));
      return !!noSc && typeof noSc.then === "string" && zeroBehindGates(d, noSc.then)
        && stableStringify((l4c?.refuses ?? []).map((r) => r.when)) === stableStringify(["person.se_rrta"])
        && rrta?.op === "test" && (rrta.gt as unknown[])?.[0] === "person.sc_rrta_count" && overSc("person.sc_rrta_count");
    },
  },
  "boundary.sc.sc.ho_over": boundaryAgrees("sc.ho_over", "sc.ho_line4", "sc.ho_line4_actual", "sc.ho_line4_cap",
    "The home office test 'square feet more than the cap' made inclusive adds only square feet equal to the cap, where the rate times the square feet and the rate times the cap are the same amount. The test is read only by line 4.",
    (line) => {
      const o = line("sc.ho_over")?.expr as { gt?: unknown[] }, a = line("sc.ho_line4_actual"), c = line("sc.ho_line4_cap");
      return stableStringify(o.gt) === stableStringify(["sc.ho_sqft", "sc.ho_cap_sqft"]) && !!a && !!c && !(a.refuses ?? []).length && !(c.refuses ?? []).length
        && a.expr.op === "multiply_count" && c.expr.op === "multiply_count" && a.expr.amount === c.expr.amount
        && a.expr.count === "sc.ho_sqft" && c.expr.count === "sc.ho_cap_sqft";
    }),
  "boundary.se.positive": boundaryAgrees("positive", "line4a", "line3", "line4a_pos",
    "The test 'line 3 more than zero' made inclusive adds only line 3 = $0, where line 4a's two branches agree: line 3 itself, and 92.35% of line 3 floored at zero, both $0. The test is read only by line 4a.",
    (line) => {
      const o = line("positive")?.expr as { gt?: unknown[] }, pos = line("line4a_pos"), floor = line("line3pos"), zero = line("zero"), rate = line("rate9235");
      if (stableStringify(o.gt) !== stableStringify(["line3", { param: "sales.zero" }]) || !pos || !floor || !zero || !rate) return false;
      return pos.expr.op === "multiply_rate" && pos.expr.amount === "line3pos" && pos.expr.rate === "rate9235" && rate.expr.op === "param"
        && floor.expr.op === "subtract_floor0" && floor.expr.from === "line3" && floor.expr.take === "zero"
        && zero.expr.op === "param" && zero.expr.ref === "sales.zero" && [pos, floor, zero, rate].every((l) => !(l.refuses ?? []).length);
    }, "se"),
  "operand.eic.eic.line1_table0.line1.key": line1KeyInTable("eic.line1_table0"),
  "operand.eic.eic.line1_table1.line1.key": line1KeyInTable("eic.line1_table1"),
  "operand.eic.eic.line1_table2.line1.key": line1KeyInTable("eic.line1_table2"),
  "operand.eic.eic.line1_table3.line1.key": line1KeyInTable("eic.line1_table3"),
  "operand.f8889.f8889.subject.line16.then0": pinned("f8889.subject is read only by line17b_figured, which only line17b reads, and only in its has_taxable alternative; has_taxable is line16 more than $0 (sales.zero), so where subject is read line16 is complete and positive, which only line16's has_dist alternative gives (the other is f8889.zero, $0), and that alternative's value is line16_figured. Where has_taxable is false or refused, subject is not read; where it is unknown, line17b evaluates line17b_figured as a way (spec 4.7.3), but line17b's other alternative is f8889.zero, which never refuses, so line17b is that unknown on both routes.",
    ["f8889.subject", "f8889.line17b_figured", "f8889.line17b", "f8889.has_taxable", "f8889.line16", "f8889.line16_figured", "f8889.has_dist", "f8889.zero", "param:sales.zero"], "98c569ae2d25ff42", "f8889.line16_figured"),
  "operand.f8889.f8889.self_dec_year.zero.then2": pinned("self_dec_year's none alternative (no December 1 coverage) is f8889.zero; the mutant reads self_family_months. self_dec_year is read only by self_in_family, which takes it where full_year is true. full_year is a choose on coverage (the coverage used: the coverage_year answer, turned to changed by the checks beneath it, clear_all_year, fsa and spouse_family, all inputs with no gates): year_same (a parameter) for self_only and family, use_last_month for changed; use_last_month takes no_last_month (the parameter hsa.no_last_month, false) where dec_coverage_if_changed is none; and dec_coverage_if_changed is year_self_only or year_family (the parameters hsa.year_self_only, self_only, and hsa.year_family, family) for those two coverage values and dec_coverage for changed. So full_year true never meets December coverage none, and the changed alternative is not taken there. full_year reads only inputs and parameters with no gates, so it is never a refusal; where it is unknown self_in_family's other way, self_family_months (self_amount times the input months_family, reading only inputs and parameters with no refusal gates), never refuses, so self_in_family is full_year's unknown on both routes (spec 4.7.3).",
    ["f8889.self_dec_year", "f8889.self_in_family", "f8889.full_year", "f8889.year_same", "f8889.use_last_month", "f8889.no_last_month", "f8889.last_month", "f8889.dec_coverage_if_changed", "f8889.coverage_year", "f8889.dec_coverage", "f8889.year_self_only", "f8889.year_family", "f8889.self_family_months", "f8889.self_amount", "f8889.self_55", "f8889.self_under55", "f8889.age55_line3", "f8889.age55", "f8889.married_family", "household.married", "f8889.family_any_time", "f8889.dec_family", "f8889.some_family_months", "f8889.months_family", "f8889.zero", "param:hsa.no_last_month", "param:hsa.year_self_only", "param:hsa.year_family", "f8889.coverage", "f8889.coverage_self", "f8889.coverage_self_spouse", "f8889.coverage_family", "f8889.eligible_all", "f8889.no_fsa", "f8889.clear_if_uniform", "f8889.fsa_if_clear", "f8889.spouse_family_if_asked", "f8889.ask_spouse_family", "f8889.sf_eligible", "f8889.sf_married", "f8889.clear_all_year", "f8889.fsa", "f8889.spouse_family", "f8889.cov_self_only", "f8889.cov_family", "f8889.cov_changed", "f8889.no", "f8889.yes", "param:hsa.no", "param:hsa.yes", "param:hsa.cov_self_only", "param:hsa.cov_family", "param:hsa.cov_changed", "household.marriage_possible", "household.married_dec31", "household.ever_married", "household.status_states_marriage", "household.no", "param:household.no", "person.age55_at_year_end_if_open_year", "person.age55_open_year", "person.age55_at_year_end", "person.no", "param:age.cut_55"], "c805897ba16ab8eb", "f8889.self_family_months"),
  "operand.f8889.f8889.family_dec_year.zero.then2": pinned("family_dec_year's none alternative (no December 1 coverage) is f8889.zero; the mutant reads line5. family_dec_year is read only by step1_total, which takes it where full_year is true. full_year is a choose on coverage (the coverage used: the coverage_year answer, turned to changed by the checks beneath it, clear_all_year, fsa and spouse_family, all inputs with no gates): year_same (a parameter) for self_only and family, use_last_month for changed; use_last_month takes no_last_month (the parameter hsa.no_last_month, false) where dec_coverage_if_changed is none; and dec_coverage_if_changed is year_self_only or year_family (the parameters hsa.year_self_only, self_only, and hsa.year_family, family) for those two coverage values and dec_coverage for changed. So full_year true never meets December coverage none, and the changed alternative is not taken there. full_year reads only inputs and parameters with no gates, so it is never a refusal; where it is unknown step1_total's other way, family_counted (the parameter line family_under55 times the input months_family), never refuses, so step1_total is full_year's unknown on both routes (spec 4.7.3).",
    ["f8889.family_dec_year", "f8889.step1_total", "f8889.full_year", "f8889.year_same", "f8889.use_last_month", "f8889.no_last_month", "f8889.last_month", "f8889.dec_coverage_if_changed", "f8889.coverage_year", "f8889.dec_coverage", "f8889.year_self_only", "f8889.year_family", "f8889.family_counted", "f8889.family_under55", "f8889.months_family", "f8889.zero", "param:hsa.no_last_month", "param:hsa.year_self_only", "param:hsa.year_family", "f8889.coverage", "f8889.coverage_self", "f8889.coverage_self_spouse", "f8889.coverage_family", "f8889.eligible_all", "f8889.no_fsa", "f8889.clear_if_uniform", "f8889.fsa_if_clear", "f8889.spouse_family_if_asked", "f8889.ask_spouse_family", "f8889.sf_eligible", "f8889.sf_married", "f8889.clear_all_year", "f8889.fsa", "f8889.spouse_family", "f8889.cov_self_only", "f8889.cov_family", "f8889.cov_changed", "f8889.no", "f8889.yes", "param:hsa.no", "param:hsa.yes", "param:hsa.cov_self_only", "param:hsa.cov_family", "param:hsa.cov_changed"], "48038fec5734c96c", "f8889.line5"),
  "operand.f8889.f8889.bad_months.counts_hold.then0": pinned("bad_months's self_only alternative is counts_hold (the parameter hsa.year_counts_hold, false); the mutant reads mfs. bad_months is read only by line13_figured, as a refusal gate after mfs, the first of its gates: a later gate is evaluated only when mfs is a known false (spec 4.7.1), and mfs is then a memoized false in the same frame (spec 4.7.6), so the mutant's alternative is false, counts_hold's value. Where the coverage used (f8889.coverage) is unknown the alternatives are ways (spec 4.7.3) and the mutant's way is that same false. Only bad_months's own value changes, where mfs is true or unknown, and no line reads it there.",
    ["f8889.bad_months", "f8889.line13_figured", "f8889.mfs", "f8889.counts_hold", "param:hsa.year_counts_hold", "f8889.coverage"], "47fedc86c39f1a7a", "f8889.mfs"),
  "operand.f8889.f8889.bad_months.counts_hold.then1": pinned("bad_months's family alternative is counts_hold (the parameter hsa.year_counts_hold, false); the mutant reads mfs. bad_months is read only by line13_figured, as a refusal gate after mfs, the first of its gates: a later gate is evaluated only when mfs is a known false (spec 4.7.1), and mfs is then a memoized false in the same frame (spec 4.7.6), so the mutant's alternative is false, counts_hold's value. Where the coverage used (f8889.coverage) is unknown the alternatives are ways (spec 4.7.3) and the mutant's way is that same false. Only bad_months's own value changes, where mfs is true or unknown, and no line reads it there.",
    ["f8889.bad_months", "f8889.line13_figured", "f8889.mfs", "f8889.counts_hold", "param:hsa.year_counts_hold", "f8889.coverage"], "47fedc86c39f1a7a", "f8889.mfs"),
  "operand.f8889.f8889.testing_failed_figured.no.then1": pinned("testing_failed_figured's alternative for testing_if_asked false is f8889.no (the parameter hsa.no, false); the mutant reads testing_prior_if_asked. testing_if_asked is any[ira_failed true, testing_prior_if_asked true], a known false only where both disjuncts are known false, so where the false alternative is taken testing_prior_if_asked is false, f8889.no's value. Nothing testing_if_asked reads has a refusal gate (ira_failed, testing_prior_if_asked, ask_last_month_prior, ask_testing, not_covered_12 and the coverage lines beneath them read only inputs and parameters with no refusal gates), so it is never a refusal; where it is unknown both alternatives are ways (spec 4.7.3), neither route's ways (not_covered_12 with f8889.no, or with testing_prior_if_asked) refuse, and testing_failed_figured is that unknown on both routes.",
    ["f8889.testing_failed_figured", "f8889.testing_if_asked", "f8889.not_covered_12", "f8889.ira_failed", "f8889.testing_prior_if_asked", "f8889.covered_12", "f8889.no", "f8889.yes", "f8889.ira_gap_if_prior", "f8889.ask_last_month_prior", "f8889.testing_prior", "f8889.coverage", "f8889.all_year", "f8889.ira_prior_if_asked", "f8889.ira_gap", "f8889.ask_testing", "f8889.coverage_year", "f8889.coverage_self", "f8889.coverage_family", "f8889.cov_changed", "f8889.months_eligible", "f8889.ira_prior", "f8889.any", "f8889.eligible_all", "f8889.coverage_self_spouse", "f8889.cov_family", "f8889.line2", "sales.zero", "f8889.line9", "f8889.clear_if_uniform", "f8889.no_fsa", "f8889.spouse_family_if_asked", "f8889.cov_self_only", "f8889.clear_all_year", "f8889.fsa_if_clear", "f8889.ask_spouse_family", "f8889.spouse_family", "f8889.fsa", "f8889.sf_eligible", "f8889.sf_married", "household.married", "household.marriage_possible", "household.married_dec31", "household.no", "f1040.status", "household.ever_married", "household.status_states_marriage", "param:hsa.no", "param:hsa.yes", "param:hsa.cov_changed", "param:hsa.cov_family", "param:sales.zero", "param:hsa.cov_self_only", "param:household.no"], "ae2d9041ec5b79e4", "f8889.testing_prior_if_asked"),
  "operand.f8880.f8880.line3b_counted.zero.then1": pinned("line3b_counted's elig_b-false alternative is f8880.zero ($0); the mutant reads line3a_counted. line3b_counted is read only by contrib_counted, sum[line3a_counted, line3b_counted], which only has_contrib reads, as contrib_counted more than $0 (sales.zero). Where the alternative is taken contrib_counted is line3a_counted plus $0 on the base route and line3a_counted twice on the mutant's: a sum returns its first operand's refusal at once (spec 4.7.4), an unknown first operand leaves both unknown, and a complete, non-negative x and 2x are both more than $0 or both $0. With elig_b unknown the mutant's line3b_counted can be a refusal where the base's is unknown only if line3a_counted refuses, and contrib_counted is then line3a_counted's refusal on both routes.",
    ["f8880.line3b_counted", "f8880.line3a_counted", "f8880.contrib_counted", "f8880.has_contrib", "f8880.zero", "param:sales.zero"], "3f732e9b6c8a30f3", "f8880.line3a_counted"),
  "operand.f8880.f8880.line3a_counted.zero.then1": pinned("line3a_counted's elig_a-false alternative is f8880.zero ($0); the mutant reads line11, a copy of clw3. line3a_counted is read only by contrib_counted, which only has_contrib reads, which only can_take_contrib reads (has_contrib true takes past7, false takes no, the false parameter savers.no_credit), which only can_take_tax reads where clw_room (clw3 more than $0) is true, or as a way where it is unknown (spec 4.7.3). With clw_room unknown can_take_tax's other way, no, never refuses, so can_take_tax is clw_room's unknown on both routes. With clw_room true clw3 is complete and positive, so with elig_a false the mutant's contrib_counted is that amount plus line3b_counted: both routes are line3b_counted's refusal or unknown alike, and otherwise has_contrib is true on the mutant's route. Where the base's has_contrib is true too both take past7; where it is false line3b_counted is $0, the base takes no (false) and the mutant past7, line7 more than $0. line7 is line6a plus line6b; line6a is $0 (elig_a false); line6b is $0 when elig_b is false, and otherwise line3b is $0 and line6b is the smaller of the cap and line5b, line3b less line4b floored at zero, which is $0 when line4b is complete. So past7 is false wherever line4b is answered. With elig_a unknown the mutant's ways line3a and line11 cannot both refuse under clw_room true (line11 is complete). Where line4b's distribution answers are withheld, line5b and so past7 are unknown and the mutant can be unknown where the base is false, so the argument is over answered inputs.",
    ["f8880.line3a_counted", "f8880.line3a", "f8880.line11", "f8880.clw3", "f8880.clw_room", "f8880.contrib_counted", "f8880.line3b_counted", "f8880.has_contrib", "f8880.can_take_contrib", "f8880.can_take_tax", "f8880.past7", "f8880.no", "f8880.line7", "f8880.line6a", "f8880.line6b", "f8880.line6b_figured", "f8880.line5b", "f8880.line3b", "f8880.line4b", "f8880.elig_a", "f8880.elig_b", "f8880.cap", "f8880.zero", "param:savers.no_credit", "param:sales.zero"], "730f77f99094e38b", "f8880.line11"),
  "operand.person.person.edu_adj.zero.then1": pinned("edu_adj's edu_student-false alternative: edu_student is then known false (memoized). edu_adj's other reader, edu_has_adj (edu_adj more than $0), is read only by edu_over_if_adj, which only edu_over_refused reads, in its edu_student-true alternative; edu_over_refused is a choice on edu_student whose false alternative is edu_no, the year parameter edu.no (false), so it is false without reading edu_adj. Lines 27 to 30 read edu_adj only in the alternative guarded by edu_aoc true; edu_aoc is a choice on edu_student whose false alternative is edu_no, so edu_aoc is false. Line 31 reads it only in the alternative guarded by edu_llc true, an all-test whose first conjunct is edu_student true, so edu_llc is false. Those alternatives (and their bindings) are not evaluated (spec 4.7.3, 4.7.4). Where edu_student is unknown, edu_adj's other alternative, edu_adj_sum (a sum of three inputs with no refusal gates, edu_a_this_year, edu_a_next_year and edu_refunds), never refuses, so edu_adj is that unknown on both routes (spec 4.7.3). edu_adj, edu_has_adj and edu_over_if_adj are helpers.",
    ["person.edu_adj", "person.edu_adj_sum", "person.edu_student", "person.edu_has_adj", "person.edu_over_if_adj", "person.edu_over_refused", "person.edu_aoc", "person.edu_no", "person.edu_llc", "person.edu_line27", "person.edu_line28", "person.edu_line29", "person.edu_line30", "person.edu_line31", "person.zero", "param:edu.no", "person.edu_a_this_year", "person.edu_a_next_year", "person.edu_refunds"], "53b8176188d247fb", "person.ira_se"),
  "operand.dependent.dependent.edu_adj.zero.then1": pinned("dependent.edu_adj's edu_student-false alternative: as for person.edu_adj, edu_has_adj is read only by edu_over_if_adj, which only edu_over_refused reads, in its edu_student-true alternative, and edu_over_refused is a choice on edu_student whose false alternative is edu_no (the year parameter edu.no, false); lines 27 to 30 read edu_adj only where edu_aoc is true, and edu_aoc is a choice on edu_student whose false alternative is edu_no; line 31 reads it only where edu_llc is true, an all-test whose first conjunct is edu_student true. Where edu_student is unknown edu_adj is that unknown on both routes, its other alternative, edu_adj_sum (a sum of three inputs with no refusal gates), never refusing (spec 4.7.3). edu_adj, edu_has_adj and edu_over_if_adj are helpers.",
    ["dependent.edu_adj", "dependent.edu_adj_sum", "dependent.edu_student", "dependent.edu_has_adj", "dependent.edu_over_if_adj", "dependent.edu_over_refused", "dependent.edu_aoc", "dependent.edu_no", "dependent.edu_llc", "dependent.edu_line27", "dependent.edu_line28", "dependent.edu_line29", "dependent.edu_line30", "dependent.edu_line31", "dependent.zero", "param:edu.no"], "9be2c554dddb4481", "dependent.dc_line2d"),
  "operand.sa.sa.deduction.standard.then1": pinned("sa.deduction's itemizes-false alternative: the mutant changes only deduction's own expression, so its refusal gates, mfs_joint_paid_if_itemizing and charity_over_if_itemizing, evaluated before its alternatives, are the same on both routes. An any-test is known false only when every disjunct was evaluated and false with no unknown remembered (spec 4.7.2), so mfs_spouse_itemizes is known false and the comparison of total_itemized (line 17) with sa.standard read standard as a known value; a known standard passed its gates and took its mfs_spouse_itemizes-false alternative, whose value is standard_amount, the same memoized value. Where itemizes is unknown both alternatives are ways (spec 4.7.3): every disjunct was then evaluated with no true one and no refusal, so total_itemized, the itemized alternative and the comparison's operand, is not a refusal, and deduction is that unknown on both routes.",
    ["sa.standard", "sa.deduction", "sa.itemizes", "sa.standard_amount", "sa.mfs_spouse_itemizes", "sa.elect_itemize", "sa.total_itemized"], "22a0ee80a3275ec7", "sa.standard_amount"),
  "operand.sa.sa.medical_premiums_if_not_large.no.then1": pinned("sa.medical_premiums_if_not_large is a choice on sa.medical_any: false takes the premiums answer sa.medical_premiums, true takes sa.no (the parameter household.no, false); the mutant reads sa.age65 in place of sa.no. Its only reader is sa.medical_asked, any[medical_any is true, medical_premiums_if_not_large is true, e05_claimed is true], evaluated in order: where sa.medical_any is true the first disjunct decides the any-test and the line is not read (an any-test returns at its first true disjunct). Where sa.medical_any is a refusal the guard refuses and both routes are that refusal. Where it is unknown both alternatives are ways (spec 4.7.3); the first way, the input sa.medical_premiums, is never a refusal, so the line is sa.medical_any's unknown on both routes.",
    ["sa.medical_premiums_if_not_large", "sa.medical_asked", "sa.medical_any", "sa.medical_premiums", "sa.no", "param:household.no"], "3fe6083dc7c6118d", "sa.age65"),
  "operand.sa.sa.home_other_if_not_owner.no.then1": pinned("sa.home_other_if_not_owner is a choice on sa.home_owner: false takes the answer sa.home_other, true takes sa.no (the parameter household.no, false); the mutant reads sa.e05_claimed in place of sa.no. Its only reader is sa.home_asked, any[home_owner is true, home_other_if_not_owner is true], evaluated in order: where sa.home_owner is true the first disjunct decides the any-test and the line is not read. Where sa.home_owner is a refusal the guard refuses and both routes are that refusal. Where it is unknown both alternatives are ways (spec 4.7.3); the first way, the input sa.home_other, is never a refusal, so the line is sa.home_owner's unknown on both routes.",
    ["sa.home_other_if_not_owner", "sa.home_asked", "sa.home_owner", "sa.home_other", "sa.no", "param:household.no"], "82945fb1a9bdef38", "sa.e05_claimed"),
  "operand.eic.eic.credit.line6.then0": (() => {
    const lines = ["eic.credit", "eic.eligible", "eic.line6", "eic.after_line4", "eic.line4", "eic.line3", "eic.line1", "eic.line2", "eic.zero", "eic.line1_in_table", "eic.line1_table", "eic.line1_table0", "eic.line1_table1", "eic.line1_table2", "eic.line1_table3", "eic.line5", "eic.line3_table0", "eic.line3_table1", "eic.line3_table2", "eic.line3_table3", "eic.line5_blank", "eic.line5_threshold", "eic.threshold_other", "eic.threshold_joint", "eic.threshold0_other", "eic.threshold1_other", "eic.threshold0_joint", "eic.threshold1_joint", "eic.smaller", "eic.step1_income", "eic.step5_income", "eic.earned_for_limit", "eic.wsb_6", "eic.wsb_4b", "eic.earned_income", "param:eic.table_start"];
    const p = pinned("eic.credit's eligible alternative reads line6, which is line2 when line4 (line3 equals line1) is true and after_line4 otherwise, so the mutant differs only where line4 is true. eligible true needs step1_income (AGI, which line3 copies, below the limit) and step5_income (earned_for_limit, whose branch value is line1's source, below the limit) complete and true, so line3 and line1 are complete there and line4 is a complete comparison. With line4 true, line5 looks up line3 in the same EIC table (by the same ssn_count choices and filing status) that line2 looks up line1 in, so where line1 is at least table_start line5 equals line2 and after_line4 (line2, or the smaller of line5 and line2) is line2; where line1 is below table_start line2 is $0 and line3, equal to line1, is below every line 5 threshold (all of which exceed table_start), so line5 is blank and after_line4 is line2. eic.credit's refusal gate, household.eic_disallowed_claim (which reads eligible and line6 itself, through household.eic_claimed and household.eic_above_zero), is evaluated at line entry before the expression, the same on both routes (spec 4.7.1); only the expression's operand changes.", lines, "dc66c727cd33400f", "eic.after_line4");
    return { reason: p.reason, reads: p.reads, premises: p.premises, holds: (d: CanonicalData): boolean => {
      const start = d.params.values["eic.table_start"]?.value;
      const th = ["eic.ws_threshold0.joint", "eic.ws_threshold1.joint", "eic.ws_threshold0.other", "eic.ws_threshold1.other"].map((k) => d.params.values[k]?.value);
      return p.holds(d) && typeof start === "number" && start > 0 && th.every((v) => typeof v === "number" && v > start);
    } };
  })(),
  "operand.qdcg.qdcg.line8.line7": minNesting("qdcg.line8", "qdcg.line5", "qdcg.line7", "qdcg.line1", "qdcg.line6"),
  "operand.scveh.scveh.l5.k5": vehicle2019("scveh.l5", "scveh.l5 looks up the vehicle's year-5 limit; the mutant looks up year 4.",
    (d) => vehicleLimit(d, "scveh.l5", "scveh.k5") && vehicleLimit(d, "scveh.l4", "scveh.k4")),
  "operand.scveh.scveh.l6.k6": vehicle2019("scveh.l6", "scveh.l6 looks up the vehicle's year-6 limit; the mutant looks up year 5.",
    (d) => vehicleLimit(d, "scveh.l6", "scveh.k6") && vehicleLimit(d, "scveh.l5", "scveh.k5")),
  "operand.scveh.scveh.d5.l5": vehicle2019("scveh.d5", "scveh.d5 is min(l5, t5); the mutant reads d4 = min(l4, t4) in place of l5, and min(min(l4, t4), t5) = min(l5, t5) when l4 = l5 and t4 >= t5.",
    (d) => vehicleYear(d, 4) && vehicleYear(d, 5)),
  "operand.scveh.scveh.d6.l6": vehicle2019("scveh.d6", "scveh.d6 is min(l6, t6); the mutant reads d5 = min(l5, t5) in place of l6, and min(min(l5, t5), t6) = min(l6, t6) when l5 = l6 and t5 >= t6.",
    (d) => vehicleYear(d, 5) && vehicleYear(d, 6)),
  "operand.scveh.scveh.claims_bonus_this_year.no.then1": pinned("scveh.claims_bonus_this_year is a choice on scveh.placed_this_year: true takes scveh.claims_bonus, false takes scveh.no (the parameter household.no, false); the mutant takes scveh.low_use (over_half false) in place of scveh.no. placed_this_year is the test 'scveh.year eq 1', and scveh.year is a keyed lookup of the recovery_year table on the input scveh.placed, whose one refusal gate is scveh.low_use. A gate that is not a known false stops the line at entry with the gate's refusal or unknown (spec 4.7.1), so placed, year and placed_this_year are known only where low_use is a known false: where placed_this_year is false, low_use is false, the value scveh.no gives. Where placed_this_year is true both routes take claims_bonus; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3); scveh.no and low_use (a test of bm_c against nonbusiness_c, products and a sum of inputs and the parameter sc.one_cent, with no refusal gate) never refuse, so the choice is placed_this_year's unknown on both routes.",
    ["scveh.claims_bonus_this_year", "scveh.placed_this_year", "scveh.year", "scveh.placed", "scveh.low_use", "scveh.over_half", "scveh.bm_c", "scveh.nonbusiness_c", "scveh.cm_c", "scveh.om_c", "scveh.cent", "scveh.miles_business", "scveh.miles_commuting", "scveh.miles_other", "scveh.no", "param:household.no", "param:sc.one_cent", "table:recovery_year"], "098e8f0256686776", "scveh.low_use"),
  "operand.f8962.f8962.filing.applicable.all.1.any.0.eq.0": pinned("filing is all[any, any[applicable, aptc]]; the mutant reads show_applicable, all[any, applicable], in place of applicable. The inner any-test is reached only when f8962.any is true or unknown. With any true, show_applicable is applicable's (memoized) value. f8962.any is forms > 0, and forms counts the Form 1095-A roster with a parameter field, so any is unknown only when that roster is unconfirmed; then aptc (aptc_total, a sum over the same roster) is unknown, never a refusal (spec 4.7.5: an unconfirmed roster evaluates nothing), and show_applicable differs from applicable only by a true turned unknown, which the outer all-test, already holding any's unknown, cannot see: both are unknown, or the same refusal of applicable.",
    ["f8962.filing", "f8962.show_applicable", "f8962.applicable", "f8962.any", "f8962.forms", "f8962.aptc", "f8962.aptc_total", "f1095a.one", "param:sales.one"], "459e978b9bfad34e", "f8962.show_applicable"),
  "operand.f2441.f2441.line13_earned.line20.all.3.gt.1": pinned("The fourth conjunct of line13_earned compares line 23 with line 20; the mutant compares it with line 24. Line 22 is f2441.zero (a $0 parameter), so line 24 is the smaller of (the smaller of line 20 and line 21) and $0, and line 23 is line 15 less $0. The fourth conjunct is reached only after line 20 < line 17 and line 20 < line 21 were each true or unknown. Line 20 is line 17, 18 and 19's smallest floored at zero, so line 20 complete means line 17 complete and the second conjunct complete: then line 20 < line 17 <= line 15 = line 23, so both comparisons are true when line 23 is complete, and both are line 23's own unknown or refusal otherwise (it is the left operand, and the right operand is complete in both when line 21 is). Line 21 unknown leaves the third conjunct unknown and line 24 unknown: the base comparison is true or line 23's incompleteness, the mutant's unknown or that refusal, so the test is the same. Line 20 unknown makes line 24 unknown, and both comparisons are line 23's refusal or unknown. A refusal of line 20 or line 21 ends the test at the second or third conjunct.",
    ["f2441.line13_earned", "f2441.line24", "f2441.line24_20_21", "f2441.line22", "f2441.zero", "f2441.line20", "f2441.line20_all", "f2441.line20_17_18", "f2441.line17", "f2441.line15", "f2441.line23", "f2441.line21", "param:sales.zero"], "3e3ee5d09b5f0888", "f2441.line24"),
  "operand.sdtw.sdtw.line4.zero.then1": pinned("sdtw.line4's filing4952-false alternative is sdtw.zero ($0); the mutant reads sdtw.line3, a copy of f4952.election through sd.investment_election. filing4952 is f4952.required, a choice on used: true takes required_test, false takes f4952.no (the parameter f4952.no, false); it is known false only when used is false (so has_election, a disjunct of used, is false and election is f4952.zero) or used is true and required_test is false (an any-test whose first disjunct is election > 0, so election was evaluated complete and not above $0). Either way line3 is $0 wherever the alternative is taken; a refused guard ends the choose before either alternative. Where filing4952 is unknown both alternatives are ways (spec 4.7.3), and line3 can make the mutant a refusal on both where the base's $0 leaves it unknown, so the argument is over answered inputs.",
    ["sdtw.line4", "sdtw.line3", "sdtw.zero", "sd.filing4952", "sd.investment_election", "f4952.required", "f4952.used", "f4952.required_test", "f4952.election", "f4952.has_election", "f4952.zero", "f4952.no", "param:f4952.no", "param:sales.zero"], "0e43686cdaa1ac7f", "sdtw.line3"),
  "operand.ssb.ssb.show16_18.mfs_together.all.1.any.0.eq.0": pinned("show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15 (all[show8_9, past9], show8_9 being all[lines8_to_15, past7] and lines8_to_15 being mfs_together false) in place of mfs_together. With mfs_together true, line 8 is mfs_base with lived_apart false, that is ssb.zero, so line 9 (line 7 less line 8, floored) is line 7 and past9 is past7, true where the any-test is reached: both are true. With mfs_together false, show10_15 is past9 (past7 is already true), so the any-tests agree. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown and line 9 is unknown or line 7's refusal (subtract evaluates both), so past9 is unknown or that refusal, which past7 has already returned: both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), line 9 is unknown or line 8's refusal, so past9 is unknown or that refusal; show8_9 is false (mfs_together true) or unknown, and show10_15 is false or past9's value. With mfs_together true the base any-test is true and the mutant's is past9's unknown (line 8 is then $0); otherwise both any-tests are past9's value. The outer test, holding past7's unknown, is unknown on both routes, or the same refusal.",
    ["ssb.show16_18", "ssb.mfs_together", "ssb.show10_15", "ssb.show8_9", "ssb.lines8_to_15", "ssb.past7", "ssb.past9", "ssb.line9", "ssb.line8", "ssb.mfs_base", "ssb.line7", "ssb.zero", "ssb.lived_apart"], "e4e2015880ddec17", "ssb.show10_15"),
  "operand.ssb.ssb.show16_18.past9.all.1.any.1.eq.0": pinned("show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15, all[all[mfs_together false, past7], past9], in place of past9. The second disjunct is reached only when mfs_together was not true. With mfs_together false and past7 true (the outer test's first conjunct), show10_15 is past9. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown, so past9 is unknown or line 7's refusal (already returned by past7): show10_15 is then unknown too, and both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), past9 is unknown or line 8's refusal, and show10_15, all[show8_9 (unknown, since lines8_to_15 is true or unknown there and past7 is unknown), past9], is past9's value; the second disjuncts agree, and the outer test, holding past7's unknown, is unknown on both routes or the same refusal.",
    ["ssb.show16_18", "ssb.mfs_together", "ssb.show10_15", "ssb.show8_9", "ssb.lines8_to_15", "ssb.past7", "ssb.past9", "ssb.line9", "ssb.line8", "ssb.mfs_base", "ssb.line7", "ssb.zero", "ssb.lived_apart"], "e4e2015880ddec17", "ssb.show10_15"),
  "operand.f8889.f8889.age55_unmarried.age55.all.0.eq.0": pinned("age55_unmarried is all[age55, household.married false]; the mutant reads age55_line3, all[age55, married_family false], in place of age55. married_family is a choose on household.married (family_any_time where true, f8889.no where false), and family_any_time is a choose on full_year (dec_family or some_family_months) over inputs and parameters with no refusal gates (coverage_year and the checks beneath it, dec_coverage, last_month, months_family, and the parameters behind year_same, year_self_only, year_family and no_last_month); household.married and age55 are derived with no refusal gates on the way (household.married a choice on marriage_possible (a choice on the input f1040.status taking the input ever_married or status_states_marriage, a test of the status) taking the input married_dec31 or household.no, the parameter household.no (false); age55 a test of the input person.birth_year against the parameter age.cut_55 and of age55_at_year_end_if_open_year, a choice on age55_open_year (a test of birth_year) taking the input age55_at_year_end or person.no). So none of these lines is a refusal. With married false, married_family is false and age55_line3 is age55. With married true the second conjunct is false on both routes, and the mutant's first conjunct is age55's value or false, never a refusal. With married unknown, married_family is unknown, so age55_line3 is false where age55 is false and otherwise age55's value or unknown, and the second conjunct is unknown: both tests are false where age55 is false and unknown otherwise.",
    ["f8889.age55_unmarried", "f8889.age55_line3", "f8889.married_family", "f8889.age55", "household.married", "f8889.family_any_time", "f8889.dec_family", "f8889.some_family_months", "f8889.full_year", "f8889.year_same", "f8889.use_last_month", "f8889.dec_coverage_if_changed", "f8889.coverage_year", "f8889.dec_coverage", "f8889.last_month", "f8889.no_last_month", "f8889.year_self_only", "f8889.year_family", "f8889.months_family", "f8889.coverage", "f8889.coverage_self", "f8889.coverage_self_spouse", "f8889.coverage_family", "f8889.eligible_all", "f8889.no_fsa", "f8889.clear_if_uniform", "f8889.fsa_if_clear", "f8889.spouse_family_if_asked", "f8889.ask_spouse_family", "f8889.sf_eligible", "f8889.sf_married", "f8889.clear_all_year", "f8889.fsa", "f8889.spouse_family", "f8889.cov_self_only", "f8889.cov_family", "f8889.cov_changed", "f8889.no", "f8889.yes", "param:hsa.no", "param:hsa.yes", "param:hsa.cov_self_only", "param:hsa.cov_family", "param:hsa.cov_changed", "household.marriage_possible", "household.married_dec31", "household.ever_married", "household.status_states_marriage", "household.no", "param:household.no", "person.age55_at_year_end_if_open_year", "person.age55_open_year", "person.age55_at_year_end", "person.no", "param:age.cut_55"], "f3ae44f60d0669dd", "f8889.age55_line3"),
  "operand.eic.eic.line1_in_table.line1.ge.0": (() => {
    const p = pinned("line1_in_table compares eic.line1 with eic.table_start; the mutant compares eic.earned_for_limit. Both choose on the same guards (self_employed false, then true) and take earned_income on the first; on the second line 1 takes wsb_6, which is wsb_4b floored at zero (subtract_floor0 from wsb_4b of eic.zero, no gates of its own), and earned_for_limit takes wsb_4b. A refused guard is the value of both; with an unknown guard both evaluate both alternatives (spec 4.7.3) and are a refusal exactly when earned_income and wsb_4b both refuse (wsb_6 refuses exactly when wsb_4b does), then earned_income's, the first way's, and otherwise that guard's unknown; an incomplete wsb_4b is wsb_6's value too. For a complete wsb_4b x, max(x, 0) >= start exactly when x >= start, because table_start is positive (checked).",
      ["eic.line1_in_table", "eic.line1", "eic.earned_for_limit", "eic.self_employed", "eic.wsb_6", "eic.wsb_4b", "eic.earned_income", "eic.zero", "param:eic.table_start"], "e98bc36d7a60ea8a", "eic.earned_for_limit");
    return { reason: p.reason, reads: p.reads, premises: p.premises, holds: (d: CanonicalData): boolean => {
      const start = d.params.values["eic.table_start"]?.value;
      return p.holds(d) && typeof start === "number" && start > 0;
    } };
  })(),
  "operand.dependent.dependent.dc_line2c.dc_incapable.all.1.eq.0": pinned("dc_line2c is all[dc_qp, dc_incapable, age test]; the mutant reads dc_disabled_qp, all[dc_incapable, dc_lived_half], in place of dc_incapable. The second conjunct is reached only when dc_qp is true or unknown (a refusal ends both tests). dc_qp true means its any-test found dc_child_all_year, dc_disabled_qp or dc_child true. dc_child_all_year and dc_child (through dc_age13) each need qc_dependent true, a choice on qualifying_child whose false alternative is dependent.no (the parameter household.no, false), so it needs qualifying_child true: qc_tests true, a chain of choices (qc_relationship, then qc_age, then self_support_if_own_money false, then joint_return_if_ever_married false) whose every other alternative is dependent.no and whose last is lived_half; lived_half is then a memoized true in the dependent's frame (spec 4.7.6), and dc_lived_half, an any-test whose first disjunct is lived_half true, is true. dc_disabled_qp true needs dc_lived_half true. So wherever dc_qp is true, dc_lived_half is true and dc_disabled_qp is dc_incapable's value (an input with no gates): the conjuncts agree. dc_qp is unknown only with an input it reads unanswered; there the mutant can be false or a refusal (through dc_lived_half) where the base is unknown, so the argument is over answered inputs: dc_qp is read by f2441.qp_count and f2441.paid_total for every dependent, and its inputs are asked on any return that reaches Form 2441.",
    ["dependent.dc_line2c", "dependent.dc_incapable", "dependent.dc_disabled_qp", "dependent.dc_qp", "dependent.dc_lived_half", "dependent.dc_child_all_year", "dependent.dc_child", "dependent.dc_age13", "dependent.qc_dependent", "dependent.qualifying_child", "dependent.qc_tests", "dependent.qc_from_age", "dependent.qc_from_support", "dependent.qc_from_joint", "dependent.no", "param:household.no", "dependent.lived_half"], "b5b7b1b9f8f8dfe0", "dependent.dc_disabled_qp"),
  "operand.eic.eic.step5_income.earned_for_limit.lt.0": pinned("step5_income compares earned_for_limit with eic.limit; the mutant compares wsb_4b, sum[earned_income, wsb_se]. earned_for_limit chooses on self_employed (sc_count > 0): earned_income when false, wsb_4b when true. With self_employed true the two are the same value. With it false sc_count is a complete 0 (a lower bound decides gt only true, spec 4.7.5), so each person's sc_count is a complete 0, has_sc is false and eic_se is person.zero ($0); wsb_se sums eic_se over the same roster with no where-test, so it is $0, and wsb_4b is earned_income's value (a sum returns its first operand's refusal at once, and an unknown plus $0 stays unknown). self_employed is never a refusal (its counts sum parameters over rosters, with no gates); it is unknown only with a $person or $sc roster unconfirmed, where the base is unknown and the mutant can be decided (earned_income's refusal), so the argument is over answered inputs: those rosters are asked on every return.",
    ["eic.step5_income", "eic.earned_for_limit", "eic.wsb_4b", "eic.wsb_se", "eic.earned_income", "eic.self_employed", "eic.sc_count", "person.sc_count", "person.has_sc", "person.eic_se", "person.zero", "param:ss.zero"], "5a7f48cd7751a68a", "eic.wsb_4b"),
  "operand.s8812.s8812.line18a.chart_eic.then0": (() => {
    const p = pinned("line18a's taking_eic-true alternative is chart_eic; the mutant reads eiw_7_figured (eiw_3 less eiw_6). It is taken only when Form 1040 line 27a, a copy of eic.credit, is above $0, so eligible is true and line6 is above $0; line6 is line2 or the smaller of line5 and line2, so line2 is above $0, line1_in_table is true and line1 is at least table_start (positive, checked). eligible true makes step1_income and step5_income complete. Line 11b (line 9 less line 10) is complete; line 9 sums line 8, a copy of Schedule 1 line 10, which sums s1.line10_ex5 (a sum that includes Schedule 1 line 3) and Schedule 1 line 5, and line 10 copies Schedule 1 line 26, which sums Schedule 1 line 15, so both are complete. earned_for_limit is complete, so earned_income (Step 5 line 1, line 1z behind scope.schedule1; less line 2, M, the sum of person.mw_not_earned over the person roster; plus line 4, $0 behind s8812.combat_pay) is complete, so M is a complete amount, at least $0, and those gates are false. Then eiw_1a is line 1z, eiw_1b $0 (the same combat-pay gate), eiw_2b Schedule 1 line 3, eiw_3 eiw_3sum floored at zero, eiw_4 M (the same sum over the same field, behind scope.schedule1) and eiw_5 Schedule 1 line 15: eiw_7_figured is max(line 1z + S1 line 3, 0) less (M + S1 line 15). S1 line 3 sums each person's sc_total and line 15 each person's se_line13. With self_employed false every Schedule C roster is empty, line 3 is $0 and each se_line13 is person.zero; chart_eic is earned_income, line 1z less M, and so is eiw_7_figured (line 1z is NonNegDollars, so the floor does not apply). With it true chart_eic is wsb_4b, line 1z plus the sum of each person's eic_se: person.zero for a person with no Schedule C (whose sc_total and se_line13 are $0), sc_total less se_line13 when files_se, and sc_total otherwise, where files_se false means Schedule SE line 4c is $0, so lines 6, the social security base, 10, 11, 12 and 13 of that person's Schedule SE are $0. So wsb_4b is line 1z + S1 line 3 less (M + S1 line 15); line1 (wsb_6, wsb_4b floored) is above $0, so line 1z + S1 line 3 is above M + S1 line 15, itself at least $0, no floor applies, and eiw_7_figured equals chart_eic. Where taking_eic is false or refused the alternative is not evaluated; where it is unknown the alternative is a way (spec 4.7.3) and chart_eic and eiw_7_figured can differ in whether they refuse, so the argument is over answered inputs. A Schedule C roster is empty when self_employed is false because self_employed tests sc_count > 0 and sc_count sums sc.one, a positive parameter (pinned).",
      ["s8812.line18a", "s8812.chart_eic", "s8812.eiw_7_figured", "s8812.taking_eic", "f1040.line27a", "eic.credit", "eic.zero", "eic.line6", "eic.after_line4", "eic.smaller", "eic.line2", "eic.line1_in_table", "eic.line1", "eic.wsb_6", "eic.eligible", "eic.step1_income", "eic.step5_income", "eic.earned_for_limit", "eic.earned_income", "eic.step5_line1", "eic.step5_line2", "eic.step5_line3", "eic.step5_line4", "eic.wsb_4b", "eic.wsb_se", "eic.self_employed", "eic.sc_count", "s8812.eiw_3", "s8812.eiw_3sum", "s8812.eiw_1a", "s8812.eiw_1b", "s8812.eiw_2b", "s8812.eiw_6", "s8812.eiw_4", "s8812.eiw_5", "s8812.zero", "f1040.line11b", "f1040.line11a", "f1040.line9", "f1040.line8", "f1040.line10", "s1.line10", "s1.line10_ex5", "s1.line26", "s1.line3", "s1.line15", "person.sc_total", "person.se_line13", "person.se_line4c", "person.files_se", "person.eic_se", "person.eic_se_has", "person.eic_part1", "person.has_sc", "person.sc_count", "person.zero", "def:se", "param:sales.zero", "param:ss.zero", "sc.one", "param:sc.one"], "03704f7f8e7a4b8d", "s8812.eiw_7_figured");
    return { reason: p.reason, reads: p.reads, premises: p.premises, holds: (d: CanonicalData): boolean => {
      const start = d.params.values["eic.table_start"]?.value;
      return p.holds(d) && typeof start === "number" && start > 0;
    } };
  })(),
  ...Object.fromEntries(([[0, "single"], [2, "mfs"], [3, "hoh"], [4, "qss"]] as const).map(([i, status]) => [`operand.dependent.dependent.spouse_relative_joint.no.then${i}`, pinned(`spouse_relative_joint is a choice on the filing status: mfj takes spouse_relative, every other status takes dependent.no (the parameter household.no, false); the mutant reads qr_other_lawful in place of dependent.no for ${status}. spouse_relative_joint is read by two lines only. qr_other_relation reads it only as the way of the guard 'qr_other_lawful is false', so wherever that alternative is taken qr_other_lawful is a memoized false in the same frame (spec 4.7.6), the value of dependent.no. qr_household_member reads it only as the way of the guard 'household_all_year is false'; qr_other_lawful is a choice on household_all_year whose false alternative is dependent.no, so there too it is false. Where the reader's guard is unknown both alternatives are ways (spec 4.7.3): qr_other_lawful is then that unknown or false (its ways are the input lawful and dependent.no, neither with a refusal gate), never a refusal, as dependent.no never is, so the reader is the guard's unknown on both routes; a refused guard ends the choose with its refusal on both routes. Where the status is unknown the mutant's way is again qr_other_lawful's false or unknown in each reading frame, never a refusal, and the mfj way spouse_relative is the same on both routes.`,
    ["dependent.spouse_relative_joint", "dependent.qr_other_relation", "dependent.qr_household_member", "dependent.qr_other_lawful", "dependent.household_all_year", "dependent.lawful", "dependent.no", "param:household.no"], "f93b2623b91faaa5", "dependent.qr_other_lawful")])),
  "operand.dependent.dependent.qr_dependent.no.then1": pinned("qr_dependent is a choice on qualifying_relative: true takes qr_dependent_resident, false takes dependent.no (the parameter household.no, false); the mutant reads qr_kidnapped in place of dependent.no. qr_kidnapped is a refusal gate of qualifying_relative (its fourth), and a line's gates are evaluated at entry before its expression (spec 4.7.1): qualifying_relative is a known false only when every gate was a known false, so wherever the false alternative is taken qr_kidnapped is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where qualifying_relative is unknown both alternatives are ways (spec 4.7.3); neither dependent.no (a parameter) nor qr_kidnapped (a choice on under_19_kidnap, a comparison of the input age, between kidnapped_if_part_year, a choice on the input lived_all_year between dependent.no and the input kidnapped, and dependent.no, with no refusal gates) refuses, so qr_dependent is that unknown on both routes.",
    ["dependent.qr_dependent", "dependent.qualifying_relative", "dependent.qr_kidnapped", "dependent.under_19_kidnap", "dependent.age", "dependent.kidnapped_if_part_year", "dependent.lived_all_year", "dependent.kidnapped", "dependent.no", "param:household.no"], "0c773da3a4836ecf", "dependent.qr_kidnapped"),
  "operand.dependent.dependent.eic_ssn_child.no.then1": pinned("eic_ssn_child is a choice on eic_child: true takes eic_ssn_known, false takes dependent.no (the parameter household.no, false); the mutant reads kidnap_eic in place of dependent.no. kidnap_eic is eic_child's first refusal gate, evaluated at entry before the expression (spec 4.7.1): eic_child is a known false only when every gate was a known false, so wherever the false alternative is taken kidnap_eic is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where eic_child is unknown both alternatives are ways (spec 4.7.3); neither dependent.no nor kidnap_eic refuses (kidnap_eic is a choice on qc_relationship between kidnap_eic_kidnapped, a choice on kidnapped_if_part_year (a choice on the input lived_all_year between dependent.no and the input kidnapped) between not_us_half and dependent.no, and dependent.no; qc_relationship and not_us_half compare inputs; none has a refusal gate), so eic_ssn_child is that unknown on both routes.",
    ["dependent.eic_ssn_child", "dependent.eic_child", "dependent.eic_ssn_known", "dependent.kidnap_eic", "dependent.kidnap_eic_kidnapped", "dependent.qc_relationship", "dependent.not_us_half", "dependent.us_half", "dependent.kidnapped_if_part_year", "dependent.lived_all_year", "dependent.kidnapped", "dependent.relationship", "dependent.no", "param:household.no"], "82b7384fca9b0aee", "dependent.kidnap_eic"),
  "operand.dependent.dependent.edu_over_refused.edu_no.then1": pinned("dependent.edu_over_refused is a choice on edu_student: true takes edu_over_if_adj, false takes edu_no (the year parameter edu.no, false); the mutant reads edu_has_adj (edu_adj more than $0) in place of edu_no. edu_adj is a choice on the same edu_student whose false alternative is dependent.zero (the parameter sales.zero, $0), so with edu_student a known false (memoized, spec 4.7.6) edu_adj is $0 and edu_has_adj is false, the value of edu_no. A refused guard ends the choose with its refusal on both routes. Where edu_student is unknown both alternatives are ways (spec 4.7.3); edu_no is a parameter and edu_has_adj cannot refuse (edu_adj's alternatives are edu_adj_sum, a sum of three inputs with no refusal gates, and dependent.zero, so edu_adj is never a refusal), so edu_over_refused is that unknown on both routes.",
    ["dependent.edu_over_refused", "dependent.edu_student", "dependent.edu_over_if_adj", "dependent.edu_has_adj", "dependent.edu_adj", "dependent.edu_adj_sum", "dependent.zero", "dependent.edu_no", "param:edu.no", "param:sales.zero"], "658323ac1619d9f1", "dependent.edu_has_adj"),
  "operand.dependent.dependent.married_screen_qr.no": pinned("married_screen_qr is a copy of dependent.no (the parameter household.no, false) behind its refusal gate dependent.married; the mutant reads married_if_ever_married_qc in place of dependent.no. married_screen_qr is read only by married_if_ever_married_qr, a choice on the input ever_married whose true alternative is married_screen_qr and whose false alternative is dependent.no. The copy is evaluated only where married was a known false (spec 4.7.1), memoized in the dependent's frame (spec 4.7.6). Through the reader ever_married is a known true, so married_if_ever_married_qc takes its own ever_married-true alternative, married_screen_qc, a copy of dependent.no behind the same gate dependent.married, a known false: false, the value of dependent.no. Where ever_married is unknown both alternatives of married_if_ever_married_qr are ways (spec 4.7.3) and dependent.no is no refusal, so the reader is that unknown on both routes; where it is false or a refusal the reader does not read married_screen_qr. married_screen_qr's own value differs only where ever_married is unknown and married false, where nothing reads it.",
    ["dependent.married_screen_qr", "dependent.married_if_ever_married_qr", "dependent.married_if_ever_married_qc", "dependent.married_screen_qc", "dependent.married", "dependent.ever_married", "dependent.no", "param:household.no"], "e1c7c9712f4ba7d9", "dependent.married_if_ever_married_qc"),
  "operand.dependent.dependent.married_screen_eic.no": pinned("married_screen_eic is a copy of dependent.no (the parameter household.no, false) behind its refusal gate dependent.married; the mutant reads married_if_ever_married_qr in place of dependent.no. married_screen_eic is read only by married_if_ever_married_eic, a choice on the input ever_married whose true alternative is married_screen_eic and whose false alternative is dependent.no. The copy is evaluated only where married was a known false (spec 4.7.1), memoized in the dependent's frame (spec 4.7.6). Through the reader ever_married is a known true, so married_if_ever_married_qr takes its own ever_married-true alternative, married_screen_qr, a copy of dependent.no behind the same gate dependent.married, a known false: false, the value of dependent.no. Where ever_married is unknown both alternatives of married_if_ever_married_eic are ways (spec 4.7.3) and dependent.no is no refusal, so the reader is that unknown on both routes; where it is false or a refusal the reader does not read married_screen_eic. married_screen_eic's own value differs only where ever_married is unknown and married false, where nothing reads it.",
    ["dependent.married_screen_eic", "dependent.married_if_ever_married_eic", "dependent.married_if_ever_married_qr", "dependent.married_screen_qr", "dependent.married", "dependent.ever_married", "dependent.no", "param:household.no"], "92039ccd5c6fa4c5", "dependent.married_if_ever_married_qr"),
  "operand.household.household.hoh_community_property.no.then1": pinned("hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for mfj. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is mfj (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates.",
    ["household.hoh_community_property", "household.hoh_eligible", "household.hoh_fails", "household.hoh_cp_married", "household.cp_any", "household.no", "f1040.status", "param:household.no"], "4429444b40732dec", "household.cp_any"),
  "operand.household.household.hoh_community_property.no.then2": pinned("hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for mfs. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is mfs (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates.",
    ["household.hoh_community_property", "household.hoh_eligible", "household.hoh_fails", "household.hoh_cp_married", "household.cp_any", "household.no", "f1040.status", "param:household.no"], "4429444b40732dec", "household.cp_any"),
  "operand.household.household.hoh_community_property.no.then4": pinned("hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for qss. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is qss (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates.",
    ["household.hoh_community_property", "household.hoh_eligible", "household.hoh_fails", "household.hoh_cp_married", "household.cp_any", "household.no", "f1040.status", "param:household.no"], "4429444b40732dec", "household.cp_any"),
  "operand.household.household.hoh_missed_test2.no.then1": pinned("hoh_missed_test2 is a choice on household.dependents_any: true takes hoh_missed_cost, false takes household.no (the parameter household.no, false); the mutant reads hoh_missed_person in place of household.no. dependents_any is dependents_listed more than 0, and dependents_listed sums dependent.one (the parameter dependent.one, 1) over the dependent roster with no filter, so dependents_any is a known false only where the roster is known to be empty. There test2_lived_persons and test2_absence_persons, sums of dependent.one over the same empty roster, are both 0, and hoh_missed_person (test2_lived_persons more than test2_absence_persons) is false, household.no's value. dependents_listed reads only the roster and a parameter and has no refusal gate, so dependents_any is never a refusal. Where it is unknown (the roster not given) both alternatives are ways (spec 4.7.3), and a choose is a refusal only when every way is: household.no never refuses, and hoh_missed_person, two sums over a roster not given, is an unknown and no refusal, so on both routes hoh_missed_test2 is dependents_any's unknown, unchanged. So hoh_missed_test2 has the same value on both routes wherever it is evaluated, and its readers, the gate hoh_missed and hoh_missed_mfs_test2 (a choice on it), receive that value on both.",
    ["household.hoh_missed_test2", "household.hoh_missed", "household.hoh_missed_mfs_test2", "household.dependents_any", "household.dependents_listed", "dependent.one", "param:dependent.one", "household.hoh_missed_cost", "household.hoh_missed_person", "household.test2_lived_persons", "household.test2_absence_persons", "household.no", "param:household.no"], "0de216653abd7137", "household.hoh_missed_person"),
  "operand.household.household.hoh_missed_mfs.no.then1": pinned("hoh_missed_mfs is a choice on household.mfs (the filing status equal to mfs; the status is an input with no refusal gates, so mfs is never a refusal): true takes hoh_missed_mfs_listed, false takes household.no (the parameter household.no, false); the mutant reads household.hoh_missed in place of household.no. hoh_missed_mfs is read only by household.hoh_fails, as the second of its two refusal gates; the first is hoh_missed. A line's gates are evaluated at entry in order, and a gate that is true, a refusal or unknown ends them (spec 4.7.1), so hoh_missed_mfs is evaluated only where hoh_missed is a known false, memoized in the same frame (spec 4.7.6): with mfs false the mutant's alternative is false, the value of household.no. A refused guard ends the choose with its refusal on both routes. Where mfs is unknown both alternatives are ways (spec 4.7.3); neither household.no nor hoh_missed (a known false) refuses, so hoh_missed_mfs is that unknown on both routes. The interview's reach pass also evaluates the gates after an unanswered first gate, but only a later gate that is true or a refusal changes what it does; there hoh_missed is unknown, so the base's false and the mutant's alternative (hoh_missed's unknown, or with mfs unknown hoh_missed_mfs's unknown on both routes) are neither, and no new input is read (hoh_missed is memoized).",
    ["household.hoh_missed_mfs", "household.hoh_fails", "household.hoh_missed", "household.mfs", "f1040.status", "household.no", "param:household.no"], "db5d9b9b733e4700", "household.hoh_missed"),
  "operand.dependent.dependent.qc_age_younger.younger.then0": pinned("qc_age_younger is a choice on the input younger: true takes younger (true), false takes disabled; the mutant reads under_24 (age below the parameter qc.student_age_limit, 24) in place of younger in the true alternative. qc_age_younger is read by qc_age, in its under_19-true alternative, and by qc_age_student, in its student-true alternative; qc_age_student is read only by qc_age_19, in its under_24-true alternative. Through qc_age, under_19 (age below the parameter qc.age_limit, 19) is a known true, so age is known and below 19 and under_24 is true. Through qc_age_student, under_24 is a memoized true (spec 4.7.6). Either way the mutant's alternative is true, the base's value. Where under_19, student or under_24 is unknown the alternative is a way (spec 4.7.3), and every way of those choices (younger, disabled, under_24, qc_age_19, qc_age_student) reads only inputs and parameters with no refusal gates, so none refuses and each line is its guard's unknown on both routes. The two age parameters are pinned (19 and 24).",
    ["dependent.qc_age_younger", "dependent.younger", "dependent.disabled", "dependent.under_24", "dependent.qc_age", "dependent.under_19", "dependent.qc_age_student", "dependent.student", "dependent.qc_age_19", "dependent.age", "param:qc.age_limit", "param:qc.student_age_limit"], "4050ec225b08f54d", "dependent.under_24"),
  "operand.sales.sales.bad_aggregate.no.then1": pinned("bad_aggregate is a choice on the route gate line route_if_chosen (an Enum(sales_route)): aggregate takes aggregate_fails, detail takes sales.no (the parameter household.no, false); the mutant reads bad_code in place of sales.no. bad_aggregate is read only by sales.one, as its third refusal gate, after bad_code (the second); gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so bad_aggregate is read only where bad_code is a memoized false in the sale's frame (spec 4.7.6), the value of sales.no. Where route_if_chosen is a refusal, the first guard refuses and bad_aggregate is that refusal on both routes. Where it is unknown both alternatives are ways (spec 4.7.3), and aggregate_fails's way is not the only one: sales.no and the memoized bad_code are not refusals, so bad_aggregate is the route's unknown on both routes.",
    ["sales.bad_aggregate", "sales.one", "sales.bad_code", "sales.route_if_chosen", "sales.aggregate_fails", "sales.digital", "sales.special", "sales.no", "param:household.no", "enum:sales_route"], "10045bc108993621", "sales.bad_code"),
  "operand.person.person.ira_dist_gate.no.then1": pinned("ira_dist_gate is a choice on ira_has (ira_contrib more than $0): true takes ira_dist_if_files, false takes person.no (the parameter household.no, false); the mutant reads ira_basis_gate, all[ira_files_8606, ira_basis_adjusted], in place of person.no. ira_contrib reads inputs with no refusal gates (ira_trad, and sav_trad through the gate sav_trad_if_ira_owner, a choice on the input ira_owner whose other alternative is person.no), so ira_has is never a refusal. With ira_has a known false (memoized, spec 4.7.6), ira_nondeductible, a choice on ira_has whose false alternative is person.zero, is $0, ira_files_8606 (ira_nondeductible more than $0) is false, and ira_basis_gate, an all-test whose first conjunct is ira_files_8606 true, is false, the value of person.no. Where ira_has is unknown both alternatives are ways (spec 4.7.3): ira_nondeductible is then unknown (its person.zero way never refuses), ira_files_8606 is unknown, and ira_basis_gate is false or unknown (ira_basis_adjusted is an input with no refusal gates), never a refusal, so ira_dist_gate is that unknown on both routes.",
    ["person.ira_dist_gate", "person.ira_has", "person.ira_contrib", "person.ira_dist_if_files", "person.ira_basis_gate", "person.ira_files_8606", "person.ira_nondeductible", "person.ira_basis_adjusted", "person.zero", "person.no", "param:household.no", "person.sav_trad_if_ira_owner", "person.ira_owner", "person.sav_trad", "person.ira_trad"], "c968c5f48798705b", "person.ira_basis_gate"),
  "operand.eic.eic.show_wsb6.self_employed.all.1.eq.0": pinned("show_wsb6 is all[eligible, self_employed]; the mutant reads show_wsb4b, all[reached_step5, self_employed], in place of self_employed. eligible is a choice on reached_step5: true takes step5_income, false takes eic.no (the parameter household.no, false); none of these lines has a refusal gate. The second conjunct is reached only when eligible is true or unknown (a false or refused first conjunct ends both tests). eligible is true only through its first alternative, so reached_step5 is then a known true, memoized in the same frame (spec 4.7.6), and show_wsb4b is self_employed's value. Where eligible is unknown, reached_step5 is true or unknown (a false one makes eligible false, a refused one makes it that refusal): if true, show_wsb4b is self_employed's value; if unknown, show_wsb4b is false where self_employed is false, self_employed's refusal where it refuses, and unknown otherwise, which is what the base all-test, already holding eligible's unknown, gives with self_employed in that place.",
    ["eic.show_wsb6", "eic.show_wsb4b", "eic.eligible", "eic.reached_step5", "eic.step5_income", "eic.self_employed", "eic.no", "param:household.no"], "97d51791077de852", "eic.show_wsb4b"),
  "operand.eic.eic.from_step1_income.no.then1": pinned("from_step1_income is a choice on step1_income: true takes from_step1_ssn, false takes eic.no (the parameter household.no, false); the mutant reads eic.clergy in place of eic.no. clergy is scope.schedule1 = true behind its own refusal gate scope.schedule1, so it is false where scope.schedule1 is a known false, that gate's refusal where it is true, unknown where it is unknown, and its refusal where it is a refusal (scope.schedule1 is an any-test over the scope items and their gate lines). step1_income compares Form 1040 line 11b with eic.limit; line 11b copies line 11a, line 9 less line 10, and line 10 has the refusal gate scope.schedule1, so wherever scope.schedule1 is true or a refusal line 10, line 11a and line 11b are refusals and so is step1_income (a subtraction and a comparison return their operands' first refusal, a refusal outranking an unknown, spec 4.7.2). So where the false alternative is taken step1_income is a known false, line 11b is complete, scope.schedule1 is a known false memoized in the same frame (spec 4.7.6), and clergy is false, the value of eic.no. A refused guard ends the choose with its refusal on both routes. Where step1_income is unknown both alternatives are ways (spec 4.7.3); scope.schedule1 is then neither true nor a refusal, so clergy is false or unknown, never a refusal, as eic.no is not, and from_step1_income is that unknown on both routes.",
    ["eic.from_step1_income", "eic.step1_income", "eic.clergy", "eic.no", "eic.limit", "f1040.line11b", "f1040.line11a", "f1040.line10", "f1040.line9", "scope.schedule1", "param:household.no"], "9a897547ab02dcee", "eic.clergy"),
  "operand.dependent.dependent.qualifying_relative.no.then1": pinned("qualifying_relative is a choice on qr_relationship: true takes qr_from_child, false takes dependent.no (the parameter household.no, false); the mutant reads qr_kidnapped in place of dependent.no. qr_kidnapped is qualifying_relative's own fourth and last refusal gate, and a line's gates are evaluated at entry before its expression (spec 4.7.1): the choice is evaluated only when every gate was a known false, so wherever it is evaluated qr_kidnapped is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no, whether the false alternative is taken or is one of the ways past an unknown qr_relationship (spec 4.7.3). A refused guard ends the choose with its refusal on both routes.",
    ["dependent.qualifying_relative", "dependent.qr_kidnapped", "dependent.no", "param:household.no"], "fe0a0a65b5a0fd87", "dependent.qr_kidnapped"),
  "operand.dependent.dependent.odc_person.no.then1": pinned("odc_person is a choice on claimed: true takes odc_from_tin, false takes dependent.no (the parameter household.no, false); the mutant reads ctc_child in place of dependent.no. claimed copies meets_tests behind the refusal gate claimed_no_tin, and meets_tests is a choice on qc_dependent: true takes qc_dependent itself, false takes qr_dependent. So claimed is a known false only through meets_tests's false alternative: qc_dependent is then a memoized false in the dependent's frame (spec 4.7.6), and ctc_child, a choice on qc_dependent whose false alternative is dependent.no, has no refusal gate and is false, the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where claimed is unknown both alternatives are ways (spec 4.7.3) and the base is that unknown, dependent.no being no refusal; the mutant differs only if odc_from_tin and ctc_child both refuse. ctc_child refuses only where qc_dependent refuses, or is true with ctc_from_tin refusing (an unknown qc_dependent leaves dependent.no a way). In both cases meets_tests is that refusal or true, so claimed is unknown only through its gate: claimed_no_tin is a choice on tin_known (no gates; tin_known is a choice on the input citizen_ssn between citizen_ssn itself and the input tin) between meets_tests (tin_known false) and dependent.no (tin_known true), so with tin_known true claimed is meets_tests's refusal or true, with tin_known false the gate is that refusal or true and claimed refuses, and claimed is unknown only with tin_known unknown. odc_from_tin is a choice on tin_known whose false alternative is dependent.no, so with tin_known unknown it is unknown, not a refusal, and odc_person is claimed's unknown on both routes.",
    ["dependent.odc_person", "dependent.claimed", "dependent.claimed_no_tin", "dependent.meets_tests", "dependent.qc_dependent", "dependent.ctc_child", "dependent.ctc_from_tin", "dependent.odc_from_tin", "dependent.tin_known", "dependent.citizen_ssn", "dependent.tin", "dependent.no", "param:household.no"], "21cbc911914ed46d", "dependent.ctc_child"),
  "operand.dependent.dependent.odc_from_tin.no.then1": pinned("odc_from_tin is a choice on tin_known (a choice on the input citizen_ssn between citizen_ssn itself and the input tin, with no gates): true takes odc_from_citizen, false takes dependent.no (the parameter household.no, false); the mutant reads meets_tests in place of dependent.no. odc_from_tin is read only by odc_person, as the alternative its choice on claimed takes when claimed is true. claimed copies meets_tests behind the refusal gate claimed_no_tin, a choice on tin_known: false takes meets_tests, true takes dependent.no. claimed is a known true only when that gate was a known false (spec 4.7.1), which with tin_known false would need meets_tests false and so claimed false, and with tin_known unknown is unknown: so wherever claimed is true tin_known is a memoized true (spec 4.7.6) and odc_from_tin takes odc_from_citizen on both routes. Where claimed is false or a refusal odc_from_tin is not read. Where claimed is unknown both alternatives of odc_person are ways (spec 4.7.3) and its false alternative, dependent.no, is no refusal, so odc_person is claimed's unknown on both routes whatever odc_from_tin is.",
    ["dependent.odc_from_tin", "dependent.odc_person", "dependent.claimed", "dependent.claimed_no_tin", "dependent.meets_tests", "dependent.tin_known", "dependent.citizen_ssn", "dependent.tin", "dependent.no", "param:household.no"], "d0e5b803198e9894", "dependent.meets_tests"),
  "operand.f8962.f8962.marriage.no.then1": pinned("marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for single. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates.",
    ["f8962.marriage", "f8962.alloc", "f8962.line9", "f8962.line24", "f8962.line25", "f8962.no", "f1040.status", "param:household.no"], "60830d6e3f3ea75c", "f8962.alloc"),
  "operand.f8962.f8962.marriage.no.then2": pinned("marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for mfs. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates.",
    ["f8962.marriage", "f8962.alloc", "f8962.line9", "f8962.line24", "f8962.line25", "f8962.no", "f1040.status", "param:household.no"], "60830d6e3f3ea75c", "f8962.alloc"),
  "operand.f8962.f8962.marriage.no.then3": pinned("marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for hoh. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates.",
    ["f8962.marriage", "f8962.alloc", "f8962.line9", "f8962.line24", "f8962.line25", "f8962.no", "f1040.status", "param:household.no"], "60830d6e3f3ea75c", "f8962.alloc"),
  "operand.f8962.f8962.marriage.no.then4": pinned("marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for qss. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates.",
    ["f8962.marriage", "f8962.alloc", "f8962.line9", "f8962.line24", "f8962.line25", "f8962.no", "f1040.status", "param:household.no"], "60830d6e3f3ea75c", "f8962.alloc"),
  "operand.f8962.f8962.alien_branch.no.then1": pinned("alien_branch is a choice on f8962.any: true takes alien_not_barred, false takes f8962.no (the parameter household.no, false); the mutant reads filing in place of f8962.no. filing is all[any, any[applicable, aptc]], so wherever f8962.any is a known false filing is false at its first conjunct (spec 4.7.2), the value of f8962.no. f8962.any is forms > 0, and forms counts the Form 1095-A roster with a parameter field and no filter, so any is never a refusal and is unknown only when that roster is unconfirmed. alien_branch is read only by line24 and line25, in each as the seventh refusal gate, after void_form (the sixth); gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1). void_form is void_forms > 0, a count over the same roster, which is unknown with no lower bound when the roster is unconfirmed (spec 4.7.5: an unconfirmed roster evaluates nothing). So alien_branch is read only where the roster is confirmed and f8962.any is known, and there the two routes agree. alien_branch's own value does differ where nothing reads it: with the roster unconfirmed and line 5 a refusal, filing refuses and alien_not_barred can (through alien_from_income), so every way of the mutant can refuse (spec 4.7.3) and it can be that refusal where the base is the unknown of f8962.any. A reader that reached alien_branch with the roster unconfirmed (anywhere but behind void_form or another line unknown on an unconfirmed roster) would see that difference; alien_branch, line24 and line25 are premises, so a new reader of alien_branch, or a change to the gate lists of line24 or line25, lapses this argument.",
    ["f8962.alien_branch", "f8962.line24", "f8962.line25", "f8962.void_form", "f8962.void_forms", "f8962.any", "f8962.forms", "f8962.filing", "f8962.no", "f1095a.one", "param:sales.one", "param:household.no"], "0afad50cfadbe47c", "f8962.filing"),
  "operand.s1a.s1a.line10_over.tips_threshold.gt.1": s1aPartFigure("s1a.line10_over", "s1a.tips_threshold", "s1a.line9_calc", "s1a.line13_amount", "s1a.line13_ssn", "s1a.line13_claim", "s1a.tips_deduction", "s1a.part2", "s1a.part2_ssn", "s1a.tips", "s1a.tip_ssn", "64040dee83a44dfc"),
  "operand.s1a.s1a.line13_figured.tips_reduction": s1aPartFigure("s1a.line13_figured", "s1a.tips_reduction", "s1a.line12_calc", "s1a.line13_amount", "s1a.line13_ssn", "s1a.line13_claim", "s1a.tips_deduction", "s1a.part2", "s1a.part2_ssn", "s1a.tips", "s1a.tip_ssn", "df2a12adf83300e3"),
  "operand.s1a.s1a.line18_over.ot_threshold.gt.1": s1aPartFigure("s1a.line18_over", "s1a.ot_threshold", "s1a.line17_calc", "s1a.line21_amount", "s1a.line21_ssn", "s1a.line21_claim", "s1a.ot_deduction", "s1a.part3", "s1a.part3_ssn", "s1a.overtime", "s1a.ot_ssn", "506340304468c038"),
  "operand.s1a.s1a.line21_figured.ot_reduction": s1aPartFigure("s1a.line21_figured", "s1a.ot_reduction", "s1a.line20_calc", "s1a.line21_amount", "s1a.line21_ssn", "s1a.line21_claim", "s1a.ot_deduction", "s1a.part3", "s1a.part3_ssn", "s1a.overtime", "s1a.ot_ssn", "d8b2d87638a48655"),
  "operand.asset.asset.s179_bad_test2_test2.over_half.eq.0": pinned("asset.s179_bad_test2_test2 is the test 'over_half eq false'; the mutant tests 's179_bad_test2_test1 eq false' (section 179 not more than the basis). Its only reader is asset.s179_bad_test2_from2, in the alternative whose guard is 'over_half eq false'; from2's only reader is asset.s179_bad_test2, in the alternative whose guard is 's179_bad_test2_test1 eq false', and s179_bad_test2's other alternative is test1 itself. Where both guards hold (taken in the frame, spec 4.7.6), test1 is a known false and over_half a known false, so both tests are true. Where test1 is a refusal, s179_bad_test2 is that refusal on both routes; where it is unknown, its alternative test1 is a way that is unknown, not a refusal, so s179_bad_test2 is test1's unknown on both routes whatever from2 is (spec 4.7.3). So s179_bad_test2, and every line reading it, has the same value on both routes; only the helpers from2 and test2_test2, evaluated as targets of their own, can differ.",
    ["asset.s179_bad_test2_test2", "asset.s179_bad_test2_from2", "asset.s179_bad_test2", "asset.s179_bad_test2_test1", "asset.over_half", "asset.not179"], "27c3bb921a39ae86", "asset.s179_bad_test2_test1"),
  // Form 5695: the guard 'kinds_answered eq false' is never true (each conjunct of the all-test is K true or K false).
  "operand.f5695.f5695.part1_any.no.then1": pinned("f5695.part1_any is a choice on f5695.kinds_answered: true takes f5695.part1_some, false takes f5695.no (the parameter household.no, false); the mutant takes f5695.sec_b_kinds in place of f5695.no. f5695.kinds_answered is an all-test whose every conjunct is any(K eq true, K eq false) over one kind line K (each a Bool choice on f5695.any between the kind's input and f5695.no, with no refusal gate), so each conjunct is true, unknown or a refusal and the all-test is never a known false (spec 4.7.2); the guard 'kinds_answered eq false' is never true. No line among the kind lines, f5695.carry_if_prior (a choice on the input s3.prior_other_forms between the input f5695.carry and f5695.no), f5695.part1_some and f5695.sec_b_kinds (any-tests of those lines) has a refusal gate, so none of them is ever a refusal. Where kinds_answered is true both routes take part1_some; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3); neither way refuses on either route (f5695.no, part1_some and sec_b_kinds are never refusals), so part1_any is kinds_answered's unknown on both routes. No value of part1_any changes.",
    ["f5695.part1_any", "f5695.kinds_answered", "f5695.part1_some", "f5695.sec_b_kinds", "f5695.carry_if_prior", "f5695.carry", "s3.prior_other_forms", "f5695.any", "f5695.no", "param:household.no", "f5695.solar_if_any", "f5695.solar", "f5695.solar_water_if_any", "f5695.solar_water", "f5695.wind_if_any", "f5695.wind", "f5695.geothermal_if_any", "f5695.geothermal", "f5695.line5a_if_any", "f5695.line5a", "f5695.line7a_if_any", "f5695.line7a", "f5695.insulation_if_any", "f5695.insulation", "f5695.doors_if_any", "f5695.doors", "f5695.windows_if_any", "f5695.windows", "f5695.panel_if_any", "f5695.panel", "f5695.audit_if_any", "f5695.audit", "f5695.heat_pump_if_any", "f5695.heat_pump", "f5695.hp_water_heater_if_any", "f5695.hp_water_heater", "f5695.central_ac_if_any", "f5695.central_ac", "f5695.water_heater_if_any", "f5695.water_heater", "f5695.furnace_if_any", "f5695.furnace", "f5695.biomass_if_any", "f5695.biomass"], "83b8a6eb83384b00", "f5695.sec_b_kinds"),
  "operand.f5695.f5695.claiming_part1.no.then1": pinned("f5695.claiming_part1 is a choice on f5695.part1_any: true takes f5695.line13_positive, false takes f5695.no (the parameter household.no, false); the mutant takes f5695.line5a_if_any in place of f5695.no. part1_any is a choice on f5695.kinds_answered (true: f5695.part1_some; false: f5695.no). f5695.kinds_answered is an all-test whose every conjunct is any(K eq true, K eq false) over one kind line K (each a Bool choice on f5695.any between the kind's input and f5695.no, with no refusal gate), so each conjunct is true, unknown or a refusal and the all-test is never a known false (spec 4.7.2); the guard 'kinds_answered eq false' is never true. No line among the kind lines, f5695.carry_if_prior (a choice on the input s3.prior_other_forms between the input f5695.carry and f5695.no), f5695.part1_some and f5695.sec_b_kinds (any-tests of those lines) has a refusal gate, so none of them is ever a refusal. So part1_any is a known false only as part1_some known false, an any-test of which one disjunct is 'line5a_if_any eq true'; that disjunct is then a known false, so the Bool line5a_if_any is false, the value f5695.no gives. Where part1_any is true both routes take line13_positive; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3), and neither f5695.no nor line5a_if_any (a choice on f5695.any between the input f5695.line5a and f5695.no, no refusal gate) ever refuses, so claiming_part1 is part1_any's unknown on both routes. No value of claiming_part1 changes.",
    ["f5695.claiming_part1", "f5695.line13_positive", "f5695.part1_any", "f5695.kinds_answered", "f5695.part1_some", "f5695.sec_b_kinds", "f5695.carry_if_prior", "f5695.carry", "s3.prior_other_forms", "f5695.any", "f5695.no", "param:household.no", "f5695.solar_if_any", "f5695.solar", "f5695.solar_water_if_any", "f5695.solar_water", "f5695.wind_if_any", "f5695.wind", "f5695.geothermal_if_any", "f5695.geothermal", "f5695.line5a_if_any", "f5695.line5a", "f5695.line7a_if_any", "f5695.line7a", "f5695.insulation_if_any", "f5695.insulation", "f5695.doors_if_any", "f5695.doors", "f5695.windows_if_any", "f5695.windows", "f5695.panel_if_any", "f5695.panel", "f5695.audit_if_any", "f5695.audit", "f5695.heat_pump_if_any", "f5695.heat_pump", "f5695.hp_water_heater_if_any", "f5695.hp_water_heater", "f5695.central_ac_if_any", "f5695.central_ac", "f5695.water_heater_if_any", "f5695.water_heater", "f5695.furnace_if_any", "f5695.furnace", "f5695.biomass_if_any", "f5695.biomass"], "392cbc3bc9efe179", "f5695.line5a_if_any"),
  "operand.s2.s2.amt_rel.zero.then1": pinned("s2.amt_rel is a choice on s2.amt_dep_any (eq true, then eq false; exhaustive for a Bool): true takes s2.amt_rel_items, false takes s2.zero (the parameter sales.zero, $0); the mutant reads s2.amt_dep in place of s2.zero. amt_dep_any is the test amt_dep > 0. Where it is a known false, amt_dep is a known NonNegDollars amount not more than 0, so $0, the value s2.zero gives. Where it is true both routes take amt_rel_items; where it is a refusal (a comparison passes its operand's refusal, spec 4.7.2) the first guard ends both routes with it. Where it is unknown, amt_dep is not a refusal (the test would be that refusal), so neither second way refuses, no route has every way a refusal, and amt_rel is amt_dep_any's unknown on both routes (spec 4.7.3). No value of amt_rel changes.",
    ["s2.amt_rel", "s2.amt_dep_any", "s2.amt_dep", "s2.zero", "param:sales.zero"], "90a73c433842427d", "s2.amt_dep"),
  "operand.s2.s2.amt_l15.amt_l13.then1": pinned("s2.amt_l15 is a choice on f1040.gate.sdtw (eq true, then eq false; exhaustive for a Bool): true takes s2.amt_l15_sdtw, false takes s2.amt_l13; the mutant reads s2.amt_l13_14, the sum of s2.amt_l13 and s2.amt_l14, in place of amt_l13. amt_l14 is a choice on the same guard, false taking s2.zero (the parameter sales.zero, $0). Where sdtw is a known false, amt_l14 is $0, so the sum is amt_l13 when amt_l13 is an amount, and amt_l13's own refusal or unknown otherwise (a sum takes its first refusal, else its first unknown, spec 4.7.4; the known $0 adds no mark). Where sdtw is true both routes take amt_l15_sdtw; where it is a refusal it ends both. Where it is unknown, amt_l14's ways are sd.line19 and the never-refusing s2.zero, so amt_l14 is an unknown, never a refusal, and amt_l13_14 is a refusal exactly where amt_l13 is: the second way refuses on one route exactly where it does on the other, so amt_l15 is the first way's refusal (amt_l15_sdtw's) on both routes or sdtw's unknown on both (spec 4.7.3). No value of amt_l15 changes.",
    ["s2.amt_l15", "s2.amt_l13_14", "s2.amt_l14", "s2.zero", "param:sales.zero"], "bbdf8065b36579bf", "s2.amt_l13_14"),
  // ---- lane m1116 begin ----
  "operand.f1116.f1116.line24.line23": pinned("f1116.line24 is the smaller of line 14 and line 23; the mutant reads line 21 in place of line 23. Line 23 is the sum of line 21 and line 22, and line 22 is a copy of f1116.zero, the parameter sales.zero ($0), with no refusal gates, so line 22 is always the amount $0. A sum takes its first refusal, else its first unknown, else the total (spec 4.7.4): where line 21 is an amount, line 23 is that amount plus $0, the same amount; where line 21 is a refusal, line 23 is that refusal; where it is unknown, line 23 is an unknown (the known $0 adds no mark), which compares equal to line 21's. Neither line 23 nor line 21 has refusal gates, so line 24 compares the same operand values on both routes and no value of line 24 changes.",
    ["f1116.line24", "f1116.line23", "f1116.line21", "f1116.line22", "f1116.zero", "param:sales.zero"], "344333e513d41342", "f1116.line21"),
  // ---- lane m1116 end ----
  // ---- lane mutG begin ----
  "operand.f1116.f1116.line18_shown.line17.gt.0": pinned("f1116.line18_shown tests line 17 more than $0; the mutant tests line 15. Line 17 is the sum of line 15 and line 16, and line 16 is a copy of f1116.zero, the parameter sales.zero ($0), with no refusal gates, so line 16 is always the amount $0. A sum takes its first refusal, else its first unknown, else the total (spec 4.7.4): where line 15 is an amount, line 17 is that amount plus $0, the same amount; where line 15 is a refusal, line 17 is that refusal; where it is unknown, line 17 is an unknown (the known $0 adds no mark), which compares equal to line 15's. Neither line 17 nor line 15 has refusal gates, so the test compares the same operand value with $0 on both routes, and line18_shown, read only by line 18's display condition, has the same value on every input.",
    ["f1116.line18_shown", "f1116.line17", "f1116.line15", "f1116.line16", "f1116.zero", "param:sales.zero"], "cfc65fde12fd1ff5", "f1116.line15"),
  // ---- lane mutG end ----
  // ---- lane mk1 begin ----
  "operand.k1p.k1p.b1_neg.zero": pinned("k1p.b1_neg is subtract_floor0 from k1p.zero take k1p.box1_if_any, max(0, 0 - B) where B is k1p.box1_if_any; the mutant takes k1p.b1_pos for k1p.zero, and k1p.b1_pos is subtract_floor0 from k1p.box1_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box1_if_any nor k1p.b1_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b1_pos passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1p.b1_neg", "k1p.b1_pos", "k1p.box1_if_any", "k1p.zero", "param:sales.zero"], "8a7e7990329d1aab", "k1p.b1_pos"),
  "operand.k1p.k1p.b2_neg.zero": pinned("k1p.b2_neg is subtract_floor0 from k1p.zero take k1p.box2_if_any, max(0, 0 - B) where B is k1p.box2_if_any; the mutant takes k1p.b2_pos for k1p.zero, and k1p.b2_pos is subtract_floor0 from k1p.box2_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box2_if_any nor k1p.b2_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b2_pos passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1p.b2_neg", "k1p.b2_pos", "k1p.box2_if_any", "k1p.zero", "param:sales.zero"], "8836fe8d9eca3c1b", "k1p.b2_pos"),
  "operand.k1p.k1p.b3_neg.zero": pinned("k1p.b3_neg is subtract_floor0 from k1p.zero take k1p.box3_if_any, max(0, 0 - B) where B is k1p.box3_if_any; the mutant takes k1p.b3_pos for k1p.zero, and k1p.b3_pos is subtract_floor0 from k1p.box3_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box3_if_any nor k1p.b3_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b3_pos passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1p.b3_neg", "k1p.b3_pos", "k1p.box3_if_any", "k1p.zero", "param:sales.zero"], "055f6d8326295c32", "k1p.b3_pos"),
  "operand.k1s.k1s.loss1.zero": pinned("k1s.loss1 is subtract_floor0 from k1s.zero take k1s.box1_if_any, max(0, 0 - B) where B is k1s.box1_if_any; the mutant takes k1s.gain1 for k1s.zero, and k1s.gain1 is subtract_floor0 from k1s.box1_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box1_if_any nor k1s.gain1 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain1 passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.loss1", "k1s.gain1", "k1s.box1_if_any", "k1s.zero", "param:sales.zero"], "a87649f0c3b2ba28", "k1s.gain1"),
  "operand.k1s.k1s.loss2.zero": pinned("k1s.loss2 is subtract_floor0 from k1s.zero take k1s.box2_if_any, max(0, 0 - B) where B is k1s.box2_if_any; the mutant takes k1s.gain2 for k1s.zero, and k1s.gain2 is subtract_floor0 from k1s.box2_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box2_if_any nor k1s.gain2 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain2 passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.loss2", "k1s.gain2", "k1s.box2_if_any", "k1s.zero", "param:sales.zero"], "2b277af890db19df", "k1s.gain2"),
  "operand.k1s.k1s.loss3.zero": pinned("k1s.loss3 is subtract_floor0 from k1s.zero take k1s.box3_if_any, max(0, 0 - B) where B is k1s.box3_if_any; the mutant takes k1s.gain3 for k1s.zero, and k1s.gain3 is subtract_floor0 from k1s.box3_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box3_if_any nor k1s.gain3 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain3 passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.loss3", "k1s.gain3", "k1s.box3_if_any", "k1s.zero", "param:sales.zero"], "c6ab65ef422a7f2a", "k1s.gain3"),
  "operand.k1s.k1s.loss7.zero": pinned("k1s.loss7 is subtract_floor0 from k1s.zero take k1s.box7_if_any, max(0, 0 - B) where B is k1s.box7_if_any; the mutant takes k1s.gain7 for k1s.zero, and k1s.gain7 is subtract_floor0 from k1s.box7_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box7_if_any nor k1s.gain7 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain7 passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.loss7", "k1s.gain7", "k1s.box7_if_any", "k1s.zero", "param:sales.zero"], "73c7c4be99ae049b", "k1s.gain7"),
  "operand.k1s.k1s.loss8.zero": pinned("k1s.loss8 is subtract_floor0 from k1s.zero take k1s.box8a_if_any, max(0, 0 - B) where B is k1s.box8a_if_any; the mutant takes k1s.gain8 for k1s.zero, and k1s.gain8 is subtract_floor0 from k1s.box8a_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box8a_if_any nor k1s.gain8 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain8 passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.loss8", "k1s.gain8", "k1s.box8a_if_any", "k1s.zero", "param:sales.zero"], "de3fdd384dfbd85c", "k1s.gain8"),
  "operand.k1s.k1s.np_loss.zero": pinned("k1s.np_loss is subtract_floor0 from k1s.zero take k1s.b1_np, max(0, 0 - B) where B is k1s.b1_np; the mutant takes k1s.np_income for k1s.zero, and k1s.np_income is subtract_floor0 from k1s.b1_np take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.b1_np nor k1s.np_income carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.np_income passes it on and the first unknown operand wins, spec 4.7.4).",
    ["k1s.np_loss", "k1s.np_income", "k1s.b1_np", "k1s.zero", "param:sales.zero"], "8df559e51dd00ad9", "k1s.np_income"),
  "operand.k1p.k1p.active.decisions_if_asked.all.0.eq.0": pinned("k1p.active is all[k1p.decisions_if_asked = true, k1p.tenth_if_decisions = true]; the mutant tests k1p.ask_active in place of decisions_if_asked. decisions_if_asked is a choice on ask_active (true: the input k1p.decisions; false: k1p.no, the parameter household.no, false), and tenth_if_decisions is a choice on decisions_if_asked (true: the input k1p.tenth; false: k1p.no). Where decisions_if_asked is true, ask_active is true, so both conjunctions are tenth_if_decisions's value. Where it is false (ask_active false, or decisions answered No), tenth_if_decisions is false and both are false. Where it is unknown, either ask_active is that unknown (has_b2 or general unanswered) and the mutant's first conjunct is the same unknown, or ask_active is true and decisions is unanswered, and in both cases tenth_if_decisions is the unknown of its guard (its other way, k1p.no, never refuses, spec 4.7.3), so both conjunctions are unknown with no conjunct false. None of these lines carries a refusal gate.",
    ["k1p.active", "k1p.decisions_if_asked", "k1p.tenth_if_decisions", "k1p.ask_active", "k1p.decisions", "k1p.tenth", "k1p.no", "param:household.no", "k1p.has_b2", "k1p.general"], "7b0d129c14bed02c", "k1p.ask_active"),
  "operand.k1s.k1s.p1_income.zero": pinned("k1s.p1_income is subtract_floor0 from k1s.b1_passive take k1s.zero (the parameter sales.zero, $0); the mutant takes k1s.col_i, a choice on k1s.ok (true: k1s.np_loss; false: k1s.zero). b1_passive and k1s.b1_np are complementary choices on k1s.material (b1_passive takes k1s.b1_net where material is false and k1s.zero where it is true; b1_np takes b1_net where material is true and zero where it is false), and np_loss is subtract_floor0 from zero take b1_np. Where ok is true: material false makes b1_np $0, so col_i is $0 and the routes agree; material true makes b1_passive $0, and max(0, 0 - col_i) = 0 = max(0, 0 - 0) since col_i is never negative; material unknown makes b1_passive that unknown, the first operand on both routes. Where ok is false col_i is zero and the routes agree. Where ok is a refusal or unknown the two p1_income values can differ, but p1_income is read only by k1s.passive_income and k1s.p5_income_raw, which are read only by k1s.col_h and k1s.p5_income, choices on ok (true: those lines; false: k1s.zero): a refusing guard ends each choice with ok's refusal, and an unknown guard leaves each the unknown of ok, since the other way, zero, never refuses (spec 4.7.3). So every reader agrees.",
    ["k1s.p1_income", "k1s.col_i", "k1s.b1_passive", "k1s.np_loss", "k1s.b1_np", "k1s.material", "k1s.zero", "param:sales.zero", "k1s.ok", "k1s.passive_income", "k1s.col_h", "k1s.p5_income_raw", "k1s.p5_income"], "736e038b4bd94d67", "k1s.col_i"),
  // ---- lane mk1 end ----
  // ---- lane mrental begin ----
  // Schedule E: a loss as a positive amount is the same whether it is taken from zero or from the floored income.
  "operand.royalty.royalty.loss_abs.zero": pinned("royalty.loss_abs is subtract_floor0 from royalty.zero ($0, the parameter sales.zero) take royalty.line21; the mutant takes royalty.line21 from royalty.income, which is subtract_floor0 from royalty.line21 take royalty.zero, that is max(line21, 0). For a known line 21: max(max(line21, 0) - line21, 0) = max(-line21, 0) = max(0 - line21, 0). Where line 21 is unknown or a refusal, royalty.income is that same value, and subtract_floor0 gives the first refusal among its operands, else unknown: both routes give line 21's refusal, or unknown. loss_abs's own refusal gate (not_at_risk_if_loss) is evaluated at entry, before the expression, the same on both routes (spec 4.7.1).",
    ["royalty.loss_abs", "royalty.income", "royalty.line21", "royalty.zero", "param:sales.zero"], "81e494636891158a", "royalty.income"),
  "operand.rental.rental.net_loss.zero": pinned("rental.net_loss is subtract_floor0 from rental.zero ($0, the parameter sales.zero) take rental.line21; the mutant takes rental.line21 from rental.net_income, which is subtract_floor0 from rental.line21 take rental.zero, that is max(line21, 0). For a known line 21: max(max(line21, 0) - line21, 0) = max(-line21, 0). Where line 21 is unknown or a refusal, rental.net_income is that same value: both routes give line 21's refusal, or unknown.",
    ["rental.net_loss", "rental.net_income", "rental.line21", "rental.zero", "param:sales.zero"], "d26464f569f6c690", "rental.net_income"),
  // Schedule E totals over the rentals: an excluded rental's summed field is $0, so the reported filter changes nothing.
  // Its where-test, rental.reported (rental.excluded eq false), is a test on inputs and never refuses.
  "filter.sche.sche.rents": pinnedRefusal("sche.rents sums rental.line3 over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line3 is a choice on rental.excluded: true takes rental.zero ($0), false takes rental.rents (an input). A rental with excluded known true adds $0 on the mutant's route and is skipped on the data's; one with excluded false is summed on both. One with excluded unknown makes the data's sum unknown (its where-test is unknown) and makes rental.line3 unknown on the mutant's (spec 4.7.3: rental.zero never refuses, so not every way refuses), so the sum is unknown on both. rental.excluded is a test on inputs and lines with no refusal gate, and rental.line3 has none, so neither route meets a refusal the other does not.",
    ["sche.rents", "rental.line3", "rental.reported", "rental.excluded", "rental.rents", "rental.zero", "param:sales.zero"], "e0812fb14c3c4af3"),
  "filter.sche.sche.rent_income": pinnedRefusal("sche.rent_income sums rental.net_income (subtract_floor0 from rental.line21 take rental.zero) over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line21 is a choice on rental.excluded whose first alternative, excluded true, is rental.zero ($0): an excluded rental's net income is $0 on the mutant's route and skipped on the data's. With excluded unknown, the data's where-test is unknown and rental.line21 is unknown (its way rental.zero never refuses, spec 4.7.3), so both sums are unknown. With excluded false both sum the same value, refusals included, in the same roster order.",
    ["sche.rent_income", "rental.net_income", "rental.line21", "rental.reported", "rental.excluded", "rental.zero", "param:sales.zero"], "517f7c2dd438eb9d"),
  "filter.sche.sche.rent_netloss": pinnedRefusal("sche.rent_netloss sums rental.net_loss (subtract_floor0 from rental.zero take rental.line21) over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line21 is a choice on rental.excluded whose first alternative, excluded true, is rental.zero ($0), so an excluded rental's net loss is $0 on the mutant's route and skipped on the data's. With excluded unknown, the data's where-test is unknown and rental.line21 is unknown (its way rental.zero never refuses, spec 4.7.3), so both sums are unknown. With excluded false both sum the same value, refusals included, in the same roster order.",
    ["sche.rent_netloss", "rental.net_loss", "rental.line21", "rental.reported", "rental.excluded", "rental.zero", "param:sales.zero"], "8956faed2d0842f1"),
  // The home test: its first conjunct is false whenever there is no personal use.
  "operand.rental.rental.home_pers10_if_any.zero.then1": pinned("rental.home_pers10_if_any's rental.personal_any-false alternative is rental.zero; the mutant reads rental.home_rent_c. Its only reader is rental.home, all(rental.personal_c gt the parameter rental.home_days (14), rental.home_pers10_if_any gt rental.home_rent_c), evaluated in order and false at the first false conjunct. Where rental.personal_any is false, rental.personal_c is its false alternative rental.zero ($0), and 0 gt 14 is false, so rental.home is false before the second conjunct is read. Where personal_any is unknown, rental.home_pers10_if_any is unknown on both routes (neither rental.home_pers10, rental.zero nor rental.home_rent_c refuses), and where it is true both take rental.home_pers10.",
    ["rental.home_pers10_if_any", "rental.home", "rental.personal_c", "rental.personal_any", "rental.zero", "param:sales.zero", "param:rental.home_days", "rental.home_rent_c", "rental.home_pers10"], "c826c9baf05d6afc", "rental.home_rent_c"),
  // Pub. 525 Worksheet 2a, line 5's test: where it changes, line 5 (line 3 less line 4, floored) is $0, so the share is $0.
  "boundary.rec.rec.w2a_line5_more": pinnedRefusal("rec.w2a_line5_more (rec.w2a_line3 gt rec.w2a_line4) is read only by rec.w2a_line7_capped and rec.w2a_line8_capped (true: the share, rec.w2a_line7_share or rec.w2a_line8_share; false: rec.zero), and they only by rec.w2a_line7 and rec.w2a_line8, in their rec.w2a_cap-true alternative. Made inclusive, the test changes only where lines 3 and 4 are known and equal; with either unknown or refused, both tests are that unknown or refusal. The shares are prorate(rec.w2a_line5, line 1 or line 2, rec.w2a_line6), and rec.w2a_line5 is subtract_floor0 from line 3 take line 4, $0 when they are equal. With rec.w2a_cap known true, line 4 is refund.line2, 5d less 5e floored, positive since 5d is more than 5e; line 3 equals it, so rec.w2a_line6 (line 1 plus line 2, of which line 3 is the smaller with 5d) is positive and known: each share is $0, as the data's rec.zero. With rec.w2a_cap known false the capped lines are not read. With rec.w2a_cap unknown, line 4 is unknown (a choice on it) or, where both its ways refuse, a refusal, so the test is the same on both routes.",
    ["rec.w2a_line5_more", "rec.w2a_line7_capped", "rec.w2a_line8_capped", "rec.w2a_line7_share", "rec.w2a_line8_share", "rec.w2a_line5", "rec.w2a_line3", "rec.w2a_line4", "rec.w2a_line6", "rec.w2a_line1", "rec.w2a_line2", "rec.w2a_cap", "refund.line2", "rec.w2a_line7", "rec.w2a_line8", "rec.zero", "param:sales.zero"], "772be5d706c36687"),
  "operand.rec.rec.w2a_line5_more.w2a_line3.gt.0": pinned("rec.w2a_line5_more tests rec.w2a_line3 gt rec.w2a_line4; the mutant tests rec.w2a_line6 gt rec.w2a_line4. rec.w2a_line3 is smaller_of(rec.w2a_line6, refund.line5d_prior_year): not more than line 6, the same refusal where line 6 refuses (line 6 is its first operand), and unknown where line 6 or 5d is unknown. The test is read only by rec.w2a_line7_capped and rec.w2a_line8_capped (true: the share, prorate(rec.w2a_line5, line 1 or line 2, rec.w2a_line6); false: rec.zero), and they only in rec.w2a_cap's true alternative. The routes differ only where line 3 is not more than line 4 and line 6 is more: there rec.w2a_line5 (line 3 less line 4, floored) is $0 and line 6 is positive, so each share is $0, as rec.zero. Where 5d is unknown, line 4 is unknown too (rec.w2a_cap or refund.line2 reads 5d), so both tests are unknown.",
    ["rec.w2a_line5_more", "rec.w2a_line7_capped", "rec.w2a_line8_capped", "rec.w2a_line7_share", "rec.w2a_line8_share", "rec.w2a_line5", "rec.w2a_line3", "rec.w2a_line4", "rec.w2a_line6", "rec.w2a_line1", "rec.w2a_line2", "rec.w2a_cap", "refund.line2", "rec.w2a_line7", "rec.w2a_line8", "rec.zero", "param:sales.zero"], "772be5d706c36687", "rec.w2a_line6"),
  "operand.rec.rec.w2a_line7_capped.zero.then1": pinned("rec.w2a_line7_capped's rec.w2a_line5_more-false alternative is rec.zero ($0); the mutant reads rec.w2a_line5, subtract_floor0 from rec.w2a_line3 take rec.w2a_line4. That alternative is taken only where rec.w2a_line5_more (line 3 gt line 4) is known false, so lines 3 and 4 are known with line 3 not more than line 4 and line 5 is $0. Where the test is unknown, both routes are unknown: neither rec.zero nor rec.w2a_line5 can refuse without the test refusing first (line 5 refuses only where line 3 or line 4 does).",
    ["rec.w2a_line7_capped", "rec.w2a_line5_more", "rec.w2a_line5", "rec.w2a_line3", "rec.w2a_line4", "rec.zero", "param:sales.zero"], "61d06acae43790ab", "rec.w2a_line5"),
  "operand.rec.rec.w2a_line8_capped.zero.then1": pinned("rec.w2a_line8_capped's rec.w2a_line5_more-false alternative is rec.zero ($0); the mutant reads rec.w2a_line7. rec.w2a_line8_capped is read only by rec.w2a_line8, in its rec.w2a_cap-true alternative. With cap true and rec.w2a_line5_more false, rec.w2a_line7 is its cap-true alternative rec.w2a_line7_capped, whose line5_more-false alternative is rec.zero: $0 on both routes. With cap unknown, rec.w2a_line8 is unknown unless every way refuses; the mutant's alternative rec.w2a_line7 is then a choice whose way rec.w2a_line7_capped is $0, so it does not refuse, as rec.zero does not. Where rec.w2a_line5_more is unknown both routes are unknown; it is never unknown where rec.w2a_line1 refuses (line 6, line 3 and the test refuse first).",
    ["rec.w2a_line8_capped", "rec.w2a_line8", "rec.w2a_line7", "rec.w2a_line7_capped", "rec.w2a_line5_more", "rec.w2a_line8_share", "rec.w2a_line7_share", "rec.w2a_line5", "rec.w2a_line3", "rec.w2a_line4", "rec.w2a_line6", "rec.w2a_line1", "rec.w2a_line2", "rec.w2a_cap", "rec.zero", "param:sales.zero"], "81cd99887ea4ff9c", "rec.w2a_line7"),
  // ---- lane mrental end ----
  // ---- lane mint begin ----
  "operand.rental.rental.home.home_pers10_if_any.all.1.gt.0": pinned("rental.home is all[rental.personal_c more than the parameter rental.home_days, rental.home_pers10_if_any more than rental.home_rent_c]; the mutant compares rental.home_pers10 (ten times days_personal, as cents) in place of home_pers10_if_any. personal_c and home_pers10_if_any are both choices on rental.personal_any: true takes personal_raw and home_pers10, false takes rental.zero (the parameter sales.zero, $0); none of these lines has a refusal gate. Where personal_any is a known true, home_pers10_if_any is home_pers10's value, so the second tests agree. Where it is a known false, personal_c is $0, not more than 14, so the first conjunct is a known false and both all-tests end false before the second. Where personal_any is unknown, personal_c and home_pers10_if_any have both alternatives as ways (spec 4.7.3), while home_pers10 reads days_personal directly, so a return that answers days_personal but not personal_any can tell the routes apart; the interview asks days_personal only after personal_any is yes, so the argument is over answered inputs.",
    ["rental.home", "rental.home_pers10_if_any", "rental.home_pers10", "rental.personal_any", "rental.personal_c", "rental.personal_raw", "rental.zero", "param:sales.zero", "param:rental.home_days"], "bd061164adafb3c4", "rental.home_pers10"),
  "operand.rec.rec.to_line1.zero.then1": pinned("rec.to_line1 is a choice on rec.path: true takes rec.line_b, false takes rec.zero (the parameter sales.zero, $0); the mutant takes rec.line_c in place of rec.zero. to_line1's only reader is refund.taxable, a choice on the same rec.path that takes to_line1 only when rec.path is true, and to_line1 then meets the same known true (memoized in the frame, spec 4.7.6) and takes line_b on both routes; where rec.path is a known false, refund.taxable takes refund.taxable_1040 and does not read to_line1. Where rec.path is unknown (scope.recovery or refund.itemized not answered), both alternatives of refund.taxable and of to_line1 are ways (spec 4.7.3), and the mutant's line_c way can refuse (through rec.line11) where rec.zero cannot, so a return with those answers withheld can tell the routes apart; the argument is over answered inputs.",
    ["rec.to_line1", "rec.path", "refund.taxable", "rec.line_b", "rec.line_c", "rec.zero", "param:sales.zero", "refund.taxable_1040"], "ef21d3868246ba52", "rec.line_c"),
  "operand.person.person.f4137_line6.zero.then1": pinned("person.f4137_line6 is a choice on person.f4137_filed (person.f4137_col_c more than $0): true takes person.f4137_line6_figured, false takes person.zero (the parameter ss.zero, $0); the mutant takes person.f4137_line4, the sum of f4137.line4 over the person's Form 4137 roster, in the false alternative. f4137.line4 is subtract_floor0 from line 2 (a copy of person.f4137_col_c) take line 3 (a copy of person.f4137_col_d). f4137_filed is a known false only where col_c is a known $0 (it is NonNegDollars). col_c and col_d are choices on the same scope.tips_unreported_if_pay: false gives person.zero to both; true gives the sums over the f4137row roster of the inputs f4137row.col_c and f4137row.col_d, which have no refusal gate. Where col_d is known, every entry's line 4 is max(0, $0 - col_d) = $0, and the sum over any roster is $0, the data's value, so the only reader, f8959.line2 (the sum of person.f4137_line6 over persons), is the same. Where a row's col_d answer is withheld, the mutant's line 4 is unknown where the data's alternative is $0; and where f4137_filed is unknown both alternatives are ways (spec 4.7.3), and the mutant's way can be unknown or another amount where the data's is $0. So the argument is over answered inputs.",
    ["person.f4137_line6", "person.f4137_filed", "person.f4137_col_c", "person.f4137_col_d", "person.f4137_rows_c", "person.f4137_rows_d", "f4137row.col_c", "f4137row.col_d", "person.f4137_line4", "f4137.line2", "f4137.line3", "f4137.line4", "person.zero", "param:ss.zero", "param:sales.zero", "f8959.line2"], "e1c8d4a7b504bc29", "person.f4137_line4"),
  "operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0": pinned("ira.mfs_cov_matters_trad is all[household.mfs = true, ira.cov_you = 0, household.mfs_apart_all_year = false]; the mutant tests ira.cov_count in place of ira.cov_you. Both sum person.one over the person entries whose person.ira_cov is true; cov_you counts only those whose person.role is taxpayer (enum person_role: taxpayer or spouse). So they differ only on an entry whose role is spouse, or unknown. The second conjunct is reached only where household.mfs is true or unknown (a known false first conjunct ends both tests). A return that is not joint has one person entry, the taxpayer's, and its role is recorded with the roster answer. Every entry is then the taxpayer's and the two counts are equal. A roster that lists a spouse on such a return fails household.roster_ok and is refused at line 1a (household.roster_bad); it is not an answer the interview gives. Where a role is withheld, cov_you is unknown and cov_count is known, so the mutant can be a known false where the base is unknown (mfs.ira.apart_covered with answers withheld). The argument is over answered inputs.",
    ["ira.mfs_cov_matters_trad", "ira.cov_you", "ira.cov_count", "household.mfs", "household.mfs_apart_all_year", "ira.mfs_cov_matters", "person.role", "person.ira_cov", "enum:person_role", "household.roster_ok", "household.roster_bad"], "290c63f5c72ed2d5", "ira.cov_count"),
  "operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0": pinned("eic.check_27c is an any-test of six all-tests, taken in order (a refusal ends it, a true ends it); the mutant's fourth disjunct (D3: reached_step3, has_qc = false, married_rules = false, age_range, us_home = true, status not mfj, qc_of_another_if_lived = true) tests eic.show5 = false in place of eic.has_qc = false. show5 is all[eligible = true, line4 = false, line5_blank = false, line2 > 0]. With the answers given: (a) has_qc true: the base D3 is false; if show5 is false and the other conjuncts of D3 hold, the second disjunct (D1: reached_step3, has_qc, step3_married, status not mfj, qc_of_another_if_lived) holds too, since married_rules false makes step3_married true, and D1 is taken first, so check_27c is true on both routes. (b) has_qc false: show5 true needs eligible true, which (eligible a choice on reached_step5, reached_step5 on reached_step3 then step34, step34 on has_qc false taking step4) needs married_rules false, age_range, us_home true and step4_dependent, that is status mfj or qc_of_another_if_lived false; either makes D3's last two conjuncts fail, so D3 is false on both routes; show5 false gives the base's conjunct. (c) Where show5 refuses: eligible's refusal is met again by D4 (worksheet_a_stop, a choice on eligible) in the base, as the same memoized value (spec 4.7.6); with eligible true, line4 and line5_blank read line3 (Form 1040 line 11b, read first by D0's below_top, whose refusal ends both tests at D0) and line1, and line1 and line2 are read again by D4 through line2_zero (line2 on line1_in_table on line1), so the base refuses with the same refusal; and D3 true in the base means qc_of_another_if_lived true, step4_dependent false and eligible false, so show5 is false, not a refusal. Where eligible or has_qc is unknown (an answer withheld) the two routes can leave different pending values or refusals, so the argument is over answered inputs.",
    ["eic.check_27c", "eic.has_qc", "eic.show5", "eic.eligible", "eic.reached_step5", "eic.reached_step3", "eic.step34", "eic.step4", "eic.step4_age", "eic.step4_home", "eic.step4_dependent", "eic.married_rules", "eic.step3_married", "eic.qc_of_another_if_lived", "eic.age_range", "eic.us_home", "eic.worksheet_a_stop", "eic.line2_zero", "eic.line2", "eic.line4", "eic.line5_blank", "eic.line3", "eic.line1", "eic.below_top", "eic.no", "param:household.no"], "996e5fdc2a5a1793", "eic.show5"),
  "operand.k1s.k1s.p1_loss.zero": pinned("k1s.p1_loss is subtract_floor0 from k1s.zero take k1s.b1_passive, max(0, 0 - B) where B is k1s.b1_passive; the mutant takes k1s.p1_income for k1s.zero, and k1s.p1_income is subtract_floor0 from k1s.b1_passive take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p1_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p1_income and k1s.zero carry no refusal gate of their own.",
    ["k1s.p1_loss", "k1s.p1_income", "k1s.b1_passive", "k1s.zero", "param:sales.zero"], "4f083083fbfe78aa", "k1s.p1_income"),
  "operand.k1s.k1s.p2_loss.zero": pinned("k1s.p2_loss is subtract_floor0 from k1s.zero take k1s.b2_net, max(0, 0 - B) where B is k1s.b2_net; the mutant takes k1s.p2_income for k1s.zero, and k1s.p2_income is subtract_floor0 from k1s.b2_net take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p2_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p2_income and k1s.zero carry no refusal gate of their own.",
    ["k1s.p2_loss", "k1s.p2_income", "k1s.b2_net", "k1s.zero", "param:sales.zero"], "41add8f272212249", "k1s.p2_income"),
  "operand.k1s.k1s.p3_loss.zero": pinned("k1s.p3_loss is subtract_floor0 from k1s.zero take k1s.b3_net, max(0, 0 - B) where B is k1s.b3_net; the mutant takes k1s.p3_income for k1s.zero, and k1s.p3_income is subtract_floor0 from k1s.b3_net take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p3_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p3_income and k1s.zero carry no refusal gate of their own.",
    ["k1s.p3_loss", "k1s.p3_income", "k1s.b3_net", "k1s.zero", "param:sales.zero"], "bc9587da2dc36b2f", "k1s.p3_income"),
  // ---- lane mint end ----
  ...nyEquivalences(),
};

// A keyed argument pinned to its premises. An equivalence argument is about what two routes evaluate to, so the
// digest covers what evaluation, or what a value sheet shows, can depend on, and nothing a reader only reads:
//   - a line premise: its expression (operator, operands in order, constants, parameter and table references,
//     guards, collection and field names, rounding unit and rule); its refusal gates in order, each as its gate
//     line and `when_known` (not the form, remedy and citation a refusal carries: their wording decides no route,
//     and where an argument needs two refusals to be the same value the sampled check below compares the values
//     themselves); its type; its printed marker (a helper's own value is not shown); its display condition; and the
//     sorted list of every line that reads it. An input's expression counts only as being an input: its question
//     text (`source`) is what the filer is asked, and no value depends on it. The line's label, citation, note,
//     ambiguity link, `display` reason and `gated_by` are not covered: evaluation reads none of them into a value.
//   - `param:`: the parameter's type and value. `enum:`: the enum's value names, in order.
//   - `table:`: the table without its title, citation and column notes.
//   - `def:`: the def's id, kind, parameters and collection keys, and each line's id with the same facts as a
//     line premise except its readers.
// The argument holds only while none of those changed; such an edit to a premise, or a new reader of a premise
// line, makes the survivor unexplained again until the argument is re-made. A wording or citation edit does not,
// nor does an edit to a refusal's form, remedy or citation.
function exprFacts(expr: Line["expr"]): unknown {
  return expr.op === "input" ? { op: "input" } : expr;
}

function lineFacts(l: Line) {
  const refuses = (l.refuses ?? []).map((r) => ({ when: r.when, when_known: r.when_known ?? false }));
  return { expr: exprFacts(l.expr), refuses, type: l.type, printed: l.printed, shown_when: l.shown_when ?? null };
}

function tableFacts(t: TableDoc): unknown {
  const { title: _title, cite: _cite, columns, ...rest } = t;
  return columns === undefined ? rest : { ...rest, columns: columns.map((c) => ({ key: c.key, statuses: c.statuses })) };
}

function defFacts(def: FormDoc): unknown {
  const collection = def.collection ? { parent: def.collection.parent ?? null, implicit: def.collection.implicit ?? null } : null;
  return { id: def.id, kind: def.kind, parameters: def.parameters ?? [], collection, lines: def.lines.map((l) => ({ id: l.id, ...lineFacts(l) })) };
}

export function premiseDigest(data: CanonicalData, lines: string[]): string {
  const facts = lines.map((id) => {
    if (id.startsWith("table:")) { const t = data.tables.find((x) => x.id === id.slice(6)); return { id, table: t ? tableFacts(t) : null }; }
    if (id.startsWith("param:")) { const p = data.params.values[id.slice(6)]; return { id, param: p ? { type: p.type, value: p.value } : null }; }
    if (id.startsWith("enum:")) { const e = data.params.enums?.[id.slice(5)]; return { id, enum: e ? { values: e.values } : null }; }
    if (id.startsWith("def:")) { const def = data.defs.find((x) => x.id === id.slice(4)); return { id, def: def ? defFacts(def) : null }; }
    const l = findLine(data, id);
    return l ? { id, ...lineFacts(l), readers: [...new Set(allReaders(data, id))].sort() } : { id, missing: true };
  });
  return createHash("sha256").update(stableStringify(facts)).digest("hex").slice(0, 16);
}

function pinned(reason: string, lines: string[], digest: string, reads: string): Conditional & { reads: string; premises: string[] } {
  return { reason: `${reason} (Premises pinned: ${lines.join(", ")}; the mutant reads ${reads}.)`, reads, premises: lines, holds: (d: CanonicalData): boolean => premiseDigest(d, lines) === digest };
}

// Self-test of what premiseDigest covers. On a synthetic form: each edit that only rewords or re-cites a premise
// leaves the digest, and each edit to something a value can depend on moves it. On the real data: with every
// input's question text, every label, every line citation and every refusal's form, remedy and citation changed, each pinned argument that held still holds;
// and changing the type of any one premise line, or the value of any one premise parameter, un-pins it.
export function premiseDigestSelfTest(baseline: CanonicalData): { problems: string[]; tested: number } {
  const problems: string[] = [];
  const cite = { doc: "t", locator: "t" };
  const line = (id: string, type: string, expr: unknown, extra: Record<string, unknown> = {}) => ({ id: `t.${id}`, printed: id, label: id, type, expr, cite, ...extra });
  const eq = (ref: string, v: unknown) => ({ op: "test", eq: [ref, { const: v }] });
  const synthetic = (): CanonicalData => ({ tax_year: YEAR,
    forms: [{ id: "t", kind: "form", tax_year: YEAR, title: "t", lines: [
      line("asked", "Bool", { op: "input", source: "Did you?" }),
      line("kind", "Enum(tv)", { op: "input", source: "Which kind?" }),
      line("amount", "NonNegDollars", { op: "input", source: "How much?" }),
      line("other", "NonNegDollars", { op: "input", source: "How much else?" }),
      line("zero", "NonNegDollars", { op: "param", ref: "t.zero" }),
      line("bad", "Bool", eq("t.kind", "b")),
      line("worse", "Bool", eq("t.kind", "c")),
      line("total", "NonNegDollars", { op: "sum", of: ["t.amount", "t.other"] }),
      line("over", "Bool", { op: "test", gt: ["t.total", { const: 100 }] }),
      line("share", "NonNegDollars", { op: "multiply_rate", amount: "t.total", rate: { param: "t.rate" } }),
      line("pick", "NonNegDollars", { op: "choose", alternatives: [{ guard: eq("t.asked", true), then: "t.share" }, { guard: eq("t.asked", false), then: "t.zero" }] },
        { refuses: [{ when: "t.bad", form: "Form T", remedy: "Use another form.", cite }, { when: "t.worse", form: "Form T", remedy: "Use another form.", cite }] }),
      line("listed", "NonNegDollars", { op: "sum_over", collection: "d", field: "d.each", where: eq("d.flag", true) }),
      line("spare1", "NonNegDollars", { op: "input", source: "Spare?" }),
      line("spare2", "NonNegDollars", { op: "input", source: "Spare?" }),
      line("spare3", "NonNegDollars", { op: "input", source: "Spare?" }),
      line("apart", "NonNegDollars", { op: "sum", of: ["t.spare1", "t.spare2"] }),
    ] }],
    defs: [{ id: "d", kind: "def", tax_year: YEAR, title: "d", collection: { cite }, lines: [
      { id: "d.flag", printed: "a", label: "flag", type: "Bool", expr: { op: "input", source: "Is it?" }, cite },
      { id: "d.each", printed: "b", label: "each", type: "NonNegDollars", expr: { op: "input", source: "Each amount?" }, cite },
      { id: "d.twice", printed: "(helper)", label: "twice", type: "NonNegDollars", expr: { op: "sum", of: ["d.each", "d.each"] }, cite },
    ] }],
    tables: [{ id: "tt", kind: "keyed", title: "Table", tax_year: YEAR, cite, columns: [{ key: "c", statuses: ["single"], note: "n" }], keys: [{ name: "k", type: "Count" }], cell: "Count", rows: [{ keys: [1], value: 2 }] }],
    params: { tax_year: YEAR, values: { "t.zero": { type: "NonNegDollars", value: 0, cite }, "t.rate": { type: "Rate", value: { num: 1, den: 2 }, cite } }, enums: { tv: { values: ["a", "b", "c"], cite } } },
    register: { tax_year: YEAR, entries: [] } }) as unknown as CanonicalData;
  // t.worse and the spare lines are not premises, so an edit that only points a premise at one of them changes no
  // premise's readers: the digest can move only through the field edited.
  const premises = ["t.asked", "t.kind", "t.amount", "t.other", "t.zero", "t.bad", "t.total", "t.over", "t.share", "t.pick", "t.listed", "t.apart", "param:t.zero", "param:t.rate", "enum:tv", "table:tt", "def:d"];
  const base = premiseDigest(synthetic(), premises);
  type Loose = any;
  const at = (d: CanonicalData, id: string): Loose => findLine(d, id)!;
  const reworded = "changed wording";
  const recited = { doc: "u", locator: "u", quote: "u" };
  const same: [string, (d: Loose) => void][] = [
    ["an input's question text", (d) => { at(d, "t.asked").expr.source = reworded; }],
    ["an enum input's question text", (d) => { at(d, "t.kind").expr.source = reworded; }],
    ["a money input's question text", (d) => { at(d, "t.amount").expr.source = reworded; }],
    ["a line's label", (d) => { at(d, "t.total").label = reworded; }],
    ["a line's citation", (d) => { at(d, "t.pick").cite = recited; }],
    ["a line's note", (d) => { at(d, "t.pick").note = reworded; }],
    ["a parameter's citation", (d) => { d.params.values["t.zero"].cite = recited; }],
    ["an enum's citation", (d) => { d.params.enums.tv.cite = recited; }],
    ["a table's title, citation and column note", (d) => { d.tables[0].title = reworded; d.tables[0].cite = recited; d.tables[0].columns[0].note = reworded; }],
    ["a def's title and collection citation", (d) => { d.defs[0].title = reworded; d.defs[0].collection.cite = recited; }],
    ["a def input's question text, label and citation", (d) => { at(d, "d.flag").expr.source = reworded; at(d, "d.each").label = reworded; at(d, "d.each").cite = recited; }],
    ["a refusal's form, remedy and citation", (d) => { const r = at(d, "t.pick").refuses[0]; r.form = "Form U"; r.remedy = reworded; r.cite = recited; }],
  ];
  const moved: [string, (d: Loose) => void][] = [
    ["an operator", (d) => { at(d, "t.total").expr.op = "smaller_of"; }],
    ["an operand", (d) => { at(d, "t.total").expr.of[1] = "t.zero"; }],
    ["an operand that is not a premise", (d) => { at(d, "t.apart").expr.of[1] = "t.spare3"; }],
    ["the order of operands", (d) => { at(d, "t.total").expr.of.reverse(); }],
    ["a constant", (d) => { at(d, "t.over").expr.gt[1].const = 101; }],
    ["a comparison", (d) => { const e = at(d, "t.over").expr; e.ge = e.gt; delete e.gt; }],
    ["an enum value compared with", (d) => { at(d, "t.bad").expr.eq[1].const = "c"; }],
    ["a parameter reference", (d) => { at(d, "t.share").expr.rate.param = "t.other_rate"; }],
    ["a parameter line's reference", (d) => { at(d, "t.zero").expr.ref = "t.rate"; }],
    ["a guard", (d) => { at(d, "t.pick").expr.alternatives[0].guard = eq("t.over", true); }],
    ["an alternative's line", (d) => { at(d, "t.pick").expr.alternatives[1].then = "t.other"; }],
    ["the order of alternatives", (d) => { at(d, "t.pick").expr.alternatives.reverse(); }],
    ["a collection filter", (d) => { at(d, "t.listed").expr.where = eq("d.flag", false); }],
    ["a collection field", (d) => { at(d, "t.listed").expr.field = "d.twice"; }],
    ["an input made a computed line", (d) => { at(d, "t.amount").expr = { op: "param", ref: "t.zero" }; }],
    ["an input's type", (d) => { at(d, "t.asked").type = "Count"; }],
    ["a computed line's type", (d) => { at(d, "t.total").type = "Dollars"; }],
    ["a refusal gate added", (d) => { at(d, "t.total").refuses = [{ when: "t.worse", form: "Form T", remedy: "Use another form.", cite }]; }],
    ["a second refusal gate added", (d) => { at(d, "t.pick").refuses.push({ when: "t.worse", form: "Form T", remedy: "Use another form.", cite }); }],
    ["a refusal gate removed", (d) => { delete at(d, "t.pick").refuses; }],
    ["a refusal gate's line", (d) => { at(d, "t.pick").refuses[0].when = "t.worse"; }],
    ["a refusal gate's when_known", (d) => { at(d, "t.pick").refuses[0].when_known = true; }],
    ["the order of refusal gates", (d) => { at(d, "t.pick").refuses.reverse(); }],
    ["a display condition", (d) => { at(d, "t.share").shown_when = "t.worse"; }],
    ["a printed marker", (d) => { at(d, "t.share").printed = "(helper)"; }],
    ["a new reader of a premise line", (d) => { d.forms[0].lines.push(line("reader", "NonNegDollars", { op: "copy", from: "t.amount" })); }],
    ["a new reader through a refusal gate", (d) => { d.forms[0].lines.push(line("reader", "NonNegDollars", { op: "param", ref: "t.zero" }, { refuses: [{ when: "t.over", form: "Form T", remedy: "r", cite }] })); }],
    ["a new reader through a display condition", (d) => { d.forms[0].lines.push(line("reader", "NonNegDollars", { op: "param", ref: "t.zero" }, { shown_when: "t.over" })); }],
    ["a premise line removed", (d) => { d.forms[0].lines = d.forms[0].lines.filter((l: Line) => l.id !== "t.other"); }],
    ["a parameter's value", (d) => { d.params.values["t.zero"].value = 1; }],
    ["a rate parameter's value", (d) => { d.params.values["t.rate"].value.den = 3; }],
    ["a parameter's type", (d) => { d.params.values["t.zero"].type = "Dollars"; }],
    ["a parameter removed", (d) => { delete d.params.values["t.rate"]; }],
    ["an enum's value names", (d) => { d.params.enums.tv.values[2] = "z"; }],
    ["an enum's value order", (d) => { d.params.enums.tv.values.reverse(); }],
    ["a table cell", (d) => { d.tables[0].rows[0].value = 3; }],
    ["a table key", (d) => { d.tables[0].rows[0].keys[0] = 2; }],
    ["a table column's statuses", (d) => { d.tables[0].columns[0].statuses = ["mfj"]; }],
    ["a def line's expression", (d) => { at(d, "d.twice").expr.of[1] = "d.flag"; }],
    ["a def line's type", (d) => { at(d, "d.each").type = "Dollars"; }],
    ["a def line's printed marker", (d) => { at(d, "d.twice").printed = "c"; }],
    ["a def line added", (d) => { d.defs[0].lines.push({ id: "d.more", printed: "c", label: "more", type: "Bool", expr: { op: "input", source: "More?" }, cite }); }],
    ["a def's collection parent", (d) => { d.defs[0].collection.parent = "t"; }],
    ["a def's parameters", (d) => { d.defs[0].parameters = ["x"]; }],
  ];
  let tested = 0;
  for (const [what, edit] of same) { const d = synthetic(); edit(d); tested++; if (premiseDigest(d, premises) !== base) problems.push(`premise digest: moved by a change that is only wording or citation (${what})`); }
  for (const [what, edit] of moved) { const d = synthetic(); edit(d); tested++; if (premiseDigest(d, premises) === base) problems.push(`premise digest: not moved by a change a value can depend on (${what})`); }

  const clone = cloneData(baseline);
  for (const doc of allDocs(clone)) for (const l of doc.lines) {
    if (l.expr.op === "input") l.expr.source = `${l.expr.source} ${reworded}`;
    l.label = `${l.label} ${reworded}`;
    l.cite = { ...l.cite, locator: `${l.cite.locator} ${reworded}` };
    for (const r of l.refuses ?? []) { r.form = `${r.form} ${reworded}`; r.remedy = `${r.remedy} ${reworded}`; r.cite = { ...r.cite, locator: `${r.cite.locator} ${reworded}` }; }
  }
  let arguments_ = 0;
  for (const [id, c] of Object.entries(EQUIVALENT_IF)) {
    if (c.premises === undefined || !c.holds(baseline)) continue;
    arguments_++;
    if (!c.holds(clone)) { problems.push(`${id}: rewording every question, label, line citation and refusal's form, remedy and citation un-pinned the argument`); continue; }
    for (const p of c.premises) {
      const prefixed = p.includes(":");
      if (prefixed && !p.startsWith("param:")) continue;
      const entry = prefixed ? clone.params.values[p.slice(6)] : undefined;
      const l = prefixed ? undefined : findLine(clone, p);
      if (!entry && !l) { problems.push(`${id}: premise ${p} is not in the data`); continue; }
      const before = entry ? entry.value : l!.type;
      if (entry) entry.value = entry.value === true ? false : entry.value === false ? true : entry.value === "changed" ? "changed again" : "changed";
      else l!.type = l!.type === "Bool" ? "Count" : "Bool";
      tested++;
      if (c.holds(clone)) problems.push(`${id}: changing ${entry ? "the value" : "the type"} of premise ${p} left the argument pinned`);
      if (entry) entry.value = before as ParamEntry["value"]; else l!.type = before as ValueType;
    }
  }
  if (arguments_ === 0 && Object.values(EQUIVALENT_IF).some((c) => c.premises !== undefined)) problems.push("premise digest self-test exercised no pinned argument");
  return { problems, tested };
}

// Why a surviving mutant is equivalent, checked against the current data: the keyed conditional
// argument when its structural conditions hold, else the first structural rule that accepts it.
export function equivalenceReason(data: CanonicalData, mutation: Mutation): string | undefined {
  const conditional = EQUIVALENT_IF[mutation.id];
  const sameTarget = conditional?.reads === undefined || conditional.reads === mutation.replacement;
  if (conditional && sameTarget && conditional.holds(data)) return conditional.reason + " (structural conditions re-checked this run.)";
  return structuralReason(data, mutation);
}

// Self-test of the `reads` check: for each pinned argument whose mutant is generated and holds, insert an
// unreferenced line of the replacement's type just before the mutated line (an expression reading no line,
// so no premise digest moves), regenerate the mutants, and require that the same id now reads the
// inserted line and no longer takes the pinned argument. Returns the problems found and the number tested.
export function retargetSelfTest(baseline: CanonicalData, muts: Mutation[]): { problems: string[]; tested: number } {
  const problems: string[] = [];
  let tested = 0;
  const byId = new Map(muts.map((m) => [m.id, m]));
  for (const [id, c] of Object.entries(EQUIVALENT_IF)) {
    if (c.reads === undefined) continue;
    const m = byId.get(id);
    if (!m) continue;
    if (m.replacement !== c.reads) { problems.push(`${id}: the pinned argument names ${c.reads} but the mutant reads ${m.replacement ?? "no line"}`); continue; }
    if (!c.holds(baseline)) continue;
    const line = lineOf(m);
    const clone = cloneData(baseline);
    const doc = docOfLine(clone, line);
    const target = findLine(clone, c.reads);
    if (!doc || !target) { problems.push(`${id}: retargeting self-test could not find ${line} or ${c.reads}`); continue; }
    const decoy = `${line}_retarget_decoy`;
    doc.lines.splice(doc.lines.findIndex((l) => l.id === line), 0, { id: decoy, printed: "(helper)", type: target.type, expr: { op: "param", ref: "sales.zero" } } as unknown as Line);
    const retargeted = mutations(clone).find((x) => x.id === id);
    if (retargeted?.replacement !== decoy) { problems.push(`${id}: retargeting self-test did not retarget the mutant to ${decoy}`); continue; }
    if (!c.holds(clone)) { problems.push(`${id}: retargeting self-test moved the premise digest, so it tests nothing`); continue; }
    tested++;
    if (equivalenceReason(clone, retargeted)?.startsWith(c.reason)) problems.push(`${id}: a mutant retargeted to ${decoy} still takes the pinned argument`);
  }
  if (tested === 0 && muts.some((m) => EQUIVALENT_IF[m.id]?.reads !== undefined)) problems.push("retargeting self-test exercised no pinned argument");
  return { problems, tested };
}

// EIC Worksheet A line 2 looks up line 1 in the EIC Table only when line 1 is at least the table's
// first amount (a positive parameter). Line 1 and earned_for_limit choose on the same self-employment
// test between the same earned income and, for a self-employed filer, Worksheet B line 6 (line 4b
// floored at zero) or line 4b itself; at a positive line 1 those agree. A lookup keyed on
// earned_for_limit is therefore read only where the two keys are equal and complete.
function line1KeyInTable(lookup: string) {
  return {
    reason: `${lookup} is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them.`,
    holds: (d: CanonicalData): boolean => {
      const lk = exprOf(d, lookup), table = exprOf(d, "eic.line1_table"), inTable = exprOf(d, "eic.line1_in_table");
      if (lk?.op !== "table_lookup" || lk.key !== "eic.line1" || table?.op !== "choose") return false;
      if (!isHelper(d, lookup) || !isHelper(d, "eic.line1_table")) return false;
      if (!(table.alternatives as { then: unknown }[]).some((a) => a.then === lookup)) return false;
      if (stableStringify(allReaders(d, lookup)) !== stableStringify(["eic.line1_table"])) return false;
      if (stableStringify(allReaders(d, "eic.line1_table")) !== stableStringify(["eic.line2"])) return false;
      if (!bindsBranches(d, "eic.line2", "eic.line1_in_table", "eic.zero", "eic.line1_table")) return false;
      const start = (inTable?.ge as unknown[] | undefined)?.[1] as { param?: string } | undefined;
      const sv = start?.param === undefined ? undefined : d.params.values[start.param]?.value;
      if (inTable?.op !== "test" || (inTable.ge as unknown[])[0] !== "eic.line1" || typeof sv !== "number" || sv <= 0) return false;
      const w6 = exprOf(d, "eic.wsb_6");
      if (w6?.op !== "subtract_floor0" || w6.from !== "eic.wsb_4b" || w6.take !== "eic.zero" || !zeroBehindGates(d, "eic.zero")) return false;
      return bindsBranches(d, "eic.line1", "eic.self_employed", "eic.earned_income", "eic.wsb_6")
        && bindsBranches(d, "eic.earned_for_limit", "eic.self_employed", "eic.earned_income", "eic.wsb_4b")
        && ungated(d, lookup, "eic.line1_table", "eic.line2", "eic.line1_in_table", "eic.line1", "eic.earned_for_limit", "eic.wsb_6", "eic.zero");
    },
  };
}

// scveh.lN looks up the auto_limit table on the vehicle's placed year and the year-N parameter line.
function vehicleLimit(d: CanonicalData, l: string, k: string): boolean {
  const e = exprOf(d, l);
  return e?.op === "keyed_lookup" && e.table === "auto_limit" && stableStringify(e.keys) === stableStringify(["scveh.placed", k]) && ungated(d, l);
}

// Year N of the vehicle: dN = min(lN, tN), tN = rN of the depreciable basis (not negative), rN the GDS rate
// for the vehicle's period, convention and year N.
function vehicleYear(d: CanonicalData, n: number): boolean {
  const dn = exprOf(d, `scveh.d${n}`), tn = exprOf(d, `scveh.t${n}`), rn = exprOf(d, `scveh.r${n}`);
  return dn?.op === "smaller_of" && stableStringify(dn.of) === stableStringify([`scveh.l${n}`, `scveh.t${n}`])
    && tn?.op === "multiply_rate" && tn.amount === "scveh.b100" && tn.rate === `scveh.r${n}` && findLine(d, "scveh.b100")?.type === "NonNegDollars"
    && rn?.op === "keyed_lookup" && rn.table === "macrs_gds" && stableStringify(rn.keys) === stableStringify(["scveh.y5", "scveh.prior_conv", `scveh.k${n}`])
    && exprOf(d, "scveh.y5")?.op === "param" && vehicleLimit(d, `scveh.l${n}`, `scveh.k${n}`) && ungated(d, `scveh.d${n}`, `scveh.t${n}`, `scveh.r${n}`);
}

function exprOf(d: CanonicalData, id: string): Record<string, unknown> | undefined {
  return findLine(d, id)?.expr as unknown as Record<string, unknown> | undefined;
}

// A line that copies, through any refusal gates, the zero parameter.
function zeroBehindGates(d: CanonicalData, id: string): boolean {
  return (stripGuards(normalizeChain(d, id)) as { parameter?: unknown }).parameter === 0;
}

// A line of the form 'its helper when gate G holds, $0 when it does not' (two alternatives,
// guards G == true and G == false), as the Schedule D Tax Worksheet encodes its skip rules.
function gateOf(d: CanonicalData, id: string): { gate: string; then: string } | undefined {
  const e = exprOf(d, id);
  if (e?.op !== "choose") return undefined;
  const alts = e.alternatives as { guard: unknown; then: unknown }[];
  const on = (g: unknown, v: boolean): string | undefined => {
    const eq = (g as { eq?: unknown[] }).eq;
    return Array.isArray(eq) && typeof eq[0] === "string" && stableStringify(eq[1]) === stableStringify({ const: v }) ? eq[0] : undefined;
  };
  if (alts.length !== 2 || typeof alts[0]!.then !== "string" || typeof alts[1]!.then !== "string") return undefined;
  const gate = on(alts[0]!.guard, true);
  if (!gate || on(alts[1]!.guard, false) !== gate || !zeroBehindGates(d, alts[1]!.then as string)) return undefined;
  return { gate, then: alts[0]!.then as string };
}

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

// ---- lane mstruct begin ----
// Unobserved lines. What the product shows or acts on is: every line that is not a helper (`(helper)`, the lines
// no form prints; every other marker, column and worksheet step counts as shown), every line marked `display` (a helper
// kept to be shown on the values sheet), every refusal (the server lists
// each consistency-check refusal among all the values as a conflict, whichever line carries it), every display
// condition, and the interview: its targets decide what is asked and what is figured, and its files and the
// product's code may name lines. A line is unobserved when it is a helper of a form (not of a definition), is not
// marked display, carries no refusal gate, reads no definition instance, is named by none of those, and every line that names it anywhere
// in its expression, refusal gates, display condition or gate is unobserved too. A mutant of such a line changes
// at most the values of those helpers. Computed from the data on every run: when a printed line, a refusal gate,
// an interview target or another observed line comes to read the chain, the rule lapses.

// The line ids named in the built interview profiles, the interview files of the year (federal and New York) and
// the product's code: the evaluator, the values sheet, the interview, the server and the client. A collection
// entry's key names a line with the entry between its document and local id (`person[taxpayer].k1p[a].sche_row`),
// so bracketed entries are dropped and every adjacent pair of a dotted name counts. Read once per run.
let productNamesMemo: Set<string> | undefined;
function productNames(): Set<string> {
  if (productNamesMemo) return productNamesMemo;
  const files: string[] = [];
  const dirFiles = (dir: string, ext: RegExp): void => {
    if (!existsSync(dir)) return;
    for (const f of readdirSync(dir).sort()) if (ext.test(f)) files.push(join(dir, f));
  };
  dirFiles(yearPath("canonical"), /^interview.*\.json$/);
  dirFiles(join(ROOT, "interview", String(YEAR)), /\.ya?ml$/);
  dirFiles(nyPath("interview"), /\.ya?ml$/);
  for (const f of ["eval", "output", "interview", "interview-words", "serve", "spouse-wording", "tick-groups", "gates", "text"]) files.push(join(ROOT, "engine", "src", `${f}.ts`));
  for (const f of ["app", "text"]) files.push(join(ROOT, "ui", `${f}.ts`));
  const names = new Set<string>();
  for (const f of files) {
    if (!existsSync(f)) continue;
    const text = readFileSync(f, "utf8").replace(/\[[^\]]*\]/g, "");
    for (const m of text.matchAll(/[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+/g)) {
      const parts = m[0].split(".");
      for (let i = 0; i + 1 < parts.length; i++) names.add(`${parts[i]}.${parts[i + 1]}`);
    }
  }
  return (productNamesMemo = names);
}

// Every line naming each line id: any string equal to the id anywhere in the naming line (expression, refusal gates,
// display condition, gate), other than its own id. Def-local ids repeat across definitions; a name shared by lines
// of several documents counts as naming each of them, which can only add readers.
type NamingLine = { doc: FormDoc; line: Line };
const namingIndexes = new WeakMap<CanonicalData, Map<string, NamingLine[]>>();
function namingLines(data: CanonicalData, id: string): NamingLine[] {
  let index = namingIndexes.get(data);
  if (!index) {
    index = new Map();
    const ids = new Set(allDocs(data).flatMap((doc) => doc.lines.map((l) => l.id)));
    for (const doc of allDocs(data)) for (const line of doc.lines) {
      const named = new Set<string>();
      const walk = (n: unknown): void => {
        if (typeof n === "string") { if (ids.has(n) && n !== line.id) named.add(n); return; }
        if (Array.isArray(n)) { n.forEach(walk); return; }
        if (n !== null && typeof n === "object") for (const v of Object.values(n)) walk(v);
      };
      for (const [k, v] of Object.entries(line)) if (k !== "id") walk(v);
      for (const n of named) (index.get(n) ?? index.set(n, []).get(n)!).push({ doc, line });
    }
    namingIndexes.set(data, index);
  }
  return index.get(id) ?? [];
}

function readsDef(n: unknown): boolean {
  if (Array.isArray(n)) return n.some(readsDef);
  if (n === null || typeof n !== "object") return false;
  return "def" in n || Object.values(n).some(readsDef);
}

// The unobserved chain from a line of `docId`: the line and every line that names it, transitively, in order of
// discovery, and the lines of the chain that nothing names (the chain's ends); undefined when any is observed.
// A line met again while its own chain is open counts as observed (the checker rejects cycles; this keeps the
// answer conservative if one slipped through).
export function unobservedChain(data: CanonicalData, docId: string, lineId: string, names: Set<string>): { chain: string[]; ends: string[] } | undefined {
  if (allDocs(data).some((doc) => doc.lines.some((l) => l.expr.op === "opaque"))) return undefined; // reads not visible in the data
  const chain: string[] = [];
  const ends: string[] = [];
  const done = new Set<string>();
  const open = new Set<string>();
  const unobserved = (doc: FormDoc | undefined, line: Line | undefined): boolean => {
    if (!doc || !line || doc.kind === "def" || line.printed !== "(helper)") return false;
    if ((line.refuses ?? []).length > 0 || line.shown_when !== undefined || line.display !== undefined || readsDef(line.expr) || names.has(line.id)) return false;
    const key = `${doc.id}\u0000${line.id}`;
    if (done.has(key)) return true;
    if (open.has(key)) return false;
    open.add(key);
    const readers = namingLines(data, line.id);
    const ok = readers.every((r) => unobserved(r.doc, r.line));
    open.delete(key);
    if (!ok) return false;
    done.add(key);
    chain.push(line.id);
    if (readers.length === 0) ends.push(line.id);
    return true;
  };
  const doc = allDocs(data).find((d) => d.id === docId);
  if (!unobserved(doc, doc?.lines.find((l) => l.id === lineId))) return undefined;
  chain.reverse();
  return { chain, ends };
}

// A mutant of a line (not a parameter or a table: unreadParameter and unreadTable cover those) whose unobserved
// chain is complete.
function unobservedLine(data: CanonicalData, mutation: Mutation, names: Set<string> = productNames()): string | undefined {
  if (mutation.id.startsWith("param.") || mutation.id.startsWith("table.")) return undefined;
  const dot = mutation.where.indexOf(".");
  const u = unobservedChain(data, mutation.where.slice(0, dot), mutation.where.slice(dot + 1), names);
  if (!u) return undefined;
  const readers = u.chain.slice(1);
  return `Unobserved line: ${u.chain[0]} is a helper with no refusal gate, read ${readers.length ? `only by helpers (${readers.join(", ")}) that are` : "by no line, and is"} likewise read by no printed line, refusal gate, display condition, definition, interview target or interview file and named in no product code (ends of the chain, read by nothing: ${u.ends.join(", ")}). The mutant can change only those helpers' own values.`;
}

// Self-test of the unobserved-line rule on synthetic forms. A helper H (a copy of a helper x2, mutated to read x1)
// read only by a helper D that nothing reads is accepted, and an evaluation shows no other line changing; then each
// way the product observes a line is planted on D or H in turn and the rule must not apply: D printed, H itself
// printed, D marked display, a printed line gated by a refusal on D, a printed line shown when D, D an interview target or named by
// product code, H carrying a refusal gate, D a definition's line reading H, and D reading a definition instance.
// The collection filter: an unread helper counting the entries of a collection where a helper flag of the entry
// holds is accepted for a mutant of the flag, and not once a printed line reads the count.
export function unobservedLineSelfTest(): string[] {
  const cite = { doc: "t", locator: "t" };
  const L = (id: string, type: string, expr: unknown, extra: Record<string, unknown> = {}) => ({ id, printed: "(helper)", label: id, type, expr, cite, ...extra });
  const input = (id: string, type = "NonNegDollars") => L(id, type, { op: "input", source: id }, { printed: "1" });
  const gate = { when: "t.D", form: "t", remedy: "t", cite };
  type Plant = { lines?: (ls: Record<string, unknown>[]) => void; defs?: unknown[]; names?: string[] };
  const data = (p: Plant = {}) => {
    const lines: Record<string, unknown>[] = [input("t.a"), input("t.f", "Bool"),
      L("t.x1", "NonNegDollars", { op: "copy", from: "t.a" }), L("t.x2", "NonNegDollars", { op: "copy", from: "t.a" }),
      L("t.H", "NonNegDollars", { op: "copy", from: "t.x2" }), L("t.D", "Bool", { op: "test", gt: ["t.H", { const: 0 }] }),
      L("t.P", "NonNegDollars", { op: "copy", from: "t.x1" }, { printed: "2" })];
    p.lines?.(lines);
    return { tax_year: YEAR, forms: [{ id: "t", kind: "form", tax_year: YEAR, title: "t", lines }], defs: p.defs ?? [], tables: [],
      params: { tax_year: YEAR, values: {}, enums: {} }, register: { entries: [] } } as unknown as CanonicalData;
  };
  const at = (ls: Record<string, unknown>[], id: string) => ls.find((l) => l["id"] === id)!;
  const problems: string[] = [];
  const reason = (d: CanonicalData, mid: string, names: string[] = []): string | undefined | null => {
    const m = mutations(d).find((x) => x.id === mid);
    return m ? unobservedLine(d, m, new Set(names)) : null;
  };
  const base = data();
  const accepted = reason(base, "operand.t.t.H.x2");
  if (accepted === null) return ["the synthetic mutant operand.t.t.H.x2 was not generated"];
  if (!accepted?.startsWith("Unobserved line")) problems.push("an unread helper chain (t.H read only by t.D, read by nothing) is not accepted");
  else {
    const m = mutations(base).find((x) => x.id === "operand.t.t.H.x2")!;
    const mut = cloneData(base); m.apply(mut);
    const inputs = { "t.a": 500, "t.f": true };
    const all = allTargets(base, inputs);
    const b = evaluate(base, inputs, all).values, v = evaluate(mut, inputs, all).values;
    for (const k of all) if (!["t.H", "t.D"].includes(k) && normal(b.get(k)! as never) !== normal(v.get(k)! as never)) problems.push(`the accepted mutant changes ${k}, outside the chain`);
  }
  const rejected: [string, Plant][] = [
    ["t.D printed", { lines: (ls) => { at(ls, "t.D")["printed"] = "3"; } }],
    ["t.H itself printed (on a value sheet)", { lines: (ls) => { at(ls, "t.H")["printed"] = "3"; } }],
    ["t.D marked (gate), not (helper)", { lines: (ls) => { at(ls, "t.D")["printed"] = "(gate)"; } }],
    ["t.D marked display (shown on the values sheet)", { lines: (ls) => { at(ls, "t.D")["display"] = "shown on the values sheet"; } }],
    ["a printed line refused when t.D", { lines: (ls) => { at(ls, "t.P")["refuses"] = [gate]; } }],
    ["a printed line shown when t.D", { lines: (ls) => { at(ls, "t.P")["shown_when"] = "t.D"; } }],
    ["t.D an interview target", { names: ["t.D"] }],
    ["t.H named by product code", { names: ["t.H"] }],
    ["t.H carrying a refusal gate", { lines: (ls) => { at(ls, "t.H")["refuses"] = [{ ...gate, when: "t.f" }]; } }],
    ["a helper reading t.D read by a printed line", { lines: (ls) => { ls.push(L("t.E", "Bool", { op: "test", eq: ["t.D", { const: true }] }), L("t.Q", "Bool", { op: "copy", from: "t.E" }, { printed: "4" })); } }],
    ["a definition's line reading t.H", { defs: [{ id: "dd", kind: "def", tax_year: YEAR, title: "dd", lines: [L("dd.r", "NonNegDollars", { op: "copy", from: "t.H" })] }] }],
    ["t.D reading a definition instance", { defs: [{ id: "dd", kind: "def", tax_year: YEAR, title: "dd", lines: [L("dd.r", "NonNegDollars", { op: "copy", from: "t.a" })] }],
      lines: (ls) => { at(ls, "t.D")["expr"] = { op: "test", gt: [{ def: "dd", bind: {}, line: "dd.r" }, "t.H"] }; } }],
  ];
  for (const [what, plant] of rejected) {
    const r = reason(data(plant), "operand.t.t.H.x2", plant.names);
    if (r === null) problems.push(`${what}: the synthetic mutant was not generated`);
    else if (r !== undefined) problems.push(`${what}: the rule still applies`);
  }
  const collection = (countPrinted: boolean) => ({ tax_year: YEAR, defs: [], tables: [], params: { tax_year: YEAR, values: {}, enums: {} }, register: { entries: [] },
    forms: [
      { id: "c", kind: "form", tax_year: YEAR, title: "c", collection: { parent: "p", cite }, lines: [input("c.v"), input("c.w"), L("c.one", "Count", { op: "copy", from: "c.v" }),
        L("c.v2", "NonNegDollars", { op: "copy", from: "c.v" }), L("c.w2", "NonNegDollars", { op: "copy", from: "c.w" }),
        L("c.flag", "Bool", { op: "test", gt: ["c.w2", { const: 0 }] })] },
      { id: "p", kind: "form", tax_year: YEAR, title: "p", collection: { implicit: "x", cite }, lines: [
        L("p.count", "Count", { op: "sum_over", collection: "c", field: "c.one", where: { op: "test", eq: ["c.flag", { const: true }] } }, countPrinted ? { printed: "5" } : {})] },
    ] }) as unknown as CanonicalData;
  const unread = reason(collection(false), "operand.c.c.flag.w2.gt.0");
  if (unread === null) problems.push("the synthetic collection-filter mutant operand.c.c.flag.w2.gt.0 was not generated");
  else if (!unread?.startsWith("Unobserved line")) problems.push("a helper flag read only by an unread collection count's filter is not accepted");
  if (reason(collection(true), "operand.c.c.flag.w2.gt.0")) problems.push("a helper flag read by a printed collection count's filter is accepted");
  return problems;
}
// ---- lane mstruct end ----

// A Schedule 1-A printed line inside a part is a gate: $0 when the part does not apply, otherwise
// the helper that figures it. Equivalences about the figure look through the gate.
function s1aFigure(d: CanonicalData, id: string): Line | undefined {
  const l = findLine(d, id);
  if (l?.expr.op !== "choose") return l;
  const thens = l.expr.alternatives.map((a) => a.then);
  const figure = thens.find((t) => t !== "s1a.zero");
  return thens.length === 2 && thens.includes("s1a.zero") && typeof figure === "string" ? findLine(d, figure) : l;
}

// Every line that reads `id` in any way (an operand, a refusal gate, a display condition).
function allReaders(d: CanonicalData, id: string): string[] {
  return readerSteps(d, id).map((r) => r.reader.id);
}

// A choose of two alternatives that takes `onFalse` when `test` is false and `onTrue` when it is true.
function bindsBranches(d: CanonicalData, chooser: string, test: string, onFalse: string, onTrue: string): boolean {
  const e = exprOf(d, chooser);
  if (e?.op !== "choose") return false;
  const alts = e.alternatives as { guard: unknown; then: unknown }[];
  const g = (v: boolean): string => stableStringify({ op: "test", eq: [test, { const: v }] });
  return alts.length === 2 && alts.some((a) => stableStringify(a.guard) === g(false) && a.then === onFalse)
    && alts.some((a) => stableStringify(a.guard) === g(true) && a.then === onTrue);
}

function ungated(d: CanonicalData, ...ids: string[]): boolean {
  return ids.every((id) => { const l = findLine(d, id); return !!l && !(l.refuses ?? []).length; });
}

function knownRate(d: CanonicalData, r: unknown): boolean {
  const ref = (r as { param?: string } | undefined)?.param;
  const v = ref === undefined ? undefined : d.params.values[ref];
  return v?.type === "Rate" && typeof (v.value as { num?: unknown }).num === "number";
}

// Schedule 1-A phase-outs: 'line A more than line B' chooses between the capped amount and the
// figured amount (the cap less a reduction of the excess). Made inclusive, the test adds only
// A = B, where the excess is zero, so the reduction and the figured amount's subtraction are zero.
// The test is read only by the chooser, so no other value sees the changed Boolean.
// A pinned argument for a removed refusal (a mutant with no replacement operand).
function pinnedRefusal(reason: string, lines: string[], digest: string): Conditional {
  return { reason: `${reason} (Premises pinned: ${lines.join(", ")}.)`, premises: lines, holds: (d: CanonicalData): boolean => premiseDigest(d, lines) === digest };
}

// Schedule 1-A Parts II and III: a helper that reads `gated` (a choice on the part flag between s1a.zero and `figure`)
// where the mutant reads `figure`, read only along the chain amount -> ssn line -> claim line -> printed line.
function s1aPartFigure(over: string, gated: string, figure: string, amount: string, ssnLine: string, claim: string, top: string,
  part: string, partSsn: string, flag: string, ssn: string, digest: string): Conditional & { reads: string } {
  return pinned(`${gated} is a choice on ${part}: false takes s1a.zero, true takes ${figure}; the mutant reads ${figure} in place of ${gated} in ${over}, a helper whose only reader is ${amount}. ${amount}'s only reader is ${ssnLine}, in its ${ssn}-true alternative; ${ssnLine}'s only reader is ${claim}, in its single, mfj, hoh and qss alternatives; ${claim}'s only reader is the printed ${top}, in its ${flag}-true alternative (${top}'s own refusal gates are evaluated at entry, the same on both routes, spec 4.7.1). ${part} is a choice on ${flag} whose true alternative is ${partSsn}, a choice on the status that takes ${ssn} for every status but mfs and s1a.no (false) for mfs. So where those three guards hold (${flag} true, a status other than mfs, ${ssn} true), ${part} is true, ${gated} is ${figure}'s memoized value (spec 4.7.6), and ${over} is the same on both routes. Where one of them is false the alternative reading ${over} is not taken, and where one is refused the choose holding it is that refusal on both routes. Where one is unknown, the choose holding it has another alternative still possible that never refuses (s1a.zero, in ${top}, ${claim} and ${ssnLine}), so it is that guard's unknown on both routes whatever ${over} is (spec 4.7.3). No printed value changes; only the helpers between ${over} and ${top} can differ where ${part} is not true.`,
    [over, gated, figure, amount, ssnLine, claim, top, part, partSsn, flag, ssn, "s1a.no", "s1a.zero", "f1040.status", "param:household.no"], digest, figure);
}

function s1aStepSkip(over: string, magi: string, base: string, pos: string, cut: string, figured: string, cap: string, chooser: string) {
  return {
    reason: `The test '${magi} more than ${base}' made inclusive adds only ${magi} = ${base}; there ${pos} is zero, the reduction ${cut} is zero (zero in whole $1,000 steps, or 6% of zero), and ${figured} (${cap} less ${cut}) equals ${cap}, the value the other branch gives. The test is read only by ${chooser}.`,
    holds: (d: CanonicalData): boolean => {
      const o = findLine(d, over), p = findLine(d, pos), c = s1aFigure(d, cut), f = findLine(d, figured), ch = findLine(d, chooser);
      if (!o || !p || !c || !f || !ch) return false;
      if (o.expr.op !== "test" || !("gt" in o.expr) || stableStringify(o.expr.gt) !== stableStringify([magi, base])) return false;
      if (stableStringify(allReaders(d, over)) !== stableStringify([chooser]) || !bindsBranches(d, chooser, over, cap, figured)) return false;
      if (p.expr.op !== "subtract_floor0" || p.expr.from !== magi || p.expr.take !== base) return false;
      if (c.expr.op !== "multiply_rate" || !knownRate(d, c.expr.rate)) return false;
      const amt = typeof c.expr.amount === "string" ? findLine(d, c.expr.amount) : undefined;
      const fromPos = c.expr.amount === pos || (amt?.expr.op === "round" && amt.expr.of === pos);
      if (!fromPos || f.expr.op !== "subtract_floor0" || f.expr.from !== cap || f.expr.take !== cut) return false;
      return ungated(d, pos, cut, c.id, figured) && (typeof c.expr.amount !== "string" || ungated(d, c.expr.amount));
    },
  };
}

// The Student Loan Interest Deduction Worksheet skips lines 6 and 7 (line 8 is zero) when line 4 is
// not more than line 5. The prorated line's part is line 6 = line 4 - line 5, which is then zero or
// negative, and `prorate` keeps its ratio at 0 or more, so the prorated line is zero there too (its
// whole, the divisor, is a positive parameter for every filing status): the skip and the formula agree,
// and a mutant that crosses between them changes no value. The test is read only by line 8.
function prorateSkip(what: string) {
  return {
    reason: `${what}; there line 6 (line 4 less line 5) is zero or negative, the prorate ratio is kept at 0, and the prorated amount equals the skip branch's zero. The test is read only by line 8.`,
    holds: (d: CanonicalData): boolean => {
      const l8 = findLine(d, "sli.line8"), fig = findLine(d, "sli.line8_figured"), l6 = findLine(d, "sli.line6"), over = findLine(d, "sli.over"), zero = findLine(d, "sli.zero");
      if (!l8 || !fig || !l6 || !over || !zero) return false;
      if (fig.expr.op !== "prorate" || fig.expr.part !== "sli.line6" || fig.expr.amount !== "sli.line1" || fig.expr.whole !== "sli.divisor") return false;
      if (l6.expr.op !== "subtract" || l6.expr.from !== "sli.line4" || l6.expr.take !== "sli.line5") return false;
      if (over.expr.op !== "test" || !("gt" in over.expr) || stableStringify(over.expr.gt) !== stableStringify(["sli.line4", "sli.line5"])) return false;
      if (zero.expr.op !== "param" || d.params.values[zero.expr.ref]?.value !== 0) return false;
      if (stableStringify(allReaders(d, "sli.over")) !== stableStringify(["sli.line8"]) || !bindsBranches(d, "sli.line8", "sli.over", "sli.zero", "sli.line8_figured")) return false;
      const positive = (id: unknown): boolean => {
        const e = typeof id === "string" ? exprOf(d, id) : undefined;
        const v = e?.op === "param" ? d.params.values[e.ref as string]?.value : undefined;
        return typeof v === "number" && v > 0;
      };
      const div = exprOf(d, "sli.divisor");
      if (div?.op !== "choose" || !(div.alternatives as { then: unknown }[]).every((a) => positive(a.then))) return false;
      return findLine(d, "sli.line1")?.type === "NonNegDollars" && ungated(d, "sli.line6", "sli.line8_figured", "sli.divisor");
    },
  };
}

// A Worksheet A line 5 amount whose EIC Table band prints the maximum credit in every column
// that uses it: with line 3 inside [amount, amount + $1) the lookup returns the maximum, line 6
// takes the smaller of it and line 2 (never above the maximum), so blank or not, line 6 is line 2.
// Checked: the plateau in the tables, and the worksheet lines that make "blank or not" equal
// (line 5 blank when line 3 is below the amount; otherwise the smaller of line 5 and line 2).
function thresholdAtPlateau(param: string, tables: string[], col: number) {
  return {
    reason: `Line 5 amount ${param}: in ${tables.join(", ")} the bands covering [${param}, ${param} + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way (only whether line 5 is shown can differ).`,
    holds: (d: CanonicalData): boolean => {
      const v = d.params.values[param]?.value; if (typeof v !== "number") return false;
      const plateau = tables.every((t) => {
        const tb = d.tables.find((x) => x.id === t); if (!tb?.bands) return false;
        const max = Math.max(...tb.bands.map((b) => b.tax[col]!));
        const cover = tb.bands.filter((b) => b.at_least < v + 100 && b.less_than > v);
        return cover.length > 0 && cover.every((b) => b.tax[col] === max);
      });
      const blank = exprOf(d, "eic.line5_blank"), smaller = exprOf(d, "eic.smaller");
      return plateau && blank?.op === "test" && stableStringify(blank.lt) === stableStringify(["eic.line3", "eic.line5_threshold"])
        && bindsBranches(d, "eic.after_line4", "eic.line5_blank", "eic.smaller", "eic.line2")
        && smaller?.op === "smaller_of" && stableStringify(smaller.of) === stableStringify(["eic.line5", "eic.line2"])
        && ungated(d, "eic.line5_blank", "eic.after_line4", "eic.smaller");
    },
  };
}

// A boundary test 'A more than B' made inclusive adds only A = B. The test is read only by a choose
// that takes `atOrBelow` when it is false and `above` when it is true, and `same` checks that the two
// branches give the same value when A = B; both routes evaluate the same operands, so an incomplete A
// or B is the same value on both. `doc` names the def when the lines are a def's (local ids).
function boundaryAgrees(over: string, chooser: string, atOrBelow: string, above: string, reason: string, same: (line: (id: string) => Line | undefined) => boolean, doc?: string) {
  return {
    reason,
    holds: (d: CanonicalData): boolean => {
      const own = doc ? d.defs.find((x) => x.id === doc)?.lines : undefined;
      if (doc && !own) return false;
      const line = (id: string): Line | undefined => (own ? own.find((l) => l.id === id) : findLine(d, id));
      const o = line(over), ch = line(chooser);
      if (!o || o.expr.op !== "test" || !("gt" in o.expr) || !ch || ch.expr.op !== "choose") return false;
      const readers = own
        ? own.filter((l) => operandRefsLocal(l.expr).includes(over) || (l.refuses ?? []).some((r) => r.when === over) || l.shown_when === over).map((l) => l.id)
        : allReaders(d, over);
      const g = (v: boolean): string => stableStringify({ op: "test", eq: [over, { const: v }] });
      const alts = ch.expr.alternatives as { guard: unknown; then: unknown }[];
      const bound = alts.length === 2 && alts.some((a) => stableStringify(a.guard) === g(false) && a.then === atOrBelow)
        && alts.some((a) => stableStringify(a.guard) === g(true) && a.then === above);
      return stableStringify(readers) === stableStringify([chooser]) && bound && same(line);
    },
  };
}

// The local line ids a def line's expression names (every string value outside the non-reference keys).
function operandRefsLocal(expr: unknown): string[] {
  const out: string[] = [];
  const skip = new Set(["ref", "collection", "const", "cite", "type", "op", "unit", "rule", "source", "label", "param"]);
  const walk = (n: unknown): void => {
    if (typeof n === "string") { out.push(n); return; }
    if (Array.isArray(n)) { for (const x of n) walk(x); return; }
    if (n !== null && typeof n === "object") for (const [k, v] of Object.entries(n)) if (!skip.has(k)) walk(v);
  };
  walk(expr);
  return out;
}

// min(X, min(Y, Z)) = min(X, Z) when X <= Y: X is Y less a non-negative W, floored at zero, and Y is
// not negative (both by the checker's NonNegDollars proof). The inner smaller_of is ungated. A refused X
// stops both; an unknown X with a refused Y is impossible (X reads Y); otherwise the incomplete
// operand that wins is the same on both routes.
function minNesting(line: string, x: string, m: string, y: string, z: string) {
  return {
    reason: `${line} is min(${x}, ${m}) and ${m} is the ungated min(${y}, ${z}); ${x} is ${y} less a non-negative amount, floored at zero, with ${y} not negative, so ${x} <= ${y} and min(${x}, min(${y}, ${z})) = min(${x}, ${z}) at every input; ${x} is read first on both routes.`,
    holds: (d: CanonicalData): boolean => {
      const l = exprOf(d, line), mm = exprOf(d, m), xx = exprOf(d, x);
      if (l?.op !== "smaller_of" || stableStringify(l.of) !== stableStringify([x, m])) return false;
      if (mm?.op !== "smaller_of" || stableStringify(mm.of) !== stableStringify([y, z]) || !ungated(d, m, x)) return false;
      if (xx?.op !== "subtract_floor0" || xx.from !== y || typeof xx.take !== "string") return false;
      return findLine(d, xx.take)?.type === "NonNegDollars" && findLine(d, y)?.type === "NonNegDollars";
    },
  };
}

// A vehicle placed in service in 2019 is in its seventh recovery year in 2025, and only then are its
// year 4 to 6 deductions read (through the unrecovered basis, which macrs_pass reads only for a 2019
// vehicle: path dominance). For it the year 4, 5 and 6 limits are one value, and every 5-year GDS
// column has non-increasing rates over years 4 to 6, so min(min(l(n-1), t(n-1)), t(n)) = min(l(n), t(n)).
function vehicle2019(line: string, what: string, check: (d: CanonicalData) => boolean) {
  return {
    reason: `${what} Only a 2019 vehicle's ${line} reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.first_year_after_recovery, so scveh.year and scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on first_year_after_recovery taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument.`,
    holds: (d: CanonicalData): boolean => {
      const is2019 = exprOf(d, "scveh.first_year_after_recovery");
      if (is2019?.op !== "test" || stableStringify(is2019.eq) !== stableStringify(["scveh.year", { const: 7, type: "Count" }])) return false;
      const recovery = d.tables.find((t) => t.id === "recovery_year")?.rows as { keys: unknown[]; value: unknown }[] | undefined;
      if ((recovery ?? []).filter((r) => r.value === 7).map((r) => stableStringify(r.keys)).join() !== stableStringify(["y2019"])) return false;
      const limits = d.tables.find((t) => t.id === "auto_limit")?.rows as { keys: unknown[]; value: unknown }[] | undefined;
      const lim = (n: number): unknown => limits?.find((r) => stableStringify(r.keys) === stableStringify(["y2019", n]))?.value;
      if (typeof lim(4) !== "number" || lim(4) !== lim(5) || lim(5) !== lim(6)) return false;
      const gds = d.tables.find((t) => t.id === "macrs_gds")?.rows as { keys: unknown[]; value: { num: number; den: number } }[] | undefined;
      const period = d.params.values["sc.period_y5"]?.value;
      const convs = [...new Set((gds ?? []).filter((r) => r.keys[0] === period).map((r) => r.keys[1]))];
      const rate = (c: unknown, n: number): number | undefined => {
        const r = gds?.find((x) => x.keys[0] === period && x.keys[1] === c && x.keys[2] === n)?.value;
        return r ? r.num / r.den : undefined;
      };
      const falling = (c: unknown): boolean => {
        const [a, b, e] = [rate(c, 4), rate(c, 5), rate(c, 6)];
        return a !== undefined && b !== undefined && e !== undefined && a >= b && b >= e;
      };
      if (!convs.length || !convs.every(falling)) return false;
      const year = (n: number): unknown => d.params.values[`sc.year${n}`]?.value;
      return year(4) === 4 && year(5) === 5 && year(6) === 6 && dominatedBy(d, line, "scveh.first_year_after_recovery", true) && check(d);
    },
  };
}

const normal = (v: { kind: string; cents?: number; value?: unknown; num?: number; den?: number }): string =>
  v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
    : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;

// `classm:<case>`: killed, but only by class M cases (the first named). A class M rerun regenerates
// those cases, so the kill can be lost unless a stage fixture keeps the case.
type Outcome = "check" | "fixtures" | `classm:${string}` | "survives";

// The fixture cases mutants are judged by. A case evaluates only the lines it expects (`targets`): a line's value is
// memoized per line and depends only on the inputs, not on which other lines the same evaluation is asked for (no
// cycles: the checker rejects them before a mutant is evaluated), so it equals the value a whole-return evaluation
// gives. That holds for a line the whole-return evaluation names (allTargets). A case that also expects a line it
// does not name, such as a def instance's line, which exists only where another line reaches it, keeps the
// whole-return evaluation (`targets` null), so that a mutant that no longer reaches the line still kills the case.
// Which lines allTargets names depends on the documents' lines, the collections and the case's rosters, none of
// which a mutant changes, so the baseline decides it for every mutant.
interface JudgingCases {
  all: (FixtureCase & { file: string; targets: string[] | null })[];
  /** The cases other than class M, grouped by file, in file order. */
  byFile: Map<string, JudgingCases["all"]>;
  /** The class M cases, in file order: the first that kills a mutant is the one reported. */
  classm: JudgingCases["all"];
}

function judgingCases(baseline: CanonicalData): JudgingCases {
  const all = loadFixtureCases(NY_MODE ? "ny" : "federal", baseline).map((c) => {
    const expected = Object.keys(c.expect ?? {});
    const named = new Set(allTargets(baseline, c.inputs));
    const targets = expected.every((t) => named.has(t)) ? expected : null;
    return { ...(c as unknown as FixtureCase), file: c.file, targets };
  });
  const byFile = new Map<string, JudgingCases["all"]>();
  for (const c of all) if (c.evidence !== "M") byFile.set(c.file, [...(byFile.get(c.file) ?? []), c]);
  return { all, byFile, classm: all.filter((c) => c.evidence === "M") };
}

// What happens to one mutant: the checker rejects it, a fixture value changes, or it survives.
// Cases other than class M are tried first, so a kill is attributed to class M only when no other case makes it.
// Among those, mutation.json (small cases built to kill mutants) goes first, then the file named for the mutant's
// document; any order gives the same outcome, the first kill only ends the search sooner.
function outcome(baseline: CanonicalData, cases: JudgingCases, m: Mutation): Outcome {
  const data = cloneData(baseline);
  m.apply(data);
  if (runChecks(data).errors.length > 0) return "check";
  const kills = (c: JudgingCases["all"][number]): boolean => {
    const result = evaluate(data, c.inputs, c.targets ?? allTargets(data, c.inputs));
    for (const [key, expected] of Object.entries(c.expect ?? {})) {
      const der = result.derivations.get(key);
      if (!der || normal(der.value) !== normal(expected)) return true;
    }
    return false;
  };
  const first = ["mutation.json", `${m.where.split(".")[0]}.json`];
  const files = [...new Set([...first, ...cases.byFile.keys()])];
  if (files.some((f) => (cases.byFile.get(f) ?? []).some(kills))) return "fixtures";
  const classm = cases.classm.find(kills);
  return classm ? `classm:${classm.id}` : "survives";
}

// --ny: only the New York mutants (documents ny_*, parameters ny.*, tables ny_*), judged by the New York fixtures;
// otherwise every mutant, as before (a New York mutant is then judged by the federal fixtures, which never read it).
// The keyed arguments of this run's jurisdiction checked on `data` without a mutation run: every generated mutant is
// taken as surviving, so staleEquivalences reports each argument whose mutant is no longer generated, reads another
// line than the argument names, or no longer holds; whether a mutant is killed is left to the run.
export function argumentProblems(data: CanonicalData): string[] {
  const muts = selectMutants(mutations(data));
  return staleEquivalences(EQUIVALENT_IF, ANSWERED_ONLY, data, muts, new Set(muts.map((m) => m.id)));
}

function selectMutants(muts: Mutation[]): Mutation[] {
  // Each jurisdiction's run takes only its own mutants: the federal fixtures never read a New York line, so a
  // New York mutant can be killed only by the New York fixtures (`mutate --ny`, its own check-all step).
  const ny = (m: Mutation): boolean => /\bny[_.]/.test(m.where);
  return NY_MODE ? muts.filter(ny) : muts.filter((m) => !ny(m));
}

function mutantsDigest(muts: Mutation[]): string {
  return createHash("sha256").update(muts.map((m) => m.id).join("\n")).digest("hex");
}

// One worker's share: every `count`-th mutant from `index`, with a digest of the whole
// mutant list so the main thread can confirm every worker split the same list.
export function mutantShare(index: number, count: number): { digest: string; outcomes: [number, Outcome][] } {
  const baseline = loadCanonical();
  const cases = judgingCases(baseline);
  const muts = selectMutants(mutations(baseline));
  const outcomes: [number, Outcome][] = [];
  for (let i = index; i < muts.length; i += count) outcomes.push([i, outcome(baseline, cases, muts[i]!)]);
  return { digest: mutantsDigest(muts), outcomes };
}

// Workers: MUTATE_WORKERS, or defaultWorkers() of pool.ts (core count less six, and at most an equal
// share of the cores among the check-all runs allowed at once); one means no workers.
function workerCount(): number {
  const set = Number(process.env.MUTATE_WORKERS);
  return Number.isInteger(set) && set > 0 ? set : defaultWorkers();
}

async function outcomesOf(baseline: CanonicalData, cases: JudgingCases, muts: Mutation[]): Promise<Outcome[]> {
  const count = workerCount();
  if (count === 1) return muts.map((m) => outcome(baseline, cases, m));
  const digest = mutantsDigest(muts);
  const shares = await Promise.all(Array.from({ length: count }, (_, index) => new Promise<ReturnType<typeof mutantShare>>((done, fail) => {
    const w = new Worker(new URL("./mutate-worker.js", import.meta.url), { workerData: { year: YEAR, index, count, ny: NY_MODE } });
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

// Whether a mutant id belongs to the New York run: the id embeds the mutant's location, which selectMutants tests.
const nyId = (id: string): boolean => /\bny[_.]/.test(id);

// The keyed arguments of `table` (and the ids of `answeredOnly`) for this run's jurisdiction that no longer explain
// a survivor: the mutant is no longer generated (its line, operand or parameter is gone or renamed), it is killed,
// or it survives without the argument applying (the line it says the mutant reads, or a premise it pins, changed).
// Each is one problem naming the entry; the run fails on any, as it does on a stale OPEN_DEFECT_SURVIVORS entry.
export function staleEquivalences(table: Record<string, Conditional>, answeredOnly: Set<string>, data: CanonicalData, muts: Mutation[], survivors: Set<string>): string[] {
  const byId = new Map(muts.map((m) => [m.id, m]));
  const inRun = (id: string): boolean => nyId(id) === NY_MODE;
  const out: string[] = [];
  for (const [id, c] of Object.entries(table)) {
    if (!inRun(id)) continue;
    const m = byId.get(id);
    if (!m) out.push(`${id}: no mutant has this id any more (its line, operand or parameter changed); remove the argument or rewrite it for the mutant that replaced it`);
    else if (!survivors.has(id)) out.push(`${id}: the mutant is killed; the argument explains nothing; remove it`);
    else if (c.reads !== undefined && c.reads !== m.replacement) out.push(`${id}: the argument says the mutant reads ${c.reads}, but it reads ${m.replacement ?? "no line"}`);
    else if (!c.holds(data)) out.push(`${id}: the mutant survives but the argument no longer holds (a line or premise it pins changed)`);
  }
  for (const id of answeredOnly) if (inRun(id) && table[id] === undefined) out.push(`${id}: listed as equivalent on answered inputs only, with no keyed argument`);
  return out;
}

// Self-test of staleEquivalences on the real data: a keyed argument that explains a surviving mutant is not reported;
// planted copies of it are, under an id no mutant has, with its mutant killed, read through another line, with a line
// premise of the argument changed in a copy of the data, and listed as answered-only with no argument. Also checks that
// every generated mutant's id and location agree on the jurisdiction, which the scope test above relies on.
export function staleEquivalenceSelfTest(baseline: CanonicalData, muts: Mutation[], survivors: Set<string>): { problems: string[]; planted: number } {
  const problems: string[] = [];
  let planted = 0;
  for (const m of mutations(baseline)) if (nyId(m.id) !== /\bny[_.]/.test(m.where)) problems.push(`${m.id}: its id and its location (${m.where}) disagree on the jurisdiction`);
  const byId = new Map(muts.map((m) => [m.id, m]));
  const used = Object.entries(EQUIVALENT_IF).find(([id, c]) => nyId(id) === NY_MODE && survivors.has(id) && byId.has(id) && c.premises?.some((p) => !p.includes(":"))
    && (c.reads === undefined || c.reads === byId.get(id)!.replacement) && c.holds(baseline));
  if (!used) {
    if (Object.keys(EQUIVALENT_IF).some((id) => nyId(id) === NY_MODE && survivors.has(id))) problems.push("stale-argument self-test found no pinned argument explaining a survivor to plant from");
    return { problems, planted };
  }
  const [id, c] = used;
  const none = new Set<string>();
  const expect = (what: string, table: Record<string, Conditional>, answered: Set<string>, data: CanonicalData, alive: Set<string>, stale: boolean): void => {
    const found = staleEquivalences(table, answered, data, muts, alive);
    if (stale) planted++;
    if (stale && found.length !== 1) problems.push(`stale-argument self-test: ${what} was ${found.length === 0 ? "not reported" : "reported more than once"}`);
    if (!stale && found.length !== 0) problems.push(`stale-argument self-test: ${what} was reported: ${found.join("; ")}`);
  };
  expect(`the argument ${id}, which explains its surviving mutant`, { [id]: c }, none, baseline, survivors, false);
  const planted_ = NY_MODE ? "operand.ny_planted.ny_planted.line1.line0" : "operand.planted.planted.line1.line0";
  expect("an argument for a mutant that no longer exists", { [planted_]: c }, none, baseline, survivors, true);
  expect("an argument whose mutant is killed", { [id]: c }, none, baseline, new Set([...survivors].filter((s) => s !== id)), true);
  expect("an argument naming another line than the mutant reads", { [id]: { ...c, reads: `${byId.get(id)!.replacement ?? id}_planted` } }, none, baseline, survivors, true);
  const changed = cloneData(baseline);
  const premise = findLine(changed, c.premises!.find((p) => !p.includes(":"))!)!;
  premise.type = premise.type === "Bool" ? "Count" : "Bool";
  expect(`an argument whose premise ${c.premises!.find((p) => !p.includes(":"))} changed`, { [id]: c }, none, changed, survivors, true);
  expect("an answered-only listing with no argument", {}, new Set([planted_]), baseline, survivors, true);
  return { problems, planted };
}

// A survivor that a recorded, still-open defect explains: it is not equivalent and is not excluded from
// the adjusted score, but it does not fail the run while the bug entry is open. The run fails if a listed
// mutant is killed (the entry is stale) or the bug entry is missing. Each jurisdiction's run checks only the entries
// for its own mutants (a New York mutant's id names an ny_ document or an ny. parameter, as selectMutants tells them).
const OPEN_DEFECT_SURVIVORS_ALL: Record<string, string> = {
  "operand.s2.s2.amt_l7.amt_l39.then1": "BUG-0764",
  "operand.s2.s2.amt_tmt_over.amt_l7.gt.0": "BUG-0764",
  "operand.s2.s2.amt_l16.amt_l15": "BUG-0764",
  "operand.k1s.k1s.col_h.zero.then1": "BUG-0928",
  "operand.k1s.k1s.col_i.zero.then1": "BUG-0928",
  "operand.k1s.k1s.col_k.zero.then1": "BUG-0928",
  "operand.k1s.k1s.p5_income.zero.then1": "BUG-0928",
  "operand.person.person.f8919_line10.f8919_line10_figured.then0": "BUG-0928",
};
const OPEN_DEFECT_SURVIVORS: Record<string, string> = Object.fromEntries(
  Object.entries(OPEN_DEFECT_SURVIVORS_ALL).filter(([id]) => /\.ny[_.]/.test(id) === NY_MODE));

// ---- The sampled check of the keyed arguments ----
// A keyed argument (EQUIVALENT_IF) is prose about the data, and its premise pin says only that the data it read has
// not changed since it was made. The sampled check tests what the argument claims by execution: the mutant and the
// data are evaluated on a sample of input sets, and every line that reads the mutated line, directly or through
// other lines, refusal gates or display conditions, and is on a value sheet (not a helper), must have the same value
// under both (unknowns are one value, as in the fixtures). The mutated line's own value may differ, and so may a
// helper's: an argument can be about what the lines that read them show (a helper is evaluated on every return,
// also where no line that reads it takes its value).
// The input sets are SAMPLED_RETURNS generated returns and the inputs of every fixture case, each as given and with
// answers withheld at each rate of SAMPLED_RATES (each answer at the rate, each roster, with its entries, at a quarter
// of it).
// An argument listed in ANSWERED_ONLY claims less and is held only to the sets that are answered returns: those as
// given whose interview reaches no input they leave unanswered (partialLabels). A set as given that still reaches an
// unanswered input (a fixture case written before a question was added) is partial, as the withheld sets are.
// A set reaches the mutant where a line the mutant changes reads other operands, or has another value, than under the
// data; it exercises the mutant where a value the mutant can change differs (the readers were shown the change and
// none passed it on to a value sheet). An argument that no set reaches is not backed by the sample: it fails the run
// unless UNEXERCISED_IF states why, with a condition the run checks.
const UNEXERCISED_IF: Record<string, { reason: string; holds: (data: CanonicalData) => boolean }> = unexercisedNy();

function unexercisedNy(): Record<string, { reason: string; holds: (data: CanonicalData) => boolean }> {
  const out: Record<string, { reason: string; holds: (data: CanonicalData) => boolean }> = {};
  // A New York band edge (bandEdge): only a taxable amount of exactly the edge plus $1 tells the mutant apart, and no
  // generated return or fixture lands on it. The argument's own condition is arithmetic, not a premise digest: it
  // requires every amount the def is bound to to be whole dollars and computes both bands' tax at edge plus $1.
  for (const id of Object.keys(EQUIVALENT_IF)) if (/^param\.ny\.(rs|city)\.[a-z]+\.b[0-9]+\.upper\.\$1$/.test(id)) {
    out[id] = { reason: "only edge + $1 can differ, and the argument computes both bands' tax there", holds: (d) => EQUIVALENT_IF[id]!.premises === undefined && EQUIVALENT_IF[id]!.holds(d) };
  }
  // The MCTMT rates multiply lines 54a and 54b, each the parameter ny.zero ($0) behind the MCTMT refusal gate: on
  // every return the rate multiplies $0 or the line refuses first, so no input can reach the change.
  for (const [zone, amount] of [["zone1", "ny_it201.line54a"], ["zone2", "ny_it201.line54b"]] as const) {
    out[`param.ny.mctmt.${zone}.+1pt`] = { reason: `the rate multiplies ${amount}, which is ny.zero ($0) behind its refusal gate`, holds: (d) => {
      const e = findLine(d, amount)?.expr as { op?: string; ref?: string } | undefined;
      return e?.op === "param" && e.ref === "ny.zero" && d.params.values["ny.zero"]?.value === 0 && EQUIVALENT_IF[`param.ny.mctmt.${zone}.+1pt`]!.holds(d);
    } };
  }
  return out;
}
const SAMPLED_RETURNS = ((n) => (Number.isInteger(n) && n >= 0 ? n : 300))(Number(process.env.MUTATE_SAMPLE ?? 300));
const SAMPLED_RATES = [0, 0.1, 0.3, 0.6];
const SAMPLE_SEED = 20261115;

/** A sampled input set: where it came from, the rate its answers were withheld at, the inputs, and whether it is a
 * partial return (answers withheld, or as given with an input the interview reaches left unanswered). */
type SampleSet = { label: string; rate: number; inputs: Record<string, unknown>; partial: boolean };

function mulberry32(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** The inputs with each answer left out with probability `rate`, and each roster with a quarter of it, by a stream
 * fixed by `seed`. A roster left out takes its entries with it: their answers and the rosters inside them. */
export function withholdAnswers(inputs: Record<string, unknown>, rate: number, seed: number): Record<string, unknown> {
  if (rate === 0) return inputs;
  const next = mulberry32(seed);
  const keys = Object.keys(inputs).sort();
  const rosters = new Set(keys.filter((k) => k.startsWith("$") && next() < rate / 4));
  // `$x` holds the entries `x[k]`, and `$x@p` the entries `p.x[k]`.
  const entries = [...rosters].map((k) => (k.includes("@") ? `${k.slice(k.indexOf("@") + 1)}.${k.slice(1, k.indexOf("@"))}[` : `${k.slice(1)}[`));
  const inside = (path: string): boolean => entries.some((e) => path.startsWith(e));
  const out: Record<string, unknown> = {};
  for (const key of keys) {
    const keep = key.startsWith("$") ? !rosters.has(key) && !(key.includes("@") && inside(key.slice(key.indexOf("@") + 1))) : !inside(key) && next() >= rate;
    if (keep) out[key] = inputs[key];
  }
  return out;
}

/** The input sets as given, before any answer is withheld: the generated returns, then every fixture case. */
function givenSets(baseline: CanonicalData, cases: JudgingCases): { label: string; inputs: Record<string, unknown> }[] {
  const generated = NY_MODE
    ? fc.sample(nyReturnArbitrary(baseline), { seed: SAMPLE_SEED, numRuns: SAMPLED_RETURNS })
    : sampleReturns(federalDocuments(baseline), SAMPLED_RETURNS, SAMPLE_SEED);
  return [
    ...(SAMPLED_RETURNS === 0 ? [] : generated).map((inputs, i) => ({ label: `generated return ${i} (seed ${SAMPLE_SEED})`, inputs })),
    ...cases.all.map((c) => ({ label: `fixture case ${c.id}`, inputs: c.inputs as Record<string, unknown> })),
  ];
}

/** Whether a return as given is partial: the interview of this run's jurisdiction still reaches an input it does not
 * answer (interviewStatus's reachable inputs). */
export function isPartialReturn(data: CanonicalData, config: InterviewData, inputs: Record<string, unknown>): boolean {
  return interviewStatus(data, config, inputs).reachableInputs.length > 0;
}

/** The labels of the sets as given that are partial returns (isPartialReturn), computed once for every worker. */
export function partialLabels(baseline: CanonicalData, cases: JudgingCases): string[] {
  const config = loadInterview(NY_MODE ? "ny" : "full");
  return givenSets(baseline, cases).filter((g) => isPartialReturn(baseline, config, g.inputs)).map((g) => g.label);
}

/** The sampled input sets of this run's jurisdiction; `partial` are the labels of the sets as given that are partial
 * returns (partialLabels). */
function sampleSets(baseline: CanonicalData, cases: JudgingCases, partial: Set<string>): SampleSet[] {
  return givenSets(baseline, cases).flatMap((g, i) => SAMPLED_RATES.map((rate, r) => ({ label: g.label, rate,
    inputs: withholdAnswers(g.inputs, rate, SAMPLE_SEED + 7919 * i + r), partial: rate > 0 || partial.has(g.label) })));
}

/** The line a derivation key is of: a top-level line's key is its id, `coll[k].x` and `p[k].coll[j].x` are lines of
 * their collection's document, and a def instance's `...|inst:def#{bindings}.x` is `def#x` (a def's line is read only
 * inside its instances, through the line that reads the instance). */
export function lineOfKey(key: string): string {
  const inst = key.lastIndexOf("|inst:");
  if (inst >= 0) return `${key.slice(inst + 6, key.indexOf("#", inst))}#${key.slice(key.lastIndexOf("}") + 2)}`;
  const close = key.lastIndexOf("]");
  if (close < 0) return key;
  const doc = /([^.\[\]]+)\[[^\]]*\]$/.exec(key.slice(0, close + 1))![1]!;
  return `${doc}.${key.slice(close + 2)}`;
}

/** The lines that read `id`, directly or through other lines (operands, refusal gates, display conditions, def
 * results read by an instance), and `id` itself. */
function downstreamOf(data: CanonicalData, id: string): Set<string> {
  const out = new Set([id]);
  const queue = [id];
  while (queue.length > 0) for (const r of allReaders(data, queue.pop()!)) if (!out.has(r)) { out.add(r); queue.push(r); }
  return out;
}

function mentionsDef(n: unknown, def: string): boolean {
  if (Array.isArray(n)) return n.some((x) => mentionsDef(x, def));
  if (n === null || typeof n !== "object") return false;
  return (n as Record<string, unknown>)["def"] === def || Object.values(n).some((x) => mentionsDef(x, def));
}

/** The lines outside every def through which a line of `doc` is read: the line itself, or, for a def's line, the
 * lines that read an instance of the def (and so on, for a def read inside another def). */
function liftedLines(data: CanonicalData, doc: FormDoc, id: string, seen: Set<string> = new Set()): string[] {
  if (doc.kind !== "def") return [id];
  if (seen.has(doc.id)) return [];
  seen.add(doc.id);
  return allDocs(data).flatMap((d) => d.lines.filter((l) => mentionsDef(l.expr, doc.id)).flatMap((l) => liftedLines(data, d, l.id, seen)));
}

/** Where a mutant changes the data: a line (`line:<doc>.<line id>`), a parameter (`param:<name>`) or a rate table
 * (`table:<id>`). */
function siteOf(m: Mutation): string {
  return m.id.startsWith("param.") ? `param:${m.where}` : m.id.startsWith("table.") ? `table:${m.where}` : `line:${m.where}`;
}

/** The lines outside every def that a mutant of the site can change first (`watch`), and the line a keyed argument
 * may let differ, the mutated line itself (`exclude`, only for a mutated line outside every def). */
function siteLines(data: CanonicalData, site: string): { watch: string[]; exclude: Set<string> } {
  const kind = site.slice(0, site.indexOf(":"));
  const name = site.slice(kind.length + 1);
  if (kind === "line") {
    const doc = allDocs(data).find((d) => d.id === name.slice(0, name.indexOf(".")))!;
    const id = name.slice(doc.id.length + 1);
    return { watch: liftedLines(data, doc, id), exclude: new Set(doc.kind === "def" ? [] : [id]) };
  }
  const readers = kind === "param"
    ? paramReaders(data, name)
    : allDocs(data).flatMap((scope) => scope.lines.filter((l) => (l.expr as { table?: string }).table === name).map((line) => ({ scope, line })));
  return { watch: [...new Set(readers.flatMap((r) => liftedLines(data, r.scope, r.line.id)))], exclude: new Set() };
}

/** What the sample showed about one mutant: the first set on which a line on a value sheet that the mutant can
 * change differs (the claim of equivalence is contradicted); how many sets exercised it (a value it can change
 * differs); and, for the self-test and for an argument over answered inputs only, what is described below. */
type SampledResult = { contradicted?: string; exercised: number; reached: number; sets: number; closureMiss?: string; partial?: string };

function valuesOf(data: CanonicalData, inputs: Record<string, unknown>, targets: string[]): Map<string, string> {
  const out = new Map<string, string>();
  for (const [k, d] of evaluate(data, inputs, targets).derivations) out.set(k, normal(d.value));
  return out;
}

/** A normalized value on one line, cut short: a refusal carries its whole citation. */
function brief(v: string): string {
  const flat = v.replace(/\s+/g, " ");
  return flat.length > 160 ? `${flat.slice(0, 160)}...` : flat;
}

/** A value exactly as a reader receives it, an unknown's details and its mark of a pending refusal gate included. */
function exactly(v: Record<string | symbol, unknown>): string {
  return `${JSON.stringify(v)}|${v[GATE_PENDING] === true}`;
}

/** The sampled check of the mutants `muts` (all of one site), each held to the sets given, or to the sets as given
 * where `answeredOnly` has its id. A line's readers receive only its value, so where every line the site can change
 * first (each entry of it) has exactly the same value under the mutant as under the data, nothing that reads them
 * can differ, and their readers are evaluated only on the other sets. Where `full` is set (the self-test), every
 * line of the return is evaluated and compared rather than the readers, and a line that differs outside the readers
 * is reported as `closureMiss`. */
function sampleSite(baseline: CanonicalData, site: string, muts: Mutation[], sets: SampleSet[], answeredOnly: Set<string>, full = false): Map<string, SampledResult> {
  const { watch, exclude } = siteLines(baseline, site);
  const watched = new Set(watch);
  const closure = new Set(watch.flatMap((w) => [...downstreamOf(baseline, w)]));
  const mutantData = muts.map((m) => { const d = cloneData(baseline); m.apply(d); return d; });
  const results = new Map(muts.map((m) => [m.id, { exercised: 0, reached: 0, sets: 0 } as SampledResult]));
  const refs = (d: { operands: { ref: string }[] }): string => d.operands.map((o) => o.ref).join("\n");
  for (const set of sets) {
    const every = allTargets(baseline, set.inputs);
    const own = every.filter((k) => watched.has(lineOfKey(k)));
    if (own.length === 0) continue;
    const ownBase = evaluate(baseline, set.inputs, own).derivations;
    let targets: string[] | undefined;
    let base: Map<string, string> | undefined;
    muts.forEach((m, i) => {
      const r = results.get(m.id)!;
      // An argument over answered inputs only is held to the answered returns; on the partial sets the first set
      // telling the mutant apart is kept as a witness of the partial return the argument excludes.
      const partial = set.partial && answeredOnly.has(m.id);
      if (partial ? r.partial !== undefined : !full && r.contradicted !== undefined) return;
      if (!partial) r.sets++;
      const ownMutant = evaluate(mutantData[i]!, set.inputs, own).derivations;
      let infected = false;
      let exact = ownMutant.size === ownBase.size;
      let reached = !exact;
      for (const [k, d] of ownMutant) {
        const b = ownBase.get(k);
        if (b === undefined) { exact = false; infected = true; continue; }
        // The mutant reached its change where a line it can change first read other operands than under the data.
        if (refs(b) !== refs(d)) reached = true;
        if (exactly(b.value as never) === exactly(d.value as never)) continue;
        exact = false;
        if (normal(b.value) !== normal(d.value)) infected = true;
      }
      if ((reached || !exact) && !partial) r.reached++;
      if (exact) return;
      targets ??= full ? every : every.filter((k) => closure.has(lineOfKey(k)));
      base ??= valuesOf(baseline, set.inputs, targets);
      const mutant = valuesOf(mutantData[i]!, set.inputs, targets);
      for (const [k, v] of mutant) {
        const b = base.get(k);
        if (b === v) continue;
        infected = true;
        const id = lineOfKey(k);
        // A def's lines are seen only through the lines that read its instances, which are compared; a helper is on
        // no value sheet and is seen only through the lines that read it; the mutated line may differ.
        if (b === undefined || k.includes("|inst:") || exclude.has(id) || isHelper(baseline, id)) continue;
        if (partial) { r.partial = `${set.label}, ${set.rate > 0 ? `answers withheld at rate ${set.rate}` : "as given, a partial return"}: ${k} is ${brief(b)} with the data and ${brief(v)} with the mutant`; return; }
        r.contradicted ??= `${set.label}, answers withheld at rate ${set.rate}: ${k} is ${brief(b)} with the data and ${brief(v)} with the mutant`;
        if (!full) return;
        if (!closure.has(id)) r.closureMiss ??= `${set.label}, rate ${set.rate}: ${k} differs and is not a reader of ${watch.join(", ")} by the closure`;
      }
      if (r.contradicted !== undefined || partial) return;
      if (infected) r.exercised++;
    });
  }
  return results;
}

/** The sampled check's work: each keyed argument that explains a survivor this run, grouped by site, and one control
 * per site, a mutant of the same site that a fixture kills (so it is not equivalent). */
export type SampledPlan = { site: string; claimed: string[]; controls: string[] }[];

export function sampledPlan(baseline: CanonicalData, muts: Mutation[], survivors: Set<string>, fixtureKilled: Set<string>): SampledPlan {
  const bySite = new Map<string, { claimed: string[]; controls: string[] }>();
  for (const m of muts) {
    const c = EQUIVALENT_IF[m.id];
    if (!c || !survivors.has(m.id) || (c.reads !== undefined && c.reads !== m.replacement) || !c.holds(baseline)) continue;
    const entry = bySite.get(siteOf(m)) ?? { claimed: [], controls: [] };
    entry.claimed.push(m.id);
    bySite.set(siteOf(m), entry);
  }
  for (const m of muts) {
    const entry = bySite.get(siteOf(m));
    if (entry && entry.controls.length === 0 && fixtureKilled.has(m.id)) entry.controls.push(m.id);
  }
  return [...bySite].map(([site, e]) => ({ site, ...e }));
}

/** The sampled check of a share of the plan (every `count`-th site from `index`), for the workers. */
export function sampledShare(index: number, count: number, plan: SampledPlan, partial: string[]): [string, SampledResult][] {
  const baseline = loadCanonical();
  const sets = sampleSets(baseline, judgingCases(baseline), new Set(partial));
  const byId = new Map(selectMutants(mutations(baseline)).map((m) => [m.id, m]));
  const out: [string, SampledResult][] = [];
  for (let i = index; i < plan.length; i += count) {
    const p = plan[i]!;
    const ms = [...p.claimed, ...p.controls].map((id) => byId.get(id)!);
    const started = Date.now();
    const results = sampleSite(baseline, p.site, ms, sets, ANSWERED_ONLY);
    // Self-test of the restriction to the readers: the controls again, every line of each return compared, on the
    // first CLOSURE_TEST_SETS sets; a line outside the readers that differs is reported.
    const whole = sampleSite(baseline, p.site, p.controls.map((id) => byId.get(id)!), sets.slice(0, CLOSURE_TEST_SETS), new Set(), true);
    for (const [id, r] of whole) if (r.closureMiss) results.get(id)!.closureMiss = r.closureMiss;
    if (process.env.MUTATE_SAMPLE_TIMES) console.error(`sampled check: ${p.site}: ${Date.now() - started} ms`);
    out.push(...results);
  }
  return out;
}
const CLOSURE_TEST_SETS = 200;

async function sampledResults(baseline: CanonicalData, plan: SampledPlan, partial: string[]): Promise<Map<string, SampledResult>> {
  const count = Math.min(workerCount(), Math.max(1, plan.length));
  if (count === 1) return new Map(sampledShare(0, 1, plan, partial));
  const shares = await Promise.all(Array.from({ length: count }, (_, index) => new Promise<[string, SampledResult][]>((done, fail) => {
    const w = new Worker(new URL("./mutate-worker.js", import.meta.url), { workerData: { year: YEAR, index, count, ny: NY_MODE, plan, partial } });
    w.once("message", done);
    w.once("error", fail);
    w.once("exit", (code) => { if (code !== 0) fail(new Error(`sampled-check worker ${index} exited with ${code}`)); });
  })));
  return new Map(shares.flat());
}

/** Self-test of isPartialReturn: a return with no answers is partial; some fixture case is an answered return (else
 * every argument over answered inputs only would be held to no set); and withholding one of its answers makes it
 * partial. */
export function partialReturnSelfTest(baseline: CanonicalData, cases: JudgingCases, partial: string[]): string[] {
  const config = loadInterview(NY_MODE ? "ny" : "full");
  const problems: string[] = [];
  if (!isPartialReturn(baseline, config, {})) problems.push("partial returns: a return with no answers is not found partial");
  const marked = new Set(partial);
  const answered = cases.all.find((c) => !marked.has(`fixture case ${c.id}`));
  if (answered === undefined) problems.push("partial returns: every fixture case is partial, so no answered return backs an argument over answered inputs only");
  else {
    // Withholding one answer of an answered return must make it partial for some answer (the first 40 tried).
    const keys = Object.keys(answered.inputs).filter((k) => !k.startsWith("$")).sort().slice(0, 40);
    const without = (k: string): Record<string, unknown> => Object.fromEntries(Object.entries(answered.inputs).filter(([key]) => key !== k));
    if (!keys.some((k) => isPartialReturn(baseline, config, without(k))))
      problems.push(`partial returns: ${answered.id} stays an answered return with any one of ${keys.length} answers withheld`);
  }
  return problems;
}

export async function runMutation(): Promise<number> {
  const baseline = loadCanonical();
  const fixtureFile = judgingCases(baseline);

  // A mismatching baseline must never make every mutant look killed.
  const baselineErrors = runChecks(baseline).errors;
  if (baselineErrors.length > 0) {
    // Every mutant would then be "killed by checker" and the score a vacuous 100% (T-225).
    throw new Error(`mutation baseline has ${baselineErrors.length} check error(s); fix them first: ${baselineErrors.slice(0, 3).join("; ")}`);
  }
  for (const c of fixtureFile.all) {
    const result=evaluate(baseline,c.inputs,c.targets ?? allTargets(baseline,c.inputs));
    for (const [key,expected] of Object.entries(c.expect ?? {})) {
      const actual=result.derivations.get(key)?.value;
      if (!actual || normal(actual)!==normal(expected)) throw new Error(`mutation baseline mismatch: ${c.id} ${key}`);
    }
  }
  const muts = selectMutants(mutations(baseline));
  const retarget = retargetSelfTest(baseline, muts);
  const survivors: Mutation[] = [];
  const classmOnly: { m: Mutation; case: string }[] = [];
  let killedByCheck = 0;
  let killedByFixtures = 0;

  const outcomes = await outcomesOf(baseline, fixtureFile, muts);
  muts.forEach((m, i) => {
    if (outcomes[i] === "check") killedByCheck++;
    else if (outcomes[i] === "fixtures") killedByFixtures++;
    else if (outcomes[i]!.startsWith("classm:")) { killedByFixtures++; classmOnly.push({ m, case: outcomes[i]!.slice("classm:".length) }); }
    else survivors.push(m);
  });

  const total = muts.length;
  const killed = killedByCheck + killedByFixtures;
  const score = total === 0 ? 0 : killed / total;
  for(const survivor of survivors) {
    const reason=equivalenceReason(baseline,survivor);
    if(reason)EQUIVALENT[survivor.id]=reason;
  }
  const equivalentSurvivors = survivors.filter((s) => s.id in EQUIVALENT);
  const answeredOnly = equivalentSurvivors.filter((s) => ANSWERED_ONLY.has(s.id) && EQUIVALENT_IF[s.id] !== undefined && EQUIVALENT[s.id] === equivalenceReason(baseline, s));
  const everyInput = equivalentSurvivors.filter((s) => !answeredOnly.includes(s));
  // ---- lane mstruct begin ----
  const unobservedSurvivors = everyInput.filter((s) => EQUIVALENT[s.id]!.startsWith("Unobserved line: "));
  const unobservedEnds = new Map<string, number>();
  for (const s of unobservedSurvivors) {
    const dot = s.where.indexOf(".");
    for (const e of unobservedChain(baseline, s.where.slice(0, dot), s.where.slice(dot + 1), productNames())?.ends ?? []) unobservedEnds.set(e, (unobservedEnds.get(e) ?? 0) + 1);
  }
  const unobservedProblems = unobservedLineSelfTest();
  // ---- lane mstruct end ----
  const openDefect = survivors.filter((s) => !(s.id in EQUIVALENT) && s.id in OPEN_DEFECT_SURVIVORS);
  const unexplained = survivors.filter((s) => !(s.id in EQUIVALENT) && !(s.id in OPEN_DEFECT_SURVIVORS));
  const inventory = readFileSync(join(ROOT, "BUG_INVENTORY.md"), "utf8");
  const openDefectProblems = Object.entries(OPEN_DEFECT_SURVIVORS).flatMap(([id, bug]) => [
    ...(survivors.some((s) => s.id === id) ? [] : [`${id}: listed for ${bug} but no longer survives; remove the entry`]),
    ...(new RegExp(`^## ${bug} — .*\\(open\\)$`, "m").test(inventory) ? [] : [`${id}: ${bug} is not an open entry in BUG_INVENTORY.md`]),
  ]);
  const survivorIds = new Set(survivors.map((s) => s.id));
  const staleArguments = staleEquivalences(EQUIVALENT_IF, ANSWERED_ONLY, baseline, muts, survivorIds);
  const staleTest = staleEquivalenceSelfTest(baseline, muts, survivorIds);
  const fixtureKilled = new Set(muts.filter((_, i) => outcomes[i] === "fixtures" || outcomes[i]!.startsWith("classm:")).map((m) => m.id));
  const plan = sampledPlan(baseline, muts, survivorIds, fixtureKilled);
  // Only an argument over answered inputs only reads which sets as given are partial returns.
  const partial = plan.some((p) => p.claimed.some((id) => ANSWERED_ONLY.has(id))) ? partialLabels(baseline, fixtureFile) : [];
  const sampled = await sampledResults(baseline, plan, partial);
  const sampledProblems: string[] = [];
  const sampledRows: string[] = [];
  let controlsTried = 0, controlsRejected = 0;
  const powerGaps: string[] = [];
  for (const p of plan) {
    for (const id of p.claimed) {
      const r = sampled.get(id)!;
      const mode = ANSWERED_ONLY.has(id) ? "answered returns" : "all sets";
      sampledRows.push(`| ${id} | ${mode} | ${r.sets} | ${r.reached} | ${r.exercised} | ${r.contradicted === undefined ? "holds" : "CONTRADICTED"}${r.reached === 0 && r.exercised === 0 && UNEXERCISED_IF[id] ? `; not reachable by a sample: ${UNEXERCISED_IF[id]!.reason}` : ""}${r.partial ? `; on a partial return: ${r.partial}` : ""} |`);
      if (r.contradicted !== undefined) sampledProblems.push(`${id}: the sample contradicts the argument: ${r.contradicted}`);
      else if (r.reached === 0 && r.exercised === 0 && !UNEXERCISED_IF[id]?.holds(baseline)) sampledProblems.push(`${id}: no sampled set reaches the mutant's change, so the sample does not back the argument; add a fixture case that reaches it or state the reason in UNEXERCISED_IF`);
    }
    for (const id of p.controls) {
      controlsTried++;
      const miss = sampled.get(id)!.closureMiss;
      if (miss) sampledProblems.push(`${id}: the readers the sampled check compares miss a line that the mutant changes: ${miss}`);
      if (sampled.get(id)!.contradicted !== undefined) controlsRejected++;
      else powerGaps.push(`${id} (${p.site})`);
    }
  }
  if (partial.length > 0) sampledProblems.push(...partialReturnSelfTest(baseline, fixtureFile, partial));
  if (plan.length > 0 && controlsTried === 0) sampledProblems.push("sampled check: no line of a keyed argument has a fixture-killed mutant to serve as a control");
  if (controlsTried > 0 && controlsRejected === 0) sampledProblems.push(`sampled check: none of the ${controlsTried} known-killed controls was rejected, so the check has shown no power`);
  const adjusted = total - equivalentSurvivors.length === 0 ? 1 : killed / (total - equivalentSurvivors.length);
  const adjustedEvery = total - everyInput.length === 0 ? 1 : killed / (total - everyInput.length);

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
  report.push(`| Killed by fixtures | ${killedByFixtures} (${classmOnly.length} only by class M cases) |`);
  report.push(`| Surviving | ${survivors.length} (${everyInput.length} provably equivalent on every input; ${answeredOnly.length} equivalent on answered inputs only) |`);
  report.push(`| Surviving on unobserved lines (among the provably equivalent) | ${unobservedSurvivors.length} |`);
  report.push(`| Mutation score (raw) | ${(score * 100).toFixed(1)}% |`);
  report.push(`| Mutation score (mutants provably equivalent on every input excluded) | ${(adjustedEvery * 100).toFixed(1)}% |`);
  report.push(`| Mutation score (also excluding those equivalent on answered inputs only) | ${(adjusted * 100).toFixed(1)}% |`);
  report.push("");
  if (classmOnly.length > 0) {
    report.push("## Killed only by class M cases");
    report.push("");
    report.push("A class M rerun regenerates its cases, so these kills can be lost. Before replacing a case named here,");
    report.push("keep it (or a stage fixture with the same facts and source-predicted values) among the stage fixtures.");
    report.push("");
    report.push("| Mutant | Kind | Location | First class M case killing it |");
    report.push("| --- | --- | --- | --- |");
    for (const { m, case: id } of classmOnly) report.push(`| ${m.id} | ${m.kind} | ${m.where} | ${id} |`);
    report.push("");
  }
  if (answeredOnly.length > 0) {
    report.push("## Surviving — equivalent on answered inputs only");
    report.push("");
    report.push("Each argument below is proven only on returns where the answers it names are given; with them withheld a");
    report.push("partial return can tell the mutant apart (spec 4.7.3). They are not counted as provably equivalent on every input.");
    report.push("");
    for (const s of answeredOnly) report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${EQUIVALENT[s.id]}`);
    report.push("");
  }
  if (everyInput.length > 0) {
    report.push("## Surviving — classified equivalent");
    report.push("");
    for (const s of everyInput) {
      if (unobservedSurvivors.includes(s)) continue;
      report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${EQUIVALENT[s.id]}`);
    }
    report.push("");
  }
  // ---- lane mstruct begin ----
  if (unobservedSurvivors.length > 0 || unobservedProblems.length > 0) {
    report.push("## Surviving — on unobserved lines");
    report.push("");
    report.push(`${unobservedSurvivors.length} surviving mutants change a helper that only helpers read, transitively, ending in helpers that nothing reads:`);
    report.push("no printed line, refusal gate, display condition, definition, interview target, interview file or product code reads or names");
    report.push("the chain, so the mutant can change only those helpers' own values. Checked against the data on every run; the rule lapses for");
    report.push("a chain as soon as something observed reads it. Counted among the provably equivalent above.");
    report.push("");
    for (const s of unobservedSurvivors) report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${EQUIVALENT[s.id]}`);
    report.push("");
    report.push("The ends of these chains, read by nothing (cleanup candidates), with the number of surviving mutants resting on each:");
    report.push("");
    for (const [e, n] of [...unobservedEnds].sort((a, b) => a[0] < b[0] ? -1 : 1)) report.push(`- ${e}: ${n}`);
    for (const p of unobservedProblems) report.push(`- PROBLEM (self-test): ${p}`);
    report.push("");
  }
  // ---- lane mstruct end ----
  if (retarget.problems.length > 0) {
    report.push("## Pinned-argument self-test");
    report.push("");
    for (const p of retarget.problems) report.push(`- PROBLEM: ${p}`);
    report.push("");
  }
  if (plan.length > 0) {
    report.push("## Keyed arguments, checked on a sample");
    report.push("");
    report.push(`Each keyed argument above is also checked by execution: the mutant and the data are evaluated on ${SAMPLED_RETURNS} generated`);
    report.push(`returns and the inputs of every fixture case, each as given and with answers withheld at rates ${SAMPLED_RATES.slice(1).join(", ")};`);
    report.push("every line on a value sheet that reads the mutated line must agree. A set reaches the mutant where the line it changes reads other");
    report.push("operands or has another value than under the data, and exercises it where a value it can change differs.");
    report.push("An argument over answered inputs only is held to the sets as given.");
    report.push(`Known-killed controls (one fixture-killed mutant per line): ${controlsRejected} of ${controlsTried} rejected by the same check.`);
    report.push("");
    report.push("| Argument | Held to | Sets | Reaching it | Exercising it | Result |");
    report.push("| --- | --- | --- | --- | --- | --- |");
    report.push(...sampledRows);
    report.push("");
    for (const p of sampledProblems) report.push(`- PROBLEM: ${p}`);
    if (powerGaps.length > 0) report.push(`- Controls the sample did not reject (its readers never differ on these sets; the kill is on the line itself or rests on a fixture's own answers): ${powerGaps.join(", ")}`);
    report.push("");
  }
  if (staleArguments.length > 0) {
    report.push("## Stale equivalence arguments");
    report.push("");
    report.push("Keyed arguments that no longer explain a surviving mutant (the run fails until each is removed or rewritten):");
    report.push("");
    for (const p of staleArguments) report.push(`- PROBLEM: ${p}`);
    report.push("");
  }
  if (openDefect.length > 0 || openDefectProblems.length > 0) {
    report.push("## Surviving — explained by an open defect");
    report.push("");
    for (const s of openDefect) report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${OPEN_DEFECT_SURVIVORS[s.id]}`);
    for (const p of openDefectProblems) report.push(`- PROBLEM: ${p}`);
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
  const outDir = reportPath();
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "mutation.md"), report.join("\n"));
  console.log(`mutation: ${total} mutants, killed by checker ${killedByCheck}, by fixtures ${killedByFixtures} (${classmOnly.length} only by class M cases), surviving ${survivors.length} (${everyInput.length} equivalent on every input, ${answeredOnly.length} on answered inputs only; score ${(score * 100).toFixed(1)}%, adjusted ${(adjustedEvery * 100).toFixed(1)}% on every input, ${(adjusted * 100).toFixed(1)}% with answered-only)`);
  console.log(`report: ${reportName("mutation.md")}`);
  for (const p of openDefectProblems) console.log(`mutation: ${p}`);
  console.log(`mutation: retargeting self-test: ${retarget.tested} pinned arguments retargeted and rejected, ${retarget.problems.length} problems`);
  for (const p of retarget.problems) console.log(`mutation: ${p}`);
  const wholeProblems = wholeParamSelfTest();
  console.log(`mutation: whole-dollar parameter self-test: ${wholeProblems.length} problems`);
  for (const p of wholeProblems) console.log(`mutation: ${p}`);
  const guardProblems = unknownGuardSelfTest();
  console.log(`mutation: unknown-guard side-condition self-test: ${guardProblems.length} problems`);
  for (const p of guardProblems) console.log(`mutation: ${p}`);
  const figureProblems = guardedFigureSelfTest();
  console.log(`mutation: guarded-figure dominance self-test: ${figureProblems.length} problems`);
  for (const p of figureProblems) console.log(`mutation: ${p}`);
  const digestTest = premiseDigestSelfTest(baseline);
  console.log(`mutation: premise-digest self-test: ${digestTest.tested} edits checked, ${digestTest.problems.length} problems`);
  for (const p of digestTest.problems) console.log(`mutation: ${p}`);
  console.log(`mutation: unobserved-line rule: ${unobservedSurvivors.length} survivors on unobserved lines; self-test ${unobservedProblems.length} problems`);
  for (const p of unobservedProblems) console.log(`mutation: unobserved-line self-test: ${p}`);
  const chooseProblems = scalarChooseSelfTest();
  console.log(`mutation: Bool and enum choose reasoning self-test: ${chooseProblems.length} problems`);
  for (const p of chooseProblems) console.log(`mutation: ${p}`);
  console.log(`mutation: ${staleArguments.length} stale equivalence arguments`);
  for (const p of staleArguments) console.log(`mutation: stale argument: ${p}`);
  console.log(`mutation: stale-argument self-test: ${staleTest.planted} planted stale arguments, ${staleTest.problems.length} problems`);
  for (const p of staleTest.problems) console.log(`mutation: ${p}`);
  console.log(`mutation: sampled check: ${plan.reduce((n, p) => n + p.claimed.length, 0)} keyed arguments on ${plan.length} lines, ${SAMPLED_RETURNS} generated returns and ${fixtureFile.all.length} fixture cases at ${SAMPLED_RATES.length} withholding rates (${partial.length} sets as given are partial returns); known-killed controls rejected ${controlsRejected} of ${controlsTried}; ${sampledProblems.length} problems`);
  for (const p of sampledProblems) console.log(`mutation: sampled check: ${p}`);
  return sampledProblems.length === 0 && staleArguments.length === 0 && staleTest.problems.length === 0 && unexplained.length === 0 && openDefectProblems.length === 0 && retarget.problems.length === 0 && wholeProblems.length === 0 && guardProblems.length === 0 && figureProblems.length === 0 && digestTest.problems.length === 0 && chooseProblems.length === 0 && unobservedProblems.length === 0 ? 0 : 1;
}
