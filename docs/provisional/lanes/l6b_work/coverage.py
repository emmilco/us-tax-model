"""Write interview/2025/coverage/vehicles_equipment.yaml: one row per child of the three questions taken apart, and
the ordinary paths. A row answers exactly the questions asked before its child, so the lists below are in the order
the interview asks them today (read from the walk of persona 13 and from interview-coverage's messages). That order
follows reachability, not seq alone: when the engine's asking order changes, reorder the lists and run this again."""
import yaml, json

bank = yaml.safe_load(open('interview/2025/questions.yaml'))['bank']['questions']
seq = {q['input']: q.get('seq') for q in bank if q.get('order') in (255, 257, 258)}
persona = yaml.safe_load(open('interview/2025/personas/05_self_employed.yaml'))['answers']
SC = 'person[taxpayer].sc[design_studio]'
business = {k: v for k, v in persona.items() if 'scveh' not in k and '$asset' not in k and k not in ('f1040.line26',)}

def spec(path):
    s = {}
    exec(open(path).read(), s)
    return {c['id']: c for c in s['CHILDREN']}
VC, AC = spec('docs/provisional/lanes/l6b_work/scveh_spec.py'), spec('docs/provisional/lanes/l6b_work/asset_spec.py')

VEH, AST = SC + '.scveh[car]', SC + '.asset[item]'
veh_clean_2025 = [('method', 'actual'), ('parking', 0), ('employee_use', False), ('miles_business', 8000), ('miles_commuting', 0),
                  ('miles_other', 2000), ('operating', 300000), ('owned', True), ('placed', 'y2025'), ('records', True),
                  ('got_other', False), ('before_2017', False), ('converted', False), ('disposed', False), ('basis_changed', False),
                  ('short_year', False), ('for_hire', False), ('investment', False), ('others_use', False), ('leasing', None),
                  ('exempt_use', None), ('qbu_low', None), ('method_other', False),
                  ('passenger', True), ('s179_elect', 0), ('bonus_choice', 'full'), ('after_jan19', True),
                  ('bonus_same', True), ('used_before', False), ('bonus_excluded', False), ('cost', 3000000), ('quarter', 'q2')]
veh_clean_2024 = [('method', 'actual'), ('parking', 0), ('employee_use', False), ('miles_business', 8000), ('miles_commuting', 0),
                  ('miles_other', 2000), ('operating', 300000), ('owned', True), ('placed', 'y2024'), ('passenger', True),
                  ('records', True), ('got_other', False), ('converted', False), ('disposed', False), ('basis_changed', False),
                  ('short_year', False), ('for_hire', False), ('investment', False), ('others_use', False), ('method_other', False),
                  ('prior_bonus', False), ('prior_smr', False), ('prior_low_use', False)]
ast_clean_2025 = [('class', 'c00_12'), ('placed', 'y2025'), ('pct', 100), ('listed', False), ('s179', 0), ('kind_excluded', False),
                  ('software', False), ('software_spread', None), ('industry', False), ('industry_item', None),
                  ('long_production', False), ('qbu_low', None), ('got_other', False),
                  ('before_2017', False), ('ended_2025', False), ('basis_changed', False), ('short_year', False),
                  ('method_other', False), ('ads_required', False), ('outside_use', False), ('not179', False), ('bonus_choice', 'full'),
                  ('after_jan19', True), ('bonus_same', True), ('used_before', False), ('cost', 200000), ('quarter', 'q2')]
ast_clean_2024 = [('class', 'c00_12'), ('placed', 'y2024'), ('kind_excluded', False), ('software', False), ('industry', False),
                  ('long_production', False), ('listed', False), ('got_other', False), ('before_2017', False),
                  ('ended_2025', False), ('basis_changed', False), ('use_changed', False)]

def path(base, clean, child, value, changes=None):
    """the answers asked before the child, then the child; None marks a question this path does not meet"""
    ch = dict(changes or {})
    out = {}
    for k, v in clean:
        v = ch.get(k, v)
        if k == child:
            out[f'{base}.{k}'] = value
            return out
        if v is not None:
            out[f'{base}.{k}'] = v
    raise SystemExit(f'{child} is not on the path')

def whole(base, clean):
    return {f'{base}.{k}': v for k, v in clean if v is not None}

rows = []
def row(id, situation, answers, expect, uses=('business',), design='lane 6b notes'):
    rows.append(dict(id=id, design=design, situation=situation, uses=list(uses), answers=answers, expect=expect))

# the carryover
row('equipment.carryover_none', 'A filer with no business and no section 179 deduction left over from an earlier year is asked for no amount.',
    {'s179.prior_form': False}, {'proceeds': {'s179.prior_form': False}, 'not_asked': ['s179.carryover']}, uses=(),
    design='s179.line10, no carryover')
row('equipment.carryover_no_business', 'A filer has a section 179 deduction left over from an earlier year and no business in 2025.',
    {'s179.prior_form': True, 's179.carryover': 300000}, {'refused': 's179.orphan'}, uses=(),
    design='s179.line10, a carryover with no Schedule C (s179.orphan)')

# the standard mileage rate
std0 = {f'$scveh@{SC}': ['car'], f'{VEH}.method': 'standard', f'{VEH}.parking': 0}
std = {**std0, f'{VEH}.miles_business': 4200}
row('vehicles.mileage_every_year', 'A person drives their own car for the business and has always taken the standard mileage rate for it.',
    {**std, f'{VEH}.smr_always': True, f'{VEH}.fleet': False},
    {'proceeds': {f'{VEH}.smr_always': True}, 'not_asked': [f'{VEH}.smr_first', f'{VEH}.owned', f'{VEH}.records']},
    design='scveh.smr_ok, the typical vehicle')
row('vehicles.mileage_first_year_only', 'An owner took the standard mileage rate in the first year, actual expenses in a later year, and the rate again in 2025.',
    {**std, f'{VEH}.smr_always': False, f'{VEH}.smr_first': True, f'{VEH}.fleet': False},
    {'proceeds': {f'{VEH}.smr_first': True}}, design='scveh.smr_ok, owned, rate used in the first year')
row('vehicles.mileage_not_first_year', 'The standard mileage rate was not used in the first year of an owned vehicle, or not for the whole lease.',
    {**std0, f'{VEH}.smr_always': False, f'{VEH}.smr_first': False},
    {'refused': f'{VEH}.smr_bad'}, design='scveh.smr_ok answered No (first year or lease)')
row('vehicles.mileage_fleet', 'Five or more vehicles were used in the business at the same time.',
    {**std0, f'{VEH}.smr_always': True, f'{VEH}.fleet': True},
    {'refused': f'{VEH}.smr_bad'}, design='scveh.smr_ok answered No (five or more vehicles)')

# the vehicle screen
vbase = {f'$scveh@{SC}': ['car']}
row('vehicles.actual_owned_plain', 'An owned car bought new in 2025 in an ordinary way, on actual expenses, with none of the special facts.',
    {**vbase, **whole(VEH, veh_clean_2025)}, {'proceeds': {f'{VEH}.records': True}},
    design='scveh.screen answered No')
VSPEC = {
    'records': (False, veh_clean_2025, None), 'got_other': (True, veh_clean_2025, None), 'before_2017': (True, veh_clean_2025, None),
    'converted': (True, veh_clean_2025, None), 'disposed': (True, veh_clean_2025, None), 'basis_changed': (True, veh_clean_2025, None),
    'short_year': (True, veh_clean_2025, None), 'for_hire': (True, veh_clean_2025, None), 'investment': (True, veh_clean_2025, None),
    'leasing': (True, veh_clean_2025, {'others_use': True}),
    'exempt_use': (True, veh_clean_2025, {'others_use': True, 'leasing': False}),
    'qbu_low': (True, veh_clean_2025, {'others_use': True, 'leasing': False, 'exempt_use': False}),
    'method_other': (True, veh_clean_2025, None),
    'prior_bonus': (True, veh_clean_2024, None), 'prior_smr': (True, veh_clean_2024, None), 'prior_low_use': (True, veh_clean_2024, None),
    'used_before': (True, veh_clean_2025, None), 'bonus_excluded': (True, veh_clean_2025, None),
}
for child, (val, clean, changes) in VSPEC.items():
    row(f'vehicles.screen_{child}', 'An owned vehicle on actual expenses: ' + VC[f'scveh.{child}']['label'].split(';')[0][:150] + '.',
        {**vbase, **path(VEH, clean, child, val, changes)}, {'refused': f'{VEH}.screened'},
        design=f'scveh.screen item, now scveh.{child}')

# the equipment screen
abase = {f'$asset@{SC}': ['item']}
row('equipment.plain_computer', 'A computer bought new in 2025 in an ordinary way and used only in the business.',
    {**abase, **whole(AST, ast_clean_2025)}, {'proceeds': {f'{AST}.kind_excluded': False}},
    design='asset.screen answered No')
ASPEC = {
    'kind_excluded': (True, ast_clean_2025, None), 'software_spread': (True, ast_clean_2025, {'software': True}),
    'industry_item': (True, ast_clean_2025, {'industry': True}), 'long_production': (True, ast_clean_2025, None),
    'got_other': (True, ast_clean_2025, None), 'before_2017': (True, ast_clean_2025, None), 'ended_2025': (True, ast_clean_2025, None),
    'basis_changed': (True, ast_clean_2025, None), 'use_changed': (True, ast_clean_2024, None), 'short_year': (True, ast_clean_2025, None),
    'method_other': (True, ast_clean_2025, None), 'ads_required': (True, ast_clean_2025, None), 'outside_use': (True, ast_clean_2025, None),
    'qbu_low': (True, ast_clean_2025, {'listed': True}), 'used_before': (True, ast_clean_2025, None),
}
for child, (val, clean, changes) in ASPEC.items():
    row(f'equipment.screen_{child}', 'An item of equipment: ' + AC[f'asset.{child}']['label'].split(';')[0][:150] + '.',
        {**abase, **path(AST, clean, child, val, changes)}, {'refused': f'{AST}.screened'},
        design=f'asset.screen item, now asset.{child}')
row('equipment.software_expensed', 'Software first used in 2025 whose whole business cost is deducted in 2025 goes on.',
    {**abase, **whole(AST, [(k, {'software': True, 'software_spread': False}.get(k, v)) for k, v in ast_clean_2025])},
    {'proceeds': {f'{AST}.software_spread': False}}, design='asset.screen, the software exception')

doc = {'tax_year': 2025, 'part': 'Business vehicles and equipment', 'profile': 'full',
       'sets': {'business': {'says': 'A single self-employed designer with one business and an office at home (the answers of persona 05), with no vehicle or equipment unless the row lists one.',
                             'answers': {**business, f'$scveh@{SC}': [], f'$asset@{SC}': []}}},
       'rows': rows}
# a row's own roster answer replaces the set's
head = ('# Coverage rows for business vehicles and equipment (lane 6b of the provisional redraft). Written by\n'
        '# docs/provisional/lanes/l6b_work/coverage.py from the bank\'s seq numbers; see opening.yaml for how a row is read.\n')
open('interview/2025/coverage/vehicles_equipment.yaml', 'w').write(head + yaml.safe_dump(doc, sort_keys=False, width=110, allow_unicode=True))
print(len(rows), 'rows')
