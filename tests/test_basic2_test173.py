from unittest import TestCase

from basic2 import test173


class TestsBasic1Test173(TestCase):
    '''23. Subtract Sum of Digits

    Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on.
    Continue this operation until the number is positive.
    '''

    def test_case1(self):
        self.assertListEqual(
            test173(2),
            0,
        )
