from unittest import TestCase

from basic1 import test055


class TestsBasic1Test055(TestCase):
    '''
    Write a Python program to find local IP addresses using Python's stdlib.
    '''

    def test_case1(self):
        self.assertTrue(
           [x for x in test055() if x.startswith('127.0.')]
        )
