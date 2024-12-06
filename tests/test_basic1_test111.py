from unittest import TestCase

from basic1 import test111


class TestsBasic1Test111(TestCase):
    '''
    Write a Python program to make file lists from the current directory using a wildcard.
    '''

    def test_case1(self):
        self.assertEqual(
            test111(),
            None,
        )
