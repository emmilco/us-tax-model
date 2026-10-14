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
