from unittest import TestCase

from basic1 import test127


class TestsBasic1Test127(TestCase):
    '''
    Write a Python program to check whether an integer fits in 64 bits.
    '''

    def test_case1(self):
        self.assertEqual(
            test127(),
            None,
        )
