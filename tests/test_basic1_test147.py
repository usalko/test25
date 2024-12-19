from unittest import TestCase

from basic1 import test147


class TestsBasic1Test147(TestCase):
    '''
    Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
    '''

    def test_case1(self):
        self.assertEqual(
            test147(),
            None,
        )
