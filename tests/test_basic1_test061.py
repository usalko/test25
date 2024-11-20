from unittest import TestCase

from basic1 import test061


class TestsBasic1Test061(TestCase):
    '''
    Write a Python program to convert the distance (in feet) to inches, yards, and miles.
    '''

    def test_case1(self):
        self.assertEqual(
            test061(),
            None,
        )
