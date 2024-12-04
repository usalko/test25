from unittest import TestCase

from basic1 import test104


class TestsBasic1Test104(TestCase):
    '''
    Write a Python program to get the effective group id, effective user id, real group id, and
    a list of supplemental group ids associated with the current process.
    Note: Availability: Unix.
    '''

    def test_case1(self):
        self.assertEqual(
            test104(),
            None,
        )
