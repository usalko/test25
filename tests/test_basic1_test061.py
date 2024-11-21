from unittest import TestCase

from basic1 import test061


class TestsBasic1Test061(TestCase):
    '''
    Write a Python program to convert the distance (in feet) to inches, yards, and miles.
    '''

    def test_case1(self):
        self.assertEqual(
            test061(2000),
            (24, 666, 0),
        )

    def test_case2(self):
        self.assertEqual(
            test061(10000),
            (12, 1573, 1),
        )
