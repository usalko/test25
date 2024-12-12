from unittest import TestCase

from basic1 import test129


class TestsBasic1Test129(TestCase):
    '''
    Write a Python program to add leading zeroes to a string.
    '''

    def test_case1(self):
        self.assertEqual(
            test129(),
            None,
        )
