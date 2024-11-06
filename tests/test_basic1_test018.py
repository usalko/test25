from unittest import TestCase
from basic1 import test018
from datetime import datetime


class TestsBasic1Test018(TestCase):
    '''
    Write a Python program to calculate the sum of three given numbers.
    If the values are equal, return three times their sum.
    '''

    def test_case1(self):
        self.assertEqual(
            test018(1, 2, 3),
            6,
        )

    def test_case2(self):
        self.assertEqual(
            test018(3, 3, 3),
            27,
        )

    def test_case3(self):
        self.assertEqual(
            test018(2, 3, 3),
            8,
        )

    def test_case4(self):
        self.assertEqual(
            test018(2, 2, 3),
            7,
        )
