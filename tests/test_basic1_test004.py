from unittest import TestCase
from basic1 import test004
from datetime import datetime


class TestsBasic1Test004(TestCase):
    '''
    Write a Python program that calculates the area of a circle based on the radius entered by the user.
    Sample Output :
    r = 1.1
    Area = 3.8013271108436504
    '''

    def test_case1(self):
        self.assertEqual(
            test004(1.1),
            '''
r = 1.1
Area = 3.8013271108436504
'''
        )