from unittest import TestCase

from basic1 import test115


class TestsBasic1Test115(TestCase):
    '''
    Write a Python program to compute the product of a list of integers (without using a for loop).
    '''

    def test_case1(self):
        self.assertEqual(
            test115(),
            None,
        )
