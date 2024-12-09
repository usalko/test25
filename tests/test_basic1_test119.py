from unittest import TestCase

from basic1 import test119


class TestsBasic1Test119(TestCase):
    '''
    Write a Python program to round a floating-point number to a specified number of decimal places.
    '''

    def test_case1(self):
        self.assertEqual(
            test119(),
            None,
        )
