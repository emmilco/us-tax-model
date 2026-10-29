// Run many returns through UsTaxes' Form 1040 model in one Node process.
//
//   USTAXES_SRC=<clone> USTAXES_DEPS=<deps> node --no-experimental-strip-types --import <this dir>/hooks.mjs \
//     run.mjs <tax year> <input.json> <output.json>
//
// input.json: [{ id, info, assets }] where `info` is UsTaxes' `Information` and `assets` its
// `Asset[]` (src/core/data/index.ts), built by ustaxes_adapter.py, with every date given as
// [year, month, day] (month 1-12) and built here as a local-time Date, because UsTaxes reads
// dates with getFullYear() and getMonth(). The return is built by the year's entry point,
// src/forms/Y<year>/irsForms/Main.ts `create1040(info, assets)`, as UsTaxes' own UI does; nothing
// is attached to or changed on the forms afterwards.
//
// output.json: { engine: {...}, cases: { id: { values: { "<form>.<accessor>": number|boolean|null } }
// | { error } } }. Each value is the accessor's result in dollars as UsTaxes computes it (a double,
// never rounded here); null where the accessor returns undefined. The accessor names are UsTaxes'
// own; ustaxes_adapter.py maps them to the project's line ids.
import { readFileSync, writeFileSync } from 'node:fs'

const [year, inPath, outPath] = process.argv.slice(2)
const { create1040 } = await import(`ustaxes/forms/Y${year}/irsForms/Main`)

const asDate = (v) => (Array.isArray(v) ? new Date(v[0], v[1] - 1, v[2]) : v)
function revive(info) {
  const tp = info.taxPayer
  tp.primaryPerson.dateOfBirth = asDate(tp.primaryPerson.dateOfBirth)
  if (tp.spouse) tp.spouse.dateOfBirth = asDate(tp.spouse.dateOfBirth)
  for (const d of tp.dependents) d.dateOfBirth = asDate(d.dateOfBirth)
  for (const h of info.healthSavingsAccounts) { h.startDate = asDate(h.startDate); h.endDate = asDate(h.endDate) }
  return info
}

const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => `l${a + i}`)
// Accessors read per form: [output prefix, object getter, accessor names]. Accessors are methods
// with no arguments; part2a/part2b of Schedule 8812 return records whose fields are read too.
const READ = [
  ['f1040', (f) => f, ['l1a', 'l1z', 'l2b', 'l3a', 'l3b', 'l6a', 'l6b', 'l7a', 'l8', 'l9', 'l10', 'l11a', 'l11b', 'l12e', 'l13a', 'l13b',
    'l14', 'l15', 'l16', 'l17', 'l18', 'l19', 'l20', 'l21', 'l22', 'l23', 'l24', 'l25a', 'l25c', 'l25d', 'l27a', 'l28', 'l29', 'l31', 'l32',
    'l33', 'l34', 'l37', 'standardDeduction']],
  ['s1', (f) => f.schedule1, ['l7', 'l9', 'l10', 'l11', 'l13', 'l15', 'l19a', 'l21', 'l26']],
  ['s1a', (f) => f.schedule1A, ['l1', 'l3', 'l4a', 'l4c', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14a', 'l14c', 'l15', 'l16',
    'l17', 'l18', 'l19', 'l20', 'l21', 'l23', 'l24', 'l25', 'l26', 'l27', 'l28', 'l29', 'l30', 'l31', 'l32', 'l33', 'l34', 'l35', 'l36a',
    'l36b', 'l37', 'l38', 'isNeeded']],
  ['s2', (f) => f.schedule2, ['l2', 'l3', 'l4', 'l8', 'l11', 'l12', 'l21']],
  ['f5329', (f) => f.f5329, ['isNeeded', 'l1', 'l8']],
  ['s3', (f) => f.schedule3, ['isNeeded', 'l1', 'l2', 'l3', 'l4', 'l5a', 'l5b', 'l8', 'l9', 'l11', 'l15']],
  ['sa', (f) => f.scheduleA, ['isNeeded', 'l1', 'l2', 'l3', 'l4', 'l5a', 'l5b', 'l5d', 'l5e', 'l7', 'l8a', 'l8e', 'l9', 'l10', 'l11', 'l12',
    'l14', 'l17']],
  ['sb', (f) => f.scheduleB, ['l2', 'l4', 'l6']],
  ['sd', (f) => f.scheduleD, ['isNeeded', 'l7', 'l13', 'l15', 'l16', 'l17', 'l21', 'to1040', 'computeTaxOnDTaxWorksheet', 'computeTaxOnQDWorksheet']],
  ['qdcg', (f) => f.qualifiedAndCapGainsWorksheet, range(1, 25)],
  ['sdtw', (f) => f.scheduleDTaxWorksheet, ['tax']],
  ['ssb', (f) => f.socialSecurityBenefitsWorksheet, range(1, 18).concat(['taxableAmount'])],
  ['sli', (f) => f.studentLoanInterestWorksheet, range(1, 9)],
  ['s8812', (f) => f.schedule8812, ['isNeeded', 'l1', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14', 'l27',
    'earnedIncomeWorksheet', 'creditLimitWorksheetA']],
  ['eic', (f) => f.scheduleEIC, ['allowed', 'credit', 'earnedIncome', 'investmentIncome']],
  ['f8889', (f) => f.f8889, ['isNeeded', 'l2', 'l3', 'l5', 'l6', 'l7', 'l8', 'l9', 'l11', 'l12', 'l13']],
  ['f8889s', (f) => f.f8889Spouse, ['isNeeded', 'l2', 'l3', 'l6', 'l13']],
  ['f8959', (f) => f.f8959, range(1, 24)],
  ['f8960', (f) => f.f8960, ['l1', 'l2', 'l5a', 'l5d', 'l8', 'l9a', 'l9b', 'l9d', 'l11', 'l12', 'l13', 'l14', 'l15', 'l16', 'l17']],
  ['f4952', (f) => f.f4952, ['l1', 'l3', 'l4a', 'l4e', 'l4g', 'l4h']],
  ['f2441', (f) => f.f2441, ['isNeeded', 'credit']],
  ['f8880', (f) => f.f8880, ['l3', 'creditRate', 'l4', 'credit']],
  ['f5695', (f) => f.f5695, ['l15', 'l30']],
  ['f6251', (f) => f.f6251, ['l11']],
  ['f8995', (f) => f.f8995, ['deductions']],
  // Form 8863: the public lines and the per-credit amounts F8863.ts keeps in private (TypeScript-only) members.
  ['f8863', (f) => f.f8863, ['isNeeded', 'aotcBeforePhaseOut', 'aotcAfterPhaseOut', 'aotcNonrefundable', 'llcBeforePhaseOut',
    'llcAfterPhaseOut', 'l8', 'l19']],
  ['f8962', (f) => f.f8962, ['isNeeded', 'contributionAmount', 'allowablePtc', 'annualAdvancePtc', 'credit', 'excessRepayment']]
]

// UsTaxes recomputes every line from the start on each call (no line is stored), so reading a few
// hundred lines of one return repeats the return's arithmetic thousands of times. The
// zero-argument line methods of the constructed forms are therefore cached per return: each own
// function property of Form 1040 and of every form object reachable from it is wrapped so that
// its first result is kept. The line methods are functions of the return's fixed inputs (the
// few that assign a field, such as computeTax building its worksheet or Form 8889 recording the
// coverage type, assign the same value on every call), so the cache changes no value;
// USTAXES_NO_CACHE=1 turns it off, and `ustaxes_adapter.py --self-test` (run by run.sh) compares the two on sample returns.
function cacheLines(obj, seen = new Set()) {
  if (obj === null || typeof obj !== 'object' || seen.has(obj)) return
  seen.add(obj)
  if (Array.isArray(obj)) { for (const x of obj) cacheLines(x, seen); return }
  for (const k of Object.keys(obj)) {
    const v = obj[k]
    if (typeof v === 'function') {
      let done = false, kept
      obj[k] = (...args) => {
        if (args.length > 0) return v(...args)
        if (!done) { kept = v(); done = true }
        return kept
      }
    } else if (v !== null && typeof v === 'object' && k !== 'info' && k !== 'assets' && k !== 'state') cacheLines(v, seen)
  }
}

function read(f) {
  if (process.env.USTAXES_NO_CACHE !== '1') cacheLines(f)
  const values = {}
  for (const [prefix, get, names] of READ) {
    const obj = get(f)
    if (obj === undefined) continue
    for (const n of names) {
      const v = obj[n]()
      values[`${prefix}.${n}`] = v === undefined ? null : v
    }
  }
  for (const part of ['part2a', 'part2b']) {
    const rec = f.schedule8812[part]()
    for (const [k, v] of Object.entries(rec)) values[`s8812.${part}.${k}`] = v === undefined ? null : v
  }
  return values
}

const cases = JSON.parse(readFileSync(inPath, 'utf8'))
const out = {}
for (const c of cases) {
  try {
    const r = create1040(revive(c.info), c.assets.map((a) => ({ ...a, openDate: asDate(a.openDate), closeDate: asDate(a.closeDate) })))
    if (r._tag === 'left') {
      out[c.id] = { error: `validation: ${JSON.stringify(r.left)}` }
      continue
    }
    const [f1040] = r.right
    out[c.id] = { values: read(f1040) }
  } catch (e) {
    out[c.id] = { error: String(e && e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e) }
  }
}
writeFileSync(outPath, JSON.stringify({ cases: out }))