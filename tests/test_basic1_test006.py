from unittest import TestCase
from basic1 import test006
from datetime import datetime


class TestsBasic1Test006(TestCase):
    '''
    Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
    '''

    def test_case1(self):
        ll, tt = test006('3, 5, 7, 23')
        self.assertListEqual(
            ll,
            ['3', ' 5', ' 7', ' 23'],
        )
        self.assertTupleEqual(
            tt,
            ('3', ' 5', ' 7', ' 23'),
        )