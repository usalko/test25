from unittest import TestCase

from basic1 import test068


class TestsBasic1Test068(TestCase):
    '''
    Write a Python program to calculate sum of digits of a number.
    '''

    def test_case1(self):
        self.assertEqual(
            test068(123),
            6,
        )
