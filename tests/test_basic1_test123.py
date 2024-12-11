from unittest import TestCase

from basic1 import test123


class TestsBasic1Test123(TestCase):
    '''
    Write a Python program to determine the largest and smallest integers, longs, and floats.
    '''

    def test_case1(self):
        self.assertEqual(
            test123(),
            None,
        )
