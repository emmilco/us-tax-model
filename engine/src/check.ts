// Static checks over the canonical data. Fails the build unless:
// references resolve; the dependency graph is acyclic; expressions type
// check (including the non-negative refinement and the dollars/rates ban);
// choose guards are exhaustive and disjoint; citations are complete with a
// snapshot hash; and the tables satisfy their structural invariants.

import { IMPLEMENTED, VOCABULARY } from "./atoms.js";
import { stableStringify } from "./util.js";
import type {
  CanonicalData,
  Expr,
  FormDoc,
  Line,
  Operand,
  ParamEntry,
  TableDoc,
  TestExpr,
  ValueType,
} from "./types.js";

type Ty =
  | { kind: "money"; nonneg: boolean }
  | { kind: "count" }
  | { kind: "rate" }
  | { kind: "bool" }
  | { kind: "enum"; name: string };

interface Ctx {
  errors: string[];
  byId: Map<string, FormDoc>;
  lineMaps: Map<string, Map<string, { line: Line; index: number }>>;
  params: CanonicalData["params"];
  tables: Map<string, TableDoc>;
  enumValues: Map<string, string[]>;
}

function contextFor(data: CanonicalData): Ctx {
  const ctx: Ctx = {
    errors: [],
    byId: new Map(),
    lineMaps: new Map(),
    params: data.params,
    tables: new Map(data.tables.map((t) => [t.id, t])),
    enumValues: new Map(Object.entries(data.params.enums).map(([k, v]) => [k, v.values])),
  };
  for (const doc of [...data.forms, ...data.defs]) {
    if (ctx.byId.has(doc.id)) ctx.errors.push(`duplicate document id '${doc.id}'`);
    ctx.byId.set(doc.id, doc);
    const lm = new Map<string, { line: Line; index: number }>();
    doc.lines.forEach((line, index) => {
      if (lm.has(line.id)) ctx.errors.push(`${doc.id}: duplicate line id '${line.id}'`);
      lm.set(line.id, { line, index });
    });
    ctx.lineMaps.set(doc.id, lm);
  }
  return ctx;
}

/** The same reference/type rules used by the build, without citation or guard analysis.
 * A model candidate is data, never code; malformed expressions become diagnostics.
 */
export function checkExpressionTypes(data: CanonicalData, documentId: string): { line: string | null; message: string }[] {
  const ctx = contextFor(data);
  const result = ctx.errors.map(message => ({ line: null as string | null, message }));
  ctx.errors = [];
  const doc = ctx.byId.get(documentId);
  if (!doc) return [...result, { line: null, message: `unknown document '${documentId}'` }];
  for (const line of doc.lines) {
    const start = ctx.errors.length;
    try { checkLine(ctx, doc, line); }
    catch { ctx.errors.push(`${documentId}.${line.id}: malformed expression`); }
    result.push(...ctx.errors.slice(start).map(message => ({ line: line.id, message })));
  }
  return result;
}

export function runChecks(data: CanonicalData): { errors: string[]; stats: string[] } {
  const ctx = contextFor(data);
  const stats: string[] = [];

  for (const doc of [...data.forms, ...data.defs]) {
    for (const line of doc.lines) {
      if (!line.shown_when) continue;
      const cond = doc.lines.find((l) => l.id === line.shown_when);
      if (!cond || cond.type !== "Bool") ctx.errors.push(`${line.id}: shown_when ${line.shown_when} is not a Bool line of ${doc.id}`);
      if (line.printed.startsWith("(")) ctx.errors.push(`${line.id}: shown_when on a helper; only a printed line is shown or left out`);
    }
    if (doc.collection) {
      checkCite(ctx, doc.collection.cite, `${doc.id} collection`);
      if (doc.collection.implicit && !doc.collection.parent) ctx.errors.push(`${doc.id}: an implicit collection needs a parent (one entry per parent entry)`);
      if (doc.kind === "def") ctx.errors.push(`${doc.id}: def cannot be a collection`);
      const seen = new Set([doc.id]);
      let parent = doc.collection.parent;
      while (parent) {
        if (seen.has(parent)) { ctx.errors.push(`${doc.id}: collection parent cycle`); break; }
        seen.add(parent);
        const pd = ctx.byId.get(parent);
        if (!pd?.collection) { ctx.errors.push(`${doc.id}: missing collection parent ${parent}`); break; }
        parent = pd.collection.parent;
      }
    }
    for (const line of doc.lines) {
      for (const r of line.refuses ?? []) {
        if (r.when_known !== undefined && r.when_known !== true) ctx.errors.push(`${line.id}: when_known must be true or omitted`);
        const hit = requireRef(ctx, doc, r.when, line.id);
        if (hit && hit.line.type !== "Bool") ctx.errors.push(`${line.id}: refusal gate must be Bool`);
        checkCite(ctx, r.cite, `${line.id} refusal`);
      }
      if (line.ambiguity && !data.register.entries.some(e=>e.id===line.ambiguity)) ctx.errors.push(`${line.id}: unknown ambiguity`);
      checkLine(ctx, doc, line);
      checkCite(ctx, line.cite, `${doc.id}.${line.id}`);
    }
  }

  checkCycles(ctx, data);

  let chooseCount = 0;
  let guardCount = 0;
  for (const doc of [...data.forms, ...data.defs]) {
    for (const line of doc.lines) {
      if (line.expr.op === "choose") {
        chooseCount++;
        guardCount += line.expr.alternatives.length;
        analyzeGuards(ctx, doc, line);
      }
    }
  }

  checkParams(ctx);
  for (const table of data.tables) checkTable(ctx, table);
  for (const entry of data.register.entries) {
    checkCite(ctx, entry.cite, `register ${entry.id}`);
    if (!entry.text_at_issue || !entry.chosen || !entry.reason || entry.readings.length === 0) {
      ctx.errors.push(`register ${entry.id}: entry is incomplete`);
    }
  }

  const opHistogram = new Map<string, number>();
  let lineCount = 0;
  let opaqueCount = 0;
  let unimplemented = 0;
  for (const doc of [...data.forms, ...data.defs]) {
    for (const line of doc.lines) {
      lineCount++;
      opHistogram.set(line.expr.op, (opHistogram.get(line.expr.op) ?? 0) + 1);
      if (line.expr.op === "opaque") opaqueCount++;
      if (!IMPLEMENTED.has(line.expr.op) && line.expr.op !== "opaque") unimplemented++;
    }
  }
  stats.push(`lines checked: ${lineCount}`);
  stats.push(
    `atoms used: ${[...opHistogram.entries()]
      .sort((a, b) => (a[0] < b[0] ? -1 : 1))
      .map(([op, n]) => `${op} ${n}`)
      .join(", ")}`,
  );
  stats.push(`choose lines: ${chooseCount}; guards checked: ${guardCount}`);
  stats.push(`opaque escapes: ${opaqueCount} (share ${lineCount ? (opaqueCount / lineCount).toFixed(4) : "0"})`);
  if (unimplemented > 0) stats.push(`lines using not-yet-implemented atoms: ${unimplemented}`);

  return { errors: ctx.errors, stats };
}

// ---------------------------------------------------------------------------
// type helpers

function parseTy(ctx: Ctx, t: string, where: string): Ty {
  if (t === "Count") return { kind: "count" };
  if (t === "Dollars") return { kind: "money", nonneg: false };
  if (t === "NonNegDollars") return { kind: "money", nonneg: true };
  if (t === "Rate") return { kind: "rate" };
  if (t === "Bool") return { kind: "bool" };
  const m = /^Enum\(([a-z_]+)\)$/.exec(t);
  if (m && m[1]) {
    if (!ctx.enumValues.has(m[1])) ctx.errors.push(`${where}: unknown enum '${m[1]}'`);
    return { kind: "enum", name: m[1] };
  }
  ctx.errors.push(`${where}: unknown type '${t}'`);
  return { kind: "money", nonneg: false };
}

function tyMoney(nonneg: boolean): Ty {
  return { kind: "money", nonneg };
}

/** declared must be able to hold inferred (money widens NonNeg -> Dollars). */
function compatible(ctx: Ctx, declared: Ty, inferred: Ty, where: string): void {
  if (declared.kind === "money" && inferred.kind === "money") {
    if (declared.nonneg && !inferred.nonneg) {
      ctx.errors.push(`${where}: declared NonNegDollars but the expression does not prove non-negativity`);
    }
    return;
  }
  if (declared.kind !== inferred.kind) {
    ctx.errors.push(`${where}: declared ${declared.kind} but the expression produces ${inferred.kind}`);
  }
}

function paramEntryTy(entry: ParamEntry): Ty {
  if (entry.type === "Count") return { kind: "count" };
  if (entry.type === "Rate") return { kind: "rate" };
  if (entry.type === "Bool") return { kind: "bool" };
  const m = /^Enum\(([a-z_]+)\)$/.exec(entry.type);
  if (m && m[1]) return { kind: "enum", name: m[1] };
  if (typeof entry.value === "number") return tyMoney(entry.value >= 0);
  if (entry.value && typeof entry.value === "object") {
    const vals = Object.values(entry.value as Record<string, number>);
    return tyMoney(vals.length > 0 && vals.every((v) => v >= 0));
  }
  return tyMoney(false);
}

function checkCite(
  ctx: Ctx,
  cite: { doc: string; revision: string; locator: string; snapshot: string },
  where: string,
): void {
  if (!cite || cite.doc === "?" || cite.locator === "?") ctx.errors.push(`${where}: citation incomplete`);
  if (!/^[0-9a-f]{64}$/.test(cite?.snapshot ?? "")) ctx.errors.push(`${where}: citation has no snapshot hash`);
  if (!cite?.revision || cite.revision === "?") ctx.errors.push(`${where}: citation has no revision`);
}

// ---------------------------------------------------------------------------
// static reference resolution

function resolveRef(ctx: Ctx, from: FormDoc, ref: string): { doc: FormDoc; line: Line; index: number } | null {
  const lm = ctx.lineMaps.get(from.id);
  const direct = lm?.get(ref);
  if (direct) return { doc: from, ...direct };
  const dot = ref.indexOf(".");
  if (dot > 0) {
    const target = ctx.byId.get(ref.slice(0, dot));
    const hit = target && ctx.lineMaps.get(target.id)?.get(ref);
    if (target && hit) return { doc: target, ...hit };
  }
  return null;
}

/** Whether collection `docId` encloses `from` (is its parent, or a parent's parent, ...). */
function encloses(ctx: Ctx, docId: string, from: FormDoc): boolean {
  let parent = from.collection?.parent;
  const seen = new Set<string>();
  while (parent && !seen.has(parent)) {
    if (parent === docId) return true;
    seen.add(parent);
    parent = ctx.byId.get(parent)?.collection?.parent;
  }
  return false;
}

function requireRef(ctx: Ctx, from: FormDoc, ref: string, where: string): { doc: FormDoc; line: Line; index: number } | null {
  const hit = resolveRef(ctx, from, ref);
  if (hit?.doc.collection && hit.doc.id !== from.id && !encloses(ctx, hit.doc.id, from)) {
    ctx.errors.push(`${where}: collection reference requires sum_over`);
    return null;
  }
  if (!hit) {
    ctx.errors.push(`${where}: reference '${ref}' does not resolve`);
    return null;
  }
  return hit;
}

function declaredTyOf(ctx: Ctx, doc: FormDoc, line: Line): Ty {
  return parseTy(ctx, line.type, `${doc.id}.${line.id}`);
}

function operandTyOf(ctx: Ctx, from: FormDoc, op: Operand, where: string): Ty {
  if (typeof op === "string") {
    const hit = requireRef(ctx, from, op, where);
    return hit ? declaredTyOf(ctx, hit.doc, hit.line) : tyMoney(false);
  }
  if ("const" in op && op.type === "Count") {
    if (typeof op.const !== "number" || !Number.isSafeInteger(op.const) || op.const < 0) ctx.errors.push(`${where}: invalid Count literal`);
    return { kind: "count" };
  }
  if ("param" in op) {
    const entry = ctx.params.values[op.param];
    if (!entry) {
      ctx.errors.push(`${where}: parameter '${op.param}' does not exist`);
      return tyMoney(false);
    }
    return paramEntryTy(entry);
  }
  const v = op.const;
  if (typeof v === "number" && !Number.isSafeInteger(v)) ctx.errors.push(`${where}: literal must be an exact integer`);
  if (typeof v === "number") return tyMoney(false);
  if (typeof v === "boolean") return { kind: "bool" };
  return { kind: "enum", name: "" }; // string constants are matched in checkTestType
}

// ---------------------------------------------------------------------------
// per-line checks

function checkLine(ctx: Ctx, doc: FormDoc, line: Line): void {
  const where = `${doc.id}.${line.id}`;
  const expr = line.expr as Expr;
  if (!VOCABULARY.includes(expr.op as (typeof VOCABULARY)[number])) {
    ctx.errors.push(`${where}: '${expr.op}' is not in the atom vocabulary`);
    return;
  }
  if (!IMPLEMENTED.has(expr.op)) {
    ctx.errors.push(`${where}: atom '${expr.op}' is not implemented in this stage`);
  }
  const declared = declaredTyOf(ctx, doc, line);

  switch (expr.op) {
    case "input": {
      if (!expr.source) ctx.errors.push(`${where}: input has no source`);
      break;
    }
    case "copy": {
      if (typeof expr.from === "string") {
        const hit = requireRef(ctx, doc, expr.from, where);
        if (hit) compatible(ctx, declared, declaredTyOf(ctx, hit.doc, hit.line), where);
      } else {
        const resultTy = checkInstance(ctx, doc, expr.from, where);
        if (resultTy) compatible(ctx, declared, resultTy, where);
      }
      break;
    }
    case "param": {
      const entry = ctx.params.values[expr.ref];
      if (!entry) {
        ctx.errors.push(`${where}: parameter '${expr.ref}' does not exist`);
      } else {
        compatible(ctx, declared, paramEntryTy(entry), where);
      }
      break;
    }
    case "sum_over": {
      const entry = ctx.byId.get(expr.collection);
      if (!entry?.collection) { ctx.errors.push(`${where}: unknown collection ${expr.collection}`); break; }
      if (entry.collection.parent !== (doc.collection ? doc.id : undefined)) ctx.errors.push(`${where}: collection parent binding mismatch`);
      const field = requireRef(ctx, entry, expr.field, where);
      if (field) {
        if (field.doc.id !== entry.id) ctx.errors.push(`${where}: sum_over field must belong to its collection`);
        const ty = declaredTyOf(ctx, field.doc, field.line);
        if (ty.kind !== "money" && ty.kind !== "count") ctx.errors.push(`${where}: sum_over field must be money or Count`);
        compatible(ctx, declared, ty, where);
      }
      if (expr.where) checkTestType(ctx, entry, expr.where, where);
      break;
    }
    case "sum": {
      if (expr.of.length === 0) ctx.errors.push(`${where}: sum of nothing`);
      let allNonneg = true;
      for (const ref of expr.of) {
        const hit = requireRef(ctx, doc, ref, where);
        if (hit) {
          const ty = declaredTyOf(ctx, hit.doc, hit.line);
          if (ty.kind !== "money") ctx.errors.push(`${where}: sum operand '${ref}' is not money`);
          allNonneg = allNonneg && ty.kind === "money" && ty.nonneg;
        }
      }
      compatible(ctx, declared, tyMoney(allNonneg), where);
      break;
    }
    case "subtract":
    case "subtract_floor0": {
      const hit = requireRef(ctx, doc, expr.from, where);
      if (hit && declaredTyOf(ctx, hit.doc, hit.line).kind !== "money") {
        ctx.errors.push(`${where}: operand '${expr.from}' is not money`);
      }
      const takeTy = operandTyOf(ctx, doc, expr.take, where);
      if (takeTy.kind !== "money") ctx.errors.push(`${where}: operand is not money`);
      compatible(ctx, declared, tyMoney(expr.op === "subtract_floor0"), where);
      break;
    }
    case "larger_of":
    case "smaller_of": {
      let allNonneg = true;
      for (const ref of expr.of) {
        const hit = requireRef(ctx, doc, ref, where);
        if (hit) {
          const ty = declaredTyOf(ctx, hit.doc, hit.line);
          if (ty.kind !== "money") ctx.errors.push(`${where}: operand '${ref}' is not money`);
          allNonneg = allNonneg && ty.kind === "money" && ty.nonneg;
        }
      }
      compatible(ctx, declared, tyMoney(allNonneg), where);
      break;
    }
    case "multiply_rate": {
      const hit = requireRef(ctx, doc, expr.amount, where);
      let amountNonneg = false;
      if (hit) {
        const ty = declaredTyOf(ctx, hit.doc, hit.line);
        if (ty.kind !== "money") ctx.errors.push(`${where}: amount '${expr.amount}' is not money`);
        amountNonneg = ty.kind === "money" && ty.nonneg;
      }
      const rateTy = operandTyOf(ctx, doc, expr.rate, where);
      if (rateTy.kind !== "rate") ctx.errors.push(`${where}: rate operand is not a Rate`);
      compatible(ctx, declared, tyMoney(amountNonneg), where);
      break;
    }
    case "multiply_count": {
      const hit = requireRef(ctx, doc, expr.amount, where);
      let amountNonneg = false;
      if (hit) {
        const ty = declaredTyOf(ctx, hit.doc, hit.line);
        if (ty.kind !== "money") ctx.errors.push(`${where}: amount '${expr.amount}' is not money`);
        amountNonneg = ty.kind === "money" && ty.nonneg;
      }
      const chit = requireRef(ctx, doc, expr.count, where);
      if (chit && declaredTyOf(ctx, chit.doc, chit.line).kind !== "count") ctx.errors.push(`${where}: count '${expr.count}' is not a Count`);
      compatible(ctx, declared, tyMoney(amountNonneg), where);
      break;
    }
    case "prorate": {
      const hit = requireRef(ctx, doc, expr.amount, where);
      let amountNonneg = false;
      if (hit) {
        const ty = declaredTyOf(ctx, hit.doc, hit.line);
        if (ty.kind !== "money") ctx.errors.push(`${where}: amount '${expr.amount}' is not money`);
        amountNonneg = ty.kind === "money" && ty.nonneg;
      }
      const phit = requireRef(ctx, doc, expr.part, where);
      if (phit && declaredTyOf(ctx, phit.doc, phit.line).kind !== "money") ctx.errors.push(`${where}: part '${expr.part}' is not money`);
      if (operandTyOf(ctx, doc, expr.whole, where).kind !== "money") ctx.errors.push(`${where}: whole operand is not money`);
      if (!Number.isInteger(expr.places) || expr.places < 0 || expr.places > 9) ctx.errors.push(`${where}: places must be a whole number from 0 to 9`);
      compatible(ctx, declared, tyMoney(amountNonneg), where);
      break;
    }
    case "round": {
      const hit = requireRef(ctx, doc, expr.of, where);
      let nonneg = false;
      if (hit) {
        const ty = declaredTyOf(ctx, hit.doc, hit.line);
        if (ty.kind !== "money") ctx.errors.push(`${where}: round operand '${expr.of}' is not money`);
        nonneg = ty.kind === "money" && ty.nonneg;
      }
      if (!(Number.isInteger(expr.unit) && expr.unit > 0)) ctx.errors.push(`${where}: round unit must be a positive integer number of cents`);
      if (!["half_up", "up", "down"].includes(expr.rule)) ctx.errors.push(`${where}: round rule must be half_up, up or down`);
      compatible(ctx, declared, tyMoney(nonneg), where);
      break;
    }
    case "keyed_lookup": {
      const table = ctx.tables.get(expr.table);
      if (!table) { ctx.errors.push(`${where}: table '${expr.table}' does not exist`); break; }
      if (table.kind !== "keyed") { ctx.errors.push(`${where}: '${expr.table}' is not a keyed table`); break; }
      const keys = table.keys ?? [];
      if (expr.keys.length !== keys.length) ctx.errors.push(`${where}: table '${expr.table}' has ${keys.length} keys, the lookup gives ${expr.keys.length}`);
      expr.keys.forEach((ref, i) => {
        const hit = requireRef(ctx, doc, ref, where);
        const want = keys[i];
        if (!hit || !want) return;
        const got = declaredTyOf(ctx, hit.doc, hit.line);
        const exp = parseTy(ctx, want.type, `table ${table.id} key ${want.name}`);
        if (got.kind !== exp.kind || (got.kind === "enum" && exp.kind === "enum" && got.name !== exp.name)) {
          ctx.errors.push(`${where}: key '${ref}' is ${got.kind === "enum" ? `Enum(${got.name})` : got.kind}, table key '${want.name}' is ${want.type}`);
        }
      });
      const cell = parseTy(ctx, table.cell ?? "", `table ${table.id} cell`);
      if (cell.kind === "enum" || cell.kind === "count" || cell.kind === "rate") {
        if (declared.kind !== cell.kind || (declared.kind === "enum" && cell.kind === "enum" && declared.name !== cell.name)) {
          ctx.errors.push(`${where}: declared type does not match the table's cell type ${table.cell}`);
        }
      } else compatible(ctx, declared, cell, where);
      break;
    }
    case "rate_lookup": {
      const table = ctx.tables.get(expr.table);
      if (!table) { ctx.errors.push(`${where}: table '${expr.table}' does not exist`); break; }
      if (table.kind !== "rate_bands") { ctx.errors.push(`${where}: '${expr.table}' is not a rate table`); break; }
      const key = requireRef(ctx, doc, expr.key, where);
      if (key && declaredTyOf(ctx, key.doc, key.line).kind !== "money") ctx.errors.push(`${where}: lookup key is not money`);
      if (table.columns && table.columns.length > 0) {
        if (expr.status === undefined) ctx.errors.push(`${where}: table '${expr.table}' has filing-status columns, the lookup gives no status`);
        else {
          const status = requireRef(ctx, doc, expr.status, where);
          if (status) {
            const ty = declaredTyOf(ctx, status.doc, status.line);
            if (ty.kind !== "enum" || ty.name !== "filing_status") ctx.errors.push(`${where}: status operand is not Enum(filing_status)`);
          }
        }
      } else if (expr.status !== undefined) ctx.errors.push(`${where}: table '${expr.table}' has one column, the lookup gives a status`);
      if (declared.kind !== "rate") ctx.errors.push(`${where}: a rate lookup's line must be declared Rate`);
      break;
    }
    case "table_lookup": {
      const table = ctx.tables.get(expr.table);
      if (!table) ctx.errors.push(`${where}: table '${expr.table}' does not exist`);
      else if (table.kind !== "tax_table") ctx.errors.push(`${where}: '${expr.table}' is not a tax table`);
      const key = requireRef(ctx, doc, expr.key, where);
      if (key && declaredTyOf(ctx, key.doc, key.line).kind !== "money") {
        ctx.errors.push(`${where}: lookup key is not money`);
      }
      const status = requireRef(ctx, doc, expr.status, where);
      if (status) {
        const ty = declaredTyOf(ctx, status.doc, status.line);
        if (ty.kind !== "enum") {
          ctx.errors.push(`${where}: status operand is not an enum`);
        } else {
          const values = ctx.enumValues.get(ty.name) ?? [];
          const covered = new Set((table?.columns ?? []).flatMap((c) => c.statuses));
          for (const v of values) {
            if (!covered.has(v)) ctx.errors.push(`${where}: table '${expr.table}' has no column for status '${v}'`);
          }
        }
      }
      const min = Math.min(...(table?.bands?.length ? table.bands.map((b) => Math.min(...b.tax)) : [0]));
      compatible(ctx, declared, tyMoney(min >= 0), where);
      break;
    }
    case "choose": {
      if (expr.alternatives.length === 0) ctx.errors.push(`${where}: choose with no alternatives`);
      let allNonneg = true;
      for (const alt of expr.alternatives) {
        checkTestType(ctx, doc, alt.guard, where);
        if (typeof alt.then === "string") {
          const hit = requireRef(ctx, doc, alt.then, where);
          if (hit) {
            const ty = declaredTyOf(ctx, hit.doc, hit.line);
            if (ty.kind !== "money") ctx.errors.push(`${where}: choose branch '${alt.then}' is not money`);
            allNonneg = allNonneg && ty.kind === "money" && ty.nonneg;
          }
        } else {
          const ty = checkInstance(ctx, doc, alt.then, where);
          if (ty && ty.kind !== "money") ctx.errors.push(`${where}: choose branch is not money`);
          // An instance's result has its def line's declared type, which the def's own check proves.
          allNonneg = allNonneg && ty !== null && ty.kind === "money" && ty.nonneg;
        }
      }
      compatible(ctx, declared, tyMoney(allNonneg), where);
      break;
    }
    case "test": {
      checkTestType(ctx, doc, expr as TestExpr, where);
      compatible(ctx, declared, { kind: "bool" }, where);
      break;
    }
    default: {
      ctx.errors.push(`${where}: atom '${expr.op}' has no checker support in this stage`);
    }
  }
}

function checkInstance(
  ctx: Ctx,
  from: FormDoc,
  inst: { def: string; bind: Record<string, Operand>; line: string },
  where: string,
): Ty | null {
  const def = ctx.byId.get(inst.def);
  if (!def || def.kind !== "def") {
    ctx.errors.push(`${where}: instance def '${inst.def}' does not exist`);
    return null;
  }
  const params = def.parameters ?? [];
  const bindKeys = Object.keys(inst.bind).sort();
  if (stableStringify(bindKeys) !== stableStringify([...params].sort())) {
    ctx.errors.push(`${where}: instance of '${inst.def}' must bind exactly [${params.join(", ")}]`);
  }
  const lm = ctx.lineMaps.get(def.id);
  for (const [name, op] of Object.entries(inst.bind)) {
    const paramLine = lm?.get(name)?.line;
    const opTy = operandTyOf(ctx, from, op, `${where} (binding ${name})`);
    if (paramLine) {
      compatible(ctx, declaredTyOf(ctx, def, paramLine), opTy, `${where} (binding ${name})`);
    }
  }
  const result = lm?.get(inst.line)?.line;
  if (!result) {
    ctx.errors.push(`${where}: '${inst.def}' has no line '${inst.line}'`);
    return null;
  }
  return declaredTyOf(ctx, def, result);
}

// ---------------------------------------------------------------------------
// test typing

function checkTestType(ctx: Ctx, doc: FormDoc, test: TestExpr, where: string): void {
  if ("all" in test) {
    if (test.all.length === 0) ctx.errors.push(`${where}: empty all`);
    for (const t of test.all) checkTestType(ctx, doc, t, where);
    return;
  }
  if ("any" in test) {
    if (test.any.length === 0) ctx.errors.push(`${where}: empty any`);
    for (const t of test.any) checkTestType(ctx, doc, t, where);
    return;
  }
  if ("not" in test) {
    checkTestType(ctx, doc, test.not, where);
    return;
  }
  const cmp = ["eq", "ne", "lt", "le", "gt", "ge"].find((k) => (test as Record<string, unknown>)[k] !== undefined);
  if (!cmp) {
    ctx.errors.push(`${where}: test has no comparison`);
    return;
  }
  const [a, b] = (test as unknown as Record<string, [Operand, Operand]>)[cmp]!;
  const at = operandTyOf(ctx, doc, a, where);
  const bt = operandTyOf(ctx, doc, b, where);
  if (at.kind === "count" && bt.kind === "count") return;
  if (at.kind === "money" && bt.kind === "money") return;
  if (at.kind === "bool" && bt.kind === "bool") return;
  if (at.kind === "enum" && bt.kind === "enum") {
    if (at.name !== "" && bt.name !== "" && at.name !== bt.name) {
      ctx.errors.push(`${where}: comparing different enum types`);
    }
    return;
  }
  ctx.errors.push(`${where}: comparison operands have incompatible types`);
}

// ---------------------------------------------------------------------------
// cycles (expanded over def instances)

interface Frame {
  doc: FormDoc;
  instKey: string | null;
  bind: Record<string, Operand> | null;
  caller: Frame | null;
}

function checkCycles(ctx: Ctx, data: CanonicalData): void {
  const WHITE = 0,
    GRAY = 1,
    BLACK = 2;
  const color = new Map<string, number>();
  const stack: string[] = [];
  const emit = (msg: string) => ctx.errors.push(msg);

  const collectRefs = (
    expr: Expr,
  ): { refs: string[]; operands: Operand[]; instances: { def: string; bind: Record<string, Operand>; line: string }[] } => {
    const refs: string[] = [];
    const operands: Operand[] = [];
    const instances: { def: string; bind: Record<string, Operand>; line: string }[] = [];
    const testOps = (test: TestExpr): void => {
      if ("all" in test) test.all.forEach(testOps);
      else if ("any" in test) test.any.forEach(testOps);
      else if ("not" in test) testOps(test.not);
      else for (const k of ["eq", "ne", "lt", "le", "gt", "ge"]) {
        const pair = (test as unknown as Record<string, Operand[]>)[k];
        if (pair) operands.push(...pair);
      }
    };
    switch (expr.op) {
      case "test": testOps(expr); break;
      case "sum":
      case "larger_of":
      case "smaller_of":
        refs.push(...expr.of);
        break;
      case "subtract":
      case "subtract_floor0":
        refs.push(expr.from);
        operands.push(expr.take);
        break;
      case "multiply_rate":
        refs.push(expr.amount);
        operands.push(expr.rate);
        break;
      case "round":
        refs.push(expr.of);
        break;
      case "multiply_count":
        refs.push(expr.amount, expr.count);
        break;
      case "prorate":
        refs.push(expr.amount, expr.part);
        operands.push(expr.whole);
        break;
      case "table_lookup":
        refs.push(expr.key, expr.status);
        break;
      case "keyed_lookup":
        refs.push(...expr.keys);
        break;
      case "rate_lookup":
        refs.push(expr.key, ...(expr.status ? [expr.status] : []));
        break;
      case "copy":
        if (typeof expr.from === "string") refs.push(expr.from);
        else instances.push({ def: expr.from.def, bind: expr.from.bind, line: expr.from.line });
        break;
      case "choose":
        for (const alt of expr.alternatives) {
          testOps(alt.guard);
          if (typeof alt.then === "string") refs.push(alt.then);
          else instances.push({ def: alt.then.def, bind: alt.then.bind, line: alt.then.line });
        }
        break;
      default:
        break;
    }
    return { refs, operands, instances };
  };

  const visitRef = (frame: Frame, ref: string): void => {
    const lm = ctx.lineMaps.get(frame.doc.id);
    if (lm?.has(ref)) {
      if (frame.instKey && (frame.doc.parameters ?? []).includes(ref) && frame.bind && frame.caller) {
        const op = frame.bind[ref];
        if (op !== undefined) visitOperand(frame.caller, op);
        return;
      }
      visitNode(frame, ref);
      return;
    }
    const dot = ref.indexOf(".");
    if (dot > 0) {
      const target = ctx.byId.get(ref.slice(0, dot));
      if (target && ctx.lineMaps.get(target.id)?.has(ref)) {
        visitNode({ doc: target, instKey: null, bind: null, caller: null }, ref);
        return;
      }
    }
    emit(`cycle walk: unresolved reference '${ref}'`);
  };

  const visitOperand = (frame: Frame, op: Operand): void => {
    if (typeof op === "string") visitRef(frame, op);
  };

  const visitNode = (frame: Frame, lineId: string): void => {
    const node = `${frame.instKey ?? frame.doc.id}.${lineId}`;
    const c = color.get(node) ?? WHITE;
    if (c === BLACK) return;
    if (c === GRAY) {
      const at = stack.indexOf(node);
      emit(`cycle: ${[...stack.slice(at), node].join(" -> ")}`);
      return;
    }
    color.set(node, GRAY);
    stack.push(node);
    const line = ctx.lineMaps.get(frame.doc.id)?.get(lineId)?.line;
    if (line) {
      const { refs, operands, instances } = collectRefs(line.expr as Expr);
      refs.push(...(line.refuses ?? []).map(r => r.when));
      if (line.expr.op === "sum_over") {
        const expr = line.expr;
        const entry = ctx.byId.get(expr.collection);
        if (entry) {
          const inner: Frame = { doc: entry, instKey: null, bind: null, caller: null };
          visitRef(inner, expr.field);
          if (expr.where) for (const op of collectRefs(expr.where).operands) visitOperand(inner, op);
        }
      }
      for (const ref of refs) visitRef(frame, ref);
      for (const op of operands) visitOperand(frame, op);
      for (const inst of instances) {
        const def = ctx.byId.get(inst.def);
        if (!def) continue;
        if (stack.some(n => n.includes(`inst:${inst.def}#`))) { emit(`recursive def ${inst.def}`); continue; }
        const key = `${frame.instKey ?? "root"}|inst:${inst.def}#${stableStringify(inst.bind).trim()}`;
        const inner: Frame = { doc: def, instKey: key, bind: inst.bind, caller: frame };
        for (const defLine of def.lines) visitNode(inner, defLine.id);
      }
    }
    stack.pop();
    color.set(node, BLACK);
  };

  for (const doc of [...data.forms, ...data.defs]) {
    if (doc.kind === "def") continue; // defs are visited through their instances
    const frame: Frame = { doc, instKey: null, bind: null, caller: null };
    for (const line of doc.lines) visitNode(frame, line.id);
  }
}

// ---------------------------------------------------------------------------
// guards

interface BoolG {
  kind: "bool";
  ref: string;
  value: boolean;
}
interface EnumG {
  kind: "enum";
  ref: string;
  value: string;
}
interface IntervalG {
  kind: "interval";
  ref: string;
  lo: number | undefined;
  loInc: boolean;
  hi: number | undefined;
  hiInc: boolean;
}

function analyzeGuards(ctx: Ctx, doc: FormDoc, line: Line): void {
  const where = `${doc.id}.${line.id}`;
  const expr = line.expr as Extract<Expr, { op: "choose" }>;
  const parsed = expr.alternatives.map((alt) => parseGuard(ctx, doc, alt.guard));
  if (parsed.some((g) => g === null)) {
    ctx.errors.push(`${where}: guard form not analyzable (supported: Bool pairs, Enum coverage, interval tiling)`);
    return;
  }
  const guards = parsed as (BoolG | EnumG | IntervalG)[];
  const kinds = new Set(guards.map((g) => g.kind));
  if (kinds.size !== 1) {
    ctx.errors.push(`${where}: guards mix kinds (${[...kinds].join(", ")})`);
    return;
  }

  if (kinds.has("bool")) {
    const refs = new Set(guards.map((g) => (g as BoolG).ref));
    if (refs.size !== 1) {
      ctx.errors.push(`${where}: Bool guards reference different lines`);
      return;
    }
    const values = (guards as BoolG[]).map((g) => g.value).sort();
    if (values.length !== 2 || values[0] !== false || values[1] !== true) {
      ctx.errors.push(`${where}: Bool guards are not exhaustive and disjoint`);
    }
    return;
  }

  if (kinds.has("enum")) {
    const refs = new Set(guards.map((g) => (g as EnumG).ref));
    if (refs.size !== 1) {
      ctx.errors.push(`${where}: enum guards reference different lines`);
      return;
    }
    const ref = [...refs][0]!;
    const hit = resolveRef(ctx, doc, ref);
    const ty = hit ? declaredTyOf(ctx, hit.doc, hit.line) : null;
    const name = ty && ty.kind === "enum" ? ty.name : null;
    const expected = name ? ctx.enumValues.get(name) ?? [] : [];
    if (!name) ctx.errors.push(`${where}: enum guard reference '${ref}' is not an enum line`);
    const seen = (guards as EnumG[]).map((g) => g.value);
    if (new Set(seen).size !== seen.length) ctx.errors.push(`${where}: enum guards duplicate a value`);
    for (const v of seen) {
      if (!expected.includes(v)) ctx.errors.push(`${where}: enum guard '${v}' is not a member`);
    }
    for (const v of expected) {
      if (!seen.includes(v)) ctx.errors.push(`${where}: enum guards are missing value '${v}'`);
    }
    return;
  }

  const refs = new Set(guards.map((g) => (g as IntervalG).ref));
  if (refs.size !== 1) {
    ctx.errors.push(`${where}: interval guards reference different lines`);
    return;
  }
  const ivs = (guards as IntervalG[]).map((g) => ({ ...g })).sort((a, b) => (a.lo ?? -Infinity) - (b.lo ?? -Infinity));
  if (ivs[0]!.lo === undefined) {
    ctx.errors.push(`${where}: interval guards start at -infinity`);
    return;
  }
  for (let i = 0; i < ivs.length; i++) {
    const g = ivs[i]!;
    if (g.lo !== undefined && g.hi !== undefined && g.lo >= g.hi) {
      ctx.errors.push(`${where}: interval guard ${i + 1} is empty`);
      continue;
    }
    const next = ivs[i + 1];
    if (!next) {
      if (g.hi !== undefined) ctx.errors.push(`${where}: interval guards do not reach +infinity`);
      break;
    }
    if (g.hi === undefined) {
      ctx.errors.push(`${where}: interval guard ${i + 1} has no upper bound but is not last`);
      break;
    }
    if (g.hi !== next.lo) {
      ctx.errors.push(`${where}: gap or overlap between interval guards ${i + 1} and ${i + 2}`);
      break;
    }
    // Exactly one side of a seam includes the seam point: [lo, hi) then [hi, ...),
    // or (lo, hi] then (hi, ...] as the Tax Computation Worksheet's "not over" rows read.
    if (g.hiInc === next.loInc) {
      ctx.errors.push(`${where}: interval guards ${i + 1}/${i + 2} ${g.hiInc ? "both include" : "both exclude"} the seam point`);
      break;
    }
  }
}

function parseGuard(ctx: Ctx, doc: FormDoc, test: TestExpr): BoolG | EnumG | IntervalG | null {
  if ("not" in test) {
    const inner = parseGuard(ctx, doc, test.not);
    if (inner && inner.kind === "bool") return { ...inner, value: !inner.value };
    return null;
  }
  if ("all" in test) {
    let combined: { ref: string; lo: number | undefined; loInc: boolean; hi: number | undefined; hiInc: boolean } | null =
      null;
    for (const part of test.all) {
      const piece = cmpToInterval(ctx, part);
      if (!piece) return null;
      if (!combined) combined = piece;
      else if (combined.ref !== piece.ref) return null;
      else {
        combined.lo = piece.lo !== undefined ? piece.lo : combined.lo;
        combined.loInc = piece.lo !== undefined ? piece.loInc : combined.loInc;
        combined.hi = piece.hi !== undefined ? piece.hi : combined.hi;
        combined.hiInc = piece.hi !== undefined ? piece.hiInc : combined.hiInc;
      }
    }
    if (!combined) return null;
    return { kind: "interval", ...combined };
  }
  if ("any" in test) return null;
  const key = (["eq", "ne", "lt", "le", "gt", "ge"] as const).find(
    (k) => (test as Record<string, unknown>)[k] !== undefined,
  );
  if (key === "ge" || key === "gt" || key === "le" || key === "lt") {
    const piece = cmpToInterval(ctx, test);
    return piece ? { kind: "interval", ...piece } : null;
  }
  if (key !== "eq") return null;
  const [a, b] = (test as unknown as Record<string, [Operand, Operand]>).eq!;
  const ref = typeof a === "string" ? a : typeof b === "string" ? (b as string) : null;
  const con: Operand | undefined = typeof a === "string" ? b : a;
  if (!ref || con === undefined || typeof con !== "object" || !("const" in con)) return null;
  if (typeof con.const === "boolean") return { kind: "bool", ref, value: con.const };
  if (typeof con.const === "string") return { kind: "enum", ref, value: con.const };
  return null;
}

/** Map one ge/gt/le/lt comparison to an interval piece on a single reference. */
function cmpToInterval(
  ctx: Ctx,
  part: TestExpr,
): { ref: string; lo: number | undefined; loInc: boolean; hi: number | undefined; hiInc: boolean } | null {
  if (!("ge" in part || "gt" in part || "le" in part || "lt" in part)) return null;
  const key = (["ge", "gt", "le", "lt"] as const).find((k) => (part as Record<string, unknown>)[k] !== undefined)!;
  const [a, b] = (part as unknown as Record<string, [Operand, Operand]>)[key]!;
  const refLeft = typeof a === "string";
  const refRight = typeof b === "string";
  if (refLeft === refRight) return null; // both or neither are references
  const ref = (refLeft ? a : b) as string;
  const bound = boundNumber(ctx, refLeft ? b : a);
  if (bound === null) return null;
  let lo: number | undefined;
  let loInc = false;
  let hi: number | undefined;
  let hiInc = false;
  if (refLeft) {
    if (key === "ge") {
      lo = bound;
      loInc = true;
    } else if (key === "gt") {
      lo = bound;
      loInc = false;
    } else if (key === "le") {
      hi = bound;
      hiInc = true;
    } else {
      hi = bound;
      hiInc = false;
    }
  } else {
    if (key === "ge") {
      hi = bound;
      hiInc = true;
    } else if (key === "gt") {
      hi = bound;
      hiInc = false;
    } else if (key === "le") {
      lo = bound;
      loInc = true;
    } else {
      lo = bound;
      loInc = false;
    }
  }
  return { ref, lo, loInc, hi, hiInc };
}

function boundNumber(ctx: Ctx, op: Operand): number | null {
  if (typeof op === "string") return null; // line-vs-line bounds are not analyzable here
  if ("const" in op && typeof op.const === "number") return op.const;
  if ("param" in op) {
    const entry = ctx.params.values[op.param];
    if (entry && typeof entry.value === "number") return entry.value;
    return null;
  }
  return null;
}

// ---------------------------------------------------------------------------
// params and tables

function checkParams(ctx: Ctx): void {
  for (const [name, entry] of Object.entries(ctx.params.values)) {
    const where = `param ${name}`;
    if (entry.type === "Count") {
      if (typeof entry.value !== "number" || !Number.isSafeInteger(entry.value) || entry.value < 0) ctx.errors.push(`${where}: invalid Count`);
    } else if (entry.type === "Rate") {
      const r = entry.value as { num?: number; den?: number };
      if (typeof r?.num !== "number" || typeof r?.den !== "number" || r.den <= 0 || r.num < 0) {
        ctx.errors.push(`${where}: invalid rate`);
      }
    } else if (entry.type.includes("Enum(")) {
      const m = /^Enum\(([a-z_]+)\)$/.exec(entry.type);
      const values = m && m[1] ? ctx.enumValues.get(m[1]) : undefined;
      if (!values || !values.includes(String(entry.value))) {
        ctx.errors.push(`${where}: value '${String(entry.value)}' is not a member of the enum`);
      }
    } else if (entry.type === "Bool") {
      if (typeof entry.value !== "boolean") ctx.errors.push(`${where}: Bool value expected`);
    } else {
      if (typeof entry.value === "number") {
        if (!Number.isSafeInteger(entry.value)) ctx.errors.push(`${where}: money must be integer cents`);
      } else if (entry.value && typeof entry.value === "object") {
        for (const [status, v] of Object.entries(entry.value as Record<string, number>)) {
          if (!ctx.enumValues.get("filing_status")?.includes(status)) {
            ctx.errors.push(`${where}: unknown filing status key '${status}'`);
          }
          if (!Number.isSafeInteger(v)) ctx.errors.push(`${where}: money must be integer cents`);
        }
        for (const v of ctx.enumValues.get("filing_status") ?? []) {
          if (!(v in (entry.value as Record<string, number>))) ctx.errors.push(`${where}: missing value for '${v}'`);
        }
      } else {
        ctx.errors.push(`${where}: value is not money`);
      }
    }
  }
  for (const [name, en] of Object.entries(ctx.params.enums)) {
    checkCite(ctx, en.cite, `enum ${name}`);
    if (new Set(en.values).size !== en.values.length) ctx.errors.push(`enum ${name}: duplicate values`);
  }
}

function checkTable(ctx: Ctx, table: TableDoc): void {
  checkCite(ctx, table.cite, `table ${table.id}`);
  if (table.kind === "tax_table") {
    const cols = table.columns ?? [];
    const bands = table.bands ?? [];
    if (cols.length === 0 || bands.length === 0) {
      ctx.errors.push(`table ${table.id}: empty table`);
      return;
    }
    const statuses = ctx.enumValues.get("filing_status") ?? [];
    const covered = new Map<string, number>();
    cols.forEach((c) => c.statuses.forEach((s) => covered.set(s, (covered.get(s) ?? 0) + 1)));
    for (const s of statuses) {
      if (covered.get(s) !== 1) ctx.errors.push(`table ${table.id}: status '${s}' is covered ${covered.get(s) ?? 0} times`);
    }
    const start = table.bounds?.at_least ?? 0;
    if (bands[0]!.at_least !== start) ctx.errors.push(`table ${table.id}: first band does not start at ${start}`);
    for (let i = 0; i < bands.length; i++) {
      const b = bands[i]!;
      if (b.tax.length !== cols.length) {
        ctx.errors.push(`table ${table.id}: band ${i} has ${b.tax.length} values for ${cols.length} columns`);
      }
      if (!b.tax.every((v) => Number.isSafeInteger(v) && v >= 0)) {
        ctx.errors.push(`table ${table.id}: band ${i} has non-money values`);
      }
      const next = bands[i + 1];
      if (next && b.less_than !== next.at_least) {
        ctx.errors.push(`table ${table.id}: bands are not contiguous at band ${i}`);
        break;
      }
    }
    const last = bands[bands.length - 1]!;
    if (table.bounds) {
      if (last.less_than !== table.bounds.less_than) ctx.errors.push(`table ${table.id}: last band ends at ${last.less_than} but the table's bounds end at ${table.bounds.less_than}`);
    } else {
      const boundary = ctx.params.values["ordinary.table_boundary"]?.value;
      if (typeof boundary === "number" && last.less_than !== boundary) {
        ctx.errors.push(`table ${table.id}: last band ends at ${last.less_than} but ordinary.table_boundary is ${boundary}`);
      }
    }
  }
  if (table.kind === "rate_bands") {
    const bands = table.rate_bands ?? [];
    const cols = table.columns ?? [];
    if (bands.length === 0) { ctx.errors.push(`table ${table.id}: empty table`); return; }
    if (cols.length > 0) {
      const covered = new Map<string, number>();
      cols.forEach((c) => c.statuses.forEach((s) => covered.set(s, (covered.get(s) ?? 0) + 1)));
      for (const s of ctx.enumValues.get("filing_status") ?? []) {
        if (covered.get(s) !== 1) ctx.errors.push(`table ${table.id}: status '${s}' is covered ${covered.get(s) ?? 0} times`);
      }
      for (const s of covered.keys()) {
        if (!(ctx.enumValues.get("filing_status") ?? []).includes(s)) ctx.errors.push(`table ${table.id}: '${s}' is not a filing status`);
      }
    }
    const width = Math.max(cols.length, 1);
    if (bands[0]!.over !== null) ctx.errors.push(`table ${table.id}: the first band is not open below`);
    if (bands[bands.length - 1]!.not_over !== null) ctx.errors.push(`table ${table.id}: the last band is not open above`);
    bands.forEach((b, i) => {
      const at = `table ${table.id} band ${i}`;
      if (b.rates.length !== width) ctx.errors.push(`${at}: ${b.rates.length} rates for ${width} columns`);
      for (const r of b.rates) {
        if (!Number.isSafeInteger(r.num) || !Number.isSafeInteger(r.den) || r.den <= 0 || r.num < 0 || r.num > r.den) ctx.errors.push(`${at}: rate is not between 0 and 1`);
      }
      if (i > 0 && b.over === null) ctx.errors.push(`${at}: only the first band may be open below`);
      if (i < bands.length - 1 && b.not_over === null) ctx.errors.push(`${at}: only the last band may be open above`);
      if (b.over !== null && !Number.isSafeInteger(b.over)) ctx.errors.push(`${at}: 'over' is not an amount`);
      if (b.not_over !== null && !Number.isSafeInteger(b.not_over)) ctx.errors.push(`${at}: 'not over' is not an amount`);
      if (b.over !== null && b.not_over !== null && !(b.over < b.not_over)) ctx.errors.push(`${at}: 'over' is not below 'not over'`);
      const next = bands[i + 1];
      if (next && next.over !== b.not_over) ctx.errors.push(`${at}: bands are not contiguous`);
    });
  }
  if (table.kind === "keyed") {
    const keys = table.keys ?? [];
    const cell = parseTy(ctx, table.cell ?? "", `table ${table.id} cell`);
    const keyTys = keys.map((k) => parseTy(ctx, k.type, `table ${table.id} key ${k.name}`));
    const seen = new Set<string>();
    (table.rows ?? []).forEach((row, i) => {
      const at = `table ${table.id} row ${i}`;
      if (row.keys.length !== keys.length) { ctx.errors.push(`${at}: ${row.keys.length} keys for ${keys.length}`); return; }
      row.keys.forEach((k, j) => {
        const ty = keyTys[j]!;
        if (ty.kind === "count" && !(Number.isSafeInteger(k) && (k as number) >= 0)) ctx.errors.push(`${at}: key ${keys[j]!.name} is not a count`);
        if (ty.kind === "enum" && !(typeof k === "string" && (ctx.enumValues.get(ty.name) ?? []).includes(k))) ctx.errors.push(`${at}: key ${keys[j]!.name} '${k}' is not a value of ${ty.name}`);
      });
      const id = JSON.stringify(row.keys);
      if (seen.has(id)) ctx.errors.push(`${at}: duplicate keys ${id}`);
      seen.add(id);
      const v = row.value;
      if (cell.kind === "rate") {
        const r = v as { num?: number; den?: number };
        if (typeof v !== "object" || !Number.isSafeInteger(r.num) || !Number.isSafeInteger(r.den) || r.den! <= 0 || r.num! < 0 || r.num! > r.den!) ctx.errors.push(`${at}: rate is not between 0 and 1`);
      } else if (cell.kind === "money" || cell.kind === "count") {
        if (!Number.isSafeInteger(v) || ((cell.kind === "count" || cell.nonneg) && (v as number) < 0)) ctx.errors.push(`${at}: value is not a ${table.cell}`);
      } else if (cell.kind === "enum") {
        if (!(typeof v === "string" && (ctx.enumValues.get(cell.name) ?? []).includes(v))) ctx.errors.push(`${at}: value '${String(v)}' is not a value of ${cell.name}`);
      } else ctx.errors.push(`${at}: unsupported cell type ${table.cell}`);
    });
  }
  if (table.kind === "bracket_schedule") {
    const schedules = table.schedules ?? {};
    for (const [from, to] of Object.entries(table.status_alias ?? {})) {
      if (!ctx.enumValues.get("filing_status")?.includes(from)) {
        ctx.errors.push(`table ${table.id}: unknown status alias key '${from}'`);
      }
      if (!(to in schedules)) {
        ctx.errors.push(`table ${table.id}: alias '${from}' points at missing schedule '${to}'`);
      }
    }
    for (const s of ["single", "mfj", "mfs", "hoh"]) {
      const rows = schedules[s];
      if (!rows || rows.length === 0) {
        ctx.errors.push(`table ${table.id}: missing schedule '${s}'`);
        continue;
      }
      rows.forEach((row, i) => {
        const next = rows[i + 1];
        if (row.upper === null && next) ctx.errors.push(`table ${table.id}.${s}: null upper bound is not last`);
        if (row.upper !== null && next?.upper != null && row.upper >= next.upper) {
          ctx.errors.push(`table ${table.id}.${s}: bounds not increasing at row ${i}`);
        }
        if (!Number.isSafeInteger(row.base) || row.base < 0 || !Number.isSafeInteger(row.over)) {
          ctx.errors.push(`table ${table.id}.${s}: row ${i} has invalid amounts`);
        }
      });
    }
  }
}
