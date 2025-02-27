from unittest import TestCase
from basic1 import test021
from datetime import datetime


class TestsBasic1Test021(TestCase):
    '''
    Write a Python program that determines whether a given number (accepted from the user)
    is even or odd, and prints an appropriate message to the user.
    '''

    def test_case1(self):
        self.assertEqual(
            test021(3),
            '3 is odd number',
        )

    def test_case2(self):
        self.assertEqual(
            test021(2),
            '2 is even number',
        )
