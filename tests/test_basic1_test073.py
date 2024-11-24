from unittest import TestCase

from basic1 import test073


class TestsBasic1Test073(TestCase):
    '''
    Write a Python program to calculate the midpoints of a line.
    '''

    def test_case1(self):
        self.assertEqual(
            test073(),
            None,
        )
