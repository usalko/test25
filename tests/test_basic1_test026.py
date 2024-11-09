from unittest import TestCase
from basic1 import test026
from datetime import datetime


class TestsBasic1Test026(TestCase):
    '''
    Write a Python program to create a histogram from a given list of integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test026([1, 2, 1, 3]),
            '''*
**
*
***
'''
        )