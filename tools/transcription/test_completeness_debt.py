#!/usr/bin/env python3
"""Regression checks for debt invalidation without qualifying stale receipts."""
import copy
import hashlib
import unittest
import completeness_debt as debt


class DebtTests(unittest.TestCase):
    def setUp(self):
        self.form = {'id': 'x', 'lines': [{'id': 'x.a', 'expr': {'op': 'copy', 'from': 'y.a'}}]}
        self.sections = [('instructions', 1, 1, 'Original source')]
        self.sha = 'a' * 64
        self.baseline = hashlib.sha256(self.sha.encode()).hexdigest()[:16]
        self.local = debt.subject(self.form, self.sections, 'policy')
        self.record = {'policy': debt.POLICY, 'origin_commit': 'b' * 40,
                       'prompt_sha': self.sha, 'subject': self.local}

    def test_foreign_context_change_preserves_only_deferred_debt(self):
        # A new full prompt would have a different hash; the local subject stays unchanged.
        self.assertTrue(debt.eligible(self.record, self.baseline, self.local, None))
        for receipt in [{'prompt_sha': self.sha}, {'prompt_sha': 'changed'}, {'parse_error': True}, {}]:
            self.assertFalse(debt.eligible(self.record, self.baseline, self.local, receipt))

    def test_own_arithmetic_source_and_policy_changes_invalidate(self):
        changed = copy.deepcopy(self.form)
        changed['lines'][0]['expr']['from'] = 'y.b'
        for current in [debt.subject(changed, self.sections, 'policy'),
                        debt.subject(self.form, [('instructions', 1, 1, 'Changed source')], 'policy'),
                        debt.subject(self.form, self.sections, 'changed policy')]:
            self.assertFalse(debt.eligible(self.record, self.baseline, current, None))

    def test_checker_keeps_full_prompt_for_stale_receipts(self):
        from unittest.mock import patch
        import check_completeness as checker
        local = debt.subject(self.form, self.sections, checker.SYSTEM)
        record = {**self.record, 'subject': local}
        kwargs = {'debt': {'stale:x': record}, 'baseline': {'stale:x': self.baseline}}
        with patch.object(checker, 'prompt_for', return_value=('new prompt', [], 'c' * 64)), patch.object(
                checker, 'sections', return_value=(self.sections, [])):
            pending, _ = checker.findings([self.form], {}, {}, **kwargs)
            self.assertEqual(pending[0]['subject'], self.sha)
            stale, _ = checker.findings([self.form], {}, {'x': {'prompt_sha': self.sha}}, **kwargs)
            self.assertEqual(stale[0]['subject'], 'c' * 64)
            current, _ = checker.findings([self.form], {}, {'x': {'prompt_sha': 'c' * 64, 'claims': []}}, **kwargs)
            self.assertEqual(current, [])

    def test_bad_migration_fails_closed(self):
        for key, value in [('policy', 'unknown'), ('prompt_sha', 'c' * 64),
                           ('origin_commit', ''), ('subject', 'wrong')]:
            record = {**self.record, key: value}
            self.assertFalse(debt.eligible(record, self.baseline, self.local, None))
        self.assertFalse(debt.eligible(None, self.baseline, self.local, None))


if __name__ == '__main__':
    unittest.main()
