from unittest import TestCase

from basic1 import test120


class TestsBasic1Test120(TestCase):
    '''
    Write a Python program to format a specified string and limit the length of a string.
    '''

    def test_case1(self):
        self.assertEqual(
            test120(),
            None,
        )
