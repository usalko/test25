from unittest import TestCase

from basic1 import test083


class TestsBasic1Test083(TestCase):
    '''
    Write a Python program to test whether all numbers in a list are greater than a certain number.
    '''

    def test_case1(self):
        self.assertEqual(
            test083(),
            None,
        )
