from unittest import TestCase

from basic1 import test095


class TestsBasic1Test095(TestCase):
    '''
    Write a Python program to check whether a string is numeric.
    '''

    def test_case1(self):
        self.assertTupleEqual(
            test095(),
            None,
        )
