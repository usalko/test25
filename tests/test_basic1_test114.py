from unittest import TestCase

from basic1 import test114


class TestsBasic1Test114(TestCase):
    '''
    Write a Python program to filter positive numbers from a list.
    '''

    def test_case1(self):
        self.assertListEqual(
            test114([1, -1, -2 , 3, 6, -12, 20]),
            [1, 3, 6, 20],
        )
