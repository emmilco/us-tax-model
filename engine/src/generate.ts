// Generated whole-return inputs: a fast-check arbitrary over every declared
// input of the supported slice, biased toward zeros, small amounts and the
// boundaries the worksheets branch on. Used by the property tests and as the
// seed of the branch-covering inputs for class M hand-work (design 2.10).
//
// Every declared root input receives a value (money inputs not modelled
// below are zero nine times in ten), so an `unknown` in a result means the
// data asked for something undeclared, not that the generator forgot a key.
import fc from "fast-check";
import type { CanonicalData, FormDoc, Inputs, Line } from "./types.js";

const WAGE_BASE = 17_610_000; // Social Security wage base, cents
const ADDL_MEDICARE_START = 20_000_000;

function halfUp(n: number, d: number): number { return Math.floor((2 * n + d) / (2 * d)); }
function rate(amount: number, num: number, den: number): number { return halfUp(amount * num, den); }

/** Root (non-collection) input lines keyed by input key, and the collection documents. */
export function declaredInputs(data: CanonicalData): { roots: Map<string, Line>; collections: FormDoc[] } {
  const roots = new Map<string, Line>();
  const collections: FormDoc[] = [];
  for (const doc of data.forms) {
    if (doc.collection) { collections.push(doc); continue; }
    for (const line of doc.lines) if (line.expr.op === "input") roots.set(line.id, line);
  }
  return { roots, collections };
}

function defaultFor(data: CanonicalData, line: Line): number | boolean | string {
  if (line.type === "Bool") return false;
  if (line.type.startsWith("Enum(")) return data.params.enums[line.type.slice(5, -1)]!.values[0]!;
  return 0;
}

const money = (max: number): fc.Arbitrary<number> => fc.oneof(
  { weight: 2, arbitrary: fc.constant(0) },
  { weight: 3, arbitrary: fc.integer({ min: 0, max: Math.min(max, 5_000_000) }) },
  { weight: 3, arbitrary: fc.integer({ min: 0, max }) },
);
const rareMoney = (max: number, percent = 10): fc.Arbitrary<number> => fc.oneof(
  { weight: 100 - percent, arbitrary: fc.constant(0) },
  { weight: percent, arbitrary: fc.integer({ min: 1, max }) },
);
const rareTrue = (percent: number): fc.Arbitrary<boolean> => fc.oneof(
  { weight: 100 - percent, arbitrary: fc.constant(false) },
  { weight: percent, arbitrary: fc.constant(true) },
);
const pct = fc.integer({ min: 0, max: 100 });

// Bool inputs whose usual value is not "false, rarely true".
const BOOL_TRUE_PERCENT: Record<string, number> = {
  "div.basis_reconciled": 95,
  "ftc.all_passive": 90, "ftc.statements": 90, "ftc.eligible": 90, "ftc.elect": 90,
  "sa.elect_itemize": 10,
};
const DEFAULT_TRUE_PERCENT = 10;

// Money inputs the generator models with structure; every other declared
// money input is rarely nonzero.
const MODELLED = new Set([
  "f1040.line3a", "sb.ordinary_dividends", "qbi.dividends", "sd.distributions", "div.box2b", "div.box2d",
  "sa.line1", "sa.line5a", "sa.line5b", "sa.line8a", "sa.line11", "f4952.line1", "f4952.line4g", "ftc.taxes",
]);

interface Employer { box1: number; box2pct: number; box7: number; over: number }
interface Sale { box: string; aggregate: boolean; code: string; special: boolean; aggregate_eligible: boolean; proceeds: number; reported_basis: number; correct_basis: number; wash_loss: number; invalid: boolean }
interface Gift { deduction: number; public_securities: boolean; special: boolean }
interface Dependent { relationship: string; age: number; student: boolean; disabled: boolean; months: number; self_support: boolean; joint_return: boolean; citizen: boolean; canada_mexico: boolean; married: boolean; tin: boolean; work_ssn: boolean; gross_income: number; supported: boolean; other_claimant: boolean; divorced_rule: boolean; multiple_support: boolean; parent_home_paid: boolean }
interface Household { taxpayer_age: number; taxpayer_tin: boolean; taxpayer_work_ssn: boolean; home_cost: boolean; unmarried: boolean }

interface Spec {
  status: string;
  profile: string;
  rrta: boolean;
  clean: boolean;
  badDividends: boolean;
  employers: Employer[];
  interest: number[];
  ordinary: number; qpct: number; qbipct: number;
  distributions: number; b2bpct: number; b2dpct: number;
  sales: Sale[];
  medical: number; saltIncome: number; saltRe: number; mortgage: number; cashGifts: number; gifts: Gift[];
  invInterest: number; election: number; ftcTaxes: number;
  dependents: Dependent[];
  household: Household;
  flags: Record<string, boolean>;
  extras: Record<string, number>;
}

export function returnArbitrary(data: CanonicalData): fc.Arbitrary<Inputs> {
  const { roots } = declaredInputs(data);
  const boolKeys = [...roots].filter(([, l]) => l.type === "Bool").map(([k]) => k);
  const extraKeys = [...roots].filter(([k, l]) => l.type !== "Bool" && !l.type.startsWith("Enum(") && !MODELLED.has(k)).map(([k]) => k);
  const employer = fc.record<Employer>({
    box1: money(40_000_000),
    box2pct: fc.integer({ min: 0, max: 30 }),
    box7: rareMoney(2_000_000),
    over: rareMoney(200_000, 5),
  });
  const sale = fc.record<Sale>({
    box: fc.oneof({ weight: 19, arbitrary: fc.constantFrom("A", "B", "C", "D", "E", "F") }, { weight: 1, arbitrary: fc.constantFrom("G", "H", "I", "J", "K", "L") }),
    aggregate: fc.boolean(),
    code: fc.constantFrom("none", "none", "B", "W", "BW"),
    invalid: rareTrue(5),
    special: rareTrue(5),
    aggregate_eligible: fc.boolean(),
    proceeds: money(10_000_000),
    reported_basis: money(10_000_000),
    correct_basis: money(10_000_000),
    wash_loss: rareMoney(100_000, 30),
  });
  const dependent = fc.record<Dependent>({
    relationship: fc.constantFrom("child", "child", "child", "sibling", "parent", "in_law", "household_member", "other"),
    age: fc.oneof({ weight: 3, arbitrary: fc.integer({ min: 0, max: 16 }) }, { weight: 1, arbitrary: fc.integer({ min: 17, max: 30 }) }, { weight: 1, arbitrary: fc.integer({ min: 31, max: 90 }) }),
    student: rareTrue(30), disabled: rareTrue(5),
    months: fc.oneof({ weight: 4, arbitrary: fc.constant(12) }, { weight: 1, arbitrary: fc.integer({ min: 0, max: 12 }) }),
    self_support: rareTrue(5), joint_return: rareTrue(3), citizen: rareTrue(90), canada_mexico: rareTrue(20), married: rareTrue(3),
    tin: rareTrue(95), work_ssn: rareTrue(90), gross_income: rareMoney(1_000_000, 20), supported: rareTrue(90),
    other_claimant: rareTrue(3), divorced_rule: rareTrue(3), multiple_support: rareTrue(2), parent_home_paid: rareTrue(30),
  });
  const household = fc.record<Household>({
    taxpayer_age: fc.integer({ min: 18, max: 80 }), taxpayer_tin: rareTrue(97), taxpayer_work_ssn: rareTrue(93),
    home_cost: rareTrue(70), unmarried: rareTrue(90),
  });
  const gift = fc.record<Gift>({
  deduction: fc.oneof({ weight: 3, arbitrary: money(500_000) }, { weight: 1, arbitrary: fc.integer({ min: 500_001, max: 2_000_000 }) }),
  public_securities: fc.boolean(),
  special: rareTrue(5),
});
  const spec = fc.record<Spec>({
    status: fc.constantFrom("single", "single", "single", "hoh", "mfj", "mfs", "qss"),
    profile: fc.constantFrom("wage", "wage", "wage", "investor"),
    rrta: rareTrue(3),
    clean: rareTrue(75),
    badDividends: rareTrue(3),
    employers: fc.array(employer, { minLength: 1, maxLength: 2 }),
    interest: fc.array(money(5_000_000), { maxLength: 2 }),
    ordinary: money(8_000_000), qpct: pct, qbipct: fc.integer({ min: 0, max: 20 }),
    distributions: money(2_000_000), b2bpct: rareMoney(100, 25), b2dpct: rareMoney(100, 25),
    sales: fc.array(sale, { maxLength: 3 }),
    medical: money(3_000_000), saltIncome: money(6_000_000), saltRe: money(2_000_000), mortgage: money(4_000_000),
    cashGifts: money(2_000_000), gifts: fc.array(gift, { maxLength: 2 }),
    invInterest: money(1_000_000), election: rareMoney(1_000_000, 20), ftcTaxes: rareMoney(45_000, 25),
    dependents: fc.array(dependent, { maxLength: 3 }),
    household,
    flags: fc.record(Object.fromEntries(boolKeys.map((k) => [k, rareTrue(BOOL_TRUE_PERCENT[k] ?? DEFAULT_TRUE_PERCENT)]))),
    extras: fc.record(Object.fromEntries(extraKeys.map((k) => [k, rareMoney(500_000, 2)]))),
  });
  return spec.map((s) => buildInputs(data, s));
}

function buildInputs(data: CanonicalData, s: Spec): Inputs {
  const { roots } = declaredInputs(data);
  const inputs: Inputs = {};
  for (const [key, line] of roots) inputs[key] = defaultFor(data, line);
  // Clean returns keep every out-of-scope flag at its usual value, so most
  // generated returns compute all the way through; the rest exercise gates.
  for (const [key, v] of Object.entries(s.flags)) inputs[key] = s.clean ? (BOOL_TRUE_PERCENT[key] ?? 0) >= 50 : v;
  for (const [key, v] of Object.entries(s.extras)) inputs[key] = s.clean ? 0 : v;
  inputs["f1040.status"] = s.status;
  // An investor has no wages and only qualified dividends and gains, which is
  // the only way the worksheets' upper skip rules and ceilings are reached.
  const investor = s.profile === "investor";

  inputs["$person"] = ["taxpayer"];
  inputs["person[taxpayer].rrta"] = s.rrta;
  const employers = s.employers.map((_, i) => `emp_${String.fromCharCode(97 + i)}`);
  inputs["$w2@person[taxpayer]"] = employers;
  s.employers.forEach((e, i) => {
    const p = `person[taxpayer].w2[${employers[i]}]`;
    const box1 = investor ? 0 : e.box1;
    const box7 = investor ? 0 : e.box7;
    const box3 = Math.min(box1, Math.max(0, WAGE_BASE - box7));
    const box5 = box1 + box7;
    inputs[`${p}.box1`] = box1;
    inputs[`${p}.box2`] = rate(box1, e.box2pct, 100);
    inputs[`${p}.box3`] = box3;
    inputs[`${p}.box7`] = box7;
    inputs[`${p}.box4`] = rate(box3 + box7, 62, 1000) + e.over;
    inputs[`${p}.box5`] = box5;
    inputs[`${p}.box6`] = rate(box5, 145, 10000) + (box5 > ADDL_MEDICARE_START ? rate(box5 - ADDL_MEDICARE_START, 9, 1000) : 0);
  });

  const interest = investor ? [] : s.interest;
  inputs["$interest"] = interest.map((_, i) => `bank_${String.fromCharCode(97 + i)}`);
  interest.forEach((a, i) => { inputs[`interest[bank_${String.fromCharCode(97 + i)}].amount`] = a; });

  const ordinary = investor ? s.ordinary * 4 : s.ordinary;
  inputs["sb.ordinary_dividends"] = ordinary;
  inputs["f1040.line3a"] = s.badDividends ? ordinary + 100 : rate(ordinary, investor ? 100 : s.qpct, 100);
  inputs["qbi.dividends"] = rate(ordinary, s.qbipct, 100);
  inputs["sd.distributions"] = s.distributions;
  const box2b = rate(s.distributions, s.b2bpct, 100);
  inputs["div.box2b"] = box2b;
  inputs["div.box2d"] = rate(s.distributions - box2b, s.b2dpct, 100);

  inputs["$sales"] = s.sales.map((_, i) => `s${i + 1}`);
  s.sales.forEach((sale, i) => {
    // The aggregate route needs a basis-reported box (A or D), no code and
    // eligibility; code B needs a basis-reported box. Invalid entries keep
    // whatever came out so the gates are exercised too.
    const basisReported = sale.box === "A" || sale.box === "D";
    let code = sale.code;
    if (!sale.invalid && code.includes("B") && !basisReported) code = code === "B" ? "none" : "W";
    const route = sale.aggregate && (sale.invalid || (basisReported && code === "none" && sale.aggregate_eligible)) ? "aggregate" : "detail";
    const entry = { box: sale.box, route, code, special: sale.invalid && sale.special, aggregate_eligible: sale.aggregate_eligible,
      proceeds: sale.proceeds, reported_basis: sale.reported_basis, correct_basis: sale.correct_basis, wash_loss: code.includes("W") ? sale.wash_loss : 0 };
    for (const [k, v] of Object.entries(entry)) inputs[`sales[s${i + 1}].${k}`] = v;
  });

  inputs["sa.line1"] = s.medical; inputs["sa.line5a"] = s.saltIncome; inputs["sa.line5b"] = s.saltRe;
  inputs["sa.line8a"] = s.mortgage; inputs["sa.line11"] = s.cashGifts;
  inputs["$gift"] = s.gifts.map((_, i) => `item_${String.fromCharCode(97 + i)}`);
  s.gifts.forEach((g, i) => { for (const [k, v] of Object.entries(g)) inputs[`gift[item_${String.fromCharCode(97 + i)}].${k}`] = v; });
  inputs["$dependent"] = s.dependents.map((_, i) => `dep_${String.fromCharCode(97 + i)}`);
  s.dependents.forEach((d, i) => { for (const [k, v] of Object.entries(d)) inputs[`dependent[dep_${String.fromCharCode(97 + i)}].${k}`] = v; });
  for (const [k, v] of Object.entries(s.household)) inputs[`household.${k}`] = v;
  inputs["f4952.line1"] = s.invInterest;
  inputs["f4952.line4g"] = s.election;
  inputs["ftc.taxes"] = s.ftcTaxes;
  return inputs;
}

/** A deterministic corpus of n generated returns. */
export function sampleReturns(data: CanonicalData, n: number, seed: number): Inputs[] {
  return fc.sample(returnArbitrary(data), { seed, numRuns: n });
}
