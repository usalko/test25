from unittest import TestCase

from basic1 import test146


class TestsBasic1Test146(TestCase):
    '''
    Write a Python program to find the location of Python module sources.
    '''

    def test_case1(self):
        self.assertEqual(
            test146(),
            None,
        )
