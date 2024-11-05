from unittest import TestCase
from basic1 import test015
from datetime import datetime


class TestsBasic1Test015(TestCase):
    '''
    Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
    '''

    def test_case1(self):
        self.assertEqual(
            test015(6),
            904.7786842338603,
        )