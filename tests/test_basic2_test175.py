from unittest import TestCase

from basic2 import test175


class TestsBasic1Test175(TestCase):
    '''25. Missing Digits Finder

    Write a Python program to find the digits that are missing from a given mobile number.
    Example: [8, 9, 5, 3, 1, 6, 3, 0, 9, 2, 5]
    Output: [4, 7]
    '''

    def test_case1(self):
        self.assertListEqual(
            test175(2),
            0,
        )
