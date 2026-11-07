// The forms a question names, found in its prompt and help and matched to the source catalogs by designation, so the
// web UI can show each one's printed title and the official statement of what it is for. Text matching only: which
// forms a question mentions is read from its reviewed wording, and nothing here bears on any value.
//
// A reference is "Form" or "Forms" followed by one form number or a list of them ("Form 8814", "Form 1040 line 16",
// "Forms 1099-INT and 1099-OID", "Form 2555 or Form 4563"), or "Schedule"/"Schedules" with schedule numbers and an
// optional parent ("Schedule J", "Schedules C, E, and F (Form 1040)"). A form number contains a digit; a schedule
// number may be letters ("SE"). A reference resolves to the catalog entry whose designation it is; a schedule named
// without its parent form resolves when the catalogs hold exactly one schedule of that number. A form number may
// carry a decimal part ("Form IT-360.1" is IT-360.1, not IT-360). New York designations are also found without the word
// "Form" ("IT-214", "IT-112-R"), but only where the bare token is a New York designation the catalogs hold (a letter pair,
// a hyphen and a number, printed with or without "Form"), so no other bare number is read as a form.

export interface Purpose { text: string; doc: string; page: number }
export interface FormEntry { id: string; designation: string; title?: string; purpose?: Purpose }
export interface FormRef { designation: string; id: string | null; title?: string; purpose?: Purpose }

const SPACE = String.raw`[\s ]+`;
const FORM_NUM = String.raw`(?:[A-Z]{1,4}-)?\d[0-9A-Z]*(?:-[0-9A-Z]+)*(?:\.\d+)?`;
const SCHEDULE_NUM = String.raw`${FORM_NUM}|[A-Z]{1,3}(?:-\d+)?`;
const END = String.raw`(?![A-Za-z0-9-])`;
const SEP = String.raw`(?:,${SPACE}|,?${SPACE}(?:and|or)${SPACE})`;
const FORMS = new RegExp(String.raw`\bForms?${SPACE}(${FORM_NUM})${END}((?:${SEP}(?:Forms?${SPACE})?${FORM_NUM}${END})*)`, "g");
const SCHEDULES = new RegExp(String.raw`\bSchedules?${SPACE}(${SCHEDULE_NUM})${END}((?:${SEP}(?:Schedules?${SPACE})?(?:${SCHEDULE_NUM})${END})*)`
  + String.raw`(?:${SPACE}?\(Forms?${SPACE}(${FORM_NUM})${END}[^)]*\))?`, "g");
const LIST_ITEM = (num: string) => new RegExp(String.raw`(?:Forms?|Schedules?)?${SPACE}?(${num})${END}`, "g");

const NY_DESIGNATION = /^(?:Form )?([A-Z]{2}-\d[0-9A-Z]*(?:-[0-9A-Z]+)*(?:\.\d+)?)$/;
const escapeRegExp = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

/** The designations a text names, in order of first mention: "Form 8814", "Schedule J", "Schedule A (Form 8971)".
 * `bareNumbers` are New York form numbers ("IT-214") that are also named without the word "Form". */
export function namedDesignations(text: string, bareNumbers: string[] = []): { designation: string; at: number; bareSchedule: boolean }[] {
  const out: { designation: string; at: number; bareSchedule: boolean }[] = [];
  // A schedule's parent form ("(Form 1040)") is part of the schedule's designation, not a form named on its own.
  const parents = [...text.matchAll(SCHEDULES)].filter((m) => m[3]).map((m) => [m.index!, m.index! + m[0].length] as const);
  for (const m of text.matchAll(FORMS)) {
    if (parents.some(([from, to]) => m.index! > from && m.index! < to)) continue;
    out.push({ designation: `Form ${m[1]}`, at: m.index!, bareSchedule: false });
    for (const n of (m[2] ?? "").matchAll(LIST_ITEM(FORM_NUM))) out.push({ designation: `Form ${n[1]}`, at: m.index!, bareSchedule: false });
  }
  for (const m of text.matchAll(SCHEDULES)) {
    const nums = [m[1]!, ...[...(m[2] ?? "").matchAll(LIST_ITEM(SCHEDULE_NUM))].map((n) => n[1]!)];
    for (const num of nums) {
      out.push({ designation: m[3] ? `Schedule ${num} (Form ${m[3]})` : `Schedule ${num}`, at: m.index!, bareSchedule: !m[3] });
    }
  }
  if (bareNumbers.length) {
    const bare = new RegExp(String.raw`(?<![A-Za-z0-9.-])(${bareNumbers.map(escapeRegExp).join("|")})(?![A-Za-z0-9-]|\.\d)`, "g");
    for (const m of text.matchAll(bare)) out.push({ designation: `Form ${m[1]}`, at: m.index!, bareSchedule: false });
  }
  return out.sort((a, b) => a.at - b.at);
}

/** A resolver over the catalogs' form and schedule entries (those whose designation begins "Form " or "Schedule "). */
export function formResolver(entries: FormEntry[]): (texts: string[]) => FormRef[] {
  const byDesignation = new Map<string, FormEntry>();
  const schedules = new Map<string, FormEntry[]>();
  const bareNumbers: string[] = [];
  for (const e of entries) {
    const ny = e.designation.match(NY_DESIGNATION);
    const key = ny ? `Form ${ny[1]}` : e.designation;
    if (!(ny || /^(Form|Schedule) \S/.test(e.designation)) || byDesignation.has(key)) continue;
    byDesignation.set(key, e);
    if (ny) bareNumbers.push(ny[1]!);
    const s = e.designation.match(/^(Schedule \S+) \(Form [^)]+\)$/);
    if (s) schedules.set(s[1]!, [...(schedules.get(s[1]!) ?? []), e]);
  }
  return (texts) => {
    const refs: FormRef[] = [];
    const seen = new Set<string>();
    for (const text of texts) {
      for (const { designation, bareSchedule } of namedDesignations(text, bareNumbers)) {
        const candidates = bareSchedule ? schedules.get(designation) ?? [] : [];
        const e = byDesignation.get(designation) ?? (candidates.length === 1 ? candidates[0] : undefined);
        const key = e ? e.id : designation;
        if (seen.has(key)) continue;
        seen.add(key);
        refs.push(e ? { designation: e.designation, id: e.id, ...(e.title ? { title: e.title } : {}), ...(e.purpose ? { purpose: e.purpose } : {}) }
          : { designation, id: null });
      }
    }
    return refs;
  };
}
