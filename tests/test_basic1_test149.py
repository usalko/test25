from unittest import TestCase

from basic1 import test149


class TestsBasic1Test149(TestCase):
    '''
    Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.
    '''

    def test_case1(self):
        self.assertEqual(
            test149(),
            None,
        )
