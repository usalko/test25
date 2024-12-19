from unittest import TestCase

from basic1 import test135


class TestsBasic1Test135(TestCase):
    '''
    Write a Python program to print a variable without spaces between values.
    Sample value : x =30
    Expected output : Value of x is "30"
    '''

    def test_case1(self):
        self.assertEqual(
            test135(),
            None,
        )
