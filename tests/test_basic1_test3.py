from unittest import TestCase
from basic1 import test3
from datetime import datetime


class TestsBasic1Test3(TestCase):
    '''
    Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
    '''

    def test_case1(self):
        tested_date_time = datetime.now()
        current_year = tested_date_time.year
        current_month = tested_date_time.month
        current_day = tested_date_time.day
        current_hours = tested_date_time.hour
        current_minutes = tested_date_time.minute
        current_seconds = tested_date_time.second
        self.assertTrue(
            test3(tested_date_time).startswith(f'{current_year:04d}-{current_month:02d}-{current_day:02d} {current_hours:02d}:{current_minutes:02d}:{current_seconds:02d}')
        )