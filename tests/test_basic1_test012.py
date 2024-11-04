from unittest import TestCase
from basic1 import test012
from datetime import datetime


class TestsBasic1Test012(TestCase):
    '''
    Write a Python program that prints the calendar for a given month and year.
    Note : Use 'calendar' module.
    '''

    def test_case1(self):
        self.assertEqual(
            test012(11, 2024),
            '''   November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
'''
        )