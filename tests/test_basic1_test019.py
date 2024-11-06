from unittest import TestCase
from basic1 import test019
from datetime import datetime


class TestsBasic1Test019(TestCase):
    '''
    Write a Python program to get a newly-generated string from a given string
    where "Is" has been added to the front. Return the string unchanged
    if the given string already begins with "Is".
    '''

    def test_case1(self):
        self.assertEqual(
            test019('Is it a code?'),
            'Is it a code?',
        )

    def test_case2(self):
        self.assertEqual(
            test019('long'),
            'Islong',
        )
