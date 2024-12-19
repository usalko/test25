from unittest import TestCase

from basic1 import test150


class TestsBasic1Test150(TestCase):
    '''
    Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.
    '''

    def test_case1(self):
        self.assertEqual(
            test150(),
            None,
        )
