from unittest import TestCase

from basic1 import test059


class TestsBasic1Test059(TestCase):
    '''
    Write a Python program to convert height (in feet and inches) to centimeters.
    '''

    def test_case1(self):
        self.assertEqual(
            test059(12, 2),
            370.84,
        )
