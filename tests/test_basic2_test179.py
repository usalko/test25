from unittest import TestCase

from basic2 import test179


class TestsBasic1Test179(TestCase):
    '''29. Common Divisors Finder

    Write a Python program to find common divisors between two numbers in a given pair.
    '''

    def test_case1(self):
        self.assertListEqual(
            test179(2),
            0,
        )
