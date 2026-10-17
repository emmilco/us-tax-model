// Renderer: produce committed, human-readable renderings of the canonical
// data — each line's encoded English beside its IRS label and citation —
// plus the parameters, tables and ambiguity register.

import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fmtMoney, fmtRate, shortHash } from "./util.js";
import { loadCanonical } from "./canonical.js";
import type { CanonicalData, CiteFilled, Expr, FormDoc, Line, Operand, TestExpr } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const OUT = join(ROOT, "rendered", "2025");

interface RenderCtx {
  forms: Map<string, FormDoc>;
  params: CanonicalData["params"];
  tables: CanonicalData["tables"];
}

export function renderAll(): void {
  const data = loadCanonical();
  const ctx: RenderCtx = {
    forms: new Map([...data.forms, ...data.defs].map((d) => [d.id, d])),
    params: data.params,
    tables: data.tables,
  };

  rmSync(OUT, { recursive: true, force: true });
  mkdirSync(OUT, { recursive: true });

  for (const doc of [...data.forms, ...data.defs].sort((a, b) => (a.id < b.id ? -1 : 1))) {
    writeFileSync(join(OUT, `${doc.id}.md`), renderDoc(doc, ctx));
  }
  writeFileSync(join(OUT, "params.md"), renderParams(data.params));
  for (const table of data.tables) {
    writeFileSync(join(OUT, `${table.id}.md`), renderTable(table, ctx));
  }
  writeFileSync(join(OUT, "ambiguities.md"), renderRegister(data.register));
  writeFileSync(join(OUT, "index.md"), renderIndex(data));
  console.log(`rendered ${2 + 1 + 2 + 1 + data.forms.length + data.defs.length} files to rendered/2025/`);
}

// ---------------------------------------------------------------------------
// operand and expression rendering

function citeLine(cite: CiteFilled): string {
  return `[${cite.doc}] ${cite.locator} (${cite.revision}; sha256 ${shortHash(cite.snapshot)})`;
}

function operandText(op: Operand, doc: FormDoc, ctx: RenderCtx): string {
  if (typeof op === "string") return refText(doc, op, ctx);
  if ("param" in op) return paramText(op.param, ctx);
  if (op.type === "Count") return `${op.const} (a count)`;
  const v = op.const;
  if (typeof v === "boolean") return v ? "true" : "false";
  if (typeof v === "number") return fmtMoney(v);
  return `'${v}'`;
}

// Printed markers of lines that are not on the IRS page: helpers, gates and
// interview questions. They are named by their authored label, since the
// marker alone says nothing a reader could check.
const HELPER_MARKERS = new Set(["(helper)", "(gate)", "(computed helper)", "(question)", "(status)"]);

function lineName(line: Line, prefix: string, doc: FormDoc): string {
  if (HELPER_MARKERS.has(line.printed)) return `${prefix}helper "${line.label}"`;
  // A marker several lines share (a worksheet's repeated row columns) is
  // qualified by the line id, since the marker alone names no single line.
  const shared = doc.lines.filter((l) => l.printed === line.printed).length > 1;
  const marker = shared ? `${line.printed} (${line.id})` : line.printed;
  if (line.printed.startsWith("(")) return `${prefix}column ${marker}`;
  return `${prefix}line ${marker}`;
}

function refText(doc: FormDoc, ref: string, ctx: RenderCtx): string {
  // Same-document reference?
  const same = doc.lines.find((l) => l.id === ref);
  if (same) return lineName(same, "", doc);
  const dot = ref.indexOf(".");
  if (dot > 0) {
    const target = ctx.forms.get(ref.slice(0, dot));
    const line = target?.lines.find((l) => l.id === ref);
    if (target && line) return lineName(line, `${target.id} `, target);
  }
  return ref;
}

function paramValueText(value: unknown): string {
  if (typeof value === "number") return fmtMoney(value);
  if (typeof value === "boolean") return String(value);
  if (typeof value === "object" && value !== null && "num" in value && "den" in value) {
    return fmtRate(value as { num: number; den: number });
  }
  const order = ["single", "mfj", "mfs", "hoh", "qss"];
  return Object.entries(value as Record<string, number>)
    .sort((a, b) => order.indexOf(a[0]) - order.indexOf(b[0]))
    .map(([k, v]) => `${k} ${fmtMoney(v)}`)
    .join("; ");
}

function paramText(name: string, ctx: RenderCtx): string {
  const entry = ctx.params.values[name];
  if (!entry) return `parameter ${name} (missing)`;
  return `${entry.type === "Count" ? entry.value : paramValueText(entry.value)} (${name})`;
}

function testText(test: TestExpr, doc: FormDoc, ctx: RenderCtx): string {
  if ("all" in test) return test.all.map((t) => testText(t, doc, ctx)).join(" and ");
  if ("any" in test) return "(" + test.any.map((t) => testText(t, doc, ctx)).join(" or ") + ")";
  if ("not" in test) return `not ${testText(test.not, doc, ctx)}`;
  const syms: Record<string, string> = { eq: "=", ne: "≠", lt: "<", le: "≤", gt: ">", ge: "≥" };
  for (const [k, sym] of Object.entries(syms)) {
    const pair = (test as unknown as Record<string, [Operand, Operand] | undefined>)[k];
    if (pair) {
      const [a, b] = pair;
      const left = typeof a === "string" ? refText(doc, a, ctx) : operandText(a, doc, ctx);
      const right = typeof b === "string" ? refText(doc, b, ctx) : operandText(b, doc, ctx);
      return `${left} ${sym} ${right}`;
    }
  }
  return "(unrenderable test)";
}

function exprText(expr: Expr, doc: FormDoc, ctx: RenderCtx): string {
  switch (expr.op) {
    case "input":
      return `Input — ${expr.source}`;
    case "copy":
      if (typeof expr.from === "string") return `Enter the amount from ${refText(doc, expr.from, ctx)}.`;
      return `Enter "${expr.from.line}" of ${ctx.forms.get(expr.from.def)?.title ?? expr.from.def} with ${listAnd(Object.entries(expr.from.bind)
        .map(([k, v]) => `${k} = ${operandText(v, doc, ctx)}`))}.`;
    case "param":
      return `Enter ${paramText(expr.ref, ctx)}.`;
    case "sum_over":
      return `Add ${expr.field} over every confirmed ${expr.collection} entry${expr.where ? ` for which ${testText(expr.where, ctx.forms.get(expr.collection)!, ctx)}` : ""}, within the current person when parent-bound. An unanswered roster is unknown.`;
    case "sum":
      return `Add ${listAnd(expr.of.map((r) => refText(doc, r, ctx)))}.`;
    case "subtract":
      return `Subtract ${operandText(expr.take, doc, ctx)} from ${refText(doc, expr.from, ctx)}.`;
    case "subtract_floor0":
      return `Subtract ${operandText(expr.take, doc, ctx)} from ${refText(doc, expr.from, ctx)}. If zero or less, enter -0-.`;
    case "smaller_of":
      return `Enter the smaller of ${listOr(expr.of.map((r) => refText(doc, r, ctx)))}.`;
    case "larger_of":
      return `Enter the larger of ${listOr(expr.of.map((r) => refText(doc, r, ctx)))}.`;
    case "multiply_rate":
      return `Multiply ${refText(doc, expr.amount, ctx)} by ${operandText(expr.rate, doc, ctx)}.`;
    case "round": {
      const how = expr.rule === "up" ? "up to the next multiple of" : expr.rule === "down" ? "down to a multiple of" : "to the nearest multiple of (half up)";
      return `Round ${refText(doc, expr.of, ctx)} ${how} ${fmtMoney(expr.unit)}.`;
    }
    case "table_lookup": {
      const table = ctx.tables.find((t) => t.id === expr.table);
      return `Use ${table?.title ?? expr.table} at ${refText(doc, expr.key, ctx)} for the filing status (${refText(
        doc,
        expr.status,
        ctx,
      )}).`;
    }
    case "choose":
      return `Choose — ${expr.alternatives
        .map(
          (alt) =>
            `[${testText(alt.guard, doc, ctx)} → ${
              typeof alt.then === "string" ? refText(doc, alt.then, ctx) : `"${alt.then.line}" of ${ctx.forms.get(alt.then.def)?.title ?? alt.then.def} with ${listAnd(Object.entries(alt.then.bind).map(([k, v]) => `${k} = ${operandText(v, doc, ctx)}`))}`
            }]`,
        )
        .join(" ")}`;
    case "test":
      return testText(expr as TestExpr, doc, ctx);
    default:
      return `${expr.op} (not rendered)`;
  }
}

function listAnd(items: string[]): string {
  if (items.length <= 1) return items[0] ?? "";
  return `${items.slice(0, -1).join(", ")}${items.length > 2 ? "," : ""} and ${items[items.length - 1]}`;
}

function listOr(items: string[]): string {
  if (items.length <= 1) return items[0] ?? "";
  return `${items.slice(0, -1).join(", ")}${items.length > 2 ? "," : ""} or ${items[items.length - 1]}`;
}

// ---------------------------------------------------------------------------
// documents

function renderDoc(doc: FormDoc, ctx: RenderCtx): string {
  const out: string[] = [];
  out.push(`# ${doc.title}`);
  out.push("");
  out.push(`- Document: \`${doc.id}\` (${doc.kind}, tax year ${doc.tax_year})`);
  if (doc.collection) out.push(`- Collection: keyed entries${doc.collection.parent ? ` within ${doc.collection.parent}` : ""}; ${citeLine(doc.collection.cite)}`);
  if (doc.parameters?.length) out.push(`- Parameters: ${doc.parameters.join(", ")}`);
  if (doc.note) out.push(`- Note: ${doc.note}`);
  out.push("");
  for (const line of doc.lines) {
    out.push(`## ${line.printed} — \`${line.id}\``);
    out.push("");
    out.push(`- **${doc.collection && doc.kind === "worksheet" || line.printed.startsWith("(") ? "Authored helper label" : "IRS"}:** ${line.label}`);
    out.push(`- **Encoded (${line.type}):** ${exprText(line.expr as Expr, doc, ctx)}`);
    for (const r of line.refuses ?? []) out.push(`- **Refusal:** when ${r.when} is true, cannot complete ${r.form}. ${r.remedy} Cite: ${citeLine(r.cite)}`);
    if (line.ambiguity) out.push(`- Interpretation: ${line.ambiguity}`);
    if (line.note) out.push(`- Note: ${line.note}`);
    out.push(`- Expr: \`${JSON.stringify(line.expr)}\``);
    out.push(`- Cite: ${citeLine(line.cite)}`);
    out.push("");
  }
  return out.join("\n");
}

function renderParams(params: CanonicalData["params"]): string {
  const out: string[] = [];
  out.push(`# Parameters, tax year ${params.tax_year}`);
  out.push("");
  out.push("## Enums");
  out.push("");
  for (const [name, en] of Object.entries(params.enums)) {
    out.push(`- \`${name}\`: ${en.values.join(", ")} — ${citeLine(en.cite)}`);
  }
  out.push("");
  out.push("## Values");
  out.push("");
  out.push("| Parameter | Type | Value | Cite |");
  out.push("| --- | --- | --- | --- |");
  for (const [name, entry] of Object.entries(params.values).sort((a, b) => (a[0] < b[0] ? -1 : 1))) {
    out.push(`| \`${name}\` | ${entry.type} | ${entry.type === "Count" ? entry.value : paramValueText(entry.value)} | ${citeLine(entry.cite)} |`);
  }
  out.push("");
  return out.join("\n");
}

function renderTable(table: CanonicalData["tables"][number], ctx: RenderCtx): string {
  const out: string[] = [];
  out.push(`# ${table.title}`);
  out.push("");
  out.push(`- Table: \`${table.id}\` (${table.kind})`);
  out.push(`- Cite: ${citeLine(table.cite)}`);
  if (table.kind === "tax_table" && table.bands && table.columns) {
    out.push("");
    out.push(`Bands: ${table.bands.length}; columns: ${table.columns.map((c) => c.key).join(", ")}`);
    out.push("");
    out.push(`| At least | Less than | ${table.columns.map((c) => c.key).join(" | ")} |`);
    out.push(`| --- | --- |${table.columns.map(() => " --- |").join("")}`);
    for (const band of table.bands) {
      out.push(
        `| ${fmtMoney(band.at_least)} | ${fmtMoney(band.less_than)} | ${band.tax.map((t) => fmtMoney(t)).join(" | ")} |`,
      );
    }
    out.push("");
  }
  if (table.kind === "bracket_schedule" && table.schedules) {
    for (const [status, rows] of Object.entries(table.schedules)) {
      out.push("");
      out.push(`## ${status}`);
      out.push("");
      out.push("| Upper bound | Base | Rate | Of excess over |");
      out.push("| --- | --- | --- | --- |");
      for (const row of rows) {
        out.push(
          `| ${row.upper === null ? "—" : fmtMoney(row.upper)} | ${fmtMoney(row.base)} | ${fmtRate(row.rate)} | ${fmtMoney(
            row.over,
          )} |`,
        );
      }
    }
    out.push("");
  }
  return out.join("\n");
}

function renderRegister(register: CanonicalData["register"]): string {
  const out: string[] = [];
  out.push(`# Ambiguity register, tax year ${register.tax_year}`);
  out.push("");
  for (const entry of register.entries) {
    out.push(`## ${entry.id}`);
    out.push("");
    out.push(`- Text at issue: ${entry.text_at_issue}`);
    out.push(`- Candidate readings: ${entry.readings.join(" | ")}`);
    out.push(`- **Chosen:** ${entry.chosen}`);
    out.push(`- Reason: ${entry.reason}`);
    if (entry.status) out.push(`- Status: ${entry.status}`);
    out.push(`- Cite: ${citeLine(entry.cite)}`);
    out.push("");
  }
  return out.join("\n");
}

function renderIndex(data: CanonicalData): string {
  const out: string[] = [];
  out.push("# Rendered data — implemented stages");
  out.push("");
  out.push("Review these renderings line by line against the archived IRS sources in `sources/2025/`.");
  out.push("");
  out.push("| File | Kind | Lines |");
  out.push("| --- | --- | --- |");
  for (const doc of [...data.forms, ...data.defs].sort((a, b) => (a.id < b.id ? -1 : 1))) {
    out.push(`| ${doc.id}.md | ${doc.kind} | ${doc.lines.length} |`);
  }
  for (const table of data.tables) {
    out.push(`| ${table.id}.md | ${table.kind} | ${table.bands?.length ?? Object.keys(table.schedules ?? {}).length} rows |`);
  }
  out.push("| params.md | parameters | |");
  out.push("| ambiguities.md | register | |");
  out.push("");
  return out.join("\n");
}
