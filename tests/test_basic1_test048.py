from unittest import TestCase

from basic1 import test048


class TestsBasic1Test048(TestCase):
    '''
    Write a Python program to parse a string to float or integer.
    '''

    def test_case1(self):
        self.assertEqual(
            test048('1'),
            1,
        )

    def test_case2(self):
        self.assertEqual(
            test048('2.0'),
            2.0,
        )

