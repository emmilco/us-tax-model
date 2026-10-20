// Core data types for the canonical form data. These mirror schema/data.schema.json.

export type Money = number; // integer cents
export type Rate = { num: number; den: number };

// Operands: a line reference ("form.line"), a literal, or a parameter.
export type Operand =
  | string // line reference, resolved within file or across forms
  | { const: number | string | boolean; type?: "Count" }
  | { param: string };

// A reference to another line, optionally through a parameterized def instance.
export type LineRef =
  | string
  | {
      def: string;
      bind: Record<string, Operand>;
      line: string;
    };

export type TestExpr =
  | { op: "test"; eq?: [Operand, Operand]; ne?: [Operand, Operand]; lt?: [Operand, Operand]; le?: [Operand, Operand]; gt?: [Operand, Operand]; ge?: [Operand, Operand] }
  | { op: "test"; all: TestExpr[] }
  | { op: "test"; any: TestExpr[] }
  | { op: "test"; not: TestExpr };

export type Expr =
  | { op: "input"; source: string }
  | { op: "copy"; from: LineRef }
  | { op: "param"; ref: string }
  | { op: "sum"; of: string[] }
  | { op: "subtract"; from: string; take: Operand }
  | { op: "subtract_floor0"; from: string; take: Operand }
  | { op: "smaller_of"; of: string[] }
  | { op: "larger_of"; of: string[] }
  | { op: "multiply_rate"; amount: string; rate: Operand }
  | { op: "table_lookup"; table: string; key: string; status: string }
  | { op: "choose"; alternatives: { guard: TestExpr; then: LineRef }[] }
  | TestExpr
  | { op: "round"; of: string; unit: number; rule: string }
  | { op: "multiply_count"; amount: string; count: string }
  | { op: "prorate"; amount: string; part: string; whole: Operand; places: number }
  | { op: "bracket_schedule"; table: string; key: string; status: string }
  | { op: "sum_over"; collection: string; field: string; where?: TestExpr }
  | { op: "keyed_lookup"; table: string; keys: string[] }
  | { op: "opaque"; name: string };

export type ValueType =
  | "Count"
  | "Dollars"
  | "NonNegDollars"
  | "Rate"
  | "Bool"
  | `Enum(${string})`;

export interface CiteAuthored {
  doc: string;
  locator: string;
  quote?: string;
}

export interface CiteFilled {
  doc: string;
  tax_year: number;
  revision: string;
  locator: string;
  snapshot: string;
  quote?: string;
}

export interface Line {
  id: string;
  printed: string;
  label: string;
  type: ValueType;
  expr: Expr | { op: "input"; source: string };
  cite: CiteFilled;
  note?: string;
  ambiguity?: string;
  /** Why an unread line is kept: shown on the values sheet. */
  display?: string;
  refuses?: { when: string; form: string; remedy: string; cite: CiteFilled }[];
}

export interface FormDoc {
  id: string;
  kind: "form" | "worksheet" | "def";
  title: string;
  tax_year: number;
  parameters?: string[];
  collection?: { parent?: string; cite: CiteFilled };
  note?: string;
  lines: Line[];
}

export interface ParamEntry {
  type: ValueType;
  value: number | Rate | boolean | string | Record<string, number>;
  cite: CiteFilled;
}

export interface ParamsDoc {
  tax_year: number;
  enums: Record<string, { values: string[]; cite: CiteFilled }>;
  values: Record<string, ParamEntry>;
}

export interface TableDoc {
  id: string;
  kind: "tax_table" | "bracket_schedule" | "keyed";
  title: string;
  tax_year: number;
  cite: CiteFilled;
  // tax_table
  columns?: { key: string; statuses: string[]; note?: string }[];
  bands?: { at_least: Money; less_than: Money; tax: Money[] }[];
  /** The amounts a printed table covers when not [0, ordinary.table_boundary). */
  bounds?: { at_least: Money; less_than: Money };
  // bracket_schedule
  status_alias?: Record<string, string>;
  schedules?: Record<string, { upper: Money | null; base: Money; rate: Rate; over: Money }[]>;
  // keyed: one row per key tuple; a cell's type is `cell` (Rate, Count, Dollars, NonNegDollars or Enum(name))
  keys?: { name: string; type: string }[];
  cell?: string;
  rows?: { keys: (string | number)[]; value: number | string | Rate }[];
}

export interface RegisterEntry {
  id: string;
  text_at_issue: string;
  readings: string[];
  chosen: string;
  reason: string;
  cite: CiteFilled;
  status?: string;
}

export interface RegisterDoc {
  tax_year: number;
  entries: RegisterEntry[];
}

export interface CanonicalData {
  forms: FormDoc[];
  defs: FormDoc[];
  params: ParamsDoc;
  tables: TableDoc[];
  register: RegisterDoc;
}

export type Inputs = Record<string, unknown>;
