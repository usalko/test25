from unittest import TestCase

from basic1 import test089


class TestsBasic1Test089(TestCase):
    '''
    Write a Python program to perform an action if a condition is true.
    Given a variable name, if the value is 1, display the string "First day of a Month!"
    and do nothing if the value is not equal.
    '''

    def test_case1(self):
        tested_value = 2
        self.assertEqual(
            test089(tested_value, 1),
            None,
        )

    def test_case2(self):
        tested_value = 1
        self.assertEqual(
            test089(tested_value, 1),
            'First day of a Month!',
        )
