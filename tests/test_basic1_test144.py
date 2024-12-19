from unittest import TestCase

from basic1 import test144


class TestsBasic1Test144(TestCase):
    '''
    Write a Python program to check whether a variable is an integer or string.
    '''

    def test_case1(self):
        self.assertEqual(
            test144(),
            None,
        )
