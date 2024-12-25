from unittest import TestCase

from basic2 import test155


class TestsBasic1Test155(TestCase):
    '''5. 3-Digit Combinations

    Write a Python program to make combinations of 3 digits.
    '''

    def test_case1(self):
        self.assertEqual(
            test155(),
            None,
        )
