from unittest import TestCase

from basic1 import test039


class TestsBasic1Test039(TestCase):
    '''
    Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
    '''

    def test_case1(self):
        self.assertEqual(
            test039(),
            None,
        )

