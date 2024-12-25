from unittest import TestCase

from basic2 import test162


class TestsBasic1Test162(TestCase):
    '''12. List Permutations Generator

    Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.
    '''

    def test_case1(self):
        self.assertEqual(
            test162(),
            None,
        )
