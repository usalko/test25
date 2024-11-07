from unittest import TestCase
from basic1 import test022
from datetime import datetime


class TestsBasic1Test022(TestCase):
    '''
    Write a Python program to count the number 4 in a given list.
    '''

    def test_case1(self):
        self.assertEqual(
            test022([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 
            1,
        )

    def test_case2(self):
        self.assertEqual(
            test022([4, 4], 4), 
            2,
        )

    def test_case3(self):
        self.assertEqual(
            test022([1, 2], 4), 
            0,
        )