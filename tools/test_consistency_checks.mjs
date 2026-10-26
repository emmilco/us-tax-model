// Core semantics: unanswered consistency checks never supply tax facts, while
// supplied contradictions and required scope gates still stop evaluation.
import assert from 'node:assert/strict';
import { evaluate } from '../engine/dist/eval.js';
import { interviewState } from '../engine/dist/interview.js';
import { hsaCalendar, attributeHsaFamily, cohereSpouseHsa } from '../engine/dist/hsa-calendar.js';

const line = (id, type, expr, extra = {}) => ({ id: `probe.${id}`, printed: id, label: id, type, expr, cite: null, ...extra });
const input = (id, type = 'NonNegDollars') => line(id, type, { op: 'input', source: id });
const check = { when: 'probe.bad', when_known: true, form: 'Supplied figures', remedy: 'Correct the supplied figures', cite: null };
const data = { forms: [{ id: 'probe', kind: 'form', tax_year: 2025, title: 'Consistency check test', lines: [
  input('amount'), input('total'), input('other'), input('scope', 'Bool'), input('later', 'Bool'),
  line('bad', 'Bool', { op: 'test', gt: ['probe.amount', 'probe.total'] }),
  line('zero', 'NonNegDollars', { op: 'param', ref: 'zero' }),
  line('result', 'NonNegDollars', { op: 'choose', alternatives: [
    { guard: { op: 'test', eq: ['probe.total', { const: 0 }] }, then: 'probe.zero' },
    { guard: { op: 'test', gt: ['probe.total', { const: 0 }] }, then: 'probe.amount' },
  ] }, { refuses: [check] }),
] }], defs: [], tables: [], params: { values: { zero: { type: 'NonNegDollars', value: 0 } }, enums: {} }, register: { entries: [] } };
const value = (facts, current = data, target = 'probe.result') => evaluate(current, facts, [target]).values.get(target);

assert.deepEqual(value({ 'probe.total': 0 }), { kind: 'money', cents: 0 });
assert.deepEqual(value({ 'probe.total': 0, 'probe.amount': null }), { kind: 'money', cents: 0 });
assert.equal(value({ 'probe.total': 0, 'probe.amount': 1 }).kind, 'refusal');
assert.equal(value({ 'probe.total': 100, 'probe.amount': 101 }).kind, 'refusal');
assert.deepEqual(value({ 'probe.total': 100, 'probe.amount': 100 }), { kind: 'money', cents: 100 });
assert.equal(value({ 'probe.total': 100 }).input, 'probe.amount');
assert.equal(value({}).kind, 'unknown');

const result = evaluate(data, { 'probe.total': 0 }, ['probe.result']);
assert.ok(!result.values.has('probe.amount'), 'an unperformed check must not add an interview question');
assert.match(result.derivations.get('probe.result').notes.join(' '), /awaits supplied figures/);
const config = { tax_year: 2025, targets: ['probe.result', 'probe.other'], initial: {}, cite: null,
  questions: ['amount', 'total', 'other', 'scope', 'later'].map((id, order) => ({ input: `probe.${id}`, prompt: id, help: '', order, cite: null })) };
assert.equal(interviewState(data, config, { 'probe.total': 0 }).question.input, 'probe.other');
assert.deepEqual(interviewState(data, config, { 'probe.total': 0 }).reachableInputs, ['probe.other']);
assert.ok(evaluate(data, { 'probe.total': 0 }, ['probe.amount', 'probe.result']).values.has('probe.amount'), 'an independently requested unknown must remain visible');

const required = structuredClone(data);
required.forms[0].lines.at(-1).refuses = [
  { ...check, when: 'probe.scope', when_known: undefined },
  { ...check, when: 'probe.later', when_known: undefined },
];
assert.equal(value({ 'probe.total': 0, 'probe.later': true }, required).input, 'probe.scope', 'ordinary gate order stays unchanged (BUG-0083)');
assert.equal(value({ 'probe.total': 0, 'probe.scope': true }, required).kind, 'refusal');

const nested = structuredClone(data);
nested.forms[0].lines[0].refuses = [{ ...check, when: 'probe.scope', when_known: undefined }];
assert.equal(value({ 'probe.total': 0, 'probe.scope': true }, nested).gate, 'probe.scope', 'a refused consistency gate must propagate its actual refusal');
// A spouse covered by a family plan in nine eligible months shares that coverage
// with the spouse eligible all twelve months; independently drawn counts 9/3
// cannot be used as already-attributed family month counts.
const calendars = attributeHsaFamily([hsaCalendar(12, 3, 'self_only'), hsaCalendar(9, 9, 'family')]);
assert.equal(calendars[0].family.filter(Boolean).length, 9);
assert.equal(calendars[1].family.filter(Boolean).length, 9);
assert.ok(calendars.every(calendar => calendar.family[11]));
for (let months = 0; months <= 12; months++) for (let family = 0; family <= months; family++) {
  const actual = hsaCalendar(months, family, family === months && months ? 'family' : 'self_only');
  assert.equal(actual.eligible.filter(Boolean).length, months);
  assert.equal(actual.family.filter(Boolean).length, family);
  assert.ok(actual.family.every((covered, index) => !covered || actual.eligible[index]));
  const treated = attributeHsaFamily([actual, hsaCalendar(12, 12, 'family')]);
  assert.equal(treated[0].family.filter(Boolean).length, months);
}
const figures = { 'f1040.status': 'mfj', '$f8889@person[taxpayer]': ['hsa'], '$f8889@person[spouse]': ['hsa'] };
for (const [person, months, family, december] of [['taxpayer', 12, 3, 'self_only'], ['spouse', 9, 9, 'family']])
  for (const [field, value] of Object.entries({ months_eligible: months, months_family: family, dec_coverage: december }))
    figures[`person[${person}].f8889[hsa].${field}`] = value;
cohereSpouseHsa(figures);
assert.equal(figures['person[taxpayer].f8889[hsa].months_family'], 9);
assert.equal(figures['person[taxpayer].f8889[hsa].dec_coverage'], 'family');
console.log('consistency checks: missing/known/contradictory figures, interview dependencies, mandatory/nested refusals and monthly spouse coverage pass');
