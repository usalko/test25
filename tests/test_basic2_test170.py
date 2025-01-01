from unittest import TestCase

from basic2 import test170


class TestsBasic1Test170(TestCase):
    '''20. Factorial Trailing Zeros

Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
Range of the number(n): (1 <= n <= 2*109).
'''

    def test_case1(self):
        self.assertListEqual(
            test170(2),
            0,
        )
