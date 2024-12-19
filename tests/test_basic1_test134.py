from unittest import TestCase

from basic1 import test134


class TestsBasic1Test134(TestCase):
    '''
    Write a Python program to input two integers on a single line.
    '''

    def test_case1(self):
        self.assertEqual(
            test134(),
            None,
        )
