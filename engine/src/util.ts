// Small shared helpers: money/rate formatting and deterministic JSON.

export function fmtMoney(cents: number): string {
  const sign = cents < 0 ? "-" : "";
  const abs = Math.abs(cents);
  const dollars = Math.floor(abs / 100);
  const rem = abs % 100;
  const d = dollars.toLocaleString("en-US");
  return rem === 0 ? `${sign}$${d}` : `${sign}$${d}.${String(rem).padStart(2, "0")}`;
}

export function fmtRate(rate: { num: number; den: number }): string {
  if (rate.den === 100) {
    const pct = rate.num;
    return `${pct}% (${(pct / 100).toFixed(2)})`;
  }
  return `${rate.num}/${rate.den}`;
}

/**
 * Printed markers of authored lines that are not on the IRS page: helpers, gates,
 * interview questions, statuses and screens.
 */
export const HELPER_MARKERS: ReadonlySet<string> = new Set(["(helper)", "(gate)", "(computed helper)", "(question)", "(status)", "(screen)"]);

/** A line whose printed marker is one of HELPER_MARKERS. */
export function isHelperLine(line: { printed: string }): boolean {
  return HELPER_MARKERS.has(line.printed);
}

/**
 * A line with any parenthesized printed marker: the helper markers, plus column markers such
 * as `(c)` and worksheet-step markers such as `(CLW 1)`. None is a numbered line of the form.
 */
export function isMarkedLine(line: { printed: string }): boolean {
  return String(line.printed).startsWith("(");
}

export function shortHash(hex: string): string {
  return hex.slice(0, 8);
}

/** Deterministic JSON with sorted object keys and a trailing newline. */
export function stableStringify(value: unknown): string {
  return JSON.stringify(sortKeys(value), null, 2) + "\n";
}

function sortKeys(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(sortKeys);
  if (value && typeof value === "object") {
    const out: Record<string, unknown> = {};
    for (const key of Object.keys(value as Record<string, unknown>).sort()) {
      out[key] = sortKeys((value as Record<string, unknown>)[key]);
    }
    return out;
  }
  return value;
}
