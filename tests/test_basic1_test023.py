from unittest import TestCase
from basic1 import test023
from datetime import datetime


class TestsBasic1Test023(TestCase):
    '''
    Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
    Return n copies of the whole string if the length is less than 2.
    '''

    def test_case1(self):
        self.assertEqual(
            test023('', 3),
            '',
        )

    def test_case2(self):
        self.assertEqual(
            test023('1', 3),
            '111',
        )

    def test_case3(self):
        self.assertEqual(
            test023('123', 6),
            '121212121212',
        )