// A fixture input may be stated relative to a year parameter, so that a boundary case
// stays on its boundary when the parameter changes from year to year:
//   {"param": "medicare.threshold", "status": "mfj", "offset": -1}
// is the parameter's value (for that filing status, if it has one per status) plus the
// offset in cents. Every other input is taken as it is.
import type { Inputs, ParamsDoc } from "./types.js";

interface ParamRef { param: string; status?: string; offset: number }

function isRef(v: unknown): v is ParamRef {
  return typeof v === "object" && v !== null && !Array.isArray(v) && typeof (v as ParamRef).param === "string";
}

export function resolveInputs(inputs: Record<string, unknown>, params: ParamsDoc, where = "fixture"): Inputs {
  const out: Record<string, unknown> = {};
  for (const [key, v] of Object.entries(inputs)) {
    if (!isRef(v)) { out[key] = v; continue; }
    const entry = params.values[v.param];
    const base = v.status === undefined ? entry?.value : (entry?.value as Record<string, unknown> | undefined)?.[v.status];
    if (typeof base !== "number" || !Number.isSafeInteger(v.offset)) {
      throw new Error(`${where}: input ${key} refers to ${v.param}${v.status ? `[${v.status}]` : ""}, which is not a dollar amount`);
    }
    out[key] = base + v.offset;
  }
  return out as Inputs;
}
