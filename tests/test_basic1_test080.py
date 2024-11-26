from unittest import TestCase

from basic1 import test080


class TestsBasic1Test080(TestCase):
    '''
    Write a Python program to get the current value of the recursion limit.
    '''

    def test_case1(self):
        self.assertEqual(
            test080(),
            None,
        )
