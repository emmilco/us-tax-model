// The evaluator: lazy, memoized evaluation over the line graph, returning a
// value and a derivation for every line. Money is integer cents throughout;
// the only rounding performed is multiply_rate's cent-level half-up (the
// register entry amb.2025.multiplication_subcent) and the explicit whole-
// dollar rounding the caller asks for when displaying results.

import type { CanonicalData, CiteFilled, Expr, FormDoc, Operand, TableDoc, TestExpr } from "./types.js";

export type Value =
  | { kind: "money"; cents: number }
  | { kind: "rate"; num: number; den: number }
  | { kind: "bool"; value: boolean }
  | { kind: "enum"; value: string }
  | { kind: "unknown"; reason: string };

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
  inputs: Record<string, number | boolean | string>;
  memo: Map<string, Derivation>;
  inProgress: Set<string>;
  errors: string[];
}

export function evaluate(
  data: CanonicalData,
  inputs: Record<string, number | boolean | string>,
  targets: string[],
): EvalResult {
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
export function evaluateAll(data: CanonicalData, inputs: Record<string, number | boolean | string>): EvalResult {
  const targets: string[] = [];
  for (const doc of [...data.forms, ...data.defs]) {
    if (doc.kind === "def") continue;
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
  } else if (line.expr.op === "input") {
    const raw = ctx.inputs[lineId];
    const value: Value =
      raw === undefined
        ? { kind: "unknown", reason: `no input supplied for ${lineId}` }
        : typeof raw === "number"
          ? { kind: "money", cents: raw }
          : typeof raw === "boolean"
            ? { kind: "bool", value: raw }
            : { kind: "enum", value: raw };
    result = { line: key, op: "input", value, operands: [], cite: line.cite, guardsNotTaken: [], notes: [] };
  } else {
    result = evalExpr(ctx, frame, lineId, line.expr as Expr, line.cite);
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
    operandsOut?.push({ ref: op, value: d.value });
    return d.value;
  }
  if ("param" in op) {
    const entry = ctx.data.params.values[op.param];
    if (!entry) {
      return { kind: "unknown", reason: `parameter ${op.param} missing` };
    }
    let value: Value;
    if (typeof entry.value === "number") {
      value = { kind: "money", cents: entry.value };
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
    typeof v === "number" ? { kind: "money", cents: v } : typeof v === "boolean" ? { kind: "bool", value: v } : { kind: "enum", value: v };
  operandsOut?.push({ ref: operandDisplay(op), value });
  return value;
}

/** Half-up at the cent: floor((2*a*n + d) / (2*d)) computes round-half-up of a*n/d toward +infinity. */
export function multiplyRateHalfUp(cents: number, num: number, den: number): number {
  return Math.floor((2 * cents * num + den) / (2 * den));
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
    case "sum": {
      let total = 0;
      let unknown: Value | null = null;
      for (const ref of expr.of) {
        const v = evalOperand(ctx, frame, ref, ops);
        if (v.kind === "money") total += v.cents;
        else if (v.kind === "unknown") unknown = v;
        else return d({ kind: "unknown", reason: `sum operand ${ref} is not money` }, "sum", ops);
      }
      return d(unknown ?? { kind: "money", cents: total }, "sum", ops);
    }
    case "subtract":
    case "subtract_floor0": {
      const from = evalOperand(ctx, frame, expr.from, ops);
      const take = evalOperand(ctx, frame, expr.take, ops);
      if (from.kind === "unknown") return d(from, expr.op, ops);
      if (take.kind === "unknown") return d(take, expr.op, ops);
      if (from.kind !== "money" || take.kind !== "money") {
        return d({ kind: "unknown", reason: "operands are not money" }, expr.op, ops);
      }
      const diff = from.cents - take.cents;
      const value = expr.op === "subtract_floor0" ? Math.max(0, diff) : diff;
      return d({ kind: "money", cents: value }, expr.op, ops);
    }
    case "smaller_of":
    case "larger_of": {
      const vals: number[] = [];
      for (const ref of expr.of) {
        const v = evalOperand(ctx, frame, ref, ops);
        if (v.kind === "unknown") return d(v, expr.op, ops);
        if (v.kind !== "money") return d({ kind: "unknown", reason: "operands are not money" }, expr.op, ops);
        vals.push(v.cents);
      }
      const value = expr.op === "smaller_of" ? Math.min(...vals) : Math.max(...vals);
      return d({ kind: "money", cents: value }, expr.op, ops);
    }
    case "multiply_rate": {
      const amount = evalOperand(ctx, frame, expr.amount, ops);
      const rate = evalOperand(ctx, frame, expr.rate, ops);
      if (amount.kind === "unknown") return d(amount, "multiply_rate", ops);
      if (rate.kind === "unknown") return d(rate, "multiply_rate", ops);
      if (amount.kind !== "money" || rate.kind !== "rate") {
        return d({ kind: "unknown", reason: "multiply_rate operands wrong" }, "multiply_rate", ops);
      }
      const cents = multiplyRateHalfUp(amount.cents, rate.num, rate.den);
      return d({ kind: "money", cents }, "multiply_rate", ops, [], ["half-up to the cent per the ambiguity register"]);
    }
    case "table_lookup": {
      const key = evalOperand(ctx, frame, expr.key, ops);
      const status = evalOperand(ctx, frame, expr.status, ops);
      const table = ctx.data.tables.find((t) => t.id === expr.table);
      if (!table || table.kind !== "tax_table") return d({ kind: "unknown", reason: `table ${expr.table} missing` }, "table_lookup", ops);
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
        const g = evalTest(ctx, frame, alt.guard);
        const gText = JSON.stringify(alt.guard);
        if (g.kind === "unknown") return d(g, "choose", ops, guardsNotTaken, [`guard unknown: ${g.reason}`]);
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
      const v = evalTest(ctx, frame, expr as TestExpr);
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

function evalTest(ctx: Ctx, frame: Frame, test: TestExpr): Value {
  if ("all" in test) {
    for (const t of test.all) {
      const v = evalTest(ctx, frame, t);
      if (v.kind !== "bool") return v;
      if (!v.value) return { kind: "bool", value: false };
    }
    return { kind: "bool", value: true };
  }
  if ("any" in test) {
    for (const t of test.any) {
      const v = evalTest(ctx, frame, t);
      if (v.kind !== "bool") return v;
      if (v.value) return { kind: "bool", value: true };
    }
    return { kind: "bool", value: false };
  }
  if ("not" in test) {
    const v = evalTest(ctx, frame, test.not);
    if (v.kind !== "bool") return v;
    return { kind: "bool", value: !v.value };
  }
  const key = (["eq", "ne", "lt", "le", "gt", "ge"] as const).find((k) => (test as Record<string, unknown>)[k] !== undefined)!;
  const [a, b] = (test as unknown as Record<string, [Operand, Operand]>)[key]!;
  const av = evalOperand(ctx, frame, a);
  const bv = evalOperand(ctx, frame, b);
  if (av.kind === "unknown") return av;
  if (bv.kind === "unknown") return bv;
  let result: boolean;
  if (av.kind === "money" && bv.kind === "money") {
    const x = av.cents;
    const y = bv.cents;
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
