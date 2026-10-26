// Generator facts, not tax-return runtime. Derive spouse-attributed coverage
// from actual month calendars so independently drawn counts cannot contradict.
import type { Inputs } from './types.js';

interface Calendar { eligible: boolean[]; family: boolean[] }

export function hsaCalendar(months: number, familyMonths: number, december: string): Calendar {
  if (!Number.isInteger(months) || months < 0 || months > 12 || !Number.isInteger(familyMonths) || familyMonths < 0 || familyMonths > months)
    throw new Error('invalid HSA calendar counts');
  const eligible = Array(12).fill(false), family = Array(12).fill(false);
  // The generator's nonempty eligible periods include December. Other temporal
  // patterns remain possible in the authored inputs and source regression cases.
  const keys = months ? [...Array.from({ length: months - 1 }, (_, i) => i), 11] : [];
  for (const key of keys) eligible[key] = true;
  const familyKeys = december === 'family' && familyMonths
    ? [11, ...keys.filter(key => key !== 11).slice(0, familyMonths - 1)] : keys.slice(0, familyMonths);
  for (const key of familyKeys) family[key] = true;
  return { eligible, family };
}

export function attributeHsaFamily(calendars: Calendar[]): Calendar[] {
  return calendars.map(calendar => ({ eligible: [...calendar.eligible], family: calendar.eligible.map((eligible, month) =>
    eligible && calendars.some(other => other.eligible[month] && other.family[month])) }));
}

export function cohereSpouseHsa(inputs: Inputs): void {
  if (inputs['f1040.status'] !== 'mfj') return;
  const entries = ['taxpayer', 'spouse'].filter(person => (inputs[`$f8889@person[${person}]`] as string[] | undefined)?.includes('hsa'))
    .map(person => `person[${person}].f8889[hsa]`);
  const raw = entries.map(key => hsaCalendar(Number(inputs[`${key}.months_eligible`]), Number(inputs[`${key}.months_family`]), String(inputs[`${key}.dec_coverage`])));
  const treated = attributeHsaFamily(raw);
  entries.forEach((key, i) => {
    const calendar = treated[i]!;
    inputs[`${key}.months_family`] = calendar.family.filter(Boolean).length;
    inputs[`${key}.dec_coverage`] = !calendar.eligible[11] ? 'none' : calendar.family[11] ? 'family' : 'self_only';
  });
}
