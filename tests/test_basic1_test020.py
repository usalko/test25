from unittest import TestCase
from basic1 import test020
from datetime import datetime


class TestsBasic1Test020(TestCase):
    '''
    Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
    '''

    def test_case1(self):
        self.assertEqual(
            test020('clone', 3),
            'clonecloneclone',
        )
