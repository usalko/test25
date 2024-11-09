from unittest import TestCase
from basic1 import test027
from datetime import datetime


class TestsBasic1Test027(TestCase):
    '''
    Write a Python program that concatenates all elements in a list into a string and returns it.
    '''

    def test_case1(self):
        self.assertEqual(
            test027(['7', '5', '3', '1', '5', '9']),
            '753159',
        )