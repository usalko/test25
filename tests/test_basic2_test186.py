from unittest import TestCase

from basic2 import test186


class TestsBasic1Test186(TestCase):
    '''36. Debt Calculation

Write a Python program to compute the amount of debt in n months. Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.
Input:
An integer n (0 <= n <= 100)
Input number of months: 7
Amount of debt: $144000
    '''

    def test_case1(self):
        self.assertListEqual(
            test186(2),
            0,
        )
