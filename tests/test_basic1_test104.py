from os import name
from unittest import TestCase

from basic1 import test104


class TestsBasic1Test104(TestCase):
    '''
    Write a Python program to get the effective group id, effective user id, real group id, and
    a list of supplemental group ids associated with the current process.
    Note: Availability: Unix.
    '''

    def test_case1(self):
        if name != 'posix':
            return
        effective_group_id, effective_user_id, real_group_id, supplemental_groups = test104()
        self.assertIsNotNone(
            effective_group_id
        )
        self.assertIsNotNone(
            effective_user_id
        )
        self.assertIsNotNone(
            real_group_id
        )
        self.assertIsNotNone(
            supplemental_groups
        )

