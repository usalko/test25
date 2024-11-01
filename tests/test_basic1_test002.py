from unittest import TestCase
from basic1 import test002


class TestsBasic1Test002(TestCase):
    '''
    Write a Python program to find out what version of Python you are using.
    '''

    def test_case1(self):
        self.assertTrue(
            test002().startswith('3.13')
        )