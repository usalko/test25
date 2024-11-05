from unittest import TestCase
from basic1 import test015
from datetime import datetime


class TestsBasic1Test015(TestCase):
    '''
    Write a Python program to calculate the difference between a given number and 17.
    If the number is greater than 17, return twice the absolute difference.
    '''

    def test_case1(self):
        self.assertEqual(
            test015(6),
            904.7786842338603,
        )