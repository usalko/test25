from unittest import TestCase
from basic1 import test005
from datetime import datetime


class TestsBasic1Test005(TestCase):
    '''
    Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
    '''

    def test_case1(self):
        self.assertTrue(
            test005(tested_date_time).startswith(f'{current_year:04d}-{current_month:02d}-{current_day:02d} {current_hours:02d}:{current_minutes:02d}:{current_seconds:02d}')
        )