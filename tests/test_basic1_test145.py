from unittest import TestCase

from basic1 import test145


class TestsBasic1Test145(TestCase):
    '''
    Write a Python program to test if a variable is a list, tuple, or set.
    '''

    def test_case1(self):
        self.assertEqual(
            test145(),
            None,
        )
