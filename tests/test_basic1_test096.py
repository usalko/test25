from unittest import TestCase

from basic1 import test096


class TestsBasic1Test096(TestCase):
    '''
    Write a Python program to print the current call stack.
    '''

    def test_case1(self):
        self.assertTrue(
            'test096' in test096(),
        )
