from unittest import TestCase

from basic2 import test164


class TestsBasic1Test164(TestCase):
    '''14. Add Without Plus

    Write a Python program to add two positive integers without using the '+' operator.
    Note: Use bit wise operations to add two numbers.
    '''

    def test_case1(self):
        self.assertEqual(
            test164(),
            None,
        )
