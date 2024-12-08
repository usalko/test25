from unittest import TestCase

from basic1 import test117


class TestsBasic1Test117(TestCase):
    '''
    Write a Python program to prove that two string variables of the same value point to the same memory location.
    '''

    def test_case1(self):
        self.assertEqual(
            test117(),
            None,
        )
