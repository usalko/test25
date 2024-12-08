from unittest import TestCase

from basic1 import test116


class TestsBasic1Test116(TestCase):
    '''
    Write a Python program to print Unicode characters.
    '''

    def test_case1(self):
        self.assertEqual(
            test116(),
            None,
        )
