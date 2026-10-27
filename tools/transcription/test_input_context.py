"""Focused offline tests of review-context freshness, not tax formulas."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import transcribe as T
import input_context as I


def line(name, source, type='NonNegDollars'):
    return {'id': name, 'printed': '1', 'type': type, 'expr': {'op':'input', 'source':source}}


class RequiredReviewInterfaces(unittest.TestCase):
    def setUp(self):
        self.own = {'id':'own', 'lines':[
            line('own.amount', 'Amount. '+ 'Public context. '*15+'Late exception applies.'),
            {'id':'own.result', 'printed':'2', 'type':'NonNegDollars',
             'expr':{'op':'copy','from':'other.amount'}}]}
        self.other = {'id':'other', 'lines':[line('other.amount','Taxable amount only.'),
            line('other.gate','Unsupported source?', 'Bool'),
            line('other.irrelevant','Other unused question?')]}
        self.context = {'forms':[self.own,self.other], 'defs':[]}
        self.second = [{'id':'own.result', 'expr':{'op':'copy','from':'other.amount'}}]

    def prompt(self):
        own=self.own['lines'][0]
        return (f"{own['id']} (printed '1', type {own['type']}): {own['expr']['source']}\n"+
                '\n'.join(T.reference_note(self.other,l) for l in self.other['lines']))

    def assess(self,prompt=None):
        return I.assess(self.own,self.second,self.context,self.prompt() if prompt is None else prompt)

    def test_relevant_interfaces_are_sufficient(self):
        prompt=self.prompt().replace(T.reference_note(self.other,self.other['lines'][-1]),'')
        self.assertEqual(self.assess(prompt)['state'],'pass')
        self.assertEqual(len(self.assess(prompt)['required']),2)

    def test_unrelated_question_changes_neither_required_hash_nor_result(self):
        prompt=self.prompt(); before=self.assess(prompt)
        self.other['lines'][-1]['expr']['source']='Unrelated changed wording.'
        after=self.assess(prompt)
        self.assertEqual((before['state'],before['required_sha256']),(after['state'],after['required_sha256']))

    def test_late_own_input_exception_is_not_truncated(self):
        self.assertEqual(self.assess(self.prompt().replace('Late exception applies.',''))['missing'],['own:own.amount'])

    def test_relevant_foreign_wording_change_invalidates_saved_context(self):
        prompt=self.prompt(); before=self.assess(prompt)
        self.other['lines'][0]['expr']['source']='Gross amount including exempt items.'
        after=self.assess(prompt)
        self.assertEqual(after['missing'],['other:other.amount'])
        self.assertNotEqual(before['required_sha256'],after['required_sha256'])

    def test_same_question_under_another_id_cannot_fill_missing_interface(self):
        prompt=self.prompt().replace('other.amount (form','other.another (form')
        self.assertEqual(self.assess(prompt)['missing'],['other:other.amount'])

    def test_stale_type_cannot_pass_on_question_words_alone(self):
        self.assertEqual(self.assess(self.prompt().replace('type NonNegDollars','type Dollars'))['state'],'fail')

    def test_omitting_candidate_dependency_does_not_shrink_authored_boundary(self):
        self.second=[]
        self.assertIn('other:other.amount',self.assess('')['missing'])

    def test_candidate_helpers_collection_fields_and_refusal_gates_add_context(self):
        self.second.append({'id':'own.helper','expr':{'op':'sum_over','collection':'other',
            'field':'other.irrelevant','where':{'op':'test','eq':['other.gate',{'const':False}]}},
            'refuses':[{'when':'other.gate','when_known':True}]})
        result=self.assess()
        self.assertEqual(result['state'],'pass')
        self.assertEqual({r['id'] for r in result['required']},{'own.amount','other.amount','other.gate','other.irrelevant'})

    def test_definition_bindings_are_traversed_as_operands(self):
        self.second=[{'id':'own.helper','expr':{'op':'copy','from':{'def':'tax_on_amount',
            'line':'tax','bind':{'amount':'other.irrelevant'}}}}]
        self.assertIn('other.irrelevant',{r['id'] for r in self.assess()['required']})

    def test_foreign_computed_boundary_exposes_only_public_metadata(self):
        computed={'id':'other.total','printed':'2','type':'NonNegDollars','label':'PRIVATE_LABEL',
            'expr':{'op':'sum','of':['PRIVATE_EXPRESSION']}}
        self.other['lines'].append(computed)
        self.second.append({'id':'own.helper','expr':{'op':'copy','from':'other.total'}})
        result=self.assess()
        self.assertEqual(result['state'],'pass')
        self.assertNotIn('PRIVATE_',str(result))
        before=result['required_sha256']
        computed['expr']={'op':'sum','of':['ANOTHER_PRIVATE_EXPRESSION']}
        self.assertEqual(before,self.assess()['required_sha256'])

    def test_assessment_does_not_mutate_request_candidate_or_authored_data(self):
        before=copy.deepcopy((self.own,self.second,self.context,self.prompt()))
        self.assess()
        self.assertEqual(before,(self.own,self.second,self.context,self.prompt()))


if __name__=='__main__':
    unittest.main()
