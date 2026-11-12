// What-if umbrella gates (`interview-length --what-if`): the questions each return would be asked if proposed umbrella
// gates were in the formal model, measured without changing the forms. An umbrella is a new Bool input whose false
// makes a group of inputs unreachable, under the conventions of the formal gates design (2026-11-06): each gated
// input keeps its id, a gate line `<input>_if_<umbrella>` (a `choose` on the umbrella, else a zero or false parameter)
// takes its place in every reader, and a roster is hidden by putting each line that reads its collection under the
// same `choose`. The gates are applied to a copy of the built data in memory; nothing is written to forms/.
//
// Each return is walked in today's order twice, as built and with the umbrellas, and the umbrella is answered as the
// filer of that return would answer it truthfully: yes when the return's walk as built answered any input it covers
// with something other than false, 0 or an empty roster (and only on a return whose walk asked one of them). Both
// walks must end with the same status, and the same values on a complete return or the same refusals on a refused
// one; a difference fails the run (it would mean the umbrella hides an input the return needs).
//
// The candidates are those of the umbrella gates design (2026-11-10); their wording there is the proposal,
// and the short labels here only name them.
import { questionTemplate, type InterviewData } from "./interview.js";
import { refsOf } from "./gates.js";
import type { CanonicalData, Expr, FormDoc, Line } from "./types.js";

export interface Umbrella {
  /** The new Bool input, `<doc>.<name>`. */
  id: string;
  label: string;
  /** Input templates (and `$roster`s) the umbrella's false makes unreachable. */
  covers: string[];
}

/** The candidates measured, by the design's names. */
export const UMBRELLAS: Umbrella[] = [
  { id: "s1.line8_any", label: "Any income for Schedule 1 line 8 (lines 8a to 8z)",
    covers: ["s1.gambling_winnings", "s1.cod_any", "s1.line8g", "s1.line8h", "s1.line8i", "s1.line8j", "s1.line8r", "s1.line8_other", "$oi8z"] },
  { id: "s1.part1_other_any", label: "Unemployment compensation or any income for Schedule 1 line 8",
    covers: ["s1.uc_paid", "s1.gambling_winnings", "s1.cod_any", "s1.line8g", "s1.line8h", "s1.line8i", "s1.line8j", "s1.line8r", "s1.line8_other", "$oi8z"] },
  { id: "sb.foreign_any", label: "Any foreign account, foreign financial asset, foreign trust or foreign corporation",
    covers: ["sb.fbar_required", "sb.form8938", "sb.line8", "sb.form5471"] },
  { id: "sb.foreign_wide_any", label: "Any foreign account, asset, trust or corporation, or excluded foreign income",
    covers: ["sb.fbar_required", "sb.form8938", "sb.line8", "sb.form5471", "sa.excluded_income"] },
  { id: "f1040.other_payments_any", label: "Federal tax withheld other than on a W-2, or any other payment toward 2025 tax",
    covers: ["f1040.line25b", "f1040.line25c_other", "f1040.line26", "s3.line10"] },
  { id: "f1040.withholding_other_any", label: "Federal tax withheld other than on a W-2 (survey B-4)",
    covers: ["f1040.line25b", "f1040.line25c_other"] },
  { id: "sd.carryovers_any", label: "A carryover into 2025 from an earlier year's return (capital loss, section 179, QBI loss)",
    covers: ["sd.carryover", "s179.line10", "qbi.carryforward"] },
  { id: "f5695.any", label: "Residential energy credits (Form 5695 Part I or Part II)",
    covers: ["f5695.part1_any", "f5695.part2_any"] },
  { id: "f2441.any", label: "Child and dependent care expenses or benefits (Form 2441)",
    covers: ["f2441.care", "f2441.benefits"] },
  { id: "s2.other_taxes_any", label: "Additional taxes this tool does not figure (merged Schedule 2 screens)",
    covers: ["s2.amt", "s2.other", "scope.other_line16", "person.x_other", "f8959.unsupported"] },
  { id: "s1.adjustments_any", label: "Educator expenses or student loan interest (Schedule 1 Part II items asked separately)",
    covers: ["person.educator_expenses", "sli.interest"] },
  { id: "s1a.any", label: "Tips, overtime or car loan interest (Schedule 1-A Parts II to IV)",
    covers: ["s1a.tips", "s1a.overtime", "s1a.carloan"] },
];

/** The umbrellas the design recommends landing, measured together. */
export const RECOMMENDED = ["s1.line8_any", "sb.foreign_any", "f1040.other_payments_any", "f5695.any", "sd.carryovers_any"];

/** Replaces every reference to `from` that `refsOf` would collect (the same keys are skipped). */
function replaceRef(node: unknown, from: string, to: string): unknown {
  if (typeof node === "string") return node === from ? to : node;
  if (Array.isArray(node)) return node.map((n) => replaceRef(n, from, to));
  if (node && typeof node === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(node)) out[k] = ["cite", "source", "label", "op", "ref", "def", "line"].includes(k) ? v : replaceRef(v, from, to);
    return out;
  }
  return node;
}

/** Whether an expression reads collection `name` anywhere. */
function readsCollection(node: unknown, name: string): boolean {
  if (Array.isArray(node)) return node.some((n) => readsCollection(n, name));
  if (node && typeof node === "object") return Object.entries(node).some(([k, v]) => (k === "collection" && v === name) || readsCollection(v, name));
  return false;
}

const isTrue = (ref: string, value: boolean) => ({ op: "test", eq: [ref, { const: value }] });

function gateExpr(umbrella: string, then: string, otherwise: string): Expr {
  return { op: "choose", alternatives: [{ guard: isTrue(umbrella, true), then }, { guard: isTrue(umbrella, false), then: otherwise }] } as unknown as Expr;
}

/** The else line for a value of `type` in `doc`: a parameter line of zero or false, added once per document. */
function elseLine(doc: FormDoc, type: string): string {
  const bool = type === "Bool";
  if (!bool && type !== "NonNegDollars" && type !== "Dollars") throw new Error(`what-if: no else for a ${type} input in ${doc.id}`);
  const id = `${doc.id}.whatif_${bool ? "no" : "zero"}`;
  if (!doc.lines.some((l) => l.id === id))
    doc.lines.push({ id, printed: "(what-if)", label: "what-if else", type: bool ? "Bool" : "NonNegDollars", expr: { op: "param", ref: bool ? "household.no" : "sales.zero" } as unknown as Expr, cite: doc.lines[0]!.cite });
  return id;
}

/** A values key with each gate line's name `<input>_if_<umbrella>` put back to the input's, so a refusal that names
 * the screen it read compares equal to the same refusal as built. */
export function unGated(key: string, umbrellas: Umbrella[]): string {
  let out = key;
  for (const u of umbrellas) out = out.split(`_if_${u.id.split(".").slice(1).join("_")}"`).join('"');
  return out;
}

/** The data and interview configurations with `umbrellas` in the formal model (in memory). */
export function applyUmbrellas(data: CanonicalData, configs: Record<string, InterviewData>, umbrellas: Umbrella[]): { data: CanonicalData; configs: Record<string, InterviewData> } {
  const d = structuredClone(data);
  const docs = (): FormDoc[] => [...d.forms, ...d.defs];
  const lineOf = (id: string): [FormDoc, Line] => {
    for (const doc of d.forms) { const l = doc.lines.find((x) => x.id === id); if (l) return [doc, l]; }
    throw new Error(`what-if: no line ${id}`);
  };
  const cs = structuredClone(configs);
  for (const u of umbrellas) {
    const home = d.forms.find((f) => f.id === u.id.split(".")[0])!;
    if (!home) throw new Error(`what-if: no document for ${u.id}`);
    if (docs().some((doc) => doc.lines.some((l) => l.id === u.id))) throw new Error(`what-if: ${u.id} already exists`);
    const short = u.id.split(".").slice(1).join("_");
    home.lines.push({ id: u.id, printed: "(gate)", label: u.label, type: "Bool", expr: { op: "input", source: u.label }, cite: home.lines[0]!.cite });
    for (const c of u.covers) {
      if (c.startsWith("$")) {
        const name = c.slice(1);
        for (const doc of docs()) {
          if (doc.id === name) continue;
          for (const l of [...doc.lines]) {
            if (!readsCollection(l.expr, name)) continue;
            const raw = `${l.id}__ungated_${short}`;
            doc.lines.push({ id: raw, printed: "(what-if)", label: l.label, type: l.type, expr: l.expr, cite: l.cite });
            l.expr = gateExpr(u.id, raw, elseLine(doc, l.type));
          }
        }
        continue;
      }
      const [doc, input] = lineOf(c);
      if (input.expr.op !== "input") throw new Error(`what-if: ${c} is not an input`);
      if (input.gated_by) throw new Error(`what-if: ${c} is already gated by ${input.gated_by}`);
      const gate = `${c}_if_${short}`;
      for (const other of docs()) for (const l of other.lines) {
        if (l.id === c) continue;
        const reads = refsOf(l.expr).has(c) || (l.refuses ?? []).some((r) => r.when === c) || l.shown_when === c;
        if (!reads) continue;
        l.expr = replaceRef(l.expr, c, gate) as Line["expr"];
        if (l.refuses) l.refuses = l.refuses.map((r) => (r.when === c ? { ...r, when: gate } : r));
        if (l.shown_when === c) l.shown_when = gate;
      }
      doc.lines.push({ id: gate, printed: "(what-if)", label: `${input.label} (when ${u.id})`, type: input.type, expr: gateExpr(u.id, c, elseLine(doc, input.type)), cite: input.cite });
      input.gated_by = gate;
    }
    for (const config of Object.values(cs)) {
      if (config.targets.some((t) => u.covers.includes(t))) throw new Error(`what-if: ${u.id} covers an interview target`);
      const orders = config.questions.filter((q) => u.covers.includes(q.input)).map((q) => q.order);
      config.questions.push({ input: u.id, prompt: u.label, help: "", order: orders.length ? Math.min(...orders) : 10, cite: config.cite });
    }
  }
  return { data: d, configs: cs };
}

/** The umbrella's truthful answer on a return, from its walk as built: yes when any input it covers was answered with
 * something other than false, 0 or an empty roster. */
export function umbrellaAnswer(u: Umbrella, events: { input: string; value: unknown }[], isClosed: (v: unknown) => boolean): boolean {
  return events.some((e) => u.covers.includes(questionTemplate(e.input)) && !isClosed(e.value));
}
