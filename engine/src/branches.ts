// Branch keys for a derivation: which guard a choose took, which side a
// smaller_of / larger_of / subtract_floor0 fell on, and which way a Bool line
// went. Shared by the fixture coverage report and the generated-input corpus
// so both count branches the same way.
import type { Derivation } from "./eval.js";

/** Strip collection instance keys so `person[taxpayer].w2[a].box1` reads `w2.box1`. */
export function templateKey(key: string): string {
  return key.includes("[") ? key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, (m) => m.split(".").filter(Boolean).at(-1)!.split("[")[0] + ".") : key;
}

/**
 * `sides` are keys of the form `line:side` (Bool true/false; floor/positive;
 * left/right); `guards` are `line#index` for the taken choose guard. Def
 * instances keep their instance key, which itself contains `#`, so the two
 * kinds are returned separately rather than told apart by the separator.
 */
export function branchKeys(der: Derivation): { sides: string[]; guards: string[] } {
  const keys: string[] = [];
  const guards: string[] = [];
  const id = templateKey(der.line);
  if (der.value.kind === "bool") keys.push(`${id}:${der.value.value}`);
  if (["subtract_floor0", "smaller_of", "larger_of"].includes(der.op)) {
    const values = der.operands.filter((o) => o.value.kind === "money").map((o) => (o.value as { cents: number }).cents);
    if (values.length >= 2) {
      const side = der.op === "subtract_floor0"
        ? (values[0]! > values[1]! ? "positive" : "floor")
        : ((der.op === "larger_of" ? values[0]! >= values[1]! : values[0]! <= values[1]!) ? "left" : "right");
      keys.push(`${id}:${side}`);
    }
  }
  if (der.op === "choose" && der.takenGuardIndex !== undefined) guards.push(`${id}#${der.takenGuardIndex}`);
  return { sides: keys, guards };
}
