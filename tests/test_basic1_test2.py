from unittest import TestCase
from basic1 import test2


class TestsBasic1Test2(TestCase):
    '''
    Write a Python program to find out what version of Python you are using.
    '''

    def test_case1(self):
        self.assertTrue(
            test2().startswith('3.13')
        )