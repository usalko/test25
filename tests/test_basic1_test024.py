from unittest import TestCase
from basic1 import test024
from datetime import datetime


class TestsBasic1Test024(TestCase):
    '''
    Write a Python program to test whether a passed letter is a vowel or not.
    '''

    def test_case1(self):
        self.assertEqual(
            test024('a'),
            True,
        )

    def test_case2(self):
        self.assertEqual(
            test024('b'),
            False,
        )
