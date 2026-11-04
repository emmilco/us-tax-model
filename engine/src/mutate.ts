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

type OperandSite = { ref: string; kind: string; path: (string | number)[]; wantType: string | undefined; tier: number };
// Every operand position is a site: keyed_lookup keys, rate_lookup and table_lookup key and status
// included. Sites of tier 2 and above (choose branch values, string operands of test expressions)
// are mutated up to the tier named by MUTATE_TIER (default 0).
const SITE_TIER = Number(process.env.MUTATE_TIER ?? 0) || 0;

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
    case "table_lookup": case "bracket_schedule":
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

      if (expr.op === "sum_over" && expr.where) out.push({id:`filter.${where}`,kind:"remove collection filter",where,apply:d=>{const e=findLine(d,line.id)!.expr; if(e.op==="sum_over") delete e.where;}});
      for (let i=0;i<(line.refuses?.length??0);i++) out.push({id:`refusal.${where}.${i}`,kind:"remove refusal",where,apply:d=>{findLine(d,line.id)!.refuses!.splice(i,1);}});
      for (let i=0;i<(line.refuses?.length??0);i++) if (line.refuses![i]!.when_known) out.push({id:`consistency.${where}.${i}`,kind:"require unanswered consistency check",where,apply:d=>{delete findLine(d,line.id)!.refuses![i]!.when_known;}});
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
          apply: (d) => {
            replaceAtPath(findLine(d, line.id)!.expr, site.path, candidate.id);
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

// The facts a reader adds to a path: when a choose takes the line only as the value of some
// alternatives (never in a guard), the disjunction of those alternatives' guards holds wherever it
// reads the line. Readers through a refusal gate or a display condition add nothing.
type ReaderStep = { reader: Line; doc: FormDoc; fact: unknown[] | undefined };
const readerIndexes = new WeakMap<CanonicalData, Map<string, ReaderStep[]>>();

function readerSteps(data: CanonicalData, id: string): ReaderStep[] {
  let index = readerIndexes.get(data);
  if (!index) {
    index = new Map();
    for (const doc of allDocs(data)) for (const l of doc.lines) {
      const expr = new Set(operandRefs(data, l.expr));
      const gates = new Set([...(l.refuses ?? []).map((r) => r.when), ...(l.shown_when ? [l.shown_when] : [])]);
      const alts = l.expr.op === "choose" ? (l.expr.alternatives as { guard: unknown; then: unknown }[]).map((a) => ({ guard: a.guard, inGuard: new Set(operandRefs(data, a.guard)), inThen: new Set(operandRefs(data, a.then)) })) : undefined;
      for (const read of new Set([...expr, ...gates])) {
        let fact: unknown[] | undefined;
        if (!gates.has(read) && alts) {
          const taking = alts.filter((a) => a.inThen.has(read));
          if (!alts.some((a) => a.inGuard.has(read)) && taking.length) fact = taking.map((a) => a.guard);
        }
        const list = index.get(read) ?? [];
        list.push({ reader: l, doc, fact });
        index.set(read, list);
      }
    }
    readerIndexes.set(data, index);
  }
  return index.get(id) ?? [];
}

// Whether test g, known true, makes test c true: the same test; eq(x, v) against ne(x, w) with
// constants v and w different; a conjunct of an all-test; or eq(G, true) for an ungated test line G
// whose own test does.
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
  }
  return false;
}

// Whether the facts on a path make the Bool line `flag` true: some fact implies flag == true, or
// flag is an ungated all-test (or single comparison) each of whose conjuncts some fact implies.
function flagHolds(data: CanonicalData, facts: unknown[][], flag: string): boolean {
  const implied = (c: unknown): boolean => facts.some((fact) => fact.every((g) => testImplies(data, g, c)));
  if (implied({ op: "test", eq: [flag, { const: true }] })) return true;
  const f = findLine(data, flag);
  if (!f || (f.refuses ?? []).length || f.expr.op !== "test") return false;
  const conjuncts = Array.isArray((f.expr as { all?: unknown[] }).all) ? (f.expr as { all: unknown[] }).all : [f.expr];
  return conjuncts.length > 0 && conjuncts.every(implied);
}

// Path dominance: every chain of readers from `start` to a printed line (or to a refusal gate or
// display condition) passes through choose alternatives whose guards, taken together, make `flag`
// true. Guards count only on readers in start's own document (one frame); readers elsewhere carry
// the facts already gathered. Then a value read from start by any printed line is read only where
// flag holds (spec 4.7.3: a choose does not evaluate an alternative it does not take).
function dominatedBy(data: CanonicalData, start: string, flag: string): boolean {
  const home = docOfLine(data, start);
  if (!home || home.kind === "def") return false;
  const seen = new Set<string>();
  const stack: { id: string; facts: unknown[][] }[] = [{ id: start, facts: [] }];
  let steps = 0;
  while (stack.length) {
    const { id, facts } = stack.pop()!;
    for (const { reader, doc, fact } of readerSteps(data, id)) {
      const next = fact && doc.id === home.id ? [...facts, fact] : facts;
      if (flagHolds(data, next, flag)) continue;
      if (reader.printed !== "(helper)") return false;
      const key = `${reader.id}|${stableStringify(next)}`;
      if (seen.has(key)) continue;
      seen.add(key);
      if (++steps > 5000) return false;
      stack.push({ id: reader.id, facts: next });
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
    if (!dominatedBy(data, line, g.flag)) continue;
    return `Guarded figure: ${gated} is ${figure} wherever ${g.flag} holds, and every printed line reads ${line} (a helper) only through choices whose guards make ${g.flag} true, so the replacement changes no printed value; where ${g.flag} does not hold only ${line}'s own, unprinted value can differ.`;
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
  return `Branch settled by its guard: where ${lineOf(mutation)} takes alternative ${m[1]} (guard ${stableStringify(alt.guard)}), the lines that guard compares are complete and fix the choices that ${pair[0]} and ${pair[1]} make, and both reduce to ${a === "ZERO" ? "the zero" : "the same value"} (through settled choices, copies${a === "ZERO" ? " and arithmetic of zeros" : ""}, with refusal gates only among the line's own, already false), so the mutated line is unchanged at every input.`;
}

// Unreachable alternative: the mutated line is a helper, and every printed line reads it only through
// choices whose guards make some ungated test line F true (path dominance, as for a guarded figure);
// F true settles the replaced alternative's guard false, so wherever a printed value depends on the
// helper that alternative is not taken, and its value is never read there.
function unreachableAlternative(data: CanonicalData, mutation: Mutation): string | undefined {
  const pair = replacedPair(mutation); if (!pair) return undefined;
  const m = /\.then(\d+)$/.exec(mutation.id); if (!m) return undefined;
  const id = lineOf(mutation), line = findLine(data, id), doc = docOfLine(data, id);
  if (!line || !doc || line.expr.op !== "choose" || !isHelper(data, id)) return undefined;
  const alt = (line.expr.alternatives as { guard: unknown; then: unknown }[])[Number(m[1])];
  if (!alt || alt.then !== pair[0]) return undefined;
  for (const f of doc.lines) {
    if (f.type !== "Bool" || f.expr.op !== "test" || (f.refuses ?? []).length) continue;
    if (decides(alt.guard, guardFacts(data, { op: "test", eq: [f.id, { const: true }] })) !== false) continue;
    if (!dominatedBy(data, id, f.id)) continue;
    return `Unreachable alternative: ${id} is a helper that every printed line reads only through choices whose guards make ${f.id} true, and ${f.id} true makes the guard of alternative ${m[1]} (${stableStringify(alt.guard)}) false; so wherever a printed value depends on ${id} that alternative is not taken, and replacing its value changes no printed value.`;
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
    for (const alt of e.alternatives as { guard: unknown; then: unknown }[]) {
      const g = absTest(data, alt.guard, env, depth + 1);
      if (typeof g === "object") return parts.length ? atom([...parts, { k: "inc", s: g.inc }]) : { k: "inc", s: g.inc };
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
  if (e.op === "table_lookup" || e.op === "bracket_schedule" || e.op === "rate_lookup") return atom([absOperand(data, e.key, env, depth + 1), e.status === undefined ? kn(null) : absOperand(data, e.status, env, depth + 1)]);
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

// The facts with split line s set to v: a test line's own test, true or false, adds what it establishes.
function factsWith(data: CanonicalData, facts: GuardFacts, s: string, v: unknown): GuardFacts {
  const l = findLine(data, s);
  if (typeof v !== "boolean" || l?.expr.op !== "test") return facts;
  const next: GuardFacts = { data, same: new Set(facts.same), known: new Map([...facts.known].map(([k, b]): [string, Bound] => [k, b.not ? { ...b, not: [...b.not] } : { ...b }])), rel: new Set(facts.rel ?? []) };
  addTest(next, l.expr, v, 0);
  return next;
}

// The guards that hold wherever a helper's value reaches a printed line: while the line has exactly one
// reader, in its own document, which takes it only as the value of one alternative, that alternative's
// guard, and then its reader's.
function pathGuards(data: CanonicalData, id: string, depth = 0): unknown[] {
  if (depth > 8 || !isHelper(data, id)) return [];
  const steps = readerSteps(data, id);
  if (steps.length !== 1) return [];
  const s = steps[0]!;
  if (!s.fact || !s.fact.length || s.doc.id !== docOfLine(data, id)?.id) return [];
  if (s.fact.length === 1) return [s.fact[0], ...pathGuards(data, s.reader.id, depth + 1)];
  // Several alternatives that each test one enum line against a value: the line is complete and has
  // none of the other values.
  const eqs = s.fact.map((g) => comparison(data, g));
  const enumLine = eqs[0]?.line, ty = enumLine ? findLine(data, enumLine)?.type ?? "" : "";
  if (!enumLine || !ty.startsWith("Enum(") || !eqs.every((c) => c?.key === "eq" && c.line === enumLine && typeof c.v === "string")) return [];
  const taken = new Set(eqs.map((c) => c!.v as string));
  const others = (data.params.enums[ty.slice(5, -1)]?.values ?? []).filter((v) => !taken.has(v));
  if (!others.length) return [];
  return [{ op: "test", all: others.map((v) => ({ op: "test", ne: [enumLine, { const: v }] })) }, ...pathGuards(data, s.reader.id, depth + 1)];
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
  const path = pathGuards(data, id);
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

// The structural rules, checked against the current data for every survivor: the first that accepts
// it gives the reason.
export function structuralReason(data: CanonicalData, mutation: Mutation): string | undefined {
  return aliasEquivalence(data, mutation) ?? sharedGateEquivalence(data, mutation) ?? floorMinusMin(data, mutation)
    ?? carriedZero(data, mutation) ?? settledBranch(data, mutation) ?? unreachableAlternative(data, mutation) ?? caseSplitBranch(data, mutation) ?? guardedFigure(data, mutation) ?? unreadParameter(data, mutation) ?? unreadTable(data, mutation);
}

// Equivalences that need an argument about evaluation order or reachability. Each is
// accepted only while the structural facts it rests on hold in the current data; when
// they lapse, the mutant is reported as unexplained again.
const EQUIVALENT_IF: Record<string, { reason: string; holds: (data: CanonicalData) => boolean }> = {
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
  "refusal.f4952.f4952.required.1": {
    reason: "The removed refusal (the alternative-allocation gate, after the unsupported-items gate) is carried by f4952.election, the first operand f4952.required reads: election refuses on the same gates in the same order with the same records, and the any-test returns the first refusal it meets. With the gate No both routes evaluate the same expression; with it Yes both refuse on the same record (the unsupported-items gate first on both); with it unanswered, the unknown election is the first pending value on both, and line 3 reaches the same gate through line 2.",
    holds: (d) => {
      const req = findLine(d, "f4952.required"), el = findLine(d, "f4952.election");
      if (!req || !el || req.expr.op !== "test" || !("any" in req.expr)) return false;
      const gates = (l: typeof req) => (l.refuses ?? []).map((r) => r.when);
      if (stableStringify(gates(req)) !== stableStringify(["f4952.unsupported", "f4952.alternative_allocation"])) return false;
      if (stableStringify(gates(el).slice(0, 2)) !== stableStringify(gates(req))) return false;
      const strip = (r: unknown) => stableStringify(r);
      if (strip(req.refuses![0]) !== strip(el.refuses![0]) || strip(req.refuses![1]) !== strip(el.refuses![1])) return false;
      return operandRefs(d, req.expr)[0] === "f4952.election";
    },
  },
  "boundary.s1a.s1a.line10_over": s1aStepSkip("s1a.line10_over", "s1a.line8", "s1a.line9", "s1a.line10_pos", "s1a.line12", "s1a.line13_figured", "s1a.line7", "s1a.line13_amount"),
  "boundary.s1a.s1a.line18_over": s1aStepSkip("s1a.line18_over", "s1a.line16", "s1a.line17", "s1a.line18_pos", "s1a.line20", "s1a.line21_figured", "s1a.line15", "s1a.line21_amount"),
  "boundary.s1a.s1a.line27_over": s1aStepSkip("s1a.line27_over", "s1a.line25", "s1a.line26", "s1a.line27_pos", "s1a.line29", "s1a.line30_figured", "s1a.line24", "s1a.line30_amount"),
  "boundary.s1a.s1a.line33_over": s1aStepSkip("s1a.line33_over", "s1a.line31", "s1a.line32", "s1a.line33_pos", "s1a.line34", "s1a.line35_figured", "s1a.senior_amount", "s1a.line35_calc"),
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
  "operand.f8959.f8959.line18.line17": {
    reason: "Line 17 is 0.9% of line 16, and line 16 is line 14 less line 15 floored at zero, where line 14 is $0 behind its refusal gate and line 15 is not negative; so line 16 and line 17 are both $0, and when line 14 refuses or is unknown both carry its value (line 16 reads line 14 first, and the rate passes it through).",
    holds: (d) => {
      const l17 = exprOf(d, "f8959.line17"), l16 = exprOf(d, "f8959.line16"), l15 = findLine(d, "f8959.line15");
      return l17?.op === "multiply_rate" && l17.amount === "f8959.line16" && l16?.op === "subtract_floor0" && l16.from === "f8959.line14" && l16.take === "f8959.line15"
        && zeroBehindGates(d, "f8959.line14") && l15?.type === "NonNegDollars";
    },
  },
  "operand.f8960.f8960.line8.line5d": {
    reason: "Line 5d is line 5a plus lines 5b and 5c, which are $0 behind the refusal entries that line 1, the first operand of line 8, carries word for word. When an entry fires, line 1 refuses with it and line 8 returns that refusal on both routes; otherwise lines 5b and 5c are $0 and line 5d equals line 5a.",
    holds: (d) => {
      const l8 = exprOf(d, "f8960.line8"), l5d = exprOf(d, "f8960.line5d"), l1 = findLine(d, "f8960.line1");
      if (l8?.op !== "sum" || (l8.of as string[])[0] !== "f8960.line1" || l5d?.op !== "sum" || stableStringify(l5d.of) !== stableStringify(["f8960.line5a", "f8960.line5b", "f8960.line5c"]) || !l1?.refuses?.length) return false;
      return ["f8960.line5b", "f8960.line5c"].every((id) => zeroBehindGates(d, id) && stableStringify(findLine(d, id)?.refuses) === stableStringify(l1.refuses));
    },
  },
  "operand.f8960.f8960.line9d.line9c": {
    reason: "Line 9c and lines 4a and 4b (the operands of line 4c) are each $0 behind the same refusal entries, word for word; so line 4c, their sum, is $0 when no entry fires and otherwise carries the same refusal (or unknown) that line 9c does.",
    holds: (d) => {
      const l4c = exprOf(d, "f8960.line4c"); const n9c = stableStringify(normalizeChain(d, "f8960.line9c"));
      return l4c?.op === "sum" && stableStringify(l4c.of) === stableStringify(["f8960.line4a", "f8960.line4b"]) && zeroBehindGates(d, "f8960.line9c")
        && ["f8960.line4a", "f8960.line4b"].every((id) => stableStringify(normalizeChain(d, id)) === n9c);
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
  "operand.f8889.f8889.subject.line16.then0": pinned("f8889.subject is read only by line17b_figured, which only line17b reads, and only in its has_taxable alternative; has_taxable is line16 more than $0 (sales.zero), so where subject is read line16 is complete and positive, which only line16's has_dist alternative gives (the other is f8889.zero, $0), and that alternative's value is line16_figured. Where has_taxable is not true, subject is not read.",
    ["f8889.subject", "f8889.line17b_figured", "f8889.line17b", "f8889.has_taxable", "f8889.line16", "f8889.line16_figured", "f8889.has_dist", "f8889.zero", "param:sales.zero"], "9f3618649628f2ee"),
  "operand.f8889.f8889.self_dec_year.zero.then1": pinned("self_dec_year's self_only alternative is read (through self_in_family, step4_total, step4 and line6_split) only by line6, and only where split is true; with use_last_month true (which self_in_family requires to read self_dec_year) and December coverage self-only, married_family's inner any-test is false (its first disjunct needs December family coverage, its second needs use_last_month false), so married_family, an all-test, is false even past an unknown married answer (spec 4.7.2) or is the same refusal on both routes, and split is false: line6 reads line5, not line6_split.",
    ["f8889.self_dec_year", "f8889.self_in_family", "f8889.self_all", "f8889.step4_total", "f8889.step4", "f8889.line6_split", "f8889.line6", "f8889.split", "f8889.married_family", "f8889.use_last_month", "f8889.dec_coverage", "f8889.self_year", "f8889.zero"], "99917228415b46ec"),
  "operand.f8889.f8889.self_in_family.self_dec_year.then0": pinned("self_in_family's use_last_month alternative: use_last_month true means December coverage is known and not none. With family coverage self_dec_year and self_all are both self_year (self_all takes self_year under use_last_month), the same memoized value; with self-only coverage step4_total reaches line6 only through line6_split, which line6 reads only where split is true, and married_family (so split) is then false or the same refusal on both routes, as for self_dec_year's zero alternative.",
    ["f8889.self_dec_year", "f8889.self_in_family", "f8889.self_all", "f8889.step4_total", "f8889.step4", "f8889.line6_split", "f8889.line6", "f8889.split", "f8889.married_family", "f8889.use_last_month", "f8889.dec_coverage", "f8889.self_year", "f8889.zero"], "99917228415b46ec"),
  "operand.person.person.edu_adj.zero.then1": pinned("edu_adj's edu_student-false alternative: edu_student is then known false (memoized). edu_over_refused is an all-test whose first conjunct, edu_student true, decides it false before edu_adj is read; lines 27 to 30 read edu_adj only in the alternative guarded by edu_aoc and line 31 only in the one guarded by edu_llc, both all-tests whose first conjunct is edu_student true, so both are false and those alternatives (and their bindings) are not evaluated (spec 4.7.3, 4.7.4). edu_adj is a helper.",
    ["person.edu_adj", "person.edu_student", "person.edu_over_refused", "person.edu_aoc", "person.edu_llc", "person.edu_line27", "person.edu_line28", "person.edu_line29", "person.edu_line30", "person.edu_line31", "person.zero"], "0365cb37a26cdbc6"),
  "operand.dependent.dependent.edu_adj.zero.then1": pinned("dependent.edu_adj's edu_student-false alternative: as for person.edu_adj, edu_over_refused is decided false by its first conjunct, and lines 27 to 31 read edu_adj only in alternatives guarded by edu_aoc or edu_llc, all-tests whose first conjunct is edu_student true. edu_adj is a helper.",
    ["dependent.edu_adj", "dependent.edu_student", "dependent.edu_over_refused", "dependent.edu_aoc", "dependent.edu_llc", "dependent.edu_line27", "dependent.edu_line28", "dependent.edu_line29", "dependent.edu_line30", "dependent.edu_line31", "dependent.zero"], "6ffdbb346213cdd6"),
  "operand.sa.sa.deduction.standard.then1": pinned("sa.deduction's itemizes-false alternative: an any-test is known false only when every disjunct was evaluated and false with no unknown remembered (spec 4.7.2), so mfs_spouse_itemizes is known false and the comparison of line 17 with sa.standard read standard as a known value; a known standard passed its gates and took its mfs_spouse_itemizes-false alternative, whose value is standardraw, the same memoized value.",
    ["sa.standard", "sa.deduction", "sa.itemizes", "sa.standardraw", "sa.mfs_spouse_itemizes", "sa.extra_blind", "sa.elect_itemize"], "770a84bb7ca5b637"),
  "operand.sa.sa.standard.zero.then0": pinned("sa.standard's mfs_spouse_itemizes-true alternative: standard is a helper read only by sa.itemizes and sa.deduction. In itemizes the mfs_spouse_itemizes disjunct is true and decides the any-test before its last disjunct, the only one that reads standard (an earlier unknown is outranked by the deciding true; an earlier refusal ends the test before standard is read); so itemizes is not false, and deduction reads standard only where itemizes is false.",
    ["sa.standard", "sa.deduction", "sa.itemizes", "sa.standardraw", "sa.mfs_spouse_itemizes", "sa.extra_blind", "sa.elect_itemize"], "770a84bb7ca5b637"),
  "operand.sc.sc.qbi_se.zero.then1": pinned("sc.qbi_se's qbi_has-false alternative: qbi_has is profit_pos more than $0, so known false means profit_pos is a complete $0; then Form 7206 line 4 is $0, f7206_has is false, lines 7 and 9 are $0, lines 8, 10 and 13 are $0, and line 14 is $0 or (hi_uses true) the smaller of line 3 and $0, which is $0 when line 3 is complete and otherwise line 3's own refusal or unknown. qbi_se's only reader is qbi_ded, the sum of qbi_se, qbi_plan ($0 under the same qbi_has) and line 14: sum($0, $0, L14) and sum(L14, $0, L14) are the same value for L14 $0, the same refusal (it is the only refusing operand) or an unknown.",
    ["sc.qbi_se", "sc.qbi_has", "sc.qbi_ded", "sc.qbi_plan", "sc.f7206_line14", "sc.f7206_min", "sc.f7206_line13", "sc.f7206_line10", "sc.f7206_line9", "sc.f7206_line8", "sc.f7206_line7", "sc.f7206_has", "sc.f7206_line4", "sc.profit_pos", "sc.f7206_line3", "param:sales.zero"], "7c26af53292d6ba0"),
  "operand.sc.sc.ho_both.zero": pinned("sc.ho_both is a helper whose only reader is sc.ho_line5_lim, in its ho_no179-false alternative; ho_line5_lim is a helper whose only reader is sc.ho_line5, in its ho_unlimited-false alternative. A printed line therefore reads ho_both only after ho_unlimited and ho_no179 were found known false in the frame (spec 4.7.3, 4.7.6), and then ho_both's gate ho_both_limits, the all-test of those two being false, is true, so ho_both is its refusal at line entry and its expression, the only part the mutant changes, is not evaluated (4.7.1). With the gate false (ho_both or ho_line5_lim evaluated as a target) only those two helpers' own values differ.",
    ["sc.ho_both", "sc.ho_both_limits", "sc.ho_line5_lim", "sc.ho_line5", "sc.ho_unlimited", "sc.ho_no179", "sc.ho_pre179_floor", "sc.zero"], "652b707f3dad34e6"),
  "operand.eic.eic.credit.line6.then0": (() => {
    const lines = ["eic.credit", "eic.eligible", "eic.line6", "eic.after_line4", "eic.line4", "eic.line3", "eic.line1", "eic.line2", "eic.zero", "eic.line1_in_table", "eic.line1_table", "eic.line1_table0", "eic.line1_table1", "eic.line1_table2", "eic.line1_table3", "eic.line5", "eic.line3_table0", "eic.line3_table1", "eic.line3_table2", "eic.line3_table3", "eic.line5_blank", "eic.line5_threshold", "eic.threshold_other", "eic.threshold_joint", "eic.threshold0_other", "eic.threshold1_other", "eic.threshold0_joint", "eic.threshold1_joint", "eic.smaller", "eic.step1_income", "eic.step5_income", "eic.earned_for_limit", "eic.wsb_6", "eic.wsb_4b", "eic.earned_income", "param:eic.table_start"];
    const p = pinned("eic.credit's eligible alternative reads line6, which is line2 when line4 (line3 equals line1) is true and after_line4 otherwise, so the mutant differs only where line4 is true. eligible true needs step1_income (AGI, which line3 copies, below the limit) and step5_income (earned_for_limit, whose branch value is line1's source, below the limit) complete and true, so line3 and line1 are complete there and line4 is a complete comparison. With line4 true, line5 looks up line3 in the same EIC table (by the same ssn_count choices and filing status) that line2 looks up line1 in, so where line1 is at least table_start line5 equals line2 and after_line4 (line2, or the smaller of line5 and line2) is line2; where line1 is below table_start line2 is $0 and line3, equal to line1, is below every line 5 threshold (all of which exceed table_start), so line5 is blank and after_line4 is line2.", lines, "02abad669a667830");
    return { reason: p.reason, holds: (d: CanonicalData): boolean => {
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
};

// A keyed argument pinned to the lines it reads: the digest of each named line's expression, refusal
// gates, type, printed marker and display condition, and of the list of every line that reads it. The
// argument holds only while none of those changed; any edit to a premise line, or a new reader of one,
// makes the survivor unexplained again until the argument is re-made.
export function premiseDigest(data: CanonicalData, lines: string[]): string {
  const facts = lines.map((id) => {
    if (id.startsWith("table:")) return { id, table: data.tables.find((t) => t.id === id.slice(6)) ?? null };
    if (id.startsWith("param:")) return { id, param: data.params.values[id.slice(6)] ?? null };
    const l = findLine(data, id);
    return l ? { id, expr: l.expr, refuses: l.refuses ?? [], type: l.type, printed: l.printed, shown_when: l.shown_when ?? null, readers: [...new Set(allReaders(data, id))].sort() } : { id, missing: true };
  });
  return createHash("sha256").update(stableStringify(facts)).digest("hex").slice(0, 16);
}

function pinned(reason: string, lines: string[], digest: string) {
  return { reason: `${reason} (Premises pinned: ${lines.join(", ")}.)`, holds: (d: CanonicalData): boolean => premiseDigest(d, lines) === digest };
}

// Why a surviving mutant is equivalent, checked against the current data: the keyed conditional
// argument when its structural conditions hold, else the first structural rule that accepts it.
export function equivalenceReason(data: CanonicalData, mutation: Mutation): string | undefined {
  const conditional = EQUIVALENT_IF[mutation.id];
  if (conditional?.holds(data)) return conditional.reason + " (structural conditions re-checked this run.)";
  return structuralReason(data, mutation);
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

// A Schedule 1-A printed line inside a part is a gate: $0 when the part does not apply, otherwise
// its "_calc" helper. Equivalences about the figure look through the gate.
function s1aFigure(d: CanonicalData, id: string): Line | undefined {
  const l = findLine(d, id);
  if (l?.expr.op !== "choose") return l;
  const thens = l.expr.alternatives.map((a) => a.then);
  return thens.length === 2 && thens.includes("s1a.zero") && thens.includes(id + "_calc") ? findLine(d, id + "_calc") : l;
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
    reason: `${what} Only a 2019 vehicle's ${line} reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6.`,
    holds: (d: CanonicalData): boolean => {
      const is2019 = exprOf(d, "scveh.is2019");
      if (is2019?.op !== "test" || stableStringify(is2019.eq) !== stableStringify(["scveh.placed", { const: "y2019" }])) return false;
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
      return year(4) === 4 && year(5) === 5 && year(6) === 6 && dominatedBy(d, line, "scveh.is2019") && check(d);
    },
  };
}

const normal = (v: { kind: string; cents?: number; value?: unknown; num?: number; den?: number }): string =>
  v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
    : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;

// `classm:<case>`: killed, but only by class M cases (the first named). A class M rerun regenerates
// those cases, so the kill can be lost unless a stage fixture keeps the case.
type Outcome = "check" | "fixtures" | `classm:${string}` | "survives";

// What happens to one mutant: the checker rejects it, a fixture value changes, or it survives.
// Cases other than class M are tried first, so a kill is attributed to class M only when no other case makes it.
function outcome(baseline: CanonicalData, cases: ReturnType<typeof loadCases>["cases"], m: Mutation): Outcome {
  const data = cloneData(baseline);
  m.apply(data);
  if (runChecks(data).errors.length > 0) return "check";
  const kills = (c: (typeof cases)[number]): boolean => {
    const result = evaluate(data, c.inputs, allTargets(data, c.inputs));
    for (const [key, expected] of Object.entries(c.expect ?? {})) {
      const der = result.derivations.get(key);
      if (!der || normal(der.value) !== normal(expected)) return true;
    }
    return false;
  };
  if (cases.some((c) => c.evidence !== "M" && kills(c))) return "fixtures";
  const classm = cases.find((c) => c.evidence === "M" && kills(c));
  return classm ? `classm:${classm.id}` : "survives";
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

// A survivor that a recorded, still-open defect explains: it is not equivalent and is not excluded from
// the adjusted score, but it does not fail the run while the bug entry is open. The run fails if a listed
// mutant is killed (the entry is stale) or the bug entry is missing.
const OPEN_DEFECT_SURVIVORS: Record<string, string> = {};

export async function runMutation(): Promise<number> {
  const baseline = loadCanonical();
  const fixtureFile = loadCases();

  // A mismatching baseline must never make every mutant look killed.
  const baselineErrors = runChecks(baseline).errors;
  if (baselineErrors.length > 0) {
    // Every mutant would then be "killed by checker" and the score a vacuous 100% (T-225).
    throw new Error(`mutation baseline has ${baselineErrors.length} check error(s); fix them first: ${baselineErrors.slice(0, 3).join("; ")}`);
  }
  for (const c of fixtureFile.cases) {
    const result=evaluate(baseline,c.inputs,allTargets(baseline,c.inputs));
    for (const [key,expected] of Object.entries(c.expect ?? {})) {
      const actual=result.derivations.get(key)?.value;
      if (!actual || normal(actual)!==normal(expected)) throw new Error(`mutation baseline mismatch: ${c.id} ${key}`);
    }
  }
  const muts = mutations(baseline);
  const survivors: Mutation[] = [];
  const classmOnly: { m: Mutation; case: string }[] = [];
  let killedByCheck = 0;
  let killedByFixtures = 0;

  const outcomes = await outcomesOf(baseline, fixtureFile.cases, muts);
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
  const openDefect = survivors.filter((s) => !(s.id in EQUIVALENT) && s.id in OPEN_DEFECT_SURVIVORS);
  const unexplained = survivors.filter((s) => !(s.id in EQUIVALENT) && !(s.id in OPEN_DEFECT_SURVIVORS));
  const inventory = readFileSync(join(ROOT, "BUG_INVENTORY.md"), "utf8");
  const openDefectProblems = Object.entries(OPEN_DEFECT_SURVIVORS).flatMap(([id, bug]) => [
    ...(survivors.some((s) => s.id === id) ? [] : [`${id}: listed for ${bug} but no longer survives; remove the entry`]),
    ...(new RegExp(`^## ${bug} — .*\\(open\\)$`, "m").test(inventory) ? [] : [`${id}: ${bug} is not an open entry in BUG_INVENTORY.md`]),
  ]);
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
  report.push(`| Killed by fixtures | ${killedByFixtures} (${classmOnly.length} only by class M cases) |`);
  report.push(`| Surviving | ${survivors.length} (${equivalentSurvivors.length} provably equivalent) |`);
  report.push(`| Mutation score (raw) | ${(score * 100).toFixed(1)}% |`);
  report.push(`| Mutation score (equivalent mutants excluded) | ${(adjusted * 100).toFixed(1)}% |`);
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
  if (equivalentSurvivors.length > 0) {
    report.push("## Surviving — classified equivalent");
    report.push("");
    for (const s of equivalentSurvivors) {
      report.push(`- \`${s.id}\` (${s.kind}, ${s.where}): ${EQUIVALENT[s.id]}`);
    }
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
  const outDir = yearPath("reports");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "mutation.md"), report.join("\n"));
  console.log(`mutation: ${total} mutants, killed by checker ${killedByCheck}, by fixtures ${killedByFixtures} (${classmOnly.length} only by class M cases), surviving ${survivors.length} (${equivalentSurvivors.length} equivalent; score ${(score * 100).toFixed(1)}%, adjusted ${(adjusted * 100).toFixed(1)}%)`);
  console.log(`report: reports/${YEAR}/mutation.md`);
  for (const p of openDefectProblems) console.log(`mutation: ${p}`);
  return unexplained.length === 0 && openDefectProblems.length === 0 ? 0 : 1;
}
