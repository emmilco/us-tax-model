// The evaluator: lazy, memoized evaluation over the line graph, returning a
// value and a derivation for every line. Money is integer cents throughout;
// the only rounding performed is multiply_rate's cent-level half-up (the
// register entry amb.2025.multiplication_subcent) and the explicit whole-
// dollar rounding the caller asks for when displaying results.

import type { CanonicalData, CiteFilled, Expr, FormDoc, Operand, TableDoc, TestExpr, Inputs, Line } from "./types.js";

export type Value =
  | { kind: "count"; value: number }
  | { kind: "refusal"; gate: string; form: string; remedy: string; cite: CiteFilled }
  | { kind: "money"; cents: number }
  | { kind: "rate"; num: number; den: number }
  | { kind: "bool"; value: boolean }
  | { kind: "enum"; value: string }
  | { kind: "unknown"; reason: string; input?: string; lowerBound?: number };

export interface Derivation {
  line: string; // canonical id (instance keyed when inside a def)
  op: string;
  value: Value;
  operands: { ref: string; value: Value }[];
  cite: CiteFilled | null;
  guardsNotTaken: { guard: string; value: Value }[];
  notes: string[];
  takenGuardIndex?: number;
}

export interface EvalResult {
  values: Map<string, Value>;
  derivations: Map<string, Derivation>;
}

interface Frame {
  doc: FormDoc;
  instKey: string | null;
  bind: Record<string, Operand> | null;
  caller: Frame | null;
}

interface Ctx {
  data: CanonicalData;
  byId: Map<string, FormDoc>;
  inputs: Inputs;
  memo: Map<string, Derivation>;
  inProgress: Set<string>;
  errors: string[];
}

export function evaluate(
  data: CanonicalData,
  inputs: Inputs,
  targets: string[],
): EvalResult {
  validateInputs(data, inputs);
  const ctx: Ctx = {
    data,
    byId: new Map([...data.forms, ...data.defs].map((d) => [d.id, d])),
    inputs,
    memo: new Map(),
    inProgress: new Set(),
    errors: [],
  };
  const rootFrames = new Map<string, Frame>();
  for (const target of targets) {
    const dot = target.indexOf(".");
    const fileId = target.slice(0, dot);
    const doc = ctx.byId.get(fileId);
    if (!doc) {
      ctx.errors.push(`target '${target}': unknown document '${fileId}'`);
      continue;
    }
    const frame = rootFrames.get(fileId) ?? { doc, instKey: null, bind: null, caller: null };
    rootFrames.set(fileId, frame);
    evalLine(ctx, frame, target);
  }
  const values = new Map<string, Value>();
  for (const [key, d] of ctx.memo) values.set(key, d.value);
  return { values, derivations: ctx.memo };
}

/** Evaluate every line of the given documents (used by compare/fixtures). */
export function evaluateAll(data: CanonicalData, inputs: Inputs): EvalResult {
  const targets: string[] = [];
  for (const doc of [...data.forms, ...data.defs]) {
    if (doc.kind === "def" || doc.collection) continue;
    for (const line of doc.lines) targets.push(line.id);
  }
  return evaluate(data, inputs, targets);
}

function errValue(ctx: Ctx, frame: Frame, lineId: string, reason: string): Derivation {
  return {
    line: canonicalKey(frame, lineId),
    op: "error",
    value: { kind: "unknown", reason },
    operands: [],
    cite: null,
    guardsNotTaken: [],
    notes: [reason],
  };
}

function canonicalKey(frame: Frame, lineId: string): string {
  const prefix = `${frame.doc.id}.`;
  const local = lineId.startsWith(prefix) ? lineId.slice(prefix.length) : lineId;
  return `${frame.instKey ?? frame.doc.id}.${local}`;
}

function evalLine(ctx: Ctx, frame: Frame, lineId: string): Derivation {
  const key = canonicalKey(frame, lineId);
  const memo = ctx.memo.get(key);
  if (memo) return memo;
  if (ctx.inProgress.has(key)) {
    const d = errValue(ctx, frame, lineId, `cycle at ${key}`);
    ctx.errors.push(d.notes[0]!);
    return d;
  }
  ctx.inProgress.add(key);

  const line = frame.doc.lines.find((l) => l.id === lineId);
  let result: Derivation;
  if (!line) {
    // Cross-document reference: resolve to the target document.
    const dot = lineId.indexOf(".");
    const target = dot > 0 ? ctx.byId.get(lineId.slice(0, dot)) : undefined;
    const targetLine = target?.lines.find((l) => l.id === lineId);
    if (target && targetLine) {
      result = evalLine(ctx, { doc: target, instKey: null, bind: null, caller: null }, lineId);
      ctx.memo.set(key, result);
      ctx.inProgress.delete(key);
      return result;
    }
    result = errValue(ctx, frame, lineId, `reference '${lineId}' does not resolve`);
    ctx.errors.push(result.notes[0]!);
  } else if (frame.instKey && (frame.doc.parameters ?? []).includes(lineId) && frame.bind && frame.caller) {
    // A def parameter inside an instance: evaluate the bound operand in the caller.
    const op = frame.bind[lineId];
    const value = op === undefined ? { kind: "unknown", reason: `unbound parameter ${lineId}` } as Value : evalOperand(ctx, frame.caller, op);
    result = {
      line: key,
      op: "bound",
      value,
      operands: op !== undefined && typeof op === "string" ? [{ ref: op, value }] : [],
      cite: line.cite,
      guardsNotTaken: [],
      notes: [],
    };
  } else {
    const gateOps: { ref: string; value: Value }[] = [];
    let blocked: Value | null = null;
    for (const refusal of line.refuses ?? []) {
      const gate = evalLine(ctx, frame, refusal.when);
      gateOps.push({ ref: gate.line, value: gate.value });
      if (gate.value.kind === "bool" && gate.value.value) {
        blocked = { kind: "refusal", gate: gate.line, form: refusal.form, remedy: refusal.remedy, cite: refusal.cite };
        break;
      }
      if (gate.value.kind !== "bool") { blocked = gate.value; break; }
    }
    if (blocked) {
      result = { line: key, op: "gate", value: blocked, operands: [], cite: line.cite, guardsNotTaken: [], notes: [] };
    } else if (line.expr.op === "input") {
      const raw = ctx.inputs[key];
      const value: Value = raw === undefined || raw === null
        ? { kind: "unknown", reason: `no input supplied for ${key}`, input: key }
        : line.type === "Count" ? { kind: "count", value: raw as number }
        : typeof raw === "number" ? { kind: "money", cents: raw }
        : typeof raw === "boolean" ? { kind: "bool", value: raw }
        : { kind: "enum", value: raw as string };
      result = { line: key, op: "input", value, operands: [], cite: line.cite, guardsNotTaken: [], notes: [] };
    } else {
      result = evalExpr(ctx, frame, lineId, line.expr as Expr, line.cite);
    }
    result.operands.unshift(...gateOps);
  }
  if (line?.ambiguity) {
    const entry=ctx.data.register.entries.find(e=>e.id===line.ambiguity);
    if(entry) result.notes.push(`Interpretation ${entry.id}: ${entry.chosen} ${entry.reason} (${entry.cite.doc}, ${entry.cite.locator})`);
  }
  ctx.memo.set(key, result);
  ctx.inProgress.delete(key);
  return result;
}

function operandDisplay(op: Operand): string {
  if (typeof op === "string") return op;
  if ("param" in op) return `#${op.param}`;
  return JSON.stringify(op.const);
}

function evalOperand(ctx: Ctx, frame: Frame, op: Operand, operandsOut?: { ref: string; value: Value }[]): Value {
  if (typeof op === "string") {
    const d = evalLine(ctx, frame, op);
    operandsOut?.push({ ref: d.line, value: d.value });
    return d.value;
  }
  if ("param" in op) {
    const entry = ctx.data.params.values[op.param];
    if (!entry) {
      return { kind: "unknown", reason: `parameter ${op.param} missing` };
    }
    let value: Value;
    if (typeof entry.value === "number") {
      value = entry.type === "Count" ? { kind: "count", value: entry.value } : { kind: "money", cents: entry.value };
    } else if (typeof entry.value === "boolean") {
      value = { kind: "bool", value: entry.value };
    } else if ("num" in entry.value) {
      value = { kind: "rate", num: entry.value.num, den: entry.value.den };
    } else {
      // Status-keyed: resolve by the return's filing status.
      const status = ctx.inputs["f1040.status"];
      if (typeof status !== "string") {
        value = { kind: "unknown", reason: "filing status not supplied for status-keyed parameter" };
      } else {
        const cents = (entry.value as Record<string, number>)[status];
        value = cents === undefined ? { kind: "unknown", reason: `no value for status '${status}'` } : { kind: "money", cents };
      }
    }
    operandsOut?.push({ ref: `#${op.param}`, value });
    return value;
  }
  const v = op.const;
  const value: Value =
    op.type === "Count" ? { kind: "count", value: v as number } : typeof v === "number" ? { kind: "money", cents: v } : typeof v === "boolean" ? { kind: "bool", value: v } : { kind: "enum", value: v };
  operandsOut?.push({ ref: operandDisplay(op), value });
  return value;
}

/** Half-up at the cent: floor((2*a*n + d) / (2*d)) computes round-half-up of a*n/d toward +infinity. */
/** Round cents to a multiple of `unit` by the named rule; floor division throughout, as the Lean atoms. */
export function roundToUnit(cents: number, unit: number, rule: string): number | null {
  const x = BigInt(cents); const u = BigInt(unit);
  const floorDiv = (a: bigint, b: bigint): bigint => { const q = a / b; return (a % b !== 0n && (a < 0n) !== (b < 0n)) ? q - 1n : q; };
  if (rule === "half_up") return safeNumber(floorDiv(2n * x + u, 2n * u) * u);
  if (rule === "up") return safeNumber(floorDiv(x + u - 1n, u) * u);
  if (rule === "down") return safeNumber(floorDiv(x, u) * u);
  return null;
}

export function multiplyRateHalfUp(cents: number, num: number, den: number): number {
  const n = 2n * BigInt(cents) * BigInt(num) + BigInt(den);
  const d = 2n * BigInt(den);
  return safeNumber(n / d - (n < 0n && n % d !== 0n ? 1n : 0n));
}

export function exactBracketCents(rows: { upper: number | null; base: number; rate: { num: number; den: number }; over: number }[], amount: number): { n: bigint; d: bigint } | null {
  for (const row of rows) {
    if (row.upper === null || amount <= row.upper) {
      const n = BigInt(row.base) * BigInt(row.rate.den) + BigInt(amount - row.over) * BigInt(row.rate.num);
      return { n, d: BigInt(row.rate.den) };
    }
  }
  return null;
}

function evalExpr(ctx: Ctx, frame: Frame, lineId: string, expr: Expr, cite: CiteFilled): Derivation {
  const d = (value: Value, op: string, operands: { ref: string; value: Value }[], guardsNotTaken: { guard: string; value: Value }[] = [], notes: string[] = []): Derivation => ({
    line: canonicalKey(frame, lineId),
    op,
    value,
    operands,
    cite,
    guardsNotTaken,
    notes,
  });
  const ops: { ref: string; value: Value }[] = [];

  switch (expr.op) {
    case "copy": {
      if (typeof expr.from === "string") {
        const v = evalOperand(ctx, frame, expr.from, ops);
        return d(v, "copy", ops);
      }
      const inst = expr.from;
      const def = ctx.byId.get(inst.def);
      if (!def) return d({ kind: "unknown", reason: `def ${inst.def} missing` }, "copy", ops);
      const key = `${frame.instKey ?? "root"}|inst:${inst.def}#${JSON.stringify(inst.bind)}`;
      const inner: Frame = { doc: def, instKey: key, bind: inst.bind, caller: frame };
      // Binding operands are evaluated in the caller frame for the record.
      for (const [name, op] of Object.entries(inst.bind)) {
        const v = evalOperand(ctx, frame, op);
        ops.push({ ref: `bind ${name} = ${operandDisplay(op)}`, value: v });
      }
      const innerDer = evalLine(ctx, inner, inst.line);
      return d(innerDer.value, "copy(instance)", ops, [], [`via ${inst.def} line ${inst.line}`]);
    }
    case "param": {
      const v = evalOperand(ctx, frame, { param: expr.ref }, ops);
      return d(v, "param", ops);
    }
    case "sum_over": {
      const entry = ctx.byId.get(expr.collection)!;
      const parent = entry.collection?.parent ? frame.instKey : null;
      const rosterKey = `$${entry.id}${parent ? "@" + parent : ""}`;
      const roster = ctx.inputs[rosterKey];
      if (!Array.isArray(roster)) return d({ kind: "unknown", reason: "collection roster not confirmed", input: rosterKey }, "sum_over", ops);
      let total = 0n;
      let missing: Value | null = null;
      const fieldType = entry.lines.find(l => l.id === expr.field)!.type;
      for (const key of [...roster].sort()) {
        const inner: Frame = { doc: entry, instKey: `${parent ? parent + "." : ""}${entry.id}[${key}]`, bind: null, caller: frame };
        if (expr.where) {
          const selected = evalTest(ctx, inner, expr.where, ops);
          if (selected.kind === "refusal") return d(selected, "sum_over", ops);
          if (selected.kind !== "bool") { missing = selected; continue; }
          if (!selected.value) continue;
        }
        const item = evalLine(ctx, inner, expr.field);
        ops.push({ ref: item.line, value: item.value });
        if (item.value.kind === "refusal") return d(item.value, "sum_over", ops);
        if (item.value.kind === "unknown") { missing = item.value; continue; }
        if (item.value.kind === "money") total += BigInt(item.value.cents);
        else if (item.value.kind === "count") total += BigInt(item.value.value);
      }
      if (missing?.kind === "unknown" && fieldType === "Count") missing = { ...missing, lowerBound: safeNumber(total) };
      return d(missing ?? (fieldType === "Count" ? { kind: "count", value: safeNumber(total) } : { kind: "money", cents: safeNumber(total) }), "sum_over", ops, [], [`confirmed roster ${rosterKey}: ${roster.join(", ")}`.trimEnd()]);
    }
    case "sum": {
      let total = 0n;
      let unknown: Value | null = null;
      for (const ref of expr.of) {
        const v = evalOperand(ctx, frame, ref, ops);
        if (v.kind === "money") total += BigInt(v.cents);
        else if (v.kind === "refusal") return d(v, "sum", ops);
        else if (v.kind === "unknown") unknown = v;
        else return d({ kind: "unknown", reason: `sum operand ${ref} is not money` }, "sum", ops);
      }
      return d(unknown ?? { kind: "money", cents: safeNumber(total) }, "sum", ops);
    }
    case "subtract":
    case "subtract_floor0": {
      const from = evalOperand(ctx, frame, expr.from, ops);
      const take = evalOperand(ctx, frame, expr.take, ops);
      if ((from.kind === "unknown" || from.kind === "refusal")) return d(from, expr.op, ops);
      if ((take.kind === "unknown" || take.kind === "refusal")) return d(take, expr.op, ops);
      if (from.kind !== "money" || take.kind !== "money") {
        return d({ kind: "unknown", reason: "operands are not money" }, expr.op, ops);
      }
      const diff = safeNumber(BigInt(from.cents) - BigInt(take.cents));
      const value = expr.op === "subtract_floor0" ? Math.max(0, diff) : diff;
      return d({ kind: "money", cents: value }, expr.op, ops);
    }
    case "smaller_of":
    case "larger_of": {
      const vals: number[] = [];
      for (const ref of expr.of) {
        const v = evalOperand(ctx, frame, ref, ops);
        if ((v.kind === "unknown" || v.kind === "refusal")) return d(v, expr.op, ops);
        if (v.kind !== "money") return d({ kind: "unknown", reason: "operands are not money" }, expr.op, ops);
        vals.push(v.cents);
      }
      const value = expr.op === "smaller_of" ? Math.min(...vals) : Math.max(...vals);
      return d({ kind: "money", cents: value }, expr.op, ops);
    }
    case "multiply_count": {
      const amount = evalOperand(ctx, frame, expr.amount, ops);
      const count = evalOperand(ctx, frame, expr.count, ops);
      if (amount.kind === "unknown" || amount.kind === "refusal") return d(amount, "multiply_count", ops);
      if (count.kind === "unknown" || count.kind === "refusal") return d(count, "multiply_count", ops);
      if (amount.kind !== "money" || count.kind !== "count") {
        return d({ kind: "unknown", reason: "multiply_count operands wrong" }, "multiply_count", ops);
      }
      return d({ kind: "money", cents: amount.cents * count.value }, "multiply_count", ops);
    }
    case "prorate": {
      const amount = evalOperand(ctx, frame, expr.amount, ops);
      const part = evalOperand(ctx, frame, expr.part, ops);
      const whole = evalOperand(ctx, frame, expr.whole, ops);
      for (const v of [amount, part, whole]) if (v.kind === "unknown" || v.kind === "refusal") return d(v, "prorate", ops);
      if (amount.kind !== "money" || part.kind !== "money" || whole.kind !== "money" || whole.cents <= 0) {
        return d({ kind: "unknown", reason: "prorate operands wrong" }, "prorate", ops);
      }
      const scale = 10 ** expr.places;
      const ratio = Math.max(0, Math.min(scale, multiplyRateHalfUp(part.cents, scale, whole.cents)));
      const cents = multiplyRateHalfUp(amount.cents, ratio, scale);
      return d({ kind: "money", cents }, "prorate", ops, [], [`ratio ${ratio}/${scale}, half-up to ${expr.places} places and not more than 1; product half-up to the cent`]);
    }
    case "multiply_rate": {
      const amount = evalOperand(ctx, frame, expr.amount, ops);
      const rate = evalOperand(ctx, frame, expr.rate, ops);
      if ((amount.kind === "unknown" || amount.kind === "refusal")) return d(amount, "multiply_rate", ops);
      if ((rate.kind === "unknown" || rate.kind === "refusal")) return d(rate, "multiply_rate", ops);
      if (amount.kind !== "money" || rate.kind !== "rate") {
        return d({ kind: "unknown", reason: "multiply_rate operands wrong" }, "multiply_rate", ops);
      }
      const cents = multiplyRateHalfUp(amount.cents, rate.num, rate.den);
      return d({ kind: "money", cents }, "multiply_rate", ops, [], ["half-up to the cent per the ambiguity register"]);
    }
    case "round": {
      const v = evalOperand(ctx, frame, expr.of, ops);
      if ((v.kind === "unknown" || v.kind === "refusal")) return d(v, "round", ops);
      if (v.kind !== "money") return d({ kind: "unknown", reason: "round operand is not money" }, "round", ops);
      if (!(Number.isInteger(expr.unit) && expr.unit > 0)) return d({ kind: "unknown", reason: "round unit is not a positive integer" }, "round", ops);
      const cents = roundToUnit(v.cents, expr.unit, expr.rule);
      if (cents === null) return d({ kind: "unknown", reason: `round rule ${expr.rule} unknown` }, "round", ops);
      return d({ kind: "money", cents }, "round", ops, [], [`${expr.rule} to a multiple of ${expr.unit} cents`]);
    }
    case "table_lookup": {
      const key = evalOperand(ctx, frame, expr.key, ops);
      const status = evalOperand(ctx, frame, expr.status, ops);
      const table = ctx.data.tables.find((t) => t.id === expr.table);
      if (!table || table.kind !== "tax_table") return d({ kind: "unknown", reason: `table ${expr.table} missing` }, "table_lookup", ops);
      if (key.kind === "unknown" || key.kind === "refusal") return d(key, "table_lookup", ops);
      if (status.kind === "unknown" || status.kind === "refusal") return d(status, "table_lookup", ops);
      if (key.kind !== "money" || status.kind !== "enum") {
        return d({ kind: "unknown", reason: "lookup key or status missing" }, "table_lookup", ops);
      }
      const col = table.columns!.findIndex((c) => c.statuses.includes(status.value));
      if (col < 0) return d({ kind: "unknown", reason: `no column for ${status.value}` }, "table_lookup", ops);
      const band = findBand(table, key.cents);
      if (!band) return d({ kind: "unknown", reason: `no band for ${key.cents} cents` }, "table_lookup", ops);
      return d({ kind: "money", cents: band.tax[col]! }, "table_lookup", ops, [], [`band ${band.at_least}-${band.less_than}`, `column ${table.columns![col]!.key}`]);
    }
    case "choose": {
      const guardsNotTaken: { guard: string; value: Value }[] = [];
      for (let gi = 0; gi < expr.alternatives.length; gi++) {
        const alt = expr.alternatives[gi]!;
        const g = evalTest(ctx, frame, alt.guard, ops);
        const gText = JSON.stringify(alt.guard);
        if ((g.kind === "unknown" || g.kind === "refusal")) return d(g, "choose", ops, guardsNotTaken, [`guard incomplete`]);
        if (g.kind !== "bool") return d({ kind: "unknown", reason: "guard not bool" }, "choose", ops);
        if (g.value) {
          const then =
            typeof alt.then === "string"
              ? evalOperand(ctx, frame, alt.then, ops)
              : (() => {
                  const def = ctx.byId.get(alt.then.def);
                  if (!def) return { kind: "unknown", reason: `def ${alt.then.def} missing` } as Value;
                  const key = `${frame.instKey ?? "root"}|inst:${alt.then.def}#${JSON.stringify(alt.then.bind)}`;
                  const inner: Frame = { doc: def, instKey: key, bind: alt.then.bind, caller: frame };
                  for (const [name, op] of Object.entries(alt.then.bind)) {
                    const v = evalOperand(ctx, frame, op);
                    ops.push({ ref: `bind ${name} = ${operandDisplay(op)}`, value: v });
                  }
                  return evalLine(ctx, inner, alt.then.line).value;
                })();
          const der = d(then, "choose", ops, guardsNotTaken, [`taken: ${gText}`]);
          der.takenGuardIndex = gi;
          return der;
        }
        guardsNotTaken.push({ guard: gText, value: g });
      }
      return d({ kind: "unknown", reason: "no guard matched" }, "choose", ops, guardsNotTaken);
    }
    case "test": {
      const v = evalTest(ctx, frame, expr as TestExpr, ops);
      return d(v, "test", ops);
    }
    default:
      return d({ kind: "unknown", reason: `atom ${expr.op} not implemented` }, expr.op, ops);
  }
}

function findBand(table: TableDoc, cents: number): { at_least: number; less_than: number; tax: number[] } | null {
  const bands = table.bands!;
  let lo = 0;
  let hi = bands.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    const b = bands[mid]!;
    if (cents < b.at_least) hi = mid - 1;
    else if (cents >= b.less_than) lo = mid + 1;
    else return b;
  }
  return null;
}

function evalTest(ctx: Ctx, frame: Frame, test: TestExpr, ops?: { ref: string; value: Value }[]): Value {
  if ("all" in test || "any" in test) {
    const isAll = "all" in test;
    const tests = "all" in test ? test.all : test.any;
    let pending: Value | null = null;
    for (const t of tests) {
      const v = evalTest(ctx, frame, t, ops);
      if (v.kind === "refusal") return v;
      if (v.kind !== "bool") { pending = v; continue; }
      if (v.value !== isAll) return {kind:"bool", value: !isAll};
    }
    return pending ?? {kind:"bool", value:isAll};
  }
  if ("not" in test) {
    const v = evalTest(ctx, frame, test.not, ops);
    if (v.kind !== "bool") return v;
    return { kind: "bool", value: !v.value };
  }
  const key = (["eq", "ne", "lt", "le", "gt", "ge"] as const).find((k) => (test as Record<string, unknown>)[k] !== undefined)!;
  const [a, b] = (test as unknown as Record<string, [Operand, Operand]>)[key]!;
  const av = evalOperand(ctx, frame, a, ops);
  const bv = evalOperand(ctx, frame, b, ops);
  if (av.kind === "unknown" && av.lowerBound !== undefined && bv.kind === "count") {
    const certain = (key === "gt" || key === "le") ? av.lowerBound > bv.value : (key === "ge" || key === "lt") ? av.lowerBound >= bv.value : av.lowerBound > bv.value;
    if (certain) return {kind:"bool",value:key === "gt" || key === "ge" || key === "ne"};
  }
  if ((av.kind === "unknown" || av.kind === "refusal")) return av;
  if ((bv.kind === "unknown" || bv.kind === "refusal")) return bv;
  let result: boolean;
  if ((av.kind === "money" && bv.kind === "money") || (av.kind === "count" && bv.kind === "count")) {
    const x = av.kind === "money" ? av.cents : av.value;
    const y = bv.kind === "money" ? bv.cents : bv.value;
    result = key === "eq" ? x === y : key === "ne" ? x !== y : key === "lt" ? x < y : key === "le" ? x <= y : key === "gt" ? x > y : x >= y;
  } else if (av.kind === "enum" && bv.kind === "enum") {
    result = key === "eq" ? av.value === bv.value : key === "ne" ? av.value !== bv.value : false;
  } else if (av.kind === "bool" && bv.kind === "bool") {
    result = key === "eq" ? av.value === bv.value : key === "ne" ? av.value !== bv.value : false;
  } else {
    return { kind: "unknown", reason: "comparison operand types" };
  }
  return { kind: "bool", value: result };
}

export function safeNumber(n: bigint): number {
  const v = Number(n);
  if (!Number.isSafeInteger(v)) throw new Error("integer exceeds exact JSON number range");
  return v;
}

/** Validate all supplied inputs, including values on currently unselected branches. */
export function validateInputs(data: CanonicalData, inputs: Inputs): void {
  const legal = new Map<string, Line>();
  const rosters = new Set<string>();
  const visit = (doc: FormDoc, prefix: string): void => {
    for (const line of doc.lines) if (line.expr.op === "input") legal.set(prefix + "." + line.id.slice(doc.id.length + 1), line);
    for (const child of data.forms.filter(d => d.collection?.parent === doc.id)) visitCollection(child, prefix);
  };
  const visitCollection = (doc: FormDoc, parent: string | null): void => {
    const rk = `$${doc.id}${parent ? "@" + parent : ""}`;
    rosters.add(rk);
    const raw = inputs[rk];
    if (raw === undefined || raw === null) return;
    if (!Array.isArray(raw) || raw.some(k => typeof k !== "string" || !/^[a-zA-Z0-9_-]+$/.test(k)) || new Set(raw).size !== raw.length) throw new Error(`${rk}: expected distinct stable entry keys`);
    for (const k of raw) visit(doc, `${parent ? parent + "." : ""}${doc.id}[${k}]`);
  };
  for (const doc of data.forms) {
    if (!doc.collection) visit(doc, doc.id);
    else if (!doc.collection.parent) visitCollection(doc, null);
  }
  for (const [key, raw] of Object.entries(inputs)) {
    if (rosters.has(key)) continue;
    const line = legal.get(key);
    if (!line) throw new Error(`${key}: input is not declared or belongs to an unlisted collection entry`);
    if (raw === null) continue;
    if (line.type === "Bool" ? typeof raw !== "boolean" : line.type.startsWith("Enum(") ? !data.params.enums[line.type.slice(5, -1)]!.values.includes(raw as string) : typeof raw !== "number" || !Number.isSafeInteger(raw) || (line.type !== "Dollars" && raw < 0)) throw new Error(`${key}: invalid ${line.type} input`);
  }
}
