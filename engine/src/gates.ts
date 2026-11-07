// Gate conventions. A gated input is an input line
// marked `gated_by: <gate line>`; its gate line is a `choose` of the same document that reads it as the `then` of an
// alternative and has an else alternative of a parameter of the input's type: zero for money, false for a Bool, a
// designated value for an enum. The marker sits on the input because the
// rule protects the input: no line other than its gate may read it, so a reader added anywhere fails at the build.
import type { CanonicalData, Expr, FormDoc, Line } from "./types.js";

/** One gate line and the input it gates. `guardRefs` are the line references its guards read. */
export interface Gate { doc: string; line: string; input: string; guardRefs: string[] }

const NOT_REFS = new Set(["cite", "source", "label", "op", "ref", "def", "line"]);

/** Every string in an expression or test that can name a line (a parameter's `ref`, a def's id and its line, and
 * wording are left out). */
export function refsOf(node: unknown, out: Set<string> = new Set()): Set<string> {
  if (typeof node === "string") out.add(node);
  else if (Array.isArray(node)) for (const n of node) refsOf(n, out);
  else if (node && typeof node === "object") for (const [k, v] of Object.entries(node)) if (!NOT_REFS.has(k)) refsOf(v, out);
  return out;
}

/** The lines `line` reads: its expression's references (a `then` instance's binds included), its refusal gates and its
 * `shown_when`. */
export function readsOf(line: Line): Set<string> {
  const out = refsOf(line.expr);
  for (const r of line.refuses ?? []) out.add(r.when);
  if (line.shown_when) out.add(line.shown_when);
  return out;
}

export function gatesOf(data: CanonicalData): Gate[] {
  const gates: Gate[] = [];
  for (const doc of data.forms) for (const l of doc.lines) {
    if (!l.gated_by) continue;
    const gate = doc.lines.find((g) => g.id === l.gated_by);
    const guardRefs = gate?.expr.op === "choose"
      ? [...new Set((gate.expr as Extract<Expr, { op: "choose" }>).alternatives.flatMap((a) => [...refsOf(a.guard)]))].sort()
      : [];
    gates.push({ doc: doc.id, line: l.gated_by, input: l.id, guardRefs });
  }
  return gates;
}

/** The gate conventions over the data: each problem names the gated input. Guard exhaustiveness is not repeated here:
 * check.ts's guard analysis requires every `choose`'s guards to be exhaustive and disjoint, so an else alternative is
 * always reachable when the gate is false. `targets`: the interview targets, which must not read a gated input
 * either. */
export function gateProblems(data: CanonicalData, targets: string[] = []): string[] {
  const problems: string[] = [];
  const docs: FormDoc[] = [...data.forms, ...data.defs];
  const readers = new Map<string, string[]>();
  for (const d of docs) for (const l of d.lines) for (const r of readsOf(l)) {
    const list = readers.get(r) ?? [];
    list.push(l.id);
    readers.set(r, list);
  }
  const gateOf = new Map<string, string[]>();
  for (const d of data.defs) for (const l of d.lines) if (l.gated_by) problems.push(`${l.id}: gated_by on a definition line; only a form's input can be gated`);
  for (const doc of data.forms) for (const l of doc.lines) {
    if (!l.gated_by) continue;
    const where = `${l.id} (gated_by ${l.gated_by})`;
    if (l.expr.op !== "input") { problems.push(`${where}: only an input line can be gated`); continue; }
    (gateOf.get(l.gated_by) ?? gateOf.set(l.gated_by, []).get(l.gated_by)!).push(l.id);
    const gate = doc.lines.find((g) => g.id === l.gated_by);
    if (!gate) { problems.push(`${where}: no line ${l.gated_by} in document ${doc.id} (the gate line must be in the input's document)`); continue; }
    if (gate.expr.op !== "choose") { problems.push(`${where}: the gate line is a ${gate.expr.op}, not a choose`); continue; }
    const others = (readers.get(l.id) ?? []).filter((r) => r !== gate.id);
    if (others.length) problems.push(`${where}: read by ${others.sort().join(", ")}; a gated input is read only by its gate line`);
    if (targets.includes(l.id)) problems.push(`${where}: an interview target; a gated input is read only by its gate line`);
    const alts = (gate.expr as Extract<Expr, { op: "choose" }>).alternatives;
    if (alts.some((a) => refsOf(a.guard).has(l.id))) problems.push(`${where}: a guard of the gate reads the gated input`);
    if (!alts.some((a) => a.then === l.id)) problems.push(`${where}: no alternative of the gate takes the gated input as its then`);
    const elseAlt = alts.find((a) => typeof a.then === "string" && a.then !== l.id && isElseLine(data, doc, a.then, l.type));
    if (!elseAlt) problems.push(`${where}: the gate has no else alternative of ${ELSE_TEXT}`);
    for (const a of alts) {
      if (typeof a.then !== "string") problems.push(`${where}: an alternative of the gate is a definition instance; a gate's alternatives are the gated input and its else`);
      else if (a.then !== l.id && !isElseLine(data, doc, a.then, l.type)) problems.push(`${where}: alternative ${a.then} is neither the gated input nor ${ELSE_TEXT}`);
    }
  }
  for (const [gate, inputs] of gateOf) if (inputs.length > 1) problems.push(`${gate}: gates ${inputs.sort().join(", ")}; a gate line gates one input`);
  return problems;
}

const ELSE_TEXT = "a parameter of the input's type (zero for money, false for a Bool, an enum value for an enum)";

/** Whether `ref` names a line of `doc` (or another form) that is a parameter fit to be the else of a gated input of type
 * `type`: a money parameter of 0 for a money input; a Bool line on a false parameter for a Bool input; a line of the
 * input's enum type on a parameter of that enum (its value the designated else) for an enum input. */
function isElseLine(data: CanonicalData, doc: FormDoc, ref: string, type: string): boolean {
  const line = doc.lines.find((x) => x.id === ref) ?? data.forms.flatMap((d) => d.lines).find((x) => x.id === ref);
  if (!line || line.expr.op !== "param") return false;
  const p = data.params.values[(line.expr as { ref: string }).ref];
  if (p === undefined) return false;
  if (type === "Bool") return line.type === "Bool" && p.type === "Bool" && p.value === false;
  if (type.startsWith("Enum(")) return line.type === type && p.type === type && typeof p.value === "string";
  return (type === "Dollars" || type === "NonNegDollars") && p.value === 0 && (p.type === "Dollars" || p.type === "NonNegDollars");
}
