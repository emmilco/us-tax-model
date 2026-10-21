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
import { YEAR } from "./year.js";

const WAGE_BASE = 17_610_000; // Social Security wage base, cents
const ADDL_MEDICARE_START = 20_000_000;

function halfUp(n: number, d: number): number { return Math.floor((2 * n + d) / (2 * d)); }
function rate(amount: number, num: number, den: number): number { return halfUp(amount * num, den); }

/** Root (non-collection) input lines keyed by input key, and the collection documents. */
const HSA = "person[taxpayer].f8889[hsa]";

export function declaredInputs(data: CanonicalData): { roots: Map<string, Line>; collections: FormDoc[] } {
  const roots = new Map<string, Line>();
  const collections: FormDoc[] = [];
  for (const doc of data.forms) {
    if (doc.collection) { collections.push(doc); continue; }
    for (const line of doc.lines) if (line.expr.op === "input") roots.set(line.id, line);
  }
  // The taxpayer's own person record is generated like a root form: one entry, keyed taxpayer.
  const person = data.forms.find((doc) => doc.id === "person");
  for (const line of person?.lines ?? []) {
    if (line.expr.op === "input") roots.set(`person[taxpayer].${line.id.slice("person.".length)}`, line);
  }
  // Every generated taxpayer has one Form 8889; with no contributions it computes zero.
  const hsa = data.forms.find((doc) => doc.id === "f8889");
  for (const line of hsa?.lines ?? []) {
    if (line.expr.op === "input") roots.set(`${HSA}.${line.id.slice("f8889.".length)}`, line);
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
  "person[taxpayer].born_before_2001": 85, "eic.us_home": 95,
  "s1a.tips": 20, "s1a.overtime": 20, "s1a.carloan": 15, "person[taxpayer].died_before_65": 2,
};
const DEFAULT_TRUE_PERCENT = 10;

// Money inputs the generator models with structure; every other declared
// money input is rarely nonzero.
const MODELLED = new Set([
  "f1040.line3a", "sb.ordinary_dividends", "qbi.dividends", "sd.distributions", "div.box2b", "div.box2d",
  "sa.line1", "sa.line5a", "sa.line5b", "sa.line8a", "sa.line11", "f4952.line1", "f4952.line4g", "ftc.taxes",
  "s1.uc_paid", "s1.uc_repaid", "person[taxpayer].educator_expenses", `${HSA}.line2`, `${HSA}.line9`, `${HSA}.months_eligible`, `${HSA}.months_family`, "sli.interest",
]);

interface Employer { box1: number; box2pct: number; box7: number; over: number }
interface Sale { box: string; aggregate: boolean; code: string; special: boolean; aggregate_eligible: boolean; proceeds: number; reported_basis: number; correct_basis: number; wash_loss: number; invalid: boolean }
interface Gift { deduction: number; public_securities: boolean; special: boolean }
interface Dependent { relationship: string; age: number; younger: boolean; student: boolean; disabled: boolean; months: number; self_support: boolean; joint_return: boolean; citizen: boolean; canada_mexico: boolean; married: boolean; tin: boolean; work_ssn: boolean; gross_income: number; supported: boolean; other_claimant: boolean; divorced_rule: boolean; multiple_support: boolean; parent_home_paid: boolean; us_half: boolean; eic_ssn: boolean }
interface Household { taxpayer_tin: boolean; taxpayer_work_ssn: boolean; home_cost: boolean; unmarried: boolean }
interface Distribution { account: string; code: string; box1: number; box5: number; rollover: number; special: boolean; annuity: boolean; cost: number; used_last_year: boolean; last_line4: number; joint_life: boolean; age: number; combined_age: number; months: number; recovered: number }

interface TipJob { qualified: boolean; amount: number }
interface OvertimeJob { flsa: boolean; special: boolean; method: string; statement: number }
interface CarLoan { kind: string; requirements: boolean; vehicle: boolean; interest: number; mixed: boolean; financed: number; nonqualifying: number; down: number; refiBalance: number; refiWhole: boolean }
interface ScheduleOneA { tips: TipJob[]; overtime: OvertimeJob[]; loans: CarLoan[] }
interface SpouseHsa { has: boolean; months: number; familyMonths: number; decFamily: boolean; contrib: number; age55: boolean; agreed: boolean; allocated: number }
interface Spouse {
  employers: Employer[]; age65: boolean; blind: boolean; tin: boolean; work_ssn: boolean; died: boolean; eicAge: boolean;
  educator: number; eligible: boolean; tips: TipJob[]; overtime: OvertimeJob[]; hsa: SpouseHsa;
}

interface Vehicle {
  standard: boolean; owned: boolean; year: number; business: number; commuting: number; other: number; parking: number;
  operating: number; lease: number; cost: number; passenger: boolean; s179: number; afterJan19: boolean; bonus: string;
  prior179: number; quarter: string; priorConv: string;
}
interface Asset { cls: number; year: number; cost: number; pct: number; listed: boolean; quarter: string; s179: number; afterJan19: boolean; bonus: string; priorConv: string; prior179: number; priorBonus: number }
interface Business {
  receipts: number; returns: number; other: number; expenses: number[]; inventory: boolean; purchases: number; endInv: number;
  home: boolean; sqft: number; homeSqft: number; health: boolean; premiums: number; ltc: { payments: number; age: string }[];
  vehicles: Vehicle[]; assets: Asset[];
}
interface Plan { kind: string; sepRate: number; sepContrib: number; deferral: number; age: string; formula: string; employer: number }

interface Adjustments {
  uc: number; ucRepaidPct: number; educator: number; sli: number;
  hsa: boolean; months: number; familyMonths: number; decFamily: boolean; contrib: number; employer: number;
}

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
  spouse: Spouse;
  household: Household;
  pensions: Distribution[];
  benefits: number;
  adj: Adjustments;
  s1a: ScheduleOneA;
  flags: Record<string, boolean>;
  extras: Record<string, number>;
  businesses: Business[]; plan: Plan; spouseBusinesses: Business[]; spousePlan: Plan;
}

// The Schedule C expense lines the generator fills (Part II), each usually zero.
const SC_EXPENSES = ["line8", "line10", "line11", "line14", "line15", "line16a", "line16b", "line17", "line18", "line19",
  "rent_equipment", "line20b", "line21", "line22", "line23", "line24a", "meals_50", "meals_80", "meals_100", "line25", "line26", "line48"];

function businessArbitrary(): fc.Arbitrary<Business> {
  const vehicle = fc.record<Vehicle>({
    standard: fc.boolean(), owned: rareTrue(85), year: fc.integer({ min: YEAR - 6, max: YEAR }),
    business: fc.integer({ min: 1_000, max: 30_000 }), commuting: rareMoney(5_000, 30), other: fc.oneof({ weight: 4, arbitrary: fc.integer({ min: 0, max: 4_000 }) }, { weight: 1, arbitrary: fc.integer({ min: 0, max: 30_000 }) }),
    parking: rareMoney(100_000, 30), operating: money(1_000_000), lease: money(800_000), cost: fc.integer({ min: 500_000, max: 8_000_000 }),
    passenger: rareTrue(85), s179: rareMoney(3_000_000, 15), afterJan19: rareTrue(80), bonus: fc.constantFrom("none", "none", "full", "forty"),
    prior179: rareMoney(1_000_000, 15), quarter: fc.constantFrom("q1", "q2", "q3", "q4"), priorConv: fc.constantFrom("hy", "hy", "hy", "mq1", "mq2", "mq3", "mq4"),
  });
  const asset = fc.record<Asset>({
    cls: fc.nat(), year: fc.oneof({ weight: 3, arbitrary: fc.constant(YEAR) }, { weight: 2, arbitrary: fc.integer({ min: YEAR - 20, max: YEAR - 1 }) }),
    cost: fc.integer({ min: 10_000, max: 5_000_000 }), pct: fc.oneof({ weight: 4, arbitrary: fc.constant(100) }, { weight: 1, arbitrary: fc.integer({ min: 1, max: 100 }) }),
    listed: rareTrue(10), quarter: fc.constantFrom("q1", "q2", "q3", "q4", "q4"), s179: rareMoney(2_000_000, 25), afterJan19: rareTrue(80),
    bonus: fc.constantFrom("none", "none", "full", "forty"), priorConv: fc.constantFrom("hy", "hy", "hy", "mq1", "mq2", "mq3", "mq4"),
    prior179: rareMoney(1_000_000, 10), priorBonus: rareMoney(1_000_000, 10),
  });
  return fc.record<Business>({
    receipts: money(25_000_000), returns: rareMoney(500_000, 10), other: rareMoney(500_000, 10),
    expenses: fc.array(rareMoney(3_000_000, 25), { minLength: SC_EXPENSES.length, maxLength: SC_EXPENSES.length }),
    inventory: rareTrue(20), purchases: money(5_000_000), endInv: money(2_000_000),
    home: rareTrue(20), sqft: fc.integer({ min: 20, max: 450 }), homeSqft: fc.integer({ min: 500, max: 3_000 }),
    health: rareTrue(15), premiums: money(2_000_000),
    ltc: fc.array(fc.record({ payments: money(800_000), age: fc.constantFrom("to40", "to50", "to60", "to70", "over70") }), { maxLength: 1 }),
    vehicles: fc.array(vehicle, { maxLength: 2 }), assets: fc.array(asset, { maxLength: 2 }),
  });
}

const planArbitrary = fc.record<Plan>({
  kind: fc.constantFrom("none", "none", "none", "none", "none", "none", "sep", "simple"), sepRate: fc.integer({ min: 1, max: 25 }),
  sepContrib: fc.oneof({ weight: 9, arbitrary: money(300_000) }, { weight: 1, arbitrary: money(7_000_000) }), deferral: fc.oneof({ weight: 9, arbitrary: money(1_000_000) }, { weight: 1, arbitrary: money(2_000_000) }), age: fc.constantFrom("under50", "under50", "age50", "age60_63"),
  formula: fc.constantFrom("match", "nonelective"), employer: fc.oneof({ weight: 9, arbitrary: money(60_000) }, { weight: 1, arbitrary: money(600_000) }),
});

/** One person's businesses: each Schedule C with its vehicles, other property and long-term care entries, and the
 * person's SEP or SIMPLE plan. Facts outside the tool's scope are given their supported answer; the screens that refuse
 * them are root inputs, varied with the other flags. */
function putBusinesses(data: CanonicalData, inputs: Inputs, P: string, list: Business[], plan: Plan): void {
  const classes = (data.tables.find((t) => t.id === "class_lives")?.rows ?? []).filter((r) => r.value !== "outside").map((r) => String(r.keys[0]));
  const keys = list.map((_, i) => `biz_${String.fromCharCode(97 + i)}`);
  inputs[`$sc@${P}`] = keys;
  list.forEach((b, i) => {
    const E = `${P}.sc[${keys[i]}]`;
    Object.assign(inputs, {
      [`${E}.statutory`]: false, [`${E}.passive`]: true, [`${E}.spouse_owned`]: false, [`${E}.method_other`]: false, [`${E}.special`]: false,
      [`${E}.at_risk`]: true, [`${E}.inventory_other`]: false, [`${E}.tips_ot`]: false,
      [`${E}.line1`]: b.receipts, [`${E}.line2`]: Math.min(b.returns, b.receipts), [`${E}.line6`]: b.other,
      [`${E}.line35`]: 0, [`${E}.line36`]: b.inventory ? b.purchases : 0, [`${E}.line37`]: 0, [`${E}.line38`]: 0, [`${E}.line39`]: 0,
      [`${E}.line41`]: b.inventory ? Math.min(b.endInv, b.purchases) : 0,
      [`${E}.ho_uses`]: b.home, [`${E}.hi_uses`]: b.health,
    });
    SC_EXPENSES.forEach((k, j) => { inputs[`${E}.${k}`] = b.expenses[j]!; });
    // Every field of the entry gets a value, as every root input does; the home office and health insurance
    // answers are read only when their question is answered yes.
    Object.assign(inputs, { [`${E}.ho_other`]: false, [`${E}.ho_sqft`]: b.home ? b.sqft : 0, [`${E}.ho_home_sqft`]: b.home ? Math.max(b.homeSqft, b.sqft) : 0,
      [`${E}.hi_screen`]: false, [`${E}.f7206_line1`]: b.health ? b.premiums : 0 });
    const ltc = b.health ? b.ltc : [];
    inputs[`$ltc@${E}`] = ltc.map((_, k) => (k === 0 ? "self" : `p${k}`));
    ltc.forEach((l, k) => { const L = `${E}.ltc[${k === 0 ? "self" : `p${k}`}]`; inputs[`${L}.payments`] = l.payments; inputs[`${L}.age`] = l.age; });
    inputs[`$scveh@${E}`] = b.vehicles.map((_, k) => `car_${k + 1}`);
    b.vehicles.forEach((v, k) => {
      const V = `${E}.scveh[car_${k + 1}]`;
      // The standard mileage rate only from the first year (owned) or for a whole lease; actual expenses otherwise.
      const method = v.standard ? "standard" : "actual";
      const s179 = method === "actual" && v.owned && v.year === YEAR ? Math.min(v.s179, v.cost) : 0;
      Object.assign(inputs, {
        [`${V}.method`]: method, [`${V}.owned`]: v.owned, [`${V}.placed_date`]: v.year, [`${V}.miles_business`]: v.business,
        [`${V}.miles_commuting`]: v.commuting, [`${V}.miles_other`]: v.other, [`${V}.parking`]: v.parking, [`${V}.smr_ok`]: true,
        [`${V}.operating`]: v.operating, [`${V}.lease`]: v.lease, [`${V}.placed`]: `y${v.year}`, [`${V}.screen`]: false,
        [`${V}.cost`]: v.cost, [`${V}.passenger`]: v.passenger, [`${V}.suv`]: false, [`${V}.s179_elect`]: s179,
        [`${V}.after_jan19`]: v.afterJan19, [`${V}.bonus_choice`]: v.year === YEAR ? v.bonus : "none", [`${V}.bonus_same`]: true,
        [`${V}.prior_179`]: v.year === YEAR ? 0 : Math.min(v.prior179, v.cost), [`${V}.quarter`]: v.quarter, [`${V}.prior_conv`]: v.priorConv,
      });
    });
    inputs[`$asset@${E}`] = b.assets.map((_, k) => `item_${k + 1}`);
    b.assets.forEach((a, k) => {
      const A = `${E}.asset[item_${k + 1}]`;
      const now = a.year === YEAR;
      const businessCost = Math.floor((a.cost * a.pct) / 100);
      Object.assign(inputs, {
        [`${A}.class`]: classes[a.cls % Math.max(1, classes.length)], [`${A}.screen`]: false, [`${A}.placed`]: `y${a.year}`,
        [`${A}.cost`]: a.cost, [`${A}.pct`]: a.listed ? Math.max(a.pct, 51) : a.pct, [`${A}.listed`]: a.listed, [`${A}.quarter`]: a.quarter,
        [`${A}.s179`]: now && a.pct > 50 ? Math.min(a.s179, businessCost) : 0, [`${A}.after_jan19`]: a.afterJan19,
        [`${A}.bonus_choice`]: a.bonus, [`${A}.bonus_same`]: true, [`${A}.prior_conv`]: a.priorConv,
        [`${A}.prior_179`]: now ? 0 : Math.min(a.prior179, businessCost), [`${A}.prior_bonus`]: now ? 0 : Math.min(a.priorBonus, Math.max(0, businessCost - Math.min(a.prior179, businessCost))),
      });
    });
  });
  {
    // The taxpayer's screens are root inputs, already varied with the other flags; the spouse's are set here.
    inputs[`${P}.se_screen`] ??= false;
    inputs[`${P}.plan`] = plan.kind;
    inputs[`${P}.plan_screen`] ??= false;
    Object.assign(inputs, { [`${P}.sep_rate`]: plan.sepRate, [`${P}.sep_contrib`]: plan.sepContrib, [`${P}.simple_deferral`]: plan.deferral,
      [`${P}.simple_age`]: plan.age, [`${P}.simple_kind`]: plan.formula, [`${P}.simple_employer`]: plan.employer });
  }
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
    younger: rareTrue(90), student: rareTrue(30), disabled: rareTrue(5),
    months: fc.oneof({ weight: 4, arbitrary: fc.constant(12) }, { weight: 1, arbitrary: fc.integer({ min: 0, max: 12 }) }),
    self_support: rareTrue(5), joint_return: rareTrue(3), citizen: rareTrue(90), canada_mexico: rareTrue(20), married: rareTrue(3),
    tin: rareTrue(95), work_ssn: rareTrue(90), gross_income: rareMoney(1_000_000, 20), supported: rareTrue(90),
    other_claimant: rareTrue(3), divorced_rule: rareTrue(3), multiple_support: rareTrue(2), parent_home_paid: rareTrue(30),
    us_half: rareTrue(85), eic_ssn: rareTrue(90),
  });
  const household = fc.record<Household>({
    taxpayer_tin: rareTrue(97), taxpayer_work_ssn: rareTrue(93),
    home_cost: rareTrue(70), unmarried: rareTrue(90),
  });
  const distribution = fc.record<Distribution>({
    account: fc.constantFrom("traditional_ira", "traditional_ira", "plan", "plan", "roth_ira"),
    code: fc.constantFrom("normal_7", "normal_7", "normal_7", "death_4", "early_exception_2", "direct_rollover_G", "qualified_roth_Q", "other"),
    box1: money(6_000_000), box5: rareMoney(500_000, 20), rollover: rareMoney(3_000_000, 15),
    special: rareTrue(5), annuity: rareTrue(30),
    cost: money(20_000_000), used_last_year: rareTrue(40), last_line4: money(200_000),
    joint_life: rareTrue(30), age: fc.integer({ min: 50, max: 80 }), combined_age: fc.integer({ min: 100, max: 160 }),
    months: fc.oneof({ weight: 4, arbitrary: fc.constant(12) }, { weight: 1, arbitrary: fc.integer({ min: 1, max: 12 }) }),
    recovered: money(5_000_000),
  });
  const gift = fc.record<Gift>({
  deduction: fc.oneof({ weight: 3, arbitrary: money(500_000) }, { weight: 1, arbitrary: fc.integer({ min: 500_001, max: 2_000_000 }) }),
  public_securities: fc.boolean(),
  special: rareTrue(5),
});
  const spec = fc.record<Spec>({
    status: fc.constantFrom("single", "single", "single", "hoh", "mfj", "mfs", "qss"),
    profile: fc.constantFrom("wage", "wage", "wage", "investor", "low", "low", "retiree", "retiree"),
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
    // Read only on a joint return: the spouse's own entry.
    spouse: fc.record<Spouse>({
      employers: fc.array(employer, { maxLength: 2 }), age65: rareTrue(25), blind: rareTrue(5), tin: rareTrue(97), work_ssn: rareTrue(93),
      died: rareTrue(3), eicAge: rareTrue(85), educator: rareMoney(60_000, 15), eligible: rareTrue(70),
      tips: fc.array(fc.record<TipJob>({ qualified: fc.constant(true), amount: money(3_000_000) }), { maxLength: 2 }),
      overtime: fc.array(fc.record<OvertimeJob>({ flsa: fc.constant(true), special: fc.constant(false), method: fc.constantFrom("premium", "employer_reported", "total_time_and_half"), statement: money(3_000_000) }), { maxLength: 1 }),
      hsa: fc.record<SpouseHsa>({ has: rareTrue(30), months: fc.oneof({ weight: 1, arbitrary: fc.constant(12) }, { weight: 1, arbitrary: fc.integer({ min: 1, max: 12 }) }),
        familyMonths: fc.integer({ min: 0, max: 12 }), decFamily: fc.boolean(), contrib: money(1_000_000), age55: rareTrue(25), agreed: rareTrue(20), allocated: money(855_000) }),
    }),
    household,
    pensions: fc.array(distribution, { minLength: 1, maxLength: 2 }),
    benefits: money(5_000_000),
    adj: fc.record<Adjustments>({
      uc: rareMoney(2_500_000, 15), ucRepaidPct: rareMoney(100, 20), educator: rareMoney(60_000, 10), sli: rareMoney(300_000, 20),
      hsa: rareTrue(15), months: fc.oneof({ weight: 1, arbitrary: fc.constant(12) }, { weight: 1, arbitrary: fc.integer({ min: 0, max: 12 }) }),
      familyMonths: fc.integer({ min: 0, max: 12 }), decFamily: fc.boolean(), contrib: money(1_000_000), employer: rareMoney(300_000, 30),
    }),
    // Schedule 1-A collections, read only when their part is claimed: employers with tips, employers
    // with overtime (every method, rarely a refused one) and car loans of each kind, sometimes mixed.
    s1a: fc.record<ScheduleOneA>({
      tips: fc.array(fc.record<TipJob>({ qualified: fc.oneof({ weight: 19, arbitrary: fc.constant(true) }, { weight: 1, arbitrary: fc.constant(false) }), amount: money(3_000_000) }), { maxLength: 3 }),
      overtime: fc.array(fc.record<OvertimeJob>({
        flsa: fc.oneof({ weight: 9, arbitrary: fc.constant(true) }, { weight: 1, arbitrary: fc.constant(false) }), special: rareTrue(5),
        method: fc.constantFrom("employer_reported", "premium", "total_time_and_half", "premium_double", "total_double", "employer_reported", "premium", "other"),
        statement: money(4_000_000) }), { maxLength: 2 }),
      loans: fc.array(fc.record<CarLoan>({
        kind: fc.constantFrom("original", "original", "original", "refinanced", "death"),
        requirements: fc.oneof({ weight: 9, arbitrary: fc.constant(true) }, { weight: 1, arbitrary: fc.constant(false) }),
        vehicle: fc.oneof({ weight: 9, arbitrary: fc.constant(true) }, { weight: 1, arbitrary: fc.constant(false) }),
        interest: money(1_500_000), mixed: rareTrue(25), financed: fc.integer({ min: 1, max: 8_000_000 }),
        nonqualifying: money(1_000_000), down: money(1_000_000), refiBalance: money(8_000_000),
        refiWhole: fc.oneof({ weight: 19, arbitrary: fc.constant(true) }, { weight: 1, arbitrary: fc.constant(false) }) }), { maxLength: 2 }),
    }),
    flags: fc.record(Object.fromEntries(boolKeys.map((k) => [k, rareTrue(BOOL_TRUE_PERCENT[k] ?? DEFAULT_TRUE_PERCENT)]))),
    extras: fc.record(Object.fromEntries(extraKeys.map((k) => [k, rareMoney(500_000, 2)]))),
    // About a third of returns have a business; a joint return's spouse sometimes has one as well.
    businesses: fc.oneof({ weight: 6, arbitrary: fc.constant<Business[]>([]) }, { weight: 3, arbitrary: fc.array(businessArbitrary(), { minLength: 1, maxLength: 1 }) },
      { weight: 1, arbitrary: fc.array(businessArbitrary(), { minLength: 2, maxLength: 2 }) }),
    plan: planArbitrary,
    spouseBusinesses: fc.oneof({ weight: 4, arbitrary: fc.constant<Business[]>([]) }, { weight: 1, arbitrary: fc.array(businessArbitrary(), { minLength: 1, maxLength: 1 }) }),
    spousePlan: planArbitrary,
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
  // The EIC's birth-date question agrees with the age-65 answer: no generated filer is born on January 1, 1961.
  inputs["person[taxpayer].born_after_1960"] = inputs["person[taxpayer].age65"] !== true;
  inputs["f1040.status"] = s.status;
  // An investor has no wages and only qualified dividends and gains, which is
  // the only way the worksheets' upper skip rules and ceilings are reached. A
  // low earner has modest wages, little interest and no dividends or sales,
  // the returns on which the earned income credit is figured.
  const investor = s.profile === "investor";
  const low = s.profile === "low";

  inputs["$person"] = ["taxpayer"];
  inputs["person[taxpayer].role"] = "taxpayer";
  inputs["$f8889@person[taxpayer]"] = ["hsa"];
  inputs["qbi.carryforward"] = 0;
  putBusinesses(data, inputs, "person[taxpayer]", s.profile === "investor" || s.profile === "retiree" ? [] : s.businesses, s.plan);
  inputs["person[taxpayer].rrta"] = s.rrta;
  const employers = s.employers.map((_, i) => `emp_${String.fromCharCode(97 + i)}`);
  inputs["$w2@person[taxpayer]"] = employers;
  s.employers.forEach((e, i) => {
    const p = `person[taxpayer].w2[${employers[i]}]`;
    const box1 = investor ? 0 : low ? e.box1 % 7_000_000 : e.box1;
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

  const interest = investor ? [] : low ? s.interest.map((a) => a % 50_000) : s.interest;
  inputs["$interest"] = interest.map((_, i) => `bank_${String.fromCharCode(97 + i)}`);
  interest.forEach((a, i) => { inputs[`interest[bank_${String.fromCharCode(97 + i)}].amount`] = a; });

  const ordinary = investor ? s.ordinary * 4 : low ? 0 : s.ordinary;
  inputs["sb.ordinary_dividends"] = ordinary;
  inputs["f1040.line3a"] = s.badDividends ? ordinary + 100 : rate(ordinary, investor ? 100 : s.qpct, 100);
  inputs["qbi.dividends"] = rate(ordinary, s.qbipct, 100);
  const distributions = low ? 0 : s.distributions;
  inputs["sd.distributions"] = distributions;
  const box2b = rate(distributions, s.b2bpct, 100);
  inputs["div.box2b"] = box2b;
  inputs["div.box2d"] = rate(distributions - box2b, s.b2dpct, 100);

  const sales = low ? [] : s.sales;
  inputs["$sales"] = sales.map((_, i) => `s${i + 1}`);
  sales.forEach((sale, i) => {
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
  const HOUSEHOLD_KEYS: Record<string, string> = { taxpayer_tin: "person[taxpayer].tin", taxpayer_work_ssn: "person[taxpayer].work_ssn" };
  for (const [k, v] of Object.entries(s.household)) inputs[HOUSEHOLD_KEYS[k] ?? `household.${k}`] = v;
  inputs["person[taxpayer].itin_applied"] = false;
  // A retiree has Form 1099-R distributions and social security benefits; the other
  // profiles have neither. A Roth IRA is given code Q and a code that the
  // account does not allow is kept only on unclean returns, so the gates are exercised too.
  const retiree = s.profile === "retiree";
  const dists = retiree ? s.pensions : [];
  inputs["$retirement"] = dists.map((_, i) => `r${i + 1}`);
  dists.forEach((d, i) => {
    const code = s.clean ? (d.account === "roth_ira" ? "qualified_roth_Q" : d.code === "qualified_roth_Q" || d.code === "other" ? "normal_7" : d.code) : d.code;
    const entry = { ...d, code, special: s.clean ? false : d.special, annuity: d.account === "plan" && d.annuity,
      box5: d.account === "plan" ? d.box5 : 0, rollover: Math.min(d.rollover, d.box1) };
    for (const [k, v] of Object.entries(entry)) inputs[`retirement[r${i + 1}].${k}`] = v;
  });
  inputs["ssb.benefits"] = retiree ? s.benefits : 0;
  // Schedule 1 items: unemployment (with part of a current-year overpayment sometimes repaid), educator expenses,
  // student loan interest, and an HSA whose month counts are always possible (family months at most the
  // eligible months, December coverage present when eligible all year); the screens are flags.
  inputs["s1.uc_paid"] = s.adj.uc;
  inputs["s1.uc_repaid"] = Math.floor((s.adj.uc * s.adj.ucRepaidPct) / 100);
  inputs["person[taxpayer].educator_expenses"] = s.adj.educator;
  inputs["sli.interest"] = s.adj.sli;
  if (s.adj.hsa) {
    const months = s.adj.months, family = Math.min(s.adj.familyMonths, months);
    inputs[`${HSA}.months_eligible`] = months;
    inputs[`${HSA}.months_family`] = family;
    inputs[`${HSA}.dec_coverage`] = months === 0 ? "none" : family === months ? "family" : family === 0 ? "self_only" : s.adj.decFamily ? "family" : "self_only";
    inputs[`${HSA}.line2`] = s.adj.contrib;
    inputs[`${HSA}.line9`] = s.adj.employer;
  }
  inputs["f4952.line1"] = s.invInterest;
  inputs["f4952.line4g"] = s.election;
  inputs["ftc.taxes"] = s.ftcTaxes;
  if (inputs["s1a.tips"] === true) {
    inputs["$tipjob@person[taxpayer]"] = s.s1a.tips.map((_, i) => `tip_${i + 1}`);
    s.s1a.tips.forEach((t, i) => { inputs[`person[taxpayer].tipjob[tip_${i + 1}].qualified`] = t.qualified; inputs[`person[taxpayer].tipjob[tip_${i + 1}].amount`] = t.amount; });
  }
  if (inputs["s1a.overtime"] === true) {
    inputs["$otjob@person[taxpayer]"] = s.s1a.overtime.map((_, i) => `ot_${i + 1}`);
    s.s1a.overtime.forEach((o, i) => {
      const k = `person[taxpayer].otjob[ot_${i + 1}]`;
      inputs[`${k}.flsa`] = o.flsa; inputs[`${k}.special_rule`] = o.special; inputs[`${k}.method`] = o.method; inputs[`${k}.statement`] = o.statement;
    });
  }
  if (inputs["s1a.carloan"] === true) {
    inputs["$carloan"] = s.s1a.loans.map((_, i) => `vin_${i + 1}`);
    s.s1a.loans.forEach((l, i) => {
      const k = `carloan[vin_${i + 1}]`;
      inputs[`${k}.kind`] = l.kind; inputs[`${k}.requirements`] = l.requirements; inputs[`${k}.vehicle`] = l.vehicle;
      inputs[`${k}.interest`] = l.interest; inputs[`${k}.mixed`] = l.mixed; inputs[`${k}.financed`] = l.financed;
      inputs[`${k}.nonqualifying`] = l.nonqualifying; inputs[`${k}.down`] = l.down;
      inputs[`${k}.refi_balance`] = l.refiBalance; inputs[`${k}.refi_whole`] = l.refiWhole;
      // Column (ii): part of the interest deducted on a Schedule C, when the return has one.
      inputs[`${k}.col_ii_input`] = s.businesses.length > 0 || s.spouseBusinesses.length > 0 ? Math.floor(l.interest / 4) : 0;
    });
  }
  // A joint return has an entry for your spouse, with its own facts, wages and entries.
  if (s.status === "mfj") {
    const sp = s.spouse, P = "person[spouse]", H = `${P}.f8889[hsa]`;
    inputs["$person"] = ["taxpayer", "spouse"];
    Object.assign(inputs, {
      [`${P}.role`]: "spouse", [`${P}.rrta`]: false, [`${P}.age65`]: sp.age65, [`${P}.blind`]: sp.blind, [`${P}.tin`]: sp.tin || sp.work_ssn,
      [`${P}.work_ssn`]: sp.work_ssn, [`${P}.itin_applied`]: false, [`${P}.born_before_2001`]: sp.eicAge || sp.age65, [`${P}.born_after_1960`]: !sp.age65 && sp.eicAge,
      [`${P}.educator_expenses`]: sp.educator, [`${P}.eligible_educator`]: sp.eligible,
    });
    if (sp.age65) inputs[`${P}.died_before_65`] = sp.died;
    const keys = sp.employers.map((_, k) => `emp_${String.fromCharCode(97 + k)}`);
    inputs[`$w2@${P}`] = keys;
    sp.employers.forEach((e, k) => {
      const box1 = e.box1, box3 = Math.min(box1, Math.max(0, WAGE_BASE - e.box7)), box5 = box1 + e.box7;
      Object.assign(inputs, { [`${P}.w2[${keys[k]}].box1`]: box1, [`${P}.w2[${keys[k]}].box2`]: rate(box1, e.box2pct, 100), [`${P}.w2[${keys[k]}].box3`]: box3,
        [`${P}.w2[${keys[k]}].box7`]: e.box7, [`${P}.w2[${keys[k]}].box4`]: rate(box3 + e.box7, 62, 1000) + e.over,
        [`${P}.w2[${keys[k]}].box5`]: box5, [`${P}.w2[${keys[k]}].box6`]: rate(box5, 145, 10000) + (box5 > ADDL_MEDICARE_START ? rate(box5 - ADDL_MEDICARE_START, 9, 1000) : 0) });
    });
    inputs[`$tipjob@${P}`] = inputs["s1a.tips"] === true ? sp.tips.map((_, k) => `tip_${k + 1}`) : [];
    if (inputs["s1a.tips"] === true) sp.tips.forEach((tj, k) => { inputs[`${P}.tipjob[tip_${k + 1}].qualified`] = tj.qualified; inputs[`${P}.tipjob[tip_${k + 1}].amount`] = tj.amount; });
    inputs[`$otjob@${P}`] = inputs["s1a.overtime"] === true ? sp.overtime.map((_, k) => `ot_${k + 1}`) : [];
    if (inputs["s1a.overtime"] === true) sp.overtime.forEach((o, k) => {
      const k2 = `${P}.otjob[ot_${k + 1}]`;
      inputs[`${k2}.flsa`] = o.flsa; inputs[`${k2}.special_rule`] = o.special; inputs[`${k2}.method`] = o.method; inputs[`${k2}.statement`] = o.statement;
    });
    const h = sp.hsa;
    inputs[`$f8889@${P}`] = h.has ? ["hsa"] : [];
    putBusinesses(data, inputs, P, s.spouseBusinesses, s.spousePlan);
    if (h.has) {
      const family = Math.min(h.familyMonths, h.months);
      Object.assign(inputs, { [`${H}.line2`]: h.contrib, [`${H}.line9`]: 0, [`${H}.unsupported`]: false, [`${H}.months_eligible`]: h.months,
        [`${H}.months_family`]: family, [`${H}.age55`]: h.age55, [`${H}.last_month`]: false,
        [`${H}.dec_coverage`]: h.months === 12 ? (family === 12 ? "family" : family === 0 ? "self_only" : h.decFamily ? "family" : "self_only") : (h.decFamily && family > 0 ? "family" : "self_only"),
        [`${H}.allocation`]: h.agreed ? "agreed" : "equal", [`${H}.allocated`]: h.allocated });
      // Your own Form 8889 uses the same allocation method; an agreed part is drawn from the same range.
      inputs[`${HSA}.allocation`] = h.agreed ? "agreed" : "equal";
      inputs[`${HSA}.allocated`] = Math.max(0, 855_000 - h.allocated);
    }
  }
  return inputs;
}

/** A deterministic corpus of n generated returns. */
export function sampleReturns(data: CanonicalData, n: number, seed: number): Inputs[] {
  return fc.sample(returnArbitrary(data), { seed, numRuns: n });
}
