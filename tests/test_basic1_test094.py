from unittest import TestCase

from basic1 import test094


class TestsBasic1Test094(TestCase):
    '''
    Write a Python program to convert the bytes in a given string to a list of integers.
    '''

    def test_case1(self):
        self.assertListEqual(
            test094('0123456789'),
            [48, 49, 50, 51, 52, 53, 54, 55, 56, 57],
        )
