from unittest import TestCase

from basic1 import test093


class TestsBasic1Test093(TestCase):
    '''
    Write a Python program to swap two variables.
    '''

    def test_case1(self):
        self.assertEqual(
            test093(),
            None,
        )
