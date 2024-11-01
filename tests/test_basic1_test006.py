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
        self.assertTrue(
            test006(tested_date_time).startswith(f'{current_year:04d}-{current_month:02d}-{current_day:02d} {current_hours:02d}:{current_minutes:02d}:{current_seconds:02d}')
        )