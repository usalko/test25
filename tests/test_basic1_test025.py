from unittest import TestCase
from basic1 import test025
from datetime import datetime


class TestsBasic1Test025(TestCase):
    '''
    Write a Python program that checks whether a specified value is contained within a group of values.
    Test Data :
    3 -> [1, 5, 8, 3] : True
    -1 -> [1, 5, 8, 3] : False
    '''

    def test_case1(self):
        self.assertEqual(
            test025([1, 5, 8, 3], 3),
            True,
        )

    def test_case1(self):
        self.assertEqual(
            test025([1, 5, 8, 3], -1),
            False,
        )