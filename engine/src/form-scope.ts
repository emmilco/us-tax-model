// The forms scope of the interview checks (`--forms a,b`): interview-rules, interview-coverage and tick-groups, run
// with it, check only what touches those forms. tools/change_scope.py computes the scope of a change and
// tools/check_all_steps.sh passes it in the light tier; the full tier runs the checks unscoped.
//
// An input key touches a form when one of its segments, with entry keys ([...]) and roster marks ($, @) removed, is the
// form's id: `person[taxpayer].f8889[hsa].line9` touches person and f8889, `$f8889@person[taxpayer]` touches f8889 and
// person. A scoped run is weaker than an unscoped one: walks that touch no form of the scope are not made, and the
// checks that need every walk (a baseline entry no longer seen, a report of all rows, a set no row uses) are not made.
import assert from "node:assert/strict";

/** The forms of `--forms a,b` (several --forms join), or null when the option is absent (an unscoped run). An empty
 * value is an empty scope: nothing is touched. */
export function formsOption(args: string[]): Set<string> | null {
  const values = args.flatMap((a, i) => (a === "--forms" && args[i + 1] !== undefined ? [args[i + 1]!] : a.startsWith("--forms=") ? [a.slice(8)] : []));
  if (!values.length && !args.includes("--forms")) return null;
  return new Set(values.flatMap((v) => v.split(",")).map((s) => s.trim()).filter(Boolean));
}

/** The form ids an input key (or a question template) names. */
export function formsOf(key: string): string[] {
  return key.replace(/\[[^\]]*\]/g, "").replace(/^\$/, "").split(/[.@]/).filter(Boolean);
}

/** Whether `key` touches a form of `forms`; every key does when `forms` is null (no scope). */
export function touches(key: string, forms: Set<string> | null): boolean {
  return forms === null || formsOf(key).some((f) => forms.has(f));
}

/** Whether any key of `keys` touches a form of `forms`. */
export function touchesAny(keys: Iterable<string>, forms: Set<string> | null): boolean {
  if (forms === null) return true;
  for (const k of keys) if (touches(k, forms)) return true;
  return false;
}

/** The scope's printed line, for a run's output. */
export function scopeLine(forms: Set<string> | null): string {
  return forms === null ? "unscoped" : `scoped to the forms ${[...forms].sort().join(", ") || "(none)"}`;
}

/** The option and the matching, on constructed keys. Each scoped check calls it from its own self-test. */
export function formScopeSelfTest(): void {
  assert.equal(formsOption([]), null);
  assert.deepEqual([...formsOption(["--forms", "f8889,sc", "--forms=asset"])!].sort(), ["asset", "f8889", "sc"]);
  assert.deepEqual([...formsOption(["--forms", ""])!], []);
  assert.deepEqual(formsOf("person[taxpayer].f8889[hsa].line9"), ["person", "f8889", "line9"]);
  assert.deepEqual(formsOf("$f8889@person[taxpayer]"), ["f8889", "person"]);
  const s = new Set(["f8889"]);
  assert.ok(touches("person[taxpayer].f8889[hsa].line9", s));
  assert.ok(touches("$f8889@person[taxpayer]", s));
  assert.ok(!touches("f1040.status", s));
  assert.ok(!touches("f88890.line1", s), "a form id is matched whole");
  assert.ok(touches("f1040.status", null), "no scope touches everything");
  assert.ok(!touchesAny(["f1040.status"], new Set()), "an empty scope touches nothing");
  assert.ok(touchesAny(["f1040.status", "f8889.line2"], s));
}
