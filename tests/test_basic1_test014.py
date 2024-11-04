from unittest import TestCase
from basic1 import test014
from datetime import datetime


class TestsBasic1Test014(TestCase):
    '''
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
    '''

    def test_case1(self):
        self.assertEqual(
            test014((2014, 7, 2), (2014, 7, 11)),
            '9 days',
        )