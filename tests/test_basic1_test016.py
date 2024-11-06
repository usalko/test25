from unittest import TestCase
from basic1 import test016
from datetime import datetime


class TestsBasic1Test016(TestCase):
    '''
    Write a Python program to calculate the difference between a given number and 17.
    If the number is greater than 17, return twice the absolute difference.
    '''

    def test_case1(self):
        self.assertEqual(
            test016(3, 17),
            -14,
        )

    def test_case2(self):
        self.assertEqual(
            test016(19, 17),
            4,
        )
