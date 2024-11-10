from unittest import TestCase

from basic1 import test032


class TestsBasic1Test032(TestCase):
    '''
    Write a Python program to find the least common multiple (LCM) of two positive integers.
    '''

    def test_case1(self):
        self.assertEqual(
            test032(3, 9),
            9,
        )

    def test_case2(self):
        self.assertEqual(
            test032(6, 12),
            12,
        )