from unittest import TestCase

from basic2 import test178


class TestsBasic1Test178(TestCase):
    '''28. Series Length and Terms

Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
Sample Data:
Input third term of the series: 3
Input 3rd last term: 3
Input Sum of the series: 15
Length of the series: 5
Series:
1 2 3 4 5
    '''

    def test_case1(self):
        self.assertListEqual(
            test178(2),
            0,
        )
