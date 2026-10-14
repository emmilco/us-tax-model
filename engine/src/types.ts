// Core data types for the canonical form data. These mirror schema/data.schema.json.

export type Money = number; // integer cents
export type Rate = { num: number; den: number };

// Operands: a line reference ("form.line"), a literal, or a parameter.
export type Operand =
  | string // line reference, resolved within file or across forms
  | { const: number | string | boolean }
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
  | { op: "bracket_schedule"; table: string; key: string; status: string }
  | { op: "sum_over"; of: string }
  | { op: "opaque"; name: string };

export type ValueType =
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
}

export interface FormDoc {
  id: string;
  kind: "form" | "worksheet" | "def";
  title: string;
  tax_year: number;
  parameters?: string[];
  note?: string;
  lines: Line[];
}

export interface ParamEntry {
  type: ValueType;
  value: number | Rate | boolean | Record<string, number>;
  cite: CiteFilled;
}

export interface ParamsDoc {
  tax_year: number;
  enums: Record<string, { values: string[]; cite: CiteFilled }>;
  values: Record<string, ParamEntry>;
}

export interface TableDoc {
  id: string;
  kind: "tax_table" | "bracket_schedule";
  title: string;
  tax_year: number;
  cite: CiteFilled;
  // tax_table
  columns?: { key: string; statuses: string[]; note?: string }[];
  bands?: { at_least: Money; less_than: Money; tax: Money[] }[];
  // bracket_schedule
  status_alias?: Record<string, string>;
  schedules?: Record<string, { upper: Money | null; base: Money; rate: Rate; over: Money }[]>;
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
