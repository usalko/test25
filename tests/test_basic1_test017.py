from unittest import TestCase
from basic1 import test017
from datetime import datetime


class TestsBasic1Test017(TestCase):
    '''
    Write a Python program to test whether a number is within 100 of 1000 or 2000.
    '''

    def test_case1(self):
        self.assertEqual(
            test017(17),
            False,
        )

    def test_case2(self):
        self.assertEqual(
            test017(1017),
            True,
        )

    def test_case3(self):
        self.assertEqual(
            test017(2017),
            True,
        )

    def test_case4(self):
        self.assertEqual(
            test017(2217),
            False,
        )

    def test_case5(self):
        self.assertEqual(
            test017(1217),
            False,
        )

    def test_case6(self):
        self.assertEqual(
            test017(1999),
            True,
        )
