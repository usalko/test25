from unittest import TestCase

from basic2 import test174


class TestsBasic1Test174(TestCase):
    '''24. Even or Odd Divisors

    Write a Python program to find the total number of even or odd divisors of a given integer.
    '''

    def test_case1(self):
        self.assertListEqual(
            test174(2),
            0,
        )
