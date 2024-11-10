from unittest import TestCase

from basic1 import test031


class TestsBasic1Test031(TestCase):
    '''
    Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test031(3, 9),
            3,
        )

    def test_case2(self):
        self.assertEqual(
            test031(17, 15),
            1,
        )