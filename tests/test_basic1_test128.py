from unittest import TestCase

from basic1 import test128


class TestsBasic1Test128(TestCase):
    '''
    Write a Python program to check whether lowercase letters exist in a string.
    '''

    def test_case1(self):
        self.assertEqual(
            test128(),
            None,
        )
